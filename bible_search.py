'''https://bible.org/chinese/e/download/pdf'''

import re

# FILE="./psalms.txt"
FILE = "./psalms_chinese.txt"
# searches= ["慈愛","讚美", "喜樂", "頌讚", "歌頌", "稱頌", "耶和華", "稱謝", "求你", "苦難", "拯救", ]
# searches= ["(歌\w)+", "(讚\w)+", "(榮耀)", "(喜\w)+", "(\w樂)+", "(救\w)+", "(謝)+", "(苦)+", "(哀)+", "(等)+", "(求)+", "(\w不要\w)+" ]
# searches= ["(等\w)+","(難\w)+","(\w難)+"]
# searches= ["(\w人)+"]
# searches= ["(人)+"]
# searches= ["(求)+"]
# searches= ["求", "人"]
# searches= ["求", "願", "要"]
# searches= ["不要"]
searches= ["稱謝", "讚美", "稱頌"]
searches= ["大衛"]
found = {}
distributions = {}
for search in searches:
    found[search] = {}
    arr = []
    arr = [0 for i in range(151)]
    distributions[search] = arr
with open(FILE, 'r') as f_obj:
    line = f_obj.readline()
    while line != "":
        '''PS|148|13||'''
        for search in searches:
            words = re.findall(search, line)
            chp_verse = re.search("PS\|([\d]+)\|([\d]+)\|",line)
            chp = int(chp_verse.group(1))
            if  chp > 150:
                print("error ! ")
            verse =  int(chp_verse.group(2))
            for word in words:
                if word in found[search]:
                    found[search][word] += 1
                    distributions[search][chp] += 1
                else:
                    found[search][word] = 1
                    distributions[search][chp] = 1
        line = f_obj.readline()
        # f_obj.tell()

    f_obj.close()

for search in searches:
    sorted_found = {k: v for k, v in sorted(found[search].items(), key=lambda item: item[1])}
    frequency = 0
    for k, v in sorted_found.items():
        frequency += v
    print(f"{search}:,{sorted_found}")
    print(f"total phrases: {len(found[search])}, total frequency: {frequency}")

for search in searches:
    print("{}:".format(search))
    print("{},".format(distributions[search]))
    # for i in range(len(distributions[search])):
    #     print("{},".format(distributions[search][i]), end='')
    # print("")
'''
{'拯救': 3, '頌讚': 4, '歌頌': 7, '慈愛': 7, '讚美': 11, '求你': 32, '耶和華': 89}
{('求壽',): 1, ('求和',): 1, ('求良',): 1, ('求困',): 1, ('求問',): 1, ('求了',): 1, ('求過',): 1, ('求奸',): 1, ('求達',): 1, ('求平',): 1, ('求我',): 2, ('求恩',): 2, ('求他',): 2, ('求福',): 2, ('求；',): 3, ('求食',): 3, ('求其',): 4, ('求。',): 6, ('求神',): 9, ('求，',): 9, ('求的',): 9, ('求主',): 12, ('求告',): 29, ('求耶',): 30, ('求你',): 286}

'''