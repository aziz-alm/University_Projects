from tkinter import *
from TkUtils import TkUtils as ut
from CardView import CardView


class DeckView:

    def __init__(self, deck_type, deck):
        self.deck_type = deck_type
        self.deck = deck

        self.window = None
        self.tree = None
        self.row_to_card = {}
        self.show_button = None

    def control(self):
        self.window = ut.top_level(f"{self.deck_type} Deck")

        # Treeview of cards in the deck (just card names)
        tree_frame = ut.frame(self.window)
        tree_frame.pack(padx=20, pady=20)

        self.tree = ut.treeview(tree_frame, ["Name"], multi=False, width=240)
        self.tree.pack()
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        # Populate rows
        for card in self.deck.get_cards():
            row_id = self.tree.insert("", END, values=(card.get_name(),))
            self.row_to_card[row_id] = card

        # Bottom row: Show Card (left, disabled until pick) + Close (right)
        button_frame = ut.frame(self.window)
        button_frame.pack(fill=X)

        self.show_button = ut.button(button_frame, "Show Card", self.show_card)
        self.show_button.pack(side=LEFT, expand=TRUE, fill=X, ipady=6)
        self.show_button.config(state=DISABLED)

        ut.button(button_frame, "Close", self.window.destroy).pack(
            side=LEFT, expand=TRUE, fill=X, ipady=6)

    def on_select(self, event):
        if self.tree.selection():
            self.show_button.config(state=NORMAL)
        else:
            self.show_button.config(state=DISABLED)

    def show_card(self):
        sel = self.tree.selection()
        if not sel:
            return
        card = self.row_to_card.get(sel[0])
        if card is not None:
            CardView(card).control()
