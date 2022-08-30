import random #导入随机数模块
dict1 = {}
list1 = ['红桃', '黑桃', '梅花', '方片']
list2 = [str(i) for i in range(1, 11)]
list2.append('J')
list2.append('Q')
list2.append('K')
list2.append('A')
list3=[]
for i in list1:
    # dict1[i] = list2
    for j in list2:
        list3.append([i,j]) #创建扑克牌
list4=input().split(',')#获取输入人数，英文逗号隔开
for i in list4:
    # print(i,":",random.sample(list3,3))
#     dict1[i]=random.sample(list3,3)
    list5=random.sample(list3, len(3 * list4))#抽取总人数X3的牌数
    dict1[i]=random.sample(list5,3)#将抽取的牌平均分给每个人
#输出
print(dict1)