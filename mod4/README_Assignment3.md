# Assignment 3


# Performs NLP 
- This assignments performs the following pre-processing steps on a summary column
- The summary column should contain various sized strings with various words and punctuation
- Pre-processing
    - Tokenization
    - Stemming
    - Lemmatization
    - Part of Speech Tagging
    
# Files
- summary_transforms.py
    - performs all pre-processing in a single script
    - docker image runs this script
    - Ensure the data is the same directory as the python script when running
- bhammin1_Assignment3 notebook
    - performs all pre-processing but in a notebook
    - all functions are the same that are in the python script
    
# Repos
- All file except for the data are in the repo under directory mod4
    - [mod4_git](https://github.com/bhammin1/ai_portfolio_summer23/tree/main/mod4)
- Docker link 
    - [mod4_docker](https://hub.docker.com/repository/docker/bhammin1/mod4/general)
    - Pull Image
        - `docker pull bhammin1/mod4:1.0`
    - To run, do the following command 
        - `docker run -it -v /output:/output bhammin1/mod4:1.0`