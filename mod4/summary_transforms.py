import pandas as pd
import nltk

def load_data(path):
    '''
    Given a path (str) to a csv returns a pandas dataframe
    '''
    df = pd.read_csv(path)
    return df

def token(colName,df):
    '''
    Given a column name (string) and pandas data frame
    Returns a series with the column tokenized
    '''
    nltk.download('punkt')
    col = df[colName] # returns a series
    col_token = col.apply(nltk.word_tokenize)
    return col_token

def stemming_col(token_col):
    '''
    Given a tokenized series, returns a series that is stemmed
    '''
    stemmer = nltk.stem.snowball.SnowballStemmer("english")
    stem_list = []
    
    # stem each token/word
    for token in token_col:
        row = []
        for t in token:
            row.append(stemmer.stem(t))
        stem_list.append(row)
    col_stem = pd.Series(stem_list)
    return col_stem

def lemmatize_col(token_col):
    '''
    Given a tokenized series, returns a series
    with lemmatization performed
    '''
    nltk.download('wordnet')
    lem = nltk.stem.WordNetLemmatizer()
    lem_list =[]
    # lemmatize each token/word
    for token in token_col:
        row = []
        for t in token:
            row.append(lem.lemmatize(t))
        lem_list.append(row)
    col_lem = pd.Series(lem_list)
    return col_lem

def pst(token_col):
    '''
    Given a tokenized series,
    returns a series with part of speech tagging
    '''
    nltk.download('averaged_perceptron_tagger')
    pst_list =[]
    # pst each token/word
    for token in token_col:
        row = []
        pst_list.append(nltk.pos_tag(token))
    col_pst = pd.Series(pst_list)
    return col_pst

def add_cols(df, cols, names):
    '''
    Given a pandas data frame (df), list of series (cols)
    and a list of column names (names)
    Updates the data frame to have all the new columns from the series
    '''
    for i in range(len(cols)):
        df[names[i]] = cols[i]

if __name__ == "__main__":
    
    # get the data
    df = load_data("./Musical_instruments_reviews.csv")
    print("Initial load of the data frame\n", df.head())
    print("\n")
    
    print("The summary column\n", df["summary"].head(10))
    print("\n")
    
    # tokenize
    summary_token = token("summary",df) # tokenize the column
    print("Summary data tokenized\n", summary_token.head(10))
    print("\n")
    
    # stemming
    summary_stem = stemming_col(summary_token)
    print("Stemming the summary column\n", summary_stem.head(10))
    print("\n")
    
    # lemmatization
    summary_lem = lemmatize_col(summary_token)
    print("Lemmization of summary column\n", summary_lem.head(10))
    print("\n")
    
    # part of speech tagging
    summary_pst = pst(summary_token)
    print("Part of speech tagging of summary column\n", summary_pst.head(5))
    print("\n")
    
    # combining all data into df
    series = [summary_token, summary_stem, summary_lem, summary_pst]
    names = ["summary_tokens", "summary_stemming", "summary_lemmatization", "summary_pst"]
    add_cols(df, series, names)
    print("Data frame with all new columns\n", df.head())
   
    
    