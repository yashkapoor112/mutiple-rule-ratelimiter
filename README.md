## mutiple-rule-ratelimiter
Analogy of a rate limiter where dynamic rules can be created and deleted.  

## Pre requisites –   
  •	Clone the current repo.  
  •	Install python3  
  •	Create virtual environment in python (in the base directory)  
     ```python3 -m venv tutorial-env```   
  •	Installing Postgres   
     ```sudo apt-get update  
        sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib```  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Create DB named targayren  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` sudo -u postgres psql   
                                        CREATE DATABASE targayren;```  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Create role by name postgres with password 12345  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` ALTER ROLE username   
                                        WITH PASSWORD 'password';```  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Make postgres the owner of the database  
```GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;```  
  •	Install requirements.txt in the virtual environment  
  ``` pip install -r requirements.txt```  

## Instructions – 
  •	Project name is WorldOfTargayren  
  •	Webapp name kills  

## After installation complete – 
  •	Run predefined migrations  
  •	Make migrations for the new model structure  
  •	Apply new migrations  

## API Details – (views.py)
  •	register_dragon():  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Adds a new dragon  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Output – Dragon ID  
   
  •	add_rule():  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Adds a new rule  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Output – Rule ID  
   
  •	delete_rule():  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Deletes a rule by ID  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Ouput – Rule deleted or not  
    
  •	kill_animals():  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o  Inputs-   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Dragon ID  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Number of animals to be killed  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Timestamp – (%Y-%m-%d-%H:%M format)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Outputs –   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Kill possible or not  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	If yes then process the kill  


## Important -   
Run this command to use the settings of the apps  
export DJANGO_SETTINGS_MODULE=WorldOfTargayren.settings  
