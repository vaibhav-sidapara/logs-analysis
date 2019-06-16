## Project: Logs Analysis

#### Description
This is the first project in Udacity's Full Stack Web Developer Nanodegree Program.

The task is to create a reporting tool that prints out reports( in plain text) based on the data in the given database (database provided by Udacity).

The Python script `logs_analysis.py` in this project uses the `psycopg2` library to query the database and produce a report that answers the following three questions:

1. What are the most popular three articles of all time?
    * Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
2. Who are the most popular article authors of all time?
    * That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors?
    * The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

The plain text file `logs_analysis_output.txt` in this project is used to display the output; that is a copy of what the program prints out.

---
#### Things to have/do before running the code
##### System Requirements
This project makes use of Linux-based virtual machine (VM).
- [Vagrant](https://www.vagrantup.com/)
- [Oracle VM VirtualBox](https://www.virtualbox.org/)
- [Git](https://git-scm.com/)

##### System Setup 
1. Git Clone  [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
    * Further Instructions provided on the above Udacity's repo on how to run the vagrant box.
    * Python & PostgreSQL database server are already installed and started in the VM 
2. Download & extract the [sql dump](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and run ```psql -d news -f newsdata.sql``` **within the vagrant machine** to import the data.
3. Git Clone this repo

##### Create Views
By first running the command `psql -d news`, create views within the vagrant machine 
```sql
CREATE OR REPLACE VIEW logs_view AS 
SELECT to_char(time,'DD-MON-YYYY') as date, 
count(*) as log_count 
FROM log GROUP BY date;
```

```sql
CREATE OR REPLACE VIEW error_logs_view AS
SELECT to_char(time,'DD-MON-YYYY') as date, count(*) as 
error_count FROM log WHERE STATUS = '404 NOT FOUND' 
GROUP BY date;
```

##### Running the code
`cd` into the project directory and run the below code within the vagrant machine
```
python logs_analysis.py
```