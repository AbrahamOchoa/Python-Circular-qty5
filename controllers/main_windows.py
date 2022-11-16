from PySide2.QtWidgets import QWidget
from views.main_window import Form

class Form (QWidget, Form):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
    
    def open_new_book_windows(self):
        pass
    def open_edit_book_windows(self):
        pass
    def open_book(self):
        pass
    def remove_book(self):
        pass
    def populate_teblo(self):
        pass
    def populate_combobox(self):
        pass
    def search_book_by_title(self):
        pass
    def search_book_category(self):
        pass
    def search(self):
        pass
    def records_qty(self):
        pass
