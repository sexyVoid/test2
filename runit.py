#`python3 runit.py`. If the program doesn't work, it's either because of the password or because OpenSSL and Python are not installed on the system.
from os import system as x4,listdir as x2
for x in x2():
 if x.split(".")[0]==bytes.fromhex("656e6372797074").decode("utf-8"):
  x4(bytes.fromhex("6f70656e73736c206165732d3235362d636263202d70626b646632202d6b66696c65207073737764202d64202d696e20").decode("utf-8")+x+bytes.fromhex("202d6f757420").decode("utf-8")+x[0x8:])
