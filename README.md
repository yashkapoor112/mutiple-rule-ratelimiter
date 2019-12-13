## mutiple-rule-ratelimiter
Analogy of a rate limiter where dynamic rules can be created and deleted.  

## Pre requisites –   
  •	Clone the current repo.  
  •	Create virtual environment in python (in the base directory)  
  •	Install python3  
  •	Installing Postgres  
      o	Create DB named targayren  
      o	Create role by name postgres with password 12345  
      o	Make postgres the owner of the database  
      o	Install Django connector for postgres psycopg   
  •	Install requirements.txt in the virtual environment  

## Instructions – 
  •	Project name is WorldOfTargayren  
  •	Webapp name kills  

## After installation complete – 
  •	Run predefined migrations  
  •	Make migrations for the new model structure  
  •	Apply new migrations  

## API Details – (views.py)
  •	register_dragon():  
    o	Adds a new dragon  
    o	Output – Dragon ID  
   
  •	add_rule():  
    o	Adds a new rule  
    o	Output – Rule ID  
   
  •	delete_rule():  
    o	Deletes a rule by ID  
    o	Ouput – Rule deleted or not  
    
  •	kill_animals():  
      o  Inputs-   
                	Dragon ID  
                	Number of animals to be killed  
                	Timestamp – (%Y-%m-%d-%H:%M format)  
      o	Outputs –   
                	Kill possible or not  
                	If yes then process the kill  


## Important -   
Run this command to use the settings of the apps  
export DJANGO_SETTINGS_MODULE=WorldOfTargayren.settings  
