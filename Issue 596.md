# Issue 596: sage wiki() doesn't close with ctl-C

Issue created by migration from https://trac.sagemath.org/ticket/596

Original creator: wdj

Original creation time: 2007-09-05 22:18:22

Assignee: was

When I execute

```
sage: wiki()
```


I get ...

```
* Open your web browser to http://localhost:9000
...
```

and it works fine.  Then how do I close it cleanly?

I've tried ctrl-C in the sage window, which gives the following...
It closes that web window but then restarts the wiki.


```
2007/09/05 13:47 -0700 [-] Received SIGINT, shutting down.
2007/09/05 13:47 -0700 [-] (Port 9000 Closed)
2007/09/05 13:47 -0700 [-] Stopping factory
<MoinMoin.server.twistedmoin.MoinSite instance at 0x4060ebec>
2007/09/05 13:47 -0700 [-] Main loop terminated.
2007/09/05 13:47 -0700 [-] Server Shut Down.
Port 9000 is already in use.  Trying next port...
**************************************************
*                                                *
* Open your web browser to http://localhost:9001 *
*                                                *
**************************************************
2007/09/05 13:47 -0700 [-] Log opened.
```

etc.

Closing the webpage first doesn't help and SAGE doesn't accept any
commands
other than ctrl-C, including ctrl-D.

Apparently Ctl-C Ctl-C (twice in rapid succession) closes it.

Reported by rjleveque`@`gmail.com (Randy Leveque)


---

Comment by was created at 2007-09-05 22:53:30

Changing component from algebraic geometry to website/wiki.


---

Comment by was created at 2007-09-05 22:53:30

I can't replicate this:

```
sage: wiki()
**************************************************
*                                                *
* Open your web browser to http://localhost:9000 *
*                                                *
**************************************************
2007/09/05 15:49 -0700 [-] Log opened.
2007/09/05 15:49 -0700 [-] twistd 2.5.0 (/home/was/s/local/bin/python 2.5.1) starting up
2007/09/05 15:49 -0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2007/09/05 15:49 -0700 [-] Loading twistedconf.py...
2007/09/05 15:49 -0700 [-] Loaded.
2007/09/05 15:49 -0700 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9000
2007/09/05 15:49 -0700 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0xb9e998>
2007/09/05 15:49 -0700 [-] set uid/gid 1000/1000
2007/09/05 15:49 -0700 [-] Received SIGINT, shutting down.
2007/09/05 15:49 -0700 [-] (Port 9000 Closed)
2007/09/05 15:49 -0700 [-] Stopping factory <MoinMoin.server.twistedmoin.MoinSite instance at 0xb9e998>
2007/09/05 15:49 -0700 [-] Main loop terminated.
2007/09/05 15:49 -0700 [-] Server Shut Down.
True
sage:       
```



---

Comment by mabshoff created at 2007-09-30 22:11:31

This might have been fixed by the sig off/on fix.

Retagged for 2.8.6 - if it isn't fixed yet it might get retagged again.

Cheers,

Michael


---

Comment by was created at 2007-10-12 06:03:59

Can anybody replicate this?


---

Comment by was created at 2007-10-13 07:36:16

Resolution: wontfix


---

Comment by was created at 2007-11-02 18:30:24

I now see this on OS X 10.5 and it is easy to replicate, so I am re-opening this. 

The problem somehow probably involves the codes that indicate a port is in use. 

 -- William


---

Comment by was created at 2007-11-02 18:30:24

Resolution changed from wontfix to 


---

Comment by was created at 2007-11-02 18:30:24

Changing status from closed to reopened.


---

Comment by rlm created at 2008-02-10 03:16:36

This is duplicated in #1871.


---

Comment by rlm created at 2008-02-10 03:16:36

Resolution: duplicate
