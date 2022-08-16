"""
File: webcrawler.py
Name: 官欣
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup

import locale


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': 't-stripe'})

        # male and female total int
        male_t = female_t = 0

        # code for locale(from internet)
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

        # loop over class:t-stripe
        for tag in tags:

            # each name have 5 index, there are 200 ranks
            for i in range(1000):

                # get the numbers of male and female
                # which is the third and five index
                if i % 5 == 2:
                    male_n = tag.tbody.text.split()[i]
                    female_n = tag.tbody.text.split()[i+2]

                    # change string to numbers
                    male_t += locale.atof(male_n)
                    female_t += locale.atof(female_n)

        # print result
        print(f'Male Number: {int(male_t)}')
        print(f'Female Number: {int(female_t)}')


if __name__ == '__main__':
    main()
