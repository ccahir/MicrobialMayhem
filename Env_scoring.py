#!/usr/bin/env python3
import sys
import re

##Class to define environments
##1. Ph [high vs low]
##2. Temp [high vs low]
##3. Salinity [high vs low]

##Create dictionary of values to assign incase the environment == True or ==False
##Most bacteria are neutrophiles hence 0 ...Acidophiles[-10] and alkaliphiles [+10]

##Thermophile can survive well in high temp (hence the reasone some of their enzymes are used for experiment e.g. Taq polymerase in PCR), Low temp slows most bacteria down unless they are cryophiles that do well in low temp, and then there is rtp


##Halophiles can tolerate extreme salinity
env = input("Where do you want to fight? Choose your Environment")
def calculate_score_env(env):
  Extreme = ('Alkaline','Hot','Cold','Acidic','Salty')
  Value_of_Env ={'extreme':-10, 'neutral':0}
  if env in Extreme:
    score = Value_of_Env['extreme']
  else:
    score = Value_of_Env['neutral']
  return score
##End of Class
Total_object = calculate_score_env(env)
print('Here is the score for each line checked', Total_object)
