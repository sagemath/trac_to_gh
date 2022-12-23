# Issue 9829: SageNB: Bad Request. Maximum length of 102400 bytes exceeded.

Issue created by migration from https://trac.sagemath.org/ticket/9830

Original creator: mpatel

Original creation time: 2010-08-28 07:44:03

Assignee: jason, was

CC:  schymans jhpalmieri

Reported by Stan Schymanski on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/c814c8cf7bc7dd87):

```
When trying to change the code of a worksheet in a text editor (using
the edit button in the worksheet), I get the following error message
whenever I want to save changes:

Bad Request
Maximum length of 102400 bytes exceeded.

Does anyone have an idea what could cause this and how this can be
circumvented?
```

Didier Deshommes replied:

```
My guess is that the web server has a limit on the size of a POST
request and that you have reached it. Typically this is 1024kb. The
solution is to increase this limit. I'm not sure how to do that for a 
wsgi application (which I assume sage is). 
```



---

Comment by mpatel created at 2010-08-28 07:50:39

We can fix this by adjusting `twisted.web2.resource.PostableResource.maxMem` near the top of `sagenb.notebook.twist`.

For now, if you have write access to your Sage distribution, you can do this yourself by putting, e.g.,

```python
resource.PostableResource.maxMem = 1000 * 1024
```

just after

```python
from twisted.web2 import server, http, resource, channel
```

near the top of 

```
SAGE_ROOT/local/lib/python2.6/site-packages/sagenb-*-py2.6.egg/sagenb/notebook/twist.py
```

and restarting the notebook server.

Here's the beginning of the class definition:

```python
class PostableResource(Resource):
    """
    A L{Resource} capable of handling the POST request method.

    @cvar maxMem: maximum memory used during the parsing of the data.
    @type maxMem: C{int}
    @cvar maxFields: maximum number of form fields allowed.
    @type maxFields: C{int}
    @cvar maxSize: maximum size of the whole post allowed.
    @type maxSize: C{int}
    """
    maxMem = 100 * 1024
    maxFields = 1024
    maxSize = 10 * 1024 * 1024

    def http_POST(self, request):
[...]
```



---

Comment by schymans created at 2011-05-19 18:17:38

The work-around does not seem to work any more as of 4.6.2.


---

Comment by chapoton created at 2020-03-28 10:02:45

old ticket about deprecated sagenb. Can we close ?


---

Comment by chapoton created at 2020-03-28 10:02:45

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2020-03-28 16:39:49

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-03-28 17:11:25

Resolution: invalid
