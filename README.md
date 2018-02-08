# chinese-childrens-libraries
A project to build a current map of 绘本馆 --subscription children's libraries in China.

file scrape.py is the current version of the code.

# Project Contributors
* Raleigh
* Angela
* Josue
* JJ
* Connie
* Steven

# Project Outline/Schedule
### Week 1
* sign up for an api key
**they never replied.  We'll need to screenscrape**
* decide on a language
**are we going to split into 2 groups?**


### Week 2
* worked on getting our Python environments to work
* make sure you are installing packages into the right version of python!
* spoofed a web client and scraped a page from dianping.com
* we figured out that calling different URL's, calls different cities.  https://www.dianping.com/search/keyword/26/0_[string] #26 is a city code.  #1 = Shanghai #2 = Beijing #3 = Hangzhou

### Week 3 
* code goal: figure out how to send a query to dianping
J-search-input is the element name of the keyword search bar.
* load query results into a data frame

### Week 4
* format the results more carefully -- explore our data.
* code goal: figure out how to loop over a list of cities
* work on compiling query results into a workable table
* how does dianping treat locations?  lat-long pairs or street addresses?
* if addresses, how do we batch geocode Chinese addresses?

### Week 5
* compile tables and join to addresses
* prepare other data for analysis (Chinese Census info from CD-ROM and Provincial Statistical Yearbooks @ UMichigan) 

### Week 6
* exploratory visual GIS analysis

### Week 7
* 
