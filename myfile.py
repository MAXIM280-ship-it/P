from pion.pion import Pion as P

import time
import cv2
import cv2.aruco as aruco

# capture = cv2.VideoCapture('rtsp://127.0.0.1/18001')
# # Загрузка изображения
# image = cv2.imread('marker.png')
# # Задаем тип маркера
# aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
# parameters = cv2.aruco.DetectorParameters()
# detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
# # Распознаем маркер
# corners, ids, _ = detector.detectMarkers(image)
# print(corners)
# image = aruco.drawDetectedMarkers(image, corners, ids)
# cv2.imshow('Detected ArUco', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

ip = "127.0.0.1"
port = 8001
port_video = 18001
STEP = 0.5
H = 1
# bot = A(ip=ip, mavlink_port=port)

# bot.arm()
# bot.takeoff()
# time.sleep(10)

# bot.goto(1,1,0,0)

drone = P(ip, port)
drone.arm()
drone.takeoff()
time.sleep(10)
def fly():
    global STEP
    global H
    time.sleep(5)
    current_x = drone.position[0]
    current_y = drone.position[1]
    drone.goto(-current_x,current_y,H,0)
    # drone.print_information()
    while True:
        print(drone.print_information())
        if int(drone.position[0]) == int(-current_x):
            print('reached')
            drone.point_reached = True
            drone.goto(-current_x, -(abs(current_y)-STEP), H, 0)
            time.sleep(5)
            fly()
            # break
fly()

vid = P(ip, port_video)


# while True:

# while move:
#     move = False
#     current_x = drone.position[0]
#     current_y = drone.position[1]
#     drone.goto(-current_x,current_y,H,0)
#     drone.print_information()
#     if int(drone.position[0]) == int(-current_x):
#         print('reached')
#         drone.point_reached = True
#         drone.goto(-current_x, -(abs(current_y)-STEP), H, 0)
#         time.sleep(3)
    
#     move = True
    # current_x = drone.position[0]
    # current_y = drone.position[1]
    # drone.goto(-current_x, current_x, H, 0)
        # print(drone.position[0], drone.position[1], drone.point_reached)
# if drone.point_reached(5,-5,H,0):
# while True:
# #     print(drone.position_controller)
# while not drone.point_reached():

