import unicodedata
from colorama import init
from colorama import Fore, Back, Style
init()
 
def preformats(string, width, align='<', fill=' '):
    # refer from : https://sarc.io/index.php/development/810-python-print-format-padding
    # use it instead of '.format()'
    count = width - get_print_width(string)
    print(count)
    return {'>': lambda s: fill * count + s,
        '<': lambda s: s + fill * count,
        '^': lambda s: fill * (count / 2) + s + fill * (count / 2 + count % 2) }[align](string)

def get_max_column(column):
    self.cur.excute("select '{}' from todo where 1".format(column))
    columns = self.cur.fetchall()
    return (max(map(get_width,columns)), columns)



def print_table(self):
    _, ids = get_max_column("id")
    id_max = 2
    what_max, whats = get_max_column("what")
    due_max, dues = get_max_column("due")
    category_max, categories = get_max_column("category")
    _, fins = get_max_column("finished")
    fin_max = 1
    
    print("┌",end="")
    print("─",end="") * id_max
    print("┬",end="")
    print("─",end="") * what_max
    print("┬",end="")
    print("─",end="") * due_max
    print("┬",end="")
    print("─",end="") * category_max
    print("┬",end="")
    print("─",end="") * fin_max
    print("┐")
    for i in range(len(ids)):

        print('│',end="")
        print(preformats(str(ids[i]),id_max,'>'))
        print('│',end="")
        print(preformats(whats[i],what_max,'>'))
        print('│',end="")
        print(preformats(dues[i],due_max,'>'))
        print('│',end="")
        print(preformats(categories[i],category_max,'>'))
        print('│',end="")
        print(preformats(str(fins[i]),fin_max,'>'))
        print('│',end="")


    # print("├",end="")
    # print("┼",end="")
    # print("┤",end="")
    # print("└",end="")
    # print("┘")
    # print("┴",end="")

    print("└",end="")print("└",end="")
    print("─",end="") * id_max
    print("┴",end="")
    print("─",end="") * what_max
    print("┴",end="")
    print("─",end="") * due_max
    print("┴",end="")
    print("─",end="") * category_max
    print("┴",end="")
    print("─",end="") * fin_max
    print("┘")
        


def get_width(s):
    s = str(s)
    s_width = 0

    for c in s:
        c_ord = ord(c)
        if (
            (ord('A') <= c_ord <= ord('Z')) or
            (ord('a') <= c_ord <= ord('z')) or
            (ord('0') <= c_ord <= ord('9')) or
            (c in " !?()_-+=@#$%^&*\\/<>,.")
        ):
            s_width += 1
        elif (
            (ord('ㄱ') <= c_ord <= ord('ㅣ')) or
            (ord('가') <= c_ord <= ord('ퟻ'))
        ):
            s_width += 2
            
        else:
            return None
        

    return s_width
print_table()