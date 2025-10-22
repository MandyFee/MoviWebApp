#def analyze_logs(path):
    #with open(path) as f:
        #for line in file:
            #timestamp, code = line.strip().split()
            #file[code] = file.get(code, 0)
   #return file
#from collections import Counter
#assert analyze_logs('logs.txt') == {'200': 2, '404': 1}
path=[
"2025-04-01T10:00:00 - 200",
"2025-04-01T10:01:00 - 404",
"2025-04-01T10:02:00 - 200",
]
def analyze_logs():
    counts = {}
    for line in path:
      timestamp, code = line.strip().split(" - ")
      counts[code] = counts.get(code, 0) +1
    return counts

assert analyze_logs() == {'200':2, '404':1}
print(analyze_logs())


