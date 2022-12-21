# Issue 9969: Flaky doctest in sage/interfaces/r.py

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-09-22 22:32:47

Assignee: mvngu

CC:  dimpase kcrisman nthiery @timokau

[Dima Pasechnik reports on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/01a01378099b9d5e/3fe4b83c4c612663#3fe4b83c4c612663):

```
Builds and tests OK on Linux amd64 (Debian unstable). Got one test failure:

sage -t  "devel/sage/sage/interfaces/r.py"
**********************************************************************
File "/usr/local/src/sage/sage-4.6.alpha1/devel/sage/sage/interfaces/r.py", line 1128:
    sage: tmpdir in sageobj(r.getwd())
Expected:
    True
Got:
    False

that however would  not repeat if I tested again...
```


I've also seen this error, on occasion.  The test lines are

```python
            sage: import tempfile
            sage: tmpdir = tempfile.mkdtemp()
            sage: r.chdir(tmpdir)
            sage: tmpdir in sageobj(r.getwd()) 
            True
```

On sage.math, I get

```python
sage: import tempfile
sage: 
sage: fail = 0
sage: for i in xrange(1000):
....:     tmpdir = tempfile.mkdtemp()
....:     r.chdir(tmpdir)
....:     if tmpdir not in sageobj(r.getwd()):
....:             fail += 1
....: 
sage: print fail
13
```

for example.


---

Comment by kcrisman created at 2010-09-23 00:11:20

That's very interesting, thanks for pointing it out.  Since the `r.chdir()` is a pretty recent addition, it's not surprising there are unusual bugs with this.  I get the same behavior on Mac OS X 10.4, so this is not platform dependent, unsurprisingly.

 I am wondering whether it is simply that the directory names are preparsed or something with all those `Integer` things - maybe these 13-20 out of 1000 are the ones that have numeric characters in the alphanumeric string?.  Though `/tmp/tmp0Py04L` only has the `04` in `Integer`, not the first `0`.  Also, I get


```
/tmp/tmpooH_dP [1] "/private/tmp/tmpooH_dP" /private/tmp/tmpooH_dP
/tmp/tmpLPmXNF [1] "/private/tmp/tmpLPmXNF" /private/tmp/tmpLPmXNF
/tmp/tmpH7BqRp [1] "/private/tmp/tmpH7BqRp" /private/tmp/tmpH7BqRp
/tmp/tmpmV9yGJ [1] "/private/tmp/tmpmV9yGJ" /private/tmp/tmpmV9yGJ
/tmp/tmpZig4LH [1] "/private/tmp/tmpZig4LH" /private/tmp/tmpZigInteger(4)H
```

in printing out the first ones until I get a failure (change the `if` loop to a `while` loop, basically), and a second time

```
/tmp/tmp2Ny1fm [1] "/private/tmp/tmp2Ny1fm" /private/tmp/tmp2Ny1fm
/tmp/tmpY6qCbW [1] "/private/tmp/tmpY6qCbW" /private/tmp/tmpY6qCbW
/tmp/tmpQWhSyG [1] "/private/tmp/tmpQWhSyG" /private/tmp/tmpQWhSyG
/tmp/tmpJnST6Z [1] "/private/tmp/tmpJnST6Z" /private/tmp/tmpJnST6Z
/tmp/tmpiP3g5g [1] "/private/tmp/tmpiP3g5g" /private/tmp/tmpiP3g5g
/tmp/tmpBo_DwU [1] "/private/tmp/tmpBo_DwU" /private/tmp/tmpBo_DwU
/tmp/tmp0O2kjX [1] "/private/tmp/tmp0O2kjX" /private/tmp/tmp0O2kjX
/tmp/tmpJzFFFs [1] "/private/tmp/tmpJzFFFs" /private/tmp/tmpJzFFFs
/tmp/tmpF3eRCC [1] "/private/tmp/tmpF3eRCC" /private/tmp/tmpF3eRCC
/tmp/tmp3Vd1Lg [1] "/private/tmp/tmp3Vd1Lg" /private/tmp/tmp3VdInteger(1)g
```

so that can't be the issue, at least not by itself.  The position of the integer seems irrelevant as well.


---

Comment by mpatel created at 2010-09-23 01:35:03

Using `str` instead of `sageobj` seems to work.  Of course, that doesn't explain the behavior of `sageobj` here.

Aside: Would we avoid the platform-dependent `/private` prefix with `sage.misc.misc.tmp_dir`?  The `sage-cleaner` would later delete the directory.


---

Comment by mpatel created at 2010-11-15 09:09:58

Ticket #10264 is an apparent duplicate.  Jeroen Demeyer has attached a patch there.


---

Comment by mpatel created at 2010-11-15 09:17:03

Replying to [comment:5 mpatel]:
> Ticket #10264 is an apparent duplicate.  Jeroen Demeyer has attached a patch there.

No, it seems to be a different problem with the same doctest.


---

Comment by jdemeyer created at 2010-11-15 09:19:56

Replying to [comment:6 mpatel]:
> No, it seems to be a different problem with the same doctest.

Exactly.  However, in order not to get into merge conflicts, I propose that any patch for this ticket actually goes to #10264.


---

Comment by jdemeyer created at 2010-11-15 09:27:31

If you look carefully, you notice that these errors happen exactly when there is a digit followed by the letter "L".


---

Comment by kcrisman created at 2010-11-15 19:00:28

Replying to [comment:8 jdemeyer]:
> If you look carefully, you notice that these errors happen exactly when there is a digit followed by the letter "L".
Hah!  You got it nailed - 

```
/tmp/tmp3Vd1Lg [1] "/private/tmp/tmp3Vd1Lg" /private/tmp/tmp3VdInteger(1)g
```

the `1L` becomes `Integer(1)`.  And all of them do that.  

So it thinks we have a 'long integer' when in fact it's just a random directory.  I think maybe this is a problem in R itself, in `setwd`?


---

Comment by jdemeyer created at 2010-11-16 08:49:37

Changing keywords from "" to "r".


---

Comment by jdemeyer created at 2010-11-16 08:49:37

Replying to [comment:9 kcrisman]:
> I think maybe this is a problem in R itself, in `setwd`?

I doubt it, since `r.getwd()` returns the right thing, but `sageobj(r.getwd())` not.


---

Comment by mpatel created at 2010-11-17 07:18:27

If I comment out line 1717 in `interfaces/r.py`

```python
        # Change 'dL' to 'Integer(d)'
        exp = rel_re_integer.sub(self._subs_integer, exp)
```

(in `sage.interfaces.r.RElement._sage_`), I get no failures with the script in the description.


---

Comment by jdemeyer created at 2010-11-17 08:19:02

Replying to [comment:11 mpatel]:
> If I comment out line 1717 in `interfaces/r.py`
> {{{
> #!python
>         # Change 'dL' to 'Integer(d)'
>         exp = rel_re_integer.sub(self._subs_integer, exp)
> }}}
> (in `sage.interfaces.r.RElement._sage_`), I get no failures with the script in the description.

But I suppose you might get errors somewhere else?


---

Comment by mpatel created at 2010-11-26 15:11:20

Replying to [comment:12 jdemeyer]:
> Replying to [comment:11 mpatel]:
> > If I comment out line 1717 in `interfaces/r.py`
> > {{{
> > #!python
> >         # Change 'dL' to 'Integer(d)'
> >         exp = rel_re_integer.sub(self._subs_integer, exp)
> > }}}
> > (in `sage.interfaces.r.RElement._sage_`), I get no failures with the script in the description.
> 
> But I suppose you might get errors somewhere else?

You're probably right.  I was just following up on your observation about long integers with an experiment.

How about

```python
sage: '"%s"' % os.path.realpath(tmpdir) == r.eval('dput(%s)' % r.getwd().name())
True
```

?  Can we simplify this?


---

Comment by mpatel created at 2010-11-26 15:17:37

Or

```python
sage: os.path.realpath(tmpdir) in str(r.getwd())
True
```

?


---

Comment by jdemeyer created at 2010-11-26 16:08:30

Personally, I am *against* changing doctests when the underlying functions are broken.  In this case, it is clearly the conversion from R to Sage which is broken, not the doctest.  By changing the doctest, we just hide the bug under the carpet instead of solving it.


---

Comment by leif created at 2010-12-02 12:32:38

Replying to [comment:15 jdemeyer]:
> Personally, I am *against* changing doctests when the underlying functions are broken.  In this case, it is clearly the conversion from R to Sage which is broken, not the doctest.  By changing the doctest, we just hide the bug under the carpet instead of solving it.

+1, though the doctest tries to test something else as I understand it.


---

Comment by wjp created at 2011-01-13 23:02:29

Changing status from new to needs_work.


---

Comment by wjp created at 2011-01-13 23:02:29

I have a patch that should fix this, but due to lack of knowledge of R I can't effectively test it. I think it needs some more doctests for the `_sage_` function.


---

Attachment


---

Comment by kcrisman created at 2011-01-14 01:48:08

Replying to [comment:17 wjp]:
> I have a patch that should fix this, but due to lack of knowledge of R I can't effectively test it. I think it needs some more doctests for the `_sage_` function.
I will eventually look at this, but because it's a rather harmless doctest failure (even though we really don't like doctest failures) I won't be able to check it out very quickly.  

I'm also putting your request from sage-devel here for reference as to what you think is needed for review - thanks!

```
If somebody more familiar with the R language and interface could take a look 
if the string-related corner cases work, and if it didn't break anything 
non-string-related (and maybe add some more doctests to the _sage_ method), 
that would be great. 
```



---

Comment by jdemeyer created at 2013-02-04 13:14:35

This is still a very annoying bug.


---

Comment by jdemeyer created at 2013-02-04 13:14:35

Changing priority from major to critical.


---

Comment by SimonKing created at 2013-05-23 20:10:28

Changing status from needs_work to needs_info.


---

Comment by SimonKing created at 2013-05-23 20:10:28

By #12415, a remark was added in r.py, pointing to this ticket:

```
            sage: os.path.realpath(tmpdir) == sageobj(r.getwd())  # known bug (:trac:`9970`)
            True
```


Note that in #12876, Nicolas changes the test by inserting os.path.realpath on the right side as well, hence:

```
            sage: os.path.realpath(tmpdir) == os.path.realpath(sageobj(r.getwd()))
            True
```


I don't know if this test is all what this ticket is about. So, please decide yourself if this ticket became a duplicate (or actually a sub-problem) of #12876


---

Comment by wjp created at 2013-05-23 20:15:30

Unrelated as far as I can tell.


---

Comment by SimonKing created at 2013-05-23 20:55:01

Replying to [comment:21 wjp]:
> Unrelated as far as I can tell.

OK, then the ticket status should probably reverted (it has been "needs work").

In any case, it seems that #12876 needs this change to make the doctest failure vanish. I suggest that a "todo" is added, referring to this ticket, stating that the doctest fix from #12876 is not a fix of the underlying problem, which is dealt with here.


---

Comment by SimonKing created at 2013-05-23 20:55:01

Changing status from needs_info to needs_review.


---

Comment by SimonKing created at 2013-05-23 20:55:11

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2013-05-24 06:30:15

Replying to [comment:22 SimonKing]:
> In any case, it seems that #12876 needs this change to make the doctest failure vanish.
Are you sure, because I don't see what #12876 has to do with either the conversion from R to Sage or with filesystem paths.


---

Comment by SimonKing created at 2013-05-24 07:02:25

Replying to [comment:24 jdemeyer]:
> Replying to [comment:22 SimonKing]:
> > In any case, it seems that #12876 needs this change to make the doctest failure vanish.
> Are you sure, because I don't see what #12876 has to do with either the conversion from R to Sage or with filesystem paths.

Well, at least it used to need it. If I recall correctly, at the time when I created the first version of this patch, we got a consistent error in the test, and with the patch the error consistently vanished.

However, as I've learned today, the tests also pass without this patch. So, we should drop it.


---

Comment by mmezzarobba created at 2015-02-10 08:57:12

Changing status from needs_work to needs_info.


---

Comment by mmezzarobba created at 2015-02-10 08:57:12

Replying to [comment:25 SimonKing]:
> However, as I've learned today, the tests also pass without this patch. So, we should drop it.

So should this ticket be closed as invalid?


---

Comment by jdemeyer created at 2015-02-10 09:26:20

Replying to [comment:30 mmezzarobba]:
> So should this ticket be closed as invalid?
*NO*


---

Comment by mmezzarobba created at 2015-02-10 10:25:44

Changing status from needs_info to needs_work.


---

Comment by novoselt created at 2018-12-24 15:39:16

As of Sage 8.5 I no longer get errors from the script above, so presumably "known bug" can be removed.

However, `r.chdir` and `os.chdir` now do the same thing, i.e. the current directory for R and Sage is the same, which suggests to me that this function should be deprecated entirely. Unless it is desirable to be able to set different directories, in which case this has to be reimplemented.


---

Comment by novoselt created at 2019-01-08 21:33:05

Timo - am I right that with rpy2 interface the working directory of python and R are always the same and so `r.chdir` does not really make sense anymore?


---

Comment by @timokau created at 2019-01-08 21:41:07

Yes that is right. I wasn't aware that there was a difference before. I think sharing a working directory is actually less confusing. You're right that `r.chdir` should be removed if we don't want to restore the old behaviour.


---

Comment by mmezzarobba created at 2020-10-08 09:36:43

downgrading priority to minor in view of the last comments


---

Comment by mmezzarobba created at 2020-10-08 09:36:43

Changing priority from critical to minor.


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.


---

Comment by mkoeppe created at 2021-07-19 00:44:56

Setting a new milestone for this ticket based on a cursory review.
