import json
from views import *
from register import *

class User(RegisterMixin, LoginMixin):
    pass

class MoTOR(RetrieveMixin, CreateMixin,UpdateMixin,DeleteMixin,ListingMixin):
   
    def MOtor(self):
         print('что вы хотите сделать?')

         while True:
            operation = input('====================================|\nCREATE - для создания записей       | \n====================================| \nLISTING для получения списка записей| \n====================================| \nRETRIEVE для получения одной записи | \n====================================|\nUPDATE для обновления записей       | \n====================================|\nDELETE для удаления записей         | \n====================================|\n ВВЕДИТЕ ДЕЙСТВИЕ : ')
            print('====================================|')
            if operation.upper()== 'CREATE':
                print(super().get_create_data())
    
            elif operation.upper() == 'LISTING':
                print(super().listing_products())
    
            elif operation.upper() == 'RETRIEVE':
                print(super().get_retrieve_data())
            
            elif operation.upper() == 'UPDATE':
                print(super().get_update_data())

            elif operation.upper() == 'DELETE':
                print(super().get_delete_data())
            else:
                print('проверьте правильно ли вы написали')

the_best_user = User()
the_best_user.registr()


a = MoTOR()
a.MOtor()