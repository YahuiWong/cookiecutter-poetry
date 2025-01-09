from {{cookiecutter.project_slug}}.settings import Settings


def test_init():
    Settings.init("app.test.yaml")
    assert Settings.debug()==True
    assert Settings.monitoring() == False
    pass