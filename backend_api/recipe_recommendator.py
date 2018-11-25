import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import requests
import ingredient_api as i_a                                    #Examples
e_d = {"mainCategory": ["3", "4", "5"],                         #mainCategory: Id drinks
                "subCategory": ["33", "132","114"],             #subCategory: Id cold drinks
                "specialDiet": ["1", "2"],                      #specialDiet: Id Lactosefree
                "maxTime": 120,                                 #preparation: int maxtime
                "minTime": 15}                                  #preparation: int mintime

body = dict(filters=dict(mainCategory=e_d["mainCategory"], subCategory=e_d["subCategory"], preparationTime=dict(maxTime=e_d["maxTime"], minTime=e_d["minTime"])))

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9a94c5afb6a34bed810db27ae4f1fbd8',
}

def recipe_recommendator(restrictions):
    """returns list of lists containing the urls to the recipes and ingredientTypes (and their amounts next to them
        if amounts are provided. EXAMPLE = [["www.recipe.com", "13205", ("240 g"), "4566", "1234"],[....]]
        :param restrictions: dictionary containing food restrictions/preferences/maxTime and minTime
        :return: list of lists"""
        
    #Idea was to call this function with !!!!restrictions object that was made with machine learning to try and guess
    #what recipes the user might like!!!!!
    
    """Oh this also makes files for Tom"""
    body = dict(filters=dict(mainCategory=restrictions["mainCategory"], subCategory=restrictions["subCategory"], specialDiet=restrictions["specialDiet"], preparationTime=dict(maxTime=restrictions["maxTime"], minTime=restrictions["minTime"])))
    r = requests.post("https://kesko.azure-api.net/v1/search/recipes", headers=headers, json=body)
    temp = r.json()
    recipes = temp["results"]
    r_url_ingredients = []
    i = 1

    for key in recipes:
        with open("recipeName{}.txt".format(i), "w") as name_file, open("shoppingList{}.json".format(i), "w") as shopping_list:
            with open("recipeImage{}.txt".format(i), "w") as file, open("nutrients{}.json".format(i), "w") as nutrientsfile:
                temporary = []                  #Used to make files for Tom, list of IngredientTypes example: "7012"
                temp2 = []                      #list for URLs, ingredientTypes and amounts
                temp2.append(key['Url'])

                try:
                    #Writes Picture Urls in a text file
                    file.write(key['PictureUrls'][0]['Normal'])
                    name_file = open("recipeName{}.txt".format(i), "w")

                    #creates txt file with only RecipeName inside. Filenames are going to be recipeName_1 recipeName_2
                    name_file.write(key["Name"])

                    subSectionIngredients = key['Ingredients'][0]['SubSectionIngredients']
                    item_names = []
                    #creates shoppingList file containing only productnames
                    for y in subSectionIngredients:
                        item_names.append(y[0]["Name"])
                    item_names = json.dumps(item_names)
                    shopping_list.write(item_names)


                except (KeyError, IndexError):
                    pass
                ingredient_list = key['Ingredients'][0]['SubSectionIngredients']
                for x in ingredient_list:
                    try:

                        temporary.append(x[0]['IngredientType'])
                        temp2.append(x[0]['IngredientType'])
                        temp2.append(x[0]['AmountInfo'])
                    except (KeyError, IndexError):
                        pass

                nutritionvalues = i_a.recipes_nutrition_values(temporary)   #Gets Nutrition attributes as a Dictionary
                nutritionsjson = json.dumps(nutritionvalues)
                nutrientsfile.write(nutritionsjson)         #writing json file for uncle Tom

                nutrientsfile.close()
                file.close()
                shopping_list.close()
                name_file.close()
                i += 1
                r_url_ingredients.append(temp2)
    return r_url_ingredients

if __name__=="__main__":
    x = recipe_recommendator(e_d)
    for item in x:
        print(item)
        print(" ")
