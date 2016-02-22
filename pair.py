import random

print("Enter filename:")
fileName = input()
f = open(fileName, 'r')
text = f.read()
names = text[:-1].split('\n')
print(len(names))
print(names)
if(not len(names)%2 == 0):
	print("Amount of names not even!")
else:
	random.shuffle(names)
	print(names)
	o = open("pairingOutput.txt", 'w')
	for i in range(len(names)//2):
		o.write(names[2*i] + " " + names[2*i + 1] + '\n')
	o.close()
