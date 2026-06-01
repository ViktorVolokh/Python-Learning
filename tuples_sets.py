import random
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)
rect_area, rect_perimeter = calculate_rectangle(10, 5)
print(f"area: {rect_area} perimeter: {rect_perimeter}")
set1 = {1, 4, 1, 2, 3, 4, 4, 6}
print(set1)
set2 = set(range(2, 20, 2))
print(set2)
print(set1 | set2)
print(set1 & set2)
i = 0
stats = []
while i < 1000:
    random_numbers = [random.randint(1, 100000) for i in range(1000000)]
    unique_numbers = set(random_numbers)
    stats.append(len(unique_numbers))
    i = i + 1
#results of one loop
print(max(stats)) #100000
print(min(stats)) #99989
print(sum(stats) / len(stats)) #99995.47
# Conclusion: Set deduplication consistently reaches the theoretical limit.


