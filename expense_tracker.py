import pandas as pd 
import numpy as np 
import os
import matplotlib.pyplot as plt

File_Name = "expense_tracker.csv"

if os.path.exists(File_Name):
    df = pd.read_csv(File_Name)
else:
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (food, travel, bills, shopping, entertainment): ").strip().lower()
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    df.loc[len(df)] = [date, category, amount, description]
    df.to_csv(File_Name, index=False)

def view_expenses():
    if df.empty:
        print("No expenses found")
    else:
        print(df)

def update_expense():
    view_expenses()
    try:
        index = int(input("Enter index to update: "))
    except:
        print("Invalid index")
        return
    if index not in df.index:
        print("Invalid index")
        return
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (food, travel, bills, shopping, entertainment): ").strip().lower()
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    df.loc[index] = [date, category, amount, description]
    df.to_csv(File_Name, index=False)

def delete_expense():
    view_expenses()
    try:
        index = int(input("Enter index to delete: "))
    except:
        print("Invalid index")
        return
    if index not in df.index:
        print("Invalid index")
        return
    df.drop(index, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(File_Name, index=False)

def category_summary():
    if df.empty:
        print("No expenses found")
    else:
        print(df.groupby("Category")["Amount"].sum())

def monthly_total():
    if df.empty:
        print("No expenses found")
        return

    df["Date"] = pd.to_datetime(df["Date"],format="%d-%m-%Y")
    df["Month"] = df["Date"].dt.month_name()
    monthly_total = df.groupby("Month")["Amount"].sum()
    print(monthly_total)

def highest_expense():
    if df.empty:
        print("No expenses found")
    else:
        print(df.loc[df["Amount"].idxmax()])

def graph():
    if df.empty:
        print("No expenses found")
        return
    category_sum = df.groupby("Category")["Amount"].sum().sort_values()
    plt.bar(category_sum.index, category_sum.values)
    plt.title("Category wise expense")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def piechart():
    if df.empty:
        print("No expenses found")
        return
    category_sum = df.groupby("Category")["Amount"].sum()
    plt.figure()
    category_sum.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Category wise expense")
    plt.show()

def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Category Summary")
        print("6. Monthly Total")
        print("7. Highest Expense")
        print("8. Graph")
        print("9. Pie Chart")
        print("10. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid choice")
            continue
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3: 
            update_expense()
        elif choice == 4:
            delete_expense()
        elif choice == 5:
            category_summary()
        elif choice == 6:
            monthly_total()
        elif choice == 7:
            highest_expense()
        elif choice == 8:
            graph()
        elif choice == 9:
            piechart()
        elif choice == 10:
            break

main()