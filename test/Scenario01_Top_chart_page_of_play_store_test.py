from selenium import webdriver
from seleniumdriver import Driver
from pages.playstorepage import PlayStorePage
from datetime import date


class TestStart():

        base_url = "https://play.google.com/store/apps/top"
        driver = Driver()
        driver.navigate(base_url)
        playstorepage=PlayStorePage(driver)
        nameList=playstorepage.play_store_page_item_list()
        today=date.today()

        for appname in nameList:
                # method to fetch all applications name
                playstorepage.perform_click_on_item(appname)
                reviews=playstorepage.total_reviews(appname)
                lastupdate=playstorepage.last_update(appname)
                playstorepage.calculate_score(today,reviews,lastupdate)

                playstorepage.top_chart_click()




