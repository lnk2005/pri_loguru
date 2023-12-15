# pri_loguru

私有自用的loguru日志模块封装，临时性提供直接存储日志到 es 中

测试版，暂时未考虑进入生产环境，比如
- 不支持控制 logger level
- logger 的配置有点抽象

## 版本发布方式
1. 修改版本号 `poetry version --next-phase`
   1. `--next-phase` 参见 [poetry version](https://python-poetry.org/docs/cli/#version)
2. 打包 并 上传 `poetry publish [-r testpypi] --build`
