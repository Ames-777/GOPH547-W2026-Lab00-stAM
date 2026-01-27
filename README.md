#GOPH 547

*Semester:* W2026
*Instructor:* B. Karchewski
*Author:* Amelia Morris

An example repository setup for a simple Python package. Includes examples using NumPy arrays and Matplotlib for visualization.

To download or clone the repository, click on the green "< > Code" button above the repository files. You can either download entire repository as a ZIP file or single files if selected, or you can clone them using HTTPS, SSH, or GitHub CLI through Python, making sure to navigate to the directory you'd like to store the files to beforehand, using the *cd /path/to/directory/* function. You can clone these files through *git clone https://github.com/Ames-777/GOPH547-W2026-Lab00-stAM.git* so that you can automatically pull updates through *git pull*.

To set up a virtual environment, which is recommended when running these files, navigate into the directory that the downloaded files are stored to, using the *cd /path/to/directory/* function. Use either *python -m venv .venv* or *python -m virtualenv .venv* depending on if you are using virtualenv or not, to create the virtual environment. To run the virtual environment, run *source ./.venv/bin/activate* after which a (.venv) should appear on the left hand side of the Terminal, indicating that the virtual environment is now activated.

To ensure the script runs properly, make sure to install the following packages by running *pip install numpy matplotlib setuptools*

Once the packages are installed, you can run the files by inputting *python driver.py*

The script *driver.py* (contained within the *examples/* folder) is designed to be used to better understand some of the tools used within the NumPy and Matplotlib packages. The first part of the script focuses on NumPy and creates various types of arrays and then performs different types of calculations on them, such as dot and cross product multiplication. The second part of the script focuses on Matplotlib and editing images, such as converting to grayscale, cropping the image, and creating multiple plots, including axis labels and titles. This script is designed to perform all edits on the rock_canyon.jpg image which is included within the *examples/* folder.

To run the code, run *python driver.py*

The expected output will contain nine different arrays and calculations on different arrays, including element-wise and dot-product multiplication, all of which is created using the NumPy package. Windows containing coloured and grayscale image of the rock_canyon.jpg, a cropped grayscale image, along with various plots containing colour values for each of the axes will also pop up in separate windows, each of which have been created using the Matplotlib package.