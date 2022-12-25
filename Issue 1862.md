# Issue 1862: implement at least some sort of useful rudimentary implicit 2d plotting function

archive/issues_001862.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  harald.schilly@gmail.com\n\n```\n{{{\nOn Jan 19, 2008 12:44 AM, Dagda <> wrote:\n> \n> Hi,\n> I was wondering if there was a way to plot relations implicitly, in 2D\n> and/or 3D. A simple example would be to plot a circle with something\n> like the following:\n> \n> plot_implicit(x^2+y^2=1)\n\nHere's how do this sort of thing using contour_plot in sage right now.\n(Note -- for efficiency reasons, you definitely want to only plot a Python\nfunction -- i.e., lambda -- at present.  This will change soon.)\n\nFirst, define this function in Sage:\n\ndef implicit_plot(f, x_range, y_range, plot_points=100):\n      return contour_plot(f, x_range, y_range, fill=False, contours=1, plot_points=plot_points)\n\nThen use it:\n\nsage: implicit_plot(lambda x,y: x^2 + y^2 - 1, (-2,2), (-2,2))\nsage: implicit_plot(lambda x,y: x^3 + x*y^2 - 1, (-2,2), (-2,2))\nsage: implicit_plot(lambda x,y: (x-y^2)*(y-x^3), (-2,2), (-2,2))\n\nThe input should be a function f of two variables, and implicit_plot as I've\ndefined it above graphs f(x,y) == 0 in the given region.\n\nThis could be turned into a first version of a genuine implicit plot at some point. \n\nJosh Kantor is also looking into some other more sophisticated related\napproaches.    It would be good to understand precisely how Sage's\ncontour_plot function works (it builds mostly on matplotlib's functions)....\n\nWilliam\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/1862\n\n",
    "created_at": "2008-01-20T07:52:09Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "implement at least some sort of useful rudimentary implicit 2d plotting function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1862",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  harald.schilly@gmail.com

```
{{{
On Jan 19, 2008 12:44 AM, Dagda <> wrote:
> 
> Hi,
> I was wondering if there was a way to plot relations implicitly, in 2D
> and/or 3D. A simple example would be to plot a circle with something
> like the following:
> 
> plot_implicit(x^2+y^2=1)

Here's how do this sort of thing using contour_plot in sage right now.
(Note -- for efficiency reasons, you definitely want to only plot a Python
function -- i.e., lambda -- at present.  This will change soon.)

First, define this function in Sage:

def implicit_plot(f, x_range, y_range, plot_points=100):
      return contour_plot(f, x_range, y_range, fill=False, contours=1, plot_points=plot_points)

Then use it:

sage: implicit_plot(lambda x,y: x^2 + y^2 - 1, (-2,2), (-2,2))
sage: implicit_plot(lambda x,y: x^3 + x*y^2 - 1, (-2,2), (-2,2))
sage: implicit_plot(lambda x,y: (x-y^2)*(y-x^3), (-2,2), (-2,2))

The input should be a function f of two variables, and implicit_plot as I've
defined it above graphs f(x,y) == 0 in the given region.

This could be turned into a first version of a genuine implicit plot at some point. 

Josh Kantor is also looking into some other more sophisticated related
approaches.    It would be good to understand precisely how Sage's
contour_plot function works (it builds mostly on matplotlib's functions)....

William
}}}

Issue created by migration from https://trac.sagemath.org/ticket/1862





---

archive/issue_comments_011759.json:
```json
{
    "body": "Robert Bradshaw's bundle at #1938 includes this functionality.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-26T13:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1862#issuecomment-11759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Robert Bradshaw's bundle at #1938 includes this functionality.

Cheers,

Michael



---

archive/issue_comments_011760.json:
```json
{
    "body": "> Robert Bradshaw's bundle at #1938 includes this functionality.\n\n\n\nI just refereed that patch and I can't find any implicit_plot functionality in it...",
    "created_at": "2008-01-27T17:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1862#issuecomment-11760",
    "user": "https://github.com/williamstein"
}
```

> Robert Bradshaw's bundle at #1938 includes this functionality.



I just refereed that patch and I can't find any implicit_plot functionality in it...



---

archive/issue_comments_011761.json:
```json
{
    "body": "Attachment [implicit-plot.patch](tarball://root/attachments/some-uuid/ticket1862/implicit-plot.patch) by cwitty created at 2008-03-02 18:31:33",
    "created_at": "2008-03-02T18:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1862#issuecomment-11761",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [implicit-plot.patch](tarball://root/attachments/some-uuid/ticket1862/implicit-plot.patch) by cwitty created at 2008-03-02 18:31:33



---

archive/issue_comments_011762.json:
```json
{
    "body": "This patch adds implicit_plot (based on contour_plot, as William suggests).  It also fixes some broken code (and adds doctests) elsewhere in plot.py .",
    "created_at": "2008-03-02T18:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1862#issuecomment-11762",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

This patch adds implicit_plot (based on contour_plot, as William suggests).  It also fixes some broken code (and adds doctests) elsewhere in plot.py .



---

archive/issue_comments_011763.json:
```json
{
    "body": "Some problems:\n\n```\nsage: x,y=var(\"x,y\")\nsage: implicit_plot(x^2+y^2-1,(-1,1),(-1,1))\n```\ntakes a very long time (in fact, I tried to kill it using ctl-c repeatedly and had a hard time).\nOn the other hand,\n\n```\nsage: f = lambda x,y: x^2+y^2-1\nsage: implicit_plot(f,(-1,1),(-1,1))\n```\nis almost instantaneous.\nCan this be fixed or at least documented?",
    "created_at": "2008-03-03T12:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1862#issuecomment-11763",
    "user": "https://github.com/wdjoyner"
}
```

Some problems:

```
sage: x,y=var("x,y")
sage: implicit_plot(x^2+y^2-1,(-1,1),(-1,1))
```
takes a very long time (in fact, I tried to kill it using ctl-c repeatedly and had a hard time).
On the other hand,

```
sage: f = lambda x,y: x^2+y^2-1
sage: implicit_plot(f,(-1,1),(-1,1))
```
is almost instantaneous.
Can this be fixed or at least documented?



---

archive/issue_comments_011764.json:
```json
{
    "body": "> Can this be fixed or at least documented?\n\n\nThis should be trivial to fix by changing implicit_plot to call fast_float.  In fact, then the relevant part of your first example would be 10 times faster than the second.",
    "created_at": "2008-03-03T13:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1862#issuecomment-11764",
    "user": "https://github.com/williamstein"
}
```

> Can this be fixed or at least documented?


This should be trivial to fix by changing implicit_plot to call fast_float.  In fact, then the relevant part of your first example would be 10 times faster than the second.



---

archive/issue_events_004507.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-03-12T04:58:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1862#event-4507"
}
```



---

archive/issue_comments_011765.json:
```json
{
    "body": "Attachment [1862.patch](tarball://root/attachments/some-uuid/ticket1862/1862.patch) by @mwhansen created at 2008-03-15 23:20:32\n\nI've put up a version of the patch ( 1862.patch ) rebased against 2.10.4.alpha0.  That's the one that should be applied.  Other than that, looks good to me.",
    "created_at": "2008-03-15T23:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1862#issuecomment-11765",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1862.patch](tarball://root/attachments/some-uuid/ticket1862/1862.patch) by @mwhansen created at 2008-03-15 23:20:32

I've put up a version of the patch ( 1862.patch ) rebased against 2.10.4.alpha0.  That's the one that should be applied.  Other than that, looks good to me.



---

archive/issue_comments_011766.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T02:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1862#issuecomment-11766",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011767.json:
```json
{
    "body": "Merged 1862.patch in Sage 2.10.4.rc0",
    "created_at": "2008-03-16T02:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1862#issuecomment-11767",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 1862.patch in Sage 2.10.4.rc0



---

archive/issue_events_004508.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T02:53:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1862",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1862#event-4508"
}
```
