# https://skillsmart.ru/algo/lvl1/b519.html

def CatalogMaker(items):
    catalog = dict()
    for line in items:
        data = line.split()
        product = data[0]
        count = data[1]
        if count not in catalog:
            catalog[count] = [product]
        else:
            catalog[count].append(product)
        catalog[count].sort()
    return catalog    

def Output(catalog):
    result = list()
    keys_list = list(catalog.keys())
    keys_list.sort(reverse=True)
    for count in keys_list:
        for product in catalog[count]:
            line = f'{product} {count}'
            result.append(line)
    return result

def ShopOLAP(N, items):
    catalog = CatalogMaker(items)
    return Output(catalog)

# items = ['платье1 6', 'сумка128 4', 'сумка23 2', 'сумка32 2']
# items1 = ["dress1 5", "handbug32 3", "dress2 1", "handbug23 2", "handbug128 4"]
# print(ShopOLAP(5, items1))
