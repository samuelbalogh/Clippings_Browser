#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import sys
import os
import random
from blessings import Terminal

data = 'data/export.txt' # exported from clippings.io
clippings = 'data/my_clippings.txt'  # original Kindle clippings format
quotes = {}
separator = ' -- '
location = 'loc.'
page = 'pg.'

t = Terminal()
with t.fullscreen():


    def build_library():
        '''Builds clippings library from 'data' and 'clippings' above
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
        '''Parses clippings in the native Kindle format (separator is '("==========")'''
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
        per_page = 'result' if items == 1 else 'results'
        subtitle_text = " ".join(['\n', '  \t', ' - - -', str(items), per_page, 'per page. Press RETURN to continue. - - - ', 3*'\n'])
        title = t.red + title_text
        subtitle = subtitle_text + t.normal
        for source, clippings in results.items():
            book_info = [title, '\n', subtitle, '\n', 'Showing clippings from: \n', source[2:], 4 * '\n']
            os.system('clear')
            print(" ".join(book_info))
            for index in range(len(clippings)):
                if index!=0 and index % items == 0:
                    try:
                        input()
                    except KeyboardInterrupt:
                        quit()
                    os.system('clear')
                    print(" ".join(book_info))
                quote = clippings[index]
                quote = t.green + quote
                print('\n -', quote)
                if index % items == items-1:
                    text =  t.normal + t.blink + 'Press RETURN to continue . . . '  
                    with t.location(0, t.height - 1):
                        print(text)
            try:
                input()
            except KeyboardInterrupt:
                quit()
        display('all', get_random_quote(quotes), 1)

    def get_random_quote_from(search_results):
        '''Returns a dictionary that contains search results for the query string, but with the quotes in random order.'''
        random_order_dict = {}
        for source, quotes in search_results.items():
            list_of_quotes = quotes
            random.shuffle(list_of_quotes)
            random_order_dict[source] = list_of_quotes
        return random_order_dict

    def get_random_quote(data):
        '''Returns random quote from the whole library'''
        random_source = random.choice(list(data.keys()))
        random_quote = random.randint(0, (len(quotes[random_source])))
        quote = {}
        try:
            quote[random_source] = [quotes[random_source][random_quote]]
        except IndexError:
            get_random_quote(data)
        return quote


    def main():
        quotes, sorted_by_title_len, sorted_by_quotes_num = build_library()
        parse_args()
        t.normal

    '''

    TODO:

    1. add argparse
    2. add command_line_runner
    3. refactor

    '''

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
            if 'all' in " ".join(sys.argv[sys.argv.index('from')+1:]):
                display('all', get_random_quote(quotes), 1)
            else:
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

    def get_random_source():
        '''Return random book from the library'''

    def mark_as_favorite():
        '''Marks currently displayed quote as favorite'''

    def get_favorites():
        '''Returns favorite quotes'''

    def save_favorites():
        '''Saves favorites to .txt file'''

