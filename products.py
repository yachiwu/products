#這個版本的csv 只能寫英文中文怪怪的
import os #作業系統 operating system
def read_file(filename):	#讀取檔案
	products = []
	with open (filename,'r',encoding ='utf-8') as f:
		for line in f:
			if 'product,price' in line:
				continue #跳到下一回,下面內容不執行
			name , price = line.strip().split(',')
			products.append([name,price])
	print(products)	
	return products			

def user_input(products):#讓使用者輸入
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入價格: ')	
		products.append([name,price])	
	print(products)
	return(products)

def print_products(products):#印出全部商品
	for product in products:
		print(product[0],'的價格是',product[1])

def write_file(filename,products):		#寫入檔案
	with open (filename,'w',encoding ='utf-8') as f:
		f.write('product,price\n')
		for product in products:
			f.write(product[0] + ',' + product[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在
		print('ya!找到檔案! ')
		products = read_file(filename)
	else:
		products = []
		print('找不到檔案....')	
	products = user_input(products)
	print_products(products)
	write_file(filename,products)
main()	