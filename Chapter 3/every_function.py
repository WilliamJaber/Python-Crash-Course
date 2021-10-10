lst_of_languages = ['Spanish', 'English', 'Arabic', 'Dutch']
print(lst_of_languages)

# Accessing Elements in a List & Using Individual Values from a List.
print(f'{lst_of_languages[0]} is my native language.')

# Modifying Elements in a List
lst_of_languages[-1] = 'French'
print(lst_of_languages)

# Appending Elements to the End of a List.
lst_of_languages.append('Chinese')
print(lst_of_languages)

# Inserting Elements into a List.
lst_of_languages.insert(-1, 'Dutch')
print(lst_of_languages)

# Removing an Item Using the pop() Method.
lst_of_languages.pop()
print(lst_of_languages)

# Popping Items from any Position in a List.
lst_of_languages.pop(-1)
print(lst_of_languages)

# Removing an Item by Value.
lst_of_languages.remove('French')
print(lst_of_languages)

# Removing an Item Using the del Statement.
del lst_of_languages[-1]
print(lst_of_languages)

# Sorting a List Temporarily with the sorted() Function.
print(sorted(lst_of_languages))

# Printing a List in Reverse Order.
lst_of_languages.reverse()
print(lst_of_languages)

# Finding the Length of a List.
print(len(lst_of_languages))

# Sorting a List Permanently with the sort() Method.
lst_of_languages.sort()
print(lst_of_languages)

lst_of_languages.sort(reverse=True)
print(lst_of_languages)
