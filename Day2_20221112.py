#!/usr/bin/env python
# coding: utf-8

# In[1]:


math = [80, 90, 70, 70, 100]

j = 1
for i in math:
  if i >= 90:
    print(j, "번째 학생은 합격입니다.")
  
  else:
    print(j, "번째 학생은 불합격입니다.")
    j += 1


# In[5]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 == 0:
        print(i)


# In[6]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 != 0:
        continue
    
    print(i)


# In[7]:


# range 함수

for i in range(1,11):   # 두 번째 수는 미만
    print(i)


# In[12]:


# for 문으로 구구단 출력하기

for i in range(2,10):   # 단을 출력
    for j in range(1,10):
        print(i, "*", j, "=", i*j, end="\t")
    print()


# In[45]:


# for 문으로 구구단 출력하기

for i in range(2,10):   # 단을 출력
    for j in range(1,10):
        print(i,"*",j,"=",i*j, end="\t")
    print()


# In[46]:


print("hello")


# In[47]:


sum=0
for i in range(0,101):
    if i % 2 == 0:
        sum = sum + i
print(sum)


# In[52]:


sum=0
for i in range(0,101,2):
    sum += i
print(sum)


# In[58]:


# 리스트 축약/내포 List Comprehension
# 리스트를 좀 더 편리하고 직관적으로 만드는 방법이다.

list1 = [1,2,3,4]
print(list1)

list2 = [num for num in list1]
print(list2)

list3 = [num                  for num in list1]
print(list3)

list4 = [num*2                  for num in list1]
print(list4)

list5 = [num                  for num in list1             if num % 2 == 0]
print(list5)


# In[59]:


# if의 고급형

no = 90
if no >= 80:
    print("합격 입니다.")
else:
    print("불합격 입니다.")


# In[65]:


# if 문 기준으로 앞쪽이 True, 뒤쪽이 False
no=80
"합격입니다."      if no>=80         else "불합격입니다."

no=65
"합격입니다." if no>=80 else "불합격입니다."


# In[ ]:




