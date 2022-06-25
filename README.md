ABOUT : 

it is computer vision project that allow us to  change volume of system with handtracking.

this project also used a library called mediapipe devloped by google for hand tacking , face detection , pose detection etc.

HOW TO USE THIS 

first of all this project is only works in ubuntu(or linux based os) its not works in windos or mac operting system

in order to install this in your system do all the step below

step 1 : 

first you should have git install in your system to install this run this command :

$ sudo apt install git

then clone this repository run the command 

$ git clone https://github.com/samthakur587/volumecontrol.git

step 2 :

now you need to install python in your system 

$ sudo apt install python3

then install pip in your system

$ sudo apt install python3-pip

step 3 :

after done this step your need change your directory to volumecontrol 

$ cd volumecontrol

now install the all the requirements for this project to do this run command

$ pip install -r requirememt.txt

step 4 :

so all done now you can run the program by using the command

$ python volumecontrol.py

so now you can change the volume of your system by changing the distance beetween your first fingure and thum . the volume gets maximum when the distance between your first fingure and thum gets maximum .

to stop the exicussion click "q" on your keyboard

NOTE :  if your are using anconda the you should make an enviorment first to do this run command :

$ conda create -n my_env

$ conda activate my_env


