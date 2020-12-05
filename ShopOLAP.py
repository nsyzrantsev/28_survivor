# https://skillsmart.ru/algo/lvl1/b519.html

def CatalogMaker(items):
    catalog = dict()
    for line in items:
        data = line.split()
        product = data[0]
        count = int(data[1])
        if product not in catalog:
            catalog[product] = count
        else:
            catalog[product] += count
    return catalog

def ReversedCatalog(catalog):
    reversed_catalog = dict()
    for k, v in catalog.items():
        if v not in reversed_catalog:
            reversed_catalog[v] = [k]
        else:
            reversed_catalog[v].append(k)
        reversed_catalog[v].sort()
    return reversed_catalog

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
    reversed_catalog = ReversedCatalog(catalog)
    return Output(reversed_catalog)

# items = ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']
# items1 = ["dress1 5", "handbug32 3", "handbug32 3", "dress2 1", "dress2 5", "handbug23 2", "handbug128 4"]
# print(ShopOLAP(6, items1))
