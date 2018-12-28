#!/usr/bin/env python
# coding: utf-8

# In[1]:


# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/8-10","84588","dd7ee62681a647bbbaa2a7f07d5d3d22" )
r.addBodyPara("class_id", "45090")
r.addBodyPara("course", "5")
# r.addFilePara("img", r"C:\Users\showa\Desktop\使用过的\4.png") #文件上传时设置
res = r.post()
print(res.text) # 返回信息


# In[ ]:




