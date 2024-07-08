from pathlib import Path

def get_cats_info(path):
    dic_cat = {}
    list_cats =[]
    try:
        with open(path, 'r', encoding='UTF-8') as cats:
            for line in cats:
                list_cats = [line.split(',')]
                for el in list_cats:
                    dic_cat = {'id': el[0],'name': el[1], 'age': el[2].strip()}
                    print(dic_cat)
    except FileNotFoundError:
        print (f'Your path {path} is wrong')

print(get_cats_info('./HW4/cats.txt'))
