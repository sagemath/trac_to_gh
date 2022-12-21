# Issue 5263: publishing a worksheet displays the URL without the hostname

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-02-14 02:16:51

Assignee: boothby

CC:  kcrisman was mpatel

When I publish a worksheet on sagenb.org, it says I can find the sheet at: http://:8000/home/pub/243

Of course, this is silly nonsense.

It might have to do with starting the notebook with address='', maybe?


---

Comment by TimothyClemans created at 2009-02-14 12:47:58

Yes it does use address. I just discovered that on my computer if I set address='sagenb.org' then I can't start the notebook.


---

Comment by mpatel created at 2009-08-10 09:35:56

#5675 appears to be a duplicate, but with wider scope.


---

Comment by jason created at 2009-08-10 14:17:33

I agree that this will probably be closed when #5675 is closed.  I think that when #5675 is closed, this ought to be checked, and then closed if everything works.


---

Comment by drkirkby created at 2009-12-21 11:02:24

It looks like this has been a long standing bug, which nobody has worked on. I would make two suggestion, though. 

Firstly, if this gets fixed, it would be sensible to detect the following range of IP addresses, and indicate they can not be routed over the internet. 

 * 10.x.x.x
 * 172.16.x.x to 172.31.x.x
 * 192.168.x.x

Secondly, perhaps a further reminder about the security risks would not go amiss either. 

Dave


---

Comment by mpatel created at 2010-01-16 04:44:23

Following the suggestions [here](http://groups.google.com/group/comp.lang.python/browse_thread/thread/d931cdc326d7032b?hl=en) and [here](http://stackoverflow.com/questions/166545/finding-a-public-facing-ip-address-in-python), I get:

```python
sage: import socket
sage: socket.gethostbyname(socket.gethostname())
'127.0.0.1'
sage: s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sage: s.connect(('google.com', 0))
sage: s.getsockname()[0]
'192.168.x.y'
sage: import urllib
sage: urllib.urlopen('http://whatismyip.org').read()
'a.b.c.d'
```

I'm looking now for ways to iterate over the available interfaces in Twisted...

By the way, there are a few suggestions to the main problem at #5675.

What is a good name for a keyword option that's inserted instead of the `interface` (post-#7639, `address` is deprecated) when `interface=''`?


---

Comment by mpatel created at 2010-01-16 06:29:32

Replying to [comment:6 mpatel]:
> I'm looking now for ways to iterate over the available interfaces in Twisted...
I _think_ Twisted just uses [socket](http://docs.python.org/library/socket.html), which 
uses the underlying system's socket library.  I don't know if there is a local, cross-platform way to iterate over `'0.0.0.0'` (all interfaces) and map each to an IP address.


---

Comment by timdumol created at 2010-01-19 00:33:28

I think using the [HTTP-HOST](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.23) header will be easier and more reliable. Here's a patch implementing that. Feel free to comment.


---

Comment by timdumol created at 2010-01-19 00:33:28

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-19 00:34:36

Uses the HTTP-HOST header to attempt to get the host name.


---

Attachment

Nice!


---

Comment by mpatel created at 2010-01-20 03:20:16

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-25 00:52:12

Resolution: fixed
