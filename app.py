import sys
from PyQt5.QtWidgets import QApplication, QFileDialog , QWidget, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton, QComboBox, QInputDialog
from PyQt5.QtGui import QIcon
import PIL
from PIL import Image
from PyQt5.QtCore import Qt
import os
import sys

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Compressor'
        self.left = 100
        self.top = 100
        self.width = 400
        self.image_width=0
        self.compress_width =0
        self.height = 600
        self.statusBar().showMessage("Message :")
        self.statusBar().setObjectName("status_bar")
        self.setFixedSize(self.width,self.height)
        self.setObjectName("main_window")
        stylesheet = ""
        with open("design.qss","r+") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    #::::::::::::::::::::::::::::::Main Window::::::::::::::::::::::::::::::::::::::::
        self.single_bubble=QFrame(self)
        self.single_bubble.setObjectName("bubble")
        self.single_bubble.move(50,100)
        self.single_bubble.mousePressEvent = self.single_bubble_click

    #___________________________________________Heading for single image____________________________________________
        self.single_bubble_heading=QLabel(self.single_bubble)
        self.single_bubble_heading.setObjectName("single_heading")
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.move(90,8)

    #---------------------------------------Text-------------------------------------
        self.single_bubble_para=QLabel(self.single_bubble)
        self.single_bubble_para.setObjectName("single_para")
        self.single_bubble_para.setText("Click here to compress single image!")
        self.single_bubble_para.move(30,32)


    
        self.dir_bubble=QFrame(self)
        self.dir_bubble.setObjectName("bubble")
        self.dir_bubble.move(50,275)
        self.dir_bubble.mousePressEvent = self.dir_bubble_click

    #_____________________________________Heading for multiple images___________________________
        self.dir_bubble_heading=QLabel(self.dir_bubble)
        self.dir_bubble_heading.setText("Compress Multiple Images ")
        self.dir_bubble_heading.setObjectName("dir_heading")
        self.dir_bubble_heading.move(45,8)

    #-------------------------------------------Text----------------------------------------
        self.dir_bubble_para=QLabel(self.dir_bubble)
        self.dir_bubble_para.setObjectName("dir_para")
        self.dir_bubble_para.setText("Want to compress multiple images at once? select the folder and get compressed version of the image in another folder")
        self.dir_bubble_para.setWordWrap(True)
        self.dir_bubble_para.move(1,2)

    #.......................................Single Frame........................................
        self.single=QFrame(self)
        self.single.setObjectName("single")
        self.single.move(50,100)
        self.single.setVisible(False)

    #********************************Arrow for Single***************************************
        self.back_arrow=QLabel(self.single)
        self.back_arrow.move(25,0)
        self.back_arrow.setObjectName("back_arrow_s")
        self.back_arrow.setTextFormat(Qt.RichText)
        self.back_arrow.setText("&#8592;")
        self.back_arrow.mousePressEvent = self.back_page_s
    #********************************End arrow***********************************************   
        self.single_bubble_heading=QLabel(self.single)
        self.single_bubble_heading.setObjectName("single_heading")
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.move(90,8)


        self.select_image_lable=QLabel(self.single)
        self.select_image_lable.setObjectName("single_para")
        self.select_image_lable.setText("Choose Image")
        self.select_image_lable.move(30, 50)


        self.image_path=QLineEdit(self.single)
        self.image_path.setObjectName("path_text")
        self.image_path.move(60,85)


        self.browse_button=QPushButton(self.single)
        self.browse_button.setText("...")
        self.browse_button.setObjectName("browse_button")
        self.browse_button.clicked.connect(self.select_file)
        self.browse_button.move(240,84)


        self.select_image_quality=QLabel(self.single)
        self.select_image_quality.setObjectName("single_para")
        self.select_image_quality.setText("Choose Quality")
        self.select_image_quality.move(30, 130)


        self.quality_path=QLineEdit(self.single)
        self.quality_path.setObjectName("quality_path_text")
        self.quality_path.move(60,160)


        self.quality_combo=QComboBox(self.single)
        self.quality_combo.setObjectName("quality_combo")
        self.quality_combo.addItem("High")
        self.quality_combo.addItem("Medium")
        self.quality_combo.addItem("Low")
        self.quality_combo.move(170,160)
        self.quality_combo.currentIndexChanged.connect(self.quality_current_value)
        self.quality_combo.resize(90,26)
        

        self.compress_button=QPushButton(self.single)
        self.compress_button.setText("Compress")
        self.compress_button.clicked.connect(self.resize_img)
        self.compress_button.setObjectName("compress_button")
        self.compress_button.move(110,260)
    #..............................End single Frame...............................

    #.................................multiple frame....................................
        self.multiple=QFrame(self)
        self.multiple.setObjectName("multiple")
        self.multiple.move(50,100)
        self.multiple.setVisible(False)
    #*********************************Arrow for multiple*******************************
        self.back_arrow_m=QLabel(self.multiple)
        self.back_arrow_m.move(15,0)
        self.back_arrow_m.setObjectName("back_arrow_m")
        self.back_arrow_m.setTextFormat(Qt.RichText)
        self.back_arrow_m.setText("&#x2190;")
        self.back_arrow_m.mousePressEvent = self.back_page_m
    #********************************End arrow***************************************
        self.dir_bubble_heading=QLabel(self.multiple)
        self.dir_bubble_heading.setText("Compress Multiple Images ")
        self.dir_bubble_heading.setObjectName("dir_heading")
        self.dir_bubble_heading.move(60,8)


        self.select_source_lable=QLabel(self.multiple)
        self.select_source_lable.setObjectName("single_para")
        self.select_source_lable.setText("Choose source directory")
        self.select_source_lable.move(30, 50)


        self.source_path=QLineEdit(self.multiple)
        self.source_path.setObjectName("path_text")
        self.source_path.move(60,85)


        self.browse_source_button=QPushButton(self.multiple)
        self.browse_source_button.setText("...")
        self.browse_source_button.setObjectName("browse_button")
        self.browse_source_button.clicked.connect(self.select_folder_source)
        self.browse_source_button.move(240,84)

        self.select_dest_lable=QLabel(self.multiple)
        self.select_dest_lable.setObjectName("single_para")
        self.select_dest_lable.setText("Choose destination directory")
        self.select_dest_lable.move(30, 130)


        self.dest_path=QLineEdit(self.multiple)
        self.dest_path.setObjectName("path_text")
        self.dest_path.move(60,160)


        self.browse_dest_button=QPushButton(self.multiple)
        self.browse_dest_button.setText("...")
        self.browse_dest_button.setObjectName("browse_button")
        self.browse_dest_button.clicked.connect(self.select_folder_dest)
        self.browse_dest_button.move(240,160)


        self.select_dir_quality=QLabel(self.multiple)
        self.select_dir_quality.setObjectName("single_para")
        self.select_dir_quality.setText("Choose Quality")
        self.select_dir_quality.move(30, 205)


        self.quality_dir_path=QLineEdit(self.multiple)
        self.quality_dir_path.setObjectName("quality_path_text")
        self.quality_dir_path.move(60,235)


        self.quality_dir_combo=QComboBox(self.multiple)
        self.quality_dir_combo.setObjectName("quality_combo")
        self.quality_dir_combo.addItem("High")
        self.quality_dir_combo.addItem("Medium")
        self.quality_dir_combo.addItem("Low")
        self.quality_dir_combo.currentIndexChanged.connect(self.quality_current_dir_value)
        self.quality_dir_combo.move(170,235)
        self.quality_dir_combo.resize(90,26)


        self.compress_dir_button=QPushButton(self.multiple)
        self.compress_dir_button.setText("Compress")
        self.compress_dir_button.clicked.connect(self.resize_folder)
        self.compress_dir_button.setObjectName("compress_button")
        self.compress_dir_button.move(110,280)
    #..................................End multiple frame...............................


    #::::::::::::::::::::::::::::::End main window::::::::::::::::::::::::::::::::::::

        self.show()

    #::::::::::::::::::::::::::::::Functions:::::::::::::::::::::::::::::::::::::::::::
    def single_bubble_click(self, event):
        print("Well done")
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.single.setVisible(True)
        self.multiple.setVisible(False)

    def dir_bubble_click(self, event):
        print("Well done")
        self.single_bubble.setVisible(False)
        self.dir_bubble.setVisible(False)
        self.single.setVisible(False)
        self.multiple.setVisible(True)

    def back_page_s(self, event):
        print("Page is Back")
        self.single.setVisible(False)
        self.single_bubble.setVisible(True)
        self.dir_bubble.setVisible(True)

    def back_page_m(self, event):
        print("Page is Back")
        self.multiple.setVisible(False)
        self.single_bubble.setVisible(True)
        self.dir_bubble.setVisible(True)

    def select_file(self):
        print("Button Clicked")
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;JPEG (*.jpeg);;PNG (*.png);;JPG (*.jpg)")
        if fileName:
            print(fileName)
        self.image_path.setText(fileName)
        img = Image.open(fileName)
        self.image_width=img.width
        self.compress_width = self.image_width
        self.quality_path.setText(str(self.image_width))

    def select_folder_source(self):
        folder = (QFileDialog.getExistingDirectory(self))
        print(folder)
        self.source_path.setText(folder)
        files = os.listdir(folder)
        first_pic = folder + "/" + files[0]
        img = Image.open(first_pic)
        self.image_width=img.width
        self.compress_width = self.image_width
        self.quality_dir_path.setText(str(self.image_width))
        self.compress_width = self.image_width
    def select_folder_dest(self):
        folder = (QFileDialog.getExistingDirectory(self))
        print(folder)
        self.dest_path.setText(folder)

    def quality_current_value(self):
        if self.quality_combo.currentText() == "High":
            self.quality_path.setText(str(self.image_width))
            self.compress_width = self.image_width
        if self.quality_combo.currentText() == "Medium":
            self.quality_path.setText(str(int(self.image_width/2)))
            self.compress_width = int(self.image_width/2)
        if self.quality_combo.currentText() == "Low":
            self.quality_path.setText(str(int(self.image_width/4)))
            self.compress_width = int(self.image_width/4)
        
    def quality_current_dir_value(self):
        if self.quality_dir_combo.currentText() == "High":
            self.quality_dir_path.setText(str(self.image_width))
            self.compress_width = self.image_width
        if self.quality_dir_combo.currentText() == "Medium":
            self.quality_dir_path.setText(str(int(self.image_width/2)))
            self.compress_width = int(self.image_width/2)
        if self.quality_dir_combo.currentText() == "Low":
            self.quality_dir_path.setText(str(int(self.image_width/4)))
            self.compress_width = int(self.image_width/4)
    

    def resize_img(self):
        old_img = self.image_path.text()
        if old_img == '':
            self.statusBar().showMessage("Message: Please select an image")
            return
        if old_img[-4:] != '.jpg' or old_img[-4:] != '.png' or old_img[-5:] != '.jpeg' or old_img[-4:] != '.JPG' or old_img[-4:] != '.PNG' or old_img[-5:] != '.JPEG':
            self.statusBar().showMessage("Message: Please select an valid image")
            return


        print(old_img)
        print(self.compress_width)
        directories = self.image_path.text().split("/")
        print(directories)
        new_image_name, okPressed = QInputDialog.getText(self, "Save Image As","Image name:", QLineEdit.Normal, "")
        if okPressed and new_image_name != '':
            print(new_image_name)

            if old_img[-4:] == ".jpeg":
                new_image_name+=".jpeg"
            if old_img[-4:] == ".png":
                new_image_name+=".png"
            if old_img[-4:] == ".jpg":
                new_image_name+=".jpg"
            else:
                new_image_name+=".jpeg"
            new_img=""
            for i in directories[:-1]:
                new_img = new_img + i + '/'
            new_img+=new_image_name
            print(new_img)
            
            self.compression_code(old_img, new_img)
            self.statusBar().showMessage("Message: Compression is completed")
            print("Compression is completed")
        
            
    def resize_folder(self):
        source_directory = self.source_path.text()

        dest_directory = self.dest_path.text()

        if source_directory == '' or dest_directory == '':
            self.statusBar().showMessage("Message: Please select source and destination")
            return
        files = os.listdir(source_directory)

        
        i=0
        for file in files:
            i+=1
            if file[-4:] == '.jpg' or file[-4:] == '.png' or file[-5:] == '.jpeg' or file[-4:] == '.JPG' or file[-4:] == '.PNG' or file[-5:] == '.JPEG':
                old_img = source_directory + '/' + file
                new_img = dest_directory + '/' + file

                img = Image.open(old_img)
                self.image_width=img.width
                self.quality_dir_path.setText(str(self.image_width))

                old_img = source_directory + '/' + file
                new_img = dest_directory + '/' + file
                self.compression_code(old_img, new_img)

                total_images= len(files)
                image_done= i
                percentage = int(image_done/total_images*100)


            else:
                print("ignor" + file)
                continue
        self.statusBar().showMessage("Message:Compression is completed"+ str(int(image_done/total_images*100)) +str('%'))

    def compression_code(self, old_img, new_img):
        try:
            img = Image.open(old_img)
            my_width = self.compress_width
            wpercent = (my_width/float(img.size[0]))
            hsize = int ((float(img.size[1])*float(wpercent)))
            img = img.resize((my_width,hsize), PIL.Image.LANCZOS)
            img.save(new_img)
        except Exception as e:
            self.statusBar().showMessage("Message :"+e)
    #:::::::::::::::::::::::::::::::::End function::::::::::::::::::::::::::::::::::::::
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())