import logging.config

from poetrymytemplete.settings import Settings
def test_init_logger():
    Settings.init("app.test.yaml")
    assert Settings.debug()==True
    assert Settings.monitoring() == False

    logging.config.dictConfig(config=Settings.get('logger'))
    # 获取根记录器：配置信息从yaml文件中获取
    root = logging.getLogger()
    # 子记录器的名字与配置文件中loggers字段内的保持一致
    my_module = logging.getLogger("my_module")
    print("rootlogger:", root.handlers)
    print("selflogger", my_module.handlers)
    # print("子记录器与根记录器的handler是否相同：", root.handlers[0] == my_module.handlers[0])
    my_module.error("DUBUG")
    root.info("INFO")
    root.error('ERROR')
    root.debug("rootDEBUG")
    pass
