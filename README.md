# Interview Test Server

For the Points developer take-home assignment, the following task is required: you are to build a tax calculator against
 this API. The purpose is to develop an income tax calculator to help illustrate how marginal taxes work. This server is
  pretty simple, only returning the tax rates for a given year. You are to calculate the amount of taxes owed by 
  inputting a yearly salary, then displaying the different rates, the total amount owed and the effective tax rates.

For all of the below assignments there are different levels that you can work on:
 * **Level 1:** The easier level, the API always behaves and the response never changes.
 * **Level 2:** More difficult, the API doesn't always behave and includes gotchas.
 
If you complete the first level with ease, feel free to jump to the next one. 

**Please timebox your solution to one day total.**

## Assignment 1: Tax Calculator

### Instructions

* Download and run this server (see [Getting Started](#getting-started))
* Build an application / tool in React or Python with the following criteria:
    * Fetches the tax rates from this API server
    * Takes a yearly salary as input
    * Calculates and displays the total taxes owed for the salary
    * Displays the amount of taxes owed per band
    * Displays the effective rate

### Level 1

* Fetch the tax rates from this server at: [localhost:5000/tax-calculator/brackets](http://localhost:5000/tax-calculator/brackets)

### Level 2

* Fetch the tax rates by year: [localhost:5000/tax-calculator/brackets/<2019,2020...>](http://localhost:5000/tax-calculator/brackets/2020)

_Warning: this endpoint has gotchas_

## Assignment 2: Autonomous Car

### Instructions

* Download and run this server (see [Getting Started](#getting-started))
* Build an application / tool in React or Python with the following criteria:
    * Fetches an autonomous car route from this API server
    * Determines if the route was a success or a failure
    * If the route results in a failure, determine the cause as well as the step and position where the failure occurred
  
### Level 1

* Fetch a successful autonomous car route from this server at: [localhost:5000/autonomous-car/routes/](http://localhost:5000/autonomous-car/routes/)

### Level 2

* Fetch a random autonomous car route by status: [localhost:5000/autonomous-car/routes/random](http://localhost:5000/autonomous-car/routes/random)

_Warning: this endpoint has gotchas_


## Getting started

```bash
docker pull ptsdocker16/interview-test-server
docker run --init -p 5000:5000 -it ptsdocker16/interview-test-server
```

Navigate to http://localhost:5000. You should see a brief set of instructions. From there you'll be able to query the above endpoints and do your assignments. If you have any problems, email the Team Lead or Engineering Hiring Manager for assistance.

## Submission Instructions

You can either submit your code as a zip file or send a link to a personal repository. Do not fork or submit pull requests to this repository. Please submit within a week or 2 of receipt of instructions, unless otherwise specified.

Please *do not fork or submit pull requests* to this repository.

Please timebox your solution to one day total.

* Implement your solution using JavaScript or Python.
* Include comments where you feel that they would be helpful.
* Include a README with instructions on how setup, run, and test the application.
* Include unit tests.

**If using JavaScript**

* Create a simple, yet visually appealing and responsive design.
* Target the latest stable version of Google Chrome.
* Format the code according to the latest eslint specs

**If using Python**

* Implement a simple yet intuitive command line interface.
* Format the code following PEP8 guidelines