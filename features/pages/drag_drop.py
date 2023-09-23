
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Browser import Browser

ObjectToDrag="draggable"
ObjectToDrap="droppable"
class dragdrop(Browser):

    def drag(self):
        element = self.driver.find_element(By.ID, ObjectToDrag)
        target = self.driver.find_element(By.ID, ObjectToDrap)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    def verify(self):
        target = self.driver.find_element(By.ID, "droppable")
        return(target)

    def slider(self):
        slider = self.driver.find_element(By.XPATH, '/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]')
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop_by_offset(slider, 280, 16).perform()

    def verifyslider(self):
        success_message = self.driver.find_element(By.ID, "range").text
        assert "100" == success_message


