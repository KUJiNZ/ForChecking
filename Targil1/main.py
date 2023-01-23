import os

from connection import Connection
from utilities import Utilities
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    server_name = os.getenv('SERVER_NAME')
    os.chdir('D:\\Sources')
    #server_name = 'DESKTOP-P0JMAVF\SQLEXPRESS'
    c = Connection().server_connect(server_name)
    cursor = c.cursor()

    name = input('Enter name to search: ')
    id_by_name = Utilities().show_id_by_name(cursor,name)
    print(id_by_name)

    id_to_show = input('Enter id to search: ')
    ls = Utilities().show_list_by_id(cursor,id_to_show)
    sum = Utilities().count_all_orders(ls)
    print(sum)