# what is Airflow?
'''
typical airflow usecase => data pipeline to trigger everyday at 10pm (a workflow)

download data (request API) => process data (Spark job) => store data (insert/update DB)

in normal cron job, if one task fails the others will still run and fail (or worse), airflow prevent s such issues.

Apache Airflow is an open source platform to programatically author, schedule, monitor workflows

airflow components :
        web server => Flask server with gunicorn serving the ui
        Scheduler => daemon in charge of scheduling workflows
        MetaStore => database where metadata are stored
        Executor => class defining how your tasks should be executed
        Worker => Process/subProcess executing your task

DAG : the process of workflow is what the dag consists of.

operator : a wrapper around the tasks that you would want to do, example
        db = connect(host, creds)
        db.insert(sql_request)

each operator has its own task,  one-operator <==> one-task

Action operator => operators executing functions or commands. bash operator, python operator,...
Transfer operator => allows transfering data between source and destination. mysql operator
Sensor operator => wait for something to happen, gets triggered and then do something

Task : an operator in your data pipeline, when you execute an operator, it becomes a task instance

Airflow is NOT a data streaming solution or data processing framework.
'''


# how does airflow work?
'''
single node architecture => all processes happen on one node (machine)

multi node => first machine includes webserver, scheduler, executor, second node is metastore db and queue, 
other nodes are worker nodes that are called "airflow worker"

folder dags => where the datapipeline files are stored at.
'''


# how to install Airflow?
'''
easiest way to install airflow is installing it on linux machine or on  a vm that runs linux.
we can add port forwarding to the VM to connect to the machine via ssh.

install remote-ssh on VScode to connect to the vm through vscode terminal

in VScode :
1- command+p
2- type "remote-ssh"
3- type "ssh -p portNumber airflow@localhost
4- select first given file to save the ssh settings
5- enter password for the vm, then you are connected to the VM
6- open the vscode terminal to access the linux machine

inside the terminal:
1- create virtual environment => python3 -m venv name-of-env
2- activate the venv => source name-of-env/bin/activate
3- install wheel => pip install wheel
4- install airflow, with the given constraints for helper modules => pip install apache-airflow==2.0.0 --constraint constraints.txt
5- initialize the metaStore database => airflow db init  (only run this command once)
6- if you type "ls" the airflow folder should be visible
7- go to airflow folder and create dags folder => mkdir dags
'''


# how to run airflow?
'''
1- go inside airflow folder
2- start airflow => airflow webserver
3- access UI on the web browser at => localhost:8080  (8080 is the forwarded port here)
4- see all the airflow helps => airflow -h
5- create a airflow admin user => airflow users create -u username -p pass -f name -l lastName -r Admin -e example@gmail.com
6- login through webUI with the given username/password
7- start the scheduler => airflow scheduler

** If a task fails, check the logs by clicking on the task from the UI and "Logs"
** The Gantt view is useful to spot bottlenecks and tasks are too long to execute
'''


# extra airflow CLI commands
'''
update database => airflow db upgrade
reset database => airflow db reset
show a list of all available dags => airflow dags list
show all tasks related to a dag => airflow tasks list dag_id_name
run a dag at a specific time and date => airflow dags trigger -e 2022-01-01 dag_id_name
'''


# DAG
'''
a dag is a datapipeline in airflow, Directed acyclic graph. 

example DAG:
create table => is_api_available => downloading_users => process_users => saving users in db

create the DAG file with python format, inside the dags folder of the VM

after creating and running the dag python file, you need to add its 'sqlite_conn_id' to 
admin->connection page of airflowUI as a new connection

each time you add a new task to the datapipeline, remember to also test the task. (run it from inside of airflow folder)
        airflow tasks test dag_id task_id date_in_past 
        airflow tasks test user_processing creating_table 2020-01-01

open the db after creating it => sqlite3 airflow.db
'''

# dependencies
'''
dependencies allow the DAG to have ordering between its tasks, so it will know which one to run at first,
and which others to follow in a correct order
add this line in the DAG object after defining all tasks =>  creating_table >> is_api_available >> extracting_user
you can also use 'set_upstream' and 'set_downstream' functions instead of >> and <<
'''


# XCOM
'''
xcom is a way to share data between different tasks of one DAG.
task_1 by default creates a xcom (key-value pair), and then in task_2 we can access it via => xcom_pull(task_ids=['task_1_id']) 
the xcom values are saved in the airflow metaStore db
'''

# run the pipeline
'''
select the DAG pipeline in the webUI, un-pause it and wait for it to run.
if all boxes are green, it means the pipeline ran successfully
'''

# scheduling DAG
'''
start date : when => 2020/01/01 10AM
scheduling interval : frequency => 10 mins
execution date => 2020/01/01 10AM

all dates in Airflow are in UTC, (london-based timeZone), it can be changed from "default_timezone" variable in 
airflow.cfg file. (better NOT to change it)
'''

# Catchup Parameter
'''
imagine this interval:
DAG A 2020/01/01 @daily  =>  DAG run1 , DAG run2, DAG run3,...

if we pause this on second day and then try to trigger and continue it on fifth day, it will run ALL dag runs from 
last time it ran successfully until today!
=> therefore if you define a daily dag run and put start date in the past => all previous remaining dag runs will be executed!

this is controlled by Catchup parameter, which by default is set to True, to prevent this, set it to false.

to reset the DAG run for repeating the whole pipeline from start, go to browse -> DAG runs, and delete the pipeline
'''
