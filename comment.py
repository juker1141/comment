data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))

print('檔案讀取完畢, 總共有', len(data), '筆留言')
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為', sum_len / len(data), '個字')

new = []
for a in data:
	if len(a) > 10000:
		new.append(a)
print('一共有', len(new), '筆留言長度大於10000')
print(new[0])
print(new[10])