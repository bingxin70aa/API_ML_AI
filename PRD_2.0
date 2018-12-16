# 学龄儿童记单词APP产品需求文档
* 前 PRD.md 现更改为PRD_1.0(肤质检测app）请[参见](https://github.com/bingxin70aa/API_ML_AI/blob/master/PRD_1.0.md)

## 前期目标PRD

文件状态 | 草稿
---|---
文档状态 | 进行中
作者 | 侯冰昕
完成日期 |2018-11-28



### 一、项目概述
**1、产品背景介绍**

因为自身是“英语单词头痛重度患者
”。觉得背单词枯燥乏味，面对字母就想睡，有多数

随着全球化的发展，人们对学习英语的需求越来越强烈，学龄儿童也是（其实多数是家长希望孩子如此）。市面上英语记忆类的app不少，但是质量参差不齐，大多数为游戏的形式来与单词记忆相结合，但主要依托于家长的积极性，而不是孩子主动学习培养出的兴趣。所以希望能够把背单词跟生活相融合，让记忆单词成为一种生活习惯，亲近并能融入生活，为深度学习英语铺路。


**2、产品概述及目标**

- name : **present**
- 这是一款通过物体识别的方式英语单词学习APP。对准物体拍摄即可获取中文和对应的英文翻译信息，并即时可进行拼写，同时将识别过的单词加入单词本中，方便再进行复习。为用户提供一个可以融入生活、激发出学习的主观能动性的单词记忆工具。

**3、目标用户、使用场景**

* 目标用户：主要针对6岁至18岁，对英语单词记忆有困难又提不起兴趣，对英语一窍不通或者半知半解的学龄孩童。

* 使用场景：任何时间地点


**4、术语和缩写解释**

术语 | 解释
---|---
NMT | neural Machine translation ,神经机器翻译
艾宾浩斯记忆曲线 | 遗忘率随时间的流逝而先快后慢，特别是在刚刚识记的短时间里，遗忘最快。
席勒-斯宾塞理论 | 艺术活动是无功利无目的自由的游戏活动，是人与生俱来的本能，艺术就起源于人的游戏本能或冲动。

[参考链接之百度](http://www.sohu.com/a/122262870_116441)
[参考链接之谷歌](http://www.sohu.com/a/157050254_642762)

**5、竞品分析**

百度翻译已经有在做实物翻译，但未让“翻译实用化”，用户需求少，受众面向较狭窄。本产品也会对此取其精华，去其糟粕，实现产品的核心价值。

### 二、产品角色

名称| 说明
---|---
系统管理员 | 拥有所有权限
用户 | 	仅有前端个人中心的权限

### 三、产品功能
**1、基本要求**

需求 | 说明
---|---
页面编码 | UTF-8
界面 | 响应式设计

**2、功能模块划分**

功能 | 说明
---|---
调用API | [Azure标记图像](https://docs.azure.cn/zh-cn/cognitive-services/computer-vision/concept-tagging-images#image-tagging-example)、[有道志云文本翻译](https://ai.youdao.com/docs/doc-trans-api.s#p08)
数据管理 | 数据库备份/优化/检测
前台：用户中心 | 个人中心
前台：搜索功能 | 单词搜索

**3、功能模块设计**

3.1后台系统

[参见](http://naotu.baidu.com/file/c1278d8409bddd4e2dd29be02869d500)



3.2 数据流程图

[参见](https://www.processon.com/view/link/5bfe6432e4b006dc83a82a2f)

![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/%E6%95%B0%E6%8D%AE%E6%B5%81%E7%A8%8B%E5%9B%BE.jpg?raw=true)

3.3功能结构

[参见](http://naotu.baidu.com/file/d5697afa5bb5f2220c82bca06f9f589c)

![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/app%E5%8A%9F%E8%83%BD%E7%BB%93%E6%9E%84%20(2).png?raw=true)

### 四、产品原型
详情见[链接](https://bingxin70aa.github.io/present_Axure/)

###### 首页（默认页面）
![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/child%E4%BA%A7%E5%93%81%E5%8E%9F%E5%9E%8B_%E9%A6%96%E9%A1%B5.jpg?raw=true)

###### 单词本

![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/child%E5%8E%9F%E5%9E%8B%E2%80%94%E2%80%94%E5%8D%95%E8%AF%8D%E6%9C%AC.jpg?raw=true)

###### 个人中心

![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/child%E4%BA%A7%E5%93%81%E5%8E%9F%E5%9E%8B%E2%80%94%E2%80%94%E4%B8%AA%E4%BA%BA%E4%B8%AD%E5%BF%83.jpg?raw=true)

###### 实物拍摄小窍门

![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/child%E4%BA%A7%E5%93%81%E5%8E%9F%E5%9E%8B%E2%80%94%E2%80%94%E5%AE%9E%E7%89%A9%E6%8B%8D%E6%91%84%E5%B0%8F%E7%AA%8D%E9%97%A8.jpg?raw=true)




### 五、产品进度
- [ ] app框架
- [x] Azure-计算机视觉-标记图像 api 调用
- [x] 有道志云-翻译API调用

### 六、项目相关代码进程与展示

* [***azure_cv_API_request***](https://github.com/bingxin70aa/API_ML_AI/blob/master/azure_cv_API_request.ipynb)
* [***youdao_translation_api_request***](https://github.com/bingxin70aa/API_ML_AI/blob/master/youdao_translation_api_request.ipynb)



### N、后期准备及参考资料
* [PRD推进方式及思考](http://note.youdao.com/noteshare?id=9e2e2d3a2cf39b53818b7f4095a0de5e)

* [杂乱无章](http://note.youdao.com/noteshare?id=6fd7164543137fb310dac76de65948fe)

* [Error](http://note.youdao.com/noteshare?id=414a03b9d7e9ccde11c0bbd1a79b8bbd)


## 实在细节
### 一、PRD
#### PRD1.加值宣言
* 将传统的背单词app与物体检测结合，打破死记硬背的方式记忆单词，赋予趣味性，为用户记忆单词提供动能，增添用户粘性。
#### PRD2.核心价值
* 依靠主观能动来进行单词记忆
#### PRD3.核心价值与用户痛点
* 用户觉得单纯的单词背诵有些枯燥无味，难以坚持
* 大部分用户觉得背单词只是任务，自身无很强的动力和自制力，多数依赖父母，由其监管下进行。
#### PRD4.人工智能概率性与用户痛点
* 可导致识别失败的因素及其如何解决：
    * 无法检测出物体
    * **解决方式**：弹出提示“无法检测出物体”，帮助用户重新返回到拍摄页面进行再次拍摄-涂抹-识别。
    * 物体识别出错或不匹配
    * **解决方式**：
         1. 用户可通过滑动卡片，选择性添加识别对象的单词及中文意思（见camera-4右侧的[释义](https://bingxin70aa.github.io/present_Axure/)
         2. 创建一个用户界面，指引人们在运行分类器之前确保摄像头画面中已经出现了要分类的目标

#### PRD5.需求列表与人工智能API加值
* 需求列表

Title | User story | Importance | Notes
---|---|---|---
识别前的拍摄 | 用户拍摄对象清晰，准确 | 非常重要|对模糊不清的图片进行反馈，以保证对象能够顺利识别
识别前的涂抹 | 用户涂抹出完整的检测区域 | 非常重要 | 用户会涂抹不完整或有缺口，需提示用户绘制完全

### 二、原型
#### 原型1.交互及界面设计

    
## 清单
* [产品原型文档](https://bingxin70aa.github.io/present_Axure/#g=1)
* 前 PRD.md 现更改为PRD_1.0(肤质检测app）请[参见](https://github.com/bingxin70aa/API_ML_AI/blob/master/PRD_1.0.md)
* 已尝试调用的API的输入输出
    * [***azure_cv_API_request***](https://github.com/bingxin70aa/API_ML_AI/blob/master/azure_cv_API_request.ipynb)
    * [***youdao_translation_api_request***](https://github.com/bingxin70aa/API_ML_AI/blob/master/youdao_translation_api_request.ipynb)

