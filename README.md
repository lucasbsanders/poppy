# poppy

Currently this is a taskmanager-liked project. In the future we are going to implement OCR, notification, firebase, etc.

# Usage

1. Register an account where the user name should contain at least 3 characters and the password should contain at least 6 characters.
2. Hit the big add button or go to sidemenu->Add New to add a task with time specified. 
3. You may delete the task by tapping the trash can icon.
4. You may check out the camera module via sidemenu->Camera.

# Known Issues

1. Because the original library of the date picker is deprecated, we are no longer able to access its date picker widget via pip install. Note that there is an improved version of this library on GitHub, but it doesn't have a pip install command. The orinal library has already been updated to a usable version, but the author hasn't updated the one linked to pip.
2. Since the date picker has been temporarily disabled, we now group every task into the upcoming category while the date for each task has been automatically set to the day when the task is created.
3. The task update function has been temporarily disabled due to unknown bugs.


Contributors:
- Lucas Sanders
- Haozhe Zhang
- Oluwapemisin Bandy-toyo
- Michel Gonzalez
