# funhouse

#### Objective:
To determine if a carnival funhouse operator should repair a faulty animatronic spider, a faulty spooky sound system, or both in order to attract more customers to purchase tickets.

#### Initial data exploration and visualizations done in R
#### Naive Bayes modeling done in Python

-------------------------------------------

#### Data Exploration:

In order to better understand the variables `time`, `age`, `spider`, `sound`, and `ticket`, I first visualized them to view frequency of occurence and observe patterns: 

![](/images/tixPlot.png)

It looks like the number of people who buy premium funhouse tickets and those who don't are roughly evenly matched. 

-------------------------------------------

![](/images/agePlot.png)

![](/images/hourPlot.png)

The age of the customers and time of day that the tickets were sold seem to both be fairly normally distributed.

-------------------------------------------

It can also be observed that some ages do purchase far more tickets than others:

![](/images/ageTixPlot.png)

However, for modeling, I will be dropping the `time` and `age` variables, as the funhouse operator cannot know when and if carnivalgoers with different ages will be in attendance. 

-------------------------------------------

In order to understand the data better, it is best to create a table grouped by spider/sound/ticket purchase occurrences:

![](/images/tableSpiderSoundTicket.png)

At first glance of the raw frequencies, it would appear that when the spider is *not* working and the sound *is* working, a lot of people buy tickets. This might be because the spider has a physical presence whether it is working or not, but the sound must be working in order to be heard. 

However, it can also be seen that almost the exact same number of people (80 vs 81) DON'T buy tickets when the spider is not working and the sound is. 

The main takeaway in this table seems to be that when both the spider and sound *are* working, the overwhelming majority of people in attendance will purchase premium tickets to the funhouse (raw frequency 52 purchases vs 12 non-purchases), and when neither device is working, the overwhelming majority will *not* buy funhouse tickets (raw frequency 17 purchases vs 45 non-purchases). At the same time, when one device is working and the other isn't, ticket purchase/non-purchase frequencies are nearly identical.

If the carnival is gearing up for its busy season, where presumably far more than 314 attendees will be present in a month, it might be wise to consider repairing both devices. To be more certain, I have calculated the conditional probabilities of ticket purchase likelihood given the working state of the spider and sound using the Naive Bayes formula.

-------------------------------------------

By running the Python script contained in this repo, it can be seen that the probability that a carnivalgoer purchases a funhouse ticket given that the spider and sound are working is: **81.96%**

The probability that they do *not* purchase a funhouse ticket when both devices are working is **23.61%**

Therefore, depending on the expected increased attendance in the following 30 days, a total repair cost of $80 for both devices might be offset by high attendance rates, given the high probability of carnivalgoers to purchase tickets when both devices are working.
