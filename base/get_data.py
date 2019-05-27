# import os,sys
#
# import yaml
#
#
import os

import yaml


class GetData(object):
    #
    # def __init__(self):
    #     pass

    def get_data(self, filename):
        # 使用os.path.abspath("path"),调用这个函数,可以放入自己想要的相对路径
        with open(os.path.abspath("C:\\Users\\bob1994\\Desktop\\代码\\homework") + os.sep + "data" + os.sep + filename, "r",
                  encoding="utf-8") as f:
            # with open( "C:\\Users\\bob1994\\Desktop\\homework\\data\\data_001.yml", "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
#
# #

#
# def getdata():
#     with open("C:\\Users\\bob1994\\Desktop\\homework\\data\\data_001.yml", "r", encoding="utf-8") as f:
#         return yaml.safe_load(f)

# print(os.getcwd() + os.sep + "data" + os.sep + "data_001.yml")
# def getdata(self,filename):
#     with open(os.getcwd() + os.sep + filename, "r", encoding="utf-8") as f:
#         return yaml.safe_load(f)

#
# a = GetData.getdata("data_001.yml")
# print(a)
