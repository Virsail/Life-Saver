# pitch
## Author

[Virsail](https://github.com/virsail)

# Description
This  is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application

## Live Link
[View Site]()

## Screenshot

![Screenshot from 2020-09-27 13-33-42](https://user-images.githubusercontent.com/66640798/94362753-36eda280-00c6-11eb-8af9-81a025c50f06.png)



## User Story
As a user i would like to:
* Comment on the different pitches posted py other users including my own pitch and leave feedback
* See the pitches posted by other users.
* Vote on a pitch by giving it an upvote or a downvote.
* Be signed in for me to leave a comment
* Receive a welcome email when i sign up to the app
* View pitches from the different categories.
* Submit a pitch to any category of choice
* View pitches I have created in my profile page


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirects to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |**submit**  | Redirects to all comments tamplate with your comment and other comments|





## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/Virsail/Life-Saver.git
  ```
2. Move to the folder 
  ```bash
  cd pitch
  
  ```
3. Running the application
  ```bash
  python3.8 manage.py server
  ```
4.Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)
* HTML
* Mako
Powershell
* Css
* Bootstrap

## Contact Information 

If you have any question or contributions, please email me at [mikeycharlesm7@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2019 **Owiti Charles**
