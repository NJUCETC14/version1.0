from tkinter.dialog import *
from tkinter import *
from tkinter.ttk import *


def modal_ar():
    global image
    #窗口实体
    window = Toplevel()
    window.title('已有模型')
    window.geometry('700x400')


    #Label(window, text='on the window').pack()

    frm = Frame(window)
    frm.pack()
    frm_l = Frame(frm)
    frm_r = Frame(frm)
    frm_r1 = Frame(frm_r)
    frm_r2 = Frame(frm_r)
    Label(frm_r, text='—选择模型———————————').pack()


    frm_l.pack(side='left',padx =0,pady =0)
    frm_r.pack(side='right',padx = 80,pady =20)
    frm_r1.pack(side='top',padx = 0,pady =20)
    Label(frm_r, text='——显示————————————').pack(side='top')
    frm_r2.pack(side='top',padx = 0,pady =20)
    #Label(frm_l, text='on the frm_l1').pack()
    #Label(frm_l, text='on the frm_l2').pack()

    Label(frm_r1, text='已有模型').pack(side='left')
    Label(frm_r2, text='请选择显示参数：').pack()


    #下拉菜单
    keyvar1 = StringVar()
    keyvar1.set('默认模型1')
    items1 = ['模型2', '模型3', '模型4', '模型5', '模型6', '模型7']
    gcombobox1 = Combobox(frm_r1, values=items1, textvariable=keyvar1)
    gcombobox1.pack(side='left')

    #菜单
    menubar = Menu(frm_r1)
    lmenu = Menu(menubar)
    menubar.add_cascade(label = 'File',menu = lmenu)

    items1 = ['New Projects', 'save', 'save as', 'close']
    for item in items1:
        lmenu.add_command(label=item)

    menubar.add_cascade(label='help', menu=lmenu)
    window['menu'] = menubar
    #多选
    l2 = Label(frm_r2, width=20, text='')
    l2.pack()
    def print_selection():
        global varstr1
        varstr1 = StringVar()
        if (var1.get() == 1) & (var2.get() == 0):
            #l2.config(text='输出假阳率 ')
            varstr1 = '输出假阳率 '
        elif (var1.get() == 0) & (var2.get() == 1):
            varstr1 = '输出假阴率 '
          #  l2.config(text='输出假阴率 ')
        elif (var1.get() == 0) & (var2.get() == 0):
           # l2.config(text='什么都不输出')
            varstr1 = '什么都不输出'
        else:
          #  l2.config(text='都输出')
            varstr1 ='都输出'
        print(varstr1)

    var1 = IntVar()
    var2 = IntVar()
    c1 = Checkbutton(frm_r2, text='假阳率', variable=var1, onvalue=1, offvalue=0)
    c1.pack()
    c2 = Checkbutton(frm_r2, text='假阴率', variable=var2, onvalue=1, offvalue=0)
    c2.pack()
    b5 = Button(window, text='确认', command=print_selection)
    b5.pack()

    # 单选
    def print_selection1():
        print('you have selected ' + var.get())
    var = StringVar()
    r1 = Radiobutton(frm_r2, text='假阴率',
                        variable=var, value='A',
                        command=print_selection1)
    r1.pack()
    r2 = Radiobutton(frm_r2, text='假阳率',
                        variable=var, value='B',
                        command=print_selection1)
    r2.pack()
    r3 = Radiobutton(frm_r2, text='其他参数',
                        variable=var, value='C',
                        command=print_selection1)
    r3.pack()

    #画布
    canvas = Canvas(frm_l, bg='white', height=300, width=400)
    image_file = PhotoImage(file='/home/yue/Desktop/ins1.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack()
    #


    #导入
    def daoru():
        pass

    #分析
    def fenxi():
        pass

    #运行
    def run():
        pass

    #按钮模块
    b1 = Button(window,text='数据导入',command= daoru)
    b2 = Button(window, text='输出分析',command = fenxi)
    b3 = Button(window, text = 'run',command = run)
    b4 = Button(window, text = 'close',command = window.quit)
    b1.pack(side='left')
    b2.pack(side='left')
    b4.pack(side='right')
    b3.pack(side='right')

    window.mainloop()




def model_train():
    global image
    #窗口实体
    window = Toplevel()
    window.title('训练模型')
    window.geometry('700x400')


    #Label(window, text='on the window').pack()

    frm = Frame(window)
    frm.pack()
    frm_l = Frame(frm)
    frm_r = Frame(frm)
    frm_r1 = Frame(frm_r)
    frm_r2 = Frame(frm_r)
    frm_r3 = Frame(frm_r)
    frm_r4 = Frame(frm_r)
    frm_r5 = Frame(frm_r)
    Label(frm_r, text='—数据预处理—————————————').pack()


    frm_l.pack(side='left',padx =0,pady =0)
    frm_r.pack(side='right',padx = 60,pady =20)
    frm_r1.pack(side='top',padx = 0,pady =20)
    Label(frm_r, text='——网络——————————————————').pack(side='top')
    frm_r2.pack(side='top',padx = 0,pady =13)
    frm_r3.pack(side='top',padx = 0,pady =16)
    Label(frm_r, text='——参数修改————————————————').pack(side='top')
    frm_r4.pack(side='top',padx = 0,pady =13)
    frm_r5.pack(side='top',padx = 0,pady =16)


    Label(frm_r1, text='数据预处理方法').pack(side='left')
    Label(frm_r2, text='选择网络').pack(side='left')


    #下拉菜单
    #右边1框架
    keyvar2 = StringVar()
    keyvar2.set('关键字')
    items2 = ['复制', '方法2', '方法3', '方法4']
    gcombobox2 = Combobox(frm_r1, values=items2, textvariable=keyvar2)
    gcombobox2.pack(side='left')
    #右边2框架
    keyvar3 = StringVar()
    keyvar3.set('关键字')
    items3 = ['CNN', 'RNN', 'SVM']
    gcombobox3 = Combobox(frm_r2, values=items3, textvariable=keyvar3)
    gcombobox3.pack()

    #输入
    entryvar4 = StringVar()
    glabel4 = Label(frm_r3, text='层数：')
    gentry4 = Entry(frm_r3, textvariable=entryvar4)
    glabel4.pack(side ='left')
    gentry4.pack()

    #输入2
    entryvar5= StringVar()
    glabel5 = Label(frm_r4, text='推荐参数范围：')
    gentry5 = Entry(frm_r4, textvariable=entryvar5)
    glabel5.pack(side ='left')
    gentry5.pack()

    entryvar6 = StringVar()
    glabel6 = Label(frm_r5, text='选择参数值：')
    gentry6 = Entry(frm_r5, textvariable=entryvar6)
    glabel6.pack(side ='left')
    gentry6.pack()


    #菜单
    menubar = Menu(frm_r1)
    lmenu = Menu(menubar)
    menubar.add_cascade(label = 'File',menu = lmenu)
    menubar.add_cascade(label = 'Help',menu = lmenu)

    items1 = ['New Projects', 'Save', 'Save as', 'Close']
    for item in items1:
        lmenu.add_command(label=item)
    window['menu'] = menubar

    #画布
    canvas = Canvas(frm_l, bg='white', height=300, width=400)
    image_file = PhotoImage(file='/home/yue/Desktop/ins1.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack()
    #
    '''
       def print_selection():
            print('you have selected ' + var.get())
    '''

    #导入
    def daoru():
        pass

    #分析
    def fenxi():
        pass

    #运行
    def run():
        pass

    #按钮模块
    b1 = Button(window,text='数据导入',command= daoru)
    b2 = Button(window, text='保存模型',command = fenxi)
    b3 = Button(window, text = 'run',command = run)
    b4 = Button(window, text = 'close',command = window.quit)
    b1.pack(side='left')
    b2.pack(side='left')
    b4.pack(side='right')
    b3.pack(side='right')

    window.mainloop()




win1 = Tk()
win1.title('工具箱')
win1.geometry('700x400')
b1 = Button(win1,text='训练数据',command= model_train)
b2 = Button(win1, text='已有模型',command = modal_ar)
b3 = Button(win1, text='关闭',command = win1.quit)
varstr3 = StringVar()
b1.place(x=300, y=100)
b2.place(x=300, y=150)
b3.place(x=300, y=200)
win1.mainloop()