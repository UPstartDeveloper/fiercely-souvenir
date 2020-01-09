![Travelly Logo](https://travelly-files.s3.us-west-1.amazonaws.com/images/Screen%20Shot%202020-01-06%20at%209.21.14%20AM.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMSJIMEYCIQC2oRvUO1sJsD%2ByvU78xhB1qiWz%2FUrmDxELhwcV4K%2Fz0AIhAJSoVgD0hVSD50O8VfhB9PTEK%2B3WS9r1ZAfIJik2NKzIKpYCCNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMDExODA1MTE5MTMwIgxLIgCeBsI0LPZ9Tngq6gHOO8glFo9IaFtaOd6IXKO72SSeGcxFmj3RK5fQRWInwHzwf7WihcNfXmyq8bI%2FuGE%2FzyD%2Bs0tBKY6fmcIQYK4AGMEsyQULCU2sTSgsFVFY2AatXXhswICSNzmF5DDdXJFwumTYx5iTLjbefpCgHS9HBlJajh2ZxM6Cr4YL7IC0mZl9YyJao3hOTYBYUpav5nOuTddyfIYsNXeIGSmq48kTohKvOiRmt%2F0OsMxw1qSh18SWl4eidwx4L%2BwvNgFbHajW0zvng52CTETQShOUBU6rfKGF4AU5BFPK%2BH9JPVlfxQw8BS7LruLJd2Uw4%2Brd8AU6gQM8Fj2%2BJkumPkGaMpGMYSR29hubEjdzXK7MKxme%2BFi%2B03WSIgaiq629juRBIrMwKp0TuN5d7pcqSct92OrigIJXy154l62PhQR5TLC9UCd1PTN8iUcBkXwLY1XeBRsyknCCsxm%2FnJdWH1mWHd5lWkvx7VU0jJhW3xCRmZQFi9qL02CJdJvvJNh7wo1WvNzxnVWVRafAwba13qOwzYjwVOHZS6ByllVQmNYvnrAIq%2BvsCVa2t8NEtJWy%2Bi1nttoVv3LhzN55rw39mG1sjKDavGgee0MNYN7E65OdgNBEKSNyA28MgxF4W8BNvV%2FBkRH%2BQq%2BudHa%2BsxwRPZ06Ke4CmR8zGNEZjfJgybXyc9DrIQJs7LdfOepOy%2Bi%2BfHQHh1fOoEZSvVjBUDXUzlqyHPG7uXMeUhcCpeVH1XIzfA3O3YwtKY4SwsXeSAd3z7G4rPk4TsluSNdiV1sX6xGwCYGPOqY6FxJpDSFbh%2FMa78WvwSvQohVLyoKgzwCsOs91qTe83e6p&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200109T184838Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQFP5D2KNLNALNHPP%2F20200109%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=1e081c64aa88ec8718ffd3295f39f5862f24be30752205b118a4c3cbf9442692)

# Travelly
## Table of Contents
1. [Why Travelly?](#why-travelly?)
2. [Technical Write-Up](#technical-write-up)
3. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [How to Contribute To This Project](#how-to-contribute-to-this-project)
    - [Installing Requirements](#installing-requirements)
4. [Running the Tests](#running-the-tests)
5. [Tech Stack](#tech-stack)
6. [Authors](#authors)
7. [License](#license)
8. [Acknowledgements](#acknowledgements)

## Why Travelly?
[See it Now (link to deployed version)](https://travelly-zr.herokuapp.com)
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

### Installing Requirements
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

## Tech Stack
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
