# Issue 9327: Bugs in the Simple Sage Server API of sagenb

Issue created by migration from Trac.

Original creator: dpoetzsch

Original creation time: 2010-06-24 12:22:29

Assignee: jason, was

CC:  robertwb jason

Keywords: simple twist

I found (and fixed) the following bugs in the file local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/simple/twist.py:

* When trying to login via the Simple Sage Server API using the sagenb.notebook.notebook_object module the following error came up:
....
/sagenb-0.8-py2.6.egg/sagenb/simple/twist.py, line 206, in render
   U = notebook_twist.notebook.user(username)
exceptions.AttributeError: 'NoneType' object has no attribute 'user'
--------------------------------------------------------------------
The problem is: The sagenb twist.py module still imports the (old and unmaintained) sage.server modules instead of the new sagenb files. It is quite logical that there is a NoneType error because there is no server started that relies on the (imported) old files.
If the two imports from sage.server in twist.py are replaced with the sagenb modules at least the login via Simple Sage Server API works quite fine.

* When login works there is another bug: On line 286 in the twist.py file where it says "return http.Response(..." the stream variable has to be converted into a string (twisted somehow seems to have problems with unicode characters because IByteStream(stream) which is called in http.Response() fails with a TypeError if stream is of type 'unicode').


---

Comment by jason created at 2010-06-27 03:50:57

Could you post patches or new versions of the affected files?  After your fixes, does the simple API seem to work?

The simple API is important for the remote sagetex feature to work.


---

Comment by dpoetzsch created at 2010-06-28 08:31:32

For my purposes the simple API seems to work after applying my fixes (this is logging in, computing stuff, logging out).


---

Attachment

The bugfixes mentioned above as a patch file


---

Comment by dpoetzsch created at 2010-06-28 08:33:14

The new file including the fixes


---

Comment by rlm created at 2010-07-06 11:53:53

Changing status from new to needs_review.


---

Attachment


---

Comment by jason created at 2010-09-28 19:42:38

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-09-28 19:42:38

This seems to work great!  Remote Sagetex works, for example.

Another ticket would be deleting the verbose output in the server logs anytime something is executed.


---

Comment by mpatel created at 2010-10-04 01:34:48

Resolution: fixed


---

Comment by mpatel created at 2010-10-08 22:26:04

David, could you add yourself to [the account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?
