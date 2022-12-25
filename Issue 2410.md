# Issue 2410: parametric_plot and constants

archive/issues_002410.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is a companion to #2409\n\n```\nsage: parametric_plot((t^2,t),-12,12)\n```\nworks as expected, but \n\n```\nsage: parametric_plot((1,t),-12,12)\n...\n<type 'exceptions.TypeError'>: 'float' object is unsubscriptable\n```\ndoes not.\n\nMore generally, I would like to see the following syntax supported \n\n```\nsage: parametric_plot((1,t),(t,-12,12))\n```\nwhich is much cleaner mathematically (no hidden reliance on variable name 't') and is also very analogous to \n\n```\nsage: plot(t,(t,-12,12))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2410\n\n",
    "created_at": "2008-03-06T20:48:30Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "parametric_plot and constants",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2410",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @williamstein

This is a companion to #2409

```
sage: parametric_plot((t^2,t),-12,12)
```
works as expected, but 

```
sage: parametric_plot((1,t),-12,12)
...
<type 'exceptions.TypeError'>: 'float' object is unsubscriptable
```
does not.

More generally, I would like to see the following syntax supported 

```
sage: parametric_plot((1,t),(t,-12,12))
```
which is much cleaner mathematically (no hidden reliance on variable name 't') and is also very analogous to 

```
sage: plot(t,(t,-12,12))
```


Issue created by migration from https://trac.sagemath.org/ticket/2410





---

archive/issue_events_005683.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-07T02:40:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2410",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2410#event-5683"
}
```



---

archive/issue_comments_016233.json:
```json
{
    "body": "For reference:\n\nparametric_plot3d automatically calls fast_float on its arguments correctly, so parametric_plot3d((1,t,2), (t,-1,3)), for example, just works.\n\nWhy are we not calling fast_float on functions in plot() or parametric_plot?  Probably because noone has had time to implement it; contour plots and vector plots both do it.  I'll open a new ticket.\n\nHere, I'll post a patch which corrects a bug in how exceptions are handled in plot.  Currently, the TypeError that is being triggered is then ignored when plot tries to access the non-existent data point (the data[i][1] line).  This changes the error in this case from a nonsensical indexing error to a sensible \"Can't call an Integer\" error (from trying to evaluate 1(-12).",
    "created_at": "2008-08-25T21:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2410#issuecomment-16233",
    "user": "https://github.com/jasongrout"
}
```

For reference:

parametric_plot3d automatically calls fast_float on its arguments correctly, so parametric_plot3d((1,t,2), (t,-1,3)), for example, just works.

Why are we not calling fast_float on functions in plot() or parametric_plot?  Probably because noone has had time to implement it; contour plots and vector plots both do it.  I'll open a new ticket.

Here, I'll post a patch which corrects a bug in how exceptions are handled in plot.  Currently, the TypeError that is being triggered is then ignored when plot tries to access the non-existent data point (the data[i][1] line).  This changes the error in this case from a nonsensical indexing error to a sensible "Can't call an Integer" error (from trying to evaluate 1(-12).



---

archive/issue_comments_016234.json:
```json
{
    "body": "Attachment [plotting-exceptions.patch](tarball://root/attachments/some-uuid/ticket2410/plotting-exceptions.patch) by @jasongrout created at 2008-08-25 21:53:53",
    "created_at": "2008-08-25T21:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2410#issuecomment-16234",
    "user": "https://github.com/jasongrout"
}
```

Attachment [plotting-exceptions.patch](tarball://root/attachments/some-uuid/ticket2410/plotting-exceptions.patch) by @jasongrout created at 2008-08-25 21:53:53



---

archive/issue_comments_016235.json:
```json
{
    "body": "See #3952 for the fast_float request.",
    "created_at": "2008-08-25T22:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2410#issuecomment-16235",
    "user": "https://github.com/jasongrout"
}
```

See #3952 for the fast_float request.



---

archive/issue_comments_016236.json:
```json
{
    "body": "The other issues will be fixed in #3952.",
    "created_at": "2008-08-26T01:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2410#issuecomment-16236",
    "user": "https://github.com/mwhansen"
}
```

The other issues will be fixed in #3952.



---

archive/issue_comments_016237.json:
```json
{
    "body": "Attachment [trac_2140.patch](tarball://root/attachments/some-uuid/ticket2410/trac_2140.patch) by @mwhansen created at 2008-08-26 03:00:40\n\nApply trac_2140.patch _after_ #3853",
    "created_at": "2008-08-26T03:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2410#issuecomment-16237",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_2140.patch](tarball://root/attachments/some-uuid/ticket2410/trac_2140.patch) by @mwhansen created at 2008-08-26 03:00:40

Apply trac_2140.patch _after_ #3853



---

archive/issue_comments_016238.json:
```json
{
    "body": "Merged trac_2140.patch in Sage 3.1.2.alpha1",
    "created_at": "2008-08-26T03:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2410#issuecomment-16238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_2140.patch in Sage 3.1.2.alpha1



---

archive/issue_events_005684.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-26T03:44:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2410",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2410#event-5684"
}
```



---

archive/issue_comments_016239.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-26T03:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2410#issuecomment-16239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
