import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

debug = True

import Leap, math
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"


    def on_frame(self, controller):
        pass #print "Frame available"

def angle_between(vector1, vector2):
    return math.degrees(vector1.angle_to(vector2))

"""def ASL_symbol(positions, palmPosition, normal): #positions is a list of finger positions, palmPosition is the palm position, and normal is the normal vector to the palm
    #define the hand position by the angles between all the bones
    forgiveness = 5
    #find "A" first
    A = true
    for
    if (angle between first bone and normal is 0) and (angle between first and second bones is 90 or -90):
   """     

def recognize_gesture(hand): #recognizes a gesture from the given hand object
    position = hand.palm_position
    normal = hand.palm_normal
    fingers = hand.fingers
    forgiveness = 5
    #find "A" first
    a = True
    if debug:
        print "is it an a?"
    for finger in fingers:
        if finger.type() == TYPE_THUMB:
            pass
        elif (finger.type() == TYPE_INDEX or finger.type == TYPE_MIDDLE) and ((math.fabs(angle_between(finger.bone(TYPE_PROXIMAL).direction, finger.bone(TYPE_INTERMEDIATE).direction)-270) > forgiveness) or (math.fabs(angle_between(finger.bone(TYPE_PROXIMAL).direction, normal)) > forgiveness)):
            a = False
            break
    if a:
        print "a"
        return 'a'
    #then find other symbols
                                                                                                                                              
def main():
    if debug:
        print "listener = SampleListener()"
    listener = SampleListener() #get the listener
    if debug:
        print "controller = Leap.Controller()"
    controller = Leap.Controller() #get the controller
    if debug:
        print "controller.add_listener(listener)"
    controller.add_listener(listener) #start listening
    if debug:
        print "frame = controller.frame()"
    frame = controller.frame() #get the frame
    if debug:
        print "hands = frame.hands"
    hands = frame.hands #get all hands
    if debug:
        print "first_hand = hands[0]"
    first_hand = hands[0] #get the first hand
    if debug:
        print "got the first hand"
    if first_hand.is_valid: #make sure there is a hand there
        if debug:
            print "first hand is valid!"
        gesture = recognize_gesture(first_hand) #recognize the gesture
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
