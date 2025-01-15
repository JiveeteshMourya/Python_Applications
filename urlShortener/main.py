import pyshorteners
link = input("Enter the link to shorten: ")

def shorten_url(link):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(link)
    print("Shortened URL: ", short_url)

shorten_url(link);