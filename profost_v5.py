from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox, QApplication, QWidget
from PyQt5.Qt import Qt
import Directory
import os, shutil

class Ui_Annotator3_1(object):
    def setupUi(self, Annotator3_1):
        Annotator3_1.setObjectName("Annotator3_1")
        Annotator3_1.resize(1936, 969)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Annotator3_1.sizePolicy().hasHeightForWidth())
        Annotator3_1.setSizePolicy(sizePolicy)
        Annotator3_1.setToolTipDuration(-1)
        self.Selected_list_list = []
        self.centralwidget = QtWidgets.QWidget(Annotator3_1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setMinimumSize(QtCore.QSize(300, 0))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.img_scroll_frame = QtWidgets.QFrame(self.main_frame)
        self.img_scroll_frame.setGeometry(QtCore.QRect(230, 0, 1361, 931))
        self.img_scroll_frame.setMinimumSize(QtCore.QSize(1250, 900))
        self.img_scroll_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.img_scroll_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.img_scroll_frame.setLineWidth(1)
        self.img_scroll_frame.setObjectName("img_scroll_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.img_scroll_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.img_scroll_frame)
        self.scrollArea.setMouseTracking(False)
        self.scrollArea.setTabletTracking(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1337, 907))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget_3 = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_3.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.listWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_3.setIconSize(QtCore.QSize(310, 220))
        self.listWidget_3.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_5.addWidget(self.listWidget_3, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.list_right_frame = QtWidgets.QFrame(self.main_frame)
        self.list_right_frame.setGeometry(QtCore.QRect(1590, 0, 921, 931))
        self.list_right_frame.setMinimumSize(QtCore.QSize(300, 0))
        self.list_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_right_frame.setObjectName("list_right_frame")
        self.layoutWidget_2 = QtWidgets.QWidget(self.list_right_frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 304, 881))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.Enter_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Enter_btn.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Enter_btn.setObjectName("Enter_btn")
        self.horizontalLayout_2.addWidget(self.Enter_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.folders = QtWidgets.QListWidget(self.layoutWidget_2)
        self.folders.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.folders.setObjectName("folders")
        self.verticalLayout_2.addWidget(self.folders)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget_2)
        self.listWidget.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images_icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btn_left_frame = QtWidgets.QFrame(self.main_frame)
        self.btn_left_frame.setGeometry(QtCore.QRect(-10, -10, 251, 891))
        self.btn_left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_left_frame.setObjectName("btn_left_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.btn_left_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Source_Dir_btn = QtWidgets.QPushButton(self.btn_left_frame)
        self.Source_Dir_btn.setMinimumSize(QtCore.QSize(209, 79))
        self.Source_Dir_btn.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images_icons/pngguru.com (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Source_Dir_btn.setIcon(icon1)
        self.Source_Dir_btn.setIconSize(QtCore.QSize(70, 70))
        self.Source_Dir_btn.setObjectName("Source_Dir_btn")
        self.verticalLayout.addWidget(self.Source_Dir_btn)
        self.Distination_Dir_btn = QtWidgets.QPushButton(self.btn_left_frame)
        self.Distination_Dir_btn.setMinimumSize(QtCore.QSize(209, 79))
        self.Distination_Dir_btn.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images_icons/pngguru.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Distination_Dir_btn.setIcon(icon2)
        self.Distination_Dir_btn.setIconSize(QtCore.QSize(70, 70))
        self.Distination_Dir_btn.setObjectName("Distination_Dir_btn")
        self.verticalLayout.addWidget(self.Distination_Dir_btn)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(self.btn_left_frame)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.Selected_list = QtWidgets.QListWidget(self.btn_left_frame)
        self.Selected_list.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.Selected_list.setObjectName("Selected_list")
        self.verticalLayout_5.addWidget(self.Selected_list)
        self.pushButton_2 = QtWidgets.QPushButton(self.btn_left_frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_2.setMaximumSize(QtCore.QSize(227, 100))
        self.pushButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.gridLayout.addWidget(self.main_frame, 1, 0, 1, 1)
        Annotator3_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Annotator3_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1936, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        Annotator3_1.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(Annotator3_1)
        self.statusBar.setObjectName("statusBar")
        Annotator3_1.setStatusBar(self.statusBar)
        self.actionHelp = QtWidgets.QAction(Annotator3_1)
        self.actionHelp.setObjectName("actionHelp")
        self.actionToggle = QtWidgets.QAction(Annotator3_1)
        self.actionToggle.setObjectName("actionToggle")
        self.menufile.addAction(self.actionHelp)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionToggle)
        self.menubar.addAction(self.menufile.menuAction())
        self.listWidget.clicked.connect(self.listwidget_clicked)
        self.folders.clicked.connect(self.folders_list_clicked)
        self.Selected_list.clicked.connect(self.selected_list_clicked)
        self.pushButton_2.clicked.connect(self.on_click_pushbutton_2)
        self.Distination_Dir_btn.clicked.connect(self.on_click_destination_dir_btn)
        self.Source_Dir_btn.clicked.connect(self.on_click_source_dir_btn)
        self.Enter_btn.clicked.connect(self.Enter_btn_clicked)
        self.lineEdit.textChanged.connect(self.update_display_list)

        self.image_list()
        self.refresh()


        self.retranslateUi(Annotator3_1)
        QtCore.QMetaObject.connectSlotsByName(Annotator3_1)

    #delete the folders selected in left side list
    def selected_list_clicked(self):
        item = self.Selected_list.currentItem()
        print()
        st = str(item.text())
        if st in self.Selected_list_list :
            pass
        a = self.Selected_list.takeItem(self.Selected_list.currentRow())
        print(a.text()," removed")
        self.Selected_list_list.remove(a.text())
        print(self.Selected_list_list)
        return

    #on click enter left side
    def on_click_pushbutton_2(self):
        ans = self.showDialog("The files will be copied")
        if ans == True:
            items = self.listWidget.selectedItems()
            num_ITEMS=[item.text() for item in self.listWidget_3.selectedItems()]
            print(num_ITEMS)
            text_file = open("./txt_files/source_dir.txt", "r")
            source_dir = text_file.read()
            text_file.close()
            text_file = open("./txt_files/destination_dir.txt", "r")
            destination_dir = text_file.read()
            text_file.close()
            folders_list = self.Selected_list_list
            location_list = self.get_image_locations()
            Directory.copy_files(num_ITEMS,source_dir, destination_dir, folders_list, location_list)
            self.Selected_list.clear()
            self.Selected_list_list.clear()
            self.listWidget_3.clearSelection()
        return
    
    #displaying image list
    def image_list(self):
        self.listWidget_3.clear()
        location_list = self.get_image_locations()
        for i in location_list:

            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(i), QtGui.QIcon.Selected, QtGui.QIcon.On)
            item.setIcon(icon)
            self.listWidget_3.addItem(item)
        return
    
    #clicking enter button right side
    def Enter_btn_clicked(self):
        destination_folders = self.destin_folders_get()
        if str(self.lineEdit.text()) in destination_folders:   
            a =0
        
        else:
            try:
                text_file = open("./txt_files/destination_dir.txt", "r")
                destination_dir = text_file.read()
                text_file.close()
                os.mkdir(destination_dir+"/"+(str(self.lineEdit.text())))
                self.lineEdit.text()
                self.lineEdit.clear()
            except:
                self.destin_folders_get
        return

    #on click source button to change source folder
    def on_click_source_dir_btn(self):
        source_dir = QFileDialog.getExistingDirectory()
        print(source_dir)
        text_file = open("./txt_files/source_dir.txt", "w")
        n = text_file.write(source_dir)
        text_file.close()
        #refresh the page image
        os.execl(sys.executable, sys.executable, *sys.argv)
        self.refresh()

    #left side list
    def selected_list_folders(self,items):
        
        if items in self.Selected_list_list:
            return
        else:
            item = QtWidgets.QListWidgetItem()
            self.Selected_list.addItem(items)
            self.Selected_list_list.append(items)
            print(self.Selected_list_list)
            return

    #destination btn
    def on_click_destination_dir_btn(self):
        destination_folder = QFileDialog.getExistingDirectory()
        text_file = open("./txt_files/destination_dir.txt", "w")
        text_file.write(destination_folder)
        text_file.close()
        # print(destination_folder)
        self.folder_lists_destin()
        return destination_folder

    #getting the imagelocations from source folder
    def get_image_locations(self):
        text_file = open("./txt_files/source_dir.txt", "r")
        source_dir = text_file.read()
        text_file.close()
        location_list = Directory.images_in_the_directorys(source_dir)
        return location_list

    #refresh btn down right corner
    def refresh(self):
        i = 0
        self.listWidget.clear()
        self.location_list = self.get_image_locations()
        
        for i in range(len(self.location_list)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(os.path.realpath(self.location_list[i]))
            
        self.image_list()
        self.folder_lists_destin()
        self.label.setText(str(len(self.location_list))+" files in the source")
        return self.location_list

    #message box
    def showDialog(self, msg):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
            return True
        else:
            return False

    #clicking the list which displays image location and name
    def listwidget_clicked(self):
        item = self.listWidget.currentItem()

    #folders list on click right side below search box
    def folders_list_clicked(self):
        item = self.folders.currentItem()
        self.selected_list_folders(str(item.text()))

    #get the destination folders 
    def destin_folders_get(self):
        text_file = open("./txt_files/destination_dir.txt", "r")
        destination_dir = text_file.read()
        text_file.close()
        return Directory.destination_dir_folder(destination_dir)

    #listing the destination folders in the right side top
    def folder_lists_destin(self):
        i = 0
        self.folders.clear()
        self.destination_dir_folders =self.destin_folders_get()    
        for i in range(len(self.destination_dir_folders)):
            item = QtWidgets.QListWidgetItem()
            self.folders.addItem(self.destination_dir_folders[i])
        return

    #displaying the updated list when we search
    def update_display_list(self, text):
        self.destination_dir_folders =self.destin_folders_get()
        res = [i for i in self.destination_dir_folders if text in i]
        self.folders.clear()
        for i in range(len(res)):
            item = QtWidgets.QListWidgetItem()
            self.folders.addItem(res[i])
        return

    #for printing names
    def retranslateUi(self, Annotator3_1):
        _translate = QtCore.QCoreApplication.translate
        Annotator3_1.setWindowTitle(_translate("Annotator3_1", "copy image to folders"))
        self.Enter_btn.setText(_translate("Annotator3_1", "Enter"))
        self.label.setText(_translate("Annotator3_1", "Number of files"))
        self.pushButton.setText(_translate("Annotator3_1", "Refresh"))
        self.Source_Dir_btn.setText(_translate("Annotator3_1", "Source Dir"))
        self.Distination_Dir_btn.setText(_translate("Annotator3_1", "Distination Dir"))
        self.label_2.setText(_translate("Annotator3_1", "click to unselect the folder"))
        self.pushButton_2.setText(_translate("Annotator3_1", "ENTER"))
        self.menufile.setTitle(_translate("Annotator3_1", "File"))
        self.actionHelp.setText(_translate("Annotator3_1", "Help"))
        self.actionToggle.setText(_translate("Annotator3_1", "Toggle"))
        #for printing the names of images
        k = 0
        location_list = self.get_image_locations()
        for i in location_list:
            __sortingEnabled = self.listWidget_3.isSortingEnabled()
            self.listWidget_3.setSortingEnabled(False)
            item = self.listWidget_3.item(k)
            self.listWidget_3.setSortingEnabled(__sortingEnabled)
            item.setText(_translate("Annotator3_1", str(os.path.basename(i))))
            k = k +1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Annotator3_1 = QtWidgets.QMainWindow()
    ui = Ui_Annotator3_1()
    ui.setupUi(Annotator3_1)
    Annotator3_1.show()
    sys.exit(app.exec_())
