# -*- coding: utf-8 -*-
"""
Purpose:
Develop a script that will analyze the style and sophistication of a document given by the user.
This document will also be compared for similarities with a second document given by the user.

@author: Charles Sternbach
"""
#Import regular expression operations.
import re

def get_input(message):
    """
    get_input(message) Reads in a message string and returns the user's input.
    :param message: Prompt the user with desired message.
    :return: The input provided by the user after reading message prompt.
    """
    user_input = input(message)
    print(user_input)
    return user_input

def parse(string):
    """
    parse(string) Reads in a string and returns a list of strings.
        For each word, all characters that are not letters are removed.
    :param string: Input document read into a single string.
    :return: Output document represented by list of words containing only letters.
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
    """
    remove_stop_words(stop_set, word_list) Reads in a set containing stop words and a list of words.
        Remove any "stop words" contained in word list.
    :param stop_set: Sets of words known as "stop words". Words that appear so frequently
        in text that they should be ignored.
    :param word_list: Input document which has been parsed using the parse() method.
    :return: Output document represented by a list which contains no "stop words".
    """
    word_list_without_stop_words = []
    for word in word_list:
        if not word in stop_set:
            word_list_without_stop_words.append(word)
    return word_list_without_stop_words

def print_avg_word_length(word_list):
    """
    print_avg_word_length(word_list) Reads in a word list, calls get_avg_word_length() method,
        and prints the value computed.
    :param word_list: Input document which includes a list of parsed words.
    :return:
    """
    print("1. Average word length: %s" % (round(get_avg_word_length(word_list), 2)))

def get_avg_word_length(word_list):
    """
    get_avg_word_length(word_list) Reads in a word list, then computes the average word length.
    :param word_list: Input document which includes a list of parsed words.
    :return: Average word length.
    """
    word_count = 0
    total_word_length = 0
    for word in word_list:
        word_count = word_count + 1
        total_word_length = total_word_length + len(word)
    return total_word_length / word_count

def print_ratio_distinct_words(word_list):
    """
    print_ratio_distinct_words(word_list) Reads in a word list, computes the ratio of distinct words
        to total words and prints the result.
    :param word_list: Input document which includes a list of parsed words.
    :return:
    """
    print("2. Ratio of distinct words to total words: %.03f" % (round(len(set(word_list)) / len(word_list), 3)))

def print_words_for_a_length(file, word_set):
    """
    print_words_for_a_length(file, word_set) Reads in a file name and corresponding word list.
        Print out a display containing a range from 0-x where x is the length of the largest word in word_set.
        For each length, print the number of different words having that length, and at most six of these words.
        If for a certain length, there are six or fewer words, then print all six,
            buf if there are more than six print the first three and the last three in alphabetical order.
    :param file: The file name of the input document.
    :param word_set: Input document which contains a set of all parsed words.
    :return:
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
    """
    print_distinct_word_pairs(file, word_list, max_sep) reads a file name, list of words, and max_sep value.
        Prints the number of distinct word pairs in the document with proper formatting. A word pair is a two-tuple of words
        that appear max_sep or fewer positions apart in the documents list.
    :param file: The file name of the input document.
    :param word_list: Input document which includes a list of parsed words.
    :param max_sep: Specifies how far apart two words can be in the document to form a pair.
    :return:
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
    """
    get_distinct_word_pairs(file, word_list, max_sep) reads a file name, list of words, and max_sep value.
        Calculates the total number of word pairs and distinct word pairs in the document.
        A word pair is a two-tuple of words that appear max_sep or fewer positions apart in the documents list.
    :param word_list: Input document which includes a list of parsed words.
    :param max_sep: Specifies how far apart two words can be in the document to form a pair.
    :return: A list of distinct word pairs, the total number of word pairs and distinct word pairs.
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
    """
    compare_documents(file_1, f1_word_list, file_2, f2_word_list) reads in the file names on the input documents,
        and the parsed list of each input document. Then it Provides a summary comparison regarding the
        complexity and similarity of the input documents.

    :param file_1: The first input document.
    :param f1_word_list: List of parsed words for input document 1.
    :param file_2: The second input document.
    :param f2_word_list: List of parsed words for input document 2.
    :return:
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
    """
    get_words_for_each_length(word_set) reads in the input set of words. Returns a list where each element is a
        set of words corresponding to a specific length.
    :param word_set: Set of parsed words from input document.
    :return: A list of sets, where each set contains words of a particular length.
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