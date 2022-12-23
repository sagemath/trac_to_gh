# Issue 6288: %lisp mode on the command line doesn't work.  why?

Issue created by migration from https://trac.sagemath.org/ticket/6288

Original creator: was

Original creation time: 2009-06-14 20:57:48

Assignee: was


```
> Another thing that does not work is "sage -
> lisp" which gave the clisp prompt. I found this rather convenient
> since I could just use the clisp within sage. Is there any plan/
> interest to switch the this lisp interface to ecl? Does ecl use
> readline?

For now you can at least start sage then type

sage: !ecl

to start ecl.  It appears to not make any use of ecl.  I don't know if this is just
a compilation problem or an ecl limitation.

The Sage <--> lisp interface already works fine:

sage: lisp.eval('(+ 2 3)')
'5'

I'm not sure why %gap works but not %lisp:

sage: %lisp
ERROR: Magic function `lisp` not found.
sage: %gap
  --> Switching to Gap <-- 
gap: 
```





---

Attachment


---

Comment by mhansen created at 2013-07-23 13:24:28

Changing status from new to needs_review.


---

Comment by chapoton created at 2013-08-21 11:55:36

ok, here is a review patch.

First I have made some minor formatting changes (pep8)

Next, I have corrected the part handling the bad names

Here is the list of interfaces with bad names:

```
[('gp', 'pari', PARI/GP interpreter),
 ('lisp', 'Lisp', Lisp Interpreter),
 ('sage0', 'sage', Sage),
 ('mupad', 'MuPAD', Mupad),
 ('lie', 'LiE', LiE Interpreter)]
```

I would prefer to avoid having the magic command "%sage" !

I also wonder if it is necessary to deprecate the bad names, instead of just using them as an alternative ?


---

Attachment


---

Comment by chapoton created at 2013-09-11 19:25:03

ping ?


---

Comment by chapoton created at 2014-01-05 10:02:40

New commits:


---

Comment by mhansen created at 2014-01-09 12:19:57

The review patch looks good.  I would probably prefer "%sage0" to "%sage".  I'd rather deprecate the bad names so that there's just one consistent way to access them.  But, I'm not too fussed either way about those two points.


---

Comment by chapoton created at 2014-01-09 19:28:28

Ok, so is there still something to do or not ?


---

Comment by mhansen created at 2014-01-09 19:40:46

I would say not.  I'm fine with your patch.


---

Comment by mhansen created at 2014-01-09 19:40:46

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-17 04:16:26

Resolution: fixed
