

# Define the images globally so they can be used in every loop
import time

import cv2

img = None
image = None
coords_list = []


def mouse_click(event, x, y, flags, param):
    global image, img
    # to check if left mouse
    # button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # font for left click event
        font = cv2.FONT_HERSHEY_TRIPLEX
        LB = 'Left Button'

        # display that left button
        # was clicked.
        # cv2.putText(img, LB, (x, y),
        #             font, 1,
        #             (255, 255, 0),
        #             2)
        coords_list.append((x,y))
        # to check if right mouse
    # button was clicked
    elif event == cv2.EVENT_RBUTTONDOWN:
        # font for right click event
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        RB = 'Right Button'

        # display that right button
        # was clicked.
        # cv2.putText(img, RB, (x, y),
        #             font, 1,
        #             (0, 255, 255),
        #             2)
        coords_list.append((x, y))



if __name__ == "__main__":
    # read image
    img = cv2.imread('C:/Users/sudha/Desktop/trendzlink/sona-data/gear4_110_collect_13_3/STN2-CAM1/Gear_4_exp3.jpg')

    while True:
        image = img.copy()
        # save all the coords of the clicked region and mark it, since it refreshes every cycle
        for coord in coords_list:
            image = cv2.circle(image, coord, 20, (0, 0, 255), -1)
        image = cv2.addWeighted(img, 0.8, image, 0.2, 0)

        cv2.imshow("image", image)
        cv2.setMouseCallback('image', mouse_click)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        del image
        # time.sleep(3)
    # close all the opened windows.
    cv2.destroyAllWindows()
