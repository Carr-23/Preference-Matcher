# ML-Attraction
Developed first generation AI machine learning based software designed to predict human interactions with visual based mediums. The dataset was gathered using PRAW on r/selfies.


## StronkOrChonk.py
This script is used for me to create the data set of images. I would be able to assign a value of 1 or 0 and then swipe to the next image

## SorC.ipynb [Version 1]
This script gets the images, resizes them, and then trains a simple CNN model for Binary Classification.

The model had issues; It was overfitted, images had useless space in background, images were too big and took too long to train. 

Due to these issues, I decided to optimize my dataset first before optimizing my model.

## face_cropper.py {thanks to [tilfin](https://gist.github.com/tilfin/98bbba47fdc4ac10c4069cce5fabd834)}

I created another script that uses OpenCV facial and eye detection to find and crop the images accordingly. This would remove the wasted space (pixels) that the model was reading as input. This would also allow the images to have more facial features per pixel than before.
This filter also allows for bad selfies to not appear.
