# grape_detection_using_opencv
This is the code for the detecting grape and count of grapes in given image.

##Overview

This is the code for [this](https://drive.google.com/file/d/1twlJ70iy7SHYNE0ZR5Kl2OfEgf8C5DVp/view?usp=drivesdk) video. We'll use OpenCV to detect a grape and count of grapes in an image. We'll perform a series of operations which i've documented in the code to eventually highlight the count in an image and then draw a green circle around it.

##Dependencies

* openCV
* numpy
* Python3

You can use [pip](https://pip.pypa.io/en/stable/) to install any missing dependencies. And you can install OpenCV using
[this](http://docs.opencv.org/2.4/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html) 
guide.

##Usage

Run 
`python detect_grape.py` 
to create a new image with the detected grapes and count of grapes. This detection takes a split second. Deep learning would be more 
accurate but requires more computation currently. Sometimes you just need to quickly detect an image and don't 
mind handcrafted which features to look for.


