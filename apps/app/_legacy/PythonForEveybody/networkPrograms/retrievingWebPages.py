import urllib.request

url = 'http://data.pr4e.org/romeo.txt'
fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())
