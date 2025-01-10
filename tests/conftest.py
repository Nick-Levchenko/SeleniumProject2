import pytest
from selenium import webdriver


class Driver(webdriver.Chrome):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

#насчет autouse, помню что ты говорил что его не используем, но хоть убей не получается без него
#сделать тест класс, не понимаю почему. Если с ходу можешь сказать в чем ошибка, скажи плз,
#сегодня целый день пытался разными способами передать драйвер туда, но работает только так
#если так сразу сказать не можешь, завтра попробую заново подобный проект сделать , может разберусь
@pytest.fixture(autouse=True)
def driver(request):
    driver = Driver()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
