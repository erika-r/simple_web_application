# web_application
Simple web application made using flask

This website was created in 4 parts
- creating a static homepage
- adding a "/formtest" endpoint which displays a web form asking for the user's name. The form is then submitted using POST and the user is redirected to a new page displaying the user's name using flask templates
- adding a "/allegiances" endpoint which calls the allegiances.csv file and returns the data in the browser as JSON data
- adding a "/allegiancedashboard" endpoint which returns a static page. Using javascript this will then make a call to the "/allegiances" endpoint and return the JSON data to construct a HTML table.
