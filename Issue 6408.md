# Issue 6408: notebook -- secure notebook doesn't work in sage-4.1.alpha1 because of twisted.web2 not being ported to python 2.6

Issue created by migration from https://trac.sagemath.org/ticket/6408

Original creator: was

Original creation time: 2009-06-25 15:23:55

Assignee: mhansen


```
sage: notebook('foobar',secure=True,address='geom.math.washington.edu')
The notebook files are stored in: foobar
******************************************************************
*                                                                *
* Open your web browser to https://geom.math.washington.edu:8000 *
*                                                                *
******************************************************************
There is an admin account.  If you do not remember the password,
quit the notebook and type notebook(reset=True).
/space/rlm/new_r/sage-4.1.alpha0/local/lib/python2.6/site-packages/twisted/persisted/sob.py:12: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import os, md5, sys
2009-06-25 08:17:28-0700 [-] Log opened.
2009-06-25 08:17:28-0700 [-] twistd 8.2.0 (/space/rlm/new_r/sage-4.1.alpha0/local/bin/python 2.6.2) starting up.
2009-06-25 08:17:28-0700 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2009-06-25 08:17:28-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8000
2009-06-25 08:17:28-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x3e2b098>
xprop:  unable to open display ''
2009-06-25 08:17:28-0700 [twisted.web2.channel.http.HTTPFactory] Unhandled Error
        Traceback (most recent call last):
          File "/space/rlm/new_r/sage-4.1.alpha0/local/lib/python2.6/site-packages/twisted/python/log.py", line 69, in callWithContext
            return context.call({ILogContext: newCtx}, func, *args, **kw)
          File "/space/rlm/new_r/sage-4.1.alpha0/local/lib/python2.6/site-packages/twisted/python/context.py", line 59, in callWithContext
            return self.currentContext().callWithContext(ctx, func, *args, **kw)
          File "/space/rlm/new_r/sage-4.1.alpha0/local/lib/python2.6/site-packages/twisted/python/context.py", line 37, in callWithContext
            return func(*args,**kw)
          File "/space/rlm/new_r/sage-4.1.alpha0/local/lib/python2.6/site-packages/twisted/internet/selectreactor.py", line 146, in _doReadOrWrite
            why = getattr(selectable, method)()
        --- <exception caught here> ---
          File "/space/rlm/new_r/sage-4.1.alpha0/local/lib/python2.6/site-packages/twisted/internet/tcp.py", line 938, in doRead
            transport = self.transport(skt, protocol, addr, self, s, self.reactor)
        exceptions.TypeError: __init__() takes exactly 6 arguments (7 given)

```



---

Comment by was created at 2009-07-09 05:31:27

The new spkg that fixes this problem is here:

 http://sage.math.washington.edu/home/wstein/patches/python_gnutls-1.1.4.p5.spkg


---

Comment by was created at 2009-07-09 19:08:46

To referee this: just compre _init_.py with the version in src/
You'll see there is a 2-line trivial obvious change.
Then just try installing the spkg and see that the secure notebook suddenly works again.
That's it.


```
teragon-2:python_gnutls-1.1.4.p5 wstein$ diff src/gnutls/interfaces/twisted/__init__.py  patches/__init__.py 
251c251
<     def __init__(self, sock, protocol, client, server, sessionno):
---
>     def __init__(self, sock, protocol, client, server, sessionno, reactor):
254c254
<         tcp.Server.__init__(self, sock, protocol, client, server, sessionno)
---
>         tcp.Server.__init__(self, sock, protocol, client, server, sessionno, reactor)
```



---

Comment by rlm created at 2009-07-09 19:10:37

Why not? :)


---

Comment by rlm created at 2009-07-09 19:10:37

Resolution: fixed
