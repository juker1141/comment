def read_file(filename):
	data = []
	count = 0
	with open(filename, 'r') as f:
		for line in f:
			data.append(line)
			count += 1
			if count % 1000 == 0:
				print(len(data))
	print('檔案載入中...')
	return data

def wc_file(data):
	wc = {} #word_count
	for d in data:
		words = d.split(' ')
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1
	print('檔案已讀取完畢')
	print('總共有', len(data), '筆留言')
	return wc

def avg_len(data):
	sum_len = 0
	for d in data:
		sum_len += len(d)
	print('留言的平均長度為', sum_len / len(data), '個字')

def file_len(data):
	new = []
	how_long = input('請輸入您想要篩選的長度: ')
	for a in data:
		if len(a) > int(how_long):
			new.append(a)
	print('一共有', len(new), '筆留言長度大於', how_long)
	
def filter_file(data):
	good = []
	key_word = input('請輸入您想搜尋的關鍵字: ')
	for d in data:
		if key_word in d:
			good.append(d)
			
	print('總共有', len(good), '筆資料提到', key_word)

def count(wc):
	for word in wc:
		if wc[word] > 1000000:
			print(word,  '出現了', wc[word], '次')#知道可以這樣寫就好

def serch(wc):
	while True:
		print('輸入quit返回主選單')
		word = input('您想查詢的字: ')
		if word == 'quit':
			break
		elif word in wc: 
			print(word, '共出現了', wc[word], '次')
		else:
			print('Sorry,該字典中查無', word)
	
def order_serch(data, wc):
	order_list = ['1.平均長度', '2.留言長度篩選', '3.特定文字出現數量', '4.搜尋', '5.離開']
	while True:
		print(order_list)
		order = input('請輸入您想使用的功能代碼: ')
		if order == '1':
			avg_len(data)
			continue
		elif order == '2':
			file_len(data)
			continue
		elif order == '3':
			filter_file(data)
			continue
		elif order == '4':
			serch(wc)
			continue
		elif order == '5':
			print('感謝您的使用')
			break

def main():
	data = read_file('reviews.txt')
	wc = wc_file(data)
	order_serch(data, wc)

main()
	


