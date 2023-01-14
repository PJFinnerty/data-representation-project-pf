# data-representation-project-pf - By Peter Finnerty

Main Project for Data Representation module in the H.Dip in Data Analytics.

## Outline

This project aims to simulate a system to manage delivery of products to Galway Cinemas. The project is intended to demonstrate core understanding of creating a Rest API, featuring a server, interacting with Data Access Object files and user input from html pages, that pass these inputs back down to a database.

#### The project at a basic level features the following:

1. A basic Flask server that has a
2. REST API, (to perform CRUD operations)
3. A main database table (which is the Cinemas table which features the names of the three cinemas, details on number of screens and location)
4. Accompanying web interface, using AJAX calls, to perform these CRUD operations

##### Additionally, it features:
5. Authorisation by the server through the HTML page (verified by the username recorded in the ipconfig file)
and
6. 3 other database tables (which are of the same design but relate to different delivery orders for each of the Cinemas) - these are all linked to the main Cinemas table. It is the delivery tables that are used to perform CRUD operations on.
7. The server and database are hosted online, at PythonAnywhere - allowing the user to access the full functionality at the following address: 'http://finnertypete.pythonanywhere.com/'

## How to Run the Server - There are two ways to run the server, and access the database, both are listed below.

## 1. Access online through python anywhere, at 'http://finnertypete.pythonanywhere.com/'
This is the recommended option as it does not require any creating of MySQL databases. The PythonAnywhere web app above, connects to a virtual MySQL table, and is configured using bash, with the required password and username. The project files are all contained within a virtual directory on Python Anywhere. The user can simple access the url and will be taken to the Homepage and can make edits to the Cinema delivery pages from there.

## 2. Access through the local host - accessing locally requires taking the steps listed below: 
#### Before starting the server, the user must run the following 4 files:
1. 'Create_CinemaList.py'
2. 'Create_EyeCinema.py'
3. 'Create_IMCHeadford.py' 
4. 'Create_IMCOranmore.py'

This will create a single database, but 4 separate SQL tables, each in the same database. Each file runs SQL insert commands to populate the tables with some initial data. Print statements in each of the files should verify to the user that the inserts have worked. Should this process fail, I have included SQL files for the 'CinemasDelivery' database, that should create the tables and pass the insert commands.

#### Following this, the user may run the server by simply running the following file:
'server_cinemas-delivery.py' - this is the main file that links to the DAO and allows the user to access http://127.0.0.1:5000/, which will direct to a login page, configured in the server file. The user should be prompted to login, at which point, they should be autoatically directed to the 'Cinemas_Homepage.html' file - their current location being http://127.0.0.1:5000/Cinemas_Homepage.html.

#### From the Cinemas_Homepage, which connects to the Cinemas table, you will be able to choose a redirect to enter delivery options at one of the following pages:
1. Delivery_Eye_Cinema.html - connects to the EyeCinema table
2. Delivery_IMC_Headford_Road.html - connected to the IMCHeadfordRoad table
3. Delivery_IMC_Oranmore.html - connected to the IMCOranmore table

On these pages, the user can choose to update a current delivery option, delete an item, or add a new item. Each of the tables contain separate items, as the cinemas in this simulation would require different items.

##### Config Files
ipconfig.py and ifconfigcinemas.py files - these two files feature user and database details to access MySQL. 

##### ** NB: Should there be an issue for the user in accessing the databases created, the username can be changed in the ipconfig files. As the DAO and server make calls to the databases according to these files, this change is all that is needed.

##### DAO Files
1. CinemasDAO.py - this file features the functions to access and manipulate the Cinemas tables
2. DAOEyeCinema.py - this accesses the EyeCinema table
3. DAOIMCHeadfordRoad.py - this accesses the IMCHeadfordRoad table
4. DAOIMCOranmore.py - this file connects the server to the IMCOranmore table

##### SQL Files (Incase there is issue with the Create table tiles, SQL files can be run directly)
1. Cinemas.sql - SQL commands to create the database CinemaDelivery and the Cinemas table
2. Cinemas-EyeCinema.sql - SQL commands to create the EyeCinema table
3. Cinemas-IMCHeadford.sql - SQL commands to create the IMCHeadford table
4. Cinemas-IMCOranmore.sql - SQL commands to create the IMCOranmore table

##### Requirements
The user must have Python and MySQL installed on their machines to run the server and access/edit the data

The .gitignore file features the relevant modules that should be ignored by git, including .venv.





