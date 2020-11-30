# Coffee Shop Full Stack

## Full Stack Nanodegree

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.


### Auth0 account
```
AUTH0_DOMAIN = 'redants.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'cof'
```

> :warning: I DID updated the POSTman collection with both `barista` and `manager` accounts, the thing is that the token does expire, so I've created two dummy accounts on my Auth0 profile, both of them are verified and functional.

#### Manager account
```
User: redants.manager@yahoo.com
password: Red123456
submitted token (which can be expired at the time of review - "Dec 01 2020 05:33:03 GMT+0200"): 
```
`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBxdGxDdTJWdmN5WlJFOE5idjZKQyJ9.eyJpc3MiOiJodHRwczovL3JlZGFudHMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYzNmZmZiMWE3NTUwMDA3NjA0YTE1MyIsImF1ZCI6ImNvZiIsImlhdCI6MTYwNjcwNzUxNCwiZXhwIjoxNjA2NzkzOTE0LCJhenAiOiJxMTEyclhXUzRBREx4dXEyZ0F5OGpnT3g2YzZ5NXpiRSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.MNn0A18PcutLClGNb301sediU_kE-j4NWAu40EG9cbc8pWKc0DR74it6FKyNBsadrWpnQfa1fTs81-3NcNqGxi1vghn8xSseL09IrYee0M56HDSmTMjFhuFYwu6SSjjKKkQorLg5TsIqeUNK8fohT80LfP03z-xre-i7ykhllMeV0XhhvD3zVAcD0WXaNnvZxu8--9lArY5Gz48hy3N4GUr577tQdTakiJSuz3Y-9EVd7jW13hcpcd80VhbujLduVI3vC5ZYZOtAskusvFhuFOn7m3BbN0f-XoM41X2755UDgQPDdNJvygGDj-_BkSCMbdz8fCS6X1GvxKuXqE3UKg`


#### Barista account
```
User: redants.barista@yahoo.com
password: Red123456
submitted token (which can be expired at the time of review - "Dec 01 2020 05:33:03 GMT+0200" ):
```
`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBxdGxDdTJWdmN5WlJFOE5idjZKQyJ9.eyJpc3MiOiJodHRwczovL3JlZGFudHMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYzQ1NWViYzI5YmQ4MDA2ZWIwMjM5MSIsImF1ZCI6ImNvZiIsImlhdCI6MTYwNjcwNzE4MywiZXhwIjoxNjA2NzkzNTgzLCJhenAiOiJxMTEyclhXUzRBREx4dXEyZ0F5OGpnT3g2YzZ5NXpiRSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.IEagMTclVci3TY0ukuc8vfXhJTErJNzvyawZGT1Jykiwk2wJB73mZqTknGZoIDPyFmDqP6uoTwN67yOuUs2Iw6V7VBmG5R7Gi1vMcDomrPR6JHyX5CVyrmgcioehdw4PqGH5akOOMfhGVtpxxp4lJrsZCCN9M4f_wtRo0yY346gT8cvWyQlxVHK3AlynbpuMXBveMgfw6Rv4UKB56vA-bAuE6ZPIQ9X1IyTXlHlS1bjMsN-7zOfT84t_YtB02w5gvQoBssc3k2pOCFwwaMr9OffZ7xt81ckNMQa5IKe8tFcDW_sBxQguH1LCjEq_Ap6A-Ahpoxx5D62ktPbPxGwM7A`


### POSTman

* Exported collection with configured tokens can be found at: `/backend/udacity-fsnd-udaspicelatte.postman_collection.json`, to successfully test make sure to add new drink before running the collection.
* Test results containing 20 successful cases: `/backend/udacity-fsnd-udaspicelatte.postman_collection_test_run.json`
* Seed collection remains untouched 


### Backend

* Added Auth0 functionalities
* Implemented RESTful endpoints
* Implemented error handlers

#### Running the app

1. Install dependencies with `pip install -r backend/requirements.txt`
2. Set the `FLASK_APP` variable running `export FLASK_APP=api.py` 
3. Run the app with `flask run --reload`

### Frontend 

* Added the Auth0 variables on `environment.ts` file
* Guarantee that the frontend can be launched upon an `ionic serve` command and the login/token retrieval are functional


### .gitignore

* Added jetbrains folder

### Resources
* https://github.com/udacity/FSND/tree/master/BasicFlaskAuth
* https://github.com/auth0-samples/auth0-python-api-samples/tree/master/00-Starter-Seed



