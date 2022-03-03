import requests
from bs4 import BeautifulSoup

URL = "https://www.singaporepools.com.sg/en/product/Pages/toto_wnf.aspx"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="number-frequency")
#print(results.prettify())
raw = []
for result in results.find_all('td'):
    raw.append(int(result.text))
    # need .text to append only the digits

#print(raw)# for milestone check

balls =[]
freq = []
extra = []

for b in range(0,len(raw),3):
    balls.append(raw[b])

for f in range(1,len(raw),3):
    freq.append(raw[f])

for e in range(2,len(raw),3):
    extra.append(raw[e])

#print(balls)
#print(freq)
#print(extra)

def max_6(l):
    work_lst = l.copy()
    # must .copy or else original list will be popped
    sort_liao = sorted(l)
    big_6 = sort_liao[-6:]
    print("most freq n:", big_6)
    idx_list = []
    for f in big_6:
        idx = work_lst.index(f)
        work_lst[idx] = "took"
        idx_list.append(idx)
    print(idx_list, "are indexes of most freq n")
    return idx_list

def min_6(l):
    work_lst = l.copy()
    # must .copy or else original list will be popped
    sort_liao = sorted(l)
    small_6 = sort_liao[:6]
    print("least freq n:",small_6)
    idx_list = []
    for s in small_6:
        idx = work_lst.index(s)
        work_lst[idx] = "took"
        idx_list.append(idx)
    print(idx_list, "are indexes of least freq n")
    return idx_list

def jackpot_n(idx_lst,balls):
    winning_n = []
    for i in idx_lst:
        winning_n.append(balls[i])
    winning_n.sort()
    return winning_n

#print(len(freq))
print("most freq 6 numbers:", jackpot_n(max_6(freq),balls))
print()
#print("any change in freq list?", len(freq))
print("least freq 6 numbers:",jackpot_n(min_6(freq),balls))


