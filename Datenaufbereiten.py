import json

badchars = set("(),-*\"'<>|:")

with open('full_format_recipes.json') as json_file:  
	data = json.load(json_file)
	outFile = "./preProcessedData.txt"
	with open (outFile, "w") as f:
		for recipe in data:
			try:
				ingredients = recipe['ingredients']
				for ingredient in ingredients:
					for c in badchars:
						ingredient = ingredient.replace(c,' ')
					try:
						f.write(ingredient+" ")
					except UnicodeEncodeError:
						print("UnicodeEncodeError")
				f.write("\n")
			except KeyError:
				print("KeyError")