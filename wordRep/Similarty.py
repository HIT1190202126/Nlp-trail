import numpy as np

result=np.load("svd-result.npy")
vec1=result[1,:]#蒙牛很牛
vec2=result[10,:]#蒙牛 挺牛的
vec3=result[0,:]#我不是蒙牛、没你想象那么纯。--要不要这么讽刺啊？蒙牛好尴尬。。。

sim1=np.sum(vec1*vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))
print(sim1)
sim2=np.sum(vec3*vec2)/(np.linalg.norm(vec3)*np.linalg.norm(vec2))
print(sim2)