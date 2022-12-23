# Issue 5649: plot doesn't work when x-range too small

archive/issues_005649.json:
```json
{
    "body": "Assignee: was\n\n\n```\nHow about:\n\nplot(P(6.403124+x), 0, 0.00001) -> okay\nplot(P(6.403124+x), 0, 0.000001) -> tick marks on both axes are\nmissing\nplot(P(6.403124+x), 0, 0.0000001) -> IndexError: list index out of\nrange\nplot(P(x), 0, 0.0001) -> ZeroDivisionError: float division\n\nThis doesn't look too good...\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5649\n\n",
    "created_at": "2009-03-31T15:48:08Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "plot doesn't work when x-range too small",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5649",
    "user": "was"
}
```
Assignee: was


```
How about:

plot(P(6.403124+x), 0, 0.00001) -> okay
plot(P(6.403124+x), 0, 0.000001) -> tick marks on both axes are
missing
plot(P(6.403124+x), 0, 0.0000001) -> IndexError: list index out of
range
plot(P(x), 0, 0.0001) -> ZeroDivisionError: float division

This doesn't look too good...
```



Issue created by migration from https://trac.sagemath.org/ticket/5649





---

archive/issue_comments_044107.json:
```json
{
    "body": "See [http://groups.google.com/group/sage-devel/browse_thread/thread/ddd9584a4bf457db](http://groups.google.com/group/sage-devel/browse_thread/thread/ddd9584a4bf457db) for a y-axis variant on this, namely\n\n\n```\nplot(2^(-20*x),(x,1,10)) \n```\n",
    "created_at": "2009-06-26T18:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44107",
    "user": "kcrisman"
}
```

See [http://groups.google.com/group/sage-devel/browse_thread/thread/ddd9584a4bf457db](http://groups.google.com/group/sage-devel/browse_thread/thread/ddd9584a4bf457db) for a y-axis variant on this, namely


```
plot(2^(-20*x),(x,1,10)) 
```




---

archive/issue_comments_044108.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-26T20:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44108",
    "user": "kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044109.json:
```json
{
    "body": "Changing assignee from was to kcrisman.",
    "created_at": "2009-06-26T20:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44109",
    "user": "kcrisman"
}
```

Changing assignee from was to kcrisman.



---

archive/issue_comments_044110.json:
```json
{
    "body": "This patch fixes most of the problems above, and has a doctest for it.\n\nThis does not fix the final example, because that is a bug in _tasteless_ticks and the numbers it is inputting to srange (presumably someone step is 0, though I couldn't reproduce it with actual numbers).  Assuming this patch is okay, recommend opening a separate ticket for improving _tasteless_ticks handling of small numbers.",
    "created_at": "2009-06-26T20:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44110",
    "user": "kcrisman"
}
```

This patch fixes most of the problems above, and has a doctest for it.

This does not fix the final example, because that is a bug in _tasteless_ticks and the numbers it is inputting to srange (presumably someone step is 0, though I couldn't reproduce it with actual numbers).  Assuming this patch is okay, recommend opening a separate ticket for improving _tasteless_ticks handling of small numbers.



---

archive/issue_comments_044111.json:
```json
{
    "body": "Attachment\n\nI would like to review this patch, but I don't understand how to reproduce the bug. What is \"P\" from the examples in the ticket description?",
    "created_at": "2009-07-16T18:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44111",
    "user": "wcauchois"
}
```

Attachment

I would like to review this patch, but I don't understand how to reproduce the bug. What is "P" from the examples in the ticket description?



---

archive/issue_comments_044112.json:
```json
{
    "body": "It was from a sage-devel discussion the reporter didn't include (http://groups.google.com/group/sage-devel/browse_thread/thread/0e9c7b897851e5de).    Anway, \n\n```\nP(x)=5*x^2 - 205 \n```\n\nin that case. But you can replicate it by making sure you have a small enough range (e.g. somewhat less than <10**-6) on any plot.   There's a small chance this will have to be rebased, but I hope that no one has been messing with axes much recently.",
    "created_at": "2009-07-16T18:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44112",
    "user": "kcrisman"
}
```

It was from a sage-devel discussion the reporter didn't include (http://groups.google.com/group/sage-devel/browse_thread/thread/0e9c7b897851e5de).    Anway, 

```
P(x)=5*x^2 - 205 
```

in that case. But you can replicate it by making sure you have a small enough range (e.g. somewhat less than <10**-6) on any plot.   There's a small chance this will have to be rebased, but I hope that no one has been messing with axes much recently.



---

archive/issue_comments_044113.json:
```json
{
    "body": "Replying to [comment:4 kcrisman]:\n\nIt applies fine to Sage 4.1. The first three examples work great with your changes, but the last one still raises a ZeroDivisionError. I'm using that function you gave me. Is there still a problem?",
    "created_at": "2009-07-16T19:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44113",
    "user": "wcauchois"
}
```

Replying to [comment:4 kcrisman]:

It applies fine to Sage 4.1. The first three examples work great with your changes, but the last one still raises a ZeroDivisionError. I'm using that function you gave me. Is there still a problem?



---

archive/issue_comments_044114.json:
```json
{
    "body": "No, as I say above, that is a problem with _tasteless_ticks and its handling of small numbers.  That should really be in a separate ticket, but I don't want to open it until I'm ready to tackle it.  You can feel free to do so, however :)",
    "created_at": "2009-07-16T19:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44114",
    "user": "kcrisman"
}
```

No, as I say above, that is a problem with _tasteless_ticks and its handling of small numbers.  That should really be in a separate ticket, but I don't want to open it until I'm ready to tackle it.  You can feel free to do so, however :)



---

archive/issue_comments_044115.json:
```json
{
    "body": "REFEREE REPORT\n\nI'd like to give this a positive review. Applies fine to Sage 4.1, and plot tick marks work better now in a great many cases.\n\nI feel like the readability of _tasteful_ticks() could be improved. Better variable names would help (\"d0\", \"d1\", and \"p\" were hard to decipher). It also looks like there is some duplicated code that could be factored out into a separate method like maybe \"extract_two_digits_and_place_value\". We can leave the refactor for another ticket perhaps :).",
    "created_at": "2009-07-16T19:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44115",
    "user": "wcauchois"
}
```

REFEREE REPORT

I'd like to give this a positive review. Applies fine to Sage 4.1, and plot tick marks work better now in a great many cases.

I feel like the readability of _tasteful_ticks() could be improved. Better variable names would help ("d0", "d1", and "p" were hard to decipher). It also looks like there is some duplicated code that could be factored out into a separate method like maybe "extract_two_digits_and_place_value". We can leave the refactor for another ticket perhaps :).



---

archive/issue_comments_044116.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T22:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44116",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_044117.json:
```json
{
    "body": "> I feel like the readability of _tasteful_ticks() could be improved. Better variable names would help (\"d0\", \"d1\", and \"p\" were hard to decipher). It also looks like there is some duplicated code that could be factored out into a separate method like maybe \"extract_two_digits_and_place_value\". We can leave the refactor for another ticket perhaps :).\n\nSee #6548.  In general there is a lot of work that could be done in axes.py when it comes to documentation and functionality.  There are several other open tickets that have partial code to either significantly rewrite it or to use matplotlib axes - but so far both these solutions have proved more difficult than just slowly improving what already exists.",
    "created_at": "2009-07-17T13:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5649#issuecomment-44117",
    "user": "kcrisman"
}
```

> I feel like the readability of _tasteful_ticks() could be improved. Better variable names would help ("d0", "d1", and "p" were hard to decipher). It also looks like there is some duplicated code that could be factored out into a separate method like maybe "extract_two_digits_and_place_value". We can leave the refactor for another ticket perhaps :).

See #6548.  In general there is a lot of work that could be done in axes.py when it comes to documentation and functionality.  There are several other open tickets that have partial code to either significantly rewrite it or to use matplotlib axes - but so far both these solutions have proved more difficult than just slowly improving what already exists.
