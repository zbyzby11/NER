# 1. ner工具

此repo使用了如下几个中文ner工具，使用前需按照官方仓库中的说明安装相关依赖、模型等。

（1）foolnltk：https://github.com/rockyzhengwu/FoolNLTK

（2）fasthan：https://github.com/fastnlp/fastHan

（3）stanfordcore：https://github.com/stanfordnlp/CoreNLP

（4）bert+bilstm+crf：https://github.com/macanv/BERT-BiLSTM-CRF-NER

# 2. 快速使用

此仓库集成了上述四种模型，只需简单调用相关模型即可

```python
from ner.ner_core import Ner

text = "我叫张三丰，我是东南大学的一名学生。"

model = Ner(model_name="nltk")
res = model.get_ner(text)
print(res)  # [[(2, 5, 'person', '张三丰'), (8, 12, 'org', '东南大学')]]
```

Ner是一个类，model_name有四种相关参数分别对应不同模型：

（1）"fasthan"对应于fasthan模型，"nltk"对应foolnltk模型，"stanford"对应于斯坦福模型，"bbc"对应于bert+bilstm+crf模型

（2）其中对于bert+bilstm+crf模型，是基于腾讯开源项目bert-as-service的C/S架构的，需要指定ip参数（即服务器端的模型）

（3）stanford模型需要下载相应的模型到"model\stanford-corenlp-full-2016-10-31\"目录下