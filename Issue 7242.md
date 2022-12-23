# Issue 7242: Convert sage to use the new standard libary multiprocessing module rather than processing

Issue created by migration from https://trac.sagemath.org/ticket/7242

Original creator: tabbott

Original creation time: 2009-10-18 23:46:15

Assignee: mabshoff

I notice that sage is still including the Python processing module.  It 
seems that in Python 2.6, a version of the processing module was merged   
into the Python standard library under the name "multiprocessing".  I am  
told that it should be possible to convert by just replacing the references to processing with new ones to multiprocessing.

See <http://www.python.org/dev/peps/pep-0371/>

We should then be able to drop the "processing" spkg.



---

Comment by mhansen created at 2009-10-19 04:28:25

Duplicate of #6503.  I'll get to this today.


---

Comment by mhansen created at 2009-10-19 04:28:25

Resolution: duplicate
