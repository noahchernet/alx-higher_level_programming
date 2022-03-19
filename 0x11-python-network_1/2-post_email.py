#!/usr/bin/python3
'''Module 2-post_email
Sends a POST request to the URL provided
'''
from urllib import parse, request
from sys import argv


def main():
    '''Program starts here. takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and displays the body
    of the response (decoded in utf-8)'''
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email})
    data.encode('utf-8')

    with request.urlopen(request.Request(url, data)) as response:
        print(response.read())


if __name__ == '__main__':
    main()
