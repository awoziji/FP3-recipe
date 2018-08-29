import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

#__________________________________MET__________________________________________
#__________________________________MET__________________________________________
#__________________________________MET__________________________________________
#__________________________________MET_______________________________________end

#MET - requests object will not allow us to pull info from thier site
# _link = 'https://www.metmuseum.org/art/collection/search#!?showOnly=highlights&offset='
# link_ = '&pageSize=0&perPage=80&sortBy=relevance&sortOrder=asc&searchField=All'
# List_of_MET_Hilight_Links = []
#
# for increment in range(0, 200):
#     List_of_MET_Hilight_Links.append(_link + str(increment*80) + link_)
#
# response_page_MET = []
#
# for link in List_of_MET_Hilight_Links:
#     response = requests.get(link)
#     try:
#         response.raise_for_status()
#         response_page_MET.append(response)
#     except:
#         break
#
# a = response_page_MET[15].text

#_________________________________NEU___________________________________________
#_________________________________NEU___________________________________________
#_________________________________NEU___________________________________________
#_________________________________NEU________________________________________end

#NEU https://www.neuegalerie.org/artist-list/all
#
# response_page_NEU = 'https://www.neuegalerie.org/artist-list/all'
# BeautifulSoup_page_NEU = BeautifulSoup(requests.get(response_page_NEU).text, "lxml")
# BeautifulSoup_page_NEU_a = BeautifulSoup_page_NEU.find_all('a')
# BeautifulSoup_page_NEU_a_href = [element.find_all('href') for element in BeautifulSoup_page_NEU_a]

#_______________________________ARTRES__________________________________________
#_______________________________ARTRES__________________________________________
#_______________________________ARTRES__________________________________________
#_______________________________ARTRES_______________________________________end

# _link = 'http://www.artres.com/C.aspx?VP3=ViewBox&VBID=2UN365FDE6XWG&VBIDL=&SMLS=1&RW=1296&RH=648&PN='
# link_ = '&IT=ThumbImageTemplate01_VForm&CT=Search&SH=1&SF=1&PPM=0&CTID=KRHEC0AOQE3R'
#
# #Think about how to generalize to n pages -> where in html is the current and total page specified?
# link_page_ARTRES = [_link + str(page_num) + link_ for page_num in range(1,7)]
# response_page_ARTRES = [requests.get(link) for link in link_page_ARTRES]
# BeautifulSoup_page_ARTRES = [BeautifulSoup(response.text, 'lxml') for response in response_page_ARTRES]
#
# page_container = []
# #form of web_container -> web_container[web_page][piece][0]
# web_container = []
# #form of link_page_ARTRES_piece -> link_page_ARTRES_piece[link]
# link_page_ARTRES_piece = []
# response_page_ARTRES_piece = []
# for html_page in BeautifulSoup_page_ARTRES:
#     for piece in range(193, 263):
#         try:
#             print('a1.1.3.1.3.' + str(piece) + ':Image')
#             page_container.append(html_page.findAll(id = 'a1.1.3.1.3.' + str(piece) + ':Image'))
#         except:
#             break
#     web_container.append(page_container)
#     page_container = []
# for webpage in range(0, len(web_container)):
#     for piece in range(0, len(web_container[webpage])):
#         link_page_ARTRES_piece.append('http://www.artres.com/' + web_container[webpage][piece][0].a['href'])
# response_page_ARTRES_piece = [requests.get(link) for link in link_page_ARTRES_piece]
# BeautifulSoup_page_ARTRES_piece = [BeautifulSoup(response.text, 'lxml') for response in response_page_ARTRES_piece]

#_______________________________Meal_Master_____________________________________
#_______________________________Meal_Master_____________________________________
#_______________________________Meal_Master_____________________________________
#_______________________________Meal_Master__________________________________end

# link_page_Meal_Master = 'http://www.garvick.com/recipes-fps/'
# response_page_Meal_Master = requests.get(link_page_Meal_Master)
# BeautifulSoup_page_Meal_Master = BeautifulSoup(response_page_Meal_Master.text, 'lxml')
# BeautifulSoup_page_Meal_Master_a = BeautifulSoup_page_Meal_Master.find_all('a')
# BeautifulSoup_page_Meal_Master_link = ['http://www.garvick.com/recipes-fps/' + tag['href'] for tag in BeautifulSoup_page_Meal_Master_a]

#_______________________________Epicurious_____________________________________
#_______________________________Epicurious_____________________________________
#_______________________________Epicurious_____________________________________
#_______________________________Epicurious__________________________________end

if False:
    #!cuisine###https://www.epicurious.com/search?content=recipe
    #1cuisine###https://www.epicurious.com/search/?cuisine=french&content=recipe

    #forward and rear link
    _link = 'https://www.epicurious.com/search/'
    link_ = 'content=recipe'

    #list of possible cuisine filters on https://www.epicurious.com/search/ page
    EPI_cuisine = ['African','American','Asian','British','Cajun/Creole','Californian','Caribbean',
        'Central/S. American','Chinese','Cuban','Eastern European','English','European',
        'French','German','Greek','Indian','Irish','Italian','Italian American','Japanese',
        'Jewish','Korean','Latin American','Mediterranean','Mexican','Middle Eastern',
        'Moroccan','Nuevo Latino','Scandinavian','South American','South Asian','Southeast Asian',
        'Southern','Southwestern','Spanish/Portuguese','Tex-Mex','Thai','Turkish','Vietnamese']

    print('conversion of cuisine labels into requestable links. First N pages per category. Use first page to determine total number of pages per category.')
    #conversion of cuisine labels into requestable links. First on N pages per category. Use first page to determine total number of pages per category.
    link_page_EPI_cuisine = [(cuisine ,_link + '?cuisine=' + cuisine.lower().replace(' ', '-') + '&' + link_) for cuisine in EPI_cuisine]
    response_page_EPI_cuisine = [requests.get(link[1]) for link in link_page_EPI_cuisine]
    BeautifulSoup_page_EPI_cuisine = [BeautifulSoup(response.text, 'lxml') for response in response_page_EPI_cuisine]
    BeautifulSoup_page_EPI_cuisine_data_total_pages = []
    for Beautiful in BeautifulSoup_page_EPI_cuisine:
        try:
            BeautifulSoup_page_EPI_cuisine_data_total_pages.append(Beautiful.find_all('nav', class_ = 'common-pagination')[0]['data-total-pages'])
        except:
            BeautifulSoup_page_EPI_cuisine_data_total_pages.append('1')

    print('reconstruction of of cuisine labels with all page numbers assosiated to each category.')
    #reconstruction of of cuisine labels with all page numbers assosiated to each category.
    link_page_EPI_cuisine_with_page_number = []
    for link, page in list(zip(link_page_EPI_cuisine, BeautifulSoup_page_EPI_cuisine_data_total_pages)):
        for itt in range(1, int(page) + 1):
            print(link[0],link[1] + '&page=' + str(itt))
            link_page_EPI_cuisine_with_page_number.append((link[0],link[1] + '&page=' + str(itt)))
    response_page_EPI_cuisine = [(link[0],requests.get(link[1])) for link in link_page_EPI_cuisine_with_page_number]
    BeautifulSoup_page_EPI_cuisine = [(response[0], BeautifulSoup(response[1].text, 'lxml')) for response in response_page_EPI_cuisine]

    print('locating <a, class = "photo-link"> to extract recipe link. Construction of recipe link.')
    #locating <a, class = 'photo-link'> to extract recipe link. Construction of recipe link.
    BeautifulSoup_page_EPI_cuisine_a = [(Beautiful[0],Beautiful[1].find_all('a', class_ = 'photo-link')) for Beautiful in BeautifulSoup_page_EPI_cuisine]
    BeautifulSoup_page_EPI_cuisine_recipe_link = []
    for Beautiful in BeautifulSoup_page_EPI_cuisine_a:
        for tag in Beautiful[1]:
            print('https://www.epicurious.com' + tag['href'])
            BeautifulSoup_page_EPI_cuisine_recipe_link.append((Beautiful[0],'https://www.epicurious.com' + tag['href']))

    recipe_df = pd.DataFrame(data={'cuisine': BeautifulSoup_page_EPI_cuisine_recipe_link[0],'recipe_link':BeautifulSoup_page_EPI_cuisine_recipe_link[1]})
    recipe_df.to_csv("./recipe_cuisine.csv", sep=',',index=False)




#############GENERALIZE
#############GENERALIZE
#############GENERALIZE
#############GENERALIZE
recipe_cuisine = pd.read_csv('recipe_cuisine.csv')

response_page_EPI_recipe = [requests.get(recipe_cuisine['recipe_link'][_recipe_link]) for _recipe_link in range(0,len(recipe_cuisine))]
BeautifulSoup_page_EPI_recipe = [BeautifulSoup(response.text, 'lxml') for response in response_page_EPI_recipe]
for a in range(0, 17):
    a = a*1000
    print(a*1000, a*1000 + 1000)
    EPI_dictionary = {'name': [], 'ingredients': [], 'recipe_category': [], 'recipe_cuisine': [], 'rating': [], 'rating_count': [], 'keywords': []}
    for Beautiful in BeautifulSoup_page_EPI_recipe[a:a+1000]:
        print('(>..)>')
        EPI_dictionary['name'].append(Beautiful.find_all('h1', itemprop = 'name')[0].text)
        EPI_dictionary['rating'].append(Beautiful.find_all('span', class_ = 'rating')[0].text)
        EPI_dictionary['rating_count'].append(Beautiful.find_all('span', class_ = 'reviews-count')[0].text)
        ingredient_string = ''
        for ingredient in Beautiful.find_all('li', class_ = 'ingredient'):
            ingredient_string += ingredient.text + ' $ '
        EPI_dictionary['ingredients'].append(ingredient_string)
        recipe_category_string = ''
        for recipe_category in Beautiful.find_all('dt', itemprop = "recipeCategory"):
            recipe_category_string += recipe_category.text + ' $ '
        EPI_dictionary['recipe_category'].append(recipe_category_string)
        recipe_cuisine_string = ''
        for recipe_cuisine_ in Beautiful.find_all('dt', itemprop = "recipeCuisine"):
            recipe_cuisine_string += recipe_cuisine_.text + ' $ '
        EPI_dictionary['recipe_cuisine'].append(recipe_cuisine_string)
        EPI_dictionary['keywords'].append(recipe_category_string + recipe_cuisine_string)
        print('          o     ')
        print('            <(..<)')

    recipe_info = pd.DataFrame(EPI_dictionary)
    recipe_cuisine_recipe_info = pd.concat([recipe_cuisine, recipe_info])
    recipe_cuisine_recipe_info.to_csv("./recipe_cuisine_recipe_info"+ str(a) +".csv", sep=',',index=False)
#####Parsing recipe pages
#recipe_cuisine = pd.read_csv('recipe_cuisine.csv')
#a = requests.get(recipe_cuisine['recipe_link'][15000])
#b = BeautifulSoup(a.text, 'lxml')
#c = b.find_all('div', class_ = "recipe-content")
###Recipe
# ingredient_string = ''
# ingredients = b.find_all('li', class_ = 'ingredient')
# for ingredient in ingredients:
#     ingredient_string += ingredient.text + ' /n/ '
# ##Preperation
# preperation = b.find_all('li', class_ = 'preparation-step')
# ###Tags
# #<dt itemprop="recipeCategory">
# recipe_category = b.find_all('dt', itemprop = "recipeCategory")
# # <dt itemprop="recipeCuisine">
# recipe_cuisine = b.find_all('dt', itemprop = "recipeCuisine")
# #review
#
# #Name - how do I get content from h1-tag?
# name = b.find_all('h1', itemprop = 'name')[0].text
# #rating
# rating = b.find_all('span', class_ = 'rating')[0].text
# rating_count = b.find_all('span', class_ = 'reviews-count')[0].text
