IfVip = input('请输入顾客是否为会员:')
TotalPrice = float(input('请输入顾客消费金额:'))
if IfVip == '是':
    if TotalPrice < 200.0:
        FinalPrice = TotalPrice * 0.8
        print('尊敬的会员顾客，您本次的总金额为', TotalPrice, '您本次折后总额为:', FinalPrice, '享受折扣为: 8 折，欢迎下次光临!')
    else:
        FinalPrice = TotalPrice * 0.75
        print('尊敬的会员顾客，您本次的总金额为', TotalPrice, '您本次折后总额为:', FinalPrice,
              '享受折扣为: 75 折，欢迎下次光临!')
elif TotalPrice < 100.0:
    print('尊敬的顾客，您本次的总金额为', TotalPrice, '您本次折后总额为:', TotalPrice,
          '欢迎下次光临!')
else:
    FinalPrice = TotalPrice * 0.9
    print('尊敬的顾客，您本次的总金额为', TotalPrice, '您本次折后总额为:', FinalPrice,
          '享受折扣为: 95 折，欢迎下次光临!')
