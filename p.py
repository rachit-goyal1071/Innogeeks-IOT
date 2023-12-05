def create_file(filename):
    file = open(filename, 'w')
    content = input("Enter the content:")
    file.write(content)
    file.close()
    
    f = open(filename, 'r')
    print(f.read())
    f.close()

# Test the function
create_file('new_file.txt')

