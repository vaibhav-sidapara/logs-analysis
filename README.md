## Project: Logs Analysis

#### DESCRIPTION
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