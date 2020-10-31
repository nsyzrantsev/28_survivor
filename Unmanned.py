# https://skillsmart.ru/algo/lvl1/a9d8.html

def wait_time(time, wait, light):
    wait = light[1] - (time+wait)%(light[1]+light[2])
    return wait

def check_position(light, L):
    if light[0] > L:
        return False
    return True

def Unmanned(L, N, track):
    time = 0
    error_count = 0
    last_light = 0
    all_wait = 0
    for light in track:
        if not check_position(light, L):
            error_count += 1
            continue
        time += light[0] - last_light
        wait_t = wait_time(time, all_wait, light)
        if wait_t > 0:
            all_wait += wait_t
        last_light = light[0]
    if error_count == N:
        return L
    time += L - track[-1][0]
    return time + all_wait
