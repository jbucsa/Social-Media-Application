# Social-Media-Application

## Terminal Commands

### Creating the VENV environment

```bash
py -m SocialMediaApplication venv
```

    
### Activating the VENV environment

- For Command Prompt - cmd
    
```bash

C:\Users\User\Social-Media-Application> SocialMediaApplication\Scripts\activate.bat

(Social-Media-Application) C:\Users\User\Social-Media-Application> 

```
   
- For Git Bash - bash
    
```bash
User@User MINGW64 ~/Social-Media-Application (main)
$ source SocialMediaApplication/Scripts/activate

(SocialMediaApplication) 
User@User MINGW64 ~/Social-Media-Application (main)
$ 

``` 

### Deactivating the VENV environment


- For Command Prompt - cmd

```bash
(SocialMediaApplication) C:\Users\User\Social-Media-Application> SocialMediaApplication\Scripts\deactivate.bat

C:\Users\User\Social-Media-Application> 

```
   
- For Git Bash - bash
    
```bash
(SocialMediaApplication) 
User@User MINGW64 ~/Social-Media-Application (main)
$ deactivate

User@User MINGW64 ~/Social-Media-Application (main)
$ 

```

## PIP Installs

The following are the PIP packages required to running the application. 

### Installing Pillow
```bash
python -m pip install Pillow
```

### Creating a Django application

```bash
pip install django

```

- Use the following command to create a django template application. Note that 'sma/' is only here because we want our project to start within a directory called 'sma'. If you leave out 'sma/', the application will be created in the directory the terminal is located in.

```bash
django-admin startapp sma/core

```

## Running a Django Server

```bash
python sma/manage.py runserver
```

## Database - Migrations and Terminal Commands 

### Make migrations

After creating the schema model (see file sma/core/models.py). Run the following terminal command to migrate the schema into the database.

```bash
python manage.py makemigrations
python manage.py migrate
```

## Administration Settings

### Create Superuser (Admin User)

To create a super user (the admin user for the application), run the following terminal command. 

```bash
python manage.py createsuperuser
user: admin
email: admin@socialmedia.com
password:
password (again): 
bypass validation
```



## Authors

Justin Bucsa
- https://github.com/jbucsa
- [![LinkedIn][linkedin-shield]][linkedin-url-Bucsa]

Aldo Resendiz
- https://github.com/aldoresendiz   
- [![LinkedIn][linkedin-shield]][linkedin-Aldoresendiz]

Thilini Dharmawardhana
- https://github.com/ThiliniDharma
- [![LinkedIn][linkedin-shield]][linkedin-Dharmawardhana]



[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url-Bucsa]: https://www.linkedin.com/in/justin-bucsa
[linkedin-Aldoresendiz]: https://www.linkedin.com/in/aldoresendiz/
[linkedin-Dharmawardhana]: https://www.linkedin.com/in/thilini-dharmawardhana-b4715717/
