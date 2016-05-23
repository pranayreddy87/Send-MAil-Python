import base64
import socket
import smtplib
msg = '\r\nI love computer networks!\n'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'
mailPort = 587
#recipient = "<pranaydaringtoo@gmail.com>"
#sender = "<peddireddy.pranay@gmail.com>"
username = "peddireddy.pranay@gmail.com"
password = 'Password1991'
# Create socket called clientSocket and establish a TCP connection with mailserver
SMTPClientSocket = socket(AF_INET, SOCK_STREAM)
SMTPClientSocket.connect((mailServer,mailPort))
recv = SMTPClientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'
# Send HELO command and print server response.
heloCommand = 'HELO this is the output\r\n'
SMTPClientSocket.send(heloCommand)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not received from server.'
 # Send username and print server response.
uname = base64.b64encode(username) + '\r\n'
ssl_clientSocket.write(rcptToCommand)
uname_recv = ssl_clientSocket.read(1024)
print uname_recv
if uname_recv[:3] != '334':
	print '334 reply not received from server'

# Send password and print server response.
pword = base64.b64encode(password) + '\r\n'
ssl_clientSocket.write(pword)
pword_recv = ssl_clientSocket.read(1024)
print pword_recv
if pword_recv[:3] != '235':
	print '235 reply not received from server'
# Send MAIL FROM command and print server response.
mailFromCommand = 'Mail From:\r\n'
SMTPClientSocket.send(mailFromCommand)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not recieved from server.'
# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO:<peddireddy.pranay@gmail.com> \r\n'
print rcptToCommand
SMTPClientSocket.send(rcptToCommand)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not recieved from server.'
# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
SMTPClientSocket.send(dataCommand)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '354 Enter mail, end with ?.? on a line by itself.'
# Send message data.
SMTPClientSocket.send(msg)
print 'Message is: ', msg
# Message ends with a single period.
SMTPClientSocket.send(endmsg)
print 'End message is: ', endmsg
#SMTPClientSocket.send(endmsg)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not recieved from server.'
# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
SMTPClientSocket.send(quitCommand)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not recieved from server.'
pass

if __name__ == '__main__':
    main()