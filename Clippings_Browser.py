#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import curses
from curses import wrapper
import re
import sys
import term as color
import os

data = 'data/export.txt'
quotes = {}
separator = ' -- '
location = 'loc.'
page = 'pg.'



def build_library(data):
    '''Builds clippings library from data (usually My clippings.txt)
    Returns quotes and sorted_quotes (sorted by number of quotes from source)'''
    with open(data, 'r') as file:
        for line in file.readlines():
            if not line.strip():
                continue
            else:
                try:
                    if page in line:
                        quote = line[:line.index(separator)]
                        source = line[line.index(separator)+2:line.index(page)-1]
                    elif location in line:
                        quote = line[:line.index(separator)]
                        source = line[line.index(separator)+2:line.index(location)-2]
                    else:
                        # print('\n \n could not parse source properly, leaving this one out')
                        continue
                    try:
                        quotes[source].append(quote)
                    except KeyError:
                        quotes[source] = [quote]
                except ValueError:
                    # print('Failed to parse quote:', line)
                    continue
    sorted_by_title_len = OrderedDict(sorted(quotes.items(), key=lambda x: len(x[0]), reverse = True))
    sorted_by_quotes_num = OrderedDict(sorted(quotes.items(), key=lambda x: len(x[1]), reverse = True))
    return quotes, sorted_by_title_len, sorted_by_quotes_num

def list_sources(quotes, sorted_quotes):
    for source in quotes:
        print(source)
    for i in sorted_quotes:
        print(i)

def search_by_source(term, data):
    '''Looks for search term among the sources (authors, books)
    Return matchin entries'''
    for source, quotes in data.items():
        if term.lower() in source.lower():
            os.system('clear')
            print(2*'\n', 7* '\t', 'Showing results for ', '"', term, '"')
            print(2*'\n', 6* '\t', '--- Showing 5 results per page. Press RETURN to continue. --- \n')
            for i in range(len(quotes)):
                if i!=0 and i % 5 == 0:
                    input()
                    os.system('clear')
                    print(2*'\n', 7* '\t', 'Showing results for ', term)
                    print(2*'\n', 6* '\t', '--- Showing 5 results per page. Press RETURN to continue. --- \n')
                i = quotes[i]
                i = color.format(i, color.green)
                print('\n -', i)

            
def main():
    quotes, sorted_by_title_len, sorted_by_quotes_num= build_library(data)
    if 'find quotes from author' in " ".join(sys.argv):
        author = " ".join(sys.argv[sys.argv.index('author')+1:])
        search_by_source(author, quotes)
    elif 'find quotes from book' in " ".join(sys.argv):
        book = " ".join(sys.argv[sys.argv.index('book')+1:])
        search_by_source(book, quotes)
    elif 'author' in sys.argv:
        if sys.argv.index('author')+1:
            author = " ".join(sys.argv[sys.argv.index('author')+1:])
            search_by_source(author, )
    elif 'book' in sys.argv:
        if sys.argv.index('book')+1:
            book = " ".join(sys.argv[sys.argv.index('book')+1:])
            search_by_source(book)
    
    
    
    sys.exit()

main()
    
    
def browse_clippings():
    '''Browse library interactively'''
    
def get_random_quote():
    '''Gets random quote from the entire library'''
    
def get_random_source():
    '''Return random book the library'''
        
def mark_as_favorite():
    '''Marks currently displayed quote as favorite'''

def get_favorites():
    '''Returns favorite quotes'''
    
def save_favorites():
    '''Saves favorites to .txt file'''
    
