# Print the multiplication table of 7 (7 x 1 to 7 x 10) in the format:  7 x 1 = 7

start = 1
end = 11
step = 1
for i in range(start, end, step):
    answer = 7 * i
    print("7X" + str(i) + "=" + str(answer))