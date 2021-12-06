from pprint import pprint
with open('recipes.txt', encoding='utf-8') as r:   # превращаем csv.reader в список
    ls = r.readlines()
    lb = []
for i in ls:
    lb.append(i.strip())
cook_book = {}
for id, i in enumerate(lb):
    if i.isdigit():
        cook_book[lb[id-1]] = []
        for g in lb[id+1:id+int(i)+1]:
            cook_book[lb[id-1]].append({'ingredient_name': g.split("|")[0], 'quantity': g.split("|")[1], 'measure': g.split("|")[2]})
pprint(cook_book)
