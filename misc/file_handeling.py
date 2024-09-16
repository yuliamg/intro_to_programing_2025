with open('./example.txt', 'r') as file:
    content_of_file = file.readlines()

print('Before modifications:', content_of_file)

first_line = content_of_file[0]

first_line = first_line + ' Added text '

content_of_file[0] = first_line

print('After modifications:', content_of_file)

to_write_modified = ''.join( content_of_file )

print(to_write_modified)
print(content_of_file)

# writing file:
with open('./output.txt', 'w') as file:
    file.write(to_write_modified)
