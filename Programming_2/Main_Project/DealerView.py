from tkinter import *
from TkUtils import TkUtils as ut
from PlayerView import PlayerView
from DeckView import DeckView
from ErrorView import ErrorView
from PlayerWinView import PlayerWinView
from model.exception.empty_deck_exception import EmptyDeckException
from model.exception.round_not_ready_exception import RoundNotReadyException


class DealerView:

    def __init__(self, root, dealer):
        self.root = root
        self.dealer = dealer

        # All player windows we open — DealerView keeps a reference so it can
        # refresh them when Deal/Play Round happens, and close them on Exit.
        self.player_views = []

        # Widgets that get refreshed
        self.score_labels = {}      # player index -> Label

    #  build
    def control(self):
        # Top: two clickable deck images side-by-side
        decks_frame = ut.frame(self.root)
        decks_frame.pack(padx=20, pady=20)

        main_img = ut.image(decks_frame, "image/deck.png", height=260, width=170)
        main_img.pack(side=LEFT, padx=10)
        main_img.bind("<Button-1>", lambda e: self.open_deck("Main", self.dealer.get_main_deck()))

        secondary_img = ut.image(decks_frame, "image/deck.png", height=260, width=170)
        secondary_img.pack(side=LEFT, padx=10)
        secondary_img.bind("<Button-1>", lambda e: self.open_deck("Secondary", self.dealer.get_secondary_deck()))

        #  Middle: 2x2 player score grid + Call button 
        middle = ut.frame(self.root)
        middle.pack(padx=20, pady=(0, 10), fill=X)

        scores_frame = ut.frame(middle)
        scores_frame.pack(side=LEFT)

        # Always show 4 slots. Slots without a player display N/A.
        players = self.dealer.get_players()
        for i in range(4):
            row = i // 2
            col = i % 2
            cell = ut.frame(scores_frame)
            cell.grid(row=row, column=col, sticky=W, padx=10, pady=2)
            ut.text(cell, f"Player {i+1}: ").pack(side=LEFT)

            if i < len(players):
                lbl = ut.text(cell, str(players[i].get_total_health()))
            else:
                lbl = ut.text(cell, "N/A")
            lbl.pack(side=LEFT)
            self.score_labels[i] = lbl

        ut.button(middle, "Call", self.call_game).pack(side=RIGHT, padx=10, ipadx=20, ipady=10)

        # --- Bottom: pink bar of three buttons ----------------------------
        bottom = ut.frame(self.root)
        bottom.pack(fill=X)

        ut.button(bottom, "Deal", self.deal).pack(side=LEFT, expand=TRUE, fill=X, ipady=8)
        ut.button(bottom, "Play Round", self.play_round).pack(side=LEFT, expand=TRUE, fill=X, ipady=8)
        ut.button(bottom, "Exit", self.exit_game).pack(side=LEFT, expand=TRUE, fill=X, ipady=8)

        # --- Open a window for every player -------------------------------
        for player in players:
            view = PlayerView(player, self)
            view.control()
            self.player_views.append(view)

        # When the dealer (root) window is closed via the X, close everything
        self.root.protocol("WM_DELETE_WINDOW", self.exit_game)

        self.refresh()

    # ----------------------------------------------------------- callbacks
    def open_deck(self, deck_type, deck):
        DeckView(deck_type, deck).control()

    def deal(self):
        try:
            self.dealer.deal()
        except EmptyDeckException as e:
            ErrorView(e).control()
            return
        # Deal succeeded -> refresh dealer scores and every player view
        self.refresh()
        for view in self.player_views:
            view.refresh()

    def play_round(self):
        try:
            self.dealer.play()
        except RoundNotReadyException as e:
            ErrorView(e).control()
            return
        self.refresh()
        for view in self.player_views:
            view.refresh()

    def call_game(self):
        # Whoever has the highest total_health wins
        players = self.dealer.get_players()
        winner = players[0]
        for p in players[1:]:
            if p.get_total_health() > winner.get_total_health():
                winner = p
        PlayerWinView(winner, self).control()

    def exit_game(self):
        # Close all player windows then the dealer (which is root) -> app ends
        for view in self.player_views:
            view.close()
        self.root.destroy()

    # ------------------------------------------------------------ refresh
    def refresh(self):
        """Update the player score labels."""
        # Deal and Play Round stay enabled at all times so the user can
        # trigger their respective error windows (rubric: Dealer 4 & 5).
        players = self.dealer.get_players()
        for i in range(4):
            if i < len(players):
                self.score_labels[i].config(text=str(players[i].get_total_health()))
            else:
                self.score_labels[i].config(text="N/A")
