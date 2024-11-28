README for Bucket Problem Solution 🚰🪣
Bucket Problem Solution in Python 🧪💻
This Python program solves the classic bucket problem using three buckets of different capacities (3 liters, 5 liters, and 9 liters) with the goal of achieving exactly 7 liters in the third bucket. The solution uses random actions and optimization techniques to simulate the process.

Problem Statement ❓
Given:

🪣 3-Liter Bucket
🪣 5-Liter Bucket
🪣 9-Liter Bucket
🎯 Goal: The third bucket must hold exactly 7 liters.

How the Program Works 🛠️
The program simulates filling, pouring, and transferring water between the buckets through the following steps:

1️⃣ Filling buckets: Each bucket can be filled to its maximum capacity.
2️⃣ Pouring buckets: A bucket can be emptied completely.
3️⃣ Transferring water: Water can be transferred from one bucket to another until the receiving bucket is full or the source bucket is empty.
4️⃣ Optimization: A heuristic method (set_optimization) attempts to prioritize efficient moves to achieve the desired result.

Key Functions ⚙️
fill_<bucket>(): Fills a specific bucket to its maximum capacity.
pour_<bucket>(): Empties a specific bucket.
pour_<source>_to_<destination>(): Transfers water from one bucket to another.
set_optimization(): Checks possible combinations to quickly reach 7 liters in the third bucket.
random_func_generator(): Executes random actions until the desired result is achieved.
Code Output 📋
When executed, the program outputs:

1️⃣ Number of steps: Total iterations taken to achieve the solution.
2️⃣ Final state: Water level in each bucket after achieving the goal.

Example Output:
yaml
Copy code
The process took place in 15 stages
First bucket: 0 L
Second bucket: 1 L
Third bucket: 7 L
How to Run 🚀
Clone this repository:
bash
Copy code
git clone <repository_url>
Navigate to the project folder:
bash
Copy code
cd bucket-problem
Run the Python file:
bash
Copy code
python bucket_problem.py
💡 Enjoy solving the bucket problem with Python! 🧑‍💻🎉
