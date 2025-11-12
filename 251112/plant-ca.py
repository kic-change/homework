UserName = input('请输入用户名: ')
PlantName = input('请输入植物名: ')


template = '''
                植树证书 
 -------------------------------------
 {username} 谢谢你： 
    你申请种植的 {plantname} ，将由伊利
 公益基金会负责种下。查看种植进程>
 
 树苗编号：NO.HBI66308960305 
 申请时间：2023年11月10日 
 种植地点：鄂尔多斯 
 -------------------------------------
'''

final = template.format(username=UserName, plantname=PlantName)


print(final)
