# Issue 3796: Do something about empty directories for pexpect interfaces

Issue created by migration from https://trac.sagemath.org/ticket/3796

Original creator: tabbott

Original creation time: 2008-08-09 18:27:40

Assignee: mabshoff

I almost forgot to open a ticket on this one.  I'm not sure what solution we should use, but here's the discussion from sage-devel:

tabbott:
>> - The sage expect wrapper script (sage/interfaces/expect.py) works if its
>> __path field (normally SAGE_ROOT/data/extcode/genus2reduction or whatever)
>> is a directory that it can't write to, but if the (empty) directory is
>> deleted, it breaks.  I'm not sure what gets put in these directories --
>> there's a function user_dir that outputs that location, but it doesn't
>> seem to be called.  Anyway, either these directories are useless and
>> shouldn't exist, or there should be a way to relocate them to ~/.sage for
>> users who don't have write access to their sage installation (I have a
>> feeling I may regret not having fixed this yet).
mabshoff:
> It sounds like a sensible idea to do so. The reason those directories
> exist is that when we send a large amount of data to a pexpect
> interface we write the input to a temp file and then use the program  
> to read the input from disk. This is a hackish solution, but is cause
> be pexpect using quadratic time copying buffers. That issue should
> obviously be fixed.
wstein:
That's not right.  We use a user-writable temp directory for data interchange
with subprocesses.  Those directories were part of the early design   
of the pexpect interface, when I imagined individual users putting code
in there that would get loaded.  The interfaces can and should be redesigned
to not use/require those interfaces.  Sorry this is vague.



---

Comment by jdemeyer created at 2014-11-06 15:47:18

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-11-06 15:47:18

Fixed by #17044.


---

Comment by jdemeyer created at 2014-11-06 15:47:36

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-11-07 16:49:49

Resolution: fixed
