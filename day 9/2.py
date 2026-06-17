batsman = {"Rohit Sharma", "Virat Kohli", "KL Rahul", "Hardik Pandya", " Krunal Pandya"}

bowler = {"Jasprit Bumrah", "Bhuvneshwar Kumar", "Mohammed Shami", "Hardik Pandya", " Krunal Pandya"}

uni = batsman.union(bowler)
print(uni)
print("\n")
intr = batsman.intersection(bowler)
print(intr)
print("\n")

diff =batsman.difference(bowler)
print(diff)