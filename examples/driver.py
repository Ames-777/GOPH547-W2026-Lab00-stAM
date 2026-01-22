import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

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
    print(f'1. A1_np:\n{A1_np}')

    #2. Produce an array of NaN with 6 rows and 3 columns.
    A_NaN = np.full((6,3), np.nan)
    print(f'2. A_NaN:\n{A_NaN}')
    
    #3. Create a column vector of odd numbers between 44 and 75.
    Col_Vec = np.c_[np.arange(45, 75, 2)]
    print(f'3. Col_Vec:\n{Col_Vec}')

    #4. Find the sum of the vector produced in [3.].
    Sum_Col_Vec = np.sum(Col_Vec)
    print(f'4. Sum_Col_Vec:\n{Sum_Col_Vec}')

    #5. Produce array:
    #A =
    #[[ 5 7 2]'
    #   1 -2 3],
    #   4 4 4]]
    A2D = np.array([[5, 7, 2], [1, -2, 3], [4, 4, 4]])
    print(f'5. A2D:\n{A2D}')

    #6. Using a single command, produce the array:
    #B =
    #[[ 1 0 0]'
    #   0 1 0].
    #   0 0 1]]
    A_diag = np.diag([1,1,1])
    print(f'6. A_diag:\n{A_diag}')

    #7. Perform element-wise multiplication of the arrays A and B from [5.] and [6.].
    AB = A2D * A_diag
    print(f'7. AB:\n{AB}')

    #8. Calculate the dot product (or matrix-multiplication) of arrays A and B.
    AB_Dot = A2D @ A_diag
    print(f'8. AB_Dot:\n{AB_Dot}')

    #9. Calculate the cross product of arrays A and B.
    AB_Cross = np.cross(A2D, A_diag)
    print(f'9. AB_Cross:\n{AB_Cross}')

    #10. Load image rock_canyon.jpg.
    img_array = np.asarray(Image.open('rock_canyon.jpg'))

    #11. Plot image using imshow() function.
    img_plot = plt.imshow(img_array)
    plt.show()
    print(f'11. Shape:\n{img_array.shape}')

    #12. Re-open the image converting to grayscale.
    img_gray = np.asarray(Image.open('rock_canyon.jpg').convert('L'))
    print(f'12. Shape:\n{img_gray.shape}')

    #13. Using only Python/NumPy, produce new smaller image array.
    img_small = img_gray[168:233, 119:147]
    print(f'13. img_small Shape:\n{img_small.shape}')
    #plt.imshow()
    plt.figure()
    plt.imshow(img_small, cmap='gray')
    plt.title("Small_Gray_Image")
    plt.axis('off')
    plt.show()

    #14. For original image, make subplot with two plots.


    #15. Include acis labels, title, legend on each subplot.


    #16. Save subplot figure as a file using savefig() function.

if __name__ == '__main__':
    main()
