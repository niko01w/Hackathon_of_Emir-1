import json


FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)
        

def get_retrieve_data():
    data = get_data()
    id = int(input('введите id продукта '))
    element = filter(int(filter(lambda x: x['id'] == id, data)))
    return element[0]


def get_create_data():
    data = get_data()
    try:
        data.append({
            'id':input('введите id продукта'),
            'marka':input('ведите марку: '),
            'model':input('введите модель:'),
            'years': int(input('год выпуска:')),
            'opisanie': input('описание :'),
            'price': round(float(input('введите цену')),2)

    })
    except ValueError:
        print('Введите корректные данные!')
        get_create_data()
    else:
        with open(FILE_PATH,'w') as file:
            json.dump(data,file , indent= 2)
    return 'CREATED'

def get_update_data():
    data = get_data()
 
    id = int(input('введите id продукта: '))
   
    update = list(filter(lambda x:x['id'] == id ,data ))

    if not update:
        return '====================================|\nнеи такого продукта\n====================================|'
    
    index_ = data.index(update[0])
   
    data[index_]['marka'] = input('====================================|\nвведите новое название продукта :')
    data[index_]['model'] =  input('====================================|\nвведите новое название продукта :')
    data[index_]['price'] = round(float(input('====================================|\nвведите новую цену на продукт:'))),2


    with open (FILE_PATH , 'w') as file:
        json.dump(data , file)
        return '====================================|\nUPDATED\n====================================|'


def get_delete_data():
    data = get_data()
    id = int(input('введите id:'))
    delete = list(filter(lambda x:x['id'] == id , data ))
    if not delete:
        return 'нет такого продукта'
    index_ = data.index(delete[0])
    data.pop(index_)
    json.dump(data , open(FILE_PATH, 'w'))
    return 'DELETED'


