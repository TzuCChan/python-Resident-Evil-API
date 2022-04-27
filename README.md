# python-Resident-Evil-API

## About

Python and Flask Project with full CRUD functionality

## Description

Users will be able to access information about Resident Evil games.

## Technologies Used

1. Python
2. Flask
3. SQL database
4. PeeWee models
5. Postman

## Endpoints

| Method | Endpoint   | Description            |
| :----- | :--------- | :--------------------- |
| POST   | /games     | Creates games.         |
| GET    | /games     | Reads all games.       |
| GET    | /games/:id | Reads a specific game. |
| PUT    | /games/:id | Updates a game.        |
| DELETE | /games/:id | Deletes a game.        |

## Processes

1. Open the terminal.
2. Go to ther folder.
3. Inside the folder, type mkvirtualenv python-flask-Resident-Evil to create the virtual environment.
4. Inside the virtual enivornment, type pip3 install flask.
5. Once flask is installed, type python app.py to find the localhost.
6. Once the localhost is found, type pip3 freeze > requirements.txt to install the necessary data.
7. Type the codes in the app.py.
8. Return to the terminal again, and type psql to access to the user(me).
9. Type \l to see my list of database.
   List of databases
   Name | Owner | Encoding | Collate | Ctype | Access privileges  
   -------------------+-------------------+----------+---------+-------+-----------------------------------------
   cosmicbinturongs | leontzuchiangchan | UTF8 | C | C |
   leontzuchiangchan | leontzuchiangchan | UTF8 | C | C |
   library | leontzuchiangchan | UTF8 | C | C |
   people | leontzuchiangchan | UTF8 | C | C |
   pets | leontzuchiangchan | UTF8 | C | C |
   postgres | leontzuchiangchan | UTF8 | C | C |
   template0 | leontzuchiangchan | UTF8 | C | C | =c/leontzuchiangchan +
   | | | | | leontzuchiangchan=CTc/leontzuchiangchan
   template1 | leontzuchiangchan | UTF8 | C | C | =c/leontzuchiangchan +
   | | | | | leontzuchiangchan=CTc/leontzuchiangchan
   (8 rows)

10. To create the new database for this project, I typed CREATE DATABASE biohazard; for my project.
    List of databases
    Name | Owner | Encoding | Collate | Ctype | Access privileges  
    -------------------+-------------------+----------+---------+-------+-----------------------------------------
    biohazard | leontzuchiangchan | UTF8 | C | C |
    cosmicbinturongs | leontzuchiangchan | UTF8 | C | C |
    leontzuchiangchan | leontzuchiangchan | UTF8 | C | C |
    library | leontzuchiangchan | UTF8 | C | C |
    people | leontzuchiangchan | UTF8 | C | C |
    pets | leontzuchiangchan | UTF8 | C | C |
    postgres | leontzuchiangchan | UTF8 | C | C |
    template0 | leontzuchiangchan | UTF8 | C | C | =c/leontzuchiangchan +
    | | | | | leontzuchiangchan=CTc/leontzuchiangchan
    template1 | leontzuchiangchan | UTF8 | C | C | =c/leontzuchiangchan +
    | | | | | leontzuchiangchan=CTc/leontzuchiangchan
    (9 rows)

11. Deployed to the Postman to get the ID.
12. Make sure the POST, PUT, DELETE work in the Postman.
