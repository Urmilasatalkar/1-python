# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:18:50 2023

@author: urmii
"""

#to get the phone number from text
import re
text1='''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''
pattern=r'\d\d\d\d\d\d\d\d\d\d'
matches=re.findall(pattern,text1)
print(matches)

#another method for getting mobile number
import re
text1='''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''
pattern=r'\d{10}'
matches=re.findall(pattern,text1)
print(matches)

#another method for getting another phone number
import re
text1='''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''
pattern=r"\(\d{3}\)-\d{3}-\d{4}"
matches=re.findall(pattern,text1)    #['(999)-333-7777']
print(matches)

#get both mobile number indian as well as US
import re
text1='''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''
pattern=r"\(\d{3}\)-\d{3}-\d{4}|\d{10}"  #[a|b]
matches=re.findall(pattern,text1)    #['(999)-333-7777']
print(matches)

#getting a strings except semicolon and hypen all letter will get print
text2='''A protracted; legal battle; over a 32-carat;
 Golconda diamond-'''
pattern='[^;-]'
match=re.findall(pattern,text2)
print(match)
match

#Note 1 – Summary of Significant Accounting Policies we want only this content
text3='''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
'''
pattern=r'Note \d - [^\n]+'
match=re.findall(pattern,text3)
print(match)
match

import re
#Note 1 – Summary of Significant Accounting Policies we want only this content
text3='''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
'''
pattern=r'Note \d - [^\n]*'
match=re.findall(pattern,text3)
print(match)
match


#Summary of Significant Accounting Policies we want only this content
#captured everything enclosed
text3='''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
'''
pattern=r'Note \d - ([^\n]+)'
match=re.findall(pattern,text3)
print(match)
match

#Different ways to print FY2020 Q1 and all..
#---------------------------------------------------------
text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
pattern=r'FY\d{4} Q\d'
match=re.findall(pattern,text4) #['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']
print(match)

#another way 
text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
pattern=r'FY\d{4} Q[1234]'
match=re.findall(pattern,text4) #['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']
print(match)

text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
pattern=r'FY\d{4} Q[1-4]'
match=re.findall(pattern,text4) #['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']
print(match)

#IGNORECASE it will ignore uppercase and lowercase characters
text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in Fy2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.'''
pattern=r'FY\d{4} Q[1-4]'
match=re.findall(pattern,text4,re.IGNORECASE) #['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']
print(match)

#by using or(|) operator 
text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.'''
pattern=r'FY\d{4} Q[1-4] |fy\d{4} Q[1-4] '
match=re.findall(pattern,text4) #['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']
print(match)

#we only want 2021 we dont want FY
text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.'''
pattern=r'FY(\d{4} Q[1-4])'
match=re.findall(pattern,text4) #['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']
print(match)

#we only want financial Dollars
text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.'''
pattern=r'\$[0-9\.]+'
match=re.findall(pattern,text4) #['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']
print(match)

#we dont want dollar
text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.'''
pattern=r'\$([0-9\.]+)'
match=re.findall(pattern,text4) #['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']
print(match)

#--------------------------------------------------------------------------------
import re
text1='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[2]
Parents	
Errol Musk
Maye Musk
Family	Musk family'''
def get_pattern_match(pattern,text1):
    match=re.findall(pattern,text1)
    if match:
        return match[0]
get_pattern_match('age (\d+)', text1)
get_pattern_match('Born(.*)\n', text1).strip()
get_pattern_match('name:(\D+)\n', text1)
get_pattern_match('Full name(.*)\n', text1)
get_pattern_match('Born.*\n(.*)', text1)
get_pattern_match('\(age.*\n(.*)', text1)


def extract_personal_info(text1):
    age=get_pattern_match('age (\d+)', text1)
    born=get_pattern_match('Born(.*)\n', text1).strip()
    name=get_pattern_match('name:(\D+)\n', text1)
    full_name=get_pattern_match('Full name(.*)\n', text1)
    BornYear=get_pattern_match('Born.*\n(.*)', text1)
    birthplace=get_pattern_match('\(age.*\n(.*)', text1)
    return{
        'age':int(age),
        'Born':born.strip(),
        'Name':name,
        'Full_Name':full_name,
        'BornYear':BornYear.strip(),
        'Birth_place':birthplace
        }
extract_personal_info(text1)

text2='''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''
def get_pattern_match(pattern,text2):
    match=re.findall(pattern,text2)
    if match:
        return match[0]
get_pattern_match('Born.*\n(.*) [\(age]', text2).strip()
get_pattern_match('(age \d+)', text2)
get_pattern_match('Occupation\(s\)(\D+)\n', text2).strip()
get_pattern_match('Relatives(.*)\(', text2).strip()
get_pattern_match('(Children.*)',text2).strip()
get_pattern_match('Born(.*)', text2).strip()


#---------------------------------------------
#tokenization
txt='Welcome to new year 2023'
x=txt.split()
print(x)

import re
def remove_special_characters(text):
    pat=r'[^a-zA-Z0-9!@#$%>]'
    return re.sub(pat,' ', text)
remove_special_characters('urmila 001 2222 Army @$ %,,,,,,,')

#remove numbers
import re
def remove_special_characters(text):
    pat=r'[^a-zA-Z!@#$%>]'
    return re.sub(pat,' ', text)
remove_special_characters('urmila 001 2222 Army @$ %,,,,,,,')
    
#remove text  
import re
def remove_special_characters(text):
    pat=r'[^!@#$%>]'
    return re.sub(pat,' ', text)
remove_special_characters('urmila 001 2222 Army @$ %,,,,,,,')   
    
#type pf tokenixzation
#1.unigram
#2.bigram
#3.trigram  
import string
def remove_puncuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text
remove_puncuation('Article: @first sentence of some important article having lot of ~ puncuation and another one;!')
    
#stemming
#stemming is the process of reducing inflected words to their word stem
#base or root form
import nltk
def get_stem(text):
    stemmer=nltk.porter.PorterStemmer()
    text=' '.join([stemmer.stem(word) for word in text.split()])
    return text
get_stem("We are eating and swimming we have been eating and swimming he eats and swims ; he ate and swam")
















