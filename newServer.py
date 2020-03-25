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
import threading
import time
import socket
import ssl
import os
import sys
import random
import signal



######################################CRUCIAL VARIABLES###########################################################


# set up initial variables:
# HOST = 'localhost'  # mine works either way, but I read some reports that the IP works better
HOST = '127.0.0.1'
# HOST = '::1'
PORT = 3310
PORTSSL = 27994
TIMER_INIT = 5

global check_status_timer
check_status_timer = TIMER_INIT

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
    context.load_cert_chain(certfile= certLocation,
                            keyfile= keyLocation)

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
                context2.load_cert_chain(certfile= certLocation,
                                         keyfile= keyLocation)
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


#################################[ SET UP THREADING ]#############################################

'''

t1 and t2 control sockets. t1 is unencrypted. t2 is encrypted.

tCoordinator coordinates t1 and t2.

strategy: activate signals thread to start. deactivate tells threads to stop. use t3 to send signals.

Kill t1,t2 from TCoordinator?

def resume(killableThread):
    killableThread.running.set()  # testing -- likely useless. from tutorial that wasn't very helpful.
    return

def pause(killableThread):
    killableThread.running.clear()  # same as above
    return
'''


''' 
        
        1:06 AM: 3/25/2020
        John,
        
        HOW THIS WORKS (above):
        
        Just think of this as being like a constructor in Java and it will almost make sense.
        
        This class is derived from the threading.py module included in Python.
        I dug through the code and figured out how to make a subclass of the Thread object.
        This subclass allows us to kill the thread on command. We can add additional
        functionality as needed, but be warned, it's rather tedious and hard to figure out 
        sometimes. I have a much easier time finding my way through Java objects for some reason,
        although Python is obviously much easier to churn out code with.
        -Will 
        





HOW THIS (hopefully) WORKS:
I'm kind of winging it here, we've never really messed with 
object oriented programming in Python, in my classes so far it's pretty much
been Java if we get very far into classes and whatnot. 

Python does not have easily killable threads according to my research.
You have to implement that on your own with weird workaraounds.
This subclass of threading.Thread will allow me to extend 
threading's functionality. I'm going to add a method that allows me to
kill the thread gracefully (I hope).

It's going to check on regular intervals if the kill signal has gone out
Once it detects the kill signal, it kills the thread.


A note on classes in Python:
"dunder" functions (weird name, it's short for double underscore)
are functions with two underscores in their names, typically looking
like this:  __init__()
They seem to be built in functions.

super seems to make a superclass.
self.arg_0 = arg[0] lets me map out argument 0, etc
self works similarly to self in Java


3/25/2020 3:25 PM

John,

I think I figured something out. Attributes of built-in python objects cannot be added to according to this

https://stackoverflow.com/questions/5741699/attribute-assignment-to-built-in-object

instead, they must be added on an instance-by-instance-basis
thus, i will see if that is doable.-Will


def murderThread(self):

        return

class killableThread(threading.Thread):
    def __init__(self, group = None, target = None, name = None,
                args = (),kwargs = None,): #init is sort of like a Java constructor
        super(killableThread,self).__init__(group = group, target = target,
                                args =args, kwargs = kwargs,name = name,)



        self.target = target
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}


        killableThread.dead = threading.Event() # if flag is set to true, thread is dead
        killableThread.running = threading.Event()  # if flag set to true, thread is alive

        killableThread.dead = False #don't want to murder this thread yet

        killableThread.running.set()  #by default is set
        #threading events are set to false i believe. built in flag attribute in Event

        if killableThread.dead == True:
            killableThread.running.clear()
            time.sleep(3) # do nothing 3 seconds?

'''

server_shutdown = False

shutdownMsg = "....Thread should be switching off...."



t1 = threading.Thread(target=unecrypted_socket, args=(HOST, PORT,))
t2 = threading.Thread(target=encrypted_socket, args=(HOST, PORTSSL,))


###############################Controls t1 and T2...

def coordinate_threads(thread1, thread2):

    # Started the threads
    t1.start()
    print("called t1.start()...")
    print("calling t2.start()...")

    t2.start()
    print("t1 and t2 called from t3...")




####################################################


def check_status():
    if server_shutdown == True:
        print(server_shutdown, "<--- server shutdown Boolean...if that says TRUE....should be shutting down")

    if server_shutdown == False:
            time.sleep(TIMER_INIT)
            print("check status...still alive")

            '''
        if 0 >= check_status_timer and server_shutdown == False:
            print("------------------------------------------")
            print("\n[THREAD STATUS CHECK]\n")
            print("Timer at zero...checking status")
            while server_shutdown == False:
                print("Server Running")
                print("server shutdown = ", server_shutdown)
                print("|T1:", t1.is_alive(), "| T2:", t2.is_alive())
                print("--------------------------------------")
                check_status()
'''

tCoordinator_1= threading.Thread(target = coordinate_threads, args =(t1,t2), daemon = True)
tCoordinator_2 = threading.Thread(target = check_status ,daemon = True)


#################################[ DEFINE FUNCTIONS}##########################


# -*- coding: utf-8 -*-
# My Name:  John Bedingfield  My Partner:  Will Watts

'''
# TO DO
-- for threading, maybe use event objects so one thread knows the other is called and can stop listening
     or perhaps it's ok, if it keeps listening
-- Is there anything missing from the SSL/TLS handshake?
-- Does the 2nd part of the encrypted connection need to use Client as Server?
-- graceful close?
-- better error checking on BazerID and num?  right now it doesn't loop back
      to give the Student another try

'''


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
        server_shutdown = True
        print(server_shutdown, "<--server shutdown Boolean... if that says TRUE....should be shutting down")

        print("READY TO SHUT DOWN SAFELY")
        print("PRESS CRL-C WHEN READY TO CLOSE")


    else:
        print('The two strings are NOT the same.')
        print('Robot was expecting: ' + numString)
        print('Robot received: ' + x3String)



    # not sure this is necessary, but it makes me feel happy
    s3.close()
    s3b.close()
    # s3c.close()
    server_shutdown = True
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
print('NEW-IMPROVED-SSL-CAPABLE ROBOT IS STARTED')
print()
print('Creating TCP socket...')
# Create the Threads, one for unencrypted and one for encrypted

#perhaps create a t3 thread that has a target of kill_all_threads and controls shutdown process


tCoordinator_1.start()
tCoordinator_2.start()




