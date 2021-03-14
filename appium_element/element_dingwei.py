import time

from appium import webdriver


class TestElementDingwei:

    def setup(self):
        desired_caps = {}
        # 启动的系统
        desired_caps['platformName'] = 'Android'
        # 系统的版本
        desired_caps['platformVersion'] = '6.0'
        # 启动的手机名
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # 启动app包名
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # 启动appActivity
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        # 不重置app缓存信息
        desired_caps['noReset'] = 'true'
        # 重置app，删除app的缓存数据，打开一个干净的app
        # desired_caps['fullReset'] = 'true'
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 关闭app
        self.driver.quit()

    def test_element_dingwei(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        # 强制等待
        time.sleep(3)
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        self.driver.find_element_by_xpath('//*[@text="BABA"]').click()
