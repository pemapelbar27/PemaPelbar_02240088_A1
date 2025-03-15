def word_counter(file):
    word_list = ["are", "was", "and"]
    try:
        with open(file, "r", encoding = "utf-8") as file:
            text_content = file.read().lower().split()
            word_counts = {}
            for word in word_list:
                word_counts[word] = text_content.count(word)
        return word_counts
    except FileNotFoundError:
        print("The file not found.")
file_path = input("Enter file_path:")
print('Word count results:', word_counter(file_path))