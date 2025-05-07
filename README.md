# Steganography Methods

- LSB (Least Significant Bit Insertion) Algorithm
- JPEG Algorithm (DCT)
- BPCS (Bit Plane Complexity Segmentation) Algorithm
- Masking and Filtering Methods
- Heuristic Steganalysis Methods

#Installing required libraries for LSB

-pip install pillow  

#Installing required libraries for DCT

-pip install numpy opencv-python matplotlib scipy
# LSB Algorithm

## 1. Converting the Message to Binary Format  
Represent the message you want to hide in ASCII codes or directly in binary format. For example, the message "hello" could be represented as:

h: 01101000
e: 01100101
l: 01101100
l: 01101100
o: 01101111

## 2. Selecting an Image  
Choose an image to hide the message in (PNG or BMP formats are preferred because they do not use lossy compression).

## 3. Hiding the Message in the LSBs of Pixels  
Examine each pixel of the image (in RGB format, each pixel has 3 channels: Red, Green, and Blue).

The Least Significant Bit (LSB) of each channel is modified, and one bit of the message you want to hide is written into it.

Repeat this process for each pixel and channel.

## 4. Creating the New Image  
After placing all the message bits into the LSBs of each pixel, create a new image. The image will usually show no visible change, as only the LSBs have been altered.

## 5. Extracting the Message (Decoding)  
To extract the hidden message, read the LSB of each pixel.

Combine the LSBs you read to retrieve the original hidden message.

These steps form the basic logic of the LSB steganography process.
# JPEG Algorithm (DCT)

## 1. Converting the Image to Grayscale  
DCT typically works with grayscale images because applying DCT to color images can be more complex. Therefore, in the first step, we convert the image to grayscale.

## 2. Creating 8x8 Blocks  
DCT usually operates on small 8x8 blocks. The image is divided into these blocks, and DCT is applied to each block.

## 3. Applying DCT  
The `np.fft.dct` function performs the DCT operation on each block. This process calculates the frequency components of each block.

## 4. Recovering with IDCT (Inverse DCT)  
To reverse the DCT, the `np.fft.idct` function is used. This process reconstructs the image, returning a result that approximates the original image from the frequency components.

## 5. Visualizing the Images  
Finally, the original image and the reconstructed image after the DCT process are displayed side by side.
# BPCS Algorithm

## 1. Converting the Image to Binary Format  
The image is first converted to grayscale (to use only the luminance information). Then, this grayscale image is transformed into a binary format, with each pixel represented by an 8-bit binary value.

## 2. Bit Plane Decomposition  
The grayscale image is decomposed into bit planes. That is, each bit of every pixel is extracted into a separate plane. For example, each bit of an 8-bit pixel can be stored on a separate plane:

- Bit 7 (Most Significant Bit - MSB)
- Bit 6
- Bit 5
- ...
- Bit 0 (Least Significant Bit - LSB)

## 3. Bit Plane Complexity Calculation  
For each bit plane, it’s important to calculate the complexity of that plane. Complexity is a measure of the variability in that bit plane. High complexity means more variability and more information. Low complexity means a more homogeneous area.

## 4. Classifying and Segmenting Bit Planes  
High complexity bit planes (those with more variability) are selected as areas for embedding the message.

Low complexity bit planes are used as the carrier for the hidden message.

## 5. Hiding the Message  
The message you want to hide is added to the low complexity bit planes. In this step, the binary data of the hidden message is written into specific bits of these low complexity bit planes.

## 6. Reconstructing the New Image  
The new image is reconstructed with the hidden message. This image appears similar to the original image but contains the hidden message.
