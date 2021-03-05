print('请不要删除money.txt文件及内容，否则将运行失败！')
print('请不要删除money.txt文件及内容，否则将运行失败！')
print('请不要删除money.txt文件及内容，否则将运行失败！')
#Tips
control = input('请问您需要存款还是取款呢？')
money = open("money.txt")
money = money.read()
money = int(money)
if control == '取款' or 'qk':
    #输入取款或者qk都可以执行
    iwillq = int(input('请输入需要取款的金额'))
    if iwillq <= money:
        money = money - iwillq
        print('取款成功，剩余金额：', money)
        cmoney = open('money.txt',"w+")
        cmoney.write(str(money))
        cmoney.close()
    else:
        print('取款失败，余额不足，剩余金额：', money)

else:

 if control == '存款' or 'ck':
     # 输入存款或者ck都可以执行
   iwillc = int(input('请输入需要存款的金额'))
   print('存款成功，剩余金额：', money + iwillc)
   money = money+ iwillc
   cmoney = open('money.txt', "w+")
   cmoney.write(str(money))
   cmoney.close()
 else:
    print('操作取消')
