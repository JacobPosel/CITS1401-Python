#Jacob Posel, 27/5/2018
#Project2FINAL.py

import sys
import math
def open_file(filename): #opens files
    import os
    if os.path.isfile(filename) == True:
        infile = open(filename, 'r').read()
        return infile
        
    else:
        sys.exit('The file does not exist, start again')
        
def divide_common(commonwords): #splits common words file and standardises them into lower case
    commonwords = commonwords.lower()
    commonwords = commonwords.split()
    return(list(commonwords))

def divide_sentences(textFile): #standardises sentences in the text by removing punctuation and splits sentences into lists
    sentencelist = []
    textFile = textFile.lower()
    for c in '"#$%&()*+,-/:;<=>@[\\]^_`{|}~':
        textFile = textFile.replace(c, ' ')
    for punctuation in '!?':
        textFile = textFile.replace(punctuation, '.')
    for lines in '\n':
        textFile = textFile.replace(lines, ' ')
    textFiles = textFile.split('.')
    for i in range(len(textFiles)):
        sentences = textFiles[i].split()
        sentencelist.append(sentences)
    return(sentencelist)
    
def remove_commonwords(sentencelist, splitCommonwords): #removes common words from sentence lists
    newsentencelist = []
    for sentences in sentencelist:
        for words in sentences:
            for words in splitCommonwords:
                while True:
                    try:
                        sentences.remove(words)
                    except ValueError:
                        break
        newsentencelist.append(sentences)
    while [] in newsentencelist:
        newsentencelist.remove([])
    return(newsentencelist)

def concept_word_profile(conword, newsentencelist): #creates profile dictionary for a given word
    conwordprofdic = {}
    for sentence in newsentencelist:
        if conword in sentence:
            for i in sentence:
                if i != conword:
                    conwordprofdic[i] = conwordprofdic.get(i, 0) + 1
    return(conwordprofdic)


def big_dic_concept(profileDicConcept, conword): #creates nested dictionary with profile dictionary as a value and concept word as a key
    bigDicConcept = {}
    bigDicConcept[conword] = profileDicConcept
    return(bigDicConcept)
    
    
def profile_dic_query(word, newsentencelist): #does same as above for query profile dictionary
    profileDicQuery = {}
    for sentence in newsentencelist:
        if word in sentence:
            for i in sentence:
                if i != word:
                    profileDicQuery[i] = profileDicQuery.get(i, 0) + 1
    return(profileDicQuery)


def big_dic_query(profileDicQuery, word): #does same as above but for nested query profile dictionary
    bigDicQuery = {}
    bigDicQuery[word] = profileDicQuery
    return(bigDicQuery)


def compare_profiles(queryProfile, conceptProfile, word, conword): #compares profiles of query and concept word and calculates consine metric
    numerator = 0
    den1 = 0
    den2 = 0
    denominator = 0
    for values in queryProfile[word]:
        if values in conceptProfile[conword]:
            score = queryProfile[word][values]*conceptProfile[conword][values]
            numerator = numerator + score
    for values in queryProfile[word]:
        den1 = den1 + queryProfile[word][values]**2
    for values1 in conceptProfile[conword]:
        den2 = den2 + conceptProfile[conword][values1]**2
    denominator = den1*den2
    if numerator == 0:
        metric = 0.00
    else:
        metric = numerator/math.sqrt(denominator)
    return(metric)
       
            
def metric_list(metricList1 ,metric, word): #appends metric scores of numerous query words into a list
    metricList0 = []
    metricList0.append(word)
    metricList0.append(metric)
    metricList1.append(metricList0)
    return(metricList1)


def sort_list(metricList1):
    return(metricList1[1])

def print_list(metricList1): #sorts the list into descending order and prints varying values depending on metric value of the top word
    metricList1.sort(key = sort_list, reverse = True)
    length = len(metricList1)
    
    if metricList1 == []:
        sys.exit('no query word has been entered, please start again')
    
    if metricList1[0][1] == 1.0: #if a query word is the same as the concept word
        for i in range(0,length):
            t = (metricList1[0+i])[1]
            t = "{0:.3f}".format(t)
            print((metricList1[0+i])[0],t)
        print(metricList1[0][0], "is the same as the concept word")
        
        for i in range(1, length):
            if metricList1[i][1] > 0 and metricList1[i][0] != metricList1[0][0]:
                print( metricList1[i][0], "is the closest synonym")
                break
            elif metricList1[i][0] != metricList1[0][0]:
                print("there are no other synonyms")
                break
            
        
    elif metricList1[0][1] == 0.000: #if none of the query words have a metric score
        for i in range(0,length):
            t = (metricList1[0+i])[1]
            t = "{0:.3f}".format(t)
            print((metricList1[0+i])[0],t)
        print("There are no synonyms")

    else: #normal conditions
        for i in range(0,length):
            t = (metricList1[0+i])[1]
            t = "{0:.3f}".format(t)
            print((metricList1[0+i])[0],t)
        print((metricList1[0][0]), "is a synonym")
    
        for i in range(1, length): #if two words have the same score
            if metricList1[0][1] == metricList1[i][1] and metricList1[0][0] != metricList1[i][0]:
                print(metricList1[i][0], "is also a synonym")
        
            


def main(corpus_file, commonwords_file_name = None):
    if commonwords_file_name != None: #main if there is a common word file
        textFile = open_file(corpus_file)
        commonwords = open_file(commonwords_file_name)
        splitCommonwords = divide_common(commonwords)
        sentencelist = divide_sentences(textFile)
        newsentencelist = remove_commonwords(sentencelist, splitCommonwords)
 
        conword = True
        while conword != "":
            conword = input("Enter the concept word (<Enter> to quit): ")
            conword = conword.lower()
            conword = conword.strip()
            if conword == '':
                break
            profileDicConcept = concept_word_profile(conword, newsentencelist)
            bigDicConcept = big_dic_concept(profileDicConcept, conword)
 

            metricList1 = []
            word = True
            while word != "":
                word = input("Enter a query word (<Enter> to quit) >> ")
                word = word.lower()
                word = word.strip()
                if word == '':
                    break
                profileDicConcept = concept_word_profile(conword, newsentencelist)
                bigDicConcept = big_dic_concept(profileDicConcept, conword)
                profileDicQuery = profile_dic_query(word, newsentencelist)
                bigDicQuery = big_dic_query(profileDicQuery, word)
                queryProfile = big_dic_query(profileDicQuery, word)
                conceptProfile = big_dic_concept(profileDicConcept, conword)
                metric = compare_profiles(queryProfile, conceptProfile, word, conword)
                metricList1 = metric_list(metricList1, metric, word)
            print_list(metricList1)
    else: #main if there is no common word
        textFile = open_file(corpus_file)
        sentencelist = divide_sentences(textFile)
 
        conword = True
        while conword != "":
            conword = input("Enter the concept word (<Enter> to quit): ")
            conword = conword.lower()
            conword = conword.strip()
            if conword == '':
                break
            profileDicConcept = concept_word_profile(conword, sentencelist)
            bigDicConcept = big_dic_concept(profileDicConcept, conword)
 

            metricList1 = []
            word = True
            while word != "":
                word = input("Enter a query word (<Enter> to quit) >> ")
                word = word.lower()
                word = word.strip()
                if word == '':
                    break
                profileDicConcept = concept_word_profile(conword, sentencelist)
                bigDicConcept = big_dic_concept(profileDicConcept, conword)
                profileDicQuery = profile_dic_query(word, sentencelist)
                bigDicQuery = big_dic_query(profileDicQuery, word)
                queryProfile = big_dic_query(profileDicQuery, word)
                conceptProfile = big_dic_concept(profileDicConcept, conword)
                metric = compare_profiles(queryProfile, conceptProfile, word, conword)
                metricList1 = metric_list(metricList1, metric, word)
                print_list(metricList1)
            


