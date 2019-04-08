# copy_from_Citrix
Copy over text from Citrix even when copy paste policy is off.

Flow:
  > visualize_color_variation.py runs in citrix remote desktop.<\br>
  It generates a image (from the text which you provided as input to variable 'test_string')
  
  > On your local desktop, take screenshot of above generated image.
  
  > Run color_picker.py - set variable 'img' = location of above screenshot image.
  It will generate the text on your local desktop
