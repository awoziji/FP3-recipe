# Flatiron-Project-3: Recipe Cuisine Type / Rating Prediction with Recipes from food52.com and epicuirous.com

# Goal
Our overarching goal for this project is to make a statement on whether the names, ingredients/recipe and general keywords from popular American food websites can help us predict if the specific recipe belongs to a certain cuisine type (e.g. American, European, Asian, South-American, Middle-Easter/African, or Unknown), or rating (on a scale 0 to 4).

# ETL 
**_Web Scrapping_** we scrapped all available recipes from two popular recipe website (food52.com and epicurious.com) and extracted the name of the recipe, the ingredients, keywords, cuisine type and rating from each of the recipes.

**_Cleaning/vectorization_** removed none-alpha-numeric symbols and common stop-words from the text (recipe name, keyword, ingredients), and transformed our output into a vectorized format with Count Vectorization.
<p align="center">
  <img src="project3_visuals/Screen Shot 2018-10-12 at 2.42.02 PM.png" title="recipe corpus for each of the cuisine types">
</p>
The graph shows a clear class imbalance as most of the cusines are American / Unknown, therefore, we should take measure to oversample our minority class. 
<p align="center">
  <img src="project3_visuals/similarityingredients.png" title="compare cosine similarity of the cuisine corpus">
</p>
The heat map showed that most of the corpora in each of our cuisine types are distinctive from each other. The corpus similarity is calculated with TFIDF vectorization and the similarity score is calculated from Cosine Similarity. 

# Extensive grid search to fine-tune our model accuracy
we conducted an extensive grid search to find the best model and hyper-parameter, including Random Forest, K-Nearest Neighbor, Support Vector Classifier, XGBoost Classifier. Our output was a multi-class/multilayer output (meaning the output is a vector, so we are mapping vector to vector in our prediction), a challenging task considering that it's beyond the scope of my current knowledge.
<p align="left">
  <img src="project3_visuals/Screen Shot 2018-10-12 at 2.43.11 PM.png" title="snapshot gridsearch ">
</p>

# Prediction Model 1: Using name and ingredients to predict cuisine type 
Category keys: American=0, Europe =1, Asian=2, Middle-eastern/african =3, unknown=4, south american =5
### BaggingClassifier(DecisionTreeClassifier(criterion='gini', max_depth=100), n_estimators=150)
<p align="left">
  <img src="project3_visuals/Screen Shot 2018-10-12 at 2.42.51 PM.png" title="confusion matrix ">
</p>

Our model predicted that most recipes belong in the 'Unknown' category as that is our dominate class. 

# Prediction Model 2: Using Name, keyword and recipe to predict rating 
Rating Scale: 0-4 
### RandomForestClassifier(n_estimators=100, max_depth= 100)
<p align="left">
  <img src="project3_visuals/Screen Shot 2018-10-12 at 2.43.59 PM.png" title="confusion matrix">
</p>
Our model is has a high true positive at predicting a recipe with 0 in which it actually has a 0 rating, however, it has a high predicting that a recipe will have a 0 rating even when its rating is 3. 

# Model Performance Demonstration 
### Example 1: Predict recipe cuisine type
recipe link: https://www.allrecipes.com/recipe/13443/harira/

Predicted cuisine type: African  / Actual cuisine type: Middle Eastern / African

Input and prediction snapshot: 
<p align="left">
  <img src="project3_visuals/Screen Shot 2018-10-12 at 2.43.29 PM.png" title="cusine type prediction demo 1">
</p>

### Example 2: Predict recipe rating

recipe link: http://allrecipes.asia/recipe/4911/saag-masoor-dal--indian-dhal-with-spinach-.aspx

Predicted rating: 4 / Actual rating: 4

Input and prediction snapshot: 
<p align="left">
  <img src="project3_visuals/Screen Shot 2018-10-12 at 2.44.25 PM.png" title="cusine type prediction demo 1">
</p>

# Conclusion:
Our model is able to make predictions about cuisine type and rating; however, understanding the limitations and the unique challenges of our dataset will help us navigate ways to find the best model or the best vectorization method.

# Limitation:
* Working with mostly text dataset is a challenging experience in respect to its high dimensionality in the vectorized stage. This complexity limited our vectorization method to Count Vectorization that does not capture the inherent complexity of language and its dependence on context.
* Our dataset is only a subset of recipes from two American websites; therefore, our sample was biased. Even though we tried to ameliorate the problem of imbalanced sample group with Random Over Sampling, it was not sufficient to overcome the intrinsic limitation of our dataset.
# Next Step:
* A deeper further understanding of Neural Network, we might be able to explore different ways to account for the complexity of language and its reliance on context during the vectorization stage.
* with a larget dataset to work with, we might be able to overcome some of the limitations we experience now with the project at its current stage.
