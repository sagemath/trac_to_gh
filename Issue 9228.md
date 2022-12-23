# Issue 9228: Bring doctests for interfaces/mwrank.py up to 100% (from 20% (2 of 10)  )

Issue created by migration from https://trac.sagemath.org/ticket/9228

Original creator: cremona

Original creation time: 2010-06-12 13:42:01

Assignee: cremona

Keywords: mwrank


```

devel/sage-main/sage/interfaces/mwrank.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-main/sage/interfaces/mwrank.py: 20% (2 of 10)

Missing documentation:
* __getattr__(self, attrname):
* __reduce__(self):
* __call__(self, cmd):
* console(self):
* _reduce_load_mwrank():
* mwrank_console():


Missing doctests:
* Mwrank(options="", server=None, server_tmpdir=None):
* __init__(self, options="", server=None,server_tmpdir=None):
```



---

Comment by cremona created at 2010-12-21 17:23:49

Changing priority from major to minor.


---

Comment by cremona created at 2010-12-21 17:23:49

After the patch:

```
%sage -coverage sage/interfaces/mwrank.py 
----------------------------------------------------------------------
sage/interfaces/mwrank.py
SCORE sage/interfaces/mwrank.py: 100% (10 of 10)
----------------------------------------------------------------------
```

and the reference manual markup has also been corrected.


---

Comment by cremona created at 2010-12-21 17:23:49

Changing status from new to needs_review.


---

Comment by aly.deines created at 2011-01-09 23:48:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-19 22:20:42

Resolution: fixed


---

Comment by jdemeyer created at 2011-01-20 09:01:23

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2011-01-20 09:01:23

For some reason, the '\t' (tab) is replaced by a series of spaces on Solaris, giving doctest errors:

```
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.6.2.alpha1/devel/sage-main/sage/interfaces/mwrank.py", line 107:
    sage: M('0 -1 1 0 0')
Expected:
    'Curve [0,-1,1,0,0] :\tRank = 0\n\n\nRegulator = 1\n'
Got:
    'Curve [0,-1,1,0,0] :    Rank = 0\n\n\nRegulator = 1\n'
**********************************************************************
```



---

Comment by jdemeyer created at 2011-01-20 09:01:23

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-01-20 09:01:33

Changing status from new to needs_work.


---

Comment by cremona created at 2011-01-20 09:30:49

OK, so I know that some people don't like my programs putting tabs into output, which I do so the output looks pretty when viewed by humans!

I suppose that one solution is to post-process the long string output by mwrank, replacing its tabs by an appropriate number of spaces.

This is just the sort of annoying triviality which makes adding doctests take so much longer than it ought!

I'll post a revised patch shortly.


---

Comment by cremona created at 2011-01-20 11:20:23

Applies to 4.6.2.alpha0


---

Attachment

The new version of the patch does what I suggested, i.e. replaces all tabs in mwrank output by three spaces;  the doctest which failed before has been adjusted accordingly.

I could not find any other doctest which would be affected by this, and tested all sage/interfaces and sage/schemes/elliptic_curves.


---

Comment by cremona created at 2011-01-20 11:22:00

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2011-01-20 12:13:43

I can't help noticing that you've replaced tabs with 3 spaces, but Solaris seems to replace them with 4 spaces -- so I suspect that it still won't work (groan).


---

Comment by cremona created at 2011-01-20 12:36:38

Replying to [comment:9 davidloeffler]:
> I can't help noticing that you've replaced tabs with 3 spaces, but Solaris seems to replace them with 4 spaces -- so I suspect that it still won't work (groan).

Think again.  I have removed the tabs so Solaris will not need to do anything!


---

Comment by jdemeyer created at 2011-01-20 12:39:46

The question is: why is the output on Solaris different in the first place?  Is it the `mwrank` program itself?  Is it pexpect?  Is it Python?


---

Comment by cremona created at 2011-01-20 13:02:55

Replying to [comment:11 jdemeyer]:
> The question is: why is the output on Solaris different in the first place?  Is it the `mwrank` program itself?  Is it pexpect?  Is it Python?

Here's a test:  on the solaris machine, do

```
echo 0 -1 1 0 0 0 0 0 0 0 | sage -mwrank -v 0 -q -l > t
```

and see if the file t contains any tab characters.  If it does, then mwrank is behaving normally and the tab conversion is happening further downstream.


---

Comment by jdemeyer created at 2011-01-20 20:01:53

Replying to [comment:12 cremona]:
> Here's a test:  on the solaris machine, do
> {{{
> echo 0 -1 1 0 0 0 0 0 0 0 | sage -mwrank -v 0 -q -l
> }}}

This is producing an actual tab character.


---

Comment by jdemeyer created at 2011-01-20 20:47:26

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-20 20:47:26

Tested on fulvia (i386 Solaris).


---

Comment by jdemeyer created at 2011-01-25 08:14:46

Resolution: fixed
