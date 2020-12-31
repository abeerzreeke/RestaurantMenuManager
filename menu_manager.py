import json

class MenuManager:
     
     def __init__(self):
          with open("menu.json", "r+") as file_obj:
               self.menu_restaurant = json.load(file_obj)

     def add_item(self,name, price):
          self.name = name
          self.price = price
          new_item = {
               'name': name,
               'price': price
          }

          for item in self.menu_restaurant['items']:
               if item['name'] == name:
                    print('Item already exists')
                    return
          self.menu_restaurant['items'].append(new_item)

     def remove_item(self,name):

          self.name = name
          for item in self.menu_restaurant['items']:
               if item['name'] == name:
                    list_items = self.menu_restaurant['items']
                    index_item = list_items.index(item)
                    del self.menu_restaurant['items'][index_item]
                    return True
          return False

     def save_to_file(self):

          with open('menu.json', 'w') as file_obj:
               json.dump(self.menu_restaurant, file_obj, indent = 2)
               return self.menu_restaurant['items']



