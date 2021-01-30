from PIL import Image , ImageOps
import numpy as np
import pandas as pd 
import csv
import cv2


q= Image.open("image.jpg")
w = Image.open("misty.jpg")
im = ImageOps.grayscale(q) 
im2 = ImageOps.grayscale(w) 
encoder = im2.resize(im.size)

### images read and greyscaled for processing

a = np.array(im)
b = np.array(encoder)

###our images are converted into a numpy array


### to correctlu bland the images encoder image is made same size as input image
width, height = im.size


encoded = np.zeros((height,width))
encoded = encoded.astype(int)

##encoding of pic 1 which is spiderman eating bagel "a" with pic 2 misty weather pic "b"
for i in range(len(a)):
    for j in range(len(a[i])):
        #print(a[i][j] * b[i][j] )
        some = a[i][j] 
        thing =b[i][j] 
        dat = int(some) * int(thing)

        if dat != 0:
            encoded[i][j] = dat
        else:
            if some ==0 and thing ==0:
                encoded[i][j] = 0
            if some !=0 and thing ==0:
                encoded[i][j] = -1
            if some ==0 and thing !=0:
                encoded[i][j] = -2

###some made up conversion rules are implemented



        

print("encoded")
print(encoded)
ofx = Image.fromarray(np.uint8(encoded) , 'L')
ofx.save("encodedimage.jpg")
ofx.show()

pd.DataFrame(encoded).to_csv("file.csv", header=None, index=None)
## encoded image is saved as an jpg and csv.

qq= Image.open("dencodercorrect.jpg")
dencotrue = ImageOps.grayscale(qq) 
xddd= ImageOps.grayscale(qq) 
dencotrue = xddd.resize(im.size)


ww = Image.open("dencoderwrong.jpg")
dencofalse = ImageOps.grayscale(ww) 
dencofalse = dencofalse.resize(im.size)
## 2 sets aof image is read to decode encoded image one is correct one is wrong 

#### but alll correct steps are done 


c = np.array(dencotrue)
d = np.array(dencofalse)

#### images numpyfied

print("loaded")
file = open("file.csv")
an = np.loadtxt(file, delimiter=",")
imagetodecode = an.astype(int)

##csv read into a numpy array

decoded1 = np.zeros((height,width))
decoded1 = decoded1.astype(int)

##decode1
for i in range(len(imagetodecode)):
    for j in range(len(imagetodecode[i])):
        #print(a[i][j] * b[i][j] )
        some = imagetodecode[i][j] 
        thing =c[i][j] 
        
       
        
        if some ==-1 :
            decoded1[i][j] = 123
        elif some == -2:
            decoded1[i][j] = 0
        elif some == 0 or thing ==0:
            decoded1[i][j] = 0
        else:
            dat = int(some) / int(thing)

            decoded1[i][j] =dat
   
of = Image.fromarray(np.uint8(decoded1) , 'L')
of.save("correct decoded.jpg")
of.show()
##and we decode with the rules  which causes litte loses yet we manage to decode near perfection





decoded2 = np.zeros((height,width))
decoded2 = decoded1.astype(int)

###decode2
for i in range(len(imagetodecode)):
    for j in range(len(imagetodecode[i])):
        #print(a[i][j] * b[i][j] )
        some = imagetodecode[i][j] 
        thing =d[i][j] 
        
       
        
        if some ==-1 :
            decoded2[i][j] = 123
        elif some == -2:
            decoded2[i][j] = thing
        elif some ==0:
            decoded2[i][j] = 0
        elif thing ==0:
            decoded2[i][j] = 0
        else:
            dat = int(some) / int(thing)

            decoded2[i][j] =dat
   
img3 = Image.fromarray(np.uint8(decoded2) , 'L')
img3.save("incorrect decoded.jpg")
img3.show()
## dont want to even show you the image thats houndted......