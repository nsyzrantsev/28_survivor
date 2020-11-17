# https://skillsmart.ru/algo/lvl1/b519.html

def CatalogSort(catalog):
    result = list()
    for k, v in catalog.items():
        line = f'{k} {v}'
        result.append(line)
    result = sorted(result)
    return result

def CatalogMaker(items):
    catalog = dict()
    for i, line in enumerate(items):
        name = line.split()[0]
        num = int(line.split()[1])
        if name in catalog:
            catalog[name] += num
        else:
            catalog[name] = num
    return catalog

def ShopOLAP(N, items):
    catalog = CatalogMaker(items)
    sorted_catalog = CatalogSort(catalog)
    return sorted_catalog
