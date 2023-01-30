# VRCOSCBPM
Getting the BPM of the music you're listening to on Spotify, and sending it to VRChat over OSC with Python.

Python 3 required! Get it from [python.org](https://www.python.org/downloads/) and save yourself some trouble.

Upon first launch, you're going to need to authorize VRCOSCBPM to access your Spotify account! This is done by hitting the "authorize" button in your browser, THEN copy-pasting the URL it takes you to back into the app. 

At that point, it should be good to go, and you shouldn't need to reauthorize.

# Configuration
The vrcoscbpm.cfg file contains configuration parameters:
  • IP
  • Port
    Where OSC messages will be sent to. "127.0.0.1:9000" is the default VRChat is listening to.
  
  • avatar_parameter_path
    The path OSC messages will be sent upon. "/avatar/parameters/BPM" will send a float between 0 and 1 to a parameter called "BPM" on your avatar.

  • animation_bpm
    The BPM, tempo, etc, of the animation you are trying to drive.

# Animation BPM
Yada yada explain animation bpm

# VRChat OSC configuration
yada yada explain how to reset OSC config for avatars

# Spotify Authorization
When you first launch, this will appear:

![image](https://user-images.githubusercontent.com/12983495/215369618-05f71ced-ff1c-4079-b098-d226fbdb8e81.png)

and then your browser will open to an authorization page:

![image](https://user-images.githubusercontent.com/12983495/215369782-f934b40d-cd88-47e2-80de-fb076657cf42.png)

hit "Authorize", and you'll be redirected right here! now, copy the very long URL in your address bar back into the program, and hit enter:

![image](https://user-images.githubusercontent.com/12983495/215372053-18d11b99-9501-45f9-b7d3-3a2991bc5eb3.png)

then it any button to build the tekore configuration, and when built, hit it again to start the program:

![image](https://user-images.githubusercontent.com/12983495/215370287-dd56f978-8e8f-47ba-87ab-9c9f877c1f66.png)

You're now authorized! Just start up VRCOSCBPM and it should start sending your BPM immidiately!
