# Issue 2346: Sage needs a simple api for interaction with other applications

Issue created by migration from https://trac.sagemath.org/ticket/2346

Original creator: robertwb

Original creation time: 2008-02-28 08:53:49

Assignee: was

Many people have shown interest in a simple API that could be used to interface with Sage. This would be useful for java applets, moodle plugins, and other applications to use Sage as a computational back end. 


---

Attachment


---

Comment by robertwb created at 2008-02-28 08:57:06

The above bundle implements a simple api over http as described in http://groups.google.com/group/sage-edu/browse_thread/thread/f2935bb4ddb72dc5

It should be completely useable in its current form, though of course there is lots of room for improvement.


---

Comment by robertwb created at 2008-02-28 08:57:21

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-02-28 08:57:21

Changing status from new to assigned.


---

Comment by mhansen created at 2008-02-28 09:56:24

A few comments:

1) Other than an unknown parent message, this applies cleanly against 2.10.3.alpha0

2) I can't get the server/simple/twisted.py tests to pass.  The following error causes all the problems:


```
 IOError: [Errno url error] unknown url type: 'https'
```


Other than that, this patch looks excellent!


---

Comment by yi created at 2008-02-28 16:15:52

the function wait_for_comp could probably make use of twisted.internet.task.LoopingCall versus basically scheduling your own callbacks. See the API documentation here:

http://twistedmatrix.com/documents/current/api/twisted.internet.task.LoopingCall.html

Other than that it looks good.


---

Comment by robertwb created at 2008-03-07 18:25:21

I'll look into the looping call thing more, but if it's what I think it is I'm not sure it satisfies all my needs. 

The Errno url error is strange, does your urllib not support secure http connections?


---

Attachment

I've re-implemented the waiting using LoopingCall, and also reduced the amount of time it spends blocking waiting for Sage input. 

I'm not sure what to do about the https error--we don't want to doctest with http as that would be a potential security vulnerability. 

mhansen: what system are you getting that error on. Is it the Sage python?


---

Comment by robertwb created at 2008-03-30 00:16:00

Perhaps we can use http://twistedmatrix.com/documents/current/api/twisted.web.client.html

(Need to do the same gnu-tls vs. OpenSSL trick as for the notebook.)


---

Attachment


---

Comment by robertwb created at 2008-04-06 04:43:49

Using twisted.web.client with the reactor and all is a major pain to do interactively (e.g. for doctests), but I was able to get it to fall back to gnutls if socket.ssl (from openssl) is not available.


---

Attachment


---

Comment by mhansen created at 2008-04-06 05:30:37

Everything works for me.  Apply the bundle and all three patches.


---

Comment by mabshoff created at 2008-04-06 06:05:45

Resolution: fixed


---

Comment by mabshoff created at 2008-04-06 06:05:45

Merged the bundle as well as the three patches in Sage 3.0.alpha2
