'''
特征工程：将原始文本、图片、数据 转化为可以用于机器学习的数字特征
---->特征值

文本、字典的特征提取
图像的特征提取:在深度学习中用
文本、字典的特征提取方法：


数据集：
    带标签(特征值；目标值)
    不带标签(特征值；)
'''

'''
对 字典型数据的特征提取
用向量来表示 特征(x1,x2,x3,x4):一维数组
用矩阵来存储 一个样本的特征[[x1,x2,x3][y1,y2,y3]....]： 二维数组

特征提取API：
sklearn.feature_extraction

文本向量化方法：
one-hot编码向量化文本、TF-IDF文本向量化、word2vec等
'''
from sklearn.feature_extraction import DictVectorizer
def dict_demo():
    """
    对“字典类型”的数据进行特征抽取
    应用场景：
        当数据中代表类别的字段较多，先转化为字典；
        或者数据本身是字典
    将代表类型的city字符串转化为 one-hot编码 ，数值保留
    sparse=true稀疏矩阵转化为...
        意义：当矩阵的绝大部分数值为零，且非零元素呈不规律分布时，这种稀疏矩阵，如one-hot编码就会产生稀疏矩阵
             消耗大量资源存储，转化后1. 压缩矩阵对象的内存台面空间2. 加速多数机器学习程序
             使用稀疏矩阵节省空间
    :return: None
    """
    data = [{'city': '北京','temperature':100}, {'city': '上海','temperature':60}, {'city': '深圳','temperature':30}]
    # 1、实例化一个转换器类
    transfer = DictVectorizer(sparse=False)#返回非稀疏sparse矩阵
    # 2、调用fit_transform
    data_ = transfer.fit_transform(data)#data:字典或者包含字典的迭代器返回值：
    print("返回的结果:\n", data_) #将代表类型的city字符串转化为 one-hot编码 ，数值保留
    # 打印特征名字
    print("特征名字：\n", transfer.get_feature_names_out())

    return None

'''
2.2 文本特征提取
作用：对文本数据进行特征值化
sklearn.feature_extraction.text.CountVectorizer(stop_words=[])
返回词频矩阵
CountVectorizer.fit_transform(X) X:文本或者包含文本字符串的可迭代对象 返回值：返回sparse矩阵
CountVectorizer.inverse_transform(X) X:array数组或者sparse矩阵 返回值:转换之前数据格
CountVectorizer.get_feature_names() 返回值:单词列表
sklearn.feature_extraction.text.TfidfVectorizer

'''

from sklearn.feature_extraction.text import CountVectorizer

def text_count_demo():
    """
    对英文文本进行特征抽取，countvetorizer
    :return: None
    步骤：
        根据总样本生成词典['dislike', 'is', 'life', 'like', 'long', 'python', 'short', 'too']
        根据样本：返回对应的词频矩阵

    对中文文本特征提取：
        因为英文是已经分开的所以不要分词
        但是对于中文，需要分词，
        如：对数据处理，jieba分词
    """
    data = ["life is short,i like like python", "life is too long,i dislike python"]
    # 1、实例化一个转换器类
    # transfer = CountVectorizer(sparse=False)
    transfer = CountVectorizer()
    # 2、调用fit_transform
    data = transfer.fit_transform(data)
    print("文本特征抽取的结果：\n", data.toarray())
    print("返回特征名字：\n", transfer.get_feature_names_out())

    return None

import jieba
def text_count_demo1():
    """
    对中文文本进行特征抽取，countvetorizer
    :return: None

    """
    data = ["目前对于无法获取因子值的样本直接进行了剔除", "该剔除逻辑会导致样本数量发生变化"]
    data = [" ".join(list(jieba.cut(i))) for i in data]
    # 1、实例化一个转换器类
    # transfer = CountVectorizer(sparse=False)
    #对中\英文这里可以选择去除停用词
    transfer = CountVectorizer(stop_words=['的'])
    # 2、调用fit_transform
    data = transfer.fit_transform(data)
    print("文本特征抽取的结果：\n", data.toarray())
    print("返回特征名字：\n", transfer.get_feature_names_out())

    return None

'''
通过 sklearn.feature_extraction.text. CountVectorizer
我们得到了词频矩阵；
通常意义上，我们将高词频的词，代表这篇文章
但是如果，有2篇文章，词xxx都在这两篇文章中大量出现， 这个结果就不准确
==============================================================
'''


'''
该如何处理某个词或短语在多篇文章中出现的次数高这种情况
TF-IDF
当有TF(词频)和IDF(逆文档频率)后，将这两个词相乘，就能得到一个词的TF-IDF的值。
某个词在文章中的TF-IDF越大，那么一般而言这个词在这篇文章的重要性会越高，所以通过计算文章中各个词的TF-IDF，由大到小排序，排在最前面的几个词，就是该文章的关键词。

TF-IDF的优点是简单快速，而且容易理解。缺点是有时候用词频来衡量文章中的一个词的重要性不够全面，有时候重要的词出现的可能不够多，
而且这种计算无法体现位置信息，无法体现词在上下文的重要性。如果要体现词的上下文结构，那么你可能需要使用word2vec算法来支持。

TF = 某词在文章中出现次数/文章总词数量（标准化）
IDF =log(文档总数/包含该词的文档+1)

应用领域：
对大量文章:文本分类
'''

from sklearn.feature_extraction.text import TfidfVectorizer
import jieba

def cut_word(text):
    """
    对中文进行分词
    "我爱北京天安门"————>"我 爱 北京 天安门"
    :param text:
    :return: text
    """
    # 用结巴对中文字符串进行分词
    text = " ".join(list(jieba.cut(text)))

    return text

def text_chinese_tfidf_demo():
    """
    TF-IDF
    :return: None
    """
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    # 将原始数据转换成分好词的形式
    text_list = []
    for sent in data:
        text_list.append(cut_word(sent))
    print(text_list)

    # 1、实例化一个转换器类
    # transfer = CountVectorizer(sparse=False)
    transfer = TfidfVectorizer(stop_words=['一种', '不会', '不要'])
    # 2、调用fit_transform
    data = transfer.fit_transform(text_list,keyword=5)
    print("文本特征抽取的结果：\n", data.toarray())   #返回值：3行（对应3个文本）；32列（对应32个特征名字）
    print("返回特征名字：\n", transfer.get_feature_names_out())

    return None

if __name__=='__main__':
    text_chinese_tfidf_demo()
