from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import fitz,os,about
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()      
        self.setWindowTitle("PDF to images")
        self.فتح_الملف=qt.QPushButton("تحديد ملف PDF")
        self.فتح_الملف.setDefault(True)
        self.فتح_الملف.clicked.connect(self.opinFile)
        self.التعديل=qt.QLineEdit()
        self.التعديل.setAccessibleName("مسار الملف")
        self.التعديل.setReadOnly(True)        
        self.تحويل=qt.QPushButton("بدء التحويل")
        self.تحويل.setDefault(True)
        self.تحويل.clicked.connect(self.convert_pdf_to_images)
        self.عن=qt.QPushButton("عن المطور")
        self.عن.setDefault(True)
        self.عن.clicked.connect(self.about)
        l=qt.QVBoxLayout()        
        l.addWidget(self.فتح_الملف)
        l.addWidget(self.التعديل)        
        l.addWidget(self.تحويل)
        l.addWidget(self.عن)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)  
    def opinFile(self):        
        file=qt.QFileDialog()
        file.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptOpen)        
        if file.exec()==qt.QFileDialog.DialogCode.Accepted:
            self.التعديل.setText(file.selectedFiles()[0])                                     
    def convert_pdf_to_images(self):    
        if not self.التعديل.text():
            qt.QMessageBox.warning(self,"تنبيه","يرجى تحديد ملف PDF")
            return
        try:        
            مستند_PDF=fitz.open(self.التعديل.text())
            عدد_الصفحات=مستند_PDF.page_count        
            if not os.path.exists("output_folder"):
                os.makedirs("output_folder")
                qt.QMessageBox.information(self,"تم","تمت العملية بنجاح")
            for page_num in range(عدد_الصفحات):
                الصفحة=مستند_PDF.load_page(page_num)
                pix=الصفحة.get_pixmap()
                مسار_الصور=os.path.join("output_folder", f"page_{page_num+1}.png")
                pix.save(مسار_الصور)
        except:
            qt.QMessageBox.warning(self,"تنبيه","حدثت مشكلة في التحويل, ربما الملف غير صالح")
    def about(self)            :
        about.dialog(self).exec()
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()