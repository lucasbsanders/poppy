# poppy

## Contributors:
- Lucas Sanders: Led weekly group progress meetings and held code review & debugging sessions with individuals outside of meetings. Created and maintaned team assets for the project such as the github repo, Teams channel, and group presentation materials. Worked on the Kivy project initial setup, build pipeline, and contributed work including reasearching and sometimes implementing features such as a local database, kivy layout features, the deployment of an API. Defined and continually clarified project requirements and coordinated work. Instructed group members on git practices.
- Haozhe Zhang: Followed tutorials to build up the framework of Kivy, including UI layout, ~~user auth~~ (deprecated), screen transition and generating, storing and displaying tasks. Based on this, also he researched how to build an APK with Buildozer and managed to overcome Android compatibility issues. After completing it, he integrated and tuned a camera module to take photos for further processing and analysis. He then implemented Bandy's OCR modules by hosting the image processing modules on Heroku and managed to process data by sending POST request, containing images converted to base64 strings.
- Oluwapemisin Bandy-toyo
- ~~Michel Gonzalez~~
- Joseph Carlson

## Directory structure:
Directory  | Contents
---------- | ----------
app_home/  | UI written in Kivy
assets/    | Static images, wireframes, some wiki documents
bin/       | Android APK file (arm64)
modules/   | Python modules for OCR and text processing

## Project work breakdown
In phase 1, we've:
- Implemented the build + deployment process
- Created a simple list of notifications in a taskmanager-like view
- Integrated the camera to take pictures
- Implemented separately the OCR and text-parsing functionality

In phase 2, we plan to extend the project by:
- Resolving UI issues
- Connecting the OCR/Text parser to the camera feature of the view
- Integrating a form that will be auto-filled by the OCR/text parser
- Implementing notifications for events

## UI Usage Instructions

1. Register an account where the user name should contain at least 3 characters and the password should contain at least 6 characters.
2. Hit the big add button or go to sidemenu->Add New to add a task with time specified. 
3. You may delete the task by tapping the trash can icon.
4. You may check out the camera module via sidemenu->Camera.

### Known Issues

1. Because the original library of the date picker is deprecated, we are no longer able to access its date picker widget via pip install. Note that there is an improved version of this library on GitHub, but it doesn't have a pip install command. The orinal library has already been updated to a usable version, but the author hasn't updated the one linked to pip.
2. Since the date picker has been temporarily disabled, we now group every task into the upcoming category while the date for each task has been automatically set to the day when the task is created.
3. The task update function has been temporarily disabled due to unknown bugs.

### Backend Repository
[Poppy API repository](https://github.com/rrrrr4788/Poppy_Backend)
