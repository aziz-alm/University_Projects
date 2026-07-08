from tkinter import *
from TkUtils import TkUtils as ut


def _card_image_path(card):
    fname = card.get_name().lower().replace(" ", "")
    return f"image/cards/{fname}.png"


class CardView:

    def __init__(self, card):
        self.card = card

    def control(self):
        window = ut.top_level(self.card.get_name())

        ut.image(window, _card_image_path(self.card),
                 height=420, width=280).pack(padx=20, pady=(20, 10))

        # Close button under the image (full-width pink bar)
        button_frame = ut.frame(window)
        button_frame.pack(fill=X)
        ut.button(button_frame, "Close", window.destroy).pack(
            expand=TRUE, fill=X, ipady=6)
