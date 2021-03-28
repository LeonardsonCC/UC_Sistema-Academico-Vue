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
        Método executado antes de todos os testes serem iniciados
        '''
        self.driver.get(self.url)
        self.nome = self.driver.find_element_by_id('nome')
        self.nota = self.driver.find_element_by_id('nota')
        self.botao = self.driver.find_element_by_id('adicionar')

    @classmethod
    def tearDown(self):
        self.nome.clear()
        self.nota.clear()

    def test1_add_invalid_grade(self):
        '''
        Testa se o sistema mostra um aviso quando uma nota inválida é submetida
        '''
        pass

    def test2_empty_Data(self):
        '''
        Testa se o sistema mostra um aviso quando o nome do aluno ou a nota estão vazios
        '''
        pass

    def test3_add_grade(self):
        '''
        Testa se o sistema adiciona uma nota e um estudante novo
        '''
        self.nome.send_keys("Estrôncio")
        self.nota.clear()
        self.nota.send_keys("3")
        self.botao.click()

        td_nome = self.driver.find_element_by_css_selector("tr:nth-of-type(1) > td:nth-of-type(1)")
        td_nota = self.driver.find_element_by_css_selector("tr:nth-of-type(1) > td:nth-of-type(2)")

        content_nome = "" if td_nome is None else td_nome.text
        content_nota = "" if td_nota is None else td_nota.text

        self.assertEqual("Estrôncio", content_nome, "Deveria ter adicionado o nome do usuário corretamente!")
        self.assertEqual("3", content_nota, "Deveria ter adicionado a nota do usuário corretamente!")

    def test4_add_another_student(self):
        '''
        Testa se o sistema adiciona um estudante novo com 2 notas
        '''
        self.nome.send_keys("Promécio")
        self.nota.clear()
        self.nota.send_keys("6")
        self.botao.click()

        self.nota.clear()
        self.nota.send_keys("1")
        self.botao.click()

        td_nome = self.driver.find_element_by_css_selector("tr:nth-of-type(2) > td:nth-of-type(1)")
        td_nota = self.driver.find_element_by_css_selector("tr:nth-of-type(2) > td:nth-of-type(2)")

        content_nome = "" if td_nome is None else td_nome.text
        content_nota = "" if td_nota is None else td_nota.text

        self.assertEqual("Promécio", content_nome, "Deveria ter adicionado o nome do usuário corretamente!")
        self.assertEqual("6, 1", content_nota, "Deveria ter adicionado as notas do usuário corretamente!")

    def test5_add_another_grade(self):
        '''
        Testa se o sistema adiciona mais uma nota ao primeiro estudante criado
        '''
        self.nome.send_keys("Estrôncio")
        self.nota.clear()
        self.nota.send_keys("8")
        self.botao.click()

        td_nome = self.driver.find_element_by_css_selector("tr:nth-of-type(1) > td:nth-of-type(1)")
        td_nota = self.driver.find_element_by_css_selector("tr:nth-of-type(1) > td:nth-of-type(2)")

        content_nome = "" if td_nome is None else td_nome.text
        content_nota = "" if td_nota is None else td_nota.text

        self.assertEqual("Estrôncio", content_nome, "Deveria ter adicionado o nome do usuário corretamente!")
        self.assertEqual("3, 8", content_nota, "Deveria ter adicionado a nota do usuário corretamente!")

    def test6_media(self):
        '''
        Testa se o sistema calcula a média corretamente
        '''
        td_media = self.driver.find_element_by_css_selector("tr:nth-of-type(1) > td:nth-of-type(3)")

        content_media = "" if td_media is None else td_media.text

        self.assertEqual("5.5", content_media, "Deveria ter calculado a média corretamente!")
