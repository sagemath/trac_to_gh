# Issue 1575: plotting -- fix vector plotting

archive/issues_001575.json:
```json
{
    "body": "Assignee: was\n\n\n```\nOn Dec 19, 2007 12:24 PM, Jason Grout <> wrote:\n> I'm teaching linear algebra next semester and plan to use Sage.  In\n> trying the \"obvious\" way to plot a vector:\n> \n> sage: v=vector([1,2])\n> sage: v.plot().show()\n> \n> I get what looks like a step function of the coordinates. \n\nYes, that's what it is.  This is very useful, e.g., when using\nvectors of data, computing Fourier transforms of them, etc. \nAnd it works in arbitrary dimensions.  \n\n>  Instead, I\n> have to do:\n> \n> sage: v=vector([1,2])\n> sage: arrow((0,0),v).show()\n> \n> which doesn't seem quite so natural to an undergraduate linear algebra\n> student.  First, is there an easier way to plot a vector (yes, I know I\n> don't have to define v above and could just give the coordinates to\n> arrow, but usually I'll be doing something with v as a vector)?  Is it\n> reasonable to redefine v.plot() to return the arrow for a vector with 3\n> or fewer dimensions, or is there some bigger reason to have things the\n> way they are now?\n\nI think that would be bad, because it's potentially confusing and\nunsystematic.  However, the following -- which you will like --\nwould be acceptable to me:\n\n   Redefine v.plot() so for dimensions <= 3 it does what you describe above,\ni.e., draws an arrow, but for dimensions >= 4 it gives an error message.\nThen add an option to plot called \"step\", which if set to True restores\nthe current behavior.    \n\nIn fact, this was my intention all along, and somehow I screwed up. \nThe current plot signature for vectors is:\n\n    def plot(self, xmin=0, xmax=1, eps=None, res=None,\n             connect=True, step=False, **kwds):\n\nNotice that step=False is already there!  \n\n\n\n-- William\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1575\n\n",
    "created_at": "2007-12-20T18:47:13Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "plotting -- fix vector plotting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1575",
    "user": "was"
}
```
Assignee: was


```
On Dec 19, 2007 12:24 PM, Jason Grout <> wrote:
> I'm teaching linear algebra next semester and plan to use Sage.  In
> trying the "obvious" way to plot a vector:
> 
> sage: v=vector([1,2])
> sage: v.plot().show()
> 
> I get what looks like a step function of the coordinates. 

Yes, that's what it is.  This is very useful, e.g., when using
vectors of data, computing Fourier transforms of them, etc. 
And it works in arbitrary dimensions.  

>  Instead, I
> have to do:
> 
> sage: v=vector([1,2])
> sage: arrow((0,0),v).show()
> 
> which doesn't seem quite so natural to an undergraduate linear algebra
> student.  First, is there an easier way to plot a vector (yes, I know I
> don't have to define v above and could just give the coordinates to
> arrow, but usually I'll be doing something with v as a vector)?  Is it
> reasonable to redefine v.plot() to return the arrow for a vector with 3
> or fewer dimensions, or is there some bigger reason to have things the
> way they are now?

I think that would be bad, because it's potentially confusing and
unsystematic.  However, the following -- which you will like --
would be acceptable to me:

   Redefine v.plot() so for dimensions <= 3 it does what you describe above,
i.e., draws an arrow, but for dimensions >= 4 it gives an error message.
Then add an option to plot called "step", which if set to True restores
the current behavior.    

In fact, this was my intention all along, and somehow I screwed up. 
The current plot signature for vectors is:

    def plot(self, xmin=0, xmax=1, eps=None, res=None,
             connect=True, step=False, **kwds):

Notice that step=False is already there!  



-- William

```


Issue created by migration from https://trac.sagemath.org/ticket/1575





---

archive/issue_comments_010016.json:
```json
{
    "body": "Changing assignee from was to jason grout.",
    "created_at": "2007-12-20T18:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10016",
    "user": "was"
}
```

Changing assignee from was to jason grout.



---

archive/issue_comments_010017.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-21T09:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10017",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010018.json:
```json
{
    "body": "Changing assignee from jason grout to jason.",
    "created_at": "2007-12-21T09:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10018",
    "user": "jason"
}
```

Changing assignee from jason grout to jason.



---

archive/issue_comments_010019.json:
```json
{
    "body": "Attachment [vector-plot.patch](tarball://root/attachments/some-uuid/ticket1575/vector-plot.patch) by jason created at 2007-12-21 09:02:36",
    "created_at": "2007-12-21T09:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10019",
    "user": "jason"
}
```

Attachment [vector-plot.patch](tarball://root/attachments/some-uuid/ticket1575/vector-plot.patch) by jason created at 2007-12-21 09:02:36



---

archive/issue_comments_010020.json:
```json
{
    "body": "In vector-plot.patch, plot is redefined to behave thusly:\n\n* the option \"type\" has values 'arrow', 'point', and 'step'\n* if 1 <= dimension <= 3, default type='arrow'\n* if dimension > 3, default type='step'\n\nThe old plot function was renamed plot_step.",
    "created_at": "2007-12-21T09:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10020",
    "user": "jason"
}
```

In vector-plot.patch, plot is redefined to behave thusly:

* the option "type" has values 'arrow', 'point', and 'step'
* if 1 <= dimension <= 3, default type='arrow'
* if dimension > 3, default type='step'

The old plot function was renamed plot_step.



---

archive/issue_comments_010021.json:
```json
{
    "body": "I just discovered that Arrow has been changed to arrow3d in sage 2.9.3.  The patch should be updated accordingly.",
    "created_at": "2008-01-15T12:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10021",
    "user": "jason"
}
```

I just discovered that Arrow has been changed to arrow3d in sage 2.9.3.  The patch should be updated accordingly.



---

archive/issue_comments_010022.json:
```json
{
    "body": "Attachment [vector-plot-updated.patch](tarball://root/attachments/some-uuid/ticket1575/vector-plot-updated.patch) by jason created at 2008-01-15 23:23:03",
    "created_at": "2008-01-15T23:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10022",
    "user": "jason"
}
```

Attachment [vector-plot-updated.patch](tarball://root/attachments/some-uuid/ticket1575/vector-plot-updated.patch) by jason created at 2008-01-15 23:23:03



---

archive/issue_comments_010023.json:
```json
{
    "body": "I've renamed the \"type\" option to \"plot_type\" and fixed the Arrow issue (the graphics interface changed around 2.9.3) and the doctest \"eps\" issue.\n\nThe vector-plot-updated.patch should be applied instead of vector-plot.patch.",
    "created_at": "2008-01-15T23:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10023",
    "user": "jason"
}
```

I've renamed the "type" option to "plot_type" and fixed the Arrow issue (the graphics interface changed around 2.9.3) and the doctest "eps" issue.

The vector-plot-updated.patch should be applied instead of vector-plot.patch.



---

archive/issue_comments_010024.json:
```json
{
    "body": "Looks good; doctests pass.",
    "created_at": "2008-01-27T03:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10024",
    "user": "cwitty"
}
```

Looks good; doctests pass.



---

archive/issue_comments_010025.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T03:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10025",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010026.json:
```json
{
    "body": "vector-plot-updated.patch merged in Sage 2.10.1.rc1.",
    "created_at": "2008-01-27T03:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1575#issuecomment-10026",
    "user": "mabshoff"
}
```

vector-plot-updated.patch merged in Sage 2.10.1.rc1.
