# Issue 436: http to https redirect for secure notebook

Issue created by migration from https://trac.sagemath.org/ticket/436

Original creator: nbruin

Original creation time: 2007-08-17 18:02:26

Assignee: boothby

Suppose a secure notebook is run on localhost:8000. Then presently, one has to type the URL `https://localhost:8000`. Would it be possible to let port localhost:8000 respond to plain http requests with a redirect to `https://localhost:8000` ? The advantage is that browsers like firefox complete `localhost:8000` to `http://localhost:8000`, and a lot of users (well, at least me) are used to this shortcut.


---

Comment by mabshoff created at 2007-08-22 21:41:13

Hello,

now that Sage defaults to https this might be a good idea to implement.

Cheers,

Michael


---

Comment by was created at 2007-11-03 15:18:38

I tried several times to figure out how to do this and couldn't.  SO, please figure out how to do it and post a patch!


---

Comment by was created at 2008-05-10 16:59:43

NOTE: The notebook now defaults to use http not https.


---

Comment by boothby created at 2009-06-16 19:49:08

This is a limitation of protocols / browsers.  Since HTTPS is merely HTTP over an SSL connection, a plaintext HTTP request looks like garbage to a HTTPS server and vice verse.  If your browser was smart enough to attempt to use SSL, that'd be fine.  However, we can't do this in Twisted because we only take one port -- an inbound connection is silently dropped by SSL, and Twisted never hears about it.  If we go to a two-port system, e.g. port 80 for http and 443 for https, then we'd be in business.  And perhaps that functionality should be implemented.

However, the issue of "user connects to port x with wrong protocol" is never going to go away.


---

Comment by was created at 2009-11-19 21:23:24

Resolution: invalid


---

Comment by was created at 2009-11-19 21:23:24

> However, the issue of "user connects to port x with wrong protocol" is never going to go away.

Tom is right.   I'm closing this ticket as invalid.
