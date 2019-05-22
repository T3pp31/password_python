password=1887 #好きなパスワードを設定。何桁でも可能
a=int(input("パスワードを入力してください(数字):"))
c=0
while password!=a and c<=4: #最初に1回パスワードを入力しているため(1+4=5)
    a=int(input("正しいパスワードを入力してください:"))
    c=c+1
if password==a:
    print("施錠しました")
else:
    print("5回入力ミスをしたため終了します")
