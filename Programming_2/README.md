# 48024 – Programming 2

> **UTS** · Autumn 2026 · 6 credit points · **Final grade: 95 (High Distinction)**

An OOP and GUI programming subject where you design, build and evaluate software from a specification, in **Java or Python**. It runs from basic programming plans through classes, lists, inheritance, and finishes on building GUIs with the **event model** and the **MVC** pattern.

This folder holds my main two-part project (a card game) and a couple of the weekly labs. Each lab was done in **both Python and Java**.

---

## What's in this repo

| Work | What it is / what I did | Language(s) | Key concepts | Weight |
|------|-------------------------|-------------|--------------|--------|
| **Main Project – Card Game** *(Assignment 1 + 2)* | A Tkinter card game. **Assignment 1** built the OO "background": the model classes (`card`, `deck`, `dealer`, `player`, `card_library`, custom exceptions) with all the game logic and no UI. **Assignment 2** wrapped that model in a full GUI using **MVC** — a login screen, the dealer dealing weapon cards to players across rounds, error dialogs, and a winner screen. | Python (Tkinter) | OO design, MVC, GUIs, event model, lists, inheritance, custom exceptions | 35% + 25% |
| **Lab 3 – NumberToWords** | Converts numbers `0–999` into words and Roman numerals until the user enters `-1`. | Python & Java | strings, recursion, incremental development | *part of labs (14%)* |
| **Lab 5 – Store (Classes)** | Menu-driven shop that tracks stock and takings across three classes (`Store`, `Product`, `CashRegister`). | Python & Java | classes, constructors, `toString`, spreading responsibility | *part of labs (14%)* |

> The subject also included quizzes, a timed LMS exam and advanced challenges — those aren't part of this repo.

---

## The main project in a bit more detail

The assignment came in two halves. Assignment 1 (the **background**, 35%) was pure logic — model the cards, the deck, the dealer and the players, plus the exceptions that guard the rules (a full hand, an empty deck, a round that isn't ready). Assignment 2 (the **front-end**, 25%) took that finished model and, without changing its behaviour, built the whole interface on top of it following **MVC** so the views only ever talk to the model through clean methods.

The game itself is a card-battle: players log in, the dealer deals a themed deck (Icicle, Iceberg, Spitfire, Blindside, Freezefire, Blazing Fury, Showdown, Shutdown…), play proceeds in rounds, and a win screen shows the result.

**Project layout**

```
Main_Project/
├── model/                      # Assignment 1 – the "background" (no UI)
│   ├── card.py  deck.py  dealer.py  player.py
│   ├── card_library.py  weapon_style.py  login_model.py
│   └── exception/              # full_hand / empty_deck / round_not_ready
├── image/                      # avatar, deck, error + card art
│   └── cards/
├── LoginView.py  DealerView.py  PlayerView.py  CardView.py   # Assignment 2 – the GUI (views)
├── DeckView.py   ErrorView.py   PlayerWinView.py
└── TkUtils.py                  # shared Tkinter styling helpers
```

[![Watch the video](https://img.youtube.com/vi/3s7VEz9IOcA/maxresdefault.jpg)](https://youtu.be/3s7VEz9IOcA)
---

## The labs

**Lab 3 – NumberToWords.** An early "basic process" lab: read numbers, print each in words and as a Roman numeral, stop on `-1`. Solved in Python and Java, using recursion for the hundreds case and a value/symbol lookup for the Roman conversion.

**Lab 5 – Store (Classes).** A first proper OO lab: a store selling one product with a cash register, driven by a text menu. The point was spreading the goals sensibly across `Store`, `Product` and `CashRegister` rather than piling everything into one class.

---

*Academic work completed for UTS 48024. Assignment work is individual.*
