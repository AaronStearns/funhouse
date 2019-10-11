# funhouse

#### Initial data exploration and visualizations done in R
#### Naive Bayes modeling done in Python

##### Data Exploration:

In order to better understand the variables `time`, `age`, `spider`, `sound`, and `ticket` I first visualized them to view frequency of occurence and observe patterns: 

![](/tixPlot.png)

It looks like the number of people who buy premium funhouse tickets and those who don't are roughly evenly matched. 

-------------------------------------------

![](/agePlot.png)

![](/hourPlot.png)

The age of the customers and time of day that the tickets were sold seem to both be fairly normally distributed.

-------------------------------------------

It can also be observed that some ages do purchase far more tickets than others:

![](/ageTixPlot.png)

-------------------------------------------

In order to understand the data better, it is best to create a table grouped by spider/sound/ticket purchase occurrences:

![](/tableSpiderSoundTicket.png)

At first glance of the raw frequencies, it would appear that when the spider is not working and the sound is working, a lot of people buy tickets. This might be because the spider has a physical presence whether it is working or not, but the sound must be working in order to be heard. 

However, it can also be seen that almost the exact same number of people (80 vs 81) DON'T buy tickets when the spider is working and the sound isn't. 

The hidden gem in this table seems to be that when both the spider and sound are working, the overwhelming majority of people currently attending the carnival will purchase premium tickets to the funhouse. (Raw frequency 52 purchases vs 12 non-purchases)

If the carnival is gearing up for its busy season, where presumably far more than 314 attendees will be present in a month, it might be wise to consider repairing both devices. To be more certain, I have calculated the conditional probabilities of ticket purchase likelihood given the working state of the spider and sound. 

Contained in this repository is a Python script 

