import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction import text
punc = ['.', ',', '"', "'", '/','?', '$','!', ':', ';', '(', ')', '[', ']', '{', '}',"%", '1','2','3','4','5','6','7','8','9','10']
stop_words = text.ENGLISH_STOP_WORDS.union(punc)
from sklearn.feature_extraction.text import TfidfVectorizer

food52url=pd.DataFrame()
def food52_urls():
    """create urls for each page on food52"""
    all_recipe_page_urls=['https://food52.com/recipes']
    for i in range(2, 221):
        test_url='https://food52.com/recipes?page='
        all_recipe_page_urls.append(test_url + str(i))
    return all_recipe_page_urls
def create_links(photo_class):
    recipe_links=[]
    link_start= 'https://food52.com'
    for i in range (0, 24):
        recipe_links.append(link_start + photo_class[i]['href'])
    return recipe_links
links=[]
for i in range(0, 219):
    links.extend(create_links((make_soup(food52_page_urls[i])).find_all("a", class_='photo')))

df=pd.read_csv('food52urls.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)
url_lst=[i for i in df['url']]
def make_soup(url):
    """make soup from the urls"""
    soup = BeautifulSoup((requests.get(url).content), "lxml")
    return soup
def make_content_soup(soup):
    """find the recipe script from soup"""
    content=soup.find_all("script", type="application/ld+json")[0]
    return content
def clean_content(content):
    "clean up content from the recipe script into string format, and back to dict for identification"
    content_text=content.text
    if '\r' in content_text:
        clean_r=content_text.replace('\r', '')
        clean_n=clean_r.replace('\\n', '')
        clean_n_again=clean_n.replace('\n', '')
    else:
        clean_n=content.text.replace('\\n', '')
        clean_n_again= clean_n.replace('\n', '')
    return eval(clean_n_again)

def make_ingredients(cleaned_content):
    """take the ingredients section from content dictionary from list into string
       add '$' for identifier of separate each ingredients """
    items=''
    for item in cleaned_content['recipeIngredient']:
        items+=item +' $ '
    return items
def rating (cleaned_content):
    """find rating from recipe """
    return cleaned_content['aggregateRating']['ratingValue']
def rating_count(cleaned_content):
    """find rating count from recipe """
    return cleaned_content['aggregateRating']['ratingCount']
def find_rating_and_count(clean_content):
    """replace 0 rating to 0 instead of None """
    if 'aggregateRating' in clean_content:
        recipe_rating=rating (clean_content)
        recipe_rating_count=rating_count(clean_content)
    else:
        recipe_rating=0
        recipe_rating_count=0
    return recipe_rating, recipe_rating_count
def get_info(url):
    """combine functions to pull content for recipes """
    soup=make_soup(url)
    content=make_content_soup(soup)
    cleaned=clean_content(content)
    return cleaned
def details_lst(cleaned_content):
    """pull info into separate columns in dataframe """
    name=cleaned_content['name']
    catagory=cleaned_content['recipeCategory']
    keywords=cleaned_content['keywords']
    ingredients=make_ingredients(cleaned_content)
    cusine=cleaned_content['recipeCuisine']
    rating=find_rating_and_count(cleaned_content)[0]
    rating_count=find_rating_and_count(cleaned_content)[1]
    detail_lst=[name, catagory, keywords, ingredients,cusine,rating,rating_count]
    return detail_lst

def cuisine_label(dataframe):
    """map catagorical labels for generalized cuisine types as specified by the keys below
    #American=0, #Europe =1, #Asian=2, #Middle-eastern/african =3, #unknown=4, #s american =5"""
    dataframe['recipe_cuisine']=dataframe.recipe_cuisine.fillna('unknown')
    cuisine_mapping={'Indian': 2,
                 'American':0,
                 'Mexican':5,
                 'French':1,
                 'Italian':1,
                 'Spanish':1,
                 'Malaysian':2,
                 'Midwestern':0,
                 'Japanese':2,
                 'Korean':2,
                 'Cantonese':2,
                 'Caribbean':5,
                 'New England':0,
                 'Californian':0,
                 'Chinese':2,
                 'Asian':2,
                 'Cuban':5,
                 'African':3,
                 'Australian/New Zealander':0,
                 'Filipino':2,
                 'Scandinavian':1,
                 'Danish':1,
                 'unknown':4,
                 'Thai':2,
                 'Persian':3,
                 'Cajun/Creole':0,
                 'Finnish':1,
                 'Middle Eastern':3,
                 'Argentine':5,
                 'Jewish':3,
                 'Tuscan':1,
                 'Southern':0,
                 'Drinks':5,
                 'Swedish':1,
                 'Eastern European':1,
                 'European':1,
                 'Ashkenazi':3,
                 'Greek':1,
                 'Central Asian':2,
                 'Southern Italian':1,
                 'German':1,
                 'Bangladeshi':3,
                 'Southeast Asian':2,
                 'South American':5,
                 'Vietnamese':2,
                 'Turkish':3,
                 'Moroccan':3,
                 'Ethiopian':3,
                 'Canadian':0,
                 'Szechuan':2,
                 'Israeli':3,
                 'Tex-Mex':0,
                 'British':1,
                 'French Provençal':1,
                 'South Asian':2,
                 'Belgian':1,
                 'Irish':1,
                 'North African':3,
                 'Polish':1,
                 'Southwestern':0,
                 'Portuguese':1,
                 'Brazilian':5}
    dataframe['CuisineLabel']=dataframe['recipe_cuisine'].map(cuisine_mapping)

def text_process(recipes):
    """clean text for nlp"""
    nopunc=[word.lower() for word in food52 if word not in stop_words]
    nopunc=''.join(nopunc)
    return [word for word in nopunc.split()]

def clean_ingredients (recipes):
    recipes = word_tokenize(recipes)
    nopunc=[word.lower() for word in recipes if word not in stop_words]
    nopunc=' '.join(nopunc)
    return [word for word in nopunc.split()]

def clean_ingredients_df(df_ingredients):
    return df_ingredients=df_ingredients.apply(lambda x:clean_ingredients(df_ingredients))

def text_vectorizer(vectorizer, scaler_df):
    vectorizer= TfidfVectorizer(analyzer=text_process).fit(scaler_df)
    scaler_df=vectorizer.fit_trainsform(scaler_df)
    return scaler_df



#functions that turn each items in each of the recipe into one long list of string
def create_recipe_item(recipe):
    recipe_item=[]
    for i in recipe:
        recipe_item=recipe_item+(i.split(' '))
    return recipe_item
def create_recipe_item_lst(recipe_list):
    lst=[]
    for i in recipe_list:
        lst.append(str(create_recipe_item(i)))
    return lst
def cleaner_ingredients(ingredients):
    for i in  ingridents:
        i=str(i)
        cleaner_ingridents=[]
        for symbol in "][,.?!''$=-_:()<>%/\1234567890":
            cleaner=i.replace(symbol, '')
        cleaner_ingridents.append(cleaner)
    return cleaner_ingridents
