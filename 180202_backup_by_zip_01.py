# -*- coding: utf-8 -*-
import os
import time

# 需要备份的文件
source=['/Users/wangyan/IdeaProjects/Weather']
# 存储备份文件的地址
target_dir = '/Users/wangyan/PycharmProjects/StudyPy01'

# 备份文件被打包为zip
# zip文件名由当前日期时间组成
target=target_dir+os.sep+\
    time.strftime('%Y%m%d%H%M%S')+'.zip'
# os.sep :会根据高做系统给出相应的分隔符

# 如果目标目录不存在，则进行创建
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

#使用zip command将文件打包为zip格式
zip_command='zip -r {0} {1}'.format(target,' '.join(source))

print('zip command is: ',zip_command)
print('running')
if os.system(zip_command)==0:
    print('Successful backup to', target)
else:
    print('backup failed')