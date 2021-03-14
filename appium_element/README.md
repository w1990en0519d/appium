# 测试用例重要组成部分

* 导入依赖的webdirver
  * ``from appium import webdirver``
* capabilities设置
* 初始化driver
  * ``dirver = webdirve.remote``
* 隐式等待，增强用例的稳定性
* 元素的定位与操作
  * find + action
* 断言 assert

# capabilities设置

* 获取appPackage包名和appActivity的名字
  * 打开cmd，连接上手机
  * 输入以下命令：
    * adb logcat ActivityManager:I | findstr "cmp"
  * 打开手机操作的app就可以获取cmp，/前面部分是appPackage包名，/后面部分是appActivity的名字，.不能省略
* automationName（工作引擎）默认使用uiautomator2(andorid默认使用默认使用uiautomator2，IOS默认使用XCUITest)
  * 一般是不用设置的
* noReset和fullReset 是否在测试前后重置相关环境（例如首次打开弹窗，或者是登录信息）
  * noReset-Ture：不重置app的状态，fullReset-Ture：重置app的状态，保持一个干净的app
  * 演示雪球的首次启动弹窗功能，noReset-Ture和fullReset-Ture使用情况
* unicodeKeyBoard和resetKeyBoard是否需要输入非英文之外的语言并在测试完成后重置输入法
  * 举例输入中文，alibab，阿里巴巴
* [官方文档](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md)
* dontStopAppOnReset首次启动的时候，不停止app（可以在调试或者运行的时候提升运行速度）
* skipDeviceInitialization跳过安装，权限设置等操作（可以调试或者运行的时候提升运行速度）

# appium元素定位

常用的两种定位方式id，accessibility_id driver.find_element_by_id(rescource-id)
driver.find_elements_by_accessibility_id(content-desc)

# 三种经典等待方式

* 强制等待：
  * sleep() 不推荐
* 隐式等待（全局性）
  * 设置一个超时时间，服务器appium会在给定的时间内，不停的查找，默认值是0，每0.5秒查找一次
  * 用法:driver.implicitly_wait()
* 显示等待（等待某个元素）
  * 针对某个元素的用显示等待，该等待方式只作用于一个元素
  * 用法：WebDriverWait(driver,10,0.5).until()
  * 在客户端等待


