# sample code to test clarify API for detecting food objects from image

from predict import getobjects

if __name__=="__main__":
   items=getobjects('images/test4.jpeg')
   print ("Objects Detected in image are")
   print (items)

