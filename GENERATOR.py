import random


def users_gen():
    a= 'insert into users(name,last_name,birth_day,registration_date,login,password)  values'
    letsnanums='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    print('henlo to generator')
    print('names gen...')
    c = ['( ' for i in range(25)]
    for i in range(25):
        b = alter_names_gen()
        c[i]+="'"+b[0]+"', '"+b[1]+"', "
    
        
    print('use date for bday gen or insert manually?(y/n)')
    bbbbb = input()
    if bbbbb=='y':
            for i in range(25):
                b = alter_date_gen()
                c[i]+="'"+b+"', "

    else:
        for i in range(25):
            b = input()
            c[i]+="'"+b+"', "
            
    print('use date for reg date gen or insert manually?(y/n)')
    bbbbb = input()
    if bbbbb=='y':
            for i in range(25):
                b = alter_date_gen()
                c[i]+="'"+b+"', "

    else:
        for i in range(25):
            b = input()
            c[i]+="'"+b+"', "

        
    s = len(letsnanums)-1
    print('gen logins...')
    for i in range(25):
        n = random.randint(5,16)
        log = "'"
        for j in range(n):
            log+= letsnanums[random.randint(0,s)]
        log+="', "
        c[i]+=log
    print('gen passwords...')
    for i in range(25):
        n = random.randint(5,16)
        log = "'"
        for j in range(n):
            log+= letsnanums[random.randint(0,s)]
        log+="'),  "
        c[i]+=log
    print('use file for output?(y/n)')
    bbbbb = input()
    if bbbbb=='y':
        print('input file name')
        cc = input()
        cc+='.txt'
        with open(cc,'w') as obj:
            print('='*20,file=obj)
            print('created by bd gen',file=obj)
            print('='*20,file=obj)
            print(*c,file=obj)
    else:
        print(*c)
            
def goods_gen():
    names=[['Black','Blue','Gray','Green','Orange','Pink','Purple','Red','White','Yellow','Cyan','Lavander'],
           ['bone china','porcelain','steal','stoneware','melamine','vitrified glass','plastic'],
           ['spoon','fork','mug','cup','coffee cup','teacup','plate','teaspoon','bowl','teapot','pitcher','eggcup','wine glass','tumbler','naplin ring','side plate','small fork','dinner plate','soub bowl','knife'],
           ['"Lalar"','"Carelerd"','"Uca"','"Pion"','"Pikampal"','"Frded"','"Mondorena"','"Vany"','"Hartoro"','"Ero"','"Lerro"']]
    c = ["( '" for i in range(25)]
    for i in range(25):
        c[i]+=random.choice(names[0])+' '+random.choice(names[1])+' '+random.choice(names[2])+' '+random.choice(names[3])+"', "+str(random.randint(100,1000))+', '+str(random.randint(40, 2000))+"), "
    print(*c)


def alter_names_gen():
    names = []
    surnames = []
    with open('gen_names.txt','r') as obj:
        b = obj.readline()
        while b:
            
            names.append(b.split()[0])
            surnames.append(b.split()[1])
            b = obj.readline()
    return [random.choice(names),random.choice(surnames)]

def alter_date_gen():
    a = str(random.randint(1970,2021))+'-'+str(random.randint(1,12)).zfill(2)+'-'+str(random.randint(1,31)).zfill(2)
    return a

users_gen()
