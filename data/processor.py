from pathlib import Path
import pandas as pd
import json

class Values:
    TITLE: str = "Title"
    CATEGORY: str = "Category"
    SERVINGS: str = "Servings"
    INGREDIENTS: str = "Ingredients"
    DESCRIPTION: str = "Description"


def load_data():
    data: str = ""
    file: Path = Path(__file__).absolute().parent.joinpath("original/recipes.txt")
    print(data)
    with file.open("r") as f:
        data = f.read()

    return data


def to_tokens(recipes: [str]):
    recipe_tokens = []

    for recipe in recipes:
        recipe_list = recipe.split("\n")
        recipe_list = [item.strip() for item in recipe_list]
        start_index = 0

        for index, item in enumerate(recipe_list):
            if "Title" in item:
                start_index = index
        recipe_list = recipe_list[start_index:]

        new_item = {
            Values.TITLE: recipe_list[0].replace(Values.TITLE + ":", "").strip(),
            Values.CATEGORY: recipe_list[1].replace("Categories:", "").strip(),
            Values.SERVINGS: recipe_list[2].replace(Values.SERVINGS + ":", "").strip(),
            Values.INGREDIENTS: [],
            Values.DESCRIPTION: "",
        }

        recipe_list = recipe_list[4:]
        ingredients = []
        for index, item in enumerate(recipe_list):
            item = item.strip()

            if item == "":
                start_index = index + 1
                break
            else:
                ingredients.append(item)

        new_item[Values.INGREDIENTS] = ingredients

        recipe_list = recipe_list[start_index:]
        recipe_list = [item for item in recipe_list if item.find('---') <= -1]
        new_item[Values.DESCRIPTION] = " ".join(recipe_list).strip()

        recipe_tokens.append(new_item)

    return recipe_tokens


def to_csv(tokens):
    df: pd.DataFrame = pd.DataFrame.from_dict(tokens)

    df.to_csv(str(Path(__file__).absolute().parent.joinpath("processed/recipes.csv")))


def to_json(tokens):
    with Path(__file__).absolute().parent.joinpath("processed/recipes.json").open("w+") as f:
        json.dump(tokens, f)


if __name__ == '__main__':
    data = load_data()
    recipes = data.split("------------- Recipe Extracted from Meal-Master (tm) Database --------------")[1:]

    print(len(recipes))
    tokens = to_tokens(recipes)
    print(len(tokens))
    print(tokens[-1])
    to_csv(tokens)
    to_json(tokens)