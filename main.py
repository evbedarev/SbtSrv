#-*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('',9090))
sock.listen(1)
conn, addr = sock.accept()
print ('connected:',addr)

a = ''
s = "Un: "
conn.send(s.encode('utf-8'))
UnPass = []

while "\n" not in a:
	data = conn.recv(1024)
	a = a + data.decode('utf-8')
	if "\n" in a:
		UnPass.append(a.rstrip())

a = ''
s = "Pw: "
conn.send(s.encode('utf-8'))

while "\n" not in a:
	data = conn.recv(1024)
	a = a + data.decode('utf-8')
	if "\n" in a:
		UnPass.append(a.rstrip())

if UnPass[0]=="admin" and UnPass[1]=="Qq123456":
	print("All ok!!!")
	s = "All ok!!! "
	print(UnPass)
else:
	conn.close()

