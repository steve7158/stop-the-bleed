# stop-the-bleed
For the hackathon stop the bleed
These commands are to performed in linux OS 
Firstly clone the repository into a folder 
# Installations: 
1. go to your terminal.

2. sudo apt-get install python-pip (install pip).

```
pip install flask 
pip install termcolor 
pip install wtforms 
pip install passlib.hash 
pip install flask_sqlalchemy 
pip install sqlalchemy.sql 
pip install pytz 
pip install datetime 
pip install werkzeug.utils 
```
TO Run go to the saved directory and enter in the terminal 

3. to set the dataset: install postgresql and pgadmin connect them follow the their documentations in their official sites 

4. create a database using pg admin by right clicking the Databases and then new database 

5. to create a table: go to terminal and enter: 

  ```
  python
  

from app import db db.create_all()
```
6. to run the application enter in the terminal` python app.py`
