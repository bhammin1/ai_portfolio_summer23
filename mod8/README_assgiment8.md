# Assignment 4


# Performs K Mean Clustering
- This assignments performs the following pre-processing steps on categorical features
- Pre-processing from previous assignment
    - Converts Boolean to Binary
    - Removes Records with Missing Features
    - Combines Levels to Form Other Category
    - One Hot Encoding (note change from last assignment due to sklearn issues)
- Then performed K means cluster
    - 2 clusters
    - 5 clusters
    - 10 clusters
    
# Files
- categorical_pred.py
    - Performs all pre-processing in a single script

- k_means_bhammin1
    - Performs all pre-processing but in a notebook
    - Then computers the K means clusters
    - For each cluser
        - Two feature graphing is performed on a few different features
        - Metrics are calculated
            - Inertia 
                - Measures the distance from each data point to the clusters centroid. The lower the score the better
            - Silhouette_score
                - Is a balance of cohesiveness, how close/tight clusters are, and separateness, how spread apart are clusters from each other.
                - Score will be between -1 and 1. Values of 0 means overlapping clusters. -1 score means clusters have been assigned wrong label
            - Davies-Bouldin score
                - The average similarity measure of each cluster with the cluster most similar to it
                - Clusters that have more distance to each other and are less dispersed will result in the best score
                - The best score is 0. The lower the better the score
        - Analysis of the metrics is listed directly after metric calculation for each cluster
        - An elbow method is performed to find the optimal number of clusters
        - Overall insight about performance is mentioned
    
# Repos
- All files are in the repo under directory mod8
    - [mod8_git](https://github.com/bhammin1/ai_portfolio_summer23/tree/main/mod8)
