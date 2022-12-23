# Issue 2347: Symbolic parsing uses eval()

Issue created by migration from https://trac.sagemath.org/ticket/2347

Original creator: robertwb

Original creation time: 2008-02-28 09:26:58

Assignee: was

This is a security risk, and limits the potential uses of Sage. For example, if I wanted to put a text box on my website where people could type in a function and it would return the derivative (computed using Sage) someone could "ask" for the derivative of `2*os.system('rm -rf /')`. Symbolic expressions should be able to be parsed in such a way that one can safely reject expressions using unknown (or non-whitelisted) functions. 


---

Comment by robertwb created at 2008-02-28 11:18:41

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-02-28 11:18:41

Changing status from new to assigned.


---

Comment by robertwb created at 2008-02-28 11:18:41

Of course, we don't want to re-write the Python parser or try to certify generic code to be safe, but in this constrained situation we should be able to treat an expression as data without worrying about it being treated as code. 

There is an added benefit that unknown tokens gan be treated as symbolic variables. I wrote up a parser in Cython that is actually 10 times faster than eval(...) and handles symbolic expressions that I think is ready to plug in, I just need to provide it with a good list of "whitelist" functions that may be called.


---

Attachment


---

Comment by mabshoff created at 2008-04-11 19:35:33

Changing priority from major to blocker.


---

Attachment

I've attached the bundle as a patch which I will review once 3.0.alpha4 comes out.  There were some problems applying the bundle against 3.0.alpha3.


---

Comment by robertwb created at 2008-04-11 23:52:26

I will rebase the bundle as I don't want to loose the history.


---

Comment by mhansen created at 2008-04-11 23:55:46

Sounds good although patches are much easier to deal with.


---

Comment by jason created at 2008-04-12 23:44:37

Just FYI, you could use queue repositories to be able to get patches that have history.  See the the help for qcommit, etc.


---

Attachment

The new bundle (against alpha3) works fine. There was only one minor conflict. Do you anticipate any major changes with alpha4? (If it's up before I go to bed I'll make sure it works against that.) 

Jason: Using mercurial queues won't help here, the issue is that half a dozen commits were compressed into a single patch. When there are more than four or five separate changesets attached to a given ticket, I find bundles a lot easier to deal with (rather than attaching all the patches separately).


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by robertwb created at 2008-04-13 07:31:33

For those of you who prefer patches, I've attached them. Patches 1-7 are exactly the same contents as the bundles, except the rebased bundle resolves a (trivial to fix) conflict in patch 2 against alpha3.


---

Attachment


---

Comment by mhansen created at 2008-04-14 22:44:39

I've looked at the changes and tested things out, and things look good to me.  This is a definite improvement than what was there before.  I included a change to combinat/root_system/dynkin_diagram.py.  2347.hg is the bundle that should be merged.


---

Comment by mabshoff created at 2008-04-14 22:55:58

Resolution: fixed


---

Comment by mabshoff created at 2008-04-14 22:55:58

Merged in Sage 3.0.alpha5


---

Comment by mabshoff created at 2008-04-14 23:19:51

Robert,

I am seeing one doctest failure:

```
sage -t -long devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/number_field.py", line 4878:
    sage: L.lift_to_base(b^4)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_145[6]>", line 1, in <module>
        L.lift_to_base(b**Integer(4))###line 4878:
    sage: L.lift_to_base(b^4)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4892, in lift_to_base
        f = QQ['y'](str_poly)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 225, in __call__
        raise TypeError,"Unable to coerce string"
    TypeError: Unable to coerce string
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/number_field.py", line 211:
    sage: L.lift_to_base(b^3 + b)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[12]>", line 1, in <module>
        L.lift_to_base(b**Integer(3) + b)###line 211:
    sage: L.lift_to_base(b^3 + b)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4892, in lift_to_base
        f = QQ['y'](str_poly)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 225, in __call__
        raise TypeError,"Unable to coerce string"
    TypeError: Unable to coerce string
**********************************************************************
```


Cheers,

Michael


---

Comment by robertwb created at 2008-04-14 23:29:11

Hmm... I ran a -testall before rebasing the bundle, but I'll see if I can get a patch for this. Should be pretty simple. (Really, it's ugly that it's going via strings at all.) 

BTW, do you have a `sage-3.0.alpha4-sage.math-only-x86_64-Linux.tar.gz` I could grab?


---

Comment by mabshoff created at 2008-04-14 23:37:34

An sage-3.0.alpha4-sage.math-only-x86_64-Linux.tar.gz should be up in the usual place in five minutes. Mike Hansen is also poking around in the general area.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-04-14 23:54:08

I've added 2347-doctest.patch which fixes the issue.


---

Comment by mabshoff created at 2008-04-15 00:04:31

Merged 2347-doctest.patch in Sage 3.0.alpha5


---

Comment by robertwb created at 2008-04-15 00:16:22

Thanks, good catch.


---

Comment by mabshoff created at 2008-04-15 00:33:24

For the record: Mike's patch fixes the issue.

Cheers,

Michael
