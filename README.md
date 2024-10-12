DocumentAnalysis Project
- A python program which implements simplified versions of much more
sophisticated methods that are used in practice in NLP field.

--

How to run the program:
- Provide the following inputs when prompted:

Enter the first file to analyze and compare  ==> testDocuments/doc1.txt

Enter the second file to analyze and compare ==> testDocuments/doc2.txt

Enter the maximum separation between words in a pair ==> 2

- You are free to change the input documents and max separation value.

To solve this problem, the program will need the following:

[1] stop.txt
- This file contains what we will refer to as "stop words" - words that should
be ignored.

[2] Input Documents:
- Request the names of two documents to analyze and compare,
- An integer "maximum separation parameter" (Read more about this below)

--

With the provided inputs, here is how we solve the problem:

Parsing:
- Break a file of text into a single list of consecutive words.
To do this, the contents from a file should be first split up into
a list of strings, where each string contains consecutive non-white-space
characters. Then each string should have all non-letters removed
and all letters converted to lowercase.

- Once this parsing is done, the list resulting from parsing the file stop.txt
is converted to a set. This set contains what are referred to in NLP as
"stop words" - words that appear so frequently in text that they should be ignored.

We then want to parse through the input documents to remove any "stop words"
that may exist.

--

Analyze Each Document's Word List:

The following methods will be used analyze the word list.

[1] Calculate and output the average word length, accurate to
two decimal places. The idea here is that word length is a
rough indicator of sophistication.

[2] Calculate and output, accurate to three decimal places,
the ratio between the number of distinct words and the total number of words.
This is a measure of the variety of language used.

[3] For each word length starting at 1, find the set of words having
that length. Print the length, the number of words having that length,
and at most six of these words. If for a certain length, there are
six or fewer words, then print all six, but if there are more than six
print the first three, and the last three in alphabetical order.

[4] Find the distinct pairs in each document.
A word pair is a two-tuple of words that appear map_sep or fewer positions
apart in the document list. The program will then output the total number
of distinct word pairs. It will also output the first 5 word pairs in
alphabetical order and the last 5 word pairs in alphabetical order.

[5] As a measure of how distinct the word pairs are, calculate and output,
accurate to three decimal places, the ratio of the number of distinct word pairs
to the total number of word pairs.

--

Compare Documents:

The goal here is to compare the documents for complexity and similarity.

[1] Determine which document has a greater average word length.
This is a rough measure of which uses more sophisticated language.

[2] Calculate the Jaccard similarity in the overall word use in the two documents.
This is accurate to 3 decimal places.

[3] Calculate the Jaccard similarity of word use for each word length.
Each output is also accurate to three decimal places.

[4] Calculate the Jaccard similarity between the word pair sets.
The output is accurate to four decimal places.