from views import *

print('что вы хотите сделать?')

while True:
    operation = input('====================================|\nCREATE - для создания записей       | \n====================================| \nLISTING для получения списка записей| \n====================================| \nRETRIEVE для получения одной записи | \n====================================|\nUPDATE для обновления записей       | \n====================================|\nDELETE для удаления записей         | \n====================================|\n ВВЕДИТЕ ДЕЙСТВИЕ : ')
    print('====================================|')
    if operation == 'CREATE':
        print(get_create_LISTING())
   
    elif operation == 'LISTING':
        print(get_LISTING())
   
    elif operation == 'RETRIEVE':
        print(get_retrieve_LISTING)
    
    elif operation == 'UPDATE':
        print(get_update_LISTING())

    elif operation == 'DELETE':
         print(get_delete_LISTING())
    else:
        print('проверьте правильно ли вы написали')