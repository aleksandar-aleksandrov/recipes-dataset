from pathlib import Path
from typing import List, Any, Dict

import pandas as pd
import json


class RecipeKeyValues:
    TITLE: str = "Title"
    CATEGORIES: str = "Categories"
    SERVINGS: str = "Servings"
    INGREDIENTS: str = "Ingredients"
    DESCRIPTION: str = "Description"


def load_data() -> str:
    data: str = ""
    file: Path = Path(__file__).absolute().parent.joinpath("original/recipes.txt")
    with file.open("r") as f:
        data = f.read()

    return data


def to_tokens(recipes: List[str]) -> List[Dict[str, Any]]:
    recipe_tokens: List[Dict[str, Any]] = []

    for recipe in recipes:
        recipe_list = [item.strip() for item in recipe.split("\n")]
        start_index = 0

        for index, item in enumerate(recipe_list):
            if "Title" in item:
                start_index = index
        recipe_list = recipe_list[start_index:]

        new_item: Dict[str, Any] = {
            RecipeKeyValues.TITLE: recipe_list[0].replace(RecipeKeyValues.TITLE + ":", "").strip(),
            RecipeKeyValues.CATEGORIES: recipe_list[1].replace(RecipeKeyValues.CATEGORIES + ":", "").strip(),
            RecipeKeyValues.SERVINGS: recipe_list[2].replace(RecipeKeyValues.SERVINGS + ":", "").strip(),
            RecipeKeyValues.INGREDIENTS: "",
            RecipeKeyValues.DESCRIPTION: "",
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

        new_item[RecipeKeyValues.INGREDIENTS] = " ".join(ingredients)

        recipe_list = recipe_list[start_index:]
        recipe_list = [item for item in recipe_list if item.find('---') <= -1]
        new_item[RecipeKeyValues.DESCRIPTION] = " ".join(recipe_list).strip()

        recipe_tokens.append(new_item)

    return recipe_tokens


def to_csv(tokens: List[Dict[str, Any]]) -> None:
    df: pd.DataFrame = pd.DataFrame.from_dict(tokens)

    df.to_csv(str(Path(__file__).absolute().parent.joinpath("processed/recipes.csv")))


def to_json(tokens: List[Dict[str, Any]]) -> None:
    with Path(__file__).absolute().parent.joinpath("processed/recipes.json").open("w+") as f:
        json.dump(tokens, f)


def to_docs(tokens: List[Dict[str, Any]]) -> None:
    path: Path = Path(__file__).absolute().parent.joinpath("processed/docs")
    path.mkdir(exist_ok=True)

    for index, token in enumerate(tokens):
        new_path = path.joinpath(f"doc{index}")
        new_path.mkdir(exist_ok=True)
        with new_path.joinpath(f"doc{index}.txt").open("w+") as f:
            f.write(token[RecipeKeyValues.INGREDIENTS])


if __name__ == '__main__':
    data: str = load_data()
    recipes: List[str] = data.split("------------- Recipe Extracted from Meal-Master (tm) Database --------------")[1:]

    print(f'Found {len(recipes)} recipes in the dataset!')

    print(f'Extracting the recipe objects...')
    tokens = to_tokens(recipes)

    print(f'Saving the recipes in CSV format...')
    to_csv(tokens)

    print(f'Saving the recipes in JSON format...')
    to_json(tokens)

    print(f'Saving the ingredients in separate documents...')
    to_docs(tokens)

    print(f'The results can be found in the data/processed folder!')
