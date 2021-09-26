from .base import Base

class Login(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_id = self.locators['username_input']['id']
        self.password_xpath = self.locators['password_input']['xpath']
        self.login_button = self.locators['login_button']['xpath']

    def do_login(self, username, password):
        self.fill_form('id', self.username_id, username)
        self.fill_form('xpath', self.password_xpath, password)
        self.click('xpath', self.login_button)

        #Validation
        assert self.driver.current_url == 'https://expert.chegg.com/expertqna'
