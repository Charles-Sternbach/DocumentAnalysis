# -*- coding: utf-8 -*-
"""
Purpose:
Develop a script that will analyze the style and sophistication of a document
given by the user. Then compare this document for similarities with a second
document provided by the user.

@author: Charles Sternbach
"""
#Import regular expression operations.
import re

def get_input(message):
    """Read in a message string and return input from the user.

    Args:
        message: Message to prompt the user with.

    Returns:
        string: A string containing a response message from the user.
    """
    user_input = input(message)
    print(user_input)
    return user_input

def parse(string):
    """Read in a string and return a list of strings containing only letters.

    Args:
        string: Input document read into a single string.

    Returns:
        list: A list of strings containing only letters.
    """
    list_of_strings = string.split()
    word_list = []
    for word in list_of_strings:
        #Remove all characters from "word" that are not letters.
        word = re.sub('[^A-Za-z]+', '', word)
        if len(word) > 0:
            word = word.lower()
            word_list.append(word)
    return word_list

def remove_stop_words(stop_set, word_list):
    """Removes any "stop words" in a list of words.

    Reads in a set containing "stop words" and a list of words.
    Remove any "stop words" words contained in the word list.

    Args:
        stop_set: Set of words known as "stop words". Words that appear so
            frequently in text that they should be ignored.
        word_list: list of words represented the parsed input document.

    Returns:
        list: A list of words with "stop words" removed.
    """
    word_list_without_stop_words = []
    for word in word_list:
        if not word in stop_set:
            word_list_without_stop_words.append(word)
    return word_list_without_stop_words

def print_avg_word_length(word_list):
    """Prints the average length of a list of words.

    Reads in a word list, calls get_avg_word_length method and prints
    the computed average word length.

    Args:
        word_list: list of words representing the parsed input document.
    """
    print("1. Average word length: %s" % (round(get_avg_word_length(word_list), 2)))

def get_avg_word_length(word_list):
    """Computes the average word length of a list of words.

    Args:
        word_list: list of words representing the parsed input document.

    Returns:
        float: Average word length.
    """
    word_count = 0
    total_word_length = 0
    for word in word_list:
        word_count = word_count + 1
        total_word_length = total_word_length + len(word)
    return total_word_length / word_count

def print_ratio_distinct_words(word_list):
    """Computes and prints the ratio of distinct words to total words.

    Args:
        word_list: list of words representing the parsed input document.
    """
    print("2. Ratio of distinct words to total words: %.03f" % (round(len(set(word_list)) / len(word_list), 3)))

def print_words_for_a_length(file, word_set):
    """Display a list showing the number of words that exist for a certain length.

    Display a list containing a range from 0-x where x is the length of
    the largest word in word_set. For each length, print the number of
    different words having that length, and at most six of these words.
    If there are more than six words, print the first and last three in
    alphabetical order.

    Args:
        file: A string containing the file name of the input document.
        word_set: List containing the parsed input document.
    """
    print("3. Word sets for document %s" % (file) + str(':'))
    # Find length of longest word
    max_length = 0
    for word in word_set:
        if len(word) > max_length:
            max_length = len(word)

    # Print evaluation for each length:
    for length in range(max_length):
        words = []
        for word in word_set:
            if len(word) == length + 1:
                words.append(word)
        words_sorted = sorted(words)
        if len(words_sorted) > 6:
            words_output = words_sorted[0] + " " + words_sorted[1] + " " + words_sorted[2] + " ... " \
                           + words_sorted[-3] + " " + words_sorted[-2] + " " + words_sorted[-1]
        else:
            s = " "
            words_output = s.join(words_sorted)
        spaces_2 = '   ' if len(words) < 10 else '  '

        if len(words_output) == 0:
            spaces_1 = '   ' if length < 10 else '  '
            print("%s%s:%s%s:" % (spaces_1, length + 1, spaces_2, len(words)))
        elif length < 9:
            print("   %s:%s%s: %s" % (length + 1, spaces_2, len(words), words_output))
        else:
            print("  %s:%s%s: %s" % (length + 1, spaces_2, len(words), words_output))

def print_distinct_word_pairs(file, word_list, max_sep):
    """Display the number of distinct word pairs and list them in the document.

    Print the number of distinct word pairs in the document with proper
    formatting. A word pair is a two-tuple of words that appear max_sep
    or fewer positions apart in the documents list.

    Args:
        file: A string containing the file name of the input document.
        word_list: List of words representing the parsed input document.
        max_sep: Integer value specifying how far apart two words can
            be in the document to form a pair.
    """
    print("4. Word pairs for document %s" % (file))
    list1, total_pairs_count, distinct_pairs_count = get_distinct_word_pairs(word_list, max_sep)
    ratio_of_distinct_word_pairs_to_total = distinct_pairs_count / total_pairs_count

    print("  %s distinct pairs" % (distinct_pairs_count))
    # Sort tuple list by key of left side, and then right side of each tuple.
    list1 = sorted(list1)
    length = len(list1)
    for i in range(5):
        tuple2 = list1[i]
        list2 = list(tuple2)
        print("  %s %s" % (list2[0], list2[1]))
    print('  ...')
    for i in range(length - 5, length):
        tuple2 = list1[i]
        list2 = list(tuple2)
        print("  %s %s" % (list2[0], list2[1]))
    print("5. Ratio of distinct word pairs to total: %.03f" % (round(ratio_of_distinct_word_pairs_to_total, 3)))

def get_distinct_word_pairs(word_list, max_sep):
    """Generate distinct word pairs from a list based on a maximum separation limit.

    Calculate the number of distinct word pairs and the total number
    of word pairs in the document given the max_sep value. Create a list
    of tuples which contain all distinct word pairs found in the document.

    Args:
        word_list: List of words representing the parsed input document.
        max_sep: Integer value specifying how far apart two words can
            be in the document to form a pair.

    Returns:
        tuple: A tuple containing a list of tuples containing distinct word
        pairs, the number of distinct word pairs and the total number of word
        pairs in the document.
    """
    list1 = []
    total_word_count = len(word_list)
    for i in range(total_word_count):
        # Prevent out of bounds in list after last element.
        end = i + 1 + max_sep
        if end >= total_word_count:
            end = total_word_count
        # Advance forward in list up to max_sep positions.
        for j in range(i + 1, end):
            # Store tuple with 2 strings in alphabetical order inside tuple.
            if word_list[i] <= word_list[j]:
                tuple1 = (word_list[i], word_list[j])
            else:
                tuple1 = (word_list[j], word_list[i])
            # Since we are always going forward and storing 2 items in order in the tuple, no danger of duplicates.
            list1.append(tuple1)
    total_pairs_count = len(list1)
    list1 = list(set(list1))
    distinct_pairs_count = len(list1)
    return list1, total_pairs_count, distinct_pairs_count

def compare_documents(file_1, f1_word_list, file_2, f2_word_list):
    """Provide a complexity and similarity comparison between two documents.

    Prints out a summary comparison regarding the complexity and similarity
    between the input documents. Measures the word length between documents.
    Then measures the Jaccard similarity in overall word use, of word use
    for each word length, and between word pair sets.

    Args:
        file_1: String containing the file name of the first input document.
        f1_word_list: List of words representing the first parsed input document.
        file_2: String containing the file name of the second input document.
        f2_word_list: List of words representing the second parsed input document.
    """
    print("\nSummary comparison")
    f1_avg_word_length = get_avg_word_length(f1_word_list)
    f2_avg_word_length = get_avg_word_length(f2_word_list)
    if f1_avg_word_length > f2_avg_word_length:
        print("1. %s on average uses longer words than %s" % (file_1, file_2))
    else:
        print("1. %s on average uses longer words than %s" % (file_2, file_1))

    f1_word_set = set(f1_word_list)
    f2_word_set = set(f2_word_list)
    set_union = f1_word_set | f2_word_set
    set_intersection = f1_word_set & f2_word_set
    # set_difference   = f1_word_set - f2_word_set
    # set_symmetric_difference = f1_word_set ^ f2_word_set
    jaccard_similarity = len(set_intersection) / len(set_union)
    print("2. Overall word use similarity: %.03f" % (round(jaccard_similarity, 3)))

    print("3. Word use similarity by length:")
    f1_list_of_sets_for_each_word_length = get_words_for_each_length(set(f1_word_list))
    f2_list_of_sets_for_each_word_length = get_words_for_each_length(set(f2_word_list))
    f1_length = len(f1_list_of_sets_for_each_word_length)
    f2_length = len(f2_list_of_sets_for_each_word_length)
    if f1_length > f2_length:
        max_length = f1_length
    else:
        max_length = f2_length
    for i in range(max_length):
        if i < f1_length and i < f2_length:
            set_union = f1_list_of_sets_for_each_word_length[i] | f2_list_of_sets_for_each_word_length[i]
            set_intersection = f1_list_of_sets_for_each_word_length[i] & f2_list_of_sets_for_each_word_length[i]
            if 0 == len(set_intersection) or 0 == len(set_union):
                jaccard_similarity = 0  # Prevent divide by 0.
            else:
                jaccard_similarity = len(set_intersection) / len(set_union)
            if i < 9:
                print("   %s: %.04f" % (i + 1, round(jaccard_similarity, 4)))
            else:
                print("  %s: %.04f" % (i + 1, round(jaccard_similarity, 4)))
        elif i < 9:
            print("   %s: %.04f" % (i + 1, round(0, 4)))
        else:
            print("  %s: %.04f" % (i + 1, round(0, 4)))
    f1_list1, f1_total_pairs_count, f1_distinct_pairs_count = get_distinct_word_pairs(file_1, f1_word_list, max_sep)
    f2_list1, f2_total_pairs_count, f2_distinct_pairs_count = get_distinct_word_pairs(file_2, f2_word_list, max_sep)
    f1_word_set = set(f1_list1)
    f2_word_set = set(f2_list1)
    set_union = f1_word_set | f2_word_set
    set_intersection = f1_word_set & f2_word_set
    # set_difference   = f1_word_set - f2_word_set
    # set_symmetric_difference = f1_word_set ^ f2_word_set
    jaccard_similarity = len(set_intersection) / len(set_union)
    print("4. Word pair similarity: %.04f" % (round(jaccard_similarity, 4)))

def get_words_for_each_length(word_set):
    """Generate a list of sets for each word length.

    Args:
        word_set: Set of words representing the parsed input document.

    Returns:
        list: A list of sets, where each set contains words of a
        particular length.
    """
    list_of_sets = []

    # Find length of longest word
    max_length = 0
    for word in word_set:
        if len(word) > max_length:
            max_length = len(word)

    # Create a set of words for each word length and store in a list.
    for length in range(max_length):
        words_for_1_word_length = set()
        for word in word_set:
            if len(word) == length + 1:
                words_for_1_word_length.add(word)
        list_of_sets.append(words_for_1_word_length)

    return list_of_sets

if __name__ == "__main__":
    #Read in text files from the user: Usage: testDocuments/filename.txt
    file_1 = get_input("Enter the first file to analyze and compare ==> ")
    file_2 = get_input("Enter the second file to analyze and compare ==> ")

    #Read in stop.txt. Contains words appear so frequently in text that they should be ignored.
    file_3 = 'testDocuments/stop.txt'

    #A word pair is a two-tuple of words that appear max_sep of fewer positions apart in the document.
    max_sep = int(get_input("Enter the maximum separation between words in a pair ==> "))

    #Open each file, read the contents of each file into a string.
    f1 = open(file_1, 'r')
    f2 = open(file_2, 'r')
    f3 = open(file_3, 'r')

    f1_string = f1.read()
    f2_string = f2.read()
    f3_string = f3.read()

    #Parse each document string to remove all non-letters and convert each word to lowercase.
    f1_word_list = parse(f1_string)
    f2_word_list = parse(f2_string)
    f3_word_list = parse(f3_string)
    #After parsing "stop.txt" convert the list into a set. To be used later.
    stop_set = set(f3_word_list)

    #Remove any "stop" words that may be contained in both input documents.
    f1_word_list = remove_stop_words(stop_set, f1_word_list)
    f2_word_list = remove_stop_words(stop_set, f2_word_list)

    #Analyze each documents word list.
    #See "Analyze Each Document's Word List" in README.txt.
    print("\nEvaluating document: %s" % file_1)
    print_avg_word_length(f1_word_list)
    print_ratio_distinct_words(f1_word_list)
    print_words_for_a_length(file_1, set(f1_word_list))
    print_distinct_word_pairs(file_1, f1_word_list, max_sep)

    print("\nEvaluating document: %s" % file_2)
    print_avg_word_length(f2_word_list)
    print_ratio_distinct_words(f2_word_list)
    print_words_for_a_length(file_2, set(f2_word_list))
    print_distinct_word_pairs(file_2, f2_word_list, max_sep)

    #Provide a summary comparison regarding the complexity and similarity of the input documents.
    #See "Compare Documents" section in README.txt for more details.
    compare_documents(file_1, f1_word_list, file_2, f2_word_list)