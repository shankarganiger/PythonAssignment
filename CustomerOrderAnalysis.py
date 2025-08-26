# %% [markdown]
# ## Analyzing customer orders using python

# %% [markdown]
# ### Create Customer Order Data Structure

# %%
customerOrders = [
    # Customers with both clothing and electronics
    ("shankar", "phone", 40.00, "electronics"),
    ("shankar", "cap", 15.00, "clothing"),
    ("shankar", "usb", 5.00, "electronics"),
    ("shankar", "usb", 5.00, "electronics"),

    ("emma", "headphones", 55.00, "electronics"),
    ("emma", "scarf", 25.00, "clothing"),

    ("ananya", "smartwatch", 130.00, "electronics"),
    ("ananya", "jacket", 45.00, "clothing"),

    ("jack", "gamingmouse", 60.00, "electronics"),
    ("jack", "TShirt", 20.00, "clothing"),

    ("liwei", "earbuds", 35.00, "electronics"),
    ("liwei", "sneakers", 50.00, "clothing"),

    # Clothing only
    ("ravi", "shorts", 15.00, "clothing"),
    ("ravi", "hoodie", 25.00, "clothing"),

    ("elena", "dress", 70.00, "clothing"),
    ("elena", "necklace", 35.00, "clothing"),

    ("sophia", "yoga pants", 40.00, "clothing"),
    ("sophia", "tank top", 10.00, "clothing"),

    # Electronics only
    ("jacob", "tablet", 120.00, "electronics"),
    ("jacob", "charger", 25.00, "electronics"),

    ("hiroshi", "keyboard", 55.00, "electronics"),
    ("hiroshi", "mousepad", 12.00, "electronics"),

    # Mixed categories (not clothing or electronics)
    ("kwame", "blender", 80.00, "homeessentials"),
    ("kwame", "towel", 12.00, "homeessentials"),

    ("fatima", "cookware set", 95.00, "homeessentials"),
    ("fatima", "journal", 15.00, "stationery")
]


# %% [markdown]
# ### Loop through the list of tuples

# %%
print("***Customer Orders***")
for customerOrder in customerOrders:
    print (customerOrder)

# %% [markdown]
# ### Create a dictionary with customer as key and products as values **{"customerName": []}**

# %%
customerProducts= {};
for customerOrder in customerOrders:
   customerProducts.setdefault(customerOrder[0], set())
   customerProducts[customerOrder[0]].add(customerOrder[1])

print("***Products purchased by customers***")
print(customerProducts)

# %% [markdown]
# ### Classify products by category 

# %%
productCategoryDictionary =  {}
for customerOrder in customerOrders:
    productCategoryDictionary.setdefault(customerOrder[3], set())
    productCategoryDictionary[customerOrder[3]].add(customerOrder[1])

print("***Product Category to product Mapping***") 
print(productCategoryDictionary)
    

# %% [markdown]
# ### Set of unique product categories 
# 

# %%
productCategories = list([item.upper() for item in productCategoryDictionary.keys()])
print("***Unique Product Categories***")
print(productCategories)

# %% [markdown]
# ### Total Customer Spend and classification

# %%
customerClassification = {}
for customerOrder in customerOrders:
    
    customerClassification.setdefault(customerOrder[0], {"totalspend":0.0, "classification":"" })
    value_dict = customerClassification[customerOrder[0]]
    if "categories" not in value_dict:
        value_dict["categories"] = set()
    
    value_dict["categories"].add(customerOrder[3])
    
    customerClassification[customerOrder[0]]["totalspend"]  =  customerClassification[customerOrder[0]]["totalspend"] + customerOrder[2];
   
for name, values in customerClassification.items():
    classification = ""
    if values["totalspend"] > 100:
        classification = 'high-value'
    elif values["totalspend"] <= 100 and values["totalspend"] >= 50:
        classification = 'moderate-value'
    else:
          classification = 'low-value'   
          
    values["classification"] = classification
    print(f"The customer '{name.upper()}' is of '{classification.upper()}'")
          
print(customerClassification)


# %% [markdown]
# ### Unique product list

# %%
productList = list([product.upper() for productlist in productCategoryDictionary.values() for product in productlist])
print(productList)

# %%


# %% [markdown]
# ### Total revenue by product category

# %%
revenueProductCategory = {}

for customerOrder in customerOrders:
    revenueProductCategory.setdefault(customerOrder[3],0.0);
    revenueProductCategory[customerOrder[3]] = revenueProductCategory[customerOrder[3]] + customerOrder[2];
    
print(revenueProductCategory)

# %% [markdown]
# ### Customers who purchased electronics products.
# 

# %% [markdown]
# 

# %%
electronicCustomers = set([ customerOrder[0].upper()  for customerOrder in customerOrders if customerOrder[3].upper() == 'ELECTRONICS'])
print(electronicCustomers)

# %% [markdown]
# ### Top three highest-spending customers using sorting.

# %%
customersWithSpending = (sorted(customerClassification.items(),key= lambda x: x[1]['totalspend'],  reverse=True))
print (customersWithSpending[:3])
i = 1 
for customer in customersWithSpending[:3]:
    print(f"Number {i} spender is {customer[0].upper()}")
    i = i+1

# %% [markdown]
# ## Organize and display data

# %%
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")

print("***Summary of each customer’s total spending and their classification***")
print("---------------------------------------------------------------")


customerwithMultipleCategories = {}
customersWithClothingandElectronics = {}
for customer in customersWithSpending:
    customerName = customer[0]
    classification = (customer[1])["classification"]
    totalSpend = (customer[1])["totalspend"]
    categories = (customer[1])["categories"]
    if(len(categories) > 1):
        customerwithMultipleCategories.setdefault(customerName,  {"categories": categories, "isClothingAndElectronics": 0})
        if("electronics" in categories and "clothing" in categories):
            (customerwithMultipleCategories[customerName])["isClothingAndElectronics"] = 1
        else:
            (customerwithMultipleCategories[customerName])["isClothingAndElectronics"] = 0
            

        
    print(f"The customer '{customer[0].upper()}' classified as '{classification.upper()}' spent {totalSpend}")
    
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("***Customers who purchased from multiple product categories***")
print("---------------------------------------------------------------")

#print(customerwithMultipleCategories)
for key,value_dict  in customerwithMultipleCategories.items():
    categories = value_dict["categories"]
    print(f" The customer '{key.upper()}' purchased in categories {categories}")

print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("***Common customers who bought both electronics and clothing***")
print("---------------------------------------------------------------")

customersWithClothingandElectronics = [name.upper() for name, values in customerwithMultipleCategories.items() if values["isClothingAndElectronics"] == 1 ]

for customer in customersWithClothingandElectronics:
    print(customer)
#print(customersWithClothingandElectronics)

#customersWithClothingandElectronics = [name for name, categories in customerwithMultipleCategories if "electronics" in categories ]

    



