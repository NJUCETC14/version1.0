import math
import numpy as np

class preTreating:
    dataFilePath = ""
    outFilePath = "out.txt"
    data = []

    def __init__(self, path, num_feature):
        self.dataFilePath = path

    # ==============================
    # 功能：读取数据文件
    # 任务：杂波去除、航迹预测、机型识别
    # 作者：沈卓恺
    # 修改日期：2018-3-7
    # ==============================
    def readFile(self):
        lines = open(self.dataFilePath).readlines()
        for i in range(1, len(lines)):
            data = lines[i].split()
            self.data.append(data)


    # ==============================
    # 功能：数据归一化
    # 任务：杂波去除、航迹预测
    # 作者：冯帆
    # 修改日期：2018-3-8
    # ==============================
    def normalization(self, f_range, a,b):
        # f_range:[[a, b], [-1], [...]...]
        # f_range.length is the number of all the features
        # if the corresponding feature needs to be normalization, the index element is [a, b]
        # else, the element is [-1]
        # ! the f_range lists is read from the GUI
        print(">>> Start normalization for \nfeatures...", f_range.length)
        f_range = [a,b]
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                arr = np.array(self.data[i])
                maxValue = arr.max()
                minValue = arr.min()
                k = (b-a)/(maxValue-minValue)
                norX = k*(float(self.data[i][j])-minValue)+a
                self.data[i][j] = str('{:.2f}'.format(norX))
        print("Normalization done...")
        return
     
    # ==============================
    # 功能：将极坐标修改为直角坐标
    # 任务：航迹预测
    # 作者：沈卓恺
    # 修改日期：2018-3-9
    # ==============================
    def modifingAxis(self, theta, radius):
        # radius, degree Indicate the index of the features
        print(">>> Start modify the AXIS...")
        for i in range(len(self.data)):
            x = float(self.data[i][radius]) * math.cos(float(self.data[i][theta]) / 180 * math.pi)
            y = float(self.data[i][radius]) * math.sin(float(self.data[i][theta]) / 180 * math.pi)
            self.data[i][theta] = str('{:.2f}'.format(x))
            self.data[i][radius] = str('{:.2f}'.format(y))
        print("Modify done...")
        return

    # ==============================
    # 功能：数据扩充，对样本数进行统计，少例样本扩充
    # 任务：杂波去除
    # 作者：冯帆
    # 修改日期：2018-3-8
    # ==============================
    def expanding_1(self):
        len_ = len(self.data)
        
        print(">>> Start expanding...\noriginal length: ", len_)
        expanded_data = []
        raw_data = np.array(self.data)
        noise_num = sum(raw_data[:,7] == '-1')
        signal_num = sum(raw_data[:,7] == '1')
        
        if(noise_num > signal_num):
            for index in range(int(round(noise_num/signal_num))):
                for item in raw_data[raw_data[:,7] == '1'].copy():
                    expanded_data.append(item.tolist()) 
            for item in raw_data[raw_data[:,7] == '-1'].copy():
                expanded_data.append(item.tolist())
        if(noise_num < signal_num):
            for index in range(int(round(signal_num/noise_num))):
                for item in raw_data[raw_data[:,7] == '-1'].copy():
                    expanded_data.append(item.tolist())
            for item in raw_data[raw_data[:,7] == '1'].copy():
                expanded_data.append(item.tolist())
        self.data = expanded_data
        return


    # ==============================
    # 功能：数据扩充：通过旋转航迹的方法扩充航迹数据
    # 任务：航迹预测
    # 作者：沈卓恺
    # 修改日期：2018-3-9
    # ==============================
    def expanding_2(self, theta):
        len_ = len(self.data)
        print(">>> Start expanding...\noriginal length: ", len_)
        new_data = []
        for i in range(len_):
            data = self.data[i].copy()
            old_theta = self.data[i][theta]
            for degree in range(18):
                new_theta = 20 * degree + float(old_theta)
                if new_theta >= 360:
                    new_theta -= 360
                data[theta] = new_theta
                new_data.append(data.copy())
        self.data = new_data.copy()
        print("Afterwards：", len(self.data), "\nExpanding done...")
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

    def testFile(self):
        fp = open(self.outFilePath, "w")
        print(">>> Start output...FilePath:"+self.outFilePath)
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                fp.write(str(self.data[i][j]))
                fp.write("\t")
            fp.write("\n")
        print("Output done...")


task = preTreating("txt/p_1_1.txt", 14)
task.readFile()
task.expanding_2(2)
task.modifingAxis(2, 3)
task.testFile()
