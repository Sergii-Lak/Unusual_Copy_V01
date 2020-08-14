from PIL import Image, ImageDraw
import time
import os

#-------------------------------------------------

color_list = [[[255, 255, 204], [255, 255, 153], [255, 255, 102], [255, 255, 51], [255, 255, 0], [204, 204, 0]],
                  [[255, 204, 102], [255, 204, 0], [255, 204, 51], [204, 153, 0], [204, 153, 51], [153, 102, 0]],
                  [[255, 153, 0], [255, 153, 51], [204, 153, 102], [204, 102, 0], [153, 102, 51], [102, 51, 0]],
                  [[255, 204, 153], [255, 153, 102], [255, 102, 0], [204, 102, 51], [153, 51, 0], [102, 0, 0]],
                  [[255, 102, 51], [204, 51, 0], [255, 51, 0], [255, 0, 0], [204, 0, 0], [153, 0, 0]],
                  [[255, 204, 204], [255, 153, 153], [255, 102, 102], [255, 51, 51], [255, 0, 51], [204, 0, 51]],
                  [[204, 153, 153], [204, 102, 102], [204, 51, 51], [153, 51, 51], [153, 0, 51], [51, 0, 0]],
                  [[255, 102, 153], [255, 51, 102], [255, 0, 102], [204, 51, 102], [153, 102, 102], [102, 51, 51]],
                  [[255, 153, 204], [255, 51, 153], [255, 0, 153], [204, 0, 102], [153, 51, 102], [102, 0, 51]],
                  [[255, 102, 204], [255, 0, 204], [255, 51, 204], [204, 102, 153], [204, 0, 153], [153, 0, 102]],
                  [[255, 204, 255], [255, 153, 255], [255, 102, 255], [255, 51, 255], [255, 0, 255],
                   [204, 51, 153]],
                  [[204, 153, 204], [204, 102, 204], [204, 0, 204], [204, 51, 204], [153, 0, 153], [153, 51, 153]],
                  [[204, 102, 255], [204, 51, 255], [204, 0, 255], [153, 0, 204], [153, 102, 153], [102, 0, 102]],
                  [[204, 153, 255], [153, 51, 204], [153, 51, 255], [153, 0, 255], [102, 0, 153], [102, 51, 102]],
                  [[153, 102, 204], [153, 102, 255], [102, 0, 204], [102, 51, 204], [102, 51, 153], [51, 0, 51]],
                  [[204, 204, 255], [153, 153, 255], [102, 51, 255], [102, 0, 255], [51, 0, 153], [51, 0, 102]],
                  [[153, 153, 204], [102, 102, 255], [102, 102, 204], [102, 102, 153], [51, 51, 153],
                   [51, 51, 102]],
                  [[51, 51, 255], [51, 0, 255], [51, 0, 204], [51, 51, 204], [0, 0, 153], [0, 0, 102]],
                  [[102, 153, 255], [51, 102, 255], [0, 0, 255], [0, 0, 204], [0, 51, 204], [0, 0, 51]],
                  [[0, 102, 255], [0, 102, 204], [51, 102, 204], [0, 51, 255], [0, 51, 153], [0, 51, 102]],
                  [[153, 204, 255], [51, 153, 255], [0, 153, 255], [102, 153, 204], [51, 102, 153], [0, 102, 153]],
                  [[102, 204, 255], [51, 204, 255], [0, 204, 255], [51, 153, 204], [0, 153, 204], [0, 51, 51]],
                  [[153, 204, 204], [102, 204, 204], [51, 153, 153], [102, 153, 153], [0, 102, 102],
                   [51, 102, 102]],
                  [[204, 255, 255], [153, 255, 255], [102, 255, 255], [51, 255, 255], [0, 255, 255], [0, 204, 204]],
                  [[153, 255, 204], [102, 255, 204], [51, 255, 204], [0, 255, 204], [51, 204, 204], [0, 153, 153]],
                  [[102, 204, 153], [51, 204, 153], [0, 204, 153], [51, 153, 102], [0, 153, 102], [0, 102, 51]],
                  [[102, 255, 153], [51, 255, 153], [0, 255, 153], [51, 204, 102], [0, 204, 102], [0, 153, 51]],
                  [[153, 255, 153], [102, 255, 102], [51, 255, 102], [0, 255, 102], [51, 153, 51], [0, 102, 0]],
                  [[204, 255, 204], [153, 204, 153], [102, 204, 102], [102, 153, 102], [51, 102, 51], [0, 51, 0]],
                  [[51, 255, 51], [0, 255, 51], [0, 255, 0], [0, 204, 0], [51, 204, 51], [0, 204, 51]],
                  [[102, 255, 0], [102, 255, 51], [51, 255, 0], [51, 204, 0], [51, 153, 0], [0, 153, 0]],
                  [[204, 255, 153], [153, 255, 102], [102, 204, 0], [102, 204, 51], [102, 153, 51], [51, 102, 0]],
                  [[153, 255, 0], [153, 255, 51], [153, 204, 102], [153, 204, 0], [153, 204, 51], [102, 153, 0]],
                  [[204, 255, 102], [204, 255, 0], [204, 255, 51], [204, 204, 153], [102, 102, 51], [51, 51, 0]],
                  [[204, 204, 102], [204, 204, 51], [153, 153, 102], [153, 153, 51], [153, 153, 0], [102, 102, 0]],
                  [[255, 255, 255], [204, 204, 204], [153, 153, 153], [102, 102, 102], [51, 51, 51], [0, 0, 0]]]


def random_chois_color():
    import random
    number_color_image = random.randint(0, 35)
    return number_color_image

def support_random(shirina,visota,large, color, draw, x1, x2, y1, y2, color_choice_user):
    if  color_choice_user == "RANDOM":
        color_image = random_chois_color()
    elif color_choice_user == "red":
        color_image = 4
    elif color_choice_user == "blue":
        color_image = 18
    elif color_choice_user == "yellow":
        color_image = 0
    elif color_choice_user == "green":
        color_image = 30
    elif color_choice_user == "brown":
        color_image = 2
    elif color_choice_user == "pink":
        color_image = 10
    elif color_choice_user == "black":
        color_image = 35
    elif color_choice_user == "turquoise":
        color_image = 23
    elif color_choice_user == "orange":
        color_image = 1
    for i in range(round(shirina / large) * round(visota / large)):

        kkk = color[x1, y1]
        fff = color[x2 - 1, y2 - 1]
        t = round((kkk + fff) / 2)
        if t >= 0 and t < 41:
            draw.line((x1, y1, x2, y2), fill=(tuple(color_list[color_image][5])), width=5)
            draw.line((x2, y1, x1, y2), fill=(tuple(color_list[color_image][5])), width=5)
        elif 41 <= t < 82:
            draw.line((x1, y1, x2, y2), fill=(tuple(color_list[color_image][4])), width=4)
            draw.line((x2, y1, x1, y2), fill=(tuple(color_list[color_image][4])), width=4)
        elif 82 <= t < 123:
            draw.line((x1, y1, x2, y2), fill=(tuple(color_list[color_image][3])), width=3)
            draw.line((x2, y1, x1, y2), fill=(tuple(color_list[color_image][3])), width=3)
        elif 123 <= t < 164:
            draw.line((x1, y1, x2, y2), fill=(tuple(color_list[color_image][2])), width=2)
            draw.line((x2, y1, x1, y2), fill=(tuple(color_list[color_image][2])), width=2)
        elif 164 <= t < 205:
            draw.line((x1, y1, x2, y2), fill=(tuple(color_list[color_image][1])), width=1)
            draw.line((x2, y1, x1, y2), fill=(tuple(color_list[color_image][1])), width=1)
        elif 205 <= t <= 255:
            pass
        x1 = x2
        x2 = x2 + large
        if x2 > shirina:
            x1 = 0
            x2 = large
            y1 = y2
            y2 = y2 + large


def check_folder(folder):
    list_values = folder.split("\\")
    list_values.remove(list_values[-1])
    folder = "\\".join(list_values) + "\\"
    return str(folder)

def check_ext(path):
    list_values = path.split(".")
    ext = list_values[-1]
    return ext

#-------------------------------------------------

list_check_ext = ["png", "PNG", "jpg", "JPG"]
list_cell_choice = ["1", "2", "5", "10"]
list_color_choice = ["RANDOM", "red", "blue", "yellow", "green", "brown", "pink", "black", "turquoise", "orange"]

def final_show_img():
    file_load = input("File load location and name file(Example: D:\Photo\yourfile.png): ")
    while os.path.exists(file_load) == False or os.path.isfile(file_load) == False:
        file_load = input(
            "The file in the folder was not found, please re-enter the path and file name(Example: D:\Photo\yourfile.png): ")

    large = input("Select the cell scale - 1, 2, 5 or 10: ")
    while large not in list_cell_choice:
        large = input("You made a mistake. Please select one of the available values:1, 2, 5, 10: ")

    print("Choose a color or write RANDOM. Available color selection: ")
    print(*list_color_choice, sep = ",")
    color_choice_user = input("Your choice color: ")
    while color_choice_user not in list_color_choice:
        print("The color was selected incorrectly. Enter RANDOM or enter the color again from the list: ")
        print(*list_color_choice, sep = ", ")
        color_choice_user = input("Your choice color: ")


    img = Image.open(file_load)
    img2 = img.convert("L")


    size = img.size
    shirina, visota = size
    p1 = list(str(shirina))
    p2 = list(str(visota))
    if p1[-1] != 0:
        p1[-1] = '0'
    if p2[-1] != 0:
        p2[-1] = '0'
    shirina = int(''.join(p1))
    visota = int(''.join(p2))

    print(F"Size pictures {shirina} , {visota}")

    color = img2.load()

    large = int(large)
    x1 = 0
    y1 = 0
    x2 = large
    y2 = large

    img_final = Image.new("RGB", ((shirina), (visota)), (255, 255, 255))
    draw = ImageDraw.Draw(img_final)

    # --------------------------------------

    support_random(shirina, visota, large, color, draw, x1, x2, y1, y2, color_choice_user)

    file_save = input("File save location and name file(Example: D:\Photo\yourfile.png): ")

    while os.path.exists(check_folder(file_save)) == False or check_ext(file_save) not in list_check_ext:
        file_save = input(
            "The folder was not found, please re-enter the path and file name(Example: D:\Photo\yourfile.png): ")

    img_final.save(file_save)
    print(F"File save in: {file_save}")
    time.sleep(2)
    img.close()
    img_final.show()

if __name__ == "__main__":
    final_show_img()