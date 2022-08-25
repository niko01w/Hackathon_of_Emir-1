from views import *

print('что вы хотите сделать?')

while True:
    operation = input('====================================|\nCREATE - для создания записей       | \n====================================| \nLISTING для получения списка записей| \n====================================| \nRETRIEVE для получения одной записи | \n====================================|\nUPDATE для обновления записей       | \n====================================|\nDELETE для удаления записей         | \n====================================|\n ВВЕДИТЕ ДЕЙСТВИЕ : ')
    print('====================================|')
    if operation.upper()== 'CREATE':
        print(get_create_data())
   
    elif operation.upper() == 'LISTING':
        print(get_data())
   
    elif operation.upper() == 'RETRIEVE':
        print(get_retrieve_data())
    
    elif operation.upper() == 'UPDATE':
        print(get_update_data())

    elif operation.upper() == 'DELETE':
         print(get_delete_data())
    else:
        print('проверьте правильно ли вы написали')
        