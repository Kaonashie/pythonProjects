listNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def create_phone_number(n):
    e = ''.join(str(n) for n in listNumbers)
    e = "(" + e[0:3] + ")" + " " + e[3:6] + "-" + e[6:] 
    print(e)
    
    
create_phone_number(listNumbers)