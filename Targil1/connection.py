import pyodbc
from Targil1 import log
class Connection:
    fn = log.Log()
    def server_connect(self,server_name):
        """
        Name: Artiom
        Date: 18.1.23
        Decription: server_connect() used to connect to DB
        Input:None
        Output: Connection
        :return: conn
        """

        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=DESKTOP-P0JMAVF\SQLEXPRESS;'
                                  'Database=Targil1;'
                                  'Trusted_Connection=yes;')
            self.fn.print_log(self.server_connect.__doc__)
            return conn
        except Exception as e:
            self.fn.print_error(e, self.server_connect.__doc__)