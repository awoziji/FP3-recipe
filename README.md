# Flatiron-Project-3: Recipe Cuisine Type / Rating Prediction with Recipes from food52.com and epicuirous.com

# Goal
Our overarching goal for this project is to make a statement on whether the names, ingredients/recipe and general keywords from popular American food websites can help us predict if the specific recipe belongs to a certain cuisine type (e.g. American, European, Asian, South-American, Middle-Easter/African, or Unknown), or rating (on a scale 0 to 4).

# Process: 
1. **_Web Scrapping_** we scrapped all the recipes from two popular recipe website (food52.com and epicurious.com), and extracted the name of the recipe, the ingredients, keywords, cuisine type and rating from each of the recipes.



2. **_Cleaning/vectorization_** removed none-alpha-numeric symbols and common stop-words from the text (recipe name, keyword, ingredients), and transformed our output into a vectorized format with Count Vectorization.

3. **_Machine Learning and Making Prediction_** using name and ingredients to predict cuisine type 

4. **_Name, keyword and recipe to predict cuisine type and rating (scale of 0-4)_**

5. **_Extensive grid search to fine-tune our model accuracy_**
we conducted an extensive grid search to find the best model and hyper-parameter, including Random Forest, K-Nearest Neighbor, Support Vector Classifier, XGBoost Classifier. Our output was a multi-class/multilayer output (meaning the output is a vector, so we are mapping vector to vector in our prediction), a challenging task considering that it's beyond the scope of my current knowledge.


# Conclusion:
Our model is able to make predictions about cuisine type and rating; however, understanding the limitations and the unique challenges of our dataset will help us navigate ways to find the best model, or the best vectorization method.

# Limitation:
* Working with mostly text dataset is a challenging experience in respect to its high dimensionality in the vectorized stage. This complexity limited our vectorization method to Count Vectorization that does not capture the inherent complexity of language and its dependence on context.
* Our dataset is only a subset of recipes from two American websites; therefore, our sample was biased. Even though we tried to ameliorate the problem of imbalanced sample group with Random Over Sampling, it was not sufficient to overcome the intrinsic limitation of our dataset.
# Next Step:
* A deeper further understanding of Neural Network, we might be able to explore different ways to account for the complexity of language and its reliance on context during the vectorization stage.
* with a larget dataset to work with, we might be able to ovcome some of the limitations we experice now with the project at its current stage.
