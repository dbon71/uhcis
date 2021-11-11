#David Bonilla
#CIS2348 Ratner
#PSID:1913106

#class for food items and definitions
class FoodItem:

	#constructor with default parameters of food item
	def __init__(self, name=None , fat=0, carbs=0, protein=0, servings=1):
		# Initializing attributes
		self.name = name
		self.fat = fat
		self.carbs = carbs
		self.protein = protein
		self.servings = servings

	#defintion to calculate calories per serving
	def get_calories(self, num_servings):
		# Calorie formula
		calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4))* num_servings;
		return calories

  #definiton to print info of each food items
	def print_info(self):
		print('Nutritional information per serving of {}:'.format(self.name))
		print('   Fat: {:.2f} g'.format(self.fat))
		print('   Carbohydrates: {:.2f} g'.format(self.carbs))
		print('   Protein: {:.2f} g'.format(self.protein))

#calling the definition
if __name__ == "__main__":

  #assigning the food attributes for item 1
	food1 = FoodItem()

	itemName = input()
	amountFat = float(input())
	amountCarbs = float(input())
	amountProtein = float(input())

  #assigning the food attributes for item 2
	food2 = FoodItem(itemName, amountFat, amountCarbs, amountProtein)

	numServings = float(input())

    #printing informtion for food 1
	food1.print_info()
	print('Number of calories for {:.2f} serving(s): {:.2f}'.format(numServings,
	food1.get_calories(numServings)))

	print()

    #printing informtion for food 2
	food2.print_info()
	print('Number of calories for {:.2f} serving(s): {:.2f}'.format(numServings,
	food2.get_calories(numServings)))
