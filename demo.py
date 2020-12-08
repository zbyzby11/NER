# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2020/12/8
@Description: 
"""
from ner.ner_core import Ner

text = "我叫张三丰，我是东南大学的一名学生。"

model1 = Ner("nltk")
model2 = Ner("stanford")
model3 = Ner("fasthan")
model4 = Ner("bbc", ip="10.201.221.229")

res1 = model1.get_ner(text)
res2 = model2.get_ner(text)
res3 = model3.get_ner(text)
res4 = model4.get_ner(text)

print(res1)  # [[(2, 5, 'person', '张三丰'), (8, 12, 'org', '东南大学')]]
print(res2)  # [('张三丰', 'PERSON'), ('东南', 'ORGANIZATION'), ('大学', 'ORGANIZATION')]
print(res3)  # [['张三丰', 'NR'], ['东南大学', 'NT']]
print(res4)  # [('张三丰', 'PER'), ('东南大学', 'ORG')]
