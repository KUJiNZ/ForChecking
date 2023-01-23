from datetime import datetime

class Log:
    def print_error(self,e, fn_desc):
        now = datetime.now()
        f = open('log.txt', 'a')
        f.writelines(f'\nError: {e}\nFunction description:{fn_desc}\nDate:{now}')
        f.flush()
        f.close()

    def print_log(self,fn_desc):
        """
                 Name: Artiom
                 Date: 18.1.23
                 Description: Printing Successful Log
                 Input: e(Exception)s
                 Output: Log
                 :return: conn
                 """
        now = datetime.now()
        f = open('log.txt', 'a')
        f.writelines(f'\nSuccess:{fn_desc}\t\nDate:{now}\n')
        f.flush()
        f.close()


