from selenium import webdriver
from datetime import date
import time

class PlayStorePage():

    def __init__(self,driver):
        self.driver=driver

        self.play_store_page_items_name="(//div[@class='ZmHEEd  fLyRuc'])//div[@class='WsMG1c nnK0zc']"
        self.play_store_app_name_xpath="//div[contains(text(),'{}')]"
        self.play_store_reviews_xpath= "//h1//span[text()='{}']//following::span[@class='AYi5wd TBRnV']/span[contains(@aria-label,'ratings')]"
        self.play_store_last_update_xpath="//h1//span[text()='{}']/following::div[@class='BgcNfc' and text()='Updated']//following-sibling::span//div//span"
        self.play_store_top_charts_click_xpath="//*[text()='Top charts']"

        # method to fetch all applications names
    def play_store_page_item_list(self):
        try:
            time.sleep(5)
            store_page = self.driver.getelements(self.play_store_page_items_name)
            itemlist=[]
            for i in range(len(store_page)):
                if(store_page[i].text != ''):
                    itemlist.append(store_page[i].text)
            print("Applications Name : ",itemlist)
            return itemlist
        except :
            print("menu page not launched")
            raise

    # method to click on app
    def perform_click_on_item(self,nameList):
        try:
            time.sleep(3)
            element = self.driver.getelement(self.play_store_app_name_xpath.format(nameList))
            self.driver.elementClick(element)
            print("Click Performed on : ",nameList)

        except BaseException as e:
            print(e)
            raise

    # method to fetch app reviews
    def total_reviews(self,appname):
        try:
            time.sleep(3)
            reviews = self.driver.getelement(self.play_store_reviews_xpath.format(appname))
            print("Number of Reviews : ", reviews.text)
            return reviews.text
        except BaseException as e:
            print("Review element not found : ",(str(e.args)))
            return False

    # method to fetch app last Update
    def last_update(self,appname):
        try:
            time.sleep(3)
            updatexpath = self.driver.getelement(self.play_store_last_update_xpath.format(appname))
            print("Last Update : ", updatexpath.text)
            return updatexpath.text
        except BaseException as e:
            print("Update element not found : ",(str(e.args)))
            return False

    # method to click on Top Chart
    def top_chart_click(self):
        try:
            #time.sleep(2)
            #self.driver.waitforelement(self.play_store_top_charts_click_xpath)
            topchartxpath = self.driver.getelement(self.play_store_top_charts_click_xpath)
            self.driver.elementClick(topchartxpath)
            topchartxpath = self.driver.getelement(self.play_store_top_charts_click_xpath)
            print("Clicked On : ", topchartxpath.text)

        except BaseException as e:
            print("Not Clicked on Top : ",str(e.args))
            raise

    def calculate_score(self,today,reviews,lastupdate):
        print(date(lastupdate))
        #delta=today-lastdate
        # print("Number of days : ",delta.days)





