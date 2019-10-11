s = input()
vowels = ['A','E','I','O','U']
score=[0,0]
for i in range(len(s)):
	if s[i] in vowels:
		score[1] += len(s) - i
	else:
		score[0] += len(s) - i

if score[1] > score[0] :
	print("Kevin",score[1])
elif score[0] > score[1] :
	print("Stuart",score[0])
else :
	print("Draw")