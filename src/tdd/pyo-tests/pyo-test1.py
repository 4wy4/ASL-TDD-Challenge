#!/usr/bin/env python2

from pyo import *

s = Server().boot()
s.start()
sf = SfPlayer("../../../examples/handshake.wav", speed = 1, loop = True).out()
