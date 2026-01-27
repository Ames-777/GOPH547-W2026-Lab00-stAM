import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import sys
from pathlib import Path

print("Python:", sys.executable)
print("CWD:", Path().resolve())
print("sys.path:")
for p in sys.path:
    print(" ", p)


from GOPH547Lab00.arrays import (
    square_ones,
    )

def main():

    #Test creating square array of ones.
    A_np = np.ones((3,3))
    A = square_ones(3)
    print(f'A_np:\n{A_np}')
    print(f'A:\n{A}')

    #1. Create array of ones with 3 rows and 5 columns.
    A1_np = np.ones((3,5))
    print(f'1. Array of ones:\n{A1_np}')

    #2. Produce an array of NaN with 6 rows and 3 columns.
    A_NaN = np.full((6,3), np.nan)
    print(f'2. NaN array:\n{A_NaN}')
    
    #3. Create a column vector of odd numbers between 44 and 75.
    Col_Vec = np.c_[np.arange(45, 75, 2)]
    print(f'3. Column vector:\n{Col_Vec}')

    #4. Find the sum of the vector produced in [3.].
    Sum_Col_Vec = np.sum(Col_Vec)
    print(f'4. Sum of column vector produced in [3.]:\n{Sum_Col_Vec}')

    #5. Produce array:
    #A =
    #[[ 5 7 2]'
    #   1 -2 3],
    #   4 4 4]]
    A2D = np.array([[5, 7, 2], [1, -2, 3], [4, 4, 4]])
    print(f'5. Array A:\n{A2D}')

    #6. Using a single command, produce the array:
    #B =
    #[[ 1 0 0]'
    #   0 1 0].
    #   0 0 1]]
    A_diag = np.diag([1,1,1])
    print(f'6. Array B:\n{A_diag}')

    #7. Perform element-wise multiplication of the arrays A and B from [5.] and [6.].
    AB = A2D * A_diag
    print(f'7. Element-wise multiplication of arrays A and B:\n{AB}')

    #8. Calculate the dot product (or matrix-multiplication) of arrays A and B.
    AB_Dot = A2D @ A_diag
    print(f'8. Dot product of arrays A and B:\n{AB_Dot}')

    #9. Calculate the cross product of arrays A and B.
    AB_Cross = np.cross(A2D, A_diag)
    print(f'9. Cross-product of arrays A and B:\n{AB_Cross}')

    #10. Load image rock_canyon.jpg.
    img_array = np.asarray(Image.open('rock_canyon.jpg'))

    #11. Plot image using imshow() function.
    img_plot = plt.imshow(img_array)
    plt.show()
    print(f'11. Image Shape:\n{img_array.shape}')

    #12. Re-open the image converting to grayscale.
    img_gray = np.asarray(Image.open('rock_canyon.jpg').convert('L'))
    print(f'12. Grayscale Shape:\n{img_gray.shape}')

    #13. Using only Python/NumPy, produce new smaller image array.
    img_small = img_gray[168:233, 119:147]
    print(f'13. img_small Shape:\n{img_small.shape}')
    #plt.imshow()
    plt.figure()
    plt.imshow(img_small, cmap='gray')
    plt.title('Small_Gray_Image')
    plt.axis('off')
    plt.show()

    #14. For original image, make subplot with two plots.
    #15. Include axis labels, title, legend on each subplot.
    #Colour channels:
    R = img_array[:, :, 0]
    G = img_array[:, :, 1]
    B = img_array[:, :, 2]

    #Mean colours along y-direction vs x-coordinate.
    Mean_R_x = np.mean(R, axis=0)
    Mean_G_x = np.mean(G, axis=0)
    Mean_B_x = np.mean(B, axis=0)
    Mean_RGB_x = np.mean(img_array, axis=(0, 2))

    #Mean colours along x-direction vs y-coordinate.
    Mean_R_y = np.mean(R, axis=1)
    Mean_G_y = np.mean(G, axis=1)
    Mean_B_y = np.mean(B, axis=1)
    Mean_RGB_y = np.mean(img_array, axis=(1, 2))

    #Creating subplots.
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    #Plotting mean colours along y-direction vs x-coordinate.
    axes[0].plot(Mean_R_x, color='red', label='Mean Red (R)')
    axes[0].plot(Mean_G_x, color='green', label='Mean Green (G)')
    axes[0].plot(Mean_B_x, color='blue', label='Mean Blue (B)')
    axes[0].plot(Mean_RGB_x, color='black', linewidth=2, label='Mean RGB')
    axes[0].set_xlabel('X-Coordinate')
    axes[0].set_ylabel('Colour Value')
    axes[0].set_title('Mean Colour Values VS X-Coordinate')
    axes[0].legend()

    #Plotting mean colours along x-direction vs y-coordinate.
    axes[1].plot(Mean_R_y, np.arange(len(Mean_R_y)), color='red', label='Mean Red')
    axes[1].plot(Mean_G_y, np.arange(len(Mean_G_y)), color='green', label='Mean Green')
    axes[1].plot(Mean_B_y, np.arange(len(Mean_B_y)), color='blue', label='Mean Blue')
    axes[1].plot(Mean_RGB_y, np.arange(len(Mean_RGB_y)), color='black', linewidth=2, label='Mean RGB')
    axes[1].set_xlabel('Colour Value')
    axes[1].set_ylabel('Y-Coordinate')
    axes[1].set_title('Mean Colour Values VS Y-Coordinate')
    axes[1].legend()

    #16. Save subplot figure as a file using savefig() function.
    plt.tight_layout()
    plt.savefig('rock_canyon_RGB_summary.png')
    print(f'16. Saved RGB summary image in examples folder.')

    plt.tight_layout()
    plt.show()
    print(f'14. and 15. Successfully created subplots.')
    print()

    
if __name__ == '__main__':
    main()
