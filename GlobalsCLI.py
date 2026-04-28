def GlobalsCLI() -> None:
	print('GlobalsCLI - MichiTheCat (c)')
	while True:
		user = input('\n> ').strip()
		if user[0:2] == 'ls':
			try:
				path = user[3:].split('/')
				if path == ['']:
					print((str(globals().keys())[11:-2]).split('\''))
				else:
					print(path)
			except:
				print('"ls" вызван неправильно!')
		elif user == '':
			pass
		else:
			print(f'"{user}" не является встроенной командой!')


if __name__ == '__main__':
	ReadMe = 'Добро пожаловать в GlobalsCLI!'
	GlobalsCLI()
