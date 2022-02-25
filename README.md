# Doctor Appointment site in Django

1. You can make an appointment with any doctor, in this site.
2. You can postpone or cancel an appointment if you want.

# To get this site running you can do the following

1. Create virtual environment to hold the packages required for this project.
2. To create a virtual environment you can do the following on your command line

`$ python3 -m venv venv`
`$ source venv/bin/activate` for linux/mac
`venv\Scripts\activate` for windows

3. After performing above steps do following to install the required packages

`(venv) $ pip install -r requirements.txt`

4. After all requirements are installed create the initial tables/migrations by followin command

`(venv) $ python manage.py makemigrations`
`(venv) $ python manage.py migrate`

5. You can now run the website by following command

`(venv) $ python manage.py runserver`

6. Now simply navigate to the **http://localhost:8000** or **http://127.0.0.1:8000** on you browser.
