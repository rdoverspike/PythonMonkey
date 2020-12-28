"""
Execute a command on your android device using the `exec` api.
"""
import sys
sys.path.append("C:/src/PythonMonkey")
import adblib
adb = adblib.ADB()
adb.connect()
for tp, serial in adb.devices():
    print("%-10s %s" % (tp, serial))
try:
    print(adb.exec(" ".join(sys.argv[1:])))
    # print(adb.shell(" ".join(sys.argv[1:])))
except Exception as e:
    print(e)

