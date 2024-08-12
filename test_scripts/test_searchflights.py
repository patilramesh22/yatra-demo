import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup","log_on_failure")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    @data(*Utils.get_data_from_csv("data/testdata.csv"))
    @unpack
    def test_search_flights(self,deptfrom,goingto,date,stop):
        search_flight_result = self.lp.search_flights(deptfrom,goingto,date)
        search_flight_result.filter_by_stop(stop)
        self.lp.page_scroll()
        all_stops = search_flight_result.get_search_flights_results()
        self.log.info(len(all_stops))
        self.ut.assert_list_item_text(all_stops,stop)
