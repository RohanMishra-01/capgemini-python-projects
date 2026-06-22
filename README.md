# Python Mini Projects

A collection of simple command-line based mini projects built with Python. Each project demonstrates core Python concepts such as functions, dictionaries, lists, loops, and modular programming.

---

## Projects Included

### 1. Library Management System
A system to manage library operations — add books, display available books, issue books to students, and return them with automatic fine calculation.

### 2. ATM Simulation
A simulation of basic ATM operations — deposit money, withdraw money, check account balance, and view transaction history.

### 3. Stone Paper Scissor Game
A classic Stone Paper Scissor game where the user plays against the computer, which makes a random move each round.

---

## Repository Structure

    python-mini-projects/
    │
    ├── library_management_system/
    │   ├── main.py
    │   ├── add_book.py
    │   ├── show_book.py
    │   ├── issue_books.py
    │   ├── return_book.py
    │   └── utils.py
    │
    ├── atm_simulation/
    │   ├── main.py
    │   ├── deposit_money.py
    │   ├── withdraw_money.py
    │   ├── display_money.py
    │   ├── bank_statement.py
    │   └── utils.py
    │
    └── stone_paper_scissor/
        ├── main.py
        ├── stone.py
        ├── paper.py
        ├── scissor.py
        ├── computer_choice.py
        └── utils.py

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### How to Run a Project

1. Clone the repository:

        git clone https://github.com/RohanMishra-01/python-mini-projects.git
        cd python-mini-projects

2. Navigate to any project folder and run its main file:

        cd library_management_system
        python main.py

        cd atm_simulation
        python main.py

        cd stone_paper_scissor
        python main.py

No external dependencies required — pure Python!

---

## Project Summaries

### Library Management System

- Add one or more books to the library
- View all available books
- Issue books to students with date and duration tracking
- Return books with automatic fine calculation

| Overdue Period     | Fine Rate               |
|--------------------|-------------------------|
| Within 7 days      | No fine                 |
| 8 - 14 days late   | Rs. 10 per day per book |
| 15 - 21 days late  | Rs. 20 per day per book |
| More than 21 days  | Full price of the book  |

---

### ATM Simulation

- Deposit and withdraw money with input validation
- Check current account balance
- View full transaction history for the session

---

### Stone Paper Scissor Game

- Play against the computer which picks randomly
- Displays both choices and the result after every round
- Covers all win, lose, and tie conditions

| User Choice | Computer Choice | Result        |
|-------------|-----------------|---------------|
| Stone       | Scissor         | User Wins     |
| Stone       | Paper           | Computer Wins |
| Paper       | Stone           | User Wins     |
| Paper       | Scissor         | Computer Wins |
| Scissor     | Paper           | User Wins     |
| Scissor     | Stone           | Computer Wins |
| Any         | Same            | Tie           |

---

## Future Improvements

- [ ] Add a GUI for each project using Tkinter
- [ ] Persist data using JSON or SQLite
- [ ] Add more mini projects to the collection
- [ ] Add unit tests for each project

---

## Contributing

Contributions are welcome. Feel free to fork the repo and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## Author

Developed by [Rohan Mishra](https://github.com/RohanMishra-01)
