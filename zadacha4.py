#Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.

with open('sp.txt', 'r') as url:
    fileStr = url.read()
    s = fileStr.split('\n')
    g = list(map(lambda x: x.split('.'), s))

    for f in g:
        print(f[1])        
