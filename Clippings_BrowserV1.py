#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import curses
from curses import wrapper
import re
import sys
import term as color
import os

data = 'data/export.txt' # exported from clippings.io
clippings = 'data/my_clippings.txt'  # original Kindle clippings format
quotes = {}
separator = ' -- '
location = 'loc.'
page = 'pg.'

quotes2 = {}

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
    
    with open(clippings, 'r', encoding='utf-8') as file:
        file = file.read()
        file_as_list = file.split("==========")
        clippings_list = []
        for entry in file_as_list:
            if 'Your Highlight' in entry:
                entry = entry.split('\n')
                clippings_list.append(entry)
                
    for i in clippings_list:
        source = i[1]
        if source[0] == '\ufeff':
            source = source[1:]
        highlight = i[-2]
        try:
            quotes[source].append(highlight)
        except KeyError:
            quotes[source] = [highlight]
            
           
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
    title_text = " ".join([2*'\n', 2* '\t', 'Showing results for ', '"', term, '"', 2* '\t'])
    subtitle_text = " ".join([2*'\n', '  \t', ' - - -  5 results per page. Press RETURN to continue. - - - \n'])
    title = color.format(title_text, color.red)
    subtitle = color.format(subtitle_text, color.red)
    for source, quotes in data.items():
        if term.lower() in source.lower():
            os.system('clear')
            print(title)
            print(subtitle)
            print(5 * '\n')
            for index in range(len(quotes)):
                if index!=0 and index % 5 == 0:
                    input()
                    os.system('clear')
                    print(title)
                    print(subtitle)
                    print(5 * '\n')
                quote = quotes[index]
                quote = color.format(quote, color.green)
                print('\n -', quote)
                if str(index)[-1] == '4' or str(index)[-1] == '9':
                        text = 'Press RETURN to continue . . . '
                        text = color.format(text, color.blink)
                        print(5 * '\n', text)
                
          
def main():
    quotes, sorted_by_title_len, sorted_by_quotes_num = build_library(data)
    if 'find quotes from author' in " ".join(sys.argv):
        author = " ".join(sys.argv[sys.argv.index('author')+1:])
        search_by_source(author, quotes)
    elif 'find quotes from book' in " ".join(sys.argv):
        book = " ".join(sys.argv[sys.argv.index('book')+1:])
        search_by_source(book, quotes)
    elif 'author' in sys.argv:
        if sys.argv.index('author')+1:
            author = " ".join(sys.argv[sys.argv.index('author')+1:])
            search_by_source(author, quotes)
    elif 'book' in sys.argv:
        if sys.argv.index('book')+1:
            book = " ".join(sys.argv[sys.argv.index('book')+1:])
            search_by_source(book, quotes)
    else:
        term = " ".join(sys.argv[1:])
        search_by_source(term, quotes)
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
    
