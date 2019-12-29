# 1K Recipe Dataset

![](assets/photo.jpg)
Photo by [Louis Hansel](https://unsplash.com/@louishansel) on [Unsplash](https://images.unsplash.com/photo-1555243896-c709bfa0b564?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80)


## What is the dataset about?
1K Recipe dataset is a list of 1024 recipes. Each recipe consists of a title, categories, servings, ingredients & description.

## How is the dataset structured?
In the `data/original` folder one can find the original unstructured and unprocessed data. The recipes are to be found in a single `recipes.txt` file. All of the recipes are described in the same format, which makes their further processing easier.

## How can one load the dataset?
In the `data/processed` folder one can find all of the listed recipes in both JSON & CSV format, which can easily be loaded with most programming languages. In addition to that, there is a `docs` in which the ingredients of each of the recipes can be found in separate files.

## How can one extend the dataset?
One could easily add new recipes in the defined format to the `recipes.txt` file. After one, the `processor.py` script should be executed to automatically update the other versions of the dataset.

## Where does the dataset come from?
I have collected the recipes from http://www.ffts.com/recipes.htm. The recipes are collected from the following sub-collections: [German 1](http://www.ffts.com/recipes/mmgermn1.zip), [German 2](http://www.ffts.com/recipes/mmgermn2.zip), [Greek](http://www.ffts.com/recipes/mm_greek.zip), [English](http://www.ffts.com/recipes/english.zip), [Mexican](http://www.ffts.com/recipes/mexican.zip), [Soup2](http://www.ffts.com/recipes/mmsoup2.zip), [Microwave 1](http://www.ffts.com/recipes/mmmicwv1.zip), [Microwave 2](http://www.ffts.com/recipes/mmmicwv1.zip), [mm0222-1](http://www.ffts.com/recipes/mm0222-1.zip), [mm0222-2](http://www.ffts.com/recipes/mm0222-2.zip), [Pasta](http://www.ffts.com/recipes/mmpasta.zip), [Spaghetti](http://www.ffts.com/recipes/mmpasta.zip). The format of the original `recipes.txt` file is the `MealMaster` format. All credit goes to the contributors as outlined on the ffts page. 
