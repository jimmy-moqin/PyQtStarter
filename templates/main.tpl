import os
uipath = os.path.dirname(os.path.abspath(__file__)) + '/ui/'
os.system("pyuic5 \"" + uipath + "{{uifn}}.ui\" -o \""+ uipath +"{{uifn}}.py\"")

from PyQt5.QtWidgets import QApplication

from src.{{lfn}} import {{lcn}}

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Ui_{{lcn}}={{lcn}}()
    Ui_{{lcn}}.show()
    sys.exit(app.exec_())

