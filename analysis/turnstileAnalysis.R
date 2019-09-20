install.packages("dplyr")
install.packages("ggplot2")
install.packages("reshape2")
library (dplyr)
library (ggplot2)
library (reshape2)


turnstile = read.csv("TurnstileFull.csv")
stationNames = read.csv("stationNames.csv")

turnstile = turnstile[,-c(1:4,6,7,10)]
stationNamesFinal<-na.omit((stationNames))
actualStations = as.data.frame(subset(turnstile, STATION %in% stationNamesFinal$STATION))
#actualStations = actualStations[,-c(1:4,6,7,10)]

stationDailyAverage <- actualStations%>% 
  group_by(STATION, DATE)%>%
  summarize(averagePerDayEntries = mean(ENTRIES),averagePerDayExits = mean(EXITS))

stationDaily <- actualStations%>% 
  group_by(STATION, DATE)%>%
  summarize(totalPerDayEntries = sum(as.numeric((ENTRIES))), totalPerDayExits = sum(as.numeric(EXITS)))

stationTotals <- actualStations%>% 
  group_by(STATION)%>%
  summarize(totalYearlyEntries = sum(as.numeric((ENTRIES))), totalYearlyExits = sum(as.numeric(EXITS)))

stationAvgTotals <- actualStations%>% 
  group_by(STATION)%>%
  summarize(totalAvgYearlyEntries = mean(as.numeric((ENTRIES))), totalAvgYearlyExits = mean(as.numeric(EXITS)))

shortListAvgTotal = stationAvgTotals[-(16:59),]
stationAvgTotalMelted <-melt(shortListAvgTotal, id.vars="STATION")

overallStationAvg = ggplot(stationAvgTotalMelted, aes(STATION, value))+
  geom_bar(aes(fill=variable), stat="identity", position = "dodge") + theme(axis.text.x = element_text(angle=30, hjust=1))+
  labs(y= "Total Number of People through Turnstile", title = "Total Number of Turnstile Entries and Exits for 15 Subway Stations")+
  scale_fill_discrete(name="Turnstiles", labels=c("Entries", "Exits"))
print(overallStationAvg)

shortListNumEscalators = stationNamesFinal[-(16:59),]
numEscl = ggplot(shortListNumEscalators, aes(STATION, NumEs))+geom_bar(aes(fill=UpTime), stat="identity")+ theme(axis.text.x = element_text(angle=30, hjust=1))+
  labs(y= "Number of Escalators per Station", title = "Total Number of Escalators and Percentage of\nTime All Working for 15 Subway Stations")+
  scale_fill_continuous(name="Precentage of Time\nAll Escalators Working")
print(numEscl)

write.csv(shortListAvgTotal,file="ShortListStationAvgTotal.csv")
write.csv(shortListNumEscalators,file="ShortListNumEscalators.csv")
