
def decorator_menu(func):
	"""Декоратор, выводит текст и принимает ответы в консоли, затем вызывает функцию и передаёт ей параметр Param.
	TextToShow - список который будет отображаться на экране
	confirm - логическое значение, будет ли выводиться подтверждение
	TextToConfirm - текст который выводится при подтверждении
	Param - Параметр который передается декорируемой функции"""
	def wrapper_menu(self,TextToShow,confirm,TextToConfirm,conn,sock,Param=""):
		
		conn.send(TextToShow.encode('cp866'))

		tmp=""
		TextConf = " "

		while "\n" not in tmp:
			data = conn.recv(1024)
			tmp = data.decode('cp866')
			Param = Param + tmp

		tmp=""
		
		"""Выбор, выдавать предупреждение или нет.
		Если параметр confirm=True то будет выдаваться предупреждение и если введен ответ 'y' то будет
		запускаться функция. Иначе будет запускаться функция без предупреждения"""

		if confirm:
			conn.send(TextToConfirm.encode('cp866'))

			while TextConf[0]!= "y":
				TextConf=""
				
				while "\n" not in tmp:
					data = conn.recv(1024)
					tmp = data.decode('cp866')
					TextConf = TextConf +tmp

				if TextConf[0]=="n":
					conn.send(TextToShow.encode('cp866'))
					break

			if TextConf[0]=="y":
				return func(self,TextToShow,confirm,TextToConfirm,conn,sock,Param)
		else:
			return func(self,TextToShow,confirm,TextToConfirm,conn,sock,Param)

	return wrapper_menu


class Menu:
	def __init__(self,conn,sock):
		"""Зацикливаем меню пока не будет выбран 5й пункт"""
		while self.mainMenu('\r\n 1. Выделить ip\r\n 2. Найти пользователя\r\n 3. Удалить пользователя\r\n 4. Удалить ПК\r\n 5. Выход\r\n Введите число: ',False,"qwe",conn,sock," ") !=5:
			pass

	@decorator_menu
	def mainMenu(self,TextToShow,confirm,TextToConfirm,conn,sock,Param=""):
		ans = 0
		try:
			ans = int(Param)

			if ans==5:
				conn.close()

			if ans==1:
				# GiveIp(conn,sock)
				self.firstChoise("\r\nКому выделить новый ip?: \r\n",True,"Вы уверены[y/n]: ", conn,sock)

			if ans==2:
				# GiveIp(conn,sock)
				self.secondChoise("\r\nВведите ФИО кого надо найти: \r\n",True,"Вы уверены[y/n]: ", conn,sock)

		except ValueError:
			tmp = "Ошибка. Введите число: \r\n"
			conn.send(tmp.encode('cp866'))

		return ans

	@decorator_menu
	def firstChoise(self,TextToShow,confirm,TextToConfirm,conn,sock,Param=""):
		print("wrapper works, give ip, gived Param: "  + Param)

	@decorator_menu
	def secondChoise(self,TextToShow,confirm,TextToConfirm,conn,sock,Param=""):
		print("wrapper works,find user, gived Param: "  + Param)

"""start program"""

import socket

sock = socket.socket()
sock.bind(('',9090))
sock.listen(1)
conn, addr = sock.accept()
print ('connected:',addr)

a = ''
s = "Pw: "
conn.send(s.encode('utf-8'))
UnPass=[]



while "\n" not in a:
	data = conn.recv(1024)
	a = a + data.decode('cp866')
	if "\n" in a:
		UnPass.append(a.rstrip())

if UnPass[0]=="админ":
	print("All ok!!!")
	s = "All ok!!! "
	s = Menu(conn,sock)
	print(UnPass)
else:
	conn.close()
