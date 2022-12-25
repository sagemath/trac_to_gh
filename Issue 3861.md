# Issue 3861: automatic line smoothing shouldn't be automatic, or should at least be documented

archive/issues_003861.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman @slel\n\nKeywords: line3d, Line, smoothing, corner_cutoff\n\nline3d for instance calls Line in \n\n/usr/local/sage/3.0.6/devel/sage/sage/plot/plot3d/shapes2.py\n\nWhich automatically applies some smoothing using corner_cutoff, which is buggy and poorly documented as in Ticket 3859:\nhttp://trac.sagemath.org/sage_trac/ticket/3859\n\n(See above Ticket for an example of how this can be bad.)\n\nIt is important that I plot lines directly, and automatic smoothing should either not be automatic, or should be documented,\neven for functions that do not reference the smoothing directly like in Line3d.  Perhaps a 'smooth' keyword is more informative than the undocumented corner_cutoff.\n\nThe smoothing is done in the Line class object, and not in pmol, so it can (and should!) be selectively applied.\n\nFixing the referenced ticket is a workaround (set corner_cutoff = 1), but is very clunky, and currently does not even work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3861\n\n",
    "created_at": "2008-08-14T22:19:12Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "automatic line smoothing shouldn't be automatic, or should at least be documented",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3861",
    "user": "https://trac.sagemath.org/admin/accounts/users/mclean"
}
```
Assignee: @williamstein

CC:  @kcrisman @slel

Keywords: line3d, Line, smoothing, corner_cutoff

line3d for instance calls Line in 

/usr/local/sage/3.0.6/devel/sage/sage/plot/plot3d/shapes2.py

Which automatically applies some smoothing using corner_cutoff, which is buggy and poorly documented as in Ticket 3859:
http://trac.sagemath.org/sage_trac/ticket/3859

(See above Ticket for an example of how this can be bad.)

It is important that I plot lines directly, and automatic smoothing should either not be automatic, or should be documented,
even for functions that do not reference the smoothing directly like in Line3d.  Perhaps a 'smooth' keyword is more informative than the undocumented corner_cutoff.

The smoothing is done in the Line class object, and not in pmol, so it can (and should!) be selectively applied.

Fixing the referenced ticket is a workaround (set corner_cutoff = 1), but is very clunky, and currently does not even work.

Issue created by migration from https://trac.sagemath.org/ticket/3861





---

archive/issue_comments_027455.json:
```json
{
    "body": "I like the idea of a smoothnes parameter, 0=False meaning don't smooth at all, 1=True being some good default, and something higher (say 2) to forceable splite the whole thing. \n\nI agree it could be better documented, but I think smoothing is very useful when you are trying to visualize curves. Of course, if you're plotting stock data then it is really bad.",
    "created_at": "2008-08-16T01:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3861#issuecomment-27455",
    "user": "https://github.com/robertwb"
}
```

I like the idea of a smoothnes parameter, 0=False meaning don't smooth at all, 1=True being some good default, and something higher (say 2) to forceable splite the whole thing. 

I agree it could be better documented, but I think smoothing is very useful when you are trying to visualize curves. Of course, if you're plotting stock data then it is really bad.



---

archive/issue_comments_027456.json:
```json
{
    "body": "I also agree with Robert.  Notice also that:\n\n\n```\n\nsage: my_points=[[0,0,0],[1,0,0],[0,1,0]]\nsage: my_points_tuples=map(tuple,my_points)\nsage: sage.plot.plot3d.shapes2.Line(my_points,corner_cutoff=0)\nTraceback (most recent call last):\n...\nTypeError: unhashable type: 'list'\n\nsage.plot.plot3d.shapes2.Line(my_points_tuples,corner_cutoff=0) #works\nsage: sage.plot.plot3d.shapes2.Line(my_points_tuples, corner_cutoff=1)\nTraceback (most recent call last):\n...\nTypeError: 'NoneType' object is unsubscriptable\nsage: sage.plot.plot3d.shapes2.Line(my_points_tuples, corner_cutoff=.999) # works\n\n```\n",
    "created_at": "2010-04-27T15:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3861#issuecomment-27456",
    "user": "https://github.com/jasongrout"
}
```

I also agree with Robert.  Notice also that:


```

sage: my_points=[[0,0,0],[1,0,0],[0,1,0]]
sage: my_points_tuples=map(tuple,my_points)
sage: sage.plot.plot3d.shapes2.Line(my_points,corner_cutoff=0)
Traceback (most recent call last):
...
TypeError: unhashable type: 'list'

sage.plot.plot3d.shapes2.Line(my_points_tuples,corner_cutoff=0) #works
sage: sage.plot.plot3d.shapes2.Line(my_points_tuples, corner_cutoff=1)
Traceback (most recent call last):
...
TypeError: 'NoneType' object is unsubscriptable
sage: sage.plot.plot3d.shapes2.Line(my_points_tuples, corner_cutoff=.999) # works

```




---

archive/issue_comments_027457.json:
```json
{
    "body": "That last error is already #3859",
    "created_at": "2010-04-27T15:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3861#issuecomment-27457",
    "user": "https://github.com/jasongrout"
}
```

That last error is already #3859



---

archive/issue_events_008845.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3861#event-8845"
}
```



---

archive/issue_events_008846.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3861#event-8846"
}
```



---

archive/issue_events_008847.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3861#event-8847"
}
```



---

archive/issue_events_008848.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3861#event-8848"
}
```



---

archive/issue_events_008849.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3861#event-8849"
}
```



---

archive/issue_events_008850.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3861#event-8850"
}
```



---

archive/issue_events_008851.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3861#event-8851"
}
```



---

archive/issue_comments_027458.json:
```json
{
    "body": "Related:\n\n- #3546: line3d with jmol draws curves instead of straight lines",
    "created_at": "2021-04-27T22:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3861#issuecomment-27458",
    "user": "https://github.com/slel"
}
```

Related:

- #3546: line3d with jmol draws curves instead of straight lines



---

archive/issue_events_008852.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2021-04-27T22:07:44Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3861#event-8852"
}
```



---

archive/issue_events_008853.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2021-04-27T22:07:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3861",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3861#event-8853"
}
```
