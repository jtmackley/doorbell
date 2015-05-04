# network.py  (c) 2013 @whaleygeek

import thread
import socket
import time

def defaultWhenHungupHandler():
  trace("CONNECTION LOST")
  
SERVER_HOST     = "0.0.0.0"
PORT            = 8888
BUFFER_SIZE     = 1204
whenHearHandler = None
whenHungupHandler = defaultWhenHungupHandler
connected       = False # TODO 'state'

myHandle        = None
peerHandle      = None

# eventually this will be a class so we can have multiple.
# for now, just keep it simple, we only need one in any one program.


def trace(message):
  print "network:" + message
  
  
def whenHungUp(thenCallFunction):
  global whenHungupHandler
  if thenCallFunction == None:
    whenHungupHandler = defaultWhenHungupHandler
  else:
    whenHungupHandler = thenCallFunction
    
    
# client calling server
def call(addr, whenHearCall):
  global peerHandle, whenHearHandler, connected, PORT
  #trace("call:" + addr)
  whenHearHandler = whenHearCall
  peerHandle = _clientOpen(addr, PORT)
  connected = True
  _startListenerThread(peerHandle, addr)
  
  
# server waiting for client
def wait(whenHearCall):
  global connected, whenHearHandler, SERVER_HOST, PORT, myHandle, peerHandle
  #trace("wait")
  whenHearHandler = whenHearCall
  
  # blocking wait
  myHandle = _serverWait(SERVER_HOST, PORT)
  peerHandle, addr = _serverAccept(myHandle)
  connected = True
  _startListenerThread(peerHandle, addr)
     
      
def isConnected():
  global connected
  #trace("isConnected")
  return connected
  
  
def say(data):
  global peerHandle
  #trace("say:" + data)
  if (peerHandle == None):
    hangUp()
  else:
    _send(peerHandle, data + "\n")
  
  
def hangUp():
  global myHandle, peerHandle, connected
  #trace("hangup")
  whenHungupHandler()
  connected = False
  
  _stopListenerThread()

  if (peerHandle != None):
    _close(peerHandle)
    peerHandle = None
  if (myHandle != None):
    _close(myHandle)
    myHandle = None
    


def _startListenerThread(handle, addr):
  thread.start_new_thread(_listenerThreadBody, (handle, addr))
  
  
def _stopListenerThread():
  #trace("_stopListenerThread")
  #TODO
  pass
  
  
def _listenerThreadBody(handle, addr):
  # trace("_listenerThreadBody:" + str(addr))
  while True:
    try:
      data = _receive(handle)
      if (data == None or len(data) == 0):
        hangUp()
        break
      whenHearHandler(data)
    except:
      hangUp()
      return  
      
      
# binding to underlying sockets

def _clientOpen(addr, port):
  #trace("open:" + addr)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((addr, port))
  return s  
  
  
def _serverWait(addr, port):
  #trace("wait connection")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((addr, port))
  s.listen(1)
  return s
  
  
def _serverAccept(handle):
  #trace("accept")
  handle2, addr = handle.accept()
  #trace("Connected by:"+ str(addr))
  return handle2, addr


def _close(handle):
  #trace("close")
  handle.close()  


def _send(handle, data):
  #trace("send:" + data)
  handle.sendall(data)


def _receive(handle):
  #trace("receive")
  data = handle.recv(BUFFER_SIZE)
  if (data == None):
    raise "lost connection"
  return data

# END
