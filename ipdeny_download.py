import requests

f = open('countries.txt', 'r')
ips = "";

for country in f:
	code = country.replace('\n', '')
	url = 'https://www.ipdeny.com/ipblocks/data/countries/'+code+'.zone'
	print('downloading '+ code + ': ' + url)
	x = requests.get(url)
	print('downloaded '+str(len(x.text.split('\n')))+' ips')
	ips += x.text
	
	
f.close()
print("writing to blocked.txt")
out = open("blocked.txt", "w")
out.write(ips)
out.close()
print("done cya")
