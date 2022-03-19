#!/usr/bin/python3
'''
Module 0-hbtn_status
Fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request


def main():
    '''Program starts here.
    Details about the http response
    are printed.
    '''
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        response_read = response.read()
        print("Body response:")
        print("\t- type:", type(response_read))
        print("\t- content:", response_read)
        print("\t- utf8 content:", response.msg)


if __name__ == '__main__':
    main()
