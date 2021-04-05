import matplotlib.pyplot as plt
import time
fname = 'data.txt'
with open(fname, 'r') as f:
    s = [i.split(',') for i in f.readlines()]
weight=[]
value=[]
ratio=[]
packbag=[]
message=[]
number=int(input("Please input the number:"))
for i in range(len(s)):
    for j in range(len(s[i])):
        if(i==0):
            weight.append(int(s[i][j]))
        else:
            value.append(int(s[i][j]))
print("the weight of knapsack is:")
print(weight)
print("the value of knapsack is:")
print(value)
plt.scatter(weight,value)
plt.xlabel("weight")#x轴标签
plt.ylabel("value")#y轴标签
plt.tick_params(axis='both')#x,y轴都有刻度
 
plt.savefig('3.2.png')#保存图片，一定要在show之前保存图片，否则保存的图片就为空白
plt.show()
#排序
for i in range(len(weight)):
    rate=weight[i]/value[i]
    ratio.append(rate)
#print(ratio)

for i in range(len(weight)):
    for j in range(len(value)):
        if i==j:
              for k in range(len(ratio)):
                  if j==k:
                      t=[weight[i],value[j],ratio[k]]
                      packbag.append(t)
print("The result of order is:")
print("weight  value  ratio")
message=sorted(packbag,key=lambda x:x[2],reverse=True)
for i in range(len(message)):
    print(message[i])

#动态规划算法
start=time.perf_counter()
c=10149
value1=[]
value1 = [[0 for j in range(c + 1)] for i in range(number + 1)]
for i in range(1, number + 1):
    for j in range(1, c + 1):
        if j<weight[i-1]:
            value1[i][j]=value1[i-1][j]
        else:
            value1[i][j]=max(value1[i-1][j],value1[i-1][j-weight[i-1]]+value[i-1])
		# 背包总容量够放当前物体，取最大价值
print('最大价值为:',value1[number][c])
x=[0 for i in range(number)]
j=c
for i in range(number,0,-1):
    if value1[i][j]>value1[i-1][j]:
        x[i - 1]=1
        j -= weight[i-1]
print('背包中所装物品为:')
for i in range(number):
    if x[i]:
        print('第', i+1, '个,', end='')
print()
end=time.perf_counter()
print("运行时间: %s Seconds"%(end-start))
