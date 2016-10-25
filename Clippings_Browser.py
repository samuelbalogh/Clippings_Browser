#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import sys
import term as color
import os
import random

data = 'data/export.txt' # exported from clippings.io
clippings = 'data/my_clippings.txt'  # original Kindle clippings format
quotes = {}
separator = ' -- '
location = 'loc.'
page = 'pg.'

def build_library():
    '''Builds clippings library from data (usually My clippings.txt)
    Returns quotes and sorted_quotes (sorted by number of quotes from source)'''
    quotes1 = parse_clippings_io(data)
    quotes2 = parse_my_clippings_txt(clippings)
    quotes = dict(quotes1, **quotes2)
    sorted_by_title_len = OrderedDict(sorted(quotes.items(), key=lambda x: len(x[0]), reverse = True))
    sorted_by_quotes_num = OrderedDict(sorted(quotes.items(), key=lambda x: len(x[1]), reverse = True))
    return quotes, sorted_by_title_len, sorted_by_quotes_num
    
def parse_clippings_io(data):
    '''Parses clippings in the format that is the output of www.clippings.io (separator is --)'''
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
                        continue
                    try:
                        quotes[source].append(quote)
                    except KeyError:
                        quotes[source] = [quote]
                except ValueError:
                    continue
    return quotes

def parse_my_clippings_txt(clippings):
    '''Parses clippings in the native Kinlde format (separator is '("==========")'''
    with open(clippings, 'r', encoding='utf-8') as file:
        file_as_list = file.read().split("==========")
        for entry in file_as_list:
            if 'Your Highlight' in entry:
                entry = entry.split('\n')
                source = entry[1]
                if source[0] == '\ufeff':
                    source = source[1:]
                highlight = entry[-2]
                try:
                    quotes[source].append(highlight)
                except KeyError:
                    quotes[source] = [highlight]
    return quotes
     

def list_sources(quotes, sorted_quotes):
    '''Lists all sources'''
    for source in quotes:
        print(source)
    for i in sorted_quotes:
        print(i)

def search_by_source(search_term, data):
    '''Looks for search term among the sources (authors, books)
    Returns matching entries as dict'''
    results = {}
    for source, quotes in data.items():
        if search_term.lower() in source.lower():
            results[source] = quotes
    return results
         
    
def display(search_term, results, items=5):
    '''Displays search results on the console with fancy coloring'''
    title_text = " ".join(['\n', 2* '\t', 'Showing results for ', '"', search_term, '"', 2* '\t'])
    subtitle_text = " ".join(['\n', '  \t', ' - - -  5 results per page. Press RETURN to continue. - - -,', 3*'\n'])
    title = color.format(title_text, color.red)
    subtitle = color.format(subtitle_text, color.red)
    for source, quotes in results.items():
        print(quotes)
        os.system('clear')
        print(title, '\n', subtitle, '\n', 'Showing quotes from:', source, 4 * '\n')
        for index in range(len(quotes)):
            if index!=0 and index % items == 0:
                input()
                os.system('clear')
                print(title, '\n', subtitle, '\n', 'Showing quotes from:', source, 4 * '\n')
            quote = quotes[index]
            quote = color.format(quote, color.green)
            print('\n -', quote)
            if index % items == items-1:
                text = color.format('Press RETURN to continue . . . ', color.blink)
                print(4 * '\n', text)
                    
def get_random_quote_from(search_results):
    '''Returns a dictionary that contains search results for the query string, but with the quotes in random order.'''
    random_order_dict = {}
    for source, quotes in search_results.items():
        list_of_quotes = quotes
        random.shuffle(list_of_quotes)
        random_order_dict[source] = list_of_quotes
    return random_order_dict

def main():
    quotes, sorted_by_title_len, sorted_by_quotes_num = build_library()
    parse_args()
          
def parse_args():
    '''Parse command line arguments and act accordingly'''
    if 'find quotes from author' in " ".join(sys.argv):
        author = " ".join(sys.argv[sys.argv.index('author')+1:])
        results = search_by_source(author, quotes)
        display(author, results)
    elif 'find quotes from book' in " ".join(sys.argv):
        book = " ".join(sys.argv[sys.argv.index('book')+1:])
        results = search_by_source(book, quotes)
        display(book, results)
    elif 'author' in sys.argv:
        if sys.argv.index('author')+1:
            author = " ".join(sys.argv[sys.argv.index('author')+1:])
            results = search_by_source(author, quotes)
            display(author, results)
    elif 'book' in sys.argv:
        if sys.argv.index('book')+1:
            book = " ".join(sys.argv[sys.argv.index('book')+1:])
            results = search_by_source(book, quotes)
            display(book, results)
    elif 'list' in sys.argv:
        list_sources(sorted_by_quotes_num, sorted_by_title_len)
    elif 'random quote from' in " ".join(sys.argv):
        source = " ".join(sys.argv[sys.argv.index('from')+1:])
        results = search_by_source(source, quotes)
        random_quotes = get_random_quote_from(results)
        display(source, random_quotes, items=1)
    else:
        term = " ".join(sys.argv[1:])
        results = search_by_source(term, quotes)
        display(term, results)
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
    
