# Issue 1473: Java3D usable from command line as well as notebook

Issue created by migration from https://trac.sagemath.org/ticket/1473

Original creator: robertwb

Original creation time: 2007-12-12 10:49:02

Assignee: was

Eventually we hope to have many tools (e.g. MayaVi) to help handle this, but Java3D works now and it should be easy to invoke the same code as an app rather than an applet. 


---

Comment by robertwb created at 2007-12-12 10:49:11

Changing status from new to assigned.


---

Comment by robertwb created at 2007-12-12 10:49:11

Changing assignee from was to robertwb.


---

Attachment


---

Attachment


---

Attachment

This works fine for me.


---

Comment by cwitty created at 2007-12-15 07:42:51

If I download `java3d-1_5_1-linux-i586.zip` from the java3d web site, I can unzipit to get (among other things) `j3d-jre.zip`.  Then I can unzip `j3d-jre.zip` to get (among other things) `libj3dcore-ogl.so`.

If I put libj3dcore-ogl.so in some directory, and set my LD_LIBRARY_PATH environment variable to point to that directory before starting Sage, then the command-line java3d code works.


---

Comment by robertwb created at 2007-12-15 07:45:17

Gluegen is supposed to take care of all of that (for applets it does) but maybe there's a way to rig it for apps too.


---

Comment by mabshoff created at 2007-12-15 09:56:53

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 09:56:53

Resolution: fixed
