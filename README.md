# [poppy](https://github.com/rrrrr4788/Poppy_Backend)
poppy is a mobile application that reads your medication labels and creates reminders for your medication doses automatically.

## Contributors:
- Lucas Sanders: Led weekly group progress meetings and held code review & debugging sessions with individuals outside of meetings. Created and maintaned team assets for the project such as the github repo, Teams channel, and group presentation materials. Worked on the Kivy project initial setup, build pipeline, and contributed work including reasearching and sometimes implementing features such as a local database, kivy layout features, the deployment of an API. Defined and continually clarified project requirements and coordinated work. Instructed group members on git practices.
- Haozhe Zhang: Followed tutorials to build up the framework of Kivy, including UI layout, ~~user auth~~ (deprecated), screen transition and generating, storing and displaying tasks. Based on this, also he researched how to build an APK with Buildozer and managed to overcome Android compatibility issues. After completing it, he integrated and tuned a camera module to take photos for further processing and analysis. He then implemented Bandy's OCR modules by hosting the image processing modules on Heroku and managed to process data by sending POST request, containing images converted to base64 strings.
- Oluwapemisin Bandy-toyo: Implemented the OCR modules for the project. Watched tutorials to learn how to use pytessaract for OCR and other tutorials to figure out how to allow pytessaract extract the most information from the image. These videos included techniques like resizing and adaptive thresholding to get the most out of the images. Researched the datetime module to allow for the creation of events in pytessaract. Researching how to process text information.
- Carlson Joseph: Attended weekly meetings and maintained contact with teammates throughout phase 2, followed online tutorials and lecture to begin and implement design of unit tests that are intended to test the functionality and accuracy of the main three backend processes: creation of events, image processing, and text_processing. Unit tests test against equality comparison of each process' main functions and user-provided correct answers, which can be deposited into seperate folders that store testing variables. 
- ~~Michel Gonzalez~~

## Directory structure:
Directory  | Contents
---------- | ----------
app_home/  | UI written in Kivy
assets/    | Static images, wireframes, some wiki documents
backend/   | Backend that integrates the OCR modules
backend/unittesting/   | Backend unit testing
executables/    | Mobile APK file for Android debugging

## Project work breakdown
In phase 1, we've:
- Implemented the build + deployment process
- Created a simple list of notifications in a taskmanager-like view
- Integrated the camera to take pictures
- Implemented separately the OCR and text-parsing functionality

In phase 2, we've:
- Resolved UI issues, streamelined the UI
- Set up an API for the OCR/Text parser to analyze the pictures taken by the camera module
- Made code improvements to the text parsing

## Using the poppy Application

1. Touch the "+" button or the sushi menu to open the Camera Screen.
2. Center a picture of any prescription description on the screen, touch "capture" and wait for the app to signal success.
 - (PC Only, optional) If you are not satisfied with the photo quality, you may replace the taken photo with any photo containing the desired info. To do this, you need to save a picture in the app_home folder, open app_home/app/view.py, and change the file name in line 41 “with open("IMG_{}.png".format(timestr), "rb") as image_file:” to the name of your picture’s filename.
3. If there are two short bursts of vibrations (mobile) or a success sound (PC), the reminders are added. Otherwise, an error signal will be sent, and you must retake the photo.
4. Restart the app to view the reminders. Reminders are triggered at the times listed, then removed from the UI.

## Mobile APK Instructions (Android) (source code found on `mobile` branch)

1. Start APK in an Android emulator.

## UI Usage Instructions (PC)

1. Kivy is not supported after python 3.7. Preferably, Kivy and its dependencies are installed/run in a virtual environment.
2. Initialization command: `pip install .`
3. Executable command: `python ./app_home/main.py --size=320x645 –dpi=94` (the flags are optional but recommended as Kivy has known issues when the screen size is incompatible with a system).

## API Local Instructions (PC)

1. In the backend directory, run the script to install the packages in requirements.txt `pip install -r backend/requirements.txt`
2. In system variables, add a variable named TESSDATA_PREFIX, with the key being \\**Project Directory**\\modules\Tesseract-OCR\tessdata.
3. Then, run `python backend/app.py` to start the server.

### Known Issues

- The resolution for the camera module is very device-specific. In our project, it has been set to 640x480, which is the default dimension. However, there is still a possibility that it will cause the program to crash.
- Sometimes the Heroku app consistently outputs "503 connection timeout" while receiving a request. There are two ways around this:
    1. Restart the dyno, email Zhang to run that proces.
    2. Run the backend server locally, explained above.
- Due to the unstability of the framework, the app can crash after several normal operations. Below are the list of the determined glitches:
    1. Hitting Android's Go Back button (or doing some gestures, depending on your device) may immediately shut down the program. 
    2. Sometimes the camera blacks out for no unknown reasons.
    3. When analyzing a picture, if the device is forced to go back to the home screen of Android, the entire screen will be blacked out when re-entering the app.

### Backend Repository
[Poppy API repository](https://github.com/rrrrr4788/Poppy_Backend)
