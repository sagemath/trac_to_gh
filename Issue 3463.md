# Issue 3463: notebook -- create a resource folder and move AnonymousToplevel to it

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-06-18 19:30:09

Assignee: boothby

This is a first step in making the Notebook code more modular like Knoboo's. 


---

Comment by TimothyClemans created at 2008-06-18 19:32:33

Changing assignee from boothby to TimothyClemans.


---

Comment by TimothyClemans created at 2008-06-18 19:32:33

Changing status from new to assigned.


---

Attachment

I'm getting the following import error and haven't been able to figure it out.


```
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/twisted/application/app.py", line 412, in getApplication
    application = service.loadApplication(filename, style, passphrase)
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/twisted/application/service.py", line 340, in loadApplication
    application = sob.loadValueFromFile(filename, 'application', passphrase)
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/twisted/persisted/sob.py", line 214, in loadValueFromFile
    exec fileObj in d, d
  File "sage_notebook/twistedconf.tac", line 47, in <module>
    import sage.server.notebook.avatars as avatars
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/avatars.py", line 20, in <module>
    import resources.toplevels as toplevels
  File "/home/tclemans/sage-3.0.3.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/resources/toplevels.py", line 3, in <module>
    import sage.server.notebook.avatars as avatars
exceptions.AttributeError: 'module' object has no attribute 'avatars'

Failed to load application: 'module' object has no attribute 'avatars'
```



---

Attachment

This was evidently the beginning of an unrealized vision.


---

Comment by was created at 2009-11-19 21:46:57

Resolution: invalid
