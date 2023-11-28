import time
import cv2
import djitellopy as tello

drone= tello.Tello()
drone.connect()

key= True

while key:
    print("t: Takeoff, c: Picture, u: Move up, d: Move down, l:Move left, r:Move right, f:Move forward, b: Move back, land: Land")
    i = input("Enter command:")
    if i=="t":
        drone.takeoff()
    elif i=="c":
        print(drone.get_battery())
        drone.streamon()
        s = True
        while s:
            img = drone.get_frame_read().frame
            time.sleep(1)
            img = cv2.resize(img, (360, 240))
            cv2.imshow("Results", img)
            cv2.imwrite("test.jpg", img)
            print("taking picture")
            time.sleep(2)
            cv2.waitKey(1)
            s = False
    elif i=="u":
        drone.move_up(80)
    elif i=="d":
        drone.move_down(20)
    elif i=="l":
        drone.move_left(100)
    elif i=="r":
        drone.move_right(100)
    elif i=="f":
        drone.move_forward(80)
    elif i=="land":
        drone.land()

drone.land()
