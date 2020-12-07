# Python Scraper

Automated Python Web Scraping Bot built with Beautiful Soup with the ablity to send CSV of extracted info to an email address. The CSV will be named for the day created so that an archive can be kept of the scrapped data.

**Please check the robots.txt file of any website you intend to scrape. To do so, simply add /robots.text to the target URL to see allowed and disallowed routes**

To use this scrapper:

- install at CL: requests | " pip install requests "

- install at CL: Beautiful Soup 4 | " pip install beautifulsoup4 "

- Fork or download the zip file.
- Open the folder contents in your IDE.
- 3 values require your personal information in the send_mail.py file

    1.) Line 11 | from email address.

    2.) Line 12 | to email address.

    3.) Line 40 | add your mail server password.


- 2 values in the scrape.py file

    1.) The URL or URL's to scrape.

    2.) Line 17 | Your personal user agent ; https://www.whatismybrowser.com/detect/what-is-my-user-agent will tell you your personal value.

- Once your values are in place, run scrape.py in the command line


License
Distributed under the MIT license.

See LICENSE for more information.
