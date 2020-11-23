*Repository for mini projects*  

1. **Networks project in CISCO Packet Tracer:**
- A small business network with guest user access was created using CISCO Packet Tracer.
- The total number of user is 70 with a maxiumum of 10 guest users.
- An FTP Server was also created to demonstrate file sharing.
- The guest and LAN network operate on different subnets to allow for separation.

2. **CNN Classifier to recognize and classify handwritten digits:**
- Uses MNIST dataset with 60,000 training images and 10,000 test images.
- Plots greyscale images using matplotlib.
- Preprocessing involved: 
  <pre>
  re-shaping into 4D to make it compatible with Keras API
  type conversion to float
  normalization using max. RGB value
  <pre>
- A Sequential model was used. 6 Layers were added:
  <pre>
  Conv2D
  MaxPooling2D
  Flatten
  Dense
  Dropout
  Dense
  <pre>
- The model uses 'adam' optimizer, 'sparse categorial entropy' loss and calculates 'accuracy' metric.
- It was trained for 10 epochs.


3. 3 mini-games created in Python:  
<pre>
    1. Dice roll simulator 
    2. Number guessing game
    3. Rock paper scissors game
</pre>
