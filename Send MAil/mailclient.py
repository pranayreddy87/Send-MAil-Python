#-------------------------------------------------------------------------------
# Name:        mailclient
# Purpose:
#
# Author:      peddireddy
#
# Created:     30/06/2015
# Copyright:   (c) peddireddy 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# turn on the "https://www.google.com/settings/security/lesssecureapps" before running
import socket
import base64
import email.utils

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

recipient = "<krishnakanth933@gmail.com>"
sender = "<python.assign.3@gmail.com>"
username = "python.assign.3@gmail.com"
password = 'Python123'

# Choose a mail server  and call it mailserver, i am using gmail

mailserver = 'smtp.gmail.com'
port = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket.socket()
clientSocket.connect((mailserver, port))
recv = clientSocket.recv(1024)
print 'test'
print 'reply received from -- '+recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO \r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print 'reply received from -- '+recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Request an encrypted connection
startTlsCommand = 'STARTTLS\r\n'
clientSocket.send(startTlsCommand)
tls_recv = clientSocket.recv(1024)
print 'reply received from -- '+tls_recv
if tls_recv[:3] != '220':
	print '220 reply not received from server'

# Encrypt the socket
ssl_clientSocket = socket.ssl(clientSocket)

# Send the AUTH LOGIN command and print server response.
authCommand = 'AUTH LOGIN\r\n'
ssl_clientSocket.write(authCommand)
auth_recv = ssl_clientSocket.read(2048)
print 'reply received from -- '+auth_recv
if auth_recv[:3] != '334':
	print '334 reply not received from server'

# Send username and print server response.
uname = base64.b64encode(username) + '\r\n'
ssl_clientSocket.write(uname)
uname_recv = ssl_clientSocket.read(1024)
print 'reply received from -- '+uname_recv
if uname_recv[:3] != '334':
	print '334 reply not received from server'

# Send password and print server response.
pword = base64.b64encode(password) + '\r\n'
ssl_clientSocket.write(pword)
pword_recv = ssl_clientSocket.read(1024)
print 'reply received from -- '+pword_recv
if pword_recv[:3] != '235':
	print '235 reply not received from server'

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: ' + sender + '\r\n'
ssl_clientSocket.write(mailFromCommand)
recv2 = ssl_clientSocket.read(1024)
print 'sending email from '+ sender +'\n\n'
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: ' + recipient + '\r\n'
ssl_clientSocket.write(rcptToCommand)
recv3 = ssl_clientSocket.read(1024)
print 'sending email to '+ recipient +'\n\n'
print recv3
if recv3[:3] != '250':
	print '250 reply not received from server.'

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
ssl_clientSocket.write(dataCommand)
recv4 = ssl_clientSocket.read(2048)
print 'reply received from -- '+ recv4
if recv4[:3] != '354':
	print '354 reply not received from server.'

# Send message data.
ssl_clientSocket.write(msg)

# Message ends with a single period.
ssl_clientSocket.write(endmsg)
recv5 = ssl_clientSocket.read(1024)
print recv5
if recv5[:3] != '250':
	print '250 reply not received from server.'

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
ssl_clientSocket.write(quitCommand)
recv6 = ssl_clientSocket.read(1024)
print 'email sent to '+recipient
print 'reply received from -- '+ recv6
if recv6[:3] != '221':
	print '\n 221 reply not received from server.'
clientSocket.close()
