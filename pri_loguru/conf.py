from abc import ABC
from dataclasses import dataclass
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
