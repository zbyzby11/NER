# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 11:36
# @Author  : zby
# @File    : ner_core.py
"""
ner模型的封装
三种模型，一个是nltk，一个是fasthan，一个是stanford ner
"""
import os

import fool

from bert_base.client import BertClient
from fastHan import FastHan
from stanfordcorenlp import StanfordCoreNLP
from config.configuration import Config
from ner.result import result_to_json


class Ner(object):
    def __init__(self, model_name, ip=None):
        config = Config()
        self.model_name = model_name
        if self.model_name == "fasthan":
            self.nltk_model = FastHan(model_type="base")
        if self.model_name == "stanford":
            path = config.project_dir
            self.stanford_model = StanfordCoreNLP(os.path.join(path, 'model\stanford-corenlp-full-2016-10-31'),
                                                  lang='zh')
        if self.model_name == "bbc":
            if not ip:
                raise ValueError("bbc模型必须填入ip")
            self.bbc_model = BertClient(ip, ner_model_dir=None, show_server_config=False, check_version=False,
                check_length=False, mode='NER')

    def get_ner(self, string):
        if self.model_name == "fasthan":
            answer = self.nltk_model(string, target="NER")
            return answer[0]
        elif self.model_name == "nltk":
            _, answer = fool.analysis(string)
            return answer
        elif self.model_name == "stanford":
            answer = []
            res = self.stanford_model.ner(string)
            for token, tag in res:
                if tag == "PERSON" or tag == "ORGANIZATION" or tag == "LOCATION":
                    answer.append((token, tag))
            return answer
        elif self.model_name == "bbc":
            rst = self.bbc_model.encode([list(string)], is_tokenized=True)
            res = result_to_json(string, rst[0])
            return res
        else:
            raise ValueError("model_name只能是fasthan、nltk、stanford、bbc四种之一")
