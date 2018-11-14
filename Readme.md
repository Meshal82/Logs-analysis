# Logs Analysis

> Meshal AL-hossan

## About the project

This is the first project for the Udacity Full Stack Nanodegree. In this project, we are working on news database and the goal of this project is to print reports based on the data to find out valuable information that helps make better business choices (for example, what articles that readers like the most). 


### Set up:
1.Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)<br>
2.clone from github [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)</br>
3- newsdata.sql file to load the database
4- Download the [database script](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip and place it under the /vagrant directory



### To Run

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

To execute the program, run `python3 ANALYSIS.py` from the command line.


### Used views

#### total
````sql

create view total as
select Date(time) as day , count(*) as visits
from log group by day order by day;
````



#### total_error
````sql

create view total_error as
select date(time) as day , count(*) as errors
from log where status='404 NOT FOUND' group by day order by day;
````


#### error_percentage 
````sql

create view error_percentage as
select total.day , round(100.000 * errors / visits , 3 ) as perc
from total join total_error
on total.day = total_error.day;
````


## Helpful Resources

* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads)
