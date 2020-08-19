#-*-coding:utf-8-*-

def mkdir(path):
    import os
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
 
    if not isExists: # 如果不存在则创建目录
        os.makedirs(path)  
        print('images文件夹创建成功！path路径名：' + path)
        return True
    else: # 如果目录存在则不创建，并提示目录已存在
        print('images文件夹已存在！path路径名：' + path)
        return False