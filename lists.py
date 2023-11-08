friends = ["kevin", "karen" , "jim ", "oscar", "toby"]

print(friends[0]) 
print(friends[-1])
print(friends[1:]) 
# from 1 up to but not including 3
print(friends[1:3])
friends[1] = "mike"

# List functions
luck_num = [4,8,15,16,24,42]

friends.extend(luck_num)

friends.append("creed")

friends.insert(1, "kelly")

friends.remove("jim")

# friends.clear()

friends.pop()

friends.index("kevin")

friends.count("jim")

friends.sort()
luck_num.sort()

luck_num.reverse() 

friends2 = friends.copy()

friends[1:2]

friends[::2]

new_list = list.copy()