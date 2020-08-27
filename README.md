# apply-engraved-effect<br>
A script used in product customizator. Purpose was to get different images from the user and return how it would look on the product. Library 'cv2' required.<br>

![alt text](https://raw.githubusercontent.com/1gn45/apply-engraved-effect/master/result.jpg)

# Using the script:
from applyengraved import CreateImage<br><br>
Set filename of image on which we want to apply engravings:<br>
img="box.jpg"              <br><br>
The image to be aded on 'img':<br>
putonimage="cat.jpg"<br><br>
White image with quadrilateral black shape that shows perspective field where the engravings will be aplyed:<br>
mask="boxedges.png"      <br><br>
The real world ratio of the field in perspective[height,width]:<br>
ratio=[2,3]                <br><br>
The same image as 'img' but photoshoped with needed effect:<br>
texture="boxengraved.jpg"   <br><br>
Might be same as 'edgesimgx', but can put more white areas where we want to avoid the angravings to be added. Can be any shapes. Only black areas of 'img' will be affected:<br><br>
flt="boxfilter.png"         <br><br>

Create engraved image:<br>
CreateImage(img, putonimage, mask, ratio, texture, flt)
