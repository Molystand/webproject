from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class MyTestCase(TestCase):
    username = 'test_username'
    email = 'test_email@mail.com'
    password = 'anypass12345'

    admin_name = 'molystand'
    admin_pass = 'password'

    sleep_time = 1

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(MyTestCase, self).setUp()

    def tearDown(self):
        self.selenium.find_element_by_name('user_logout').click()

        self.selenium.quit()
        super(MyTestCase, self).tearDown()

    def test001_register_and_login(self):
        sel = self.selenium
        sel.get('http://mydigitalnews.ru')
        sel.find_element_by_name('user_register').click()
        sel.find_element_by_name('username').send_keys(self.username)
        sel.find_element_by_name('email').send_keys(self.email)
        sel.find_element_by_name('password1').send_keys(self.password)
        sel.find_element_by_name('password2').send_keys(self.password)
        sel.find_element_by_name('register').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)
        self.assertEqual(sel.title, 'Вход - mydigitalnews', 'Пользователь не зарегистрирован')

        # sel.find_element_by_name('user_login').click()
        sel.find_element_by_name('username').send_keys(self.username)
        sel.find_element_by_name('password').send_keys(self.password)
        sel.find_element_by_name('login').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)
        self.assertEqual(sel.title, 'Все статьи - mydigitalnews', 'Вход не выполнен')

    def test002_create_tag(self):
        sel = self.selenium
        sel.get('http://mydigitalnews.ru')
        sel.find_element_by_name('user_login').click()
        sel.find_element_by_name('username').send_keys('user123')
        sel.find_element_by_name('password').send_keys('anypass12345')
        sel.find_element_by_name('login').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)
        self.assertEqual(sel.title, 'Все статьи - mydigitalnews', 'Вход не выполнен')

        sel.find_element_by_name('panel-create-tag').click()
        time.sleep(self.sleep_time)
        self.assertEqual(sel.title, 'Создание тега - mydigitalnews', 'Тег не может быть создан данным пользователем')

        sel.find_element_by_name('title').send_keys('aaa')
        sel.find_element_by_name('slug').send_keys('test-tag')
        sel.find_element_by_name('create-tag').click()
        time.sleep(self.sleep_time)
        self.assertIn('Новости по тегу ', sel.find_element_by_tag_name('h2').text,
                            'Тег не создан. Возможно, неверно указаны данные в форме')

    def test003_create_news(self):
        sel = self.selenium
        sel.get('http://mydigitalnews.ru')
        sel.find_element_by_name('user_login').click()
        sel.find_element_by_name('username').send_keys(self.admin_name)
        sel.find_element_by_name('password').send_keys(self.admin_pass)
        sel.find_element_by_name('login').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)
        self.assertEqual(sel.title, 'Все статьи - mydigitalnews', 'Вход не выполнен')

        sel.find_element_by_name('panel-create-news').click()
        time.sleep(self.sleep_time)
        self.assertEqual(sel.title, 'Создание новости - mydigitalnews', 'Новость не может быть создана данным пользователем')

        sel.find_element_by_name('title').send_keys('Заголовок')
        sel.find_element_by_name('text_preview').send_keys('Превью')
        sel.find_element_by_name('text').send_keys('Текст новости')
        sel.find_element_by_name('create-news').click()
        time.sleep(self.sleep_time)
        self.assertEqual('Оставить комментарий', sel.find_element_by_tag_name('button').text,
                      'Новость не создана. Возможно, неверно указаны данные в форме')

    def test004_update_tag(self):
        sel = self.selenium
        sel.get('http://mydigitalnews.ru')
        sel.find_element_by_name('user_login').click()
        sel.find_element_by_name('username').send_keys(self.admin_name)
        sel.find_element_by_name('password').send_keys(self.admin_pass)
        sel.find_element_by_name('login').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)

        sel.find_element_by_link_text('Теги').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_class_name('badge').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_name('panel-update').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_name('title').clear()
        sel.find_element_by_name('title').send_keys('aa')
        sel.find_element_by_name('slug').send_keys('qwe')
        sel.find_element_by_tag_name('button').click()
        time.sleep(self.sleep_time)
        self.assertIn('Новости по тегу ', sel.find_element_by_tag_name('h2').text,
                      'Тег не создан. Возможно, неверно указаны данные в форме')

    def test005_update_news(self):
        sel = self.selenium
        sel.get('http://mydigitalnews.ru')
        sel.find_element_by_name('user_login').click()
        sel.find_element_by_name('username').send_keys(self.admin_name)
        sel.find_element_by_name('password').send_keys(self.admin_pass)
        sel.find_element_by_name('login').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)

        sel.find_element_by_link_text('Далее').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_name('panel-update').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_name('title').send_keys('1')
        sel.find_element_by_tag_name('button').click()
        time.sleep(self.sleep_time)
        self.assertEqual('Оставить комментарий', sel.find_element_by_tag_name('button').text,
                         'Новость не создана. Возможно, неверно указаны данные в форме')

    def test006_create_comment(self):
        sel = self.selenium
        sel.get('http://mydigitalnews.ru')
        sel.find_element_by_name('user_login').click()
        sel.find_element_by_name('username').send_keys('user_not_editor')
        sel.find_element_by_name('password').send_keys('anypass12345')
        sel.find_element_by_name('login').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)

        sel.find_element_by_link_text('Далее').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_name('text').send_keys('Тестовый комментарий')
        sel.find_element_by_tag_name('button').click()
        time.sleep(self.sleep_time)
        self.assertEqual(sel.find_element_by_name('text').text, '')

    def test007_delete_tag(self):
        sel = self.selenium
        sel.get('http://mydigitalnews.ru')
        sel.find_element_by_name('user_login').click()
        sel.find_element_by_name('username').send_keys(self.admin_name)
        sel.find_element_by_name('password').send_keys(self.admin_pass)
        sel.find_element_by_name('login').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)

        sel.find_element_by_link_text('Теги').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_class_name('badge').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_name('panel-delete').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_name('delete-tag').click()
        time.sleep(self.sleep_time)
        self.assertEqual(sel.title, 'Список тегов - mydigitalnews', 'При удалении тега что-то пошло не так')

    def test008_delete_tag(self):
        sel = self.selenium
        sel.get('http://mydigitalnews.ru')
        sel.find_element_by_name('user_login').click()
        sel.find_element_by_name('username').send_keys(self.admin_name)
        sel.find_element_by_name('password').send_keys(self.admin_pass)
        sel.find_element_by_name('login').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)

        sel.find_element_by_link_text('Далее').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_name('panel-delete').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_name('delete-news').click()
        time.sleep(self.sleep_time)
        self.assertEqual(sel.title, 'Все статьи - mydigitalnews', 'При удалении новости что-то пошло не так')

    def test009_delete_user(self):
        sel = self.selenium
        sel.get('http://mydigitalnews.ru/admin')
        # sel.find_element_by_name('user_login').click()
        sel.find_element_by_name('username').send_keys(self.admin_name)
        sel.find_element_by_name('password').send_keys(self.admin_pass)
        sel.find_element_by_css_selector('div.submit-row > input[type="submit"').send_keys(Keys.RETURN)
        time.sleep(self.sleep_time)

        sel.find_element_by_link_text('Пользователи').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_link_text(self.username).click()
        time.sleep(self.sleep_time)
        sel.find_element_by_class_name('deletelink').click()
        time.sleep(self.sleep_time)
        sel.find_element_by_css_selector('input[type="submit"]').click()
        time.sleep(self.sleep_time)

        self.assertIn('был успешно удален.', sel.find_element_by_css_selector('ul.messagelist > li.success').text,
                      'Пользователь не был удалён')
        sel.get('http://mydigitalnews.ru')
        time.sleep(self.sleep_time)
