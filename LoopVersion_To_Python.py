# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # API Test Calance US LOOP VERSION

# %%
# Dependencies and Setup
import pandas as pd
import requests
import json 


# %%
# Make Request tor Commit Comment b2b08f6
response = requests.get('https://api.bitbucket.org/2.0/repositories/calanceus/api-test/commits')
json1 = response.json()
# Display to find location
print(json.dumps(json1, indent=5, sort_keys=True))


# %%
# Create and Open File
file = open("Commit_Comments_LoopVersion", "w+")
# Create Loop to Pull Messages and Print to Text File
for value in reversed(json1["values"]):
    file.write(value["message"])
# Close File
file.close()

