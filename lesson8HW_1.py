apple = 0
sell = 0

money = int(input('現在有多少錢?'))
x = int(input('買進一顆蘋果要多少錢?'))
y = int(input('一顆蘋果賣多少錢?'))
if x > y:
    print('老闆每賣一顆蘋果虧',x - y,'元')
else:
    print('老闆每賣一顆蘋果賺',y - x,'元')
z = int(input('有幾顆蘋果'))
apple = apple + z

print('現在有',apple,'顆蘋果')

print('歡迎來到123計算系統')


i = 0
while i < 1:
    print('a:買進')
    print('b:賣出')
    print('c:今日收入')
    print('d:庫存')
    print('e:離開')
    s = str(input('現在要做什麼?'))
    if s == 'a':
        print ('現在有',money,'元')
        buy = int(input('要買進多少蘋果'))
        g = buy * y
        if money < g:
            print('需要',g,'元','目前沒有那麼多的錢')
        else:
            apple = apple + buy
            print('現在有',apple,'顆蘋果')
            print('應付:', g ,'元')
            money = money - int(g) 
            print ('現在有',money,'元')
        
    elif s == 'b':
        print ('現在有',money,'元')
        print('現在有',apple,'顆蘋果')
        sell = int(input('要賣幾顆?'))
        h = sell * y      
        if apple < sell:
            print('需要',h,'元','目前蘋果不足')
        else:
            print('應收:', h ,'元')
        money = money + h
        apple = apple - sell
        print('現在有',apple,'顆蘋果')
        print ('現在有',money,'元')
            
    elif s == 'c':
        print('現在有',apple,'顆蘋果')
        print('總共賣出',sell,'顆蘋果')
        print('有',money,'元')
        
    elif s == 'd':
        print('現在有',apple,'顆蘋果')
        
    elif s == 'e':
        i = i + 1
        print('感謝使用123計算系統')
