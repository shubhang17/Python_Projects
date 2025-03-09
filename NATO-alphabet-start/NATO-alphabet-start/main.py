# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
import pandas
#TODO 1: To import a Dictionary in Readable format as A:"alfa"
new_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_new_dict = {row.letter:row.code for (index,row) in new_dict.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word=input("Enter a Word: ").upper()
output_list=[nato_new_dict[letter] for letter in user_word]
print(output_list)