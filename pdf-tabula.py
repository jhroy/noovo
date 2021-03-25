# coding utf-8
# ©2021 Jean-Hugues Roy. GNU GPL v3.

import tabula, csv
import pandas as pan

fichierIn = "numeris.csv"
fichierOut = "cotesEcoute2.csv"

f1 = open(fichierIn)
fichiers = csv.reader(f1)

for fichier in fichiers:
	# print(fichier)
	nomFichier = "pdfs/{}".format(fichier[3])
	print(nomFichier)
	df = tabula.read_pdf(nomFichier, pages="all")
	try:
		info = df[0]
		# print(len(info),info.shape())
		# print(len(info))
		# print(info["2+ AMM/"])
		for index,ligne in info.iterrows():
			emission = []
			emission.append(fichier[0])
			emission.append(fichier[1])
			emission.append(fichier[3])
			emission.append(fichier[4])
			emission.append(fichier[5])
			emission.append(fichier[6])
			# print(len(ligne),ligne[-1])
			for item in ligne.dropna():
				# if item != None:
				# print(item)
				emission.append(item)

			print(emission)
			asterix = open(fichierOut,"a")
			obelix = csv.writer(asterix)
			obelix.writerow(emission)
			print("*"*10)
	except:
		pass