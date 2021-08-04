# web-scraping-challenge
Web Scraping Assignment - Milinda 'ML' Liyanage

## Summary

* This assignment was done in three steps.
* First step was to scrape the data using a jupyter notebook.
* Second step was to convert the jupyter notebook into python code.
* As the third step, the scraped data is then saved into a mongo DB and rendered on to a web browser.

### The following tasks were done for the first step, jupyter notebook: 

* A jupyter notebook was created for coding and testing.
* Used Spliter, BeautifulSoup and Webdriver to get to the webpages and collect the data.
* Pandas was used to store table data.
* Four websites were scraped for text, images & tables.
* The table data was read in to data frame and cleaned.
* The collected data was then put in dictionaries.
* The cleaned data frame (table data) was converted to HTML table format prior to saving.
* A single dictionary was created at the end of scraping with 4 pairs of the scraped data.
* The created jupyter notebook is called [mission_to_mars](Missions_to_Mars/mission_to_mars.ipynb).

### The following tasks were done for the second step, creating python code: 

* A new python file called [scrape_mars](Missions_to_Mars/scrape_mars.py) created. 
* The jupyter notebook code was converted to python functions.
* 4 separate functions were created to scrape the individual websites.
* A main function was created to call the 4 functions. This function would be called from the main app.


### The following tasks were done for the third step, creating an app: 

* A new python file called [app](Missions_to_Mars/app.py) created. 
* As required two routes were created for the application.
* One route to scrape the data and save in to a mongo DB.
* The other route to read and render the data on to the web browser.

### Generated files: 

#### jupyter notebook
* [mission_to_mars](Missions_to_Mars/mission_to_mars.ipynb).

#### python
* [scrape_mars](Missions_to_Mars/scrape_mars.py)
* [app](Missions_to_Mars/app.py)

#### HTML pages
* [index](Missions_to_Mars/templates/index.html)

#### CSS
* [style](Missions_to_Mars/static/css/style.css) 

#### Images
* [Scraped Information](Images/scraped_information.png)



