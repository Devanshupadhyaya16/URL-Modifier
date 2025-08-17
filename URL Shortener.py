import pyshorteners

url = input("Enter the URL for shortening : \n")

print("URL After shortening :- ",pyshorteners.shortener().tinyurl.short(url))