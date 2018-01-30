import pdftables_api
import os

dir = raw_input("Insert folder path: ")

for entry in os.listdir(dir):
	if entry.endswith(".pdf"):
	
		a = os.path.join(dir, entry)
		b = os.path.join(dir, entry)
		d = b.split(".pdf")[0]
		
		c = pdftables_api.Client('5d8bp4bt79zt')
		
		c.xlsx(a, d + ".xlsx")

		print '"'+ entry +'"' , "Converted Successfully"
		
		continue
	else:
		continue
		
print "Done!"