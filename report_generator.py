import sys
import re
import os

''' 
input file sample:
[valhalla_route_calculation_la_boundary] Valhalla Diagnostic) Boundary: la_boundary |
Requested: 99 | Successful: 99 | Failed: 0 | BiasIterFwd: 464.15 | BiasIterBwd:
601.01 | UnbiasIterFwd: 7457.08 | UnbiasIterBwd: 8597.42 

[la_boundary] Routing) Boundary: la_boundary | Requested: 5502 | Successful: 5494 |
Failed: 8 | Match pct: 84.86

[la_boundary] Guidance) Boundary: la_boundary | Total: 5494 | Steps Failed Count: 806
| Unnamed Start Count: 68 | Unnamed Middle Count: 61 | Unnamed Mid Short Count: 29 |
Unnamed Mid Medium Count: 13 | Unnamed Mid Long Count: 24 | Unnamed End Count: 93 |
Unnamed Verbal Count: 97

[la_boundary] Angles) Boundary: la_boundary | Total routes: 2199 | Total turns
compared: 11376 | Mismatches: 155 | Mismatch pct: 1.36 | Skipped: 12424 
'''


parser = {"Valhalla Diagnostic": {"Total":"(?<=Requested: )\d+", "Pass":"(?<=Successful: )\d+", "Fail": "(?<=Failed: )\d+", "Rate":0},
         "Routing":    {"Total":"(?<=Requested: )\d+", "Pass":"(?<=Successful: )\d+", "Fail": "(?<=Failed: )\d+", "Rate":0},
         "Guidance": {"Total":"(?<=Total: )\d+","Pass":None, "Fail": "(?<=Steps Failed Count: )\d+", "Rate":0},
         "Angles": {"Total":"(?<=Total turns compared: )\d+","Pass":"(?<=Total turns compared: )\d+", "Fail": "(?<=Mismatches: )\d+", "Rate":0}
}

if len(sys.argv) !=3 :
    #print help
    p,n = os.path.split(sys.argv[0])
    print ("Usage: {} ".format(n))
    print ("{} input output ".format(n))
    print ("input:   Valhalla log")
    print ("output:  Summary report in CSV format")
    exit (0)



in_file=open(sys.argv[1], "r")
line = in_file.readline()
while line != "" :
    k = re.search(r'(?<=\] ).+(?=\))', line).group(0)
    if k in parser:
        t = 0
        p = 0
        f = 0
        r = -1
        if parser[k]["Total"]:
            t = int(re.search (parser[k]["Total"], line).group(0))
        if parser[k]["Pass"]:
            p = int(re.search (parser[k]["Pass"], line).group(0))
        if parser[k]["Fail"]:
            f = int(re.search (parser[k]["Fail"], line).group(0))
        if p==0 and t !=0 and f !=0:
            p = t -f
        if t !=0 :
            r = p * 100 // t
        parser[k]["Rate"] = r
    line = in_file.readline()
    in_file.tell()
in_file.close()


with open(sys.argv[2], 'w') as csv_file:
    csv_file.write("Category\tSuccess Rate\n")
    for k, v in parser.items():
        csv_file.write( "{}\t{}\n". format(k, v["Rate"]))
    csv_file.close()


