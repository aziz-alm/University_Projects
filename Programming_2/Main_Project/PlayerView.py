from tkinter import *
from TkUtils import TkUtils as ut
from ErrorView import ErrorView
from model.exception.full_hand_exception import FullHandException


def card_image_path(card):
    """'Blazing Fury' -> 'image/cards/blazingfury.png'"""
    fname = card.get_name().lower().replace(" ", "")
    return f"image/cards/{fname}.png"


class PlayerView:

    def __init__(self, player, dealer_view):
        self.player = player
        self.dealer_view = dealer_view

        self.window = None

        # LEFT: placed hand
        self.hand_tree = None
        self.hand_row_to_card = {}
        self.select_button = None

        # MIDDLE: temp hand
        self.temp_list = None
        self.temp_index_to_card = {}
        self.place_button = None

        # RIGHT: card image
        self.image_holder = None
        self.image_widget = None

    # ------------------------------------------------------------------ build
    def control(self):
        self.window = ut.top_level(self.player.get_name())

        # One horizontal row holding the three sections
        main = ut.frame(self.window)
        main.pack(padx=20, pady=20)

        # ----- LEFT: placed hand treeview + Select button ---------------
        left = ut.frame(main)
        left.pack(side=LEFT, padx=10)

        self.hand_tree = ut.treeview(left, ["Name", "Attack", "Style", "Health"],
                                     multi=False, width=320)
        self.hand_tree.pack()
        self.hand_tree.bind("<<TreeviewSelect>>", self.on_hand_select)

        select_frame = ut.frame(left)
        select_frame.pack(fill=X, pady=(5, 0))
        self.select_button = ut.button(select_frame, "Select", self.do_select)
        self.select_button.pack(expand=TRUE, fill=X, ipady=6)
        self.select_button.config(state=DISABLED)

        # ----- MIDDLE: temp hand list + Place button --------------------
        middle = ut.frame(main)
        middle.pack(side=LEFT, padx=10)

        self.temp_list = Listbox(middle, height=12, width=25,
                                 borderwidth=1, relief=SOLID,
                                 background="white",
                                 selectbackground=ut.red,
                                 selectforeground="white",
                                 exportselection=False,
                                 highlightthickness=0)
        self.temp_list.pack()
        self.temp_list.bind("<<ListboxSelect>>", self.on_temp_select)

        place_frame = ut.frame(middle)
        place_frame.pack(fill=X, pady=(5, 0))
        self.place_button = ut.button(place_frame, "Place", self.do_place)
        self.place_button.pack(expand=TRUE, fill=X, ipady=6)
        self.place_button.config(state=DISABLED)

        # ----- RIGHT: card image ----------------------------------------
        right = ut.frame(main)
        right.pack(side=LEFT, padx=10)

        self.image_holder = ut.frame(right)
        self.image_holder.pack()

        # Closing this window with the X just closes this player's window
        self.window.protocol("WM_DELETE_WINDOW", self.close)

        self.refresh()

    # ----------------------------------------------------------- callbacks
    def on_hand_select(self, event):
        # Enable/disable the Select button based on whether a row is picked
        if self.hand_tree.selection():
            self.select_button.config(state=NORMAL)
        else:
            self.select_button.config(state=DISABLED)

    def on_temp_select(self, event):
        # Enable/disable the Place button based on whether an item is picked
        if self.temp_list.curselection():
            self.place_button.config(state=NORMAL)
        else:
            self.place_button.config(state=DISABLED)

    def do_select(self):
        """User confirmed they want to play this card next round."""
        sel = self.hand_tree.selection()
        if not sel:
            return
        card = self.hand_row_to_card.get(sel[0])
        if card is None:
            return
        self.player.select(card)
        self._draw_image()
        # Tell the dealer view so the Play Round logic sees the new selection
        self.dealer_view.refresh()

    def do_place(self):
        """Move the picked temp-hand card into the player's actual hand."""
        idx_sel = self.temp_list.curselection()
        if not idx_sel:
            return
        card = self.temp_index_to_card.get(idx_sel[0])
        if card is None:
            return
        try:
            self.player.place(card)
        except FullHandException as e:
            ErrorView(e).control()
            return
        self.refresh()
        self.dealer_view.refresh()

    def close(self):
        if self.window is not None:
            try:
                self.window.destroy()
            except Exception:
                pass
            self.window = None

    # ------------------------------------------------------------ refresh
    def refresh(self):
        # Rebuild placed-hand treeview from player.get_hand()
        for row in self.hand_tree.get_children():
            self.hand_tree.delete(row)
        self.hand_row_to_card = {}
        for card in self.player.get_hand():
            row_id = self.hand_tree.insert("", END, values=(
                card.get_name(),
                card.get_attack(),
                str(card.get_style()),
                card.get_health(),
            ))
            self.hand_row_to_card[row_id] = card

        # Rebuild temp-hand listbox from player.get_temp_hand()
        self.temp_list.delete(0, END)
        self.temp_index_to_card = {}
        for i, card in enumerate(self.player.get_temp_hand()):
            self.temp_list.insert(END, card.get_name())
            self.temp_index_to_card[i] = card

        # Both action buttons reset to disabled (no row/item is selected
        # right after a refresh)
        self.select_button.config(state=DISABLED)
        self.place_button.config(state=DISABLED)

        # Update the card image on the right
        self._draw_image()

    def _draw_image(self):
        if self.image_holder is None:
            return
        if self.image_widget is not None:
            self.image_widget.destroy()
        selected = self.player.get_selected_card()
        path = card_image_path(selected) if selected else "image/cards/empty.png"
        self.image_widget = ut.image(self.image_holder, path, height=280, width=180)
        self.image_widget.pack()
