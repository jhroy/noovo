# coding: utf-8
# ©2021 Jean-Hugues Roy. GNU GPL v3.

import requests, time, csv, urllib
from bs4 import BeautifulSoup

numeris = "numeris.html"
fichier = "numeris.csv"

page = BeautifulSoup(open(numeris), "html.parser")

# print(page)
n = 0

for li in page.find_all("li"):
	if "20" in li.text.strip() and "ational" not in li.text.strip():
		n += 1
		# print(n,li.text.strip())
		pdf = li.find("a")["href"]
		# print(pdf)
		nom = pdf.split("/")[-1]
		nom = urllib.parse.unquote(nom)
		# print(nom)
		periode1 = li.find("a")["title"].strip()
		# periode2 = li.find("a").text.strip()
		semaine = li.find("div",class_="week3").text.strip()
		jour = li.find("div",class_="date3").text.strip()
		
		fichpdf = requests.get(pdf)
		with open("pdfs/{}".format(nom), 'wb') as fuck:
			fuck.write(fichpdf.content)
		
		infos = [n,periode1,pdf,nom,semaine,jour]
		# if periode1 != periode2:
		# 	print(infos)
		print(infos)
		
		asterix = open(fichier,"a")
		obelix = csv.writer(asterix)
		obelix.writerow(infos)
		
		print("*"*20)
		time.sleep(2)