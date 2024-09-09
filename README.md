# Coffee Shop Domain Modeling

## Objective

The goal of this project is to apply object-oriented programming principles to build a Python application that models a Coffee Shop domain. This assessment tests your ability to design classes, implement methods, establish relationships between objects, and handle data appropriately.

## Scenario

In this project, I modeled a Coffee Shop domain with three main entities:

**Customer:** Represents a person who can place orders.\
**Coffee:** Represents different types of coffee available for ordering.\
**Order:** Connects a Customer to a Coffee through an order, with a specific price.

The **relationships** are as follows:

A *Customer* can place many *Orders*.\
A *Coffee* can have many *Orders*.\
An *Order* belongs to one *Customer* and one *Coffee*.

## Project Structure

coffee_shop/\
├── customer.py\
├── coffee.py\
├── order.py\
├── debug.py\
├── Pipfile\
├── Pipfile.lock\
├── README.md\
└── tests/\
    ├──    -test_customer.py\
    ├──    -test_coffee.py\
    └──    -test_order.py

## Project Structure

### Directory Structure:
I created a new directory called coffee_shop to hold the project files.

### Virtual Environment:
I set up a virtual environment using pipenv to manage dependencies:

pipenv install\
pipenv shell

### Install Dependencies:
I installed pytest for testing:

pipenv install pytest

## Repository Link
https://github.com/code-iddih/task-phase-03-week-02-code-challenge

## Acknowledgement

Thanks to William Ayim - My Technical Mentor and Tutor.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
