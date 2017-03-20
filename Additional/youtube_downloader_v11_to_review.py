# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 00:51:29 2017

@author: Mikhail Belousov
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

#TBD
# - use regex to validate names (smb_to_avoid = "#<$+%>!`&*'|{?\"=}/:\ @")
# - add multithreading (threading or multiprocessing)?
# - control number of threads as savemedia can forcibly close connection if too many requests are sended
# - retrieve downloading for file in case of failure
# - handle file names in Unicode(Russian, Chinese etc.)
# - save download history?
# - choose file resolution and\or  duration

#Questions for now:
# 1.Because of unstable connections (vpn in China), in case of connection issues browser just stops downloading, but doesn't return control to my script. How can I handle this exception?
#
# 2. As consequenses, I want to speed up downloading. Which module, threading or multirpocessing, is better for this purpose? How to control number of active downloads?
#
# 3. Can I check results of downloading in a more efficient way? E.g. can I get file size from Chrome before download starts?

def getHTMLPage(playlist):
    """Extracts playlist html source from youtube"""
    try:
        r = requests.get(playlist, timeout=30)
        r.enconding = 'utf8'
        r.raise_for_status()
        return r.text
    except:
        return ''


def getPlaylistLinks(playlist_page):
    """Gets links of all videos in the playlist"""
    soup = BeautifulSoup(playlist_page, 'html.parser')
    clip_links = []
    a = soup.find_all('a', {'class': 'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link '})
    for entry in a:
        try:
            href = 'https://www.youtube.com/'+entry.attrs['href'][:20]
            name = entry.string.strip()
            clip_links.append([name, href])
        except:
            continue
    h1 = soup.find('h1', {'class': 'pl-header-title'})
    playlist_name = h1.string.strip()
    return clip_links, playlist_name


def downloadFromSavemedia(url, driver, clip_link, number):
    """Helper function for getDownloads, initiates download from
    savemedia.com"""
    driver.get(url)
    try:
        start_time = time.time()

        #input youtube clip link adn press enter
        input_bar = driver.find_element_by_id("video-url")
        input_bar.send_keys(clip_link, Keys.ENTER)
        submit_button = driver.find_element_by_id('download-submit')
        submit_button.click()

        #get a page with download options, parse link to auto download
        #it's name is wrapper_link
        driver.implicitly_wait(6)
        download_button = driver.find_element_by_id("get_video")
        wrapper_link = download_button.get_attribute('data-href')
        print('Got the link, ' + wrapper_link)
        if wrapper_link is None:
            raise Exception('Did not get the link')

        #after this statement Chrome starts auto download
        driver.get(url+wrapper_link)
        if time.time() - start_time > 120:
            raise Exception('Overtime')
        return True
    except Exception as e:
        print('Download error: {0} for file #{1}'.format(e, number))
        return False


def checkFileStatus(file_name):
    """Helper function for getDownloads, waits file to be downloaded"""
    print('Ok, writing exactly ' + file_name)
    checkFlag = False
    while not checkFlag:
        if os.path.exists(file_name):
            print(file_name + " exists")
            check_one = os.path.getsize(file_name)
            time.sleep(5)
            check_two = os.path.getsize(file_name)
            if check_two == check_one:
                checkFlag = True
                print(file_name + ' has been saved')
                return
        else:
            time.sleep(5)


def getDownloads(clip_links, home_dir):
    """Manages the whole downloading process
    - opens webdrive with Chrome
    - saves and renames files from valid links
    -  quits webdrive"""
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": home_dir}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromedriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    savemediaurl = 'http://savemedia.com/'

    #for loop for all links from youtube's playlist
    for index, entry in enumerate(clip_links):
        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
        saved_file = downloadFromSavemedia(savemediaurl, driver, entry[1], index+1)
        if saved_file:
            old_name = entry[0] + '.mp4'
            checkFileStatus(old_name)
            new_name = str(index+1).zfill(2) + '. ' + entry[0] + '.mp4'
            os.rename(old_name, new_name)
        driver.quit()
    return


def main():
    """Implements the logics of this script"""
    playlist = 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDfV1MIRBOcqClP6VZXsvyZS'
    html = getHTMLPage(playlist)
    clip_links, playlist_name = getPlaylistLinks(html)
    if not os.path.exists(("C:\\Users\Mikhail Belousov\\Downloads\\" + playlist_name)):
        os.makedirs("C:\\Users\Mikhail Belousov\\Downloads\\" + playlist_name)
    os.chdir("C:\\Users\Mikhail Belousov\\Downloads\\" + playlist_name)
    home_dir = os.getcwd()
    getDownloads(clip_links, home_dir)

if __name__ == '__main__':
    main()