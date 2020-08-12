def odometer(data):
    if len(data) < 2 or len(data) % 2 != 0:
        return 'Ошибка количества данных'
    
    distance = 0
    i = 1
    while i < len(data):
        speed = data[i-1]
        if i >= 3:
            time = data[i] - data[i-2]
        else:
            time = data[i]
        distance += speed*time
        i += 2
    return distance
