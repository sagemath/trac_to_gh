# Issue 4077: notebook - ReactorNotRunning error consistently seen in sage-3.1.2.rc0

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-09-08 12:52:39

Assignee: boothby

Traceback when I hit CLTRL-C to stop the notebook. 

This is happening in sage-3.1.2.rc0 with and without the spkg at #4074.


```
2008-09-08 05:45:38-0700 [-] Log opened.
2008-09-08 05:45:38-0700 [-] twistd 8.1.0 (/home/tclemans/sage-3.1.2.rc0/local/bin/python 2.5.2) starting up
2008-09-08 05:45:38-0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008-09-08 05:45:38-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8999
2008-09-08 05:45:38-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x2b779155d9e0>
2008-09-08 05:45:49-0700 [-] Saving notebook...
2008-09-08 05:45:49-0700 [-] Notebook cleanly saved.
2008-09-08 05:45:49-0700 [-] Saving notebook...
2008-09-08 05:45:49-0700 [-] Unhandled Error
        Traceback (most recent call last):
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 1048, in run
            self.mainLoop()
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 1057, in mainLoop
            self.runUntilCurrent()
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 705, in runUntilCurrent
            call.func(*call.args, **call.kw)
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 545, in fireSystemEvent
            event.fireEvent()
        --- <exception caught here> ---
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 368, in fireEvent
            result = callable(*args, **kwargs)
          File "notebooktesting/twistedconf.tac", line 25, in save_notebook
            reactor.stop()
          File "/home/tclemans/sage-3.1.2.rc0/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/internet/base.py", line 495, in stop
            "Can't stop reactor that isn't running.")
        twisted.internet.error.ReactorNotRunning: Can't stop reactor that isn't running.

2008-09-08 05:45:49-0700 [-] (Port 8999 Closed)
2008-09-08 05:45:49-0700 [-] Stopping factory <twisted.web2.channel.http.HTTPFactory instance at 0x2b779155d9e0>
2008-09-08 05:45:49-0700 [-] Main loop terminated.
2008-09-08 05:45:49-0700 [-] Server Shut Down.
True
```



---

Attachment


---

Comment by mhansen created at 2008-09-08 23:20:30

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-08 23:20:30

Changing assignee from boothby to mhansen.


---

Comment by mabshoff created at 2008-09-09 04:58:16

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-09 04:59:59

Merged in Sage 3.1.2.rc1


---

Comment by mabshoff created at 2008-09-09 04:59:59

Resolution: fixed
