# A simple network chat program between to Raspberry Pi's

import network
import sys

def heard(phrase):
  print "them:" + phrase

print "Chat Program"

if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)

print "Chat away!"  
while network.isConnected():
  phrase = raw_input()
  print "me:" + phrase
  network.say(phrase)
  
