from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
class yt_vedio():
    def web_driver_chrome(self):
            options = webdriver.ChromeOptions()
            options.add_argument("--verbose")
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument("--window-size=1920, 1200")
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=options)
            return driver 
    def web_driver_firefox(self):
            options = webdriver.FirefoxOptions()
            options.add_argument("--verbose")
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument("--window-size=1920, 1200")
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Firefox(options=options)
            return driver
    def yt_vedios_data(self, url,browser='Chrome',abort=bool):
        if browser=='Chrome' or browser=='chrome':
            driver = self.web_driver_chrome()
            self.url = url
            try:
                driver.get(self.url)
                prev_h = 0
                videos = driver.find_elements(By.XPATH, '//*[@id="contents"]')
                counter=0
                while True:
                    counter=counter+1
                    height = driver.execute_script('''
                        return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );''')
                    driver.execute_script(f"window.scrollTo({prev_h},{prev_h+2000})")
                    time.sleep(3)
                    prev_h += driver.execute_script('return window.innerHeight;')
                    if prev_h >= height:
                        break
                    if abort==True:
                        if counter>=15:
                            abortinput=input("Do you want to abort? press [y] for yes. ")
                            if abortinput=="y" or abortinput=="Y":
                                break
                            else:
                                counter=0
                videos = driver.find_elements(By.XPATH, '//*[@id="contents"]')
                title = list()
                views = list()
                when = list()
                for vedio in videos:
                    title.append(vedio.find_element(By.ID, 'video-title').text)
                    views.append(vedio.find_element(
                        By.XPATH, './/*[@id="metadata-line"]/span[1]').text)
                    when .append(vedio.find_element(
                        By.XPATH, './/*[@id="metadata-line"]/span[2]').text)
                    

                list_of_dic = {'title': title, 'views': views, 'when': when}
                
                driver.quit()
                return list_of_dic
            except:
                driver.quit()
                logging.error("Invalid url")
        else:
            driver =self.web_driver_firefox()
            self.url = url
            try:
                driver.get(self.url)
                prev_h = 0
                counter=0
                while True:
                    counter+=counter
                    height = driver.execute_script('''
                        return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );''')
                    driver.execute_script(f"window.scrollTo({prev_h},{prev_h+2000})")
                    time.sleep(3)
                    prev_h += driver.execute_script('return window.innerHeight;')
                    if prev_h >= height:
                        break
                    if abort==True:
                        if counter>=15:
                            abortinput=input("Do you want to stop? press [y] for yes. ")
                            if abortinput=="y" or abortinput=="Y":
                                break
                            else:
                                counter=0
                videos = driver.find_elements(By.XPATH, '//*[@id="contents"]')
                title = list()
                views = list()
                when = list()
                for vedio in videos:
                    title.append(vedio.find_element(By.ID, 'video-title').text)
                    views.append(vedio.find_element(
                        By.XPATH, './/*[@id="metadata-line"]/span[1]').text)
                    when .append(vedio.find_element(
                        By.XPATH, './/*[@id="metadata-line"]/span[2]').text)
                list_of_dic = {'title': title, 'views': views, 'when': when}
                
                driver.quit()
                return list_of_dic
            except:
                driver.quit()
                logging.error("Invalid url")
    def yt_vedio_comment(self,url,browser='Chrome'):
        if browser=='Chrome' or browser=='chrome':
            try:
                driver =self.web_driver_chrome()
                self.url = url
                driver.get(url)
                time.sleep(5)
                prev_h = 0
                while True:
                    #Returns the page length dynamically
                    height = driver.execute_script('''
                            return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );
                        ''')
                    driver.execute_script(f"window.scrollTo({prev_h},{prev_h+2000})")
                    time.sleep(3)
                    prev_h += driver.execute_script('return window.innerHeight;')
                    if prev_h >= height:
                        break
                comments_text = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
                # print(elements)
                txt=list()
                for element in comments_text:
                    txt.append(element.text)
                comment_likes=driver.find_elements(By.XPATH,'//*[@id="vote-count-middle"]')
                likes=list()
                for element in comment_likes:
                    likes.append(element.text)
                time_posted=list()
                comment_time=driver.find_elements(By.XPATH,'//*[@id="header-author"]/yt-formatted-string/a')
                for element in comment_time:
                    time_posted.append(element.text)
                dic={'comment_text':txt,'likes':likes,'comment_time':time_posted}
                driver.quit()
                return dic

            except:
                driver.quit()
                logging.error('Invalid url')
        else: 
            driver =self.web_driver_firefox()
            self.url = url
            try:
                driver.get(url)
                time.sleep(5)
                prev_h = 0
                while True:
                    #Returns the page lenght dynamically
                    height = driver.execute_script('''
                            return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                        );
                        ''')
                    driver.execute_script(f"window.scrollTo({prev_h},{prev_h+2000})")
                    time.sleep(3)
                    prev_h += driver.execute_script('return window.innerHeight;')
                    if prev_h >= height:
                        break
                comments_text = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
                # print(elements)
                txt=list()
                for element in comments_text:
                    txt.append(element.text)
                comment_likes=driver.find_elements(By.XPATH,'//*[@id="vote-count-middle"]')
                likes=list()
                for element in comment_likes:
                    likes.append(element.text)
                time_posted=list()
                comment_time=driver.find_elements(By.XPATH,'//*[@id="header-author"]/yt-formatted-string/a')
                for element in comment_time:
                    time_posted.append(element.text)
                dic={'comment_text':txt,'likes':likes,'comment_posting_time':time_posted}
                
                driver.quit()
                return dic

            except:
                driver.quit()
                logging.error('Invalid url')
    def yt_vedio_links(self,url):
        try:
            driver =self.web_driver_chrome()
            self.url = url
            driver.get(url)
            time.sleep(5)
            prev_h = 0
            prev_h = driver.execute_script("return document.documentElement.scrollHeight;")
            while True:
                # Scrolling to the bottom
                driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                time.sleep(3)

               
                new_height = driver.execute_script("return document.documentElement.scrollHeight;")
                if new_height == prev_h:
                    break
                prev_h = new_height

            
            links = driver.find_elements(By.XPATH, '//*[@id="video-title-link"]')
            vedio_links = [link.get_attribute('href') for link in links]
            return vedio_links
        except:
                driver.quit()
                logging.error('Invalid url')
