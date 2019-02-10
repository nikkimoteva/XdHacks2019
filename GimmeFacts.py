import random

facts = list()


def gimmeFacts():
   facts.insert(0, "Artificial Trans Fats Are Unsuitable for Human Consumption")
   facts.insert(1, "You Don't Need to Eat Every 2–3 Hours")
   facts.insert(2, "Meat Doesn’t Rot in Your Colon")
   facts.insert(3, "Eggs Are One of the Healthiest Foods You Can Eat")
   facts.insert(4, "Sugary Drinks Are the Most Fattening Product in the Modern Diet")
   facts.insert(5, "Low-Fat Doesn’t Mean Healthy")
   facts.insert(6, "Fruit Juice Isn’t That Different From Sugary Soft Drinks")
   facts.insert(7, "Feeding Your Gut Bacteria Is Critical")
   facts.insert(8, "Cholesterol Isn’t the Enemy")
   facts.insert(9, "Weight Loss Supplements Rarely Work")
   facts.insert(10, "Health Is About More Than Your Weight")
   facts.insert(11, "Calories Count — But You Don't Necessarily Need to Count Them")
   facts.insert(12, "People With Type 2 Diabetes Shouldn’t Follow a High-Carb Diet")
   facts.insert(13, "Neither Fat nor Carbs Make You Fat")
   facts.insert(14, "Junk Food Can Be Addictive")
   facts.insert(15, "Never Trust Health Claims on Packaging")
   facts.insert(16, "Certain Vegetable Oils Should Be Avoided")
   facts.insert(17, "‘Organic’ or ‘Gluten-Free’ Doesn’t Mean Healthy")
   facts.insert(18, "Don’t Blame New Health Problems on Old Foods")

   return random.choice(facts)


gimmeFacts()