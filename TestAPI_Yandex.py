import unittest

from main import creating_folder, checking_folder_creation, DELETE_folder_creation

token = ''

param_list_test_1 = [('Код ответа соответствует 201', 'new_path/')]

param_list_test_2 = [('Результат создания папки - папка появилась в списке файлов', 'new_path/'),
                     ('Ошибка 404', 'old_path/')]

param_list_test_3 = [('Папка удалена', 'new_path/'),
                     ('Ошибка 404', 'old_path/')]


class Test_unit(unittest.TestCase):

    def test_1(self):
        for param_1, param_2 in param_list_test_1:
            self.assertEqual(param_1, creating_folder(token, param_2), 'Вывод не соответствует ожиданию')

    def test_2(self):
        for param_1, param_2 in param_list_test_2:
            self.assertEqual(param_1, checking_folder_creation(token, param_2), 'Вывод не соответствует ожиданию')

    def test_3(self):
        for param_1, param_2 in param_list_test_3:
            self.assertEqual(param_1, DELETE_folder_creation(token, param_2), 'Вывод не соответствует ожиданию')


if __name__ == '__main__':
    unittest.main()