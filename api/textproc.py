########################################
## process texts in datasets
########################################
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

import re
def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)

def ReplaceThreeOrMore(s):
    # pattern to look for three or more repetitions of any character, including
    # newlines.
    pattern = re.compile(r"(.)\1{2,}", re.DOTALL) 
    return pattern.sub(r"\1", s)

def splitstring(s):
    # searching the number of characters to split on
    proposed_pattern = s[0]
    for i, c in enumerate(s[1:], 1):
        if c != " ":
            if proposed_pattern == s[i:(i+len(proposed_pattern))]:
                # found it
                break
            else:
                proposed_pattern += c
    else:
        exit(1)

    return proposed_pattern

def clean_numbers(x):

    x = re.sub('[0-9]{5,}', '#####', x)
    x = re.sub('[0-9]{4}', '####', x)
    x = re.sub('[0-9]{3}', '###', x)
    x = re.sub('[0-9]{2}', '##', x)
    return x
#Regex to remove all Non-Alpha Numeric and space
special_character_removal=re.compile(r'[^a-z\d ]',re.IGNORECASE)

#regex to replace all numerics
replace_numbers=re.compile(r'\d+',re.IGNORECASE)

def _get_mispell(mispell_dict):
    mispell_re = re.compile('(%s)' % '|'.join(mispell_dict.keys()))
    return mispell_dict, mispell_re


mispell_dict = {'colour':'color',
                'centre':'center',
                'didnt':'did not',
                'doesnt':'does not',
                'isnt':'is not',
                'shouldnt':'should not',
                'favourite':'favorite',
                'travelling':'traveling',
                'counselling':'counseling',
                'theatre':'theater',
                'cancelled':'canceled',
                'labour':'labor',
                'organisation':'organization',
                'wwii':'world war 2',
                'citicise':'criticize',
                'instagram': 'social medium',
                'whatsapp': 'social medium',
                'snapchat': 'social medium'

                }
mispellings, mispellings_re = _get_mispell(mispell_dict)

def replace_typical_misspell(text):
    def replace(match):
        return mispellings[match.group(0)]

    return mispellings_re.sub(replace, text)

def clean_text(x):

    x = str(x)
    for punct in "/-'":
        x = x.replace(punct, ' ')
    for punct in '&':
        x = x.replace(punct, f' {punct} ')
    for punct in '?!.,"#$%\'()*+-/:;<=>@[\\]^_`{|}~' + '“”’':
        x = x.replace(punct, '')
    return x

def text_to_wordlist(text,to_lower=False, rem_urls=False, rem_3plus=False,
                     clean_t=True, clean_num=True,mispelling=True,rem_specwords= False,
                     split_repeated=True, rem_special=False, rep_num=False, 
                     man_adj=True, rem_stopwords=False, stem_snowball=False,
                     stem_porter=False, lemmatize=False):

    # Clean the text, with the option to remove stopwords and to stem words.
    
    # Convert words to lower case and split them
    if rem_urls:
        text = remove_urls(text)
    if to_lower:    
        text = text.lower()
    if rem_3plus:    
        text = ReplaceThreeOrMore(text)
        
    if clean_t:
        text= clean_text(text)
        
    if clean_num:
        text= clean_numbers(text)    
        
    if mispelling:
        text= replace_typical_misspell(text)

    if man_adj: 
        # Clean the text
        text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
        text = re.sub(r"what's", "what is ", text)
        text = re.sub(r"\'s", " ", text)
        text = re.sub(r"\'ve", " have ", text)
        text = re.sub(r"can't", "cannot ", text)
        text = re.sub(r"n't", " not ", text)
        text = re.sub(r"i'm", "i am ", text)
        text = re.sub(r"\'re", " are ", text)
        text = re.sub(r"\'d", " would ", text)
        text = re.sub(r"\'ll", " will ", text)
        text = re.sub(r",", " ", text)
        text = re.sub(r"\.", " ", text)
        text = re.sub(r"!", " ! ", text)
        text = re.sub(r"\/", " ", text)
        text = re.sub(r"\^", " ^ ", text)
        text = re.sub(r"\+", " + ", text)
        text = re.sub(r"\-", " - ", text)
        text = re.sub(r"\=", " = ", text)
        text = re.sub(r"'", " ", text)
        text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
        text = re.sub(r":", " : ", text)
        text = re.sub(r" e g ", " eg ", text)
        text = re.sub(r" b g ", " bg ", text)
        text = re.sub(r" u s ", " american ", text)
        text = re.sub(r"\0s", "0", text)
        text = re.sub(r" 9 11 ", "911", text)
        text = re.sub(r"e - mail", "email", text)
        text = re.sub(r"j k", "jk", text)
        text = re.sub(r"\s{2,}", " ", text)

    # split them into a list
    text = text.split()
    
    if split_repeated:
        for i, c in enumerate(text):
            text[i]=splitstring(c)
    
    if rem_specwords:    
        to_remove = ['a','to','of','and']
        text = [w for w in text if not w in to_remove]
        
    # Optionally, remove stop words
    if rem_stopwords:
        stops = set(stopwords.words("english"))
        text = [w for w in text if not w in stops]
    
    text = " ".join(text)
    
    #Remove Special Characters
    if rem_special: 
        text=special_character_removal.sub('',text)
    
    #Replace Numbers
    if rep_num:     
        text=replace_numbers.sub('n',text)

    # Optionally, shorten words to their stems
    if stem_snowball:
        text = text.split()
        stemmer = SnowballStemmer('english')
        stemmed_words = [stemmer.stem(word) for word in text]
        text = " ".join(stemmed_words)
    
    if stem_porter:
        st = PorterStemmer()
        txt = " ".join([st.stem(w) for w in text.split()])
        
    if lemmatize:
        wordnet_lemmatizer = WordNetLemmatizer()
        txt = " ".join([wordnet_lemmatizer.lemmatize(w) for w in text.split()])   
 
    # Return a list of words
    return(text)