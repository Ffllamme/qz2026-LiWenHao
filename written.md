一、

1.B  2.B  3.B  4.B  5.A  6.B  7.A  8.B  9.B

 二、
 
 第1题
 
 a与b是浅拷贝的关系，a与b第一层子数据的去留不相互影响，但是子数据还是共用的，修改其中一方的子数据的数值会影响另一方的子数据的数值。
 a与c是深拷贝的关系，每一层数据都相互独立，互不影响。
 
 a=[[1,2,99],[3,4]]
 
 b=[[1,2],[3,4]]
 
 a与b是浅拷贝的关系，A与b第一层子数据的去留不相互影响，但是子数据还是共用的，修改其中一方的子数据的数值会影响另一方的子数据的数值。
 a与c是深拷贝的关系，每一层数据都相互独立，互不影响。
 
 第2题
 
1.代码：

'''python

    error = []

    for log in logs:

    if log["level"] == "ERROR":
    
        error.append(log)
        
print(error)

2.

  amount= {}

 for i in logs: 

    name = i["user"]
    
    if name in amount:
    
        amount[name] = amount[name] + 1 
        
    else:
    
        amount[name] = 1
        
 print(amount)

3.使用len只会告诉我字典里有多少条数据，但是不会对每个用户出现的次数进行统计

第3题

代码：

  a = input("输入被除数")

  b = input("输入除数")

  try:

    a=int(a)

    b=int(b)

    print(a)

    print(b)

    result=a/b

     print(float(result))

 except( ZeroDivisionError  , ValueError):

     print("出错了")

 原因：

 except能够提前覆盖所有错误类型，而if需要将错误类型一一写出
