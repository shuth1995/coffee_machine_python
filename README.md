# Coffee Machine Simulator

This project simulates a basic coffee vending machine using Python. Users can interact with the machine through the terminal to:

- Buy espresso, latte, or cappuccino
- Refill the machine's ingredients
- Withdraw cash
- View remaining resources
- Exit the machine

The logic is implemented using object-oriented programming (OOP), encapsulating drink types and machine state.

---

## 💡 Features

- Ingredient tracking (water, milk, beans, cups)
- Dynamic inventory updates
- Order handling based on resource availability
- Cash accumulation and withdrawal
- Console-based user interaction

---

## 🧾 Example Session
```text
Write action (buy, fill, take, remaining, exit):

buy
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
1

I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):

remaining

The coffee machine has:
150 ml of water
400 ml of milk
104 g of coffee beans
7 disposable cups
$558 of money
```

---

## 🚀 Getting Started

To run the program:

```bash
python coffee_machine.py
```

## 📁 File Structure
•	coffee_machine.py: main program file
•	README.md: project description and usage
•	requirements.txt: dependencies
