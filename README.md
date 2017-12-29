# IMDBScraper
I could not find any library that could scrape data off IMDB given advanced search filters. Here is my attempt at filling that void.
## How to install
This script uses scrapy, so that should be installed first. Also note these instructions are only for python3. You can get it using pip3/pip installer.

``` sudo pip3 install scrapy ```

Then clone this repository.

``` git clone https://github.com/Hallicopter/imdbscraper ```
### And that's it, it is installed!

## Usage
It is very easy to use this script. First cd into the directory (by default this will be your home directory.)

``` cd ~/imdbscraper ```

Then go to this imdb advanced search link [here](http://www.imdb.com/search/title).
Here you can enter all the filters you want and then hit search. You would be redirected to the search results page. Copy the URL of this page. For my example, I searched for IMDB top 100 movies. This is the link I got:

http://www.imdb.com/search/title?groups=top_100

Now open your terminal from the imdbscraper folderand enter this :

```` scrapy runspider imdb.py -o test.json -a search='http://www.imdb.com/search/title?groups=top_100'````

Here the ```` search ```` parameter is your starting page for the crawler to begin. The spider will continue crawling till it hits the end of the search result. The ```` -o test.json ```` is used to save the result in a json file called test.json. You can change this to whatever you want. 

## Format of the json file.
````python
[
  {
    "director": "Vittorio De Sica", 
    "imdb_link": "http://www.imdb.com/title/tt0040522/?ref_=adv_li_tt",
    "lead_actors": ["Lamberto Maggiorani", "Enzo Staiola", "Lianella Carell",
    "Elena Altieri"], 
    "film_name": ["Bicycle Thieves"]
  },
  {
   "director": "Charles Chaplin",
   "imdb_link": "http://www.imdb.com/title/tt0012349/?ref_=adv_li_tt", 
   "lead_actors": ["Charles Chaplin", "Edna Purviance", "Jackie Coogan", "Carl Miller"],
   "film_name": ["The Kid"]
  }
] 
````
## And that's it. 
A file containing the results of this example is there in the repository for you to checkout. I will try to add more features in future iterations of this script.
