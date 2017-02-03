#-*- coding: utf-8 -*-

def mainmenu(conn,sock):

	def decorator_menu(func):
		"""Декоратор, выводит текст и принимает ответы в консоли, затем вызывает функцию и передаёт ей параметр Param"""
		def wrapper_menu(TextToShow,TextToConfirm,conn,sock,Param=""):
			conn.send(TextToShow.encode('cp866'))
			tmp=""
			TextConf = " "
			while "\n" not in tmp:
				data = conn.recv(1024)
				tmp = data.decode('cp866')
				Param = Param + tmp
			tmp=""

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
				func(TextToShow,TextToConfirm,conn,sock,Param)

		return wrapper_menu

	"""Описание функций обработки меню"""
	@decorator_menu
	def first_choise(TextToShow,TextToConfirm,conn,sock,Param=""):
		print("wrapper works, give ip, gived Param: "  + Param)

	@decorator_menu
	def second_choise(TextToShow,TextToConfirm,conn,sock,Param=""):
		print("wrapper works,find user, gived Param: "  + Param)

	tmp = ''
	ans = 0

	MenuList = ['1. Выделить ip\r\n','2. Найти пользователя\r\n','3. Удалить пользователя\r\n', '4. Удалить ПК\r\n','5. Выход\r\n','Введите число: ']
	
	for i in MenuList:
		conn.send(i.encode('cp866'))

	while "\rn" not in tmp:
		data = conn.recv(1024)
		tmp = data.decode('cp866')

		try:
			ans = int(tmp)

			if ans==5:
				break
				conn.close()

			if ans==1:
				# GiveIp(conn,sock)
				first_choise("\r\nКому выделить новый ip?: \r\n","Вы уверены[y/n]: ", conn,sock)

			if ans==2:
				# GiveIp(conn,sock)
				second_choise("\r\nВведите ФИО кого надо найти: \r\n","Вы уверены[y/n]: ", conn,sock)

		except ValueError:
			tmp = "Ошибка. Введите число: \r\n"
			conn.send(tmp.encode('cp866'))

	print(UnPass)

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
	mainmenu(conn,sock)
	print(UnPass)
else:
	conn.close()

