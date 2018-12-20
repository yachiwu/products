products = []
#讀取檔案
with open ('products.csv','r') as f:
	for line in f:
		if '商品,價格' in line:
			continue #跳到下一回,下面內容不執行
		name , price = line.strip().split(',')
		products.append([name,price])
print(products)		
#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')	
	products.append([name,price])	
print(products)

#印出全部商品
for product in products:
	print(product[0],'的價格是',product[1])
#寫入檔案
with open ('products.csv','w') as f:
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')
