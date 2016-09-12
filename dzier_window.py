# Script name: weather.py
# Author: Dan Burke
# Date created: 10 Sept 2016
# Description: Pull weather data and notify if conditions
#              are pleasant enough to open windows
# Parameters: zipcode - 5-digit integer
# Syntax: python weather.py zipcode

# Import library to read HTML pages
import urllib
# Import library for regular expressions
import re, sys, datetime

# Read in zipcode
zip = sys.argv[1]

# Get current time
now = datetime.datetime.now()

# Read weather site to get current pollen level
sock = urllib.urlopen("https://www.wunderground.com/DisplayPollen.asp?Zipcode=" + zip)
pollen_vals = []
for line in sock:
    line = line.rstrip()
    pollen_levels = re.findall('<p>\d\.\d\d</p>',line)
    if len(pollen_levels) > 0:
        pollen_val = re.findall('\d\.\d\d',line)
        pollen_vals.append(pollen_val)

curr_pollen_level = pollen_vals[0][0]

# Read weather site to extract current temperature
sock2 = urllib.urlopen("https://www.wunderground.com/cgi-bin/findweather/getForecast?query=" + zip)
for line in sock2:
    line = line.rstrip()
    humidity = re.findall('\"humidity\":\d+',line)
    if len(humidity) > 0:
        humidity_val = re.findall('\d+',line)[0]
    temp = re.findall("temp_now:",line)
    if len(temp) > 0:
        temp_val = re.findall('\d+\.\d',line)[0]

# Output values to screen
print "Current weather conditions for " + zip
print "Last update: ", now, "\n"
print "Current temperature: " + temp_val
print "Current humidity: " + humidity_val + "%"
print "Current pollen level: " + curr_pollen_level


# Output values to screen
print "Current weather conditions for " + zip + "\n"
print "Current temperature: " + temp_val
print "Current humidity: " + humidity_val + "%"
print "Current pollen level: " + curr_pollen_level
