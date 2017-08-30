#!/usr/bin/python  
#coding=utf-8   
  
''''' 
通过webdriverde 凡是，利用PhantomJS来登录 
电脑上需要安装Selenium 
'''  
  
import time,sys  
from selenium import webdriver  
  
reload(sys)  
sys.setdefaultencoding('utf-8')  
  
#计算时间函数  
def print_run_time(func):  
    def wrapper(self, *args, **kw):  
        local_time = time.time()  
        func(self)  
        print 'run time is {:.2f}'.format(time.time() - local_time)  
    return wrapper  
  
class heibanke:  
    @print_run_time  
    def heibank_ex02(self):  
        testurl="http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/"  
        url='http://www.heibanke.com/lesson/crawler_ex02/'  
        cap = webdriver.DesiredCapabilities.PHANTOMJS  
        driver = webdriver.PhantomJS()  
        driver.get(testurl)  
        driver.find_element_by_name("username").send_keys("test")  
        driver.find_element_by_name("password").send_keys("test123")  
        driver.find_element_by_id("id_submit").click()  
        print driver.find_element_by_tag_name('h3').text  
      
        for i in xrange(31):  
            driver.get(url)  
            #print driver.current_url  
            driver.find_element_by_name("username").send_keys("test")  
            driver.find_element_by_name("password").send_keys(i)  
            driver.find_element_by_id("id_submit").click()  
            print "当前输入的密码是:",i,  
            if "错误" not in driver.find_element_by_tag_name('h3').text:  
                print driver.find_element_by_tag_name('h3').text  
                break  
            print driver.find_element_by_tag_name('h3').text  
        print 'end'  
        driver.quit()  
        return  
  
if __name__ == '__main__':  
    h2=heibanke()  
    h2.heibank_ex02() 