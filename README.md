﻿# SalmonSpaghetti 🍣🍝🤖
 
**ChessAI** created using Python 🐍, playable on [Lichess](https://lichess.org/@/SalmonSpaghetti) ♟️

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

<div style="text-align: center;">
   <img src="https://github.com/user-attachments/assets/bad91b9b-9ea2-43b8-8b0b-e1131f639554" alt="Salmon Spaghetti Demo" width="25%" />
</div>
<small><i>Salmon Spaghetti v1.0 beating me in an ultrabullet chess game.</i></small>

### 📖 Key Features :
- **[Beserk](https://pypi.org/project/berserk/)**: Uses Beserk Python Client for connecting to Lichess API. Handles token session, JSON and PGN.
- **[Python-Chess](https://python-chess.readthedocs.io/en/latest/)**: Uses Python Chess Library for move generation, validation and allows for bot to play chess variants such as [Chess960](https://en.wikipedia.org/wiki/Fischer_random_chess)
- **[Lichess](https://lichess.org/@/SalmonSpaghetti)**: Popular Non-Profit Chess Platform

### 👓 As of v1.0, this Chess AI is not the smartest. The bot has some strategy though, such as:
- **Checkmate in 1**: Be careful, because SalmonSpaghetti does not miss Mate in 1.
- **Free Pieces**: SalmonSpaghetti tries not to hang its pieces, and tries to take free pieces but they are not perfect just yet.
- **King Safety**: The bot tries to avoid walking into checkmate. See if you can beat them at Bullet Chess! (1+0)?

### ✏️ SalmonSpaghetti is trying the best to improve with some cheeky puzzles. Next things to implement is:
- **Move Depth**: SalmonSpaghetti does not look past depth1/2
- **Piece Value**: The bot will trade a queen for a bishop, they do not know any better
- **Bitboards**: SalmonSpaghetti does not have eyes. It is spaghetti. We will give them eyes soon.

<small><i>Sneak Peek: Salmon Spaghetti in training.</i></small>
 <img src="https://github.com/user-attachments/assets/1a39c887-f12d-4a73-99d5-8bdbcefdf482" alt="Alt text" width="25%" />

