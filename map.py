import opening as op
import state_processor as sp
import cv2
import numpy as np
import pyautogui
import matplotlib.pyplot as plt
from PIL import Image
import main as m
# ds_location = op.window_capture()
# print(ds_location)

s = ''
with open("emulator_location.txt") as f:
    s = f.read()
    print(type(s))
coords = s.split('\n')
for i in range(0, 4):
    coords[i] = int(coords[i])

        # else:
        #     if int(r) == 115:
        #         print(new_img[x,y])


# # Resize the image
# new_contour = edg
# new_contour = cv2.cvtColor(new_contour, cv2.COLOR_BGR2RGB)
# height, width = new_contour.shape[0], new_contour.shape[1]
# std_ascii_plot = []

# for x in range(height):
#     row = []
#     for y in range(width):
#         r, g, b = new_contour[x, y]
#         if int(r) != 0 and int(g) != 0 and int(b) != 0:
#             row.append("1")
#         else:
#             row.append("0")
#             # p = str(x) + " " + str(y)
#             # print(p)
#     std_ascii_plot.append(row)

# f = open("current_thing.txt", "w")
# for i in std_ascii_plot:
#     buff = ""
#     for j in i:
#         buff = buff + j
#     buff = buff + "\n"
#     # print(buff)
#     f.write(buff)
# f.close()





def map_check():
    # m.score = len(locations) * 10
    with open("overworld_data.txt") as f:
        s = f.read()
        print(type(s))
    m.p_coords = s.split('\n')
    for i in range(0, 4):
        m.p_coords[i] = int(m.p_coords[i])
    m.current_location = int(m.p_coords[0])
    if(m.current_location != m.previous_location):
        if m.previous_location != 0:
            m.saved_maps[m.previous_location] = [m.map, m.first, m.second]
            if m.current_location in m.saved_maps:
                m.map = m.saved_maps[m.current_location][0]
                m.first = m.saved_maps[m.current_location][1]
                m.second = m.saved_maps[m.current_location][2]
            else:
                m.map = [[0],
                       [9],
                       [0]]
                m.first = 1
                m.second = 0
    if m.p_coords[0] not in m.locations:
        m.locations.append(m.p_coords[0])

    m.curr_coords[0], m.curr_coords[1], m.curr_coords[2] = m.p_coords[1], m.p_coords[2], m.p_coords[3]
    
    #x axis
    if m.curr_coords[0] > m.prev_coords[0]:
        if m.prev_coords[0] != 0:
            m.map[m.first][m.second] = 1
            m.second += 1
            if m.second >= len(m.map[0]):
                for i in range(len(m.map)):
                    m.map[i].append(0)
                m.second = len(m.map[0])-1
            m.map[m.first][m.second] = 9

    if m.curr_coords[0] < m.prev_coords[0]:
        if m.prev_coords[0] != 0:
            m.map[m.first][m.second] = 1
            m.second -= 1
            if m.second < 0:
                for i in range(len(m.map)):
                    m.map[i].insert(0,0)
                m.second = 0
            m.map[m.first][m.second] = 9
    
    #y axis
    if m.curr_coords[1] < m.prev_coords[1]:
        if m.prev_coords[0] != 0:
            m.map[m.first][m.second] = 1
            m.first -= 1
            if m.first < 0:
                m.map.insert(0, [0 for row in range(len(m.map[0]))])
                m.first = 0
            m.map[m.first][m.second] = 9

    if m.curr_coords[1] > m.prev_coords[1]:
        if m.prev_coords[0] != 0:
            m.map[m.first][m.second] = 1
            m.first += 1
            if m.first >= len(m.map):
                m.map.append([0 for row in range(len(m.map[0]))])
                m.irst = len(m.map)-1
            m.map[m.first][m.second] = 9


    edg, og_img = sp.capture_and_process_screenshot(coords)

    ctrs, _ = cv2.findContours(edg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_image = og_img.copy()
    cv2.drawContours(contour_image, ctrs, -1, (0,255,0), 2)
    # # Display the image with contours

    new_img = cv2.cvtColor(og_img, cv2.COLOR_BGR2RGB)
    width, height = og_img.shape[0], og_img.shape[1]
    player_coords = [0,0]
    target_coords = [0,0]
    for y in range(height):      # this row
        for x in range(width):   # and this row was exchanged
            r, g, b = new_img[x,y]
            if int(r) == 189 and int(g) == 74 and int(b) == 41:
                # print("player coords: ")
                # print(y)
                # print(x)
                # print("\n")
                player_coords = [y, x]
            if int(r) == 181 and int(g) == 82 and int(b) == 57:
                # print("target coords: ")
                # print(y)
                # print(x)
                # print("\n")
                target_coords = [y, x]

    new_size = (80, 20)  # Example: Half of the original size
    scaled_player_coords = [int(player_coords[0] * 0.15), int(player_coords[1] * 0.04)]
    scaled_target_coords = [int(target_coords[0] * 0.15), int(target_coords[1] * 0.04)]

    print(player_coords)
    print(target_coords)
    print(scaled_player_coords)
    print(scaled_target_coords)

    # Resize the image
    new_contour = cv2.resize(edg, new_size, interpolation=cv2.INTER_AREA)
    new_contour = cv2.cvtColor(new_contour, cv2.COLOR_BGR2RGB)
    height, width = new_contour.shape[0], new_contour.shape[1]
    std_ascii_plot = []

    for x in range(height):
        row = []
        for y in range(width):
            r, g, b = new_contour[x, y]
            if scaled_player_coords[1] == x and scaled_player_coords[0] == y:
                row.append("🅿️")
            if scaled_target_coords[1] == x and scaled_target_coords[0] == y and (scaled_target_coords[1] != 0 and scaled_target_coords[0] != 0):
                row.append("🚀")
            if int(r) != 0 and int(g) != 0 and int(b) != 0:
                row.append("E")
            else:
                row.append(".")
                # p = str(x) + " " + str(y)
                # print(p)
        std_ascii_plot.append(row)

    f = open("current_thing.txt", "w")
    for i in std_ascii_plot:
        buff = ""
        for j in i:
            buff = buff + j
        buff = buff + "\n"
        # print(buff)
        # f.write(buff)
    print("\n\n\n\n")
    emoji_map = []
    for j in m.map:
        buffer = []
        for i in j: 
            if i == 0: 
                buffer.append('?')
            elif i == 9: 
                buffer.append('🅿️')
            elif i == 1: 
                buffer.append('.')
        emoji_map.append(buffer)
    for k in emoji_map:
        print(k)
    m.previous_location = m.current_location
    print(m.prev_coords)
    print(m.curr_coords)
    # print(map[first][second])
    f.close()

    m.prev_coords[0], m.prev_coords[1], m.prev_coords[2] = m.curr_coords[0], m.curr_coords[1], m.curr_coords[2] 
# areas = [cv2.contourArea(cnt) for cnt in ctrs]

# min_area = 200
# max_area = 4000

# filtered_contours = [cnt for cnt in ctrs if min_area < cv2.contourArea(cnt) < max_area]

# player_position = None
# for contour in filtered_contours:
#     x, y, w, h = cv2.boundingRect(contour)
#     player_position=(x + w // 2, y + h // 2)
# print(player_position)

# for cnt in filtered_contours:
#     cv2.drawContours(contour_image, [cnt], -1, (0, 0, 255), 2)

# Display the filtered contours
# plt.imshow(cv2.cvtColor(og_img, cv2.COLOR_BGR2RGB))
# plt.title("Filtered Contours (Player Character)")
# plt.show()