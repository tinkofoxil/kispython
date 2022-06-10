import unittest


def ultimate_answer(question):
        """Выводит на печать переданный аргумент и возвращает строку ответа."""
        print(f'Ваш вопрос: {question}')
        return f'Ответ на ваш вопрос "{question}": 42'


class TestExample(unittest.TestCase):

    def test_case_1(self):
        self.assertIsInstance(ultimate_answer('Что делать?'), str, 'Тест провален')


    def test_case_2(self):
        result = 'Ответ на ваш вопрос "Кем быть?": 42'
        self.assertEqual(ultimate_answer('Кем быть?'), result, 'Тест провален')


    def test_case_3(self):
        self.assertTrue(ultimate_answer('Кто виноват?'), 'Тест провален')


    def test_case_4(self):
        self.assertIsNotNone(ultimate_answer('To be, or not to be?'), 'Тест провален')


    def test_case_5(self):
        self.assertIn('42', ultimate_answer('Who am I?'), 'Тест провален')


if __name__ == '__main__':
    unittest.main()
