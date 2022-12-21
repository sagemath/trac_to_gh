# Issue 5675: notebook with address="" option should set the address to something useful

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-03 13:27:21

Assignee: boothby

CC:  acleone


```
On Thu, 02 Apr 2009 at 11:53PM -0700, Ondrej Certik wrote:
>
> Hi,
>
[...]
> sage: notebook(secure=False, address="")
> [...]
>
> and it starts firefox on the local machine with this address:
>
> http://[www.:8000.com]/?startup_token=41e2a34e89e40139333a8113e9be2a50
>
> which obviously fails. This also happens with sage 3.2.3 (I didn't try
> other versions).

This has been around for a while; I haven't filed a ticket for it, since
I just retype the URL.
```


It used to be in the notebook that address="" was an error.  Then when we switched to twisted, it suddenly meant "listen on all interfaces".  Now it's a common option to give.  

The two places I know of where the address is given are: (1) when popping up a web browser pointed at the notebook, and (2) when publishing a worksheet and it shows the URL where people can get the published version.

Ideas:
   * If one gives address="", everywhere else, set the address to the fully qualified domain name.  How to get that in Python?
   * If one gives address="", simply never automatically pop up a viewer, and doesn't display the URL for published worksheets (since it is wrong).  If people want proper URL's they shouldn't be lazy with their address= option.
   * Make address="" an error, and require the user to give a proper fully qualified name.


---

Comment by mpatel created at 2009-08-10 09:35:41

This ticket subsumes #5263.


---

Comment by mpatel created at 2010-01-16 06:49:39

There is [socket.getfqdn](http://docs.python.org/library/socket.html#socket.getfqdn), but does it help?  On `boxen`:

```python
sage: import socket
sage: socket.getfqdn()
'localhost'
sage: socket.gethostbyname_ex(socket.gethostname())
('localhost', ['boxen', 'boxen'], ['127.0.0.1', '128.208.160.197'])
```

On a local Linux machine, I get

```python
sage: import socket
sage: socket.getfqdn()
'localhost.localdomain'
sage: socket.gethostbyname_ex(socket.gethostname())
('localhost.localdomain', ['localhost', 'foo'], ['127.0.0.1'])
```

all of which happen to be in `/etc/hosts`.

What if we just add an option `published_host=_` (or a variation) and insert it into URLs for published (and remote!) worksheets when `interface=_`?  We could print a warning or raise an error, if both are left empty.


---

Comment by timdumol created at 2010-01-19 06:24:04

Renaming this to a more appropriate title.


---

Attachment

This sets the hostname to localhost if interface="" when launching the page


---

Comment by timdumol created at 2010-01-19 06:31:34

This fixes the issue described.


---

Comment by timdumol created at 2010-01-19 06:31:34

Changing status from new to needs_review.


---

Comment by acleone created at 2010-01-19 23:03:08

LGTM.  See #5263.  This bug is only for a blank option passed to `sage -n interface=''`.


---

Comment by acleone created at 2010-01-19 23:03:08

Changing status from needs_review to positive_review.


---

Comment by acleone created at 2010-01-19 23:15:23

I see a few cases:
1. The user starts the server on his/her computer.  localhost works fine
2. The user starts the server on a network computer via ssh, in which case the browser should probably auto-open to whatever address the user used to ssh into computer.  However we can't get this information, and last time I tried firefox doesn't open anyway (when starting the notebook in an ssh session).

See #5263 for the publish url bug.


---

Comment by mpatel created at 2010-01-25 01:03:31

Resolution: fixed
