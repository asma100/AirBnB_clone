AirBnB Clone - README.md
Project Description

This project implements a basic command-line interface (CLI) for managing an AirBnB clone application. It utilizes a storage engine to persist data models like Users, States, Cities, Amenities, Places, and Reviews.

Command Interpreter

The project employs the HBNBCommand class to provide an interactive command-line interface. Users can interact with the application by issuing commands to create, read, update, and delete various data models.

Starting the Command Interpreter

Navigate to the project directory using your terminal.
Execute the following command:
Bash
python console.py
Use code with caution.
This will launch the HBNBCommand prompt:

(hbnb) 
Using the Command Interpreter

The command interpreter accepts various commands to manage data models. Here's a breakdown of some common commands:

Create: Creates a new instance of a specific model class.

Example: (hbnb) User create email="example@email.com" password="password123"
Show: Retrieves and displays the string representation of an existing instance.

Example: (hbnb) State show State.1234
Destroy: Deletes an instance based on the class name and ID.

Example: (hbnb) City destroy City.5678
Update: Modifies an existing instance by updating its attributes.

Example: (hbnb) Place update Place.9011 name="New Place"
All: Retrieves and displays string representations of all instances of a specific class (or all classes if no class is specified).

Example: (hbnb) Amenity all
Count: Prints the number of instances belonging to a specific class.

Example: (hbnb) User count
