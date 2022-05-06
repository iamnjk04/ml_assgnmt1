student = ['NJK', 'Zimba', 'Anku', 'Shrz', 'Zimba', 'Hancy','Hancy']
percentage = [80, 47, 73, 97, 52,86,56]     
print("\nCombine the values of the said two lists into a dictionary:")
dictionary = dict(zip(student, percentage))
dictionary = dict((k, v) for k, v in dictionary.items() if v >= 50)
print(dictionary)