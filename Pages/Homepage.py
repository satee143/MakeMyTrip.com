from Utils import util
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Homepage():

    def __init__(self,driver):
        self.driver=driver
        self.flights_linktext_xpath='//span[text()="Flights"]'
        self.round_radiobutton_xpath='//li[text()="Round Trip"]'
        self.from_textbox_id='fromCity'
        self.to_textbox_id='toCity'
        self.fromdate_calendar_lable_xpath='//span[contains(text(),"DEPARTURE")]'
        self.date_calendar_xpath='//div[@aria-label="'+util.fromdate+'"]'
        self.toddate_calender_label_xpath='//span[contains(text(),"RETURN")]'
        self.todate_xpath='//div[@aria-label="'+util.todate+'"]'
        self.search_button_xpath='//a[text()="Search"]'
        self.Departure_list_xpath='//div[@class="splitVw-sctn pull-left"]//*[@class="fli-list splitVw-listing"]'
        self.Return_list_xpath='//div[@class="splitVw-sctn pull-right"]//*[@class="fli-list splitVw-listing"]'
        self.NonStop_radio_button_xpath='//label[@for="filter_stop0"]'
        self.OneStop_radio_button_xpath='//label[@for="filter_stop1"]'
        self.From_Link_xpath='//div[@class="splitVw-sctn pull-left"]//div[@class="fli-list splitVw-listing"]['+str(util.rand)+']//p[@class="actual-price"]'
        self.Return_Link_xpath='//div[@class="splitVw-sctn pull-right"]//div[@class="fli-list splitVw-listing"]['+str(util.rand1)+']//p[@class="actual-price"]'
        self.ListedOutDeparturePrice_link_xpath='//div[@class="splitVw-footer-left "]//p[@class="actual-price"]'
        self.ListedOutReturnPrice_link_xpath = '//div[@class="splitVw-footer-right "]//p[@class="actual-price"]'
        self.ListedOutTotalPrice_link_xpath = '//span[@class="splitVw-total-fare"]'


    def Select_Flight(self):
        self.driver.find_element_by_xpath(self.flights_linktext_xpath).click()
        self.driver.find_element_by_xpath(self.round_radiobutton_xpath).click()
        self.driver.find_element_by_id(self.from_textbox_id).send_keys(util.FROM)
        self.driver.find_element_by_id(self.to_textbox_id).send_keys(util.TO)
        self.driver.find_element_by_xpath(self.fromdate_calendar_lable_xpath).click()
        self.driver.find_element_by_xpath(self.date_calendar_xpath).click()
        self.driver.find_element_by_xpath(self.toddate_calender_label_xpath).click()
        self.driver.find_element_by_xpath(self.todate_xpath).click()
        self.driver.find_element_by_xpath(self.search_button_xpath).click()


    def Retrive_All_Flights(self):
        for x in range(25):
            self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        Total_Departure_Flights=len(self.driver.find_elements_by_xpath(self.Departure_list_xpath))
        print('Total Departure Flights Are in Round Trip are: ',Total_Departure_Flights)
        Total_Return_Flights=len(self.driver.find_elements_by_xpath(self.Return_list_xpath))
        print('Total Return Flights are in Round Trip are:',Total_Return_Flights)
        print()
        for x in range(40):
            self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)


    def Retrive_NonStop_Flights(self):
        self.driver.find_element_by_xpath(self.NonStop_radio_button_xpath).click()
        Total_Departure_Flights = len(self.driver.find_elements_by_xpath(self.Departure_list_xpath))
        print('Total Departure Flights Are in Round Trip Non Stop Flights are: ', Total_Departure_Flights)
        Total_Return_Flights = len(self.driver.find_elements_by_xpath(self.Return_list_xpath))
        print('Total Return Flights are in Round Trip Non Stop Flights are:', Total_Return_Flights)
        print()


    def Retrive_OneStop_Flights(self):
        self.driver.find_element_by_xpath(self.NonStop_radio_button_xpath).click()
        self.driver.find_element_by_xpath(self.OneStop_radio_button_xpath).click()
        Total_Departure_Flights = len(self.driver.find_elements_by_xpath(self.Departure_list_xpath))
        print('Total Departure Flights Are in Round Trip One Stop Flights are: ', Total_Departure_Flights)
        Total_Return_Flights = len(self.driver.find_elements_by_xpath(self.Return_list_xpath))
        print('Total Return Flights are in Round Trip One Stop Flights are:', Total_Return_Flights)
        print()


    def Select_Departure_Flight(self):
        self.driver.find_element_by_xpath(self.OneStop_radio_button_xpath).click()
        action=ActionChains(self.driver)
        element1=action.move_to_element(self.driver.find_element_by_xpath(self.From_Link_xpath))
        element1.click().perform()
        value=self.driver.find_element_by_xpath(self.From_Link_xpath).text
        #print(value)
        self.value1=int(value[2:].replace(',',''))
        #print(self.value1)
        listoutprice=self.driver.find_element_by_xpath(self.ListedOutDeparturePrice_link_xpath).text
        #print(listoutprice)
        assert value == listoutprice
        print('The Selected Flight UPWARD FARE :',value,'Displayed FARE for UPWARD at bottom is :',listoutprice)
        print('PRICE ARE MATCHED UPWARD DIRECTION')
        print()


    def Select_Return_Flight(self):
        ele=self.driver.find_element_by_xpath(self.Return_Link_xpath)
        self.driver.execute_script("arguments[0].click();",ele)
        value=self.driver.find_element_by_xpath(self.Return_Link_xpath).text
        #print(value)
        self.value2=int(value[2:].replace(',',''))
        #print(self.value2)
        listoutprice2=self.driver.find_element_by_xpath(self.ListedOutReturnPrice_link_xpath).text
        #print(listoutprice2)
        assert value==listoutprice2
        print('The Selected Flight RETURN FARE :',self.value2,'Displayed FARE for RETURN at bottom is :',listoutprice2)
        print('PRICE ARE MATCHED RETURN DIRECTION')
        print()


    def Caculate_and_Compare(self):
        total=self.value1+self.value2
        total_price=self.driver.find_element_by_xpath(self.ListedOutTotalPrice_link_xpath).text
        total_price1 = int(total_price[2:].replace(',', ''))
        #print(total)
        #print(total_price)
        assert total_price1 == total
        print('The Selected UPWARD Flight RETURN Flight Total  FARE :',total,'Displayed Total FARE at bottom is :',total_price1)
        print('The Sum of UP FARE AND RETURN FARE ARE EQUAL TO THE LISTED OUT TOTAL FARE')



