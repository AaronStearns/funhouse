library(tidyverse)
library(lubridate)

df <- read.csv("/data/funhouse_data.csv", stringsAsFactors=FALSE)
df$time <- hm(df$time)
df$hour <- hour(df$time)


df %>%
  group_by(age) %>%
  summarise(totals = n()) %>%
  ggplot(aes(x = age, y = totals, fill = "red")) +
  geom_bar(stat = "identity", alpha = 0.95) +
  ggtitle("Total attendees by age") + 
  theme_bw() + 
  theme(legend.position="none") 


df %>%
  group_by(ticket) %>%
  summarise(totals = n()) %>%
  ggplot(aes(x = ticket, y = totals, fill = ticket)) +
  geom_bar(stat = "identity", alpha = 0.95) +
  ggtitle("Tickets purchased") + 
  theme_bw() +
  theme(legend.position="none") 


df %>%
  group_by(hour) %>%
  summarise(totals = n()) %>%
  ggplot(aes(x = hour, y = totals, fill = "red")) +
  geom_bar(stat = "identity", alpha = 0.95) +
  ggtitle("Tickets purchased by hour") + 
  theme_bw() + 
  theme(legend.position="none") 



df %>%
  group_by(ticket, age) %>%
  summarise(totals = n()) %>% arrange(desc(age)) %>% 
  ggplot(aes(x = ticket, y = totals, fill = ticket)) +
  geom_bar(stat = "identity", position = "dodge", alpha = 0.95) +
  facet_wrap(~age) +
  ggtitle("Purchased/Not Purchased by age") + 
  theme_bw() + 
  theme(legend.position="none") 


df %>%
  group_by(spider, sound, ticket) %>%
  summarise(totals = n()) %>%
  arrange(desc(totals))

###################################################
