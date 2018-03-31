from string import ascii_uppercase

d=dict(zip(ascii_uppercase, list(range(1, len(ascii_uppercase) + 1))))

def get_name_values(arr):
	arr=sorted(arr)
	finalScore = 0
	for index, name in enumerate(arr):
		score = sum(d[letter] for letter in name.strip('"'))*(index+1)
		finalScore+=score
	return finalScore

if __name__=="__main__":
	f = open("files/P022Text.txt").read().split(",")
	print(f)
	print(type(f))
	print(get_name_values(f))