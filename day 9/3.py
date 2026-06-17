orange_cap = {"Virat Kohli": 890, "Rohit Sharma": 850, "David Warner": 780}

print(orange_cap["David Warner"])
# print(orange_cap["KL Rahul"])
orange_cap.update({"KL Rahul": 750})
print(orange_cap["KL Rahul"])

for i,v in orange_cap.items():
    print("key: " + i + " value: " + str(v))