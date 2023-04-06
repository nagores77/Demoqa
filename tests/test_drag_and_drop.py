from pages.droppable import DroppAble
from selenium.webdriver import ActionChains
import allure
import time


def test_drug_and_drop(browser):

    drag_drop = DroppAble(browser)
    drag_drop.visit()
    action_chains = ActionChains(browser)
    #assert not drag_drop.drag.check_css('backgroundColor', '#000000')
    action_chains.drag_and_drop(
        drag_drop.drag.find_element(),  #element
        drag_drop.drop.find_element()).perform()  # target
    time.sleep(1)
    assert drag_drop.drop.check_css('backgroundColor', '#4682B4')
    # Method grab 'element' at center and move it to 'target'
    # element to grab, then target where to drop

    action_chains.drag_and_drop(drag_drop.drop.find_element(), drag_drop.drag.find_element()).perform()
    assert drag_drop.drop.check_css('backgroundColor', '#4682B4')

    #action_chains.drag_and_drop_by_offset(drag_drop.drop, )
