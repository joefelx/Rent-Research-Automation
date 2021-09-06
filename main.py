from selenium import webdriver
import time


PATH = "C:\Development\chromedriver.exe"


class RentResearch:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D")
        self.rents = []
        self.addresses = []
        self.links = []

    def getinfo(self):
        rentlist = self.driver.find_elements_by_class_name("list-card-price")
        for prices in rentlist:
            rent = prices.text
            self.rents.append(int(rent.split("/")[0].split("$")[1].replace(",", "")))

        addresslist = self.driver.find_elements_by_class_name("list-card-addr")
        for address in addresslist:
            self.addresses.append(address.text)

        linklist = self.driver.find_elements_by_css_selector(".list-card-info a")
        for link in linklist:
            self.links.append(link.get_attribute('href'))

    def writeform(self):
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfMuXB24uGbgMtyJ-45-3rw-OO7GfY-cb_TQwPXbFPomPjf6g/viewform?pli=1&pli=1")
        time.sleep(5)
        for i in range(len(self.rents)):
            addressfield = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
            addressfield.send_keys(self.addresses[i])
            rentfield = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            rentfield.send_keys(self.rents[i])
            linkfield = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            linkfield.send_keys(self.links[i])
            self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
            time.sleep(5)
            self.driver.find_element_by_link_text("Submit another response").click()
            time.sleep(5)

        self.driver.quit()


research = RentResearch(path=PATH)
research.getinfo()
research.writeform()


