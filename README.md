# test-repetition
<details open>

**<summary> Concept list </summary>**

- [Description](#Description) 
- [License](#License)
- [Docker command](#Docker-command)
- [Usage ](#Usage )
  - [Contact book endpoints](#Contact-book)    
    - [Admin](#Admin)
    - [List of all contacts](#List-of-contacts)
    - [Delete](#Delete)
    - [Update-contact](#Update-contact)
    - [Add-contact](#Add-contact)
    - [Filters](#Filters)
    - [Home](#Home)
    - [Register](#Register)
    - [Login](#Login)
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
