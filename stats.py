def get_word_count(text):
    text_array = text.split()
    num_words = len(text_array)
    return num_words

def get_char_count(text):
    text = text.lower()
    c_dic = {}
    for c in text:
        if c in c_dic:
            c_dic[c] += 1
        else:
            c_dic[c] = 1
    return c_dic

def print_report(filepath, wc, dic):
    report_sort = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    print("=============== BOOKBOT ===============")
    print(f"Analyzing book found at {filepath}")
    print("------------ Word Count --------------")
    print(f"Found {wc} total words")
    print("------ Character Count ------")
    for report_list in report_sort:
        if report_list[0].isalpha():
            print(f"{report_list[0]}: {report_list[1]}")
    print("================= END =================")
