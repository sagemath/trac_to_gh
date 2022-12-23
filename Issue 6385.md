# Issue 6385: Python relative import messes up Sage command line arguments

Issue created by migration from https://trac.sagemath.org/ticket/6385

Original creator: rlm

Original creation time: 2009-06-22 17:58:12

Assignee: tbd

From: 

http://groups.google.com/group/sage-devel/browse_thread/thread/a9e80289571de40e

On Mon, Jun 22, 2009 at 6:38 PM, Robert Miller<rlmills...`@`gmail.com> wrote:

> I tried running the Sage notebook as follows, from SAGE_ROOT/devel/
> sage-main:

> $ ../../sage -notebook

> And I get the following error:

> Please wait while the Sage Notebook server starts...
> Traceback (most recent call last):
>  File "/Users/rlmill/sage-4.0.2/local/bin/sage-notebook", line 9, in
> <module>
>    from sage.server.notebook.all import notebook
>  File "/Users/rlmill/sage-4.0.2/devel/sage-main/sage/server/notebook/
> all.py", line 15, in <module>
>    from notebook_object import notebook, inotebook
>  File "/Users/rlmill/sage-4.0.2/devel/sage-main/sage/server/notebook/
> notebook_object.py", line 19, in <module>
>    import notebook as _notebook
>  File "/Users/rlmill/sage-4.0.2/devel/sage-main/sage/server/notebook/
> notebook.py", line 22, in <module>
>    from   sage.structure.sage_object import SageObject, load
> ImportError: No module named sage_object

> Can anyone reproduce this?

In python imports are relative by default, so "import sage" does not
mean what you think.   I think long ago I hacked around this problem
for just typing "sage" to start sage, by making it change to a
different directory during startup.   (I vaguely recall doing that
specifically to get Sage to work on Cygwin, actually.)

So I think the above should be considered a bug, and you should
definitely report it to trac.  Probably the fix is to change the
directory during part of Sage startup, to thwart Python's relative
import system.

William 


---

Comment by aapitzsch created at 2014-06-22 13:07:51

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-06-22 13:07:51

Is it still a problem?


---

Comment by jdemeyer created at 2014-10-01 12:19:53

I think it's no longer an issue (although I cannot explain why the problem no longer occurs).


---

Comment by jdemeyer created at 2014-10-01 12:19:53

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-10-13 15:48:06

Resolution: fixed
