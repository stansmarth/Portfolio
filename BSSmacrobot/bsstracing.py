import traceback
from importlib import reload
from pynput.keyboard import Key
from pynput.mouse import Button
from convertAhkPattern import ahkPatternToPython
from pixelcolour import getPixelColor
import platform
import imagehash
import random


def acchold(key, duration):
    ws = loadsettings.load()["walkspeed"]
    pag.keyDown(key)
    sleep(duration*ws/28)
    pag.keyUp(key)

sideTime = 0
frontTime = 0.45
#move.press(",")
acchold('a',0.3)
for i in range(3):
    acchold("w", frontTime)
    acchold("a", sideTime)
    acchold("s", frontTime)
    acchold("d", sideTime)

sideTime = 0
frontTime = 0.45
move.press(",")
acchold('a',0.3)
for i in range(3):
    acchold("s", frontTime)
    acchold("d", sideTime)
    acchold("w", frontTime)
    acchold("d", sideTime)
for i in range(3):
    acchold("s", frontTime)
    acchold("a", sideTime)
    acchold("w", frontTime)
    acchold("a", sideTime)


def runPath(name):
    path = f"./paths/{name}"
    #try running a automator workflow
    #if it doesnt exist, run the .py file instead
    setdat = loadsettings.load()
    ws = setdat["walkspeed"]
    if os.path.exists(path+".workflow"):
        os.system(f"/usr/bin/automator {path}.workflow")
    else:
        exec(open(f"{path}.py").read())
        
def pagmove(k,t):
    pag.keyDown(k)
    time.sleep(t)
    pag.keyUp(k)

def pagPress(key, delay = 0.02):
    pag.keyDown(key, _pause = False)
    time.sleep(delay)
    pag.keyUp(key, _pause = False)


