import unittest
import os
from selenium import webdriver
from classes.tests import TestLogin, TestNota

path = os.getcwd()
url = "http://localhost:8080"

#Necessário colocar na pasta o arquivo chromedriver.exe com a mesma versão do Chrome instalado.
#Endereço: https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(executable_path=r"%s/chromedriver.exe" % path) 

if __name__ == '__main__':
    TestLogin.driver = driver
    TestLogin.url = url+"/#/"

    TestNota.driver = driver
    TestNota.url = url+"/#/sistema"

    unittest.main(exit=False)
    driver.quit()