
class Orders:

    order_list = {'Pizza':'1',
        'Noodles':'2',
        'Rice':'3',
        'Poutine':'4',
        'Pasta':'5'
        }
    message_template = 'I want to order for {1} {0}.'


    def random_message(self):
        key = list(self.order_list.keys())[0]
        value = self.order_list[key]
        return self.message_template.format(key,value)

print(Orders().random_message())

