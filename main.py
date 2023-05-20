import os

import jinja2


def mk(path):
    '''make dir'''
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print('The project dir is already exist! plsease change the project name!')

def addInit(path):
    '''add init file'''
    with open(path + '/__init__.py','w') as f:
        f.write('')


def create(pjn,mwm,uifn,wn,lfn,lcn):
    path = os.getcwd()
    # get file path
    tplPath = os.path.dirname(os.path.abspath(__file__)) + '/templates'
    # create project folder
    mk(path + '/' + pjn)
    # create src folder
    mk(path + '/' + pjn + '/src')
    # create ui folder
    mk(path + '/' + pjn + '/ui')
    # create resource folder
    mk(path + '/' + pjn + '/resource')
    # create img folder
    mk(path + '/' + pjn + '/resource/img')
    # create qrc folder
    mk(path + '/' + pjn + '/resource/qrc')
    # create qss folder
    mk(path + '/' + pjn + '/resource/qss')
    # create utils folder
    mk(path + '/' + pjn + '/utils')
    # create test folder
    mk(path + '/' + pjn + '/test')

    # add init file
    addInit(path + '/' + pjn + '/src')
    addInit(path + '/' + pjn + '/ui')
    addInit(path + '/' + pjn + '/utils')
    
    # create ui file
    if mwm == "MainWindow":
        jinja2.Template(open(tplPath + '/MainWindow.tpl').read()).stream(wn=wn).dump(path + '/' + pjn + '/ui/' + uifn + '.ui')
    elif mwm == "Widget":
        jinja2.Template(open(tplPath + '/Widget.tpl').read()).stream(wn=wn).dump(path + '/' + pjn + '/ui/' + uifn + '.ui')
    
    # create main file
    jinja2.Template(open(tplPath + '/main.tpl').read()).stream(lfn=lfn,lcn=lcn,uifn=uifn).dump(path + '/' + pjn + '/main.py')

    # create logic file
    jinja2.Template(open(tplPath + '/mainlogic.tpl').read()).stream(uifn=uifn, wn=wn, lcn=lcn, mwm=mwm).dump(path + '/' + pjn + '/src/' + lfn + '.py')

# welcome
welcome = " Welcome to the PyQtStarter! "

setProjectName_en = "Please set the project name: "
setProjectName_zh = "请设置项目名称："
setUiFileName_en = "Please set the ui file name: "
setUiFileName_zh = "请设置ui文件名："
setMainWindowMode_en = "1. MainWindow \n2. Widget\nPlease choose the MainWindow mode:"
setMainWindowMode_zh = "1. MainWindow \n2. Widget\n请选择主窗口模式:"
setWindowName_en = "Please set the MainWindow name: "
setWindowName_zh = "请设置主窗口名称："
setLogicFileName_en = "Please set the main logic file name: "
setLogicFileName_zh = "请设置逻辑文件名："
setLogicClassName_en = "Please set the main logic class name: "
setLogicClassName_zh = "请设置主逻辑类名："
print("{:=^50}".format(welcome))

while True:
    # choose language
    print("1. English")
    print("2. 中文")
    languageNum = input("Please choose a language/请选取一种语言:")
    if languageNum == "1":
        lang = "en"
        pjn = input(setProjectName_en)
        mwmNum = input(setMainWindowMode_en)
        if mwmNum == "1":
            mwm = "MainWindow"
        elif mwmNum == "2":
            mwm = "Widget"
        else:
            print("Wrong input!/输入错误！")
            break
        uifn = input(setUiFileName_en)
        wn = input(setWindowName_en)
        lfn = input(setLogicFileName_en)
        lcn = input(setLogicClassName_en)
        create(pjn,mwm,uifn,wn,lfn,lcn)
        print("The project has been created successfully!")
        print("-"*50)
        print("You can Input 'cd " + pjn + "' to enter the project folder!")
        print("You can run the project by 'python main.py'!")
        break
        
    elif languageNum == "2":
        lang = "zh"
        pjn = input(setProjectName_zh)
        mwmNum = input(setMainWindowMode_zh)
        if mwmNum == "1":
            mwm = "MainWindow"
        elif mwmNum == "2":
            mwm = "Widget"
        else:
            print("Wrong input!/输入错误！")
            break
        uifn = input(setUiFileName_zh)
        wn = input(setWindowName_zh)
        lfn = input(setLogicFileName_zh)
        lcn = input(setLogicClassName_zh)
        create(pjn,mwm,uifn,wn,lfn,lcn)
        print("项目创建成功！")
        print("-"*50)
        print("输入 cd " + pjn + " 进入项目文件夹！")
        print("通过 python main.py 运行项目！")
        break

    else:
        print("Wrong input!/输入错误！")
        break
    



