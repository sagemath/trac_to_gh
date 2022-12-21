# Issue 2359: notebook -- make it so when you send a kill signal to the notebook server it saves state

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-01 06:18:26

Assignee: boothby

Kill signal does this

```
2008/03/01 01:10 -0500 [-] Received SIGTERM, shutting down.
2008/03/01 01:10 -0500 [-] (Port 8000 Closed)
2008/03/01 01:10 -0500 [-] Stopping factory <twisted.web2.channel.http.HTTPFactory instance at 0x2a41530>
2008/03/01 01:10 -0500 [-] Main loop terminated.
2008/03/01 01:10 -0500 [-] Server Shut Down.
```


Control C does this

```
2008/03/01 01:12 -0500 [-] (Notebook cleanly saved. Press control-C again to exit.)
```


We should change the notebook so it catches the kill and saves the notebook cleanly.   I have no idea how to do this.  Maybe some sort of "hook" into Twisted.  If anybody knows twisted or reads the docs and figures this out, post here!


---

Comment by jason created at 2008-03-01 20:27:02

The python atexit module might help here:

http://docs.python.org/lib/module-atexit.html


---

Comment by yi created at 2008-03-03 21:40:38

If you want to do things the twisted way, here is something that should work:

reactor.addSystemEventTrigger('before', 'shutdown', f)

f is a function you want to be called BEFORE the reactor shuts down.  Here is some more documentation about how to properly use this feature:

http://twistedmatrix.com/documents/current/api/twisted.internet.interfaces.IReactorCore.html#addSystemEventTrigger

Cheers,
Yi

http://yiqiang.org


---

Comment by was created at 2008-05-11 07:12:21

The attached patch fixes the issues:

{{{ 
   1. I followed Yi's suggestion which worked like a charm.
   2. As a bonus I also fixed the "have to hit control-c twice to stop the notebook server" crap. Now
      it stops just fine with one single control-c.
   3. I changed twistd.pd to twistd.pid  -- it's a typo since it's supposed to be a pin id.
}}}


---

Comment by yi created at 2008-05-11 17:12:05

A couple of comments:

1) As far as I can tell the last bit of the patch (involving polynomials) has nothing to do with this issue. Could you explain what that does?

2) Is save_notebook() only used on shutdown? Isn't it possible that in the future, someone would want to call save_notebook while the notebook is running? If that's true, you probably do not want to call reactor.stop() in save_notebook unless you're _certain_ that save_notebook() is the last thing you want to do. 

Besides that this patch looks great!


---

Comment by boothby created at 2008-05-12 05:40:55

Removed polynomial garbage


---

Attachment

works for me -- I uploaded a cleaned up patch.


---

Comment by mabshoff created at 2008-05-12 11:11:32

Resolution: fixed


---

Comment by mabshoff created at 2008-05-12 11:11:32

Merged in Sage 3.0.2.alpha1
