# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 11:06
# @Author  : zby
# @File    : result.py


def result_to_json(string, tags):
    """
    将模型标注序列和输入序列结合 转化为结果
    :param string: 输入序列
    :param tags: 标注结果
    :return:
    """
    item = {"entities": []}
    entity_name = ""
    entity_start = 0
    idx = 0
    last_tag = ''

    res = []

    for char, tag in zip(string, tags):
        if tag[0] == "S":
            # self.append(char, idx, idx+1, tag[2:])
            item["entities"].append({"word": char, "start": idx, "end": idx + 1, "type": tag[2:]})
        elif tag[0] == "B":
            if entity_name != '':
                # self.append(entity_name, entity_start, idx, last_tag[2:])
                item["entities"].append({"word": entity_name, "start": entity_start, "end": idx, "type": last_tag[2:]})
                entity_name = ""
            entity_name += char
            entity_start = idx
        elif tag[0] == "I":
            entity_name += char
        elif tag[0] == "O":
            if entity_name != '':
                item["entities"].append({"word": entity_name, "start": entity_start, "end": idx, "type": last_tag[2:]})
                entity_name = ""
        else:
            entity_name = ""
            entity_start = idx
        idx += 1
        last_tag = tag
    if entity_name != '':
        item["entities"].append({"word": entity_name, "start": entity_start, "end": idx, "type": last_tag[2:]})

    entity_list = item.get("entities")
    if len(entity_list) == 0:
        return []
    for dic in entity_list:
        start_index = dic.get("start", -1)
        end_index = dic.get("end", -1)
        entity_type = dic.get("type", "Other")
        res.append((string[start_index: end_index], entity_type))
    return res
