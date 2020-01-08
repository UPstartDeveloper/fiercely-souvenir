# Travelly
#### [See it Now (link to deployed version)](https://travelly-zr.herokuapp.com)
If you love to travel, there's no better time to be alive. The travel industry is on the rise, but how do we ensure that travelers enjoy their experiences with airports and airlines?
Travelly is an online travel tool that helps first-time fliers navigate the airport, and connects them with amazing airlines.

## Technical Write-Up
To learn the why and how behind Travelly, please read [my Technical Writeup on Medium](https://medium.com/@zain_raza/break-through-airport-confusion-lost-at-the-airport-part-2-d4867452c9c2).

## Getting Started
### Prerequisites
- Must have Git installed
- Must have a GitHub account
- Must have Python 3.7.* installed
- Must know how to work in a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/)
(Docker should work as well, I've just never used it before)

### How to Contribute To This Project:
These instructions will help you get a copy of the repository up and running on your local machine.
- Fork this repository (click the "Fork" button at the top right of the page, then click on your profile image).
- Clone your forked repository onto your local machine
```
git clone https://github.com/<YOUR_GITHUB_USERNAME>/fiercely-souvenir.git
```
- Start your virtual environment, and be sure to see the 'Installing Requirements' section below to make sure you have all the required dependencies!

- Create a new branch for the feature you want to work on, or the bug fix you want to make:
```
git checkout -b feature/branch-name or bugfix/branch-name
```
- Make your changes (be sure to commit and push!)
```
git add .
git commit -m "[YOUR COMMIT MESSAGE HERE]"
git push origin branch-name
```
- Don't forget to add yourself to the [CONTRIBUTORS.md](CONTRIBUTORS.md) file!
Please credit your own work, by adding your name to the list in this format:
```
Name: [YOUR_NAME](Link to your GitHub Account, social media, or other personal link)
About Me: 2-3 sentences to introduce yourself
Feature: What did you contribute?
Technologies: What did you use to build your contribution?
Fun Fact: optional trivia about yourself!
```
- Create new Pull Request from your forked repository - Click the "New Pull Request" button located at the top of your repo
- Wait for your PR review and merge approval!
- If you care about this work, then I humbly ask you to **please star this repository and spread the word with more developers! Thank you!**

#### Installing Requirements
To ensure you have a development experience that's **as smooth as possible**, please follow these instructions:

- Once you have activated your Python virtual environment, please be sure to run the following command from the command line, to ensure you have all the dependencies
you may need to use for this project:
```
python -m pip install -r requirements.txt
```
- You may always double check the dependencies you have using this command:
```
python -m pip list
```
- If you install any new dependencies, please be sure to record them using
```
python -m pip freeze > requirements.txt
```
Thank you in advance for contributing to this project!

## Running the Tests
Within the `fiercely-souvenir/travelly` directory, you can run the tests for this project from the command line, using:
```
python manage.py test
```
If you would like to add tests of your own and don't know how, please be sure to read the [Django 3.0 documentation on testing](https://docs.djangoproject.com/en/2.2/topics/testing/overview/#).
If you are writing tests for the `api` package, you may also like to consult the [Django REST Framework documentation](https://www.django-rest-framework.org/api-guide/testing/).

## Built With
- Django - web framework for the backend
- Bootstrap 4 - styling the front end
- PostgreSQL - production database schema
- Django REST Framework - framework building the API (found in the [explorer_buddy.explorer.api package](/explorer_buddy/explorer/api/)).
- AWS S3 - file storage for image uploads
- Gmail - email server

## Authors
1. **Zain Raza** - *Initial work* - Make School Student, Data Science Concentration
    * Want to see more? Take a peek at Zain's entire portfolio, at [https://www.makeschool.com/portfolio/Syed-Raza](https://www.makeschool.com/portfolio/Syed-Raza).


## License
This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for more details.

## Acknowledgements
- Mom and Dad - Thank you both for the sacrifices you have made for our family. I have been traveling on planes
since I was two years old, and it is all thanks to your commitment to giving us a better life.
- [Django Software Foundation](https://www.djangoproject.com/) - This project's backend is built off the Django web framework for Python.
Thanks so much for all the open source contributions you guys are making!
- Dani Roxberry and Meredith Murphy (Make School BEW Instructors) - thank you both for helping me learn how to use the Django Web Framework!
- Billie Thompson - inspired this README.md file with her amazing [README.md template on GitHub Gist!](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
