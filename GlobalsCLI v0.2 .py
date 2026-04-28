if __name__ == '__main__': __name__ = '__debug__' # Для тестов как бы выглядело в виде модуля


# Ниже переменные заданы для примера
if __name__ == '__main__':
	a = 23; Peoples = ['Human1', 'Human2']; Money = {'Деньга один': 100, 'Коэфициент': [50, 39]}
	ReadMe = "Привет, GlobalsCLI!"


# Функции модуля ниже
def _ShowAll() -> None: # показать все переменные
	ActualGlobals = globals() # ибо изменяется размер из-за объявления key
	for key in ActualGlobals:
		print(key)

def _ShowIn(key:str) -> None: # показать данные конкретной переменной
	ActualGlobals = globals()
	print(ActualGlobals[key])


# Проверки всякие ниже
if __name__ == '__main__':
	_ShowAll()
	print()
	_ShowIn('a')
	

# Сама функция модуля
print('Версия кода: v0.2a\nАвтор: MichiTheCat-RedStar')
while True:
	_UserInput = input('\nGlobalsCLI:~$ ').lower().strip()
	if _UserInput == '':
		continue
	elif _UserInput == 'help':
		print('help - помощь\nall - показывает все имена переменных\ntouch - посмотреть содержание конкретной переменной')
	elif _UserInput == 'all':
		_ShowAll()
	elif _UserInput == 'touch':
		_UserInput = input('\nGlobalsCLI/touch:~$ ').strip()
		try:
			_ShowIn(_UserInput)
		except:
			print(f'"{_UserInput}" не найдено!')
	else:
		print(f'"{_UserInput}" не найдено!')
