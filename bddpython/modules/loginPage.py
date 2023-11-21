from selenium import webdriver
from page_objects import PageObject, PageElement


class loginPage(PageObject):
    txt_email = PageElement(id_='login_email')
    txt_password = PageElement(css='input[title$=password')
    btn_login = PageElement(class_name='button[id*=btnLogin')
    msg_alerta = PageElement(id='.alert-login')

    def logar(self, email, password):
        self.txt_email.send_keys(email)
        self.txt_password.send_keys(password)
        self.btn_login.click()


#browser = webdriver.Chrome()

#g = Google(browser, 'http://google.com/')
#g.search('live de python')
# g.lucky('live de python')
# g.search_bar.send_keys('live de python')
# # g.btn_search.click()
# g.btn_lucky.click()