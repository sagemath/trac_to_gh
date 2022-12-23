# Issue 4894: [with patch; needs review] save_session -- bug when saving %cython functions, etc.

Issue created by migration from https://trac.sagemath.org/ticket/4894

Original creator: was

Original creation time: 2008-12-30 22:51:08

Assignee: boothby

I was easily able to replicate the following:

```
M. Yurko
 to sage-support
	
show details 1:32 PM (1 hour ago)
	
	
Reply
	
	

I have recently been using save_session a bit, and I uncovered what I
believe is a bug. If the worksheet of the session that I'm trying to
save contains a cython function, then load_session chokes. For
example:

var1 = 1
var2 = 2
var3 = srange(1,10000)
var4 = range(1,3000)
var5 = 1234.123456

%cython
def test(double x):
   return x

save_session('test_session')

and then I save and exit, and re-enter the worksheet

load_session('test_session')

and I get

Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/home/myurko/.sage/sage_notebook/worksheets/admin/28/code/
1.py", line 6, in <module>
   load_session(\u0027test_session\u0027)
 File "/home/myurko/sage-3.2.1/local/lib/python2.5/site-packages/
SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>

 File "session.pyx", line 300, in sage.misc.session.load_session
(sage/misc/session.c:1403)
 File "sage_object.pyx", line 477, in sage.structure.sage_object.load
(sage/structure/sage_object.c:4865)
 File "sage_object.pyx", line 598, in
sage.structure.sage_object.loads (sage/structure/sage_object.c:6121)
RuntimeError: No module named
_home_myurko__sage_sage_notebook_worksheets_admin_28_code_sage8_spyx_0
invalid data stream
invalid load key, 'x'.
Unable to load pickled data.

When I ran save_session with verbose = true, I noticed that it saved
test, which according to the docstring shouldn't have happened. Does
anyone have any workarounds for this issue?
```



---

Comment by was created at 2008-12-30 23:08:21

The attached patch fixes the problem by explicitly not saving builtin (or not)) functions or classes, since in fact defining classes also breaks load_session and save_session.

It just occurred to me that one can still make sessions that can't be reloaded.  E.g.,

```
class Foo:
    pass

f = Foo()
```


Then save_session followed by quit and load_session fails.  However, I doubt there is any good way to deal with this.  Fortunately, in the above case, unlike in the case that this bug is about, one can simply re-evaluate the code to define Foo, and suddenly load_session works fine. 
I've put a comment abou this in the patch.


---

Attachment


---

Comment by mabshoff created at 2009-01-03 06:01:39

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-03 06:01:51

Merged in Sage 3.2.3.final


---

Comment by mabshoff created at 2009-01-03 06:01:51

Resolution: fixed
