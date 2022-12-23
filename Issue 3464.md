# Issue 3464: notebook server error on sage.math (port detection problem)

Issue created by migration from https://trac.sagemath.org/ticket/3464

Original creator: craigcitro

Original creation time: 2008-06-18 21:40:52

Assignee: boothby

CC:  boothby was yqiang

The notebook code that detects whether or not a port is in use and finds a new port seems to be broken on sage.math -- two of us just tried while William had a server on port 8000, and we got the following:


```
******************************************************************
*                                                                *
* Open your web browser to https://sage.math.washington.edu:8000 *
*                                                                *
******************************************************************
There is an admin account.  If you do not remember the password,
quit the notebook and type notebook(reset=True).
2008-06-18 14:33:23-0700 [-] Log opened.
2008-06-18 14:33:23-0700 [-] twistd 8.0.1 (/home/was/s/local/bin/python 2.5.2) starting up
2008-06-18 14:33:23-0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008-06-18 14:33:23-0700 [-] Traceback (most recent call last):
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/bin/twistd", line 5, in <module>
2008-06-18 14:33:23-0700 [-]     pkg_resources.run_script('Twisted==8.0.1', 'twistd')
2008-06-18 14:33:23-0700 [-]   File "build/bdist.linux-x86_64/egg/pkg_resources.py", line 448, in run_script
2008-06-18 14:33:23-0700 [-]   File "build/bdist.linux-x86_64/egg/pkg_resources.py", line 1166, in run_script
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/EGG-INFO/scripts/twistd", line 21, in <module>
2008-06-18 14:33:23-0700 [-]     run()
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/scripts/twistd.py", line 24, in run
2008-06-18 14:33:23-0700 [-]     app.run(runApp, ServerOptions)
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/application/app.py", line 599, in run
2008-06-18 14:33:23-0700 [-]     runApp(config)
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/scripts/twistd.py", line 20, in runApp
2008-06-18 14:33:23-0700 [-]     _SomeApplicationRunner(config).run()
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/application/app.py", line 333, in run
2008-06-18 14:33:23-0700 [-]     self.postApplication()
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/scripts/_twistd_unix.py", line 259, in postApplication
2008-06-18 14:33:23-0700 [-]     startApplication(self.config, self.application)
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/scripts/_twistd_unix.py", line 213, in startApplication
2008-06-18 14:33:23-0700 [-]     service.IService(application).privilegedStartService()
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/application/service.py", line 227, in privilegedStartService
2008-06-18 14:33:23-0700 [-]     service.privilegedStartService()
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/application/internet.py", line 85, in privilegedStartService
2008-06-18 14:33:23-0700 [-]     self._port = self._getPort()
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packag
es/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/application/internet.py", line 116, in _getPort
2008-06-18 14:33:23-0700 [-]     *self.args, **self.kwargs)
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/gnutls/interfaces/twisted/__init__.py", line 355, in listenTLS
2008-06-18 14:33:23-0700 [-]     p.startListening()
2008-06-18 14:33:23-0700 [-]   File "/home/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-linux-x86_64.egg/twisted/internet/tcp.py", line 739, in startListening
2008-06-18 14:33:23-0700 [-]     raise CannotListenError, (self.interface, self.port, le)
2008-06-18 14:33:23-0700 [-] twisted.internet.error.CannotListenError: Couldn't listen on sage.math.washington.edu:8000: (98, 'Address already in use').
xprop:  unable to open display ''
usage:  xprop [-options ...] [[format [dformat]] atom] ...

where options include:
    -grammar                       print out full grammar for command line
    -display host:dpy              the X server to contact
    -id id                         resource id of window to examine
    -name name                     name of window to examine
    -font name                     name of font to examine
    -remove propname               remove a property
    -set propname value            set a property to a given value
    -root                          examine the root window
    -len n                         display at most n bytes of any property
    -notype                        do not display the type field
    -fs filename                   where to look for formats for properties
    -frame                         don't ignore window manager frames
    -f propname format [dformat]   formats to use for property of given name
    -spy                           examine window properties forever

---------------------------------------------------------------------------
error                                     Traceback (most recent call last)

/home/citro/.sage/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/server/notebook/notebook_object.py in __call__(self, *args, **kwds)
    141     """
    142     def __call__(self, *args, **kwds):
--> 143         return self.notebook(*args, **kwds)
    144 
    145     notebook = run_notebook.notebook_twisted

/home/was/s/local/lib/python2.5/site-packages/sage/server/notebook/run_notebook.py in notebook_twisted(self, directory, port, address, port_tries, secure, reset, accounts, require_login, server_pool, ulimit, timeout, open_viewer, sagetex_path, start_path, fork, quiet)
    269     if open_viewer:
    270         "Open viewer automatically isn't fully implemented.  You have to manually open your web browser to the above URL."
--> 271     return run(port)
    272 
    273 

/home/was/s/local/lib/python2.5/site-packages/sage/server/notebook/run_notebook.py in run(port)
    253             e = os.system(cmd)
    254         if e == 256:
--> 255             raise socket.error
    256         return True
    257         # end of inner function run

error: 

```



---

Comment by AlexGhitza created at 2009-01-23 02:50:29

Changing type from defect to enhancement.


---

Comment by was created at 2009-11-19 21:41:47

Changing type from enhancement to defect.


---

Comment by was created at 2009-11-19 21:45:13

Resolution: fixed


---

Comment by was created at 2009-11-19 21:45:13

I definitely cannot replicate this on sage.math, even using sudo to login as craig.    Everything seems to work fine.   So evidently it is already fixed.
