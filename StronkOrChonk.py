import praw
import requests
import time
import os
import keyboard
from PIL import Image
from pynput.keyboard import Key, Controller
import json

def getImages():
    reddit = praw.Reddit(client_id='1Gy4zNNu1JlnIA', client_secret='1GzLnVE1fcIqZ9rrOUYyOP_Kzkk', user_agent='VCC')

    startTime = time.time()
    top_posts = reddit.subreddit('selfies').top('all', limit=None)
    for post in top_posts:
        url = (post.url)
        file_name = url.split("/")
        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)
        file_name = file_name[-1]
        if "." not in file_name:
            file_name += ".jpg"
        #print(file_name)
        r = requests.get(url)
        with open('selfies/'+ file_name,"wb") as f:
            f.write(r.content)

    print('Total Time: ', time.time() - startTime)

def previewImages(imageFile):
    im = Image.open('selfies/' + imageFile)
    im.show()


def getAllImages():
    files = os.listdir('selfies/')
    return files

def stronk_or_chonk(girls):
    kb = Controller()
    yValues = []
    print(len(girls))
    for girl in girls:
        print('This is a ', end = '')
        while True:
            if keyboard.is_pressed('s'):
                print('1', end = '')
                yValues.append(1)
                kb.press(Key.right)
                kb.release(Key.right)
                print('Stronk ;)')
                break
            elif keyboard.is_pressed('c'):
                print('0', end = '')
                yValues.append(0)
                kb.press(Key.right)
                kb.release(Key.right)
                print('Chonk :/')
                break
            elif keyboard.is_pressed('p'):
                time.sleep(120)
                print('We Back to the grind')
                break

            time.sleep(0.001)
        time.sleep(0.25)

    with open('yValues.json', 'w') as f:
        json.dump(yValues, f)


def main():
    file = getAllImages()
    #previewImages(file[0])
    keyboard.wait('esc')
    print('Stronk or Chonk')
    print('---------------')
    stronk_or_chonk(file)


if __name__ == "__main__":
    main()
