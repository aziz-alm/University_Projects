from tkinter import *
from TkUtils import TkUtils as ut


class ErrorView:

    def __init__(self, exception):
        # Store class name and message separately so we display each clearly
        self.error_class = type(exception).__name__
        self.error_message = str(exception)#message name

    def control(self):
        window = ut.top_level("Error")#The Title

        # Top: error icon
        ut.image(window, "image/error.png",#Img path
                 height=140, width=140).pack(padx=20, pady=(20, 10))#size..etc

        # The exception class name
        ut.error_label(window, self.error_class).pack(padx=20, pady=(0, 5))

        # The error message
        ut.text(window, self.error_message).pack(padx=20, pady=(0, 15))

        # Close button at the bottom (full-width pink bar, like the others)
        button_frame = ut.frame(window)
        button_frame.pack(fill=X)
        ut.button(button_frame, "Close", window.destroy).pack(
            expand=TRUE, fill=X, ipady=6)#close window
