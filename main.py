import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def fetch_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def parse_atcoder_contests(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    contests = soup.find('div', id = 'contest-table-upcoming')
    title = contests.h3.text
    print(title)
    tbody = contests.tbody.find_all('tr')
    td_inside = []
    for tr in tbody:
        td_inside.append(tr.find_all('td'))
    
    Time = []
    Contest_name = []
    Durations = []
    Rated_range = []
    for element in td_inside:
        Time.append(element[0].a.time.text)
        Contest_name.append(element[1].a.text)
        Durations.append(element[2].text)
        Rated_range.append(element[3].text)
    
    data = [
    ["Start Time (local time)", "Contest Name", "Duration","Rated Range"],
    ]

    for i in range(len(tbody)):
        contests = []
        contests.append(Time[i])
        contests.append(Contest_name[i])
        contests.append(Durations[i])
        contests.append(Rated_range[i])
        data.append(contests)
        
    
    return data

def parse_codeforces_contests(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    contests = soup.find('div', class_ = 'datatable')
    internal_div = contests.find_all('div')
    contest_rows = internal_div[6].table.find_all('tr')
    del contest_rows[0]
    tr_inside = []
    for tr in contest_rows:
        tr_inside.append(tr.find_all('td'))
    
    titles = []
    time = []
    length = []
    for trs in tr_inside:
        titles.append(trs[0].text)
        time.append(trs[2].a.text)
        length.append(trs[3].text)
    
    codeforce_data = [
        ['Name','Time','Length']
    ]
    
     
    for i in range(len(tr_inside)):
        new_contest = []
        new_contest.append(titles[i])
        new_contest.append(time[i])
        new_contest.append(length[i])
        codeforce_data.append(new_contest)
        
    return codeforce_data

def print_table(title, data):
    print(title.center(120))
    table = tabulate(data, headers="firstrow", tablefmt="grid")
    print(table)

# Fetch AtCoder data
atcoder_url = "https://atcoder.jp/contests/"
atcoder_html_result = fetch_html_content(atcoder_url)
if atcoder_html_result is not None:
    atcoder_data = parse_atcoder_contests(atcoder_html_result)
    print_table("ATCODER", atcoder_data)
else:
    print("ERROR WHILE FETCHING ATCODER")

# Fetch Codeforces data
codeforces_url = 'https://codeforces.com/contests'
codeforces_html_result = fetch_html_content(codeforces_url)
if codeforces_html_result is not None:
    codeforces_data = parse_codeforces_contests(codeforces_html_result)
    print_table("CODEFORCES", codeforces_data)
else:
    print("ERROR WHILE FETCHING CODEFORCES")

