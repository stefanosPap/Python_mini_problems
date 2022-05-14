Simple Notes for creating a desktop launcher. After this you will be able to launch the app by double clicking the icon on desktop.

**Steps**

1) Create a .desktop file and fill it with the lines below:

[Desktop Entry]
Version=1.0
Name=matrix comparison
Exec=/home/stefanos/Desktop/Python_mini_problems/numpy_speed_comparison/matrix_comparison.py (path to the .py file)
Icon=/home/stefanos/Desktop/Python_mini_problems/numpy_speed_comparison/lena.png (path to the icon file)
Type=Application
Terminal=true

2) Right click on the .desktop file: 
2.1 Properties -> Permissions -> Click Allow executing file as program
2.2 Change Access for Others to Read Only 

3) Right click on the .desktop file and click Allow Launching 

4) Double click on the icon that was created to launch the program
