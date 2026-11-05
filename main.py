import csv
def clean_text(x):
  return x.strip().replace('\n','')
def valid(x):
  num = clean_text(x)
  return len(num)>=50
def write_file(input_file,output_file):
  data = []
  try:
    with open(input_file,'r',encoding='utf-8',newline='') as f:
    read = csv.reader(f)
    next(read)
    for t in read:
      rew_text = t[0]
      txt = clean_text(rew_text)
      v = valid(rew_text)
      length = len(txt)
      data.append({
        'text':txt,
        'length':length, 
        'valid':v
           })
  except FileNotFoundError:
    print('覆盖文件不存在')
    return
  except UnicodeDecodeError:
    print('读取编码错误')
    return
  except Exception as e:
    print(f'读取文件时发生错误:{e}')
    return
  try:
      with open(output_file,'w',encoding='utf-8',newline='') as f:
        write = csv.DictWriter(f,fieldnames=['text','length','valid'])
        write.writeheader()
        write.writerows(data)
  except OSErroor:
    print('写入失败')
    return
  except Exception as e:
    print(f'输入错误:{e}')
    return
if __name__ == '__main__':
  write_file('raw_text.csv','result_text.csv')
