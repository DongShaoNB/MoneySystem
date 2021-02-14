control = input('请问您需要存款还是取款呢？')
money = 10000
if control == '取款':
    iwillq = int(input('请输入需要取款的金额'))
    if iwillq <= money:
        print('取款成功，剩余金额：', money - iwillq)
    else:
        print('取款失败，剩余金额：', money)

else:

 if control == '存款':
   iwillc = int(input('请输入需要存款的金额'))
   print('存款成功，剩余金额：', money + iwillc)
 else:
    print('操作取消')
