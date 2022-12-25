# Issue 3133: allow parametric_plot and parametric_plot3d to take a vector as input

archive/issues_003133.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman @jasongrout\n\n\n```\n\n\nOn Thu, May 8, 2008 at 1:32 AM, Dan Drake <drake@mathsci.kaist.ac.kr> wrote:\n> I'm teaching ODEs right now and I'd like to plot the usual sort of\n>  solution to a 2-by-2 linear DE system, but the following doesn't work:\n>  \n>   sage: evec = vector([1,2])\n>   sage: var('t')\n>   sage: parametric_plot( exp(-t) * evec, 0, 2)\n>  \n>  The traceback's complaint is \"<type 'exceptions.TypeError'>: function\n>  takes at most 1 positional arguments (2 given)\".\n>  \n>  I know I could manually do (exp(-t), 2*exp(-t)), but the above form\n>  seems so natural. Is there a way to get that to work?\n\nYou could type\n\nsage: parametric_plot( list(exp(-t) * evec), 0, 2)\n\nI think it would be reasonable for us to improve parametric_plot so that it takes a vector \nas input instead of just a list or tuple. \n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3133\n\n",
    "created_at": "2008-05-08T13:58:14Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "allow parametric_plot and parametric_plot3d to take a vector as input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3133",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @kcrisman @jasongrout


```


On Thu, May 8, 2008 at 1:32 AM, Dan Drake <drake@mathsci.kaist.ac.kr> wrote:
> I'm teaching ODEs right now and I'd like to plot the usual sort of
>  solution to a 2-by-2 linear DE system, but the following doesn't work:
>  
>   sage: evec = vector([1,2])
>   sage: var('t')
>   sage: parametric_plot( exp(-t) * evec, 0, 2)
>  
>  The traceback's complaint is "<type 'exceptions.TypeError'>: function
>  takes at most 1 positional arguments (2 given)".
>  
>  I know I could manually do (exp(-t), 2*exp(-t)), but the above form
>  seems so natural. Is there a way to get that to work?

You could type

sage: parametric_plot( list(exp(-t) * evec), 0, 2)

I think it would be reasonable for us to improve parametric_plot so that it takes a vector 
as input instead of just a list or tuple. 

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/3133





---

archive/issue_comments_021713.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2009-03-06T21:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21713",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_021714.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-06T21:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21714",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021715.json:
```json
{
    "body": "As a test, the following should work:\n\n\n```\nsage: var('x')\nsage: parametric_plot(vector([x,2*x,3*x^2]), (x,-1,3))\n```\n",
    "created_at": "2009-03-06T21:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21715",
    "user": "https://github.com/jasongrout"
}
```

As a test, the following should work:


```
sage: var('x')
sage: parametric_plot(vector([x,2*x,3*x^2]), (x,-1,3))
```




---

archive/issue_comments_021716.json:
```json
{
    "body": "The error is different now too:\n\n\n```\nsage: sage: var('x')\nx\nsage: sage: parametric_plot(vector([x,2*x,3*x^2]), (x,-1,3))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (21, 0))\n\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/grout/.sage/temp/good/20161/_home_grout__sage_init_sage_0.py in <module>()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.pyc in parametric_plot(funcs, *args, **kwargs)\n   1892         return plot(funcs, *args, **kwargs)\n   1893     elif (num_funcs == 3 and num_vars <= 2):\n-> 1894         return sage.plot.plot3d.parametric_plot3d.parametric_plot3d(funcs, *args, **kwargs)\n   1895     else:\n   1896         raise ValueError, \"the number of functions and the number of free variables is not a possible combination for 2d or 3d parametric plots\"\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.pyc in parametric_plot3d(f, urange, vrange, plot_points, **kwds)\n    372             \n    373     if not isinstance(f, (tuple, list)) or len(f) != 3:\n--> 374         raise ValueError, \"f must be a list or tuple of length 3\"\n    375 \n    376     if vrange is None:\n\nValueError: f must be a list or tuple of length 3\nsage: \n```\n",
    "created_at": "2009-03-06T21:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21716",
    "user": "https://github.com/jasongrout"
}
```

The error is different now too:


```
sage: sage: var('x')
x
sage: sage: parametric_plot(vector([x,2*x,3*x^2]), (x,-1,3))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (21, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/grout/.sage/temp/good/20161/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.pyc in parametric_plot(funcs, *args, **kwargs)
   1892         return plot(funcs, *args, **kwargs)
   1893     elif (num_funcs == 3 and num_vars <= 2):
-> 1894         return sage.plot.plot3d.parametric_plot3d.parametric_plot3d(funcs, *args, **kwargs)
   1895     else:
   1896         raise ValueError, "the number of functions and the number of free variables is not a possible combination for 2d or 3d parametric plots"

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.pyc in parametric_plot3d(f, urange, vrange, plot_points, **kwds)
    372             
    373     if not isinstance(f, (tuple, list)) or len(f) != 3:
--> 374         raise ValueError, "f must be a list or tuple of length 3"
    375 
    376     if vrange is None:

ValueError: f must be a list or tuple of length 3
sage: 
```




---

archive/issue_comments_021717.json:
```json
{
    "body": "See #3315 for another input format that parametric_plot should take (functions returning tuples)",
    "created_at": "2009-03-06T21:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21717",
    "user": "https://github.com/jasongrout"
}
```

See #3315 for another input format that parametric_plot should take (functions returning tuples)



---

archive/issue_comments_021718.json:
```json
{
    "body": "Attachment [trac-3133-parametric_plot-vector.patch](tarball://root/attachments/some-uuid/ticket3133/trac-3133-parametric_plot-vector.patch) by @jasongrout created at 2009-09-17 21:44:17",
    "created_at": "2009-09-17T21:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21718",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-3133-parametric_plot-vector.patch](tarball://root/attachments/some-uuid/ticket3133/trac-3133-parametric_plot-vector.patch) by @jasongrout created at 2009-09-17 21:44:17



---

archive/issue_comments_021719.json:
```json
{
    "body": "Positive review of the content.  My only concern is that the \"internal\" functions now have their names changed so we could possibly have to deprecate the non-underscored versions of them (however, only using the underscored ones).   What do you think?  Probably it's unnecessary, since they were never in the global namespace.",
    "created_at": "2009-09-18T12:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21719",
    "user": "https://github.com/kcrisman"
}
```

Positive review of the content.  My only concern is that the "internal" functions now have their names changed so we could possibly have to deprecate the non-underscored versions of them (however, only using the underscored ones).   What do you think?  Probably it's unnecessary, since they were never in the global namespace.



---

archive/issue_comments_021720.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> Positive review of the content.  My only concern is that the \"internal\" functions now have their names changed so we could possibly have to deprecate the non-underscored versions of them (however, only using the underscored ones).   What do you think?  Probably it's unnecessary, since they were never in the global namespace.\n\nI thought it was probably okay since they were not in the global namespace *and* their documentation said that they were internal functions.  I was just making them more conventional internal functions.\n\nIf you'd like I can make them deprecated.  Let me know.  I think it's okay in this case to just change the names.",
    "created_at": "2009-09-18T14:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21720",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:5 kcrisman]:
> Positive review of the content.  My only concern is that the "internal" functions now have their names changed so we could possibly have to deprecate the non-underscored versions of them (however, only using the underscored ones).   What do you think?  Probably it's unnecessary, since they were never in the global namespace.

I thought it was probably okay since they were not in the global namespace *and* their documentation said that they were internal functions.  I was just making them more conventional internal functions.

If you'd like I can make them deprecated.  Let me know.  I think it's okay in this case to just change the names.



---

archive/issue_comments_021721.json:
```json
{
    "body": "My thoughts exactly, actually - just wanted to see what your reasoning was.",
    "created_at": "2009-09-18T14:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21721",
    "user": "https://github.com/kcrisman"
}
```

My thoughts exactly, actually - just wanted to see what your reasoning was.



---

archive/issue_comments_021722.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-19T20:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21722",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_021723.json:
```json
{
    "body": "See #6963 for a follow up to this ticket.",
    "created_at": "2009-09-19T20:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3133#issuecomment-21723",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #6963 for a follow up to this ticket.
