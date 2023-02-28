from requests import get
from bs4 import BeautifulSoup

base_url = "https://remoteok.com/remote"
search_term = 'react'

response = get(f"{base_url}-{search_term}-jobs", headers={"User-Agent": "1"})

if response.status_code != 200:
    print("Can't request website")
else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    jobs = soup.find_all('tr', class_='job')
    # print(jobs)

    for job_section in jobs:
        companyLink = job_section.find_all('span', class_="companyLink")

        names = companyLink[0]
        #name = names.find('h3').string
        name = names.get_text(strip=True)

        company_position = job_section.find_all('td', class_="company")
        positions = company_position[0]
        position = positions.find('h2').get_text(strip=True)

        etc = []
        data = job_section.find_all('div', class_="location")
        for datas in data:
            etc.append(datas.string)
        job_data = {
            'company' : name,
            'position' : position,
            'etc' : etc}
        results.append(job_data)

    for i in results:
        print(i)
        print('\n\n\n\n\n')