from appium import webdriver
from selenium.webdriver.common.by import By


class Testworkwechat:
    caps = {}
    caps['platformName'] = "android"
    caps['deviceName'] = "127.0.0.1:7555"
    caps['appPackage'] = "com.tencent.wework"
    caps['appActivity'] = ".launch.WwMainActivity"
    caps['noReset'] = 'true'

    def setup(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.caps)
        # self.resolve_windows()
        self.driver.implicitly_wait(5)

        # 启动app,第一个参数是包名，第二个参数是activity
        # self.driver.start_activity('com.tencent.wework','.launch.WwMainActivity')

    def teardown(self):
        self.driver.quit()

    def test_workwehcat(self):
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.tencent.wework:id/drb'and@text='通讯录']").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/h1x']//*[@text='添加成员']").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/c7t']//*[@text='手动输入添加']").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/au7'and@text='必填']").send_keys('test1')

    def resolve_windows(self):
        """权限处理弹窗"""
        try:
            els = self.driver.find_elements_by_class_name('android.widget.Button')
            while True:
                for el in els:
                    if el.text == u'允许':
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("允许")').click()
                    elif el.text == u'始终允许':
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
                    elif el.text == u'确定':
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
        except:
            print('未检测到弹窗')
