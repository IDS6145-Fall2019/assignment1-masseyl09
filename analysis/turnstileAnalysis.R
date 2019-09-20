

turnstile = read.csv("TurnstileFull.csv")
stationNames = read.csv("stationNames.csv")

turnstile = turnstile[,-c(1:4,6,7,10)]
stationNamesFinal<-na.omit((stationNames))
actualStations = subset(turnstile, STATION %in% stationNamesFinal$STATION)
actualStations = actualStations[,-c(1:4,6,7,10)]


