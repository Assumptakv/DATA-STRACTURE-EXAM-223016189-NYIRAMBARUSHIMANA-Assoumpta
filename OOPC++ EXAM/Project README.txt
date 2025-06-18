ATM Cash Dispenser Simulator (C++ Project)-README

         I. Project Description

This C++ program simulates an ATM cash dispenser system that allows users to:
* Add and remove currency denominations (e.g., 5000 Frw, 2000 Frw).
* Withdraw money using two different strategies:
1. Greedy Algorithm – uses the largest denominations first.
2. Optimal Algorithm – uses the least number of notes.
It demonstrates key Object-Oriented Programming (OOP) concepts such as inheritance, polymorphism, abstraction, and dynamic memory management.

            II. Assigned Task

* Use inheritance and polymorphism to model a cash dispenser.
* Implement two strategies for dispensing cash:
o Greedy: Prioritizes higher denominations.
o Optimal: Minimizes the number of notes used.
* Allow the user to:
o Dynamically add or remove denominations.
o Interact with the system via a text menu.
* Clean up all dynamically allocated memory.


        III. How It Was Completed

1. Class Structure
* Denomination: A struct storing the value and a pointer to the number of available notes.
* Dispenser: Abstract base class containing a pure virtual function withdraw().
* GreedyDispenser: Derived class implementing the greedy withdrawal strategy.
* OptimalDispenser: Derived class implementing the least-notes withdrawal strategy using Depth-First Search (DFS).
2. Memory Management
* Denomination counts are dynamically allocated (new int) and properly deleted to avoid memory leaks.
* Denominations can be added or removed at runtime, and their memory is managed with care.
3. Strategies
* Greedy: Tries to use the highest denomination as much as possible.
* Optimal: Searches all combinations using recursion to find the one with the fewest notes.
4. User Menu
The main() function provides a looped menu:
* Option 1: Add a denomination.
* Option 2: Remove a denomination.
* Option 3: Withdraw using the Greedy strategy.
* Option 4: Withdraw using the Optimal strategy.
* Option 5: View available denominations.
* Option 0: Exit and clean memory.
5. Code Annotations
The source code is fully commented to explain:
* The purpose of each function and class.
* How dynamic memory and pointers are used.
* The control flow of the withdrawal algorithms.
*   Sample Output (Screenshots Recommended)
You should include screenshots of:
1. Adding denominations.
2. A successful greedy withdrawal.
3. A successful optimal withdrawal.
4. A failed withdrawal (e.g., amount not dispensable).
5. Current denominations after transactions.
Key C++ Concepts Demonstrated
* Classes & Inheritance
* Pure Virtual Functions
* Dynamic Memory (new and delete)
* Vectors and Algorithms
* Function Objects (std::function)
* Recursive Search (DFS)
* Example Use Case

ATM Cash Dispenser
1. Add Denomination
2. Remove Denomination
3. Withdraw (Greedy)
4. Withdraw (Optimal)
5. Show Denominations
0. Exit
Enter choice: 1
Enter denomination value and count: 5000 5
Added denomination: 5000 x 5

Enter choice: 3
Enter amount to withdraw: 10000
Take 2 x 5000
Withdrawal successful.

* Memory Management Notes
At the end of the program, all dynamically allocated memory for:
* Denomination counts (int*)
* Denomination array (Denomination*)
is deleted to avoid memory leaks.


  IV. Annotated codes with comments

#include <iostream>       // For input and output
#include <vector>         // For using the vector container
#include <algorithm>      // For functions like min()
#include <climits>        // For INT_MAX constant
#include <functional>     // For using std::function
using namespace std;

// Structure to represent a denomination with value and pointer to count
struct Denomination {
    int value;        // The value of the note
    int* count;       // Pointer to the number of available notes of this denomination
};

// Abstract base class for Dispenser
class Dispenser {
protected:
    Denomination* denoms;  // Pointer to array of Denomination
    int n;                 // Number of denominations
public:
    Dispenser(Denomination* d, int size) : denoms(d), n(size) {}  // Constructor
    virtual bool withdraw(int amount) = 0; // Pure virtual function for withdrawal
    virtual ~Dispenser() {}               // Virtual destructor
};

// Greedy strategy: use largest denominations first
class GreedyDispenser : public Dispenser {
public:
    GreedyDispenser(Denomination* d, int size) : Dispenser(d, size) {}

    bool withdraw(int amount) override {
        cout << "\nGreedy withdrawal attempt: " << amount << endl;
        vector<int> tempCounts(n); // Copy of current counts
        for (int i = 0; i < n; ++i)
            tempCounts[i] = *(denoms + i)->count;

        for (int i = 0; i < n; ++i) {
            int take = min(tempCounts[i], amount / denoms[i].value); // Max number of notes to use
            amount -= take * denoms[i].value; // Reduce the amount
            tempCounts[i] -= take; // Reduce from temporary count
            if (take > 0)
                cout << "Take " << take << " x " << denoms[i].value << endl;
        }

        if (amount == 0) {
            for (int i = 0; i < n; ++i)
                *(denoms + i)->count = tempCounts[i];
            cout << "Withdrawal successful.\n";
            return true;
        }
        cout << "Cannot dispense full amount.\n";
        return false;
    }
};

// Optimal strategy: use the least number of notes
class OptimalDispenser : public Dispenser {
public:
    OptimalDispenser(Denomination* d, int size) : Dispenser(d, size) {}

    bool withdraw(int amount) override {
        cout << "\nOptimal withdrawal attempt: " << amount << endl;
        vector<int> current(n, 0), bestCombo(n, 0); // Track current and best combo
        int minNotes = INT_MAX;

        function<void(int, int)> dfs = [&](int idx, int rem) {
            if (rem == 0) {
                int totalNotes = 0;
                for (int c : current) totalNotes += c;
                if (totalNotes < minNotes) {
                    minNotes = totalNotes;
                    bestCombo = current;
                }
                return;
            }
            if (idx == n || rem < 0) return;

            int maxUse = min(*(denoms + idx)->count, rem / (denoms + idx)->value);
            for (int i = 0; i <= maxUse; ++i) {
                current[idx] = i;
                dfs(idx + 1, rem - i * (denoms + idx)->value);
                current[idx] = 0;
            }
        };

        dfs(0, amount);

        if (minNotes == INT_MAX) {
            cout << "Cannot dispense full amount optimally.\n";
            return false;
        }

        for (int i = 0; i < n; ++i) {
            if (bestCombo[i] > 0) {
                cout << "Take " << bestCombo[i] << " x " << denoms[i].value << endl;
                *(denoms + i)->count -= bestCombo[i];
            }
        }
        cout << "Withdrawal successful.\n";
        return true;
    }
};

// Global variables for denominations
Denomination* denoms = nullptr;
int nDenoms = 0;

// Add a new denomination
void addDenomination(int value, int count) {
    Denomination* newDenoms = new Denomination[nDenoms + 1];
    for (int i = 0; i < nDenoms; ++i)
        newDenoms[i] = denoms[i];

    int* c = new int(count);
    newDenoms[nDenoms] = { value, c };

    delete[] denoms;
    denoms = newDenoms;
    nDenoms++;
    cout << "Added denomination: " << value << " x " << count << endl;
}

// Remove a denomination
void removeDenomination(int value) {
    int idx = -1;
    for (int i = 0; i < nDenoms; ++i) {
        if (denoms[i].value == value) {
            idx = i;
            break;
        }
    }
    if (idx == -1) {
        cout << "Value not found.\n";
        return;
    }

    delete denoms[idx].count; // Free memory of count
    Denomination* newDenoms = new Denomination[nDenoms - 1];
    for (int i = 0, j = 0; i < nDenoms; ++i) {
        if (i != idx)
            newDenoms[j++] = denoms[i];
    }
    delete[] denoms;
    denoms = newDenoms;
    nDenoms--;
    cout << "Removed denomination: " << value << endl;
}

// Display current denominations
void showDenominations() {
    cout << "\nCurrent Denominations:\n";
    for (int i = 0; i < nDenoms; ++i)
        cout << denoms[i].value << " x " << *denoms[i].count << endl;
}

int main() {
    Dispenser* machines[2]; // machines[0] = Greedy, machines[1] = Optimal
    int choice;

    while (true) {
        cout << "\nATM Cash Dispenser\n";
        cout << "1. Add Denomination\n";
        cout << "2. Remove Denomination\n";
        cout << "3. Withdraw (Greedy)\n";
        cout << "4. Withdraw (Optimal)\n";
        cout << "5. Show Denominations\n";
        cout << "0. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 0) break;

        switch (choice) {
            case 1: {
                int v, c;
                cout << "Enter denomination value and count: ";
                cin >> v >> c;
                addDenomination(v, c);
                break;
            }
            case 2: {
                int v;
                cout << "Enter denomination value to remove: ";
                cin >> v;
                removeDenomination(v);
                break;
            }
            case 3: {
                if (nDenoms == 0) {
                    cout << "No denominations available.\n";
                    break;
                }
                int amt;
                cout << "Enter amount to withdraw: ";
                cin >> amt;
                machines[0] = new GreedyDispenser(denoms, nDenoms);
                machines[0]->withdraw(amt);
                delete machines[0];
                break;
            }
            case 4: {
                if (nDenoms == 0) {
                    cout << "No denominations available.\n";
                    break;
                }
                int amt;
                cout << "Enter amount to withdraw: ";
                cin >> amt;
                machines[1] = new OptimalDispenser(denoms, nDenoms);
                machines[1]->withdraw(amt);
                delete machines[1];
                break;
            }
            case 5:
                showDenominations();
                break;
            default:
                cout << "Invalid option.\n";
        }
    }

    for (int i = 0; i < nDenoms; ++i)
        delete denoms[i].count; // Free count memory
    delete[] denoms;           // Free denomination array

    cout << "Exiting ATM system.\n";
    return 0;
}



