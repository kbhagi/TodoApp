### Todo App 

A console version of Todo App written in pure python 3.6 , no frameworks used except for the standard built-in libraries. 
This is a task manager that used to keep oneself organized for the day. It can do the following :
1. Add a Task
2. Search a Task
3. Delete a Task
4. Update a Task

For persistence , have built a simple DB which uses a file for storage.  This DB mimics a database but is primitive , trivial in nature.

### How does it work : 

  The app is composed of model.py , controller.py , view.py and DB.py. It follows the MVC pattern.  All the data from a file called db.json is read in a certain format into a list in memory. The list is modified and again written back into a file. The operations such as Search , Delete and Update happens on the elements in the list 
  Task name is taken as a key for search, update and delete
  
#### Why did i build it :
I used to watch tutorials to learn either a framework , crack an interview , pass a cert exam . Honestly none of these task made me feel satisfied. It always used to be some other person telling me how / what to do. There came a desire to build something for myself. Lot of ideas came across my mind. The aim was to start from basics. Databases seemed fascinating to me. What data structures are they using. How do they work. 

#### packages used  
 * datetime
 * os
 * pathlib
