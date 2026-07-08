from tkinter import *
from TkUtils import TkUtils as ut
from model.player import Player
from model.dealer import Dealer
from DealerView import DealerView
from model.login_model import LoginModel


class LoginView:

    def __init__(self, root, model):
        self.model = model
        self.root = root

        self.player_1_entry = None
        self.player_2_entry = None
        self.player_3_entry = None
        self.player_4_entry = None

    def control(self):
        # Top frame: 4 columns of (avatar + entry)
        entry_frame = ut.frame(self.root)

        self.player_1_entry = self._make_column(entry_frame, "Davey", False)#Deufalt can't be changed
        self.player_2_entry = self._make_column(entry_frame, "Jenny", False)#Deufalt can't be changed
        self.player_3_entry = self._make_column(entry_frame, "", True)# the user should fill it
        self.player_4_entry = self._make_column(entry_frame, "", True)# the user should fill it

        entry_frame.pack(pady=(20, 30), padx=30)#frame size 

        # Bottom frame: Start Game button full width pink bar
        button_frame = ut.frame(self.root)
        ut.button(button_frame, "Start Game", self.start).pack(expand=TRUE, fill=X, ipady=6)#giving it the name etc.
        button_frame.pack(expand=TRUE, fill=X)

    def _make_column(self, parent, placeholder, editable):
        """Make a column with an avatar image on top and an entry below."""
        col = ut.frame(parent)
        ut.image(col, "image/avatar.png", height=120, width=80).pack(pady=(0, 8))
        entry = ut.entry(col, placeholder, editable)
        entry.pack(pady=(0, 5))
        col.pack(side=LEFT, padx=10, pady=10)
        return entry

    def start(self):
        # Always add players 1 and 2 (name fields not editable, always have values)
        self.model.add_to_game(Player(self.player_1_entry.get()))
        self.model.add_to_game(Player(self.player_2_entry.get()))

        # Players 3 and 4 only added if they typed a name
        name3 = self.player_3_entry.get().strip()
        if name3:
            self.model.add_to_game(Player(name3))

        name4 = self.player_4_entry.get().strip()
        if name4:
            self.model.add_to_game(Player(name4))

        # Set up the dealer with the chosen players, then open the dealer window
        # using the existing root (login becomes dealer). Player windows are
        # opened by DealerView itself.
        dealer = Dealer(self.model.get_players())
        DealerView(ut.same_window("Dealer", self.root), dealer).control()


if __name__ == "__main__":
    root = ut.root()
    LoginView(root, LoginModel()).control()
    root.mainloop()
