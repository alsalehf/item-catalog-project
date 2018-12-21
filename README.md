# Catalog App
This is a sports items catalog website. This website has predefined sports categories. These are:\
**1.** Baseball\
**2.** Basketball\
**3.** Foosball.\
**4.** Frisbee.\
**5.** Hockey.\
**6.** Rock Climbing.\
**7.** Skating.\
**8.** Snowboarding.\
**9.** Soccer.\
\
 Users in this website can perform the following:\
  **1.** Login to the app using Google user account authentication through the oAuth API\
  **2.** Add new items based to the catalog under the predefined categories.\
  **3.** Edit/Delete the items the user have created.\
It connects to **SQL** database using **Python 2.7.12** and it uses **Flask** framework to perform HTTP requests. Also, **SQLAlchemy** was used in order to connect to the database.\
\
Run these in the command line to construct and fill the database & run the website:\
`cd item-catalog-project`\
`python database_setup.py`\
`python seeder.py`\
`python item-catalog.py`\
\
Now, open your favorite browser and type the following to access the website:\
`http://localhost:8000`
