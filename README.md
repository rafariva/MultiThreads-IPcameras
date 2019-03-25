# Multiple IP cameras using Threads

A script that allow you to use multi ip camera using threads avoiding the lag or buffering for multi adquisition images.

1. Modify video_capture.py file, and change:
  a. the list of ipcameras and cameras names
  b. the database_folder (default: database)
2. Press ENTER to take a snap on all cameras, press Q or ESC to quit

3. For visualize all the captures, run view_captures.py
  a. Press ENTER for forward, SPACE for backward

Thats all. Have fun!


Reproduce: [nrsyed multithread](https://github.com/nrsyed/computer-vision/tree/master/multithread)
