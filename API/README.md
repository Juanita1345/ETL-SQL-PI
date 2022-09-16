## **CREATION**

This is the file's structure for API creation:



Here is a simple description and steps of what we could find in each script:

* **DB_con.py**: Here is made the connection to database

1. Import <u>create_engine</u> from <u>sqlalchemy</u> package. This is used to create a engine connection to the database. 

2. Create variable <u>engine</u> where is almacenate de connection. This has the structure

<ul>
mysql+pymysql:Name:Password@host:port/DB_name
</ul>

3. Create variable <u>conn</u> where is declare te connection to database


* **Test.py** : Here is made the specific querys needed to answer the information requested 

1. Import <u>pandas</u> and <u>numpy</u> packages. 

<ul>
Each query have the following structure:
</ul>

2. Create <u>query_#</u> as string with MySQL structure

3. Create a dataframe with pandas calling the query and the connection

4. Declare a variable <u>anws_#</u> with answer of question

* **user.py**: Here is made path that we need for our API 

1.

<ul>

1.1 Import <u>APIRuter</u> from <u>FastApi</u> packages. 

1.2 Import <u>anws_#</u> given on Test.py. 

1.3 Import connection <u>conn</u> started up on DB_con.py. 

1.4 Import <u>APIRuter</u> from <u>FastApi</u> packages
</ul>

2. Used <u>APIRuter</u> for being able to define paths in a different script.

3. Declare a class with the structure of personalized query

4. For export queries is used the get method, where also is created a page for each question.

5. For personalized query is used the post method, where is defined a function and there is extract the query string. With pandas is executed that query ans storaged on a dataframe, and that one is converted to dictionary.

* **API-PI.py**: This is the main script for creating an API

1.
<ul>
1.1 Import <u>fastapi</u> from <u>FastAPI</u> packages

1.2 Import <u>user</u> created on user.py
</ul>

2. Create the app with FastAPI 

3. Call the path with the <u>user</u> created on user.py

4. Use the get method to create a welcome message which will help to identfy if the API is running correctly.