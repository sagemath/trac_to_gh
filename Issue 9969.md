# Issue 9969: Flaky doctest in sage/interfaces/r.py

archive/issues_009969.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  dimpase kcrisman nthiery @timokau\n\n[Dima Pasechnik reports on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/01a01378099b9d5e/3fe4b83c4c612663#3fe4b83c4c612663):\n\n```\nBuilds and tests OK on Linux amd64 (Debian unstable). Got one test failure:\n\nsage -t  \"devel/sage/sage/interfaces/r.py\"\n**********************************************************************\nFile \"/usr/local/src/sage/sage-4.6.alpha1/devel/sage/sage/interfaces/r.py\", line 1128:\n    sage: tmpdir in sageobj(r.getwd())\nExpected:\n    True\nGot:\n    False\n\nthat however would  not repeat if I tested again...\n```\n\n\nI've also seen this error, on occasion.  The test lines are\n\n```python\n            sage: import tempfile\n            sage: tmpdir = tempfile.mkdtemp()\n            sage: r.chdir(tmpdir)\n            sage: tmpdir in sageobj(r.getwd()) \n            True\n```\n\nOn sage.math, I get\n\n```python\nsage: import tempfile\nsage: \nsage: fail = 0\nsage: for i in xrange(1000):\n....:     tmpdir = tempfile.mkdtemp()\n....:     r.chdir(tmpdir)\n....:     if tmpdir not in sageobj(r.getwd()):\n....:             fail += 1\n....: \nsage: print fail\n13\n```\n\nfor example.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9970\n\n",
    "created_at": "2010-09-22T22:32:47Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Flaky doctest in sage/interfaces/r.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9969",
    "user": "mpatel"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/9970





---

archive/issue_comments_099930.json:
```json
{
    "body": "That's very interesting, thanks for pointing it out.  Since the `r.chdir()` is a pretty recent addition, it's not surprising there are unusual bugs with this.  I get the same behavior on Mac OS X 10.4, so this is not platform dependent, unsurprisingly.\n\n I am wondering whether it is simply that the directory names are preparsed or something with all those `Integer` things - maybe these 13-20 out of 1000 are the ones that have numeric characters in the alphanumeric string?.  Though `/tmp/tmp0Py04L` only has the `04` in `Integer`, not the first `0`.  Also, I get\n\n\n```\n/tmp/tmpooH_dP [1] \"/private/tmp/tmpooH_dP\" /private/tmp/tmpooH_dP\n/tmp/tmpLPmXNF [1] \"/private/tmp/tmpLPmXNF\" /private/tmp/tmpLPmXNF\n/tmp/tmpH7BqRp [1] \"/private/tmp/tmpH7BqRp\" /private/tmp/tmpH7BqRp\n/tmp/tmpmV9yGJ [1] \"/private/tmp/tmpmV9yGJ\" /private/tmp/tmpmV9yGJ\n/tmp/tmpZig4LH [1] \"/private/tmp/tmpZig4LH\" /private/tmp/tmpZigInteger(4)H\n```\n\nin printing out the first ones until I get a failure (change the `if` loop to a `while` loop, basically), and a second time\n\n```\n/tmp/tmp2Ny1fm [1] \"/private/tmp/tmp2Ny1fm\" /private/tmp/tmp2Ny1fm\n/tmp/tmpY6qCbW [1] \"/private/tmp/tmpY6qCbW\" /private/tmp/tmpY6qCbW\n/tmp/tmpQWhSyG [1] \"/private/tmp/tmpQWhSyG\" /private/tmp/tmpQWhSyG\n/tmp/tmpJnST6Z [1] \"/private/tmp/tmpJnST6Z\" /private/tmp/tmpJnST6Z\n/tmp/tmpiP3g5g [1] \"/private/tmp/tmpiP3g5g\" /private/tmp/tmpiP3g5g\n/tmp/tmpBo_DwU [1] \"/private/tmp/tmpBo_DwU\" /private/tmp/tmpBo_DwU\n/tmp/tmp0O2kjX [1] \"/private/tmp/tmp0O2kjX\" /private/tmp/tmp0O2kjX\n/tmp/tmpJzFFFs [1] \"/private/tmp/tmpJzFFFs\" /private/tmp/tmpJzFFFs\n/tmp/tmpF3eRCC [1] \"/private/tmp/tmpF3eRCC\" /private/tmp/tmpF3eRCC\n/tmp/tmp3Vd1Lg [1] \"/private/tmp/tmp3Vd1Lg\" /private/tmp/tmp3VdInteger(1)g\n```\n\nso that can't be the issue, at least not by itself.  The position of the integer seems irrelevant as well.",
    "created_at": "2010-09-23T00:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99930",
    "user": "kcrisman"
}
```

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

archive/issue_comments_099931.json:
```json
{
    "body": "Using `str` instead of `sageobj` seems to work.  Of course, that doesn't explain the behavior of `sageobj` here.\n\nAside: Would we avoid the platform-dependent `/private` prefix with `sage.misc.misc.tmp_dir`?  The `sage-cleaner` would later delete the directory.",
    "created_at": "2010-09-23T01:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99931",
    "user": "mpatel"
}
```

Using `str` instead of `sageobj` seems to work.  Of course, that doesn't explain the behavior of `sageobj` here.

Aside: Would we avoid the platform-dependent `/private` prefix with `sage.misc.misc.tmp_dir`?  The `sage-cleaner` would later delete the directory.



---

archive/issue_comments_099932.json:
```json
{
    "body": "Ticket #10264 is an apparent duplicate.  Jeroen Demeyer has attached a patch there.",
    "created_at": "2010-11-15T09:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99932",
    "user": "mpatel"
}
```

Ticket #10264 is an apparent duplicate.  Jeroen Demeyer has attached a patch there.



---

archive/issue_comments_099933.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> Ticket #10264 is an apparent duplicate.  Jeroen Demeyer has attached a patch there.\n\nNo, it seems to be a different problem with the same doctest.",
    "created_at": "2010-11-15T09:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99933",
    "user": "mpatel"
}
```

Replying to [comment:5 mpatel]:
> Ticket #10264 is an apparent duplicate.  Jeroen Demeyer has attached a patch there.

No, it seems to be a different problem with the same doctest.



---

archive/issue_comments_099934.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> No, it seems to be a different problem with the same doctest.\n\nExactly.  However, in order not to get into merge conflicts, I propose that any patch for this ticket actually goes to #10264.",
    "created_at": "2010-11-15T09:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99934",
    "user": "jdemeyer"
}
```

Replying to [comment:6 mpatel]:
> No, it seems to be a different problem with the same doctest.

Exactly.  However, in order not to get into merge conflicts, I propose that any patch for this ticket actually goes to #10264.



---

archive/issue_comments_099935.json:
```json
{
    "body": "If you look carefully, you notice that these errors happen exactly when there is a digit followed by the letter \"L\".",
    "created_at": "2010-11-15T09:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99935",
    "user": "jdemeyer"
}
```

If you look carefully, you notice that these errors happen exactly when there is a digit followed by the letter "L".



---

archive/issue_comments_099936.json:
```json
{
    "body": "Replying to [comment:8 jdemeyer]:\n> If you look carefully, you notice that these errors happen exactly when there is a digit followed by the letter \"L\".\nHah!  You got it nailed - \n\n```\n/tmp/tmp3Vd1Lg [1] \"/private/tmp/tmp3Vd1Lg\" /private/tmp/tmp3VdInteger(1)g\n```\n\nthe `1L` becomes `Integer(1)`.  And all of them do that.  \n\nSo it thinks we have a 'long integer' when in fact it's just a random directory.  I think maybe this is a problem in R itself, in `setwd`?",
    "created_at": "2010-11-15T19:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99936",
    "user": "kcrisman"
}
```

Replying to [comment:8 jdemeyer]:
> If you look carefully, you notice that these errors happen exactly when there is a digit followed by the letter "L".
Hah!  You got it nailed - 

```
/tmp/tmp3Vd1Lg [1] "/private/tmp/tmp3Vd1Lg" /private/tmp/tmp3VdInteger(1)g
```

the `1L` becomes `Integer(1)`.  And all of them do that.  

So it thinks we have a 'long integer' when in fact it's just a random directory.  I think maybe this is a problem in R itself, in `setwd`?



---

archive/issue_comments_099937.json:
```json
{
    "body": "Changing keywords from \"\" to \"r\".",
    "created_at": "2010-11-16T08:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99937",
    "user": "jdemeyer"
}
```

Changing keywords from "" to "r".



---

archive/issue_comments_099938.json:
```json
{
    "body": "Replying to [comment:9 kcrisman]:\n> I think maybe this is a problem in R itself, in `setwd`?\n\nI doubt it, since `r.getwd()` returns the right thing, but `sageobj(r.getwd())` not.",
    "created_at": "2010-11-16T08:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99938",
    "user": "jdemeyer"
}
```

Replying to [comment:9 kcrisman]:
> I think maybe this is a problem in R itself, in `setwd`?

I doubt it, since `r.getwd()` returns the right thing, but `sageobj(r.getwd())` not.



---

archive/issue_comments_099939.json:
```json
{
    "body": "If I comment out line 1717 in `interfaces/r.py`\n\n```python\n        # Change 'dL' to 'Integer(d)'\n        exp = rel_re_integer.sub(self._subs_integer, exp)\n```\n\n(in `sage.interfaces.r.RElement._sage_`), I get no failures with the script in the description.",
    "created_at": "2010-11-17T07:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99939",
    "user": "mpatel"
}
```

If I comment out line 1717 in `interfaces/r.py`

```python
        # Change 'dL' to 'Integer(d)'
        exp = rel_re_integer.sub(self._subs_integer, exp)
```

(in `sage.interfaces.r.RElement._sage_`), I get no failures with the script in the description.



---

archive/issue_comments_099940.json:
```json
{
    "body": "Replying to [comment:11 mpatel]:\n> If I comment out line 1717 in `interfaces/r.py`\n> {{{\n> #!python\n>         # Change 'dL' to 'Integer(d)'\n>         exp = rel_re_integer.sub(self._subs_integer, exp)\n> }}}\n> (in `sage.interfaces.r.RElement._sage_`), I get no failures with the script in the description.\n\nBut I suppose you might get errors somewhere else?",
    "created_at": "2010-11-17T08:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99940",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_099941.json:
```json
{
    "body": "Replying to [comment:12 jdemeyer]:\n> Replying to [comment:11 mpatel]:\n> > If I comment out line 1717 in `interfaces/r.py`\n> > {{{\n> > #!python\n> >         # Change 'dL' to 'Integer(d)'\n> >         exp = rel_re_integer.sub(self._subs_integer, exp)\n> > }}}\n> > (in `sage.interfaces.r.RElement._sage_`), I get no failures with the script in the description.\n> \n> But I suppose you might get errors somewhere else?\n\nYou're probably right.  I was just following up on your observation about long integers with an experiment.\n\nHow about\n\n```python\nsage: '\"%s\"' % os.path.realpath(tmpdir) == r.eval('dput(%s)' % r.getwd().name())\nTrue\n```\n\n?  Can we simplify this?",
    "created_at": "2010-11-26T15:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99941",
    "user": "mpatel"
}
```

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

archive/issue_comments_099942.json:
```json
{
    "body": "Or\n\n```python\nsage: os.path.realpath(tmpdir) in str(r.getwd())\nTrue\n```\n\n?",
    "created_at": "2010-11-26T15:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99942",
    "user": "mpatel"
}
```

Or

```python
sage: os.path.realpath(tmpdir) in str(r.getwd())
True
```

?



---

archive/issue_comments_099943.json:
```json
{
    "body": "Personally, I am **against** changing doctests when the underlying functions are broken.  In this case, it is clearly the conversion from R to Sage which is broken, not the doctest.  By changing the doctest, we just hide the bug under the carpet instead of solving it.",
    "created_at": "2010-11-26T16:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99943",
    "user": "jdemeyer"
}
```

Personally, I am **against** changing doctests when the underlying functions are broken.  In this case, it is clearly the conversion from R to Sage which is broken, not the doctest.  By changing the doctest, we just hide the bug under the carpet instead of solving it.



---

archive/issue_comments_099944.json:
```json
{
    "body": "Replying to [comment:15 jdemeyer]:\n> Personally, I am **against** changing doctests when the underlying functions are broken.  In this case, it is clearly the conversion from R to Sage which is broken, not the doctest.  By changing the doctest, we just hide the bug under the carpet instead of solving it.\n\n+1, though the doctest tries to test something else as I understand it.",
    "created_at": "2010-12-02T12:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99944",
    "user": "leif"
}
```

Replying to [comment:15 jdemeyer]:
> Personally, I am **against** changing doctests when the underlying functions are broken.  In this case, it is clearly the conversion from R to Sage which is broken, not the doctest.  By changing the doctest, we just hide the bug under the carpet instead of solving it.

+1, though the doctest tries to test something else as I understand it.



---

archive/issue_comments_099945.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-01-13T23:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99945",
    "user": "wjp"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_099946.json:
```json
{
    "body": "I have a patch that should fix this, but due to lack of knowledge of R I can't effectively test it. I think it needs some more doctests for the `_sage_` function.",
    "created_at": "2011-01-13T23:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99946",
    "user": "wjp"
}
```

I have a patch that should fix this, but due to lack of knowledge of R I can't effectively test it. I think it needs some more doctests for the `_sage_` function.



---

archive/issue_comments_099947.json:
```json
{
    "body": "Attachment [9970_r_strings.patch](tarball://root/attachments/some-uuid/ticket9970/9970_r_strings.patch) by wjp created at 2011-01-13 23:22:24",
    "created_at": "2011-01-13T23:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99947",
    "user": "wjp"
}
```

Attachment [9970_r_strings.patch](tarball://root/attachments/some-uuid/ticket9970/9970_r_strings.patch) by wjp created at 2011-01-13 23:22:24



---

archive/issue_comments_099948.json:
```json
{
    "body": "Replying to [comment:17 wjp]:\n> I have a patch that should fix this, but due to lack of knowledge of R I can't effectively test it. I think it needs some more doctests for the `_sage_` function.\nI will eventually look at this, but because it's a rather harmless doctest failure (even though we really don't like doctest failures) I won't be able to check it out very quickly.  \n\nI'm also putting your request from sage-devel here for reference as to what you think is needed for review - thanks!\n\n```\nIf somebody more familiar with the R language and interface could take a look \nif the string-related corner cases work, and if it didn't break anything \nnon-string-related (and maybe add some more doctests to the _sage_ method), \nthat would be great. \n```\n",
    "created_at": "2011-01-14T01:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99948",
    "user": "kcrisman"
}
```

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

archive/issue_comments_099949.json:
```json
{
    "body": "This is still a very annoying bug.",
    "created_at": "2013-02-04T13:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99949",
    "user": "jdemeyer"
}
```

This is still a very annoying bug.



---

archive/issue_comments_099950.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2013-02-04T13:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99950",
    "user": "jdemeyer"
}
```

Changing priority from major to critical.



---

archive/issue_comments_099951.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2013-05-23T20:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99951",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_099952.json:
```json
{
    "body": "By #12415, a remark was added in r.py, pointing to this ticket:\n\n```\n            sage: os.path.realpath(tmpdir) == sageobj(r.getwd())  # known bug (:trac:`9970`)\n            True\n```\n\n\nNote that in #12876, Nicolas changes the test by inserting os.path.realpath on the right side as well, hence:\n\n```\n            sage: os.path.realpath(tmpdir) == os.path.realpath(sageobj(r.getwd()))\n            True\n```\n\n\nI don't know if this test is all what this ticket is about. So, please decide yourself if this ticket became a duplicate (or actually a sub-problem) of #12876",
    "created_at": "2013-05-23T20:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99952",
    "user": "SimonKing"
}
```

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

archive/issue_comments_099953.json:
```json
{
    "body": "Unrelated as far as I can tell.",
    "created_at": "2013-05-23T20:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99953",
    "user": "wjp"
}
```

Unrelated as far as I can tell.



---

archive/issue_comments_099954.json:
```json
{
    "body": "Replying to [comment:21 wjp]:\n> Unrelated as far as I can tell.\n\nOK, then the ticket status should probably reverted (it has been \"needs work\").\n\nIn any case, it seems that #12876 needs this change to make the doctest failure vanish. I suggest that a \"todo\" is added, referring to this ticket, stating that the doctest fix from #12876 is not a fix of the underlying problem, which is dealt with here.",
    "created_at": "2013-05-23T20:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99954",
    "user": "SimonKing"
}
```

Replying to [comment:21 wjp]:
> Unrelated as far as I can tell.

OK, then the ticket status should probably reverted (it has been "needs work").

In any case, it seems that #12876 needs this change to make the doctest failure vanish. I suggest that a "todo" is added, referring to this ticket, stating that the doctest fix from #12876 is not a fix of the underlying problem, which is dealt with here.



---

archive/issue_comments_099955.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-05-23T20:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99955",
    "user": "SimonKing"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_099956.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-05-23T20:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99956",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099957.json:
```json
{
    "body": "Replying to [comment:22 SimonKing]:\n> In any case, it seems that #12876 needs this change to make the doctest failure vanish.\nAre you sure, because I don't see what #12876 has to do with either the conversion from R to Sage or with filesystem paths.",
    "created_at": "2013-05-24T06:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99957",
    "user": "jdemeyer"
}
```

Replying to [comment:22 SimonKing]:
> In any case, it seems that #12876 needs this change to make the doctest failure vanish.
Are you sure, because I don't see what #12876 has to do with either the conversion from R to Sage or with filesystem paths.



---

archive/issue_comments_099958.json:
```json
{
    "body": "Replying to [comment:24 jdemeyer]:\n> Replying to [comment:22 SimonKing]:\n> > In any case, it seems that #12876 needs this change to make the doctest failure vanish.\n> Are you sure, because I don't see what #12876 has to do with either the conversion from R to Sage or with filesystem paths.\n\nWell, at least it used to need it. If I recall correctly, at the time when I created the first version of this patch, we got a consistent error in the test, and with the patch the error consistently vanished.\n\nHowever, as I've learned today, the tests also pass without this patch. So, we should drop it.",
    "created_at": "2013-05-24T07:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99958",
    "user": "SimonKing"
}
```

Replying to [comment:24 jdemeyer]:
> Replying to [comment:22 SimonKing]:
> > In any case, it seems that #12876 needs this change to make the doctest failure vanish.
> Are you sure, because I don't see what #12876 has to do with either the conversion from R to Sage or with filesystem paths.

Well, at least it used to need it. If I recall correctly, at the time when I created the first version of this patch, we got a consistent error in the test, and with the patch the error consistently vanished.

However, as I've learned today, the tests also pass without this patch. So, we should drop it.



---

archive/issue_comments_099959.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2015-02-10T08:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99959",
    "user": "mmezzarobba"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_099960.json:
```json
{
    "body": "Replying to [comment:25 SimonKing]:\n> However, as I've learned today, the tests also pass without this patch. So, we should drop it.\n\nSo should this ticket be closed as invalid?",
    "created_at": "2015-02-10T08:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99960",
    "user": "mmezzarobba"
}
```

Replying to [comment:25 SimonKing]:
> However, as I've learned today, the tests also pass without this patch. So, we should drop it.

So should this ticket be closed as invalid?



---

archive/issue_comments_099961.json:
```json
{
    "body": "Replying to [comment:30 mmezzarobba]:\n> So should this ticket be closed as invalid?\n**NO**",
    "created_at": "2015-02-10T09:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99961",
    "user": "jdemeyer"
}
```

Replying to [comment:30 mmezzarobba]:
> So should this ticket be closed as invalid?
**NO**



---

archive/issue_comments_099962.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2015-02-10T10:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99962",
    "user": "mmezzarobba"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_099963.json:
```json
{
    "body": "As of Sage 8.5 I no longer get errors from the script above, so presumably \"known bug\" can be removed.\n\nHowever, `r.chdir` and `os.chdir` now do the same thing, i.e. the current directory for R and Sage is the same, which suggests to me that this function should be deprecated entirely. Unless it is desirable to be able to set different directories, in which case this has to be reimplemented.",
    "created_at": "2018-12-24T15:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99963",
    "user": "novoselt"
}
```

As of Sage 8.5 I no longer get errors from the script above, so presumably "known bug" can be removed.

However, `r.chdir` and `os.chdir` now do the same thing, i.e. the current directory for R and Sage is the same, which suggests to me that this function should be deprecated entirely. Unless it is desirable to be able to set different directories, in which case this has to be reimplemented.



---

archive/issue_comments_099964.json:
```json
{
    "body": "Timo - am I right that with rpy2 interface the working directory of python and R are always the same and so `r.chdir` does not really make sense anymore?",
    "created_at": "2019-01-08T21:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99964",
    "user": "novoselt"
}
```

Timo - am I right that with rpy2 interface the working directory of python and R are always the same and so `r.chdir` does not really make sense anymore?



---

archive/issue_comments_099965.json:
```json
{
    "body": "Yes that is right. I wasn't aware that there was a difference before. I think sharing a working directory is actually less confusing. You're right that `r.chdir` should be removed if we don't want to restore the old behaviour.",
    "created_at": "2019-01-08T21:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99965",
    "user": "@timokau"
}
```

Yes that is right. I wasn't aware that there was a difference before. I think sharing a working directory is actually less confusing. You're right that `r.chdir` should be removed if we don't want to restore the old behaviour.



---

archive/issue_comments_099966.json:
```json
{
    "body": "downgrading priority to minor in view of the last comments",
    "created_at": "2020-10-08T09:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99966",
    "user": "mmezzarobba"
}
```

downgrading priority to minor in view of the last comments



---

archive/issue_comments_099967.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2020-10-08T09:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99967",
    "user": "mmezzarobba"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_099968.json:
```json
{
    "body": "Setting new milestone based on a cursory review of ticket status, priority, and last modification date.",
    "created_at": "2021-02-13T20:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99968",
    "user": "mkoeppe"
}
```

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.



---

archive/issue_comments_099969.json:
```json
{
    "body": "Setting a new milestone for this ticket based on a cursory review.",
    "created_at": "2021-07-19T00:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9969#issuecomment-99969",
    "user": "mkoeppe"
}
```

Setting a new milestone for this ticket based on a cursory review.
