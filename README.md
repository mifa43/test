# test-repetition
<details open>

**<summary> Concept list </summary>**

- [Description](#Description) 
- [License](#License)
- [Docker command](#Docker-command)
- [Usage ](#Usage )
  - [Contact book endpoints](#Contact-book)    
    - [Admin](#Admin)
    - [Register](#Register)
    - [Login](#Login)
    - [Add-contact](#Add-contact)
    - [List of all contacts](#List-of-contacts)
    - [Delete](#Delete)
    - [Update-contact](#Update-contact)
    - [Filters](#Filters)
    - [Home](#Home)
- [Contact](#Contact)

</details>

___

## Description
##### This is a repository for creating a simple 'Contact Book' application for a test task for Alas d.o.o.


## License
- Apache License 
- ##### [Read more about licenses](https://github.com/mifa43/test-repetition/blob/main/LICENSE)


## Docker command
- **Terminal :**
> ##### Go to the root folder where docker-compose is located and this command will make sure that the application starts successfully.

    docker-compose up --build -d

> ##### This command will open logs so that background execution can be monitored.

    docker container logs -f DjangoTest

> ##### If it is necessary to call some of the django-admin commands, this can be done with the accompanying command.

    docker exec -it DjangoTest /bin/bash

## Usage

- <http://localhost:8001> - (Access the application).

### Admin

- <http://localhost:8001/admin> - (Access the admin panel).

> #### login as admin

    Username: admin1
    Password: mypassword1

### Register

> If we try to access one of the endpoints we will only see a link that requires logging in by clicking on it, we get a login form where we need to authenticate. If we do not have an account, there is a link for registration below.

### Login

> After successfully creating an account, you are ready to log in and perform the first actions in the application (Contact Book).

### Add contact

> To create a contact, it is necessary to fill in the fields and add a contact by pressing the button.

### List of all contacts

> To view your contact list, tap contacts in the navigation bar and a contact information tab will be displayed