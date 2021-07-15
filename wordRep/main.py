import numpy as np
import re
import jieba

# 读取文档转字符串,并对字符串进行分词
def getFILE(name):
    f=open(name,"r",encoding='utf-8')
    line=f.readline()
    line=line[:-1]
    A=[]
    while line:
        line=f.readline()
        str=line
        str=re.sub("(-)?[0-9]\t","",str)
        listJieba = jieba.lcut(str)  # 对句子进行分词
        A.append(listJieba)
        line=line[:-1]
    f.close()
    return  A

# 制造one-hot向量
def getOneHot(partitionStr):
    global OneHot
    OneHot = []
    for sentence in partitionStr:
        for word0 in sentence:
            if not (word0 in OneHot):
                OneHot.append(word0)
    return  OneHot

#对partitionStr里面的句子进行挨个转换,
def convert(wordList,partionStr):
    M_rol= len(partionStr)  #行
    M_col= len(wordList)    #列
    retM=np.zeros((M_rol,M_col))
    i=0
    for sentence in partitionStr:
        for word0 in sentence:
            retM[i][wordList.index(word0)]=retM[i][wordList.index(word0)]+1
        i=i+1
    print(np.shape(retM))
    return  retM

#对矩阵进行点互信息的处理,照着学长的代码敲的,感觉有点不明白..
def pmi(M,positive=True):
    col_tols=M.sum(axis=0)
    row_tols=M.sum(axis=1)
    total=col_tols.sum()
    expect=np.outer(row_tols,col_tols)/total
    M=M/expect
    with np.errstate(divide='ignore'):
        M=np.log(M)
    M[np.isinf(M)]=0.0
    if(positive):
        M[M<0]=0.0
    print(np.shape(M))
    return M


def toSVD():
    OH = getOneHot(partitionStr)
    M0 = convert(OH, partitionStr)
    np.save("M0.npy", M0)
    print("进行svd")
    U, s, vh = np.linalg.svd(M0,full_matrices=1)
    print(s)
    np.save("svd-U.npy", U)
    np.save("svd-s.npy", s)
    np.save("svd-vh.npy", vh)


#主函数
if __name__ == '__main__':
    partitionStr=getFILE("corps\\chinese.txt")
    #print(partitionStr)
    print(partitionStr[1])
    print(partitionStr[10])

# partitionStr=np.mat(partitionStr)
   # np.save("jieBaFenCi.npy", partitionStr)

    #toSVD()

