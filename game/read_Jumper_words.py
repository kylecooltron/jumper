import csv

class read_Jumper_words:
    def read_Jumper_words(filename, key_index_num):
        dictionary = {}
        try:
            with open(filename, "rt") as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                for row_list in reader:
                    key = row_list[key_index_num]
                    dictionary[key] = row_list
            return dictionary
        except PermissionError as perm_err:
            print("Error: You do not have permission to open this file")
            print(perm_err)
            exit()