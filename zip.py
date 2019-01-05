'''
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(type(zipped))
#print(len(zipped)) zip class has no len
for li in zipped:
    print (li)
'''

students, subjects = map(int,input().split())

subject_scores = []

for i in range (subjects):
    lis = list(map(float, input().split()))
    subject_scores.append(lis)
#print (subject_scores)

student_subject_scores = zip(*subject_scores)
#print (student_subject_scores)
for lis in student_subject_scores:
    s = 0.0
    #print (lis)
    for score in lis:
        s += score
    print ("%.1f"%(s/subjects))


