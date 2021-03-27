import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from time import sleep

class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(self):
        '''
        Método executado antes de cada teste ser iniciado
        '''
        self.driver.get(self.url)
        self.login = self.driver.find_element_by_id('login')
        self.senha = self.driver.find_element_by_id('senha')
        self.botao = self.driver.find_element_by_id('logar')

    def test_invalid(self):
        '''
        Testa se o sistema mostra um aviso ao inserir um login incorreto e se a URL continua a mesma
        '''
        self.login.send_keys("admin")
        self.senha.send_keys("1234")
        self.botao.click()
        message = self.driver.find_elements_by_class_name("uk-notification-message")
        current_url = self.driver.current_url
        if(message):
            message = True
        self.assertTrue(message, "Deveria mostrar um aviso")
        self.assertEqual(self.url, current_url, "Não deveria mudar de URL")

    def test_valid(self):
        '''
        Testa se o sistema muda de página ao inserir um login correto
        '''
        self.login.send_keys("admin")
        self.senha.send_keys("123")
        self.botao.click()
        current_url = self.driver.current_url
        self.assertNotEqual(self.url, current_url, "Deveria mudar de URL!")


class TestNota(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        Método executado antes dos testes serem iniciados
        '''
        self.driver.get(self.url)

    def test_add_invalid(self):
        pass

    def test_add_valid(self):
        pass

    def test_media(self):
        pass