# Assignment 4


# Performs Transformations on Categorical Data
- This assignments performs the following pre-processing steps on categorical features
- Pre-processing
    - Converts Boolean to Binary
    - Removes Records with Missing Features
    - Combines Levels to Form Other Category
    - One Hot Encoding
  - Additional Feature
      - Splits data into feature numpy array and label (y) numpy array
      - This allows data to be ready to be feed into a NN (scikit-learn)
    
# Files
- categorical_data.py
    - performs all pre-processing in a single script
    - docker image runs this script
    - Ensure the data is the same directory as the python script when running
- bhammin1_Assignment4_notebook 
    - performs all pre-processing but in a notebook
    - all functions are the same that are in the python script
    
# Repos
- All files are in the repo under directory mod5
    - [mod5_git](https://github.com/bhammin1/ai_portfolio_summer23/tree/main/mod5)
- Docker link 
    - [mod5_docker](https://hub.docker.com/repository/docker/bhammin1/mod5/general)
    - Pull Image
        - `docker pull bhammin1/mod5:1.0`
    - To run, do the following command 
        - `docker run -it -v /output:/output bhammin1/mod5:1.0`