# 测试独立git
#加一行注释
raw_texts = [
    "  这是第一条测试文本，长度足够用来验证有效性，我们需要确保它的字符数超过五十个，这样才能返回有效结果。  \n",
    "短文本\n",
    "",
    "  第二条长文本，同样需要满足长度要求，用来测试批量处理的正确性，确保每一条数据都能被正确清洗和校验。  ",
    123,
    None
]

def clean_text(t):
    return t.strip().replace('\n', '')

def valid(t):
    return len(t) >= 50, len(t)

def batch_process(data_list):
    result = []
    for item in data_list:
        try:
            cleaned = clean_text(item)
            is_valid, length = valid(cleaned)
            item_text = {
                'text': cleaned,
                'length': length,
                'is_valid': is_valid
            }
        except (TypeError, AttributeError):
            item_text = {
                'text': '',
                'length': 0,
                'is_valid': False
            }
        result.append(item_text)
    return result

res = batch_process(raw_texts)
print(res)

with open('text_result.txt', 'w', encoding='utf-8') as f:
    for item in res:
        status = '有效' if item['is_valid'] else '无效'
        f.write(f"[{status}] 长度:{item['length']} 内容:{item['text']}\n")
