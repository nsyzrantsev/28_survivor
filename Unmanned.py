# https://skillsmart.ru/algo/lvl1/a9d8.html

def Unmanned(L, N, track):
    time = 0
    old_light = 0
    for i in track:
        new_light = i[0]
        red = i[1]
        green = i[2]
        time += new_light - old_light
        if red > new_light:
            time += red - new_light
        old_light = new_light
    if track[-1][0] < L:
        time += L - track[-1][0]
    return time
