"""
int FindMinInsert(string s, int l, int r)
{ if ( l &gt;= r ) return 0;
     if (s[l] == s[r]) return FindMinInsert(s, l+1, r-1);
     int insert_left = FindMinInsert(s, l, r-1) +1;
     int insert_right = FindMinInsert(s, l+1, r) +1;
     return min(insert_left, insert_right);
}
"""

def  FindMinInsert(s,  l,  r, lists, lis):

    if  l >= r:
        print (lis)
        lists.append(lis[:])
        return 0
    if s[l] == s[r]:
        lis.append(s[l])
        ret = FindMinInsert(s, l+1, r-1, lists, lis)
        lis.pop()
        return ret
    new_lis = lis[:]
    new_lis.append(s[r])
    new_lis.append("-")
    insert_left = FindMinInsert(s, l, r-1, lists, new_lis) +1
    lis.append(s[l])
    lis.append("+")
    insert_right = FindMinInsert(s, l+1, r, lists, lis) +1
    return min(insert_left, insert_right)

lists = []
s = "1234542"
lis =[]
result = FindMinInsert(s, 0, len(s)-1, lists, lis)
print (result)