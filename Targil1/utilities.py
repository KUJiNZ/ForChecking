from log import Log
class Utilities:
    def create_tables(self,cursor, table_name):
        cursor.execute('''
                CREATE TABLE ? (
                    id int primary key,
                    name nvarchar(50),
                    city nvarchar(50)
                    )
                       ''', (table_name))
        cursor.commit()

        cursor.execute('''
                    CREATE TABLE orders (
                        id int,
                        cust_id int FOREIGN KEY REFERENCES Cust (id),
                        date date,
                        sum int
                        )
                           ''')
        cursor.commit()

    def show_id_by_name(self,cursor, name):
        """
               Name: Artiom
               Date: 18.1.23
               Decription: Showing id by inputed name
               Input:None
               Output: None
               :return: ID
               """
        try:
            cursor.execute("""
                            SELECT id
                            FROM cust
                            Where name = ?;
                            """, (name))
            ID = cursor.fetchall()
            cursor.commit()
            Log().print_log('show_list_by_name')
            return ID
        except Exception as e:
            Log().print_error(e, 'show_id_by_name')

    def show_list_by_id(self,cursor, id):
        """
                       Name: Artiom
                       Date: 18.1.23
                       Decription: Showing orders by inputed id
                       Input:None
                       Output: None
                       :return: records
                       """
        try:
            cursor.execute("""
                            SELECT *
                            FROM Orders as o
                            INNER JOIN Cust as c
                            ON o.cust_id = c.id
                            Where cust_id = ?;
                            """, (id))
            records = cursor.fetchall()
            for row in records:
                row = tuple(row)
            cursor.commit()
            Log().print_log('show_list_by_id')
            return records
        except Exception as e:
            Log().print_error(e, 'show_list_by_id')

    def count_all_orders(self,ls):
        """
               Name: Artiom
               Date: 18.1.23
               Decription: Counting sum or orders
               Input:None
               Output: sum
               :return: ID
               """
        try:
            sum = 0
            ls = self.pyodbc_row_to_list(ls)
            for i in range(len(ls)):
                sum += int(ls[i][3])
            Log().print_log('count_all_orders')
            return sum
        except Exception as e:
            Log().print_error(e, 'count_all_orders')

    def pyodbc_row_to_list(self,ls):
        """
                       Name: Artiom
                       Date: 18.1.23
                       Decription: Converting odbc rows in list to list of lists
                       Input:None
                       Output: None
                       :return: ID
                       """
        try:
            lst = []
            for row in ls:
                lst.append(list(row))
            Log().print_log('pyodbc_row_to_list')
            return lst
        except Exception as e:
            Log().print_error(e, 'pyodbc_row_to_list')