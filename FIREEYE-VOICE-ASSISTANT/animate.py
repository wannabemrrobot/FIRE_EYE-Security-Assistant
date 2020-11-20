import itertools
import threading
import time
import sys

def parent_animate():
    done = False
    #here is the animation
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rLoading >>  ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(5)
    done = True
parent_animate()