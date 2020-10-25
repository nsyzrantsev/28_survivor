# https://skillsmart.ru/algo/lvl1/l1e7.html

def PrintingCosts(line):
    toner_dict = {' ': 0,
                  "'`": 3,
                  '.': 4,
                  '"': 6,
                  ',-^': 7,
                  ':_': 8,
                  '!~': 9,
                  '>\\/<': 10,
                  ';': 11,
                  '(|)': 12,
                  'vrx+': 13,
                  'Y': 14,
                  '?i': 15,
                  'Ll': 16,
                  'tcu*': 17,
                  'J{X}fI[': 18,
                  'Vz1': 19,
                  'oFjC': 20,
                  'hK4ks': 21,
                  '20Z%m': 22,
                  '8P3eUa': 23,
                  '&Ay': 24,
                  'bdpGSqHN': 25,
                  'D9W6O': 26,
                  '5': 27,
                  'RM': 28,
                  '$B': 29,
                  'g': 30,
                  'Q': 31,
                  '@': 32
                }
    cons_list = list()
    for j in line:
        for key, value in toner_dict.items():
            for i in key:
                if i == j:
                    cons_list.append(value)
    toner = 0
    for i in cons_list:
        toner += i
    if len(cons_list) < len(line):
        toner += (len(line) - len(cons_list))*23
    return toner
