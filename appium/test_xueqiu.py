from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class Test_xueqiu:
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 系统名称
    # desired_caps['platformVersion'] = '4.4.2'  # 系统的版本号
    desired_caps['deviceName'] = '127.0.0.1:7555'  # 设备名称，这里是虚拟机，这个没有严格的规定
    desired_caps['appPackage'] = 'com.xueqiu.android'  # APP包名
    desired_caps['appActivity'] = '.common.MainActivity'  # APP入口的activity
    desired_caps['noReset'] = 'true'

    def setup(self):
        # # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_xueqiu(self):
        # element1 = self.driver.find_element(By.ID, 'com.xueqiu.android:id/home_search')
        # element1.click()
        # element2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # element2.send_keys("alibaba")
        # element3 = self.driver.find_element(By.XPATH, "//*[@text='阿里巴巴']")
        # element3.click()
        # element4 = self.driver.find_element(By.XPATH, "//*[@text='阿里巴巴']/../..//*[@text='加自选']")
        # element4.click()

        element1 = self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/home_search')
        element1.click()
        element2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        element2.send_keys("alibaba")
        element3 = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']")
        element3.click()
        try:
            element4 = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']/../..//*[@text='加自选']")
            element4.click()
            text1=self.driver.find_element(MobileBy.XPATH,"//*[@text='阿里巴巴']/../..//*[@resource-id='com.xueqiu.android:id/followed_btn']").get_attribute('text')
            assert  text1 == '已添加'
            print(text1)
        except:
            print('元素未找到，加自选失败,执行取消自选操作')
            # 取消自选操作
            element5 = self.driver.find_element(MobileBy.XPATH,"//*[@text='阿里巴巴']/../..//*[@text='已添加']")
            element5.click()
            # text2=self.driver.find_element(MobileBy.XPATH,"//*[@text='阿里巴巴']/../..//*[@resource-id='com.xueqiu.android:id/followed_btn']").get_attribute('text')
            # assert  text2 == '加自选'
            # print(text2)