

class preTreating:
    dataFilePath = ""
    data = []

    def __init__(self, path):
        self.dataFilePath = path

    # ==============================
    # 功能：读取数据文件
    # 任务：杂波去除、航迹预测、机型识别
    # 作者：沈卓恺
    # 修改日期：2018-3-7
    # ==============================
    def readFile(self):
        self.data = open(self.dataFilePath).readlines()

    # ==============================
    # 功能：数据归一化
    # 任务：杂波去除、航迹预测
    # 作者：
    # 修改日期：
    # ==============================
    def normalization(self, f_range):
        # f_range:[[a, b], [-1], [...]...]
        # f_range.length is the number of all the feature
        # if the corresponding feature needs to be normalization, the index element is [a, b]
        # else, the element is [-1]
        # ! the f_range lists is read from the GUI
        return

    # ==============================
    # 功能：数据扩充
    # 任务：杂波去除
    # 作者：
    # 修改日期：
    # ==============================
    def expanding_1(self):
        return

    # ==============================
    # 功能：数据扩充
    # 任务：航迹预测
    # 作者：
    # 修改日期：
    # ==============================
    def expanding_2(self):
        return

    # ==============================
    # 功能：航迹截取
    # 任务：航迹预测
    # 作者：
    # 修改日期：
    # ==============================
    def generatingSubtrace(self):
        return

    # ==============================
    # 功能：
    # 任务：
    # 作者：
    # 修改日期：
    # ==============================
    def TODO(self):
        return