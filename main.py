#-*- coding: utf-8 -*-

def mainmenu(conn,sock):
	tmp = ''
	MenuList = ['1. Выделить ip\r\n','2. Найти пользователя\r\n','3. Удалить пользователя\r\n', '4. Удалить ПК\r\n','5. Выход\r\n']
	for i in MenuList:
		conn.send(i.encode('cp866'))

	while "\n" not in tmp:
		data = conn.recv(1024)
		tmp = data.decode('cp866')
		if tmp=="5":
			break
			conn.close()
			
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

