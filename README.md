# Didi_plus_plus
----
## 背景
   **2016微软penta hackathon 最具商业价值奖 滴滴打车plus**
   
在当今时代，社会日益多元化，人们的要求也呈现了多元化趋势。纵观所有的打车软件，无一例外的都是抢单制。作为乘客，我们只能被司机所选择，而没有自己的主动选择权。我们所做的，就是通过大数据的分析，得到司机的各项评价指标。在用户选车的时候，根据用户个性化的需求，为用户推荐适合的司机与车辆。

------
## 实现过程

对于已经获得的出租车数据进行处理，数据格式如下
    
![image](/src/taxi.jpg)

通过对特征进行提取，对每名司机进行评估，制作专属“名片”，存储在数据库中，下面是其中一个司机的“名片”
    
![image](/src/idcard.jpg)   

index.html为前端文件，使用html css javascript编写，由于github pages为静态网页，该网页的demo可以下载之后查看
   
   
通过调用百度地图的API,结合后端处理的数据，对用户进行推荐数据库由于大小超出限制，打包上传query.py可以对其进行查询
   
----
If you have questions or ideas, just create an issue. Acknowledgement for my teammates [Weihong Lin](https://github.com/lwher), [Junping Pan]() and [Zehua Zhang]().

