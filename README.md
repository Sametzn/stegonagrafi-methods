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

# JPEG Algorithm (DCT)

**Converting the Image to Grayscale:**  
DCT typically works with grayscale images because applying DCT to color images can be more complex. Therefore, in the first step, we convert the image to grayscale.

**Creating 8x8 Blocks:**  
DCT usually operates on small 8x8 blocks. The image is divided into these blocks, and DCT is applied to each block.

**Applying DCT:**  
The `np.fft.dct` function performs the DCT operation on each block. This process calculates the frequency components of each block.

**Recovering with IDCT (Inverse DCT):**  
To reverse the DCT, the `np.fft.idct` function is used. This process reconstructs the image, returning a result that approximates the original image from the frequency components.

**Visualizing the Images:**  
Finally, the original image and the reconstructed image after the DCT process are displayed side by side.


