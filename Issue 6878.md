# Issue 6878: [with patch, needs review] allow the exclusion of points from the plot range

archive/issues_006878.json:
```json
{
    "body": "Assignee: was\n\nKeywords: plot\n\nThe attached patch adds a new option 'exclude' to the plot command\nwhich allows to exclude points from the plot.\n\nThis is useful if there are discontinuities in the function you are plotting.\n\n\n```\nsage: plot(floor(x), (x, 1, 10), exclude = [1..10])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6878\n\n",
    "created_at": "2009-09-03T13:27:41Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] allow the exclusion of points from the plot range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6878",
    "user": "whuss"
}
```
Assignee: was

Keywords: plot

The attached patch adds a new option 'exclude' to the plot command
which allows to exclude points from the plot.

This is useful if there are discontinuities in the function you are plotting.


```
sage: plot(floor(x), (x, 1, 10), exclude = [1..10])
```


Issue created by migration from https://trac.sagemath.org/ticket/6878





---

archive/issue_comments_056774.json:
```json
{
    "body": "Very nice!\n\nThis line:\n\n\n```\npoints = [e.right() for e in exclude.solve(v) if e.left() == v] \n```\n\n\nshould also check that v is not in the right side.  Alternatively, you could use the solution_dict parameter to make sure you get a solution.",
    "created_at": "2009-09-15T09:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56774",
    "user": "jason"
}
```

Very nice!

This line:


```
points = [e.right() for e in exclude.solve(v) if e.left() == v] 
```


should also check that v is not in the right side.  Alternatively, you could use the solution_dict parameter to make sure you get a solution.



---

archive/issue_comments_056775.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> Very nice!\n> \n> This line:\n> \n> {{{\n> points = [e.right() for e in exclude.solve(v) if e.left() == v] \n> }}}\n> \n> should also check that v is not in the right side.  Alternatively, you could use the solution_dict parameter to make sure you get a solution.\n\nThe new version of the patch includes your suggestion.",
    "created_at": "2009-09-28T12:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56775",
    "user": "whuss"
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

archive/issue_comments_056776.json:
```json
{
    "body": "Some more comments after examining things more carefully:\n\n* Use \"is not None\" rather than \"!= None\", as the \"is not None\" is way, way faster (it's a pointer comparison)\n\n* If I have just a few excluded points, but lots more poles, won't the break during the calculation of the exclusions also jump out of the loop that deals with detecting poles?  That means my poles past the last exclusion point are ignored.\n\n* Can you put a brief comment in about `(x0 < exclusion_point <= x1 or x0 <= exclusion_point < x1)`?  It may be just that it's too late, but this is confusing me a bit.\n\nThose are the only issues I find; the code other than that works fine.  I have not tested the output (nice doctests, though!).",
    "created_at": "2009-10-01T04:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56776",
    "user": "jason"
}
```

Some more comments after examining things more carefully:

* Use "is not None" rather than "!= None", as the "is not None" is way, way faster (it's a pointer comparison)

* If I have just a few excluded points, but lots more poles, won't the break during the calculation of the exclusions also jump out of the loop that deals with detecting poles?  That means my poles past the last exclusion point are ignored.

* Can you put a brief comment in about `(x0 < exclusion_point <= x1 or x0 <= exclusion_point < x1)`?  It may be just that it's too late, but this is confusing me a bit.

Those are the only issues I find; the code other than that works fine.  I have not tested the output (nice doctests, though!).



---

archive/issue_comments_056777.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:3 jason]:\n> Some more comments after examining things more carefully:\n> \n>  * Use \"is not None\" rather than \"!= None\", as the \"is not None\" is way, way faster (it's a pointer comparison)\n\nDone\n \n>  * If I have just a few excluded points, but lots more poles, won't the break during the calculation of the exclusions also jump out of the loop that deals with detecting poles?  That means my poles past the last exclusion point are ignored.\n\nYou are right. I have fixed this.\n\n>  * Can you put a brief comment in about `(x0 < exclusion_point <= x1 or x0 <= exclusion_point < x1)`?  It may be just that it's too late, but this is confusing me a bit.\n\nI don't know anymore why I have written it that way. I have changed it to\n\n`(x0 <= exclusion_point <= x1)`\n \n> Those are the only issues I find; the code other than that works fine.  I have not tested the output (nice doctests, though!).",
    "created_at": "2009-10-16T15:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56777",
    "user": "whuss"
}
```

Attachment

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

archive/issue_comments_056778.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-16T15:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56778",
    "user": "whuss"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056779.json:
```json
{
    "body": "Changing assignee from was to whuss.",
    "created_at": "2009-12-20T10:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56779",
    "user": "whuss"
}
```

Changing assignee from was to whuss.



---

archive/issue_comments_056780.json:
```json
{
    "body": "Works as advertised with the caveat that if the exclusion points are less than xmin or greater than xmax then the plot range is extended (beyond either xmin and xmax). Statements below demonstrate this. \n\n(IMHO, I think this is new functionality that works and its easy to specify an exclude range that is inside xmin..xmax to get the plot range you want so it should go in the next milestone release - so Im giving it a positive review).\n\n\n```\nsage: plot(floor(x), xmin=0, xmax=10)              \n\nsage: plot(floor(x), xmin=0, xmax=10, exclude = [1..15])\n\nsage: plot(floor(x), xmin=0, xmax=10, exclude = [1..10])\n\nsage: plot(floor(x), xmin=0, xmax=10, exclude = [5..10])\n```\n\n\n(I guess if we dont want the exclusion points to modify the plot range - which is ideal - this should be in a new ticket)",
    "created_at": "2010-01-31T03:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56780",
    "user": "rossk"
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

archive/issue_comments_056781.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T03:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56781",
    "user": "rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056782.json:
```json
{
    "body": "The commit string is not sufficiently descriptive.  I've refreshed it to\n\n```\n#6878: Allow the exclusion of points from the plot range\n```\n\n\nin the queue for 4.3.3.alpha0.",
    "created_at": "2010-02-10T15:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56782",
    "user": "mpatel"
}
```

The commit string is not sufficiently descriptive.  I've refreshed it to

```
#6878: Allow the exclusion of points from the plot range
```


in the queue for 4.3.3.alpha0.



---

archive/issue_comments_056783.json:
```json
{
    "body": "Please remember to update the relevant ticket fields --- the release managers use an automated script to generate lists of merged tickets.",
    "created_at": "2010-02-11T10:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56783",
    "user": "mpatel"
}
```

Please remember to update the relevant ticket fields --- the release managers use an automated script to generate lists of merged tickets.



---

archive/issue_comments_056784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6878#issuecomment-56784",
    "user": "mpatel"
}
```

Resolution: fixed
