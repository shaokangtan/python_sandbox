engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers           # union
engineering_management = engineers & managers            # intersection
fulltime_management = managers - engineers - programmers # difference
engineers.add('Marvin')                                  # add element
print (engineers)
#set(['Jane', 'Marvin', 'Janice', 'John', 'Jack'])
print (employees.issuperset(engineers))     # superset test
#False
employees.update(engineers)         # update from another set
print (employees.issuperset(engineers))
#True
for group in [engineers, programmers, managers, employees]:
    group.discard('Susan')          # unconditionally remove element
    print (group)
#set(['Jane', 'Marvin', 'Janice', 'John', 'Jack'])
#set(['Janice', 'Jack', 'Sam'])
#set(['Jane', 'Zack', 'Jack'])
#set(['Jack', 'Sam', 'Jane', 'Marvin', 'Janice', 'John', 'Zack'])