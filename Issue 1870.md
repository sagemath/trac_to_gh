# Issue 1870: somehow we completely broke the moinmoin wiki stuff included in Sage on OS X.

Issue created by migration from https://trac.sagemath.org/ticket/1870

Original creator: was

Original creation time: 2008-01-20 22:12:58

Assignee: was

Try this with a fresh sage-2.10.  I've only tested this on my osx laptop so far. 
This does not fail on Linux (sage.math.washington.edu at least). 


```
sage: wiki()
**************************************************
*                                                *
* Open your web browser to http://localhost:9000 *
*                                                *
**************************************************
2008/01/20 15:08 -0700 [-] Log opened.
2008/01/20 15:08 -0700 [-] twistd 2.5.0 (/Users/was/s/local/bin/python 2.5.1) starting up
2008/01/20 15:08 -0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008/01/20 15:08 -0700 [-] Loading twistedconf.py...
2008/01/20 15:08 -0700 [-] Loaded.
2008/01/20 15:08 -0700 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9000
2008/01/20 15:08 -0700 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x7aecb0>
2008/01/20 15:08 -0700 [-] Traceback (most recent call last):
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/bin/twistd", line 21, in <module>
2008/01/20 15:08 -0700 [-]     run()
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/scripts/twistd.py", line 27, in run
2008/01/20 15:08 -0700 [-]     app.run(runApp, ServerOptions)
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/application/app.py", line 379, in run
2008/01/20 15:08 -0700 [-]     runApp(config)
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/scripts/twistd.py", line 23, in runApp
2008/01/20 15:08 -0700 [-]     _SomeApplicationRunner(config).run()
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/application/app.py", line 158, in run
2008/01/20 15:08 -0700 [-]     self.postApplication()
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/scripts/_twistd_unix.py", line 213, in postApplication
2008/01/20 15:08 -0700 [-]     startApplication(self.config, self.application)
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/scripts/_twistd_unix.py", line 182, in startApplication
2008/01/20 15:08 -0700 [-]     shedPrivileges(config['euid'], uid, gid)
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/scripts/_twistd_unix.py", line 148, in shedPrivileges
2008/01/20 15:08 -0700 [-]     switchUID(uid, gid, euid)
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/python/util.py", line 651, in switchUID
2008/01/20 15:08 -0700 [-]     initgroups(uid, gid)
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/python/util.py", line 621, in initgroups
2008/01/20 15:08 -0700 [-]     _setgroups_until_success(l)
2008/01/20 15:08 -0700 [-]   File "/Users/was/s/local/lib/python2.5/site-packages/twisted/python/util.py", line 575, in _setgroups_until_success
2008/01/20 15:08 -0700 [-]     setgroups(l)
2008/01/20 15:08 -0700 [-] OSError: [Errno 1] Operation not permitted
True
```



---

Comment by rlm created at 2009-03-06 10:32:07

I think this ticket is invalid. `wiki()` works fine for me, in 
Sage 3.3 without
 and 3.4.rc0 with 
the new moin spkg installed, on OSX 10.5.

Someone else (was?) please verify so we can close this ticket.


---

Comment by kcrisman created at 2009-12-28 17:56:15

This has gotten fantastically worse - at least on 4.3 on Macintel!  Check this out - I had to close the window manually, as Ctrl-C and Ctrl-D did absolutely nothing.   The only thing I can think about why this wouldn't be valid is that maybe I have bad permissions? 

Also, why is it still in the sage_wiki folder and not in .sage/sage_wiki or something similar to what is now done with the notebook?

```
sage: wiki()
/Users/.../sage-4.3/local/lib/python2.6/site-packages/MoinMoin/user.py:9: DeprecationWarning: the sha module is deprecated; use the hashlib module instead
  import os, time, sha, codecs
**************************************************
*                                                *
* Open your web browser to http://localhost:9000 *
*                                                *
**************************************************
/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/spread/pb.py:30: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import md5
/Users/.../sage-4.3/local/lib/python2.6/site-packages/MoinMoin/user.py:9: DeprecationWarning: the sha module is deprecated; use the hashlib module instead
  import os, time, sha, codecs
2009-12-28 12:27:23-0500 [-] Log opened.
2009-12-28 12:27:23-0500 [-] twistd 8.2.0 (/Users/.../sage-4.3/local/bin/python 2.6.2) starting up.
2009-12-28 12:27:23-0500 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2009-12-28 12:27:23-0500 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9000
2009-12-28 12:27:23-0500 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x1268b70>
2009-12-28 12:27:23-0500 [-] Traceback (most recent call last):
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/bin/twistd", line 21, in <module>
2009-12-28 12:27:23-0500 [-]     run()
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 27, in run
2009-12-28 12:27:23-0500 [-]     app.run(runApp, ServerOptions)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 694, in run
2009-12-28 12:27:23-0500 [-]     runApp(config)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 23, in runApp
2009-12-28 12:27:23-0500 [-]     _SomeApplicationRunner(config).run()
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 423, in run
2009-12-28 12:27:23-0500 [-]     self.postApplication()
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 206, in postApplication
2009-12-28 12:27:23-0500 [-]     self.startApplication(self.application)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 319, in startApplication
2009-12-28 12:27:23-0500 [-]     self.shedPrivileges(self.config['euid'], uid, gid)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 290, in shedPrivileges
2009-12-28 12:27:23-0500 [-]     switchUID(uid, gid, euid)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 663, in switchUID
2009-12-28 12:27:23-0500 [-]     initgroups(uid, gid)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 640, in initgroups
2009-12-28 12:27:23-0500 [-]     _setgroups_until_success(l)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 586, in _setgroups_until_success
2009-12-28 12:27:23-0500 [-]     setgroups(l)
2009-12-28 12:27:23-0500 [-] OSError: [Errno 1] Operation not permitted
Port 9000 is already in use.  Trying next port...
**************************************************
*                                                *
* Open your web browser to http://localhost:9001 *
*                                                *
**************************************************
Removing stale pidfile /Users/.../sage_wiki/twistd.pid
/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/spread/pb.py:30: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import md5
/Users/.../sage-4.3/local/lib/python2.6/site-packages/MoinMoin/user.py:9: DeprecationWarning: the sha module is deprecated; use the hashlib module instead
  import os, time, sha, codecs
2009-12-28 12:27:23-0500 [-] Log opened.
2009-12-28 12:27:23-0500 [-] twistd 8.2.0 (/Users/.../sage-4.3/local/bin/python 2.6.2) starting up.
2009-12-28 12:27:23-0500 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2009-12-28 12:27:23-0500 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9001
2009-12-28 12:27:23-0500 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x1268b70>
2009-12-28 12:27:23-0500 [-] Traceback (most recent call last):
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/bin/twistd", line 21, in <module>
2009-12-28 12:27:23-0500 [-]     run()
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 27, in run
2009-12-28 12:27:23-0500 [-]     app.run(runApp, ServerOptions)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 694, in run
2009-12-28 12:27:23-0500 [-]     runApp(config)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 23, in runApp
2009-12-28 12:27:23-0500 [-]     _SomeApplicationRunner(config).run()
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 423, in run
2009-12-28 12:27:23-0500 [-]     self.postApplication()
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 206, in postApplication
2009-12-28 12:27:23-0500 [-]     self.startApplication(self.application)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 319, in startApplication
2009-12-28 12:27:23-0500 [-]     self.shedPrivileges(self.config['euid'], uid, gid)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 290, in shedPrivileges
2009-12-28 12:27:23-0500 [-]     switchUID(uid, gid, euid)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 663, in switchUID
2009-12-28 12:27:23-0500 [-]     initgroups(uid, gid)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 640, in initgroups
2009-12-28 12:27:23-0500 [-]     _setgroups_until_success(l)
2009-12-28 12:27:23-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 586, in _setgroups_until_success
2009-12-28 12:27:23-0500 [-]     setgroups(l)
2009-12-28 12:27:23-0500 [-] OSError: [Errno 1] Operation not permitted
Port 9000 is already in use.  Trying next port...
**************************************************
*                                                *
* Open your web browser to http://localhost:9002 *
*                                                *
**************************************************
Removing stale pidfile /Users/.../sage_wiki/twistd.pid
/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/spread/pb.py:30: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import md5
/Users/.../sage-4.3/local/lib/python2.6/site-packages/MoinMoin/user.py:9: DeprecationWarning: the sha module is deprecated; use the hashlib module instead
  import os, time, sha, codecs
2009-12-28 12:27:24-0500 [-] Log opened.
2009-12-28 12:27:24-0500 [-] twistd 8.2.0 (/Users/.../sage-4.3/local/bin/python 2.6.2) starting up.
2009-12-28 12:27:24-0500 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2009-12-28 12:27:24-0500 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9002
2009-12-28 12:27:24-0500 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x1268b70>
2009-12-28 12:27:24-0500 [-] Traceback (most recent call last):
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/bin/twistd", line 21, in <module>
2009-12-28 12:27:24-0500 [-]     run()
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 27, in run
2009-12-28 12:27:24-0500 [-]     app.run(runApp, ServerOptions)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 694, in run
2009-12-28 12:27:24-0500 [-]     runApp(config)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 23, in runApp
2009-12-28 12:27:24-0500 [-]     _SomeApplicationRunner(config).run()
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 423, in run
2009-12-28 12:27:24-0500 [-]     self.postApplication()
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 206, in postApplication
2009-12-28 12:27:24-0500 [-]     self.startApplication(self.application)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 319, in startApplication
2009-12-28 12:27:24-0500 [-]     self.shedPrivileges(self.config['euid'], uid, gid)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 290, in shedPrivileges
2009-12-28 12:27:24-0500 [-]     switchUID(uid, gid, euid)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 663, in switchUID
2009-12-28 12:27:24-0500 [-]     initgroups(uid, gid)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 640, in initgroups
2009-12-28 12:27:24-0500 [-]     _setgroups_until_success(l)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 586, in _setgroups_until_success
2009-12-28 12:27:24-0500 [-]     setgroups(l)
2009-12-28 12:27:24-0500 [-] OSError: [Errno 1] Operation not permitted
Port 9000 is already in use.  Trying next port...
**************************************************
*                                                *
* Open your web browser to http://localhost:9003 *
*                                                *
**************************************************
Removing stale pidfile /Users/.../sage_wiki/twistd.pid
/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/spread/pb.py:30: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import md5
/Users/.../sage-4.3/local/lib/python2.6/site-packages/MoinMoin/user.py:9: DeprecationWarning: the sha module is deprecated; use the hashlib module instead
  import os, time, sha, codecs
2009-12-28 12:27:24-0500 [-] Log opened.
2009-12-28 12:27:24-0500 [-] twistd 8.2.0 (/Users/.../sage-4.3/local/bin/python 2.6.2) starting up.
2009-12-28 12:27:24-0500 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2009-12-28 12:27:24-0500 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9003
2009-12-28 12:27:24-0500 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x1268b70>
2009-12-28 12:27:24-0500 [-] Traceback (most recent call last):
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/bin/twistd", line 21, in <module>
2009-12-28 12:27:24-0500 [-]     run()
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 27, in run
2009-12-28 12:27:24-0500 [-]     app.run(runApp, ServerOptions)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 694, in run
2009-12-28 12:27:24-0500 [-]     runApp(config)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 23, in runApp
2009-12-28 12:27:24-0500 [-]     _SomeApplicationRunner(config).run()
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 423, in run
2009-12-28 12:27:24-0500 [-]     self.postApplication()
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 206, in postApplication
2009-12-28 12:27:24-0500 [-]     self.startApplication(self.application)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 319, in startApplication
2009-12-28 12:27:24-0500 [-]     self.shedPrivileges(self.config['euid'], uid, gid)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 290, in shedPrivileges
2009-12-28 12:27:24-0500 [-]     switchUID(uid, gid, euid)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 663, in switchUID
2009-12-28 12:27:24-0500 [-]     initgroups(uid, gid)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 640, in initgroups
2009-12-28 12:27:24-0500 [-]     _setgroups_until_success(l)
2009-12-28 12:27:24-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 586, in _setgroups_until_success
2009-12-28 12:27:24-0500 [-]     setgroups(l)
2009-12-28 12:27:24-0500 [-] OSError: [Errno 1] Operation not permitted
Port 9000 is already in use.  Trying next port...
**************************************************
*                                                *
* Open your web browser to http://localhost:9004 *
*                                                *
**************************************************
Removing stale pidfile /Users/.../sage_wiki/twistd.pid
/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/spread/pb.py:30: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import md5
/Users/.../sage-4.3/local/lib/python2.6/site-packages/MoinMoin/user.py:9: DeprecationWarning: the sha module is deprecated; use the hashlib module instead
  import os, time, sha, codecs
2009-12-28 12:27:25-0500 [-] Log opened.
2009-12-28 12:27:25-0500 [-] twistd 8.2.0 (/Users/.../sage-4.3/local/bin/python 2.6.2) starting up.
2009-12-28 12:27:25-0500 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2009-12-28 12:27:25-0500 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9004
2009-12-28 12:27:25-0500 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x1268b70>
2009-12-28 12:27:25-0500 [-] Traceback (most recent call last):
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/bin/twistd", line 21, in <module>
2009-12-28 12:27:25-0500 [-]     run()
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 27, in run
2009-12-28 12:27:25-0500 [-]     app.run(runApp, ServerOptions)
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 694, in run
2009-12-28 12:27:25-0500 [-]     runApp(config)
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/twistd.py", line 23, in runApp
2009-12-28 12:27:25-0500 [-]     _SomeApplicationRunner(config).run()
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/application/app.py", line 423, in run
2009-12-28 12:27:25-0500 [-]     self.postApplication()
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 206, in postApplication
2009-12-28 12:27:25-0500 [-]     self.startApplication(self.application)
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 319, in startApplication
2009-12-28 12:27:25-0500 [-]     self.shedPrivileges(self.config['euid'], uid, gid)
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/scripts/_twistd_unix.py", line 290, in shedPrivileges
2009-12-28 12:27:25-0500 [-]     switchUID(uid, gid, euid)
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 663, in switchUID
2009-12-28 12:27:25-0500 [-]     initgroups(uid, gid)
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 640, in initgroups
2009-12-28 12:27:25-0500 [-]     _setgroups_until_success(l)
2009-12-28 12:27:25-0500 [-]   File "/Users/.../sage-4.3/local/lib/python2.6/site-packages/twisted/python/util.py", line 586, in _setgroups_until_success
2009-12-28 12:27:25-0500 [-]     setgroups(l)
2009-12-28 12:27:25-0500 [-] OSError: [Errno 1] Operation not permitted
Port 9000 is already in use.  Trying next port...
```



---

Comment by mpatel created at 2010-01-16 20:10:50

If it helps: There's new Moin Moin spkg at #3693.


---

Comment by timdumol created at 2010-01-16 23:10:13

#3693 fixes this.


---

Comment by mpatel created at 2010-01-21 10:27:40

Replying to [comment:2 kcrisman]:
> Also, why is it still in the sage_wiki folder and not in .sage/sage_wiki or something similar to what is now done with the notebook?

I'm not sure.  We do the same with `trac()` and the [optional] Trac spkg.  It makes sense to use a default directory under `DOT_SAGE`, but I think upgrading existing MoinMoin wikis can be problematic.


---

Comment by was created at 2010-01-21 16:57:26

Replying to [comment:5 mpatel]:
> Replying to [comment:2 kcrisman]:
> > Also, why is it still in the sage_wiki folder and not in .sage/sage_wiki or something similar to what is now done with the notebook?
> 
> I'm not sure.  We do the same with `trac()` and the [optional] Trac spkg.  It makes sense to use a default directory under `DOT_SAGE`, but I think upgrading existing MoinMoin wikis can be problematic.


When I wrote the wiki and trac command, there was no .sage/* folder, and the SAge notebook was stored in sage_notebook in the current directory.   The notebook has moved over to be in .sage, but nobody moved the wiki and trac yet.   It would be reasonable to do so.  HOWEVER, note that this would break all my wiki's, since a typical situation is:


```
sage@sagemath:~/wiki/sage$ ls
nohup.err  nohup.out  sage_wiki  start
sage@sagemath:~/wiki/sage$ more start
ulimit -v 2000000; nohup echo "wiki(port=9001, address='')" | sage-new  > nohup.out 2>nohup.err &
sage@sagemath:~/wiki/sage$
```


If you change the wiki to be in $HOME/.sage by default, then suddenly all my wiki's will get started on top of each other (hence all but one will fail to start). 

So it might be worth checking if there is a wiki directory "sage_wiki" in the current directory, and only if there isn't then default to $HOME/.sage/moinmoin.


---

Comment by was created at 2010-01-21 16:58:51

I've made updating where wiki() stores its file #8027.


---

Comment by mpatel created at 2010-02-11 14:25:21

Should be fixed by #3693.


---

Comment by mpatel created at 2010-02-11 14:25:21

Resolution: fixed
