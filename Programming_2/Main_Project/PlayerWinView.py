from tkinter import *
from TkUtils import TkUtils as ut


class PlayerWinView:

    def __init__(self, winner, dealer_view):
        self.winner = winner
        self.dealer_view = dealer_view

    def control(self):
        window = ut.top_level("Game Over")

        ut.label(window, "Winner!").pack(padx=40, pady=(20, 10))
        ut.text(window, f"Player: {self.winner.get_name()}").pack(padx=40, pady=2)
        ut.text(window, f"Total Health: {self.winner.get_total_health()}").pack(padx=40, pady=(2, 15))

        button_frame = ut.frame(window)
        button_frame.pack(fill=X)
        # Closing the Game Over window ends the whole game
        ut.button(button_frame, "OK", self.dealer_view.exit_game).pack(
            expand=TRUE, fill=X, ipady=6)

        # X button on this window also ends the game (game's already called)
        window.protocol("WM_DELETE_WINDOW", self.dealer_view.exit_game)
