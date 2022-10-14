# Django FS Tasks

## Todo task list
Build a Django application with following functionalities

1. Exposes an API to store the emails. Feel free to use Django REST Framework
2. A view to list down the emails in the reverse chronological order and show the number of new emails added this calendar month
3. Integrate the api with the email collection widget present in this project.
4. Bonus - set up a celery task that runs every Monday and Wednesday and prints the number of new emails added in the current calendar month to the console.

## Implementation notes

### Project structure
- Django project named **mysite**
- Project has only 1 custom app: **unity**

#### Data Models

- Store: to save Store's information
- Leads: to save Store's Leads, who subscribed to each individual Store
Beside unity app models, the User Model was used to present store owner. User data model used to implement authentication as well.

#### Authentication
I had changed from **TokenAPI** to **Django OAuth Toolkit**

After install and configure app, we need go to creat clientapp for each Store.
1. login to the application
- Access to the link: http://127.0.0.1:8000/admin
- Enter user and password
![](D:\MyProjects\DjangoTestR1\django_test_r1\doc_assets\images\login.png)

2. Create application
- Click to the **add** button **Applications** on the group **Django Oauth Toolkit**
- Enter information to create Application for client - **Kafa**
![](D:\MyProjects\DjangoTestR1\django_test_r1\doc_assets\images\add_application.png)
- Client application was added, we will use Client id and Client secret to get Access token key for client application to consume our API. 
3. We can send request to get access token key like below:
> curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/

The result returned will be something like this:
> {
    "access_token": "j0qGAqBCKlAt0gh30V4Ap9sQ9uoqV3",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write groups",
    "refresh_token": "BiYIe2C4fyfHBeSSAtYY9Oo91Q1t91"
}
4. Consume API - Leads Subscribed
Once done, we can use the api for leads to subscribe.
Send request to API like below:
![](D:\MyProjects\DjangoTestR1\django_test_r1\doc_assets\images\consume.png)

When API was called, it will check the Access Token key was assigned to which application, and we can get User to determine Store accordingly.

### Using Celery for cron-jobs.

#### Schedule task

1. setup crontab to run on 0th minute of each Monday and Wednesday
![](D:\MyProjects\DjangoTestR1\django_test_r1\doc_assets\images\crontabs.png)
2. apply crontab to the task
![](D:\MyProjects\DjangoTestR1\django_test_r1\doc_assets\images\schedule task.png)
We will use rabbitMQ and Celery to demo simple automation task.

#### Install rabbitMQ on windows using docker
We can run Docker Command to execute rabbitMQ
> docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management

#### Run celery beat
celery -A unity beat -l INFO  --scheduler django_celery_beat.schedulers:DatabaseScheduler

### Run celery worker
> celery -A tutorial worker -l INFO -P solo
![](D:\MyProjects\DjangoTestR1\django_test_r1\doc_assets\images\celery_worker_console.png)

