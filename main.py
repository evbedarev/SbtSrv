#-*- coding: utf-8 -*-

def mainmenu(conn,sock):
	tmp = ''
	ans = 0
	MenuList = ['1. Выделить ip\r\n','2. Найти пользователя\r\n','3. Удалить пользователя\r\n', '4. Удалить ПК\r\n','5. Выход\r\n']
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
				GiveIp(conn,sock)

		except ValueError:
			tmp = "Ошибка. Введите число: \r\n"
			conn.send(tmp.encode('cp866'))

	print(UnPass)

def GiveIp(conn,sock):
	Fio = "Введите ФИО: \r\n"
	tmp = ""
	conn.send(Fio.encode('cp866'))
	Fio = ""
	while "\n" not in tmp:
		data = conn.recv(1024)
		tmp = data.decode('cp866')
		Fio = Fio + tmp

	print(Fio)

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

