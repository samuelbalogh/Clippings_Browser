## Clippings Browser

A simple command line app for Unix systems to browser your Kindle clippings, written in Python.

### Background

I wanted a program that can quickly sort my clippings and display them in a simple way. 

The script can parse two types of data.

1. The raw format of your Kindle clippings file, found in the 'documents' folder of your Kindle. Usually named *My_clippings.txt.*
This file uses multiple lines for a clipping and uses '========' as the separator.
2. The format from clippings.io (a good service, by the way, just not enough). They use '--' as separator and clippings take up a single line.


### Usage

#### Get quotes from author/book

```
$ python Clippings_Browser.py find quote from book you are not so smart
```

Output:
```
             Showing results for  " you are not so smart " 		 
 
   	  - - -  5 results per page. Press RETURN to continue. - - -, 

 Showing quotes from: - David McRaney, You Are Not So Smart 



 - Yet you lock your keys in the car. You forget what it was you were about to say. You get fat. You go broke. Others do it too. From bank crises to sexual escapades, we can all be really stupid sometimes.

 - the world around you is the product of dealing with these biases, not overcoming them.

 - Your brain is better at seeing the world in some ways, like social situations, and not so good in others, like logic puzzles with numbered cards.

 - You have a deep desire to be right all of the time and a deeper desire to see yourself in a positive light both morally and behaviorally.

 - You have a deep desire to be right all of the time and a deeper desire to see yourself in a positive light both morally and behaviorally. You can stretch your mind pretty far to achieve these goals.
```

    
#### Get random quote from author/book

```
$ python Clippings_Browser.py get random quote from Scott Adams
```


Output:

```
                Showing results for  " scott adams " 		 
 
   	  - - -  5 results per page. Press RETURN to continue. - - -, 
 
 Showing quotes from: - Scott Adams, How to Fail at Almost Everything and Still Win Big: Kind of the Story of My Life 



 - When I combined my meager business skills with my bad art skills and my fairly ordinary writing talent, the mixture was powerful.
 
 
 
  Press RETURN to continue . . . 
```

