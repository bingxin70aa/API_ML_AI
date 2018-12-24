# 云起APP产品需求文档
* 首个产品需求文档“ PRD.md” 现更改为“PRD_1.0”(肤质检测app）请[参见](https://github.com/bingxin70aa/API_ML_AI/blob/master/PRD_1.0.md)

- [PRD](#前期目标PRD)
    - [加值宣言](#1产品背景介绍加值宣言)
    - [核心价值](#4产品概述及目标)
    - [核心价值与用户痛点](#2用户痛点)
    - [人工智能概率性与用户痛点](#5人工智能的概率性)
    - [需求列表与人工智能API加值](#7需求列表)
- [原型](#四产品原型)
    - [交互及界面设计](#企鹅默认页面)
    - [信息设计](#三产品功能)
    - [原型文档](https://bingxin70aa.github.io/Axure_interactive_care_app/)
- [API产品使用关键AI或机器学习之API的输出入展示](#六产品使用关键AI或机器学习之API的输出入展示)
    - [使用水平](#六产品使用关键AI或机器学习之API的输出入展示)
    - [使用比较分析](#3使用比较分析结果)
    - [使用后风险报告](#4风险报告)
    - [加分项](#7需求列表)


## 前期目标PRD

文件状态 | 草稿
---|---
文档状态 | 进行中
版本 | V2.1
作者 | 侯冰昕
完成日期 | to be continued

## 修改历史

版本 | 日期 |修改内容
---|---|---
V2.1 | 2018-11-28| APP游戏化

前 V2.0-child（无添加游戏元素前） [参见](https://github.com/bingxin70aa/API_ML_AI/blob/master/PRD_2.0.md)



### 一、项目概述
#### 1、产品背景介绍(加值宣言)

* 随着全球化的发展，人们对学习英语的需求越来越强烈，学龄儿童也是（尽管绝大多数是家长希望孩子如此）。市面上单词学习类的app不少，但是质量参差不齐，并且主要依托于家长的积极性，而不是孩子主动学习培养出的兴趣。因此希望能够把背单词跟生活相融合，让记忆单词成为一种生活习惯，亲近并能融入生活，为深度学习英语铺路。

* 市面上很早就出现了实物翻译的app，例如百度翻译，但是由于流程较于繁琐，需要涂抹后才能够锁定目标，再进行识别；而且未让“翻译实用化”，仅是放置于整个翻译系统的“小应用”中，没有确切的用户需求，因此本产品除了可以简化识别流程外，也针对用户需求将实物翻译赋予了实际意义，使其物尽其用。

#### 2、用户痛点
* 孩子：
   
    * 仅会初期对实物翻译app有好奇心，但难以长久。
    * 百度的实物翻译的流程较繁琐，需进行涂抹后才能锁定识别对象。
    * 用户觉得单纯的单词背诵些枯燥无味，难以坚持
    * 大部分用户觉得背单词只是任务，自身无很强的动力和自制力，多数依赖父母，由其监管下进行。
    * 单词背不下来（引入艾宾浩斯记忆曲线+K12群体记忆持久度的一个弹性变化）
* 家长：
    * 相比以前，当代家长更专注于培养孩子的兴趣，而不是是死读书的应试教育。（[极光大数据](http://www.gzqcyx.com/p/162923-248237-18953.html)）
    * 担心孩子看手机时间长，对眼睛不好


#### 3、术语和缩写解释

术语 | 解释
---|---
艾宾浩斯记忆曲线 | 遗忘率随时间的流逝而先快后慢，特别是在刚刚识记的短时间里，遗忘最快。
k12 | K12,教育类专用名词（kindergarten through twelfth grade），是学前教育至高中教育的缩写，现在普遍被用来代指基础教育。




#### 4、产品概述及目标

- name : **云起**
- 这是一款通过云养企鹅这种游戏的方式来培养孩子学习英语兴趣的习APP。
    * 主要特色功能 1：**游戏方面**，通过饲养养企鹅的方式来取代传统背单词APP较为功利性的打卡签到，不仅增添趣味性，还为用户记忆单词提供动能，增添用户粘性。
    * 主要特色功能 2：**获取单词的方式（API）**。可以通过物体识别的方式获取单词，即对准物体拍摄即可获取中文和对应的英文翻译信息，并即时可进行拼写，同时将识别过的单词加入<单词cool>中，方便再进行复习。为用户提供一个可以融入生活、**激发**出学习的**主观能动性**的单词记忆工具。

#### 5、人工智能的概率性
* 可能导致识别失败的因素及其如何解决：
    * 无法检测出物体
    * **解决方式**：弹出提示“无法检测出物体”，帮助用户重新返回到拍摄页面进行再次拍摄-识别。
    * 物体识别出错或不匹配
    * **解决方式**：
         1. 用户可通过滑动卡片，选择性添加识别对象的单词及中文意思（见交互原型的[链接](https://bingxin70aa.github.io/Axure_interactive_care_app/)）
         2. 创建一个用户界面，指引人们在运行分类器之前确保摄像头画面中已经出现了要分类的目标

#### 6、目标用户、使用场景
* 目标用户：主要针对5岁至18岁，对英语单词记忆有困难又提不起兴趣，对英语一窍不通或者半知半解的学龄孩童。

* 使用场景：任何时间地点

#### 7、需求列表

功能 | 用户案例 | 重要程度 | 技术领域
---|---|---|---
物体检测 | 用户想要学习物体的英文单词 |重要|[计算机视觉-Azure-REST API-分析图像](https://docs.azure.cn/zh-cn/cognitive-services/computer-vision/concept-tagging-images#image-tagging-example)
单词翻译 | 用户想要了解检测对象的中文释义 | 重要|[有道智云API](https://ai.youdao.com/docs/doc-trans-api.s#p08)


### 二、产品角色

名称| 说明
---|---
系统管理员 | 拥有所有权限
超级饲养员 | 除个人中心权限外，解锁所有附加功能（见说明）
普通用户 | 	仅有前端个人中心的权限

### 三、产品功能

#### 1、产品功能结构图

详细[参见](http://naotu.baidu.com/file/5b20bc63ca50292ff8df5be236ec1e97?token=f53846efae32b3ab)

![产品功能结构图](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/V2.1_function_structure_diagram.jpg?raw=true)

#### 2、产品信息结构图


详细[参见](http://naotu.baidu.com/file/0ab62f902fa8ed684cbcc9578942eb05?token=b1e3a5c414bca935)

注：*表示<超级饲养员>/购买后才拥有的功能


#### 3、物体识别流程图

[参见](https://www.processon.com/view/link/5bfe6432e4b006dc83a82a2f)

![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/%E6%95%B0%E6%8D%AE%E6%B5%81%E7%A8%8B%E5%9B%BE.jpg?raw=true)


### 四、产品原型
* 产品原型文档见[链接](https://bingxin70aa.github.io/present_Axure/)

* 可交互产品原型见[链接](https://bingxin70aa.github.io/Axure_interactive_care_app/)

###### 单词cool
![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/V2.1_prototype_word.jpeg?raw=true)

###### 企鹅（默认页面）

![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/V2.1_prototype_penguin.jpeg?raw=true)

* 通过分析图像的API调用，识别出被测对象的名字并返回中文+英文注释

###### PK榜

![pk榜](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/V2.1_portotype_pk.jpeg?raw=true)

###### 我的

![image](https://github.com/bingxin70aa/API_ML_AI/blob/master/img/V2.1_prototype_mine.jpeg?raw=true)




### 五、产品进度
- [x] app产品框架
- [x] Azure-计算机视觉-标记图像 api 调用
- [x] 有道志云-翻译API调用
- [ ] 游戏规则

### 六、产品使用关键AI或机器学习之API的输出入展示

#### 1、Azure
**Azure-标记图像api**

[***azure_cv_API_request***](https://github.com/bingxin70aa/API_ML_AI/blob/master/azure_cv_API_request.ipynb)

识别后，输出结果如下：
>['building',
 'outdoor',
 'street',
 'city',
 'people',
 'busy',
 'night',
 'ride',
 'crowd']
-------------------

**有道志云-翻译API**
* [***youdao_translation_api_request***](https://github.com/bingxin70aa/API_ML_AI/blob/master/youdao_translation_api_request.ipynb)




#### 2、TensorFlow Object Detection API(舍弃)
* [***Object_Detaction_api_request***](https://github.com/bingxin70aa/API_ML_AI/blob/master/AzureAPI_vs_ObjectDetectionAPI_vs_baiduAPI_vs_Face%2B%2BAPI%20.ipynb)

#### 3、使用比较分析结果

[参见](https://github.com/bingxin70aa/API_ML_AI/blob/master/AzureAPI_vs_ObjectDetectionAPI_vs_baiduAPI_vs_Face%2B%2BAPI%20.ipynb)
> * Google Object Detection API 
* 格外的强大，同一张图片可以识别出14个对象并且进行截取储存，相比之下Azure_API在识别个数上较为不足。
* 但是其劣势也比较明显，目前尝试的模型仅支持80种物体。之前尝试识别[老虎](http://f2.dn.anqu.com/orgin/NTkzNg==/allimg/120624/30-120624153613.jpg)因为不存在在类型对象中，所以返回的对象变成相差甚远的了“长颈鹿“（giraffe）。
* 识别速度也比较慢，尽管可以调整检测速度(detection_speed)，但相对应的识别精准度也会下降很多，当检测速度调整为fast时同样是该[图片](https://upload-images.jianshu.io/upload_images/14204282-d2168c34274d01ab.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) 仅能识别到7个对象。
>* 百度API
* 识别效果垫底，肉眼可见不赘述
>* Face++_Detect Scene And Object API
* 相比之下，Face++的API精准度远不如Azure和谷歌的API，不仅将对象的空间误识别为超市（事实上是饭堂），数量上也并没有优势。


* 速度：百度>Azure>Face++>谷歌
* 精准度：谷歌>Azure>Face++>百度
* 价格（粗略判断）：Face++>Azure>百度>谷歌


* **结论**：因为Azure-标记图像的调用结果已经能满足用户的调用需求，而目前（力所能及之下）调用google Object Detection API的结果缺点过于明显，因此Azure-标记图像更加适用该产品。


#### 4、风险报告
##### 4.1 物体检测API发展性
* 中国产业调研网发布的2016-2022年中国机器视觉市场现状研究分析与发展趋势预测报告认为，国内机器视觉专利数量逐年增加，各大高校及企业纷纷投入精力在机器视觉领域进行研究，国内机器视觉行业正处于一个飞速发展的阶段。国内机器视觉产业主要集中沿海发达省份及北京地区，江苏、广东、浙江、北京、上海五省市专利数量占到全国总申请数量的75%。

##### 4.2 输入输出限制

[参见](https://github.com/bingxin70aa/API_ML_AI/blob/master/Azure_cv_image_tag_risk.ipynb)
* 黑白照片不影响识别结果（不涉及灰度）
* 模糊的照片会对识别个数以及识别准确率带来一定程度的影响
* 在识别人的方面准确率较高，但物体上如果物体离镜头过近、角度问题、或是没有拍摄出物体的基本特征就会导致识别错误或是识别不准确。


* 改进方法：
    * 在进行识别之前，浮现提示语，提醒用户尽量保持平稳拍摄，并提示用户将检测物体的基本特征完整的拍摄出来。

##### 4.3 市场竞争程度
###### 4.3.1 物体识别app市场
* 百度翻译 ：实物检测在该翻译APP的<小应用>中存在。识别物体的流程为：输入图片（相册/相机）——圈出（涂抹出）检测对象——输出中英翻译结果。在识别物体中增加了涂抹的一个步骤，给用户带来了不必要的麻烦，而且识别成功率很低（2/5）.识别失败后就会重新再进行图片输入，流程过于繁琐，给用户带来不好的用户体验。
* 听道/eyemene : 针对于盲人朋友的一款为生活提供便利的 app，因用户画像差异较大便不予以比较。

###### 4.3.2 单词记忆app市场
* 不背单词/墨墨/百词斩/沪江开心词场 ：市面上的单词记忆类app多数是给带有功利性目的（考研/四六级/高考）的用户去背诵单词，而不是为了让用户培养对单词兴趣。且让K12群体与大学生、出国党、工作党都共用一套记忆曲线模型，与“因材施教”的教育理念显然有所悖斥。同时，此类APP也没有针对用户的记忆情况有个评估结果的反馈，很容易猜想是否用户因为缺乏能动性导致多数都半途而废难以坚持完成记忆任务。

### N、后期准备及参考资料
* [PRD初期推进方式及思考](http://note.youdao.com/noteshare?id=9e2e2d3a2cf39b53818b7f4095a0de5e)

* [杂乱无章](http://note.youdao.com/noteshare?id=6fd7164543137fb310dac76de65948fe)

* [Error](http://note.youdao.com/noteshare?id=414a03b9d7e9ccde11c0bbd1a79b8bbd)

    
## 清单
* [产品原型文档](https://bingxin70aa.github.io/present_Axure/#g=1)
* [可交互产品原型](https://bingxin70aa.github.io/Axure_interactive_care_app/)
* 前 PRD.md 现更改为PRD_1.0(肤质检测app）请[参见](https://github.com/bingxin70aa/API_ML_AI/blob/master/PRD_1.0.md)
* 已尝试调用的API的输入输出
    * [***azure_cv_API_request***](https://github.com/bingxin70aa/API_ML_AI/blob/master/azure_cv_API_request.ipynb)
    * [***youdao_translation_api_request***](https://github.com/bingxin70aa/API_ML_AI/blob/master/youdao_translation_api_request.ipynb)
* 使用比较分析（包含Object Detection API的调用）
    * [AzureAPI_vs_ObjectDetectionAPI_vs_baiduAPI_vs_Face++API](https://github.com/bingxin70aa/API_ML_AI/blob/master/AzureAPI_vs_ObjectDetectionAPI_vs_baiduAPI_vs_Face%2B%2BAPI%20.ipynb)
* 使用后风险报告_输入输出限制 [参见](https://github.com/bingxin70aa/API_ML_AI/blob/master/Azure_cv_image_tag_risk.ipynb)
