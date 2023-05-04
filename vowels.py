def vowels(String):
    return [each for each in String if each in "aeiou"]
test = input("Enter any word: ")
result = vowels(test)
print(result)


print("............................................................................")

def capitali(String):
    return String.upper()
word = input("Enter the desired word any case :")
print(capitali(word))

print("...............................................................")

def merge_dicts(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3

doc1 = {1:"hello", 2:"world"}
doc2 = {3:"Hope", 4:"Your Doing well"}
print(merge_dicts(doc1, doc2))




