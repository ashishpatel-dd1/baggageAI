# baggageAI

AUTHOR :- **Ashish Patel**

BaggageAI Computer Vision
Case Study:- Image Processing

Given two sets of images:- background and threat objects.Your task is to cut the threat objects, scale it down, rotate with 45 degree and paste it
into the background images using image processing techniques in python.

## project structure

![dir baggageAI](https://github.com/ashishpatel-dd1/baggageAI/blob/main/ss/Screenshot%202021-07-26%20230115.jpg?raw=true)


```background_images```  :- contains all original background images provided


```final_out``` :- contains all final output iamges that sre to be used for assessment


```masks``` :- auto generated masksed images of threat images


```resized``` :- auto generated, resized and rotated threat image files


```resized_masks``` :- auto generated resized and rotated masked images


```ss``` :- contains screenshots used in the present README.md


```threat_images``` :- contains all original images provided



### *Alternate files, to be used for improving software*
**NOT FOR ASSESSMENT PURPOSE**


*threats_resized :- alternate resized, rotated images saved after running the threat.py script mentioned below*


*adaptive_thresholding.py :- test script to implement openCV adaptive thresholding*


*baggage_blend.py :- blending and pasting threat_images to background_images*  **(PRIMITIVE STAGE)**


*test.ipynb :- temperory jupyter notebook used for testing purpose*


*threat.py :- NOT A VIRUS. alternate more automatized method for rotating, resizing, threat_images*  **(TO BE USED ALONG WITH baggage_blend.py)**


### ****SOLUTION FILES****

**final_out** :- final output images to be considered for assessment

**baggageAI.ipynb** :- final program jupyter notebook for assessment




## HOW IT WORKS !!!


Import all required libraries

Load images to process, here threat_images. Read them using the Globbing utility of Python.

```
image_list = [Image.open(item) for i in [glob.glob('D:\\Documents\\baggageAI\\threat_images\\*.%s' % ext) 
            for ext in ["jpg","gif","png","tga"]] for item in i]
```            
This snippet can be used to read multiple extensions of images some of which are already provided above.



Next up is the Masking of the ```threat_images```

```TRANSPARENCY=60


for img in image_list:
  mask_2=img.convert("L")
  th=240
  mask_2 = mask_2.point(lambda i: i < th and 255) 
  paste_mask_2 = mask_2.split()[0].point(lambda i: i * TRANSPARENCY / 100.)
  masked.append(paste_mask_2)
 
```

This snippet shows what threshold is used for difference between foreground sand background, here 240
TRANSPERENCY is in Percentage i.e 60%
After the process the masks are then saved into a masks folder.


Next is the Basis of the software i.e Resizing, Rotating of Images and their Masks.

```images=cv2.imread(filename)  
    image = imutils.resize(images,height=i) 
    rotate = rotate_bound(image, 45)
 ```
 
Here we have used the rotate bound function to rotate the images without the image getting cropped.
Again, these processed images are saved to a directory. 

The openCV functions ```cv2.getRotationMatrix2D, cv2.warpAffine``` when rotaing the iage doesn't check for image cropping while rotating the image,
so we have defined a function ```def rotate_bound()``` to get complete image.

The same procedure is followed for the Rotation and resizing of their respective masks.

```images = cv2.cvtColor(np.array(filename),cv2.COLOR_GRAY2BGR)
    image = imutils.resize(images,height=i)
    rotate = rotate_bound(image, 45)
```
Finally, these resized masks are saved to the directory of the same name.

And for the final step, these processed threat_images and their masks are cobined and the resultant threat_images without
background are then pasted over background_images, and as the transperency is 60% the normal human eyes would not be able to 
tell apart if the threat images have pasted onto the background images.

These are then saved to the ```final_out``` folder.


## *NOTE
While doing this code I came across a problem...which is as you know typing out the path of the image directories completely, which was really 
a huge headache.
So to comeup with a solution I have already started programming alternate scripts to overcome those headaches.

These files are mentioned above and are not yet completed. 

### *Do not use those files as it will do more harm than good.*
