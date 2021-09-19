import os
import subprocess
from multiprocessing import Process
from sys import platform
def publish():
    if platform == "linux":
        subprocess.call(['gnome-terminal', '-e', 'python publisher.py'])
    else:
        os.system("python publisher.py")
def recieve():
    if platform == "linux":
        subprocess.call(['gnome-terminal', '-e', 'python reciever.py'])
    else:
        os.system("python reciever.py")

p = Process(target=publish)
q = Process(target=recieve)

p.start()
q.start()
p.join()
q.join()


