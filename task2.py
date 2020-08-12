def odometer(data):
    if len(data) < 2 or len(data) % 2 != 0:
        return 'Ошибка количества данных'
    
    distance = 0
    i = 1
    while i < len(data):
        speed = data[i]
        if i >= 2:
            time = data[i-1] - data[i-3]
        else:
            time = data[i-1]
        distance += speed*time
        i += 2
    return distance
