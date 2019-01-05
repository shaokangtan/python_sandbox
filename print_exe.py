# referecne: https://pyformat.info/
#            http://thomas-cokelaer.info/tutorials/python/print.html


"""basic"""
print ('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
#attribute: use {: attribute } to assign the attribute to the output,
#           such as type(d,f,o,x), width(w.p), precision, alignment(^,<,>)
print("octol {:o} hex {:x}".format(12345,12345))
#center align ^
print('{:^10}'.format('test'))
#left align <
print('{:10}'.format('test'))
print('{:_<10}'.format('test'))
#right align >
print('{:>10}'.format('test'))
#truncating
print('{:.5}'.format('xylophone'))

data = {'first': 'Hodor', 'last': 'Hodor!'}
print ('{first} {last}'.format(**data))

"""accessing data structure"""
person = {'first': 'Jean-Luc', 'last': 'Picard'}
print ('{p[first]} {p[last]}'.format(p=person))
data = [4, 8, 15, 16, 23, 42]
print ('{d[4]} {d[5]}'.format(d=data))
class Plant(object):
    type = 'tree'
print ('{p.type}'.format(p=Plant()))

from datetime import datetime
print ('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))
dt = datetime(2001, 2, 3, 4, 5)
print ('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))

print ('{:{align}{width}}'.format('test', align='^', width='10'))
print ('{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3))
print ('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2))