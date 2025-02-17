# Cone-detection

![answer](https://github.com/user-attachments/assets/75f2bd55-e586-451d-a27c-91567ea4656d)

# Methodology
1. Thresholding to find color where the cones are
2. Using contouring to find the overall image area of all the spots with the cones
3. Drawing a line across the centroid of those points (one for the left of the center and one for the right)

# Issues
I am getting a slight error on the left line, as it is skewed due to some noise

# Libraries 
1. OpenCV
2. Numpy



