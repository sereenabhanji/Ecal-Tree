#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 22:47:49 2023

@author: sereenabhanji
"""

from bs4 import BeautifulSoup


with open ("mcgill_ecal.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
    
    
class Course:
    def __init__(self, name, url, prerequisites):
        self.name = name
        self.url = url
        self.prerequisites = prerequisites


#soup = BeautifulSoup("https://www.mcgill.ca/study/2023-2024/courses/search", 'html.parser')

tester = soup.findAll('a', href=True)

courses = [c.attrs.get('href')for c in soup.select('h4.field-content')]
print(courses)
#print(tester)
links = []

for i in range (74,90):
    course = Course("hello", tester[i]['href'],["comp 250"])
    links.append(course)
    print(course.url)

    
next_page = soup.findAll('li', class_='pager-next')
coursename = next_page[0]
print(coursename)

#pattern = re.compile(r"\"^\$")
#result = re.search(pattern, coursename)






