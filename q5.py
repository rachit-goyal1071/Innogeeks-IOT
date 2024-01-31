def fetch_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = fetch_even_numbers(numbers)
print(even_nums)

def create_file(filename):
    try:
        file = open(filename, 'w')
        file.write("This is a new file")
    finally:
        file.close()

# Test the function
create_file('new_file.txt')