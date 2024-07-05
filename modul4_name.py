def test_function():
    def inner_function():
        return print('Я в области видимости функции test_function')

    inner_function()
    return print('Тестирую область видимости')

test_function()
# inner_function()