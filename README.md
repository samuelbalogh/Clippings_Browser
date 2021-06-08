## Clippings Browser

A simple command line app for Unix systems to browser your Kindle clippings, written in Python.

### Background

I wanted a program that can quickly sort my clippings and display them in a simple way. 

The script can parse two types of data:

1. The raw format of your Kindle clippings file, found in the 'documents' folder of your Kindle. Usually named *My_clippings.txt.*
This file uses multiple lines for a clipping and uses '========' as the separator.
2. The format from clippings.io (a good service, by the way, just not enough). They use '--' as separator and clippings take up a single line.


### Quickstart

1. Clone repo
2. Install requirements: `python -m venv env; . ./env/bin/activate; pip install -r requirements.txt`
3. Replace `data/my_clippings.txt` with your clippings library (it can be found in the documents folder of your Kindle). If you are using clippings.io, you can export your clippings using their format. In this case, name your file `export.txt`.
4. Run `$ python Clippings_Browser.py [author name]`
5. Enjoy.

### Usage

```
positional arguments:
  QUERY                 the source of the clippings: author, book title,
                        article title, etc.

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_OF_CLIPPINGS, --number_of_clippings NUMBER_OF_CLIPPINGS
                        number of clippings to display per page
  -l, --list            view list of sources (authors and books)
  -r, --random          get random clipping
```


##### Get quotes from author/book

```
$ python Clippings_Browser.py Scott Adams -n 3
```

Output:
```
Press Ctrl + C to exit...

 Showing results for  " Scott Adams " 		 
 3 results per page.  


 Showing clippings from: 
 Scott Adams, How to Fail at Almost Everything and Still Win Big: Kind of the Story of My Life 


 * All I know for sure is that I pursued a conscious strategy of managing my opportunities in a way that would make it easier for luck to find me.


 * Passionate people who fail don’t get a chance to offer their advice to the rest of us. But successful passionate people are writing books and answering interview questions about their secrets for success every day. Naturally those successful people want you to believe that success is a product of their awesomeness, but they also want to retain some humility. You can’t be humble and say, “I succeeded because I am far smarter than the average person.” But you can say your passion was a key to your success,

 * Success caused passion more than passion caused success.

                                                                      Press RETURN to continue 
             
```

    
##### Get random quote from author/book

```
$ python Clippings_Browser.py Chris Hadfield -r
```


Output:

```
 Press Ctrl + C to exit...

 Showing results for  " Hadfield " 		 
 5 results per page.  
 

 Showing clippings from: 
 Chris Hadfield, An Astronaut's Guide to Life on Earth 


 * The life of an astronaut is one of simulating, practicing and anticipating, trying to build the necessary skills and create the correct mind-set.


 * the North American subculture of pretense, where watching Top Chef is the same thing as knowing how to cook.

 * Beatles’ “Here Comes the Sun”

 * just the pleasantly selfish simplicity of being responsible only for myself.

 * stern taskmaster


                                                                      Press RETURN to continue . .

```

