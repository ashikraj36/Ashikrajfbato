
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile 
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
