import re
pattern='黑客|破解|反爬'
s='我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗?'
new_s=re.sub(pattern,'XXX',s)
print(new_s)
print('-'*50)
s2='https://www.bilibili.com/video/BV1wD4y1o7AS?spm_id_from=4'
pattern2='[//|/|?]'
lst=re.split(pattern2,s2)
print(lst)
