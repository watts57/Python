# -*- coding: utf-8 -*-
# My Name:  Will Watts  My Partner:  John Bedingfield



import socket
import time
import sys
import pprint

try:
    import ssl
except ImportError:
    print('import error')
    pass
else:
    print('')

# set up initial variables:
# HOST = 'localhost'  # mine works either way, but I read some reports that the IP works better
HOST = '127.0.0.1'
# HOST = '::1'
PORT = 3310
PORTSSL = 27994

studentID = 'bedingjd'
messageToSend = 7  # per the instructions, this needs to be a num such that


#                       5 < num < 10, although other numbers work with the Robot

def connect_unencrypted(HOST, PORT):
    # define a socket and connect
    print('2. Attempting to connect to s (Port ' + str(PORT) + ')')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))

    # pass BlazerID
    print('connected, passing BlazerID')
    studentIDBytes = str.encode(studentID)  # need to convert to bytes, since sendall requires bytes
    s.sendall(studentIDBytes)  # sending StudentID
    print('   sent: ' + str(studentIDBytes))

    # receive a new port number
    newPort = s.recv(4096)  # also tried 1024, amount of bytes
    print()
    print("3. Received New Port: " + str(newPort))

    s.close()
    print('  closed s on port: ' + str(PORT))
    print()

    NPJTI4 = newPort.decode()  # this converts from bytes to String
    NPJTI4Int = int(NPJTI4)  # recast as an int
    print('3b. Attempting to connect to s_2 on Port: ' + str(NPJTI4Int))
    s_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_2.bind((HOST, NPJTI4Int))
    # s_2.connect((HOST, NPJTI4Int))
    s_2.listen(1)

    conn, addr = s_2.accept()
    print('   conn: ' + str(conn) + ' | addr ' + str(addr))
    # print status
    print('Server from ' + str(addr[0]) + ' at port ' + str(addr[1]) + ' connected')

    # receive the ffffff,eeeeee tuple (UDP port info)
    print()
    print('4. Receiving ffffff,eeeee')
    ffffff_TupleByte = conn.recv(4096)
    print('   ', end='')
    print(ffffff_TupleByte)
    ffffff_TupleString = str(ffffff_TupleByte)
    # print(ffffff_TupleString)
    ffffff = int(ffffff_TupleString[2:7])
    eeeeee = int(ffffff_TupleString[8:13])
    print('     f: ' + str(ffffff) + ' e: ' + str(eeeeee))

    s_2.close()
    print('   closed s_2 on port ' + str(NPJTI4Int))
    print()

    connect_UDP(HOST, ffffff, eeeeee)

    return


def connect_encrypted(HOST, PORTSSL):
    # good resource: https://docs.python.org/2/library/ssl.html

    print('2. Attempting to connect to s encrypted via Port ' + str(PORTSSL))
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='mysite.local')
    conn.connect((HOST, PORTSSL))  # this begins the SSL handshake

    # get cert
    cert = conn.getpeercert()
    # print cert for testing purposes
    print()
    print('Received the following cert:')
    pprint.pprint(cert)

    # send the message
    print()
    print('connected, passing BlazerID')
    studentIDBytes = str.encode(studentID)  # need to convert to bytes, since sendall requires bytes
    conn.sendall(studentIDBytes)  # sending StudentID
    print('   sent: ' + str(studentIDBytes))

    # time.sleep(3)

    # receive a new port number
    newPort = conn.recv(4096)  # also tried 1024, amount of bytes
    print()
    print("3. Received New Port: " + str(newPort))

    conn.close()
    print()
    print('  closed s on port: ' + str(PORTSSL))
    print()

    NPJTI4 = newPort.decode()  # this converts from bytes to String
    NPJTI4Int = int(NPJTI4)  # recast as an int
    print('3b. Attempting to connect to s_2 on encrypted Port: ' + str(NPJTI4Int))
    context2 = ssl.create_default_context()
    conn2 = context2.wrap_socket(socket.socket(socket.AF_INET), server_hostname='mysite.local')
    conn2.connect((HOST, NPJTI4Int))

    # get cert
    cert2 = conn2.getpeercert()
    # print cert for testing purposes
    print()
    print('Received the following cert:')
    pprint.pprint(cert2)

    # receive the ffffff,eeeeee tuple (UDP port info)
    print()
    print('4. Receiving ffffff,eeeee')
    ffffff_TupleByte = conn2.recv(4096)
    print('   ', end='')
    print(ffffff_TupleByte)
    ffffff_TupleString = str(ffffff_TupleByte)
    # print(ffffff_TupleString)
    ffffff = int(ffffff_TupleString[2:7])
    eeeeee = int(ffffff_TupleString[8:13])
    print('     f: ' + str(ffffff) + ' e: ' + str(eeeeee))

    conn2.close()
    print('   closed port ' + str(NPJTI4Int))
    print()

    connect_UDP(HOST, ffffff, eeeeee)

    return


def connect_UDP(HOST, RobotPort, ClientPort):
    # setting up the variables
    ffffff = RobotPort
    eeeeee = ClientPort
    expectedAnswer = messageToSend * 10
    messageToSendInBytes = str.encode(str(messageToSend))

    # make the UDP socket connection
    print('4b. Attempting to create a UDP connection, and pass x')
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP: DGRAM

    # the UDP way to send data:
    time.sleep(3)  # may not be necessary
    s3.sendto(messageToSendInBytes, (HOST, ffffff))
    print('   sent message x = ' + str(messageToSend) + ' on port ffffff (' + str(ffffff) + ') : ')
    print('   ', end='')
    print(messageToSendInBytes)

    # set up a new socket to receive num*10
    s3b = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s3b.bind((HOST, eeeeee))
    x, addr3b = s3b.recvfrom(4096)
    print('======= Received from port eeeeee (' + str(eeeeee) + ') xxx: ')
    print(x)
    xString = x.decode()
    xInt = int(x)

    print('4c. Received num*10, xxx= ' + str(len(x)))
    if expectedAnswer == len(x):
        print('   This matched the expected value: ' + str(expectedAnswer))
    else:
        print('   This did NOT match the expected value: ' + str(expectedAnswer))
    # s3b.close()

    print()
    print('5. Sending back string xxx on port ffffff (' + str(ffffff) + ')')

    # form message in bytes to send back, and send it 5 times, one second apart
    messageToSendInBytes2b = str.encode(xString)
    for i in range(0, 5):
        s3.sendto(messageToSendInBytes2b, (HOST, ffffff))
        print('UDP packet ' + str(i + 1) + ' sent')
        time.sleep(1)  # wait one second

    # clean up the resources (not sure this is completely necessary with UDP,
    #     but it makes me feel happy)
    s3.close()
    s3b.close()
    print('   closed s3 on port: ' + str(ffffff))
    print('   closed s3b on port: ' + str(eeeeee))
    return


# =======  main =======
# check command line for appropriate arguments
if (len(sys.argv) > 1) and (sys.argv[1] == "-s"):
    # execute SSL code
    # sslS = ssl.wrap_socket(s)
    print('Passed argument: ', end='')
    print(sys.argv[1])
    print()
    connect_encrypted(HOST, PORTSSL)
else:
    print('Passed no arguments, connecting unencrypted')
    print()
    # define a socket and connect
    connect_unencrypted(HOST, PORT)

print('Done!')





