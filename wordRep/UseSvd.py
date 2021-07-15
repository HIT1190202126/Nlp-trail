import  numpy as np

U=np.load("svd-U.npy")
s=np.load("svd-s.npy")
vh=np.load("svd-vh.npy")
print(np.shape(U))
s=np.diag(s)
print(np.shape(s))
print(np.shape(vh))
#k=100
k=100
kk=s[0:k,0:k]
print(np.shape(kk))
back=np.dot(U[:,:k],kk)
back=np.dot(back,vh[:k,:])
#print(back)
np.save("svd-result.npy",back)