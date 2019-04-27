from Pages.Homepage import Homepage
import pytest


#@pytest.mark.dependency(depends=['a'])
@pytest.mark.usefixtures('Browser_setup')
class TestSEARCH():
    def test_flightsearch(self):

        global driver, home
        driver = self.driver
        home = Homepage(driver)
        home.Select_Flight()
        home.Retrive_All_Flights()
        driver.implicitly_wait(30)

    def test_Nonstop_and_OneStop_Flights(self):
        home.Retrive_NonStop_Flights()
        home.Retrive_OneStop_Flights()

    def test_Select_Flights(self):
        home.Select_Departure_Flight()
        home.Select_Return_Flight()
        home.Caculate_and_Compare()
