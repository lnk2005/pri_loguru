import builtins
import datetime
import logging
import threading

from elasticsearch import Elasticsearch, helpers

from conf import EsHandlersConfig


class EsHandlers(logging.Handler):
    def __init__(self, index: str, queue_size: int = 100, conf: EsHandlersConfig = None):
        logging.Handler.__init__(self)
        self.index = index

        if conf.use_https:
            self.es = Elasticsearch(
                conf.host,
                basic_auth=(conf.author, conf.passwd),
                ca_certs=conf.cert_path,
                verify_certs=conf.verify_certs,
            )
        else:
            self.es = Elasticsearch(
                conf.host,
                basic_auth=(conf.author, conf.passwd),
            )

        self._lock = threading.Lock()
        self._queue_size = queue_size
        self._queue = []

    def emit(self, record):
        """
        将日志提交到 es，没有做索引，没有测试并发
        :param record: 日志记录
        :return:
        """

        rec = record.__dict__
        rec["log_date"] = datetime.datetime.now()
        rec["_index"] = self.index

        for key in rec:
            match type(rec[key]):
                case builtins.tuple:
                    rec[key] = str(rec[key])

        with self._lock:
            self._queue.append(rec)
            if len(self._queue) == self._queue_size:
                res = None
                try:
                    print("一次更新")
                    res = helpers.bulk(self.es, self._queue)
                    self._queue = []
                except Exception as e:
                    print(e)
                finally:
                    print(res)
