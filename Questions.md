**23-813-0704: Computational Linguistics Lab**

**Lab Cycle 1 \- Regular Expressions**

**Date: 16/07/2026**

1. Write regular expressions for the following languages and implement them using Python library. By “word”, we mean an alphabetic string separated from other words by whitespace, any relevant punctuation, line breaks, and so forth.   
   1. The set of all strings with two consecutive repeated words (e.g., “Humbert Humbert” and “the the” but not “the bug” or “the big bug”);  
   2. all strings that start at the beginning of the line with an integer and that end at the end of the line with a word;  
   3. all strings that have both the word grotto and the word raven in them (but not, e.g., words like grottos that merely contain the word grotto);  
   4. Write a pattern that places the first word of an English sentence in a register. Deal with punctuation.

           The program reads input from a file and prints output to the terminal.

2. Implement an ELIZA-like program, using substitutions. Choose a domain in which your program can legitimately engage in simple conversations. The program should exit when the user types “BYE BYE”  
     
3. Implement a simple rule-based Text tokenizer for the English language using regular expressions. Your tokenizer should consider punctuation and special symbols as separate tokens. Contractions like "isn't" should be treated as 2 tokens: "is" and "n't". Also identify abbreviations (eg, U.S.A) and internal hyphenation (eg., ice-cream) as single tokens.  
     
4. Design and implement a Finite State Automata(FSA) that accepts English plural nouns ending with the character  ‘y’, e.g. boys, toys, ponies, skies, and puppies but not boies or toies or ponys. (Hint: Words that end with a vowel followed by ‘y’ are appended with ‘s' and will not be replaced with “ies” in their plural form).  
     
5. Design and implement a Finite State Transducer(FST) that accepts lexical forms of English words(e.g. shown below) and generates its corresponding plurals, based on the e-insertion spelling rule **є \=\> e / {x,s,z}^ \_\_ s\#**  
   ^ is the morpheme boundary and \# \- word boundary  
   

| Input | Output |
| :---: | :---: |
| fox^s\# 	 | foxes |
| boy^s\# | boys |

   

6. Implement a Byte Pair tokenizer for English using a small, representative corpus. Print each intermediate step in vocabulary creation. Discuss your choices and their impact.  
   **Lab Cycle 2**  
     
   **Date: 30/07/26**

7. Implement the *Minimum Edit Distance* algorithm to find the edit distance between any two given strings. Also, list the edit operations.  
8. Design and implement a statistical spell checker for detecting and correcting non-word spelling errors in English, using the bigram language model. Your program should do the following:  
   1. Tokenize the corpus and create a vocabulary of unique words.  
   2. Create a bi-gram frequency table for all possible bigrams in the corpus.  
   3. Scan the given input text to identify the non-word spelling errors  
   4. Generate the candidate list using 1 edit distance from the misspelled words   
   5. Suggest the best candidate word by calculating the probability of the given sentence using the bigram LM.  
9. Implement a text classifier for sentiment analysis using the Naive Bayes theorem. Use Add-k smoothing to handle zero probabilities. Compare the performance of your classifier for k values 0.25, 0.75, and 1\.  
     
   **Lab Cycle 3**  
     
   **Date: 13/8/26**  
     
     
10. Implement the Viterbi algorithm to find the most probable POS tag sequence for a given sentence, using the given probabilities:

          
                        

11. Write a Python code to calculate bigrams from a given corpus and calculate the probability of any given sentence  
12. Write a program to compute the TF-IDF matrix given a set of training documents. Also, calculate the cosine similarity between any two given documents or two given words.  
13. Write a program to compute the PPMI matrix given a set of training documents. Also, calculate the cosine similarity between any two given documents or two given words.  
14. Implement a Naive Bayes classifier with add-1 smoothing using the given test data and disambiguate any word in a given test sentence.  Use Bag-of-words as the feature. You may define your vocabulary.  
    **Sample Input :**  

| No. | Sentence | Sense |
| :---- | :---- | :---- |
| 1 | I love fish. The smoked bass fish was delicious. | fish |
| 2 | The bass fish swam along the line. | fish |
| 3 | He hauled in a big catch of smoked bass fish. | fish |
| 4 | The bass guitar player played a smooth jazz line. | guitar |

*Test Sentence:*  He loves jazz. The bass line provided the foundation for the guitar solo in the jazz piece  
*Test word*: bass  
**Output:** guitar

**Lab Cycle 4**

**Date: 27/8/26**