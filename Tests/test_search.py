from Pages.Homepage import Homepage
from Utils import util
import time
import pytest

@pytest.mark.usefixtures('Browser_setup')
class TestSEARCH():
    def test_flightsearch(self):
        driver=self.driver
        home=Homepage(driver)
        home.Select_Flight()
        home.Retrive_All_Flights()
        home.Retrive_NonStop_Flights()
        home.Retrive_OneStop_Flights()
        home.Select_Departure_Flight()
        home.Select_Return_Flight()
        home.Caculate_and_Compare()