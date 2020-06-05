class app:
    def start(self):
        if self.driver=None:
            caps={}
            caps['platformName']="android"
            caps['deviceName']="127.0.0.1:7555"
            caps['appPackage']="com.tencent.wework"
            caps['appActivity']=".contact.controller.ContactDetailBriefInfoProfileActivity"
            caps['noReset']=True


