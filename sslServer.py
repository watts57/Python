'''

Work in progress. Still trying to find the cleanest way to struccture this.

CONCLUSION> THREADING IS A DEAD END AS FAR AS QUITTING GRACEFULLY GOES. MULTIPROCESSING SEEMS TO BE A SAFER BET
AS FAR AS INCLUDED MODULES GO IN PYTHON. PYTHON BEHAVES DIFFERENTLY THAN JAVA IN THIS REGARD.


==============TO DO: ====================

NOTES: 5:07PM
3/25/20
Multiprocessing module:   ---> as in, you type "import multiprocessing"

With multiprocessing module it
may be possible to do what I've struggled with for 30 hours in 5 minutes using that module.
It's an included Python 3 module that works very similarly to threading.
Threading is supposed to be more ideal for non CPU intensive tasks, while multiprocessing is supposed to be
more ideal for CPU intensive tasks. Since this is fairly lightweight, I suppose we can sacrifice some efficiency for
the sake of sanity.


LAST BIG THING TO TEST:
multiprocessing


Last things:
debug?
clean up print statements if needed (check)
test with client called normally and with -s to make sure all is well
see if client can be cleaned up any




'''

#####################IMPORT MODULES
import sys
import time
import socket
import ssl
import random

IDLE = 1
######################################CRUCIAL VARIABLES###########################################################


# set up initial variables:
# HOST = 'localhost'  # mine works either way, but I read some reports that the IP works better
HOST = '127.0.0.1'
# HOST = '::1'
PORT = 3310
PORTSSL = 27994
TIMER_INIT = 5

STARTED = 0

certLocation = "C:\\Program Files\OpenSSL-Win64\\bin\\public.cer"
keyLocation = "C:\\Program Files\OpenSSL-Win64\\bin\\private.key"


####################################John's sockets######################################
def unecrypted_socket(HOST, PORT):
    '''
    # Creates an unencrypted connection for assignment Paras 2, 3, 4a
    #  Takes a string HOST which is the IPv4 address of the host
    #  Takes an integer PORT which is the inital port for the connection: 3310
    '''

    # set up a socket and listen for connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print('Listening for TCP traffic on port ' + str(PORT))
    print('TCP socket created, ready for listening and accepting connection...')
    print('waiting for connection on port ' + str(PORT))
    print()

    # accept the connection
    conn, addr = s.accept()
    print('   conn: ' + str(conn) + ' | addr ' + str(addr))

    # print status
    print('Client from ' + str(addr[0]) + ' at port ' + str(addr[1]) + ' connected')

    blazerID = conn.recv(4096)
    if len(blazerID) == 8:
        print()
        print('BlazerID received: ', end='')
        print(blazerID.decode())

        # create a random port number
        newPort = random.randrange(28000, 28300)

        print('Requesting STUDENT to accept TCP <', end='')
        print(str(newPort), end='')
        print('>...')

        # convert newPort to bytes
        newPortInBytes = str.encode(str(newPort))

        # wait one second, and then send the new port number (dddddd)
        time.sleep(1)
        # send the new port number
        conn.sendall(newPortInBytes)
        print('Done')

        print()
        print('closing socket')

        s.close()
        print('closed s')

        # 2nd connection
        print()
        print('Connecting to the STUDENT s1 <' + str(newPort) + '>')
        s_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_2.connect((HOST, newPort))

        # create the UDP port numbers and send to Student
        newUDPRobotPort = random.randrange(28301, 28600)
        newUDPStudentPort = random.randrange(23000, 23500)
        print('Sending the UDP information: to ROBOT: <' + str(newUDPRobotPort) +
              '>, to STUDENT: <' + str(newUDPStudentPort) + '>...')
        # create the tuple ffffff, eeeeee
        tupleToSend = str(newUDPRobotPort) + ',' + str(newUDPStudentPort)
        tupleToSendInBytes = str.encode(tupleToSend)
        s_2.sendall(tupleToSendInBytes)  # sending UDP port tuple
        print('Done')

        # connect via UDP and finish
        UDP_socket(HOST, newUDPRobotPort, newUDPStudentPort)



    else:
        print('That is not a valid BlazerID')

    return


def encrypted_socket(HOST, PORTSSL):
    '''
    # Creates an encrypted connection for assignment Paras 2, 3, 4a
    #  Takes a string HOST which is the IPv4 address of the host
    #  Takes an integer PORTSSL which is the inital port for the SSL connection: 27994
    '''
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # context.load_cert_chain(certfile="MySiteCert", keyfile="C:\\OpenSSL\\bin\\mykeyfile.pem")
    # context.load_cert_chain(certfile="C:\\OpenSSL\\bin\\mycertfile.pem", keyfile="C:\\OpenSSL\\bin\\mykeyfile.pem")
    context.load_cert_chain(certfile=certLocation,
                            keyfile=keyLocation)

    bindsocket = socket.socket()
    bindsocket.bind((HOST, PORTSSL))
    bindsocket.listen(5)
    print('Listening for TCP traffic on port ' + str(PORTSSL))
    print('TCP socket created, ready for listening and accepting connection...')
    print('waiting for encrypted connection on port ' + str(PORTSSL))
    print()

    # accept the connection
    while True:
        newsocket, addr = bindsocket.accept()
        print('   conn: ' + str(newsocket) + ' | addr ' + str(addr))

        # print status
        print('Client from ' + str(addr[0]) + ' at port ' + str(addr[1]) + ' connected')

        connstream = context.wrap_socket(newsocket, server_side=True)
        try:
            # myMethod(connstream)  # if we want to put this in a seperate method
            data = connstream.read()
            # null data means the client is done
            print(data)
            '''
            while data:
                if not data: # or we can pass to method: do_something(connstream, data):
                    # we'll assume do_something returns False
                    # when we're finished with client
                    print('Received: ', end = '')
                    print(data)
                    break
                data = connstream.read()
            '''

            # Check to ensure the BlazerID is a BlazerID
            print()
            if len(data) == 8:

                print('BlazerID received: ', end='')
                print(str(data.decode()))
                print()

                # create a random port number
                newPort = random.randrange(28000, 29000)

                print('Requesting STUDENT to accept (encrypted) TCP <', end='')
                print(str(newPort), end='')
                print('>...')

                # convert newPort to bytes
                newPortInBytes = str.encode(str(newPort))

                # wait one second, and then send the new port number (dddddd)
                time.sleep(1)
                connstream.sendall(newPortInBytes)
                print('Done')

                print()
                print('closing socket')
                # connstream.shutdown(socket.SHUT_RDWR)
                # connstream.close()
                newsocket.close()
                # bindsocket.close()

                print()
                print('done closing socket')

                # 2nd connection ******* TO DO *******
                # does this connection need to be reversed?
                # that is, have the Student present their cert in the handshake
                print()
                print('Connecting to the STUDENT s1 <' + str(newPort) + '>')
                context2 = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
                context2.load_cert_chain(certfile=certLocation,
                                         keyfile=keyLocation)
                bindsocket2 = socket.socket()
                bindsocket2.bind((HOST, newPort))
                bindsocket2.listen(5)
                print('Listening for TCP traffic on port ' + str(newPort))
                print('TCP socket created, ready for listening and accepting connection...')
                print('waiting for encrypted connection on port ' + str(newPort))
                print()

                # accept the socket
                newsocket2, addr2 = bindsocket2.accept()
                print('   conn: ' + str(newsocket2) + ' | addr ' + str(addr2))
                # print status
                print('Client from ' + str(addr2[0]) + ' at port ' + str(addr2[1]) + ' connected')

                # create the UDP port numbers and send to Student
                newUDPRobotPort = random.randrange(28301, 28600)
                newUDPStudentPort = random.randrange(23000, 23500)
                print('Sending the UDP information: to ROBOT: <' + str(newUDPRobotPort) +
                      '>, to STUDENT: <' + str(newUDPStudentPort) + '>...')
                # create the tuple ffffff, eeeeee
                tupleToSend = str(newUDPRobotPort) + ',' + str(newUDPStudentPort)
                tupleToSendInBytes = str.encode(tupleToSend)

                connstream2 = context.wrap_socket(newsocket2, server_side=True)

                connstream2.sendall(tupleToSendInBytes)  # sending UDP port tuple
                print('Done')
                print()
                newsocket.close()
                print()
                print('done closing socket')

                # connect via UDP and finish
                UDP_socket(HOST, newUDPRobotPort, newUDPStudentPort)


            else:
                print('That is not a valid BlazerID')

            # finished with client
        finally:
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()

    return



def UDP_socket(HOST, RobotPort, StudentPort):
    '''
    # Creates a UDP connection for assignment Para 4
    #  Takes a string HOST which is the IPv4 address of the host
    #  Takes an integer RobotPort which is the inital port for the connection: ffffff
    #  Takes an integer StudentPort which is the inital port for the connection: eeeeee
    '''
    ffffff = RobotPort
    eeeeee = StudentPort

    # make the UDP socket connection
    print('Preparing to receive X...')
    s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP: DGRAM
    s3.bind((HOST, ffffff))
    x, addr3 = s3.recvfrom(4096)

    xInt = int(x)
    print('Got x = ' + str(xInt))

    # check to ensure the input is valid
    if 5 < xInt < 10:
        xxx = xInt * 10
    else:
        print('That number is not between 5 and 10')

    # create the message to send back, number of bytes = x * 10
    numString = createNumString(xxx)
    numStringBytes = str.encode(numString)

    # send back the message 5 times
    s3b = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP: DGRAM

    print('Sending UDP packets:')
    print('Message to transmit: ' + numString)
    # wait one second, and then send the string
    time.sleep(1)
    for i in range(1, 6):
        s3b.sendto(numStringBytes, (HOST, eeeeee))
        print('UDP packet ' + str(i) + ' sent')
        time.sleep(1)  # wait one second

    # set up a new socket to receive the Student's return string
    print('Receiving UDP packet:')
    x2, addr3c = s3.recvfrom(4096)
    x2String = str(x2)
    x3String = x2.decode()
    print('Received: ' + str(x3String))

    # check to ensure the strings match
    if numString == x3String:
        print('The two strings are the same.')





    else:
        print('The two strings are NOT the same.')
        print('Robot was expecting: ' + numString)
        print('Robot received: ' + x3String)




    # not sure this is necessary, but it makes me feel happy
    s3.close()
    s3b.close()
    # s3c.close()

    return


def createNumString(xxx):
    '''
    # a little helper function to create the string to send to student
    #  Takes an integer xxx
    #  returns a string whose length is xxx * 10
    '''
    numString = ''
    for i in range(0, xxx, 10):
        # numString = numString + str(i%10)
        numString = numString + '123456789'
        y = i // 10 + 1
        numString = numString + str(y)

    return numString


# ======= start main =======
if STARTED == 0:
    print('NEW-IMPROVED-SSL-CAPABLE ROBOT IS STARTED')
    print()
    print('Creating TCP socket...')
    STARTED = STARTED +1






import multiprocessing


p1= multiprocessing.Process(target = unecrypted_socket, args= (HOST,PORT)) #same general idea as threading
#this has more built in functionality than threading does in python.
p2= multiprocessing.Process(target=encrypted_socket, args=(HOST, PORTSSL))

global processes
processes = []
processes.append(p1)
processes.append(p2)

#perhaps killing the thread that controls the port NOT chosen will stop the hang up?




if __name__ == '__main__': #this prevents this from happening recursively --- makesit so p1 and p2 are only called from main

    for p in processes:
        p.start()



























