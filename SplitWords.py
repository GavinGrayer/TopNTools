import glob
import random
import jieba
# from PyInstaller.utils.hooks import collect_data_files
#
# datas = collect_data_files("jieba")

#[1] 加载语料库
jieba.load_userdict('./user_dict.txt')

# [2] 读取内容
def get_content(path):
    with open(path, encoding='utf-8', errors='ignore') as f:
        content = ''
        for line in f:
           #去除空行
            line = line.strip()
            content += line
        return content

# [3] 样本TopK 
def get_TF(words, topK=10):
    tf_dic = {}
    #遍历words中的每个词，如果这个词在tf_dic中出现过，则令其加一。
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) + 1
        #将字典tf_dic排序后取出前topK.
    return sorted(tf_dic.items(), key = lambda x: x[1], reverse=True)[:topK]

# [4] 整理常用的停用词
def stop_words(path):
    with open(path,encoding='utf-8') as f:
        return [l.strip() for l in f]
    
#修改cut函数,path是你的停用词表所放的位置
def cut(content,path):
    split_words = [x for x in jieba.cut(content) if x not in stop_words(path)]
    return split_words 


def main():
    # 读取文件内容
    files = glob.glob('./data.txt')
    corpus = [get_content(x) for x in files]
    print(len(corpus))
 
    # sample_inx = random.randint(0, len(corpus))
    sample_inx = 0
    split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words('./stop_words.txt')]
    #print('样本之一：' + corpus[sample_inx])
    print('样本分词效果：' + '/'.join(split_words))
    print('样本的topK(10)词：' + str(get_TF(split_words)))
    return get_TF(split_words)


def split(data='今天的天气怎么样你今天感觉好点了吗'):
    corpus = data.split()
    sample_inx = 0
    split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words('./stop_words.txt')]
    #print('样本分词效果：' + '/'.join(split_words))
    return get_TF(split_words)
    
# split()
#main()