control = input('请问您需要存款还是取款呢？')
if control == '取款':
    money = 10000
    iwillq = int(input('请输入需要取款的金额'))
    if iwillq <= money:
        print('取款成功')
        print('剩余金额：', money - iwillq)
    else:
        print('没这么多钱取你🐎呢')
else:
    money = 10000
    iwillc = int(input('请输入需要存款的金额'))
    print('存款成功')
    print('剩余金额：', money + iwillc)
