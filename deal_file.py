import os
# 预处字符串
def clear_comment(comment):
    comment = comment.strip(' ')
    comment = comment.strip('i')
    comment = comment.strip('I')
    comment = comment.replace('、', '')
    comment = comment.replace('~', '。')
    comment = comment.replace('～', '')
    comment = comment.replace('{"error_message": "EMPTY SENTENCE"}', '')
    comment = comment.replace('…', '')
    comment = comment.replace('\r', '')
    comment = comment.replace('\t', '')
    comment = comment.replace('\f', '')
    # comment = comment.replace('\n', '')
    comment = comment.replace('/', '')
    comment = comment.replace('、', ' ')
    comment = comment.replace('/', '')
    # comment = comment.replace(' ', '')
    # comment = comment.replace(' ', '')
    comment = comment.replace('_', '')
    comment = comment.replace('?', ' ')
    comment = comment.replace('？', ' ')
    comment = comment.replace('了', '')
    comment = comment.replace('➕', '')
    comment = comment.replace('\ufeff', '')
    comment = comment.replace(' the ', ' ')
    comment = comment.replace(' a ', ' ')
    comment = comment.replace(' of ', ' ')
    comment = comment.replace(' is ', ' ')
    comment = comment.replace(' I ', ' ')
    comment = comment.replace(' i ', ' ')
    comment = comment.replace(' to ', ' ')
    return comment

# 获取文件夹下所有的翻译内容
def get_content(trn_wath):
    file_content = []
    for (dirpath, dirnames, filenames) in os.walk(trn_wath):
        for file_name in filenames:
            file_wath = os.path.join(dirpath,file_name)
            # print(file_wath)
            if os.path.exists(file_wath) is False:
                return None

            fd = open(file_wath,'r',encoding="UTF-8")
            text = fd.readline()
            text = clear_comment(text)
            # print(text)
            file_content.append(text)
            # print(file_content)
            fd.close()
    return  file_content

#建立文件
def creat_file(content):
    fd = open("train_txt", 'w', encoding="Utf-8")
    fd.write(content)
    fd.close()
    return

