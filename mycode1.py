
# coding: utf-8

# In[1]:


name = "Felipe"


# In[2]:


age = 25


# In[3]:


print (age)


# In[4]:


print(name)


# In[5]:


print ("my name is")


# In[6]:


print("my name is", name)


# In[7]:


print ("My age is", age)


# In[10]:


print("My name is", name, "and my age is", age)


# In[11]:


print(name)


# In[12]:


newage = age - 12


# In[15]:


print(newage)


# In[14]:


print(newage = age - 10)


# In[16]:


multipliedage = age*2


# In[17]:


print ("Your age is actually", newage)


# In[18]:


print("Your multiplied age is", multipliedage)


# In[19]:


sequence = "CTAGCTAG"


# In[20]:


print (sequence)


# In[21]:


print(sequence[0])


# In[22]:


print(sequence[3])


# In[23]:


print("My fourth letter is",sequence[3])


# In[24]:


len (sequence)


# In[25]:


print("Sequence length is", len(sequence))


# In[26]:


print(sequence[0:3])


# In[27]:


sequence[0:3]


# In[28]:


type(age)


# In[30]:


COX2 = "TACG"


# In[31]:


COX1="CTAG"


# In[33]:


COX1 +COX2


# In[35]:


firstname = "Felipe"


# In[36]:


lastname="Chen"


# In[37]:


firstname + " " + lastname


# In[38]:


len(age)


# In[39]:


name + age


# ## 

# In[40]:


5^2


# In[41]:


5**2


# In[42]:


7^6


# In[43]:


3^1


# In[44]:


25^5


# In[45]:


5%2


# In[46]:


4^2


# In[47]:


4^3


# In[48]:


4^4


# In[49]:


4^5


# In[50]:


13^1


# In[51]:


13^4


# In[52]:


#this is a comment


# In[53]:


#adding 2 sequence because they are the same gene


# In[54]:


COX1 + COX2


# In[55]:


max(2,3,15,26,7)


# In[56]:


round(9.5)


# In[57]:


round(2.415948)


# In[58]:


round(2.1234867,3)


# In[59]:


help(round)


# In[60]:


help(^)


# In[61]:


help(min)


# In[62]:


max(21,32,45)


# In[63]:


ans + min(21,32,45)


# In[64]:


max(21,32,45)+min(21,32,45)


# In[65]:


hundred_C = "C" *100


# In[66]:


COX1 + hundred_C


# In[67]:


help(toupper)


# In[68]:


help(ToUpper)


# In[69]:


help(TOUPPER)


# In[70]:


len(COX1+hundred_C)


# In[71]:


COX1.lower()


# In[72]:


import math


# In[73]:


math.cos(60)


# In[74]:


math.sin(180)


# In[75]:


math.sin(90)


# In[76]:


math.cos(90)


# In[78]:


print("the sine of 180 is", math.sin(180))


# In[79]:


pi


# In[80]:


math.pi


# In[81]:


pi = math.pi


# In[82]:


math.sin(pi)


# In[83]:


math.sin(math.pi)


# In[84]:


math.cos(pi)


# In[85]:


help(math)


# In[86]:


from math import pi


# In[87]:


pi


# In[88]:


import math as m


# In[89]:


m.tan(90)


# In[90]:


from math import e


# In[91]:


math.log(e)


# In[92]:


from math import *


# In[93]:


log(e)


# In[94]:


tau


# In[95]:


angle = degrees(pi/2)


# In[96]:


print(angle)


# In[97]:


import pandas


# In[98]:


help(pandas)


# In[99]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[100]:


pandas.read_excel("../../../Documents/042018_042218 Composite COD.xlsx")


# In[102]:


pandas.read_csv("Data/gapminder_gdp_asia.csv")


# In[107]:


oceania_data = pandas.read_csv("Data/gapminder_gdp_oceania.csv", index_col="country")


# In[104]:


type(oceania_data)


# In[105]:


print(data)


# In[108]:


print(oceania_data)


# In[109]:


oceania_data.info()


# In[110]:


oceania_data


# In[111]:


oceania_data.T


# In[112]:


oceania_data.describe()


# In[114]:


oceania_data.T.describe()


# In[118]:


america_data = pandas.read_csv("Data/gapminder_gdp_americas.csv",index_col="country")


# In[124]:


america_data


# In[119]:


america_data.describe()


# In[120]:


america_data.T.describe()


# In[121]:


america_data.T.describe()


# In[122]:


america_data.T


# In[123]:


america_data.T.describe()


# In[127]:


america_data.columns


# In[128]:


oceania_data.columns


# In[129]:


oceania_data


# In[131]:


oceania_data.iloc[1,2]


# In[133]:


oceania_data.loc["Australia","gdpPercap_1952"]


# In[134]:


oceania_data.loc["Australia",:]


# In[135]:


oceania_data.loc[:,"gdpPercap_1952"]


# In[136]:


oceania_data.loc["Australia","gdpPercap_1952":"gdpPercap_1962"]


# In[137]:


oceania_data


# In[138]:


oceania_data.iloc[:, 0:3]


# In[140]:


aus5262 = oceania_data.iloc[0,0:3]


# In[141]:


aus5262.max()


# In[142]:


aus5262.min()


# In[143]:


oceania_data.iloc[:,0:3].max()


# In[144]:


clear(aus5262)


# In[145]:


aus5262


# In[146]:


help(clear)


# In[147]:


subset = oceania_data.iloc[:,0:3]


# In[148]:


print (subset > 11000)


# In[149]:


subset[subset >11000]


# In[150]:


subset[subset>11000].describe()


# In[153]:


europe_data = pandas.read_csv("Data/gapminder_gdp_europe.csv",index_col="country")


# In[154]:


europe_data


# In[155]:


europe_data.loc["Serbia","gdpPercap_2007"]


# In[156]:


europe_subset = europe_data.loc["Italy":"Norway","gdpPercap_1962":"gdpPercap_1972"]


# In[157]:


europe_subset[europe_subset < 15000].describe()

