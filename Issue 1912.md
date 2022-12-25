# Issue 1912: Displaying a list of graphic objects prints what appears to be an empty list

archive/issues_001912.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\n```\n\n> As a final comment, I'll note that the following behavior with objects\n> which automatically display is interesting:\n> \n> sage: C=circle((0,0),1);P=plot(sin,0,1)\n> sage: [C,P]\n> [, ]\n> \n> and then a display of circle above a plot of sin (in the notebook) or\n> two separate pictures (in the command line).  I have no idea what, if\n> any, connection should be made with this work, though.\n\nI think it is just printing out the list for you to see and the \"print\" function for a graphics object displays the object, so you see each object \"printed\" out.\n\nIt would be nice if the text display indicated this, instead of \"[, ]\".  Maybe something like \"[<Graphic object>, <Graphic object>]\", since the objects actually are there.  It misleadingly looks like you have an empty list.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1912\n\n",
    "created_at": "2008-01-24T16:08:14Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Displaying a list of graphic objects prints what appears to be an empty list",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1912",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @kcrisman

```

> As a final comment, I'll note that the following behavior with objects
> which automatically display is interesting:
> 
> sage: C=circle((0,0),1);P=plot(sin,0,1)
> sage: [C,P]
> [, ]
> 
> and then a display of circle above a plot of sin (in the notebook) or
> two separate pictures (in the command line).  I have no idea what, if
> any, connection should be made with this work, though.

I think it is just printing out the list for you to see and the "print" function for a graphics object displays the object, so you see each object "printed" out.

It would be nice if the text display indicated this, instead of "[, ]".  Maybe something like "[<Graphic object>, <Graphic object>]", since the objects actually are there.  It misleadingly looks like you have an empty list.
```


Issue created by migration from https://trac.sagemath.org/ticket/1912





---

archive/issue_comments_012079.json:
```json
{
    "body": "> It would be nice if the text display indicated this, instead of \"[, ]\".  Maybe \n> something like \"[<Graphic object>, <Graphic object>]\", since the objects \n> actually are there.  It misleadingly looks like you have an empty list.\n\n\nI agree.  However, I have *absolutely no clue* how or even if this is possible to implement in Python.  I almost think it isn't.   More precisely, we could easily\nmake it so we have\n \n sage: plot(sin, 0,1)\n <Graphic object>\n [an actual image]\n\nbut that would be really ugly. \n\nWilliam",
    "created_at": "2008-01-24T16:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12079",
    "user": "https://github.com/williamstein"
}
```

> It would be nice if the text display indicated this, instead of "[, ]".  Maybe 
> something like "[<Graphic object>, <Graphic object>]", since the objects 
> actually are there.  It misleadingly looks like you have an empty list.


I agree.  However, I have *absolutely no clue* how or even if this is possible to implement in Python.  I almost think it isn't.   More precisely, we could easily
make it so we have
 
 sage: plot(sin, 0,1)
 <Graphic object>
 [an actual image]

but that would be really ugly. 

William



---

archive/issue_comments_012080.json:
```json
{
    "body": "Actually, I vaguely recall there is a \"displayhook\" in Python that is called\nwhen one types\n\n```\n sage: <arbitrary object>\n```\nMaybe we could overload that so if <arbitrary object> is a list or tuple then\ninstead of calling _repr_ on each graphics object, we call __str__.\n\n\nWilliam\n\nIt's weird.  Every time I think something is impossible I immediately seem to think of a solution...",
    "created_at": "2008-01-24T16:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12080",
    "user": "https://github.com/williamstein"
}
```

Actually, I vaguely recall there is a "displayhook" in Python that is called
when one types

```
 sage: <arbitrary object>
```
Maybe we could overload that so if <arbitrary object> is a list or tuple then
instead of calling _repr_ on each graphics object, we call __str__.


William

It's weird.  Every time I think something is impossible I immediately seem to think of a solution...



---

archive/issue_comments_012081.json:
```json
{
    "body": "Another idea: make it return <Graphic object> whenever it creates an object; but in IPython/the notebook, check to see if it's about to print \"<Graphic object>\", and if so print nothing instead.",
    "created_at": "2008-01-24T18:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12081",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Another idea: make it return <Graphic object> whenever it creates an object; but in IPython/the notebook, check to see if it's about to print "<Graphic object>", and if so print nothing instead.



---

archive/issue_comments_012082.json:
```json
{
    "body": "> It's weird. Every time I think something is impossible I immediately seem to think of a solution...\n\n\nWe ought to put you in charge of more hard problems!  So...do you think it's impossible to prove the Riemann hypothesis? :)",
    "created_at": "2008-01-24T18:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12082",
    "user": "https://github.com/jasongrout"
}
```

> It's weird. Every time I think something is impossible I immediately seem to think of a solution...


We ought to put you in charge of more hard problems!  So...do you think it's impossible to prove the Riemann hypothesis? :)



---

archive/issue_comments_012083.json:
```json
{
    "body": "I think either of these solutions works okay, but I prefer the first since it clearly tells the user that they just constructed a list of graphic objects.\n\n```\nsage: [graphic1, graphic2]\n# Displays each graphic, as well as:\n[<graphic object>, <graphic object>]\n```\n\n```\nsage: [graphic1, graphic2]\n# Displays each graphic, but doesn't print anything\n```\n\nJust for comparison, Mathematica 6 actually prints out the graphics, surrounded by the delimiters (so the graphics are really inside the list and appear that way) when using the notebook and prints out just a string representation {-Graphics-} when used from the command line.",
    "created_at": "2008-01-24T18:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12083",
    "user": "https://github.com/jasongrout"
}
```

I think either of these solutions works okay, but I prefer the first since it clearly tells the user that they just constructed a list of graphic objects.

```
sage: [graphic1, graphic2]
# Displays each graphic, as well as:
[<graphic object>, <graphic object>]
```

```
sage: [graphic1, graphic2]
# Displays each graphic, but doesn't print anything
```

Just for comparison, Mathematica 6 actually prints out the graphics, surrounded by the delimiters (so the graphics are really inside the list and appear that way) when using the notebook and prints out just a string representation {-Graphics-} when used from the command line.



---

archive/issue_comments_012084.json:
```json
{
    "body": "This idea of Jason Grout is the sort of thing we can do to solve this sort of problem:\n\n```\ndef pretty_print (object):\n    if object is None:\n        return\n    if isinstance(object, (sage.plot.plot.Graphics, sage.plot.plot3d.base.Graphics3d)):\n        print repr(object)\n        return\n    import __builtin__\n    __builtin__._=object\n    try:\n        print html(\"$$\"+latex(object)+\"$$\")\n    except:\n        import sys\n        sys.__displayhook__(object)\n\ndef notebook_pretty(enable=True):\n    import sys\n    if enable:\n        sys.displayhook = pretty_print\n    else:\n        sys.displayhook = sys.__displayhook__\n\n# To enable the pretty-printing\nnotebook_pretty(True)\n```",
    "created_at": "2008-01-25T06:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12084",
    "user": "https://github.com/williamstein"
}
```

This idea of Jason Grout is the sort of thing we can do to solve this sort of problem:

```
def pretty_print (object):
    if object is None:
        return
    if isinstance(object, (sage.plot.plot.Graphics, sage.plot.plot3d.base.Graphics3d)):
        print repr(object)
        return
    import __builtin__
    __builtin__._=object
    try:
        print html("$$"+latex(object)+"$$")
    except:
        import sys
        sys.__displayhook__(object)

def notebook_pretty(enable=True):
    import sys
    if enable:
        sys.displayhook = pretty_print
    else:
        sys.displayhook = sys.__displayhook__

# To enable the pretty-printing
notebook_pretty(True)
```



---

archive/issue_comments_012085.json:
```json
{
    "body": "See #1922 for the above pretty_print functions.",
    "created_at": "2008-01-25T08:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12085",
    "user": "https://github.com/jasongrout"
}
```

See #1922 for the above pretty_print functions.



---

archive/issue_events_004602.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1912#event-4602"
}
```



---

archive/issue_events_004603.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1912#event-4603"
}
```



---

archive/issue_events_004604.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1912#event-4604"
}
```



---

archive/issue_events_004605.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2014-02-15T13:29:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1912#event-4605"
}
```



---

archive/issue_events_004606.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2014-02-15T13:29:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1912#event-4606"
}
```



---

archive/issue_comments_012086.json:
```json
{
    "body": "Appears to be fixed, most probably as part of #14469. And there is already a doctest covering this behaviour.",
    "created_at": "2014-02-15T13:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12086",
    "user": "https://github.com/mezzarobba"
}
```

Appears to be fixed, most probably as part of #14469. And there is already a doctest covering this behaviour.



---

archive/issue_comments_012087.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-15T13:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12087",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_012088.json:
```json
{
    "body": "Ok, I think this can be closed.",
    "created_at": "2014-03-05T09:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12088",
    "user": "https://github.com/fchapoton"
}
```

Ok, I think this can be closed.



---

archive/issue_comments_012089.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-05T09:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12089",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_012090.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-03-05T17:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1912#issuecomment-12090",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_004607.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-03-05T17:00:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1912",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1912#event-4607"
}
```
