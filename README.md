# Assignment 1 - Designing Models and Analyzing Data 
(remove: **text between brackets to be removed**)

> * Participant name: Lauren Massey
> * Project Title: (Title of the problem you are looking and modeling)

# General Introduction

The first part of this assignment explores designing models (and basic Python/Git features). 

We will look at **subway model in a city** system. A **subway system** is an underground, tube, or metro, underground railway system used to transport large numbers of passengers within urban and suburban areas - modern subways use different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently. 

The second part of the assignment explores data analysis. Data analysis and visualization is key to both the input and output of simulations. This assignment explores different random number generators, distributions, visualizations, and statistics. Additionally, it will look at getting you accustomed to specifying input and output variables to a system. We will also practice working with real data.


# Part 1: Designing a Model - Subway System

New York City has an estimated population of 8,398,748, as of July 2018, that live within 306 square miles [1][2]. This creates a population desnisty of about 27,443.06 people per square mile][2]. The resulting congested streets of NYC have lead to the usage of an underground subway system. This subway system is a common way to travel efficently through the NYC and consists of 472 stations that serve 27 subway lines [2]. It is estimated that the average day rideship for the NYC subways system is 5,437,587 people[4]. The US Census Bureau estimates that NYC's population will continue to grow at a rate of 3% each year or approximately a population growth os 27,000 persons[1]. This evergrowing population will consquently put more demand on the NYC subway system.

The NYC subway system uses escalators to transport riders to and from the underground platforms. Of the 472 stations, 59 have escalators[5]. The direction of an escalator at a certain time can reduce the congestion a station may expereince, especially during rush hour. With the increasing popultion of riders in NYC, usage of these escalators need to be optimatized to ensure efficent transportation through the NYC subway system. A discrete-simualtion of rideship at stations with escalators could be used to model the direction of escalators and throughput of riders. This practice of changing the direction of the escalators is not uncommon and is used often when peak transit of people will be going in the same directions, such as exiting a sport stadium after a game.

The Metropolitan Transportation Authority (MTA) generates data multiple times a day on the amount of riders that have entered and exited a certain station via the turnstiles[5]. The data is collected nine times a day: 12am, 4am, 8am, 12pm, 4pm, 8pm. This data will be useful in the simualtion to know the throughput at subway stations at certain time intervals.

![Image of Subway City System](images/subway_turn.png)[6]

Also, MTA produces performance data about the percentage of time each escalator is fully functioning[5].  This can be used to simulate the strain of travel when an escalator is down and what should be done with the remaining escalators at that station [5].

![Image of Subway City System](images/escalator.png)[7]

References
1. https://www1.nyc.gov/site/planning/planning-level/nyc-population/current-future-populations.page
2. https://www.newworldencyclopedia.org/entry/New_York_City
3. http://web.mta.info/nyct/subway/howto_sub.htm
4. http://web.mta.info/nyct/facts/ridership/
5. http://web.mta.info/developers/developer-data-terms.html#data
6. https://truthout.org/articles/arrested-for-jumping-a-turnstile-how-new-york-city-punishes-the-poor/
7. https://thecity.nyc/2019/07/nycs-second-avenue-subway-escalators-fail-to-rise-report.html


## (Part 1.1): Requirements (Experimental Design) **(10%)**
####Problem
The throughput of riders in the NYC subway system can get congested at certain time intervals in a day. Optimizing the direction of the subway escalators may alleviate some of the congestion by providing more paths in a desired direction during peak hours. 
####Requirements

(remove: You should start by specifying a set of requirements. I specified a topic a Subway escalator. What exactly does that mean - practice formulating your own set of requirements and an experiment. Define problems cities face and hypothesize how a subway system could help alleviate these issue. This helps you think about your problem communication and system objectives inputs, functions, and outputs - they should be clearly specified.)

## (Part 1.2) Subway (My Problem) Model **(10%)**

(remove: add a high-level overview of your model, the part below should link to the model directory markdown files)
(remove: Look at the [**Object Diagram**](model/object_diagram.md) for how to structure this part of Part 2 for each diagram. Only the Object diagram has the template, the rest are blank. )

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of (what are you providing details of)
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## (Part 1.3) Subway (My Problem) Simulation **(10%)**

(remove: Describe how you would simulate this - including type of simulation, rough details, inputs, outputs, and how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)


## (Part 1.4) Subway City (My Problem) Model **(10%)**
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)
You are expected to create the python files - the code should run without errors, create and object(s) for your system, but not provide function detail.



## (Part 1.5) Specifying the Inputs to a System **(10%)**

(remove the below points once ideas are satisfied)
* Specify the independent and dependent input variables of your subway esclator model
* Specify where the data will come from measured subset of real data (empirical) or synthetic data
* What kind of statistics are important to capture this input data
* How do you plan to analyze the output of your model?
* What ways will you visualize your data - charts, and graphs you will create?
* What clever way will you visualize your output with a useful infographic?



# Part 2: Creating a Model from Code

## (Part 2.1) **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model **(10%)**
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template for the code found in  [**the following folder**](code/POTS_system/).



# Part 3: Data Analysis

## (Part 3.1) - Real Data **(10%)**

Find a datasource that looks at part of this model - subway stations locations / escalator number, heights, widths / volume of passangers - ridership numbers   (*fits* - we are pretty loose here, it can be anything.)

* Write up a paragraph that describes the data and how it fits into your system.
* Load the data into Python
* Calculate a few useful statistic on the data - keep it simple- STD, means, etc..., this is just designed * to get used to working with real data. Explain the insights you derive from these statistics.
* Visualize the raw data - visualize a few critical aspects of the data to better describe what it is, what it is showing, and why its useful to your system.
* Calculate and plot some summary statistics that better describe the data.

(Add your plots and visualization here)
(Put your data into the data directory)


## (Part 3.2) -  Plotting 2D Random Number Generators **(15%)**

This portion of the assignment looks at generating random numbers in Python and understanding how to properly plot them. Plot two different random numbers, pseudo random and quasi random, for five different N values. There should be 10 subplots, all properly formatted 2D plots. Note, each of the N points will have two coordinates, an x and a y, therefore you will need to generate two random numbers for each point. You should replace the image with your results in a simalar format. Discuss how the patterns differ. Feel free to change the N values from the suggested N values in the image to state your case.

![Image of 2d template City](images/2Dtemplate.png)


## (Part 3.3) -  Plotting 1D Random Distributions **(15%)**

Now, choose three different distributions to plot in 1D, or as a histogram. Choose a pseudo-random generator and generate three different distributions. Example distributions are Uniform (part 8), Normal, Exponential, Poisson, and Chi-Squared, but feel free to use any three distributions of your choice. Again, plot each distribution for five different Ns. This will result in 15 different subplots, formatted similar to the image in Part 8. Include your properly formmated 1D plots below and breifly describe what we are looking at and how things change as N is changed.

Repeat the above using a quasi-random generator. Discuss the similarities and differences.
