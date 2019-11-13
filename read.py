data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 50000 == 0:
			print(len(data))

print('讀取完了，總共有', len(data), '筆資料')
#算平均留言長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均是', sum_len / len(data))

#filter
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '則，長度小於100')

#specific
good = []

for d in data:
	if 'abc' in d:
		good.append(d)
print('一共有',len(good),'提到abc')
print(good)