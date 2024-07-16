from pathlib import Path

def get_cats_info(path):
     
    try:
        with open(path, 'r', encoding='UTF-8') as cats:
            list_cats = []
            for line in cats:
                dic_cat = {
                    'id': line.split(',')[0],
                    'name': line.split(',')[1],
                     'age': line.split(',')[2].strip()
                     }
                list_cats.append(dic_cat)
    except FileNotFoundError:
        print (f'Your path {path} is wrong')
    return list_cats

print(get_cats_info('HW4/cats.txt'))
