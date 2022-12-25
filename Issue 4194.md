# Issue 4194: pylab plots cut off

archive/issues_004194.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mvgnu @mwhansen @jasongrout\n\nKeywords: plot\n\nOn Thursday 25 September 2008, Stan Schymanski wrote on [sage-support]:\n> Dear all,\n\n>\n> When I upgraded to 3.1.2, I found that some of my plots generated\n> using pylab in the notebooks miss their bottom bits. It seems to be\n> related to the dpi setting. Example:\n\n{{{\nimport pylab\nx1 = srange(0,1.1,0.01)\nd1 = [2*x+x^2 for x in x1]\npylab.clf() # clear the figure first\npylab.figure(1)\npylab.plot(x1,d1, label=\"d1\")\npylab.ylabel(\"$f(x)$\") # label the axes\npylab.xlabel(\"$x$\")\npylab.savefig('foo.png',dpi=72) # fire!\n}}}\n> If I leave the \"dpi=72\" out in the last line, the plot is larger and\n> complete. This problem did not occur in sage 3.1.1, so I assume that\n> it is a bug.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4194\n\n",
    "created_at": "2008-09-25T10:21:00Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "pylab plots cut off",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4194",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

CC:  mvgnu @mwhansen @jasongrout

Keywords: plot

On Thursday 25 September 2008, Stan Schymanski wrote on [sage-support]:
> Dear all,

>
> When I upgraded to 3.1.2, I found that some of my plots generated
> using pylab in the notebooks miss their bottom bits. It seems to be
> related to the dpi setting. Example:

{{{
import pylab
x1 = srange(0,1.1,0.01)
d1 = [2*x+x^2 for x in x1]
pylab.clf() # clear the figure first
pylab.figure(1)
pylab.plot(x1,d1, label="d1")
pylab.ylabel("$f(x)$") # label the axes
pylab.xlabel("$x$")
pylab.savefig('foo.png',dpi=72) # fire!
}}}
> If I leave the "dpi=72" out in the last line, the plot is larger and
> complete. This problem did not occur in sage 3.1.1, so I assume that
> it is a bug.

Issue created by migration from https://trac.sagemath.org/ticket/4194





---

archive/issue_comments_030374.json:
```json
{
    "body": "This is because matplotlib doesn't like the Sage Integer 72.  If you change the 72 to int(72), then things work.  We should probably write an email to the matplotlib mailing list asking them how hard it would be to make it play nicely with Sage types.\n\nWe also encounter similar issues with numpy and scipy.",
    "created_at": "2008-09-27T00:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30374",
    "user": "https://github.com/mwhansen"
}
```

This is because matplotlib doesn't like the Sage Integer 72.  If you change the 72 to int(72), then things work.  We should probably write an email to the matplotlib mailing list asking them how hard it would be to make it play nicely with Sage types.

We also encounter similar issues with numpy and scipy.



---

archive/issue_comments_030375.json:
```json
{
    "body": "Attachment [foo.png](tarball://root/attachments/some-uuid/ticket4194/foo.png) by @kcrisman created at 2009-09-15 17:34:07\n\nTo release manager:\nThis now works, given #5448 (and possibly earlier).\n\n```\nsage: import pylab\nsage: x1 = srange(0,1.1,0.01)\nsage: d1 = [2*x+x^2 for x in x1]\nsage: pylab.clf() # clear the figure first\nsage: pylab.figure(1)\n<matplotlib.figure.Figure object at 0x16d41d0>\nsage: pylab.plot(x1,d1, label=\"d1\")\n[<matplotlib.lines.Line2D object at 0x102ceb0>]\nsage: pylab.ylabel(\"$f(x)$\") # label the axes\n<matplotlib.text.Text object at 0x4413f0>\nsage: pylab.xlabel(\"$x$\")\n<matplotlib.text.Text object at 0x1038890>\nsage: pylab.savefig('foo.png',dpi=72)\n```\nfoo.png is attached.",
    "created_at": "2009-09-15T17:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30375",
    "user": "https://github.com/kcrisman"
}
```

Attachment [foo.png](tarball://root/attachments/some-uuid/ticket4194/foo.png) by @kcrisman created at 2009-09-15 17:34:07

To release manager:
This now works, given #5448 (and possibly earlier).

```
sage: import pylab
sage: x1 = srange(0,1.1,0.01)
sage: d1 = [2*x+x^2 for x in x1]
sage: pylab.clf() # clear the figure first
sage: pylab.figure(1)
<matplotlib.figure.Figure object at 0x16d41d0>
sage: pylab.plot(x1,d1, label="d1")
[<matplotlib.lines.Line2D object at 0x102ceb0>]
sage: pylab.ylabel("$f(x)$") # label the axes
<matplotlib.text.Text object at 0x4413f0>
sage: pylab.xlabel("$x$")
<matplotlib.text.Text object at 0x1038890>
sage: pylab.savefig('foo.png',dpi=72)
```
foo.png is attached.



---

archive/issue_comments_030376.json:
```json
{
    "body": "kcrisman says this works now, so should be closed.",
    "created_at": "2009-09-29T16:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30376",
    "user": "https://github.com/jasongrout"
}
```

kcrisman says this works now, so should be closed.



---

archive/issue_comments_030377.json:
```json
{
    "body": "Don't close this.\n\nSomething really, really weird is going on.\n\nIn a fresh Sage session (not even in the notebook, just in a Sage console session), running the following (simplified from above) code produces png that is cut off which is about 12K:\n\n```\nimport matplotlib.pyplot as plt\nimport numpy\nplt.figure()\nplt.plot(numpy.arange(0,1.1,0.01))\nplt.savefig('foo.png',dpi=72) # fire!\n```\n\nHowever, immediately saving the figure again using `plt.savefig('foo.png',dpi=72)` writes a 13K file which is not cut off.\n\nDoing the same test with sage -python yields the correct figure the first time.  Doing the same test with the system python yields the correct figure the first time.  This is with the matplotlib 0.99.1 spkg installed.",
    "created_at": "2009-10-01T03:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30377",
    "user": "https://github.com/jasongrout"
}
```

Don't close this.

Something really, really weird is going on.

In a fresh Sage session (not even in the notebook, just in a Sage console session), running the following (simplified from above) code produces png that is cut off which is about 12K:

```
import matplotlib.pyplot as plt
import numpy
plt.figure()
plt.plot(numpy.arange(0,1.1,0.01))
plt.savefig('foo.png',dpi=72) # fire!
```

However, immediately saving the figure again using `plt.savefig('foo.png',dpi=72)` writes a 13K file which is not cut off.

Doing the same test with sage -python yields the correct figure the first time.  Doing the same test with the system python yields the correct figure the first time.  This is with the matplotlib 0.99.1 spkg installed.



---

archive/issue_comments_030378.json:
```json
{
    "body": "I've posted to the matplotlib-user mailing list today about this issue.",
    "created_at": "2009-10-01T16:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30378",
    "user": "https://github.com/jasongrout"
}
```

I've posted to the matplotlib-user mailing list today about this issue.



---

archive/issue_comments_030379.json:
```json
{
    "body": "With sage 4.6.0 it is still cut off (matplotlib 1.0.0)",
    "created_at": "2011-01-11T04:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30379",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

With sage 4.6.0 it is still cut off (matplotlib 1.0.0)



---

archive/issue_comments_030380.json:
```json
{
    "body": "for those interested, here is the matplotlib-users discussion\n\nhttp://sourceforge.net/mailarchive/forum.php?thread_name=6e8d907b0910061125o4f93bfb4u2ec934042c057ddd%40mail.gmail.com&forum_name=matplotlib-users",
    "created_at": "2011-01-11T04:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30380",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

for those interested, here is the matplotlib-users discussion

http://sourceforge.net/mailarchive/forum.php?thread_name=6e8d907b0910061125o4f93bfb4u2ec934042c057ddd%40mail.gmail.com&forum_name=matplotlib-users



---

archive/issue_comments_030381.json:
```json
{
    "body": "workaround for matplotlib 1.0.0 bug",
    "created_at": "2011-01-11T05:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30381",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

workaround for matplotlib 1.0.0 bug



---

archive/issue_comments_030382.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-11T05:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30382",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030383.json:
```json
{
    "body": "Attachment [trac_4196_mpl_workaround.patch](tarball://root/attachments/some-uuid/ticket4194/trac_4196_mpl_workaround.patch) by ryan created at 2011-01-11 05:33:10\n\naccording to the matplotlib-users discussion, the issue arises because the file is not flushed before being closed.  This patch correctly opens, writes and most importantly flush the file before closing.\n\nThe bug still appears to exist upstream.",
    "created_at": "2011-01-11T05:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30383",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_4196_mpl_workaround.patch](tarball://root/attachments/some-uuid/ticket4194/trac_4196_mpl_workaround.patch) by ryan created at 2011-01-11 05:33:10

according to the matplotlib-users discussion, the issue arises because the file is not flushed before being closed.  This patch correctly opens, writes and most importantly flush the file before closing.

The bug still appears to exist upstream.



---

archive/issue_comments_030384.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-11T06:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30384",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_030385.json:
```json
{
    "body": "see #10588.  Upgrading to matplotlib 1.0.1 should fix the issue",
    "created_at": "2011-01-11T06:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30385",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

see #10588.  Upgrading to matplotlib 1.0.1 should fix the issue



---

archive/issue_comments_030386.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-18T18:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30386",
    "user": "https://github.com/jasongrout"
}
```

Resolution: fixed



---

archive/issue_events_009513.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2011-10-18T18:25:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4194#event-9513"
}
```



---

archive/issue_comments_030387.json:
```json
{
    "body": "Indeed, this is now fixed.",
    "created_at": "2011-10-18T18:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4194#issuecomment-30387",
    "user": "https://github.com/jasongrout"
}
```

Indeed, this is now fixed.
