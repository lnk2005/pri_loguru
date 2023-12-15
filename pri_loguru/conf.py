from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import List


class HandlerConfig(ABC):
    pass


@dataclass
class EsHandlersConfig(HandlerConfig, ABC):
    use_https: bool

    host: str | List[str]
    author: str
    passwd: str

    cert_path: str
    verify_certs: bool

    index: str = f'simple_log_{datetime.now().strftime("%Y%m%d")}'
    queue_size: int = 1  # 一次性提交的日志条数
