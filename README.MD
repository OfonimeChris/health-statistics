CODES DEFINITION/EXPLANATION

1.Group9_flask.ipynb: 
 -We created a database using Sqlite3 called "health_insurrance.db"
 -We created a table called "health"
 -We inserted the data in our table
 -We printed out the data from the table saved in the database
 -We commit and close our database


2.Build_db_fillin.py:
 -Imports necessary libraries: "pathlib", "sqlite3", and "pandas" (as "pd").
 -Defines a function "create_db()" to create an SQLite database from a health-related CSV file.
 -Connects to an SQLite database, reads CSV data into a Pandas DataFrame, and writes it to an SQLite table.
 -Executes a SQL query to fetch and print data from the created SQLite table.
 -Commits changes to the database and closes the connection.
 -The main block sets specific parameters and calls the "create_db()" function to execute the database creation process.


3.App_insurr_1.py:
 -Sets up a Flask web application ("app") and imports necessary modules ("Flask", "render_template", "sqlite3", "pathlib").
 -Defines routes ("/", "about", "data") using "@app.route()" decorators:
  -"/"renders "index_fillin.html" at the root URL.
  -"/about"renders "about.html".
  -"/data" connects to an SQLite database, fetches health data from the "health" table, and renders it in a table format using "data_table_fillin.html".
  -Specifically within the "/data" route:
  -Establishes a connection to the SQLite database and retrieves data using SQL queries.
  -Passes the fetched data ("health") to the "data_table_fillin.html" template.
  -Runs the Flask application with debugging enabled if the script is executed directly.


4.Index_fillin.html:
 -Defines an HTML document with the title "Health Statistics Insight."
 -Displays a webpage with a main heading "Welcome to our Home page!" and introductory text "Where do you want to go?"
 -Provides a list of hyperlinks:
 -One hyperlink labeled "Link to About page" that, in a web application context (e.g., Flask), dynamically generates a URL  for navigating to the 'About' page.
  -Another hyperlink labeled "Link to Data page" that, similarly, generates a URL for navigating to the 'Data' page within the web application.


5.about.html:
 -Defines an HTML document with the title "Health Statistics Insight."
 -Displays an "About Our Website" section:
  Acknowledges visitors for accessing the HealthStat Insight platform.
  Describes the platform's focus on health-related data analysis and its mission to provide insightful health trend   information for informed healthcare decisions.
 -Provides information on the data source:
  Mentions obtaining the dataset from DataWorld, a platform offering various datasets for statistical analysis.
 -Details the variables within the dataset:
  Lists five variables: PatientID, Age, Gender, BMI, and BloodPressure.
  Describes each variable's significance and relevance in health analysis:
    -PatientID: Unique identifier for individuals in the dataset.
    -Age: Represents individuals' ages in years and its importance in health analysis.
    -Gender: Identifies an individual's biological sex and its relevance in assessing health risks.
    -BMI (Body Mass Index): Measures body fat based on weight and height, aiding in categorizing weight-related health conditions.
    -Blood Pressure: Reflects blood force on blood vessel walls, crucial for assessing cardiovascular health.


6.data_table_fillin.html:
 -Defines an HTML document with the title "Health Statistics Insight."
 -Sets up a style block to define the appearance of tables using CSS.
 -Styles tables to have collapsed borders and specific padding for table cells ("th" and "td").
 -Sets a background color for table headers ("th" elements).
 -Displays a heading "Our Data" ("<h1>") indicating the section's content.
 -Constructs a table to display health-related data with table headers:
  -The table headers are: PatientID, Age, Gender, BMI, and BloodPressure.
 -Uses template placeholders ({ health }) to incorporate data dynamically, likely from a templating engine in a web framework (e.g., Flask).
 -Utilizes a template loop ({% for h in health %} ... {% endfor %}) to iterate through each entry in the `health` dataset.
  Generates table rows ("<tr>") with individual data entries displayed in table cells ("<td>").
  Extracts and displays specific data elements (PatientID, Age, Gender, BMI, BloodPressure) within the table cells using template variables ({{ h[0] }}, {{ h[1] }}, {{ h[2] }}, {{ h[3] }}, {{ h[4] }}).
    
    
    

