# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # API Test Calance US

# %%
# Dependencies and Setup
import pandas as pd
import requests
import json 


# %%
# Make Request tor Commit Comment b2b08f6
response = requests.get('https://api.bitbucket.org/2.0/repositories/calanceus/api-test/commit/b2b08f6')
json1 = response.json()
# Display to find location
print(json.dumps(json1, indent=5, sort_keys=True))


# %%
# Print to verify
print(json1["message"])


# %%
# Make Request tor Commit Comment 9de016d
response = requests.get('https://api.bitbucket.org/2.0/repositories/calanceus/api-test/commit/9de016d')
json2 = response.json()


# %%
# Make Request tor Commit Comment ce03dc0
response = requests.get('https://api.bitbucket.org/2.0/repositories/calanceus/api-test/commit/ce03dc0')
json3 = response.json()


# %%
# Make Request tor Commit Comment 5c69e6a
response = requests.get('https://api.bitbucket.org/2.0/repositories/calanceus/api-test/commit/5c69e6a')
json4 = response.json()


# %%
# Make Request tor Commit Comment 3aab06e
response = requests.get('https://api.bitbucket.org/2.0/repositories/calanceus/api-test/commit/3aab06e')
json5 = response.json()


# %%
# Make Request tor Commit Comment bf43da5
response = requests.get('https://api.bitbucket.org/2.0/repositories/calanceus/api-test/commit/bf43da5')
json6 = response.json()


# %%
# Make Request tor Commit Comment 947362e
response = requests.get('https://api.bitbucket.org/2.0/repositories/calanceus/api-test/commit/947362e')
json7 = response.json()


# %%
# Print Out Comments in Chronological order
import sys
filename  = open("Commit_comments",'w')
sys.stdout = filename
print(json7["message"])
print(json6["message"])
print(json5["message"])
print(json4["message"])
print(json3["message"])
print(json2["message"])
print(json1["message"])

