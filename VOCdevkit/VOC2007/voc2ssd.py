#----------------------------------------------------------------------#
#   验证集的划分在train.py代码里面进行
#   test.txt和val.txt里面没有内容是正常的。训练不会使用到。
#----------------------------------------------------------------------#
import os
import random

random.seed(0)

xmlfilepath = r'Annotations'
saveBasePath = r'ImageSets/Main'

#----------------------------------------------------------------------#
#   想要增加测试集修改train_percent
#   train_percent不需要修改
#----------------------------------------------------------------------#
trainval_percent = 1  # 划分整个数据集百分之几作为trainval
train_percent = 0.8  # trainval中train所占比例

temp_xml = os.listdir(xmlfilepath)
total_xml = []
for xml in temp_xml:
    if xml.endswith(".xml"):
        total_xml.append(xml)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

print("train and val size", tv)
print("train size", tr)

# ftrainval = open('ImageSets/Main/trainval.txt', 'w')  # 这种方式打开也可以
ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')

### 注意ftrain、ftest、fval是可以调换位置的，根据需要改变
### 正常的顺序是 ftrain.write(name)、fval.write(name)、ftest.write(name)
### 在此，我将fval.write(name)、ftest.write(name)调换了，因为划分需要
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            ftest.write(name)
    else:
        fval.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
