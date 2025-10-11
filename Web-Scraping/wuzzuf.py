import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


job_title = []
location = []
skills = []
company_name = []
links = []
salary = []
responsibilities = []
date = []

page_num = 0
while True:
    try:
# use requests to fetch the url 
        result =  requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}")

        # save page content 
        src = result.content

        # create soup object to parse content
        soup = BeautifulSoup(src,"lxml")
        page_limit = int(soup.find("strong").text)
        if (page_num > page_limit // 15):
            print("pages ended")
            break
        # find all the elements containing the info we need
        # job titles , job skills , company names , location names
        job_titles = soup.find_all("h2" , {"class" : "css-m604qf"})
        company_names = soup.find_all("a" , {"class" : "css-17s97q8"})
        location_names = soup.find_all("span" , {"class" : "css-5wys0k"})
        job_skills = soup.find_all("div" , {"class" : "css-y4udm8"})
        posted_new = soup.find_all("div",{"class" : "css-4c4ojb"})
        posted_old = soup.find_all("div",{"class" : "css-do6t5g"}) 
        posted = [*posted_new , *posted_old]
    # print(job_titles)
    # print(company_name)
    # print(location_names)
    # print(job_skills)

    # loop over returned lists to extrract needed info into other lists
        for i in range (len(job_titles)):
            job_title.append(job_titles[i].text)
            links.append(job_titles[i].find("a").attrs["href"])
            location.append(location_names[i].text)
            skills.append(job_skills[i].text)
            company_name.append(company_names[i].text)
            date.append(posted[i].text)

        page_num += 1 
        print("page switched ")
    except:
        print("error occured ")
        break 
# for link in links: 
#     result =  requests.get(link)
#     src = result.content
#     soup = BeautifulSoup(src,"lxml")
#     #salaries = soup.find("span", {"class":"css-4xky9y"})
#     #salary.append(salaries.text.strip())
#     responsibilities = soup.find("div", {"class":"css-1t5f0fr"}).ul
#     respon_text =" "
#     for li in responsibilities.find_all("li"):
#         respon_text += li.text + " | "
#     respon_text = respon_text[:-2]

#     responsibilities.append(respon_text)
 


#print(job_title)
#print(company_name)
#print(location)
#print(skills)

# create a csv file and fill it with values 
file_list = [job_title,company_name,date,location,skills,links]
exported = zip_longest(*file_list)
with open("jobtest.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job_title","company_name" ,"date", "location", "skills", "links" , "responsibilties "])
    wr.writerows(exported)



