# funhouse

Initial data exploration and visualizations done in R
Modeling done in Python

### Data Exploration:

In order to better understand the variables `time`, `age`, `spider`, `sound`, and `ticket` I first visualized them to view frequency of occurence and observe patterns: 

![](/tixPlot.png)

It looks like the number of people who buy premium funhouse tickets and those who don't are nearly evenly matched. 

-------------------------------------------

![](/agePlot.png)

![](/hourPlot.png)

The age of the customers and time of day that the tickets were sold seem to both be fairly normally distributed.

-------------------------------------------

It can be observed that some ages do purchase far more tickets than others

![](/ageTixPlot.png)

-------------------------------------------

In order to understand the data better, it is best to create a table to group by and summarize spider/sound/ticket purchase occurrences

![](/tableSpiderSoundTicket.png)

At first glance of the raw frequencies, it would appear that when the spider is not working and the sound is working, far more people buy tickets than when the spider is working and the sound is not. 
