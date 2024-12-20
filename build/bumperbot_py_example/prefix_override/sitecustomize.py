import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mylovetron/bumperbot_ws/install/bumperbot_py_example'
