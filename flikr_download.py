#! python3 
""" flikr_download.py - Downloads images of specified object from flickr to the Imgs folder, so don't forget to create a folder named Imgs,
                        you can even specify the number of images to be downloaded (default is 100)
"""

# Importing required libraries
import requests, os
import flickrapi
import urllib
from PIL import Image
import sys


def flikrDownload(fullPath, keyword, count=100):
    # Flickr api access key 
    flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

    # Checking if path exists
    if not os.path.isdir(fullPath):
        print(os.path.isdir(fullPath))
        return "Path doesn't exists"

    # Walking for the images using flickr api
    photos = flickr.walk(text=keyword,
                        tag_mode='all',
                        tags=keyword,
                        extras='url_c',
                        per_page=400,
                        sort='relevance')

    # Collecting the images urls
    urls = []
    for i, photo in enumerate(photos):
        if i > int(count):
            break
            
        url = photo.get('url_c')
        urls.append(url)

    # Getting the absolute path to store the images
    print("Downloading ", count, keyword, "images to :-->")

    # Downloading images one by one
    for i in range(1, int(count)+1):
        try:
            # Specifying the path with extension
            path = str(fullPath + "\\")+ keyword + "_" + str(i)+ ".jpg"
            print(path)
            
            # Retrieving the url and storing it in specified path
            urllib.request.urlretrieve(urls[i-1], path)
            image = Image.open(path)
            image.save(path)
            
        except Exception:
            pass
            
    return "Download done."