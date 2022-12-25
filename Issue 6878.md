# Issue 6878: [with patch, needs review] allow the exclusion of points from the plot range

archive/issues_006878.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: plot\n\nThe attached patch adds a new option 'exclude' to the plot command\nwhich allows to exclude points from the plot.\n\nThis is useful if there are discontinuities in the function you are plotting.\n\n\n```\nsage: plot(floor(x), (x, 1, 10), exclude = [1..10])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6878\n\n",
    "created_at": "2009-09-03T13:27:41Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "[with patch, needs review] allow the exclusion of points from the plot range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6878",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```
Assignee: @williamstein

Keywords: plot

The attached patch adds a new option 'exclude' to the plot command
which allows to exclude points from the plot.

This is useful if there are discontinuities in the function you are plotting.


```
sage: plot(floor(x), (x, 1, 10), exclude = [1..10])
```


Issue created by migration from https://trac.sagemath.org/ticket/6878





---

archive/issue_comments_056668.json:
```json
{
    "body": "Very nice!\n\nThis line:\n\n\n```\npoints = [e.right() for e in exclude.solve(v) if e.left() == v] \n```\n\n\nshould also check that v is not in the right side.  Alternatively, you could use the solution_dict parameter to make sure you get a solution.",
    "created_at": "2009-09-15T09:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56668",
    "user": "https://github.com/jasongrout"
}
```

Very nice!

This line:


```
points = [e.right() for e in exclude.solve(v) if e.left() == v] 
```


should also check that v is not in the right side.  Alternatively, you could use the solution_dict parameter to make sure you get a solution.



---

archive/issue_comments_056669.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> Very nice!\n> \n> This line:\n> \n> {{{\n> points = [e.right() for e in exclude.solve(v) if e.left() == v] \n> }}}\n> \n> should also check that v is not in the right side.  Alternatively, you could use the solution_dict parameter to make sure you get a solution.\n\nThe new version of the patch includes your suggestion.",
    "created_at": "2009-09-28T12:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56669",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Replying to [comment:1 jason]:
> Very nice!
> 
> This line:
> 
> {{{
> points = [e.right() for e in exclude.solve(v) if e.left() == v] 
> }}}
> 
> should also check that v is not in the right side.  Alternatively, you could use the solution_dict parameter to make sure you get a solution.

The new version of the patch includes your suggestion.



---

archive/issue_comments_056670.json:
```json
{
    "body": "Some more comments after examining things more carefully:\n\n* Use \"is not None\" rather than \"!= None\", as the \"is not None\" is way, way faster (it's a pointer comparison)\n\n* If I have just a few excluded points, but lots more poles, won't the break during the calculation of the exclusions also jump out of the loop that deals with detecting poles?  That means my poles past the last exclusion point are ignored.\n\n* Can you put a brief comment in about `(x0 < exclusion_point <= x1 or x0 <= exclusion_point < x1)`?  It may be just that it's too late, but this is confusing me a bit.\n\nThose are the only issues I find; the code other than that works fine.  I have not tested the output (nice doctests, though!).",
    "created_at": "2009-10-01T04:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56670",
    "user": "https://github.com/jasongrout"
}
```

Some more comments after examining things more carefully:

* Use "is not None" rather than "!= None", as the "is not None" is way, way faster (it's a pointer comparison)

* If I have just a few excluded points, but lots more poles, won't the break during the calculation of the exclusions also jump out of the loop that deals with detecting poles?  That means my poles past the last exclusion point are ignored.

* Can you put a brief comment in about `(x0 < exclusion_point <= x1 or x0 <= exclusion_point < x1)`?  It may be just that it's too late, but this is confusing me a bit.

Those are the only issues I find; the code other than that works fine.  I have not tested the output (nice doctests, though!).



---

archive/issue_comments_056671.json:
```json
{
    "body": "Attachment [trac_6878_exclude.patch](tarball://root/attachments/some-uuid/ticket6878/trac_6878_exclude.patch) by whuss created at 2009-10-16 15:52:20\n\nReplying to [comment:3 jason]:\n> Some more comments after examining things more carefully:\n> \n>  * Use \"is not None\" rather than \"!= None\", as the \"is not None\" is way, way faster (it's a pointer comparison)\n\nDone\n \n>  * If I have just a few excluded points, but lots more poles, won't the break during the calculation of the exclusions also jump out of the loop that deals with detecting poles?  That means my poles past the last exclusion point are ignored.\n\nYou are right. I have fixed this.\n\n>  * Can you put a brief comment in about `(x0 < exclusion_point <= x1 or x0 <= exclusion_point < x1)`?  It may be just that it's too late, but this is confusing me a bit.\n\nI don't know anymore why I have written it that way. I have changed it to\n\n`(x0 <= exclusion_point <= x1)`\n \n> Those are the only issues I find; the code other than that works fine.  I have not tested the output (nice doctests, though!).",
    "created_at": "2009-10-16T15:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56671",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [trac_6878_exclude.patch](tarball://root/attachments/some-uuid/ticket6878/trac_6878_exclude.patch) by whuss created at 2009-10-16 15:52:20

Replying to [comment:3 jason]:
> Some more comments after examining things more carefully:
> 
>  * Use "is not None" rather than "!= None", as the "is not None" is way, way faster (it's a pointer comparison)

Done
 
>  * If I have just a few excluded points, but lots more poles, won't the break during the calculation of the exclusions also jump out of the loop that deals with detecting poles?  That means my poles past the last exclusion point are ignored.

You are right. I have fixed this.

>  * Can you put a brief comment in about `(x0 < exclusion_point <= x1 or x0 <= exclusion_point < x1)`?  It may be just that it's too late, but this is confusing me a bit.

I don't know anymore why I have written it that way. I have changed it to

`(x0 <= exclusion_point <= x1)`
 
> Those are the only issues I find; the code other than that works fine.  I have not tested the output (nice doctests, though!).



---

archive/issue_comments_056672.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-16T15:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56672",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056673.json:
```json
{
    "body": "Changing assignee from @williamstein to whuss.",
    "created_at": "2009-12-20T10:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56673",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing assignee from @williamstein to whuss.



---

archive/issue_comments_056674.json:
```json
{
    "body": "Works as advertised with the caveat that if the exclusion points are less than xmin or greater than xmax then the plot range is extended (beyond either xmin and xmax). Statements below demonstrate this. \n\n(IMHO, I think this is new functionality that works and its easy to specify an exclude range that is inside xmin..xmax to get the plot range you want so it should go in the next milestone release - so Im giving it a positive review).\n\n\n```\nsage: plot(floor(x), xmin=0, xmax=10)              \n\nsage: plot(floor(x), xmin=0, xmax=10, exclude = [1..15])\n\nsage: plot(floor(x), xmin=0, xmax=10, exclude = [1..10])\n\nsage: plot(floor(x), xmin=0, xmax=10, exclude = [5..10])\n```\n\n\n(I guess if we dont want the exclusion points to modify the plot range - which is ideal - this should be in a new ticket)",
    "created_at": "2010-01-31T03:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56674",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Works as advertised with the caveat that if the exclusion points are less than xmin or greater than xmax then the plot range is extended (beyond either xmin and xmax). Statements below demonstrate this. 

(IMHO, I think this is new functionality that works and its easy to specify an exclude range that is inside xmin..xmax to get the plot range you want so it should go in the next milestone release - so Im giving it a positive review).


```
sage: plot(floor(x), xmin=0, xmax=10)              

sage: plot(floor(x), xmin=0, xmax=10, exclude = [1..15])

sage: plot(floor(x), xmin=0, xmax=10, exclude = [1..10])

sage: plot(floor(x), xmin=0, xmax=10, exclude = [5..10])
```


(I guess if we dont want the exclusion points to modify the plot range - which is ideal - this should be in a new ticket)



---

archive/issue_comments_056675.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T03:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56675",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056676.json:
```json
{
    "body": "The commit string is not sufficiently descriptive.  I've refreshed it to\n\n```\n#6878: Allow the exclusion of points from the plot range\n```\n\n\nin the queue for 4.3.3.alpha0.",
    "created_at": "2010-02-10T15:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56676",
    "user": "https://github.com/qed777"
}
```

The commit string is not sufficiently descriptive.  I've refreshed it to

```
#6878: Allow the exclusion of points from the plot range
```


in the queue for 4.3.3.alpha0.



---

archive/issue_comments_056677.json:
```json
{
    "body": "Please remember to update the relevant ticket fields --- the release managers use an automated script to generate lists of merged tickets.",
    "created_at": "2010-02-11T10:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56677",
    "user": "https://github.com/qed777"
}
```

Please remember to update the relevant ticket fields --- the release managers use an automated script to generate lists of merged tickets.



---

archive/issue_comments_056678.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56678",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_016176.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T14:59:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6878#event-16176"
}
```
