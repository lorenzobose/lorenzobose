n = 0 
temp = 1
risultato=[]
risultato.append(n)
max = int(input("Inserire numero massimo al quale si vuole arrivare: "))	
while n < max: 
	n1 = n
	n = temp + n
	temp = n1
	risultato.append(n)
print(risultato)
	
