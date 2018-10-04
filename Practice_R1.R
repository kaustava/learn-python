# first step clean the object list to free up ram
rm(list=ls())

# set working directory to save temp files , replace any backslash by forward slash
setwd("E:/DATA SCIENCE PREPERATION/EDWISOR/Dataset_library")

#verify working directory has been set correctly as desired
getwd()

#default sample dataset in R studio for practice.
df1 = mtcars

#take the data in a excel file
write.csv(data, "mt_cars.csv", row.names = TRUE)

write_xlsx(data,"mt_cars.xlsx", col_names = TRUE)
library(xlsx)

rm(list=ls())
write.xlsx(df1,"mt_cars1.xlsx", row.names = TRUE)
