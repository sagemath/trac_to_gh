# Issue 9911: extraneous argument in deprecation in #7154

archive/issues_009911.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  ryan\n\nIn #7154, the rename_keyword deprecation decorator has an extra argument.  Right now, it's:\n\n\n```\n@rename_keyword(deprecated='Sage 4.6', deprecated_option='thickness', thickness='width') \n```\n\n\nbut should just be\n\n\n```\n@rename_keyword(deprecated='Sage 4.6', thickness='width') \n```\n\n\nMy bad for not catching this in the review stage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9912\n\n",
    "created_at": "2010-09-15T13:47:29Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "extraneous argument in deprecation in #7154",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9911",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  ryan

In #7154, the rename_keyword deprecation decorator has an extra argument.  Right now, it's:


```
@rename_keyword(deprecated='Sage 4.6', deprecated_option='thickness', thickness='width') 
```


but should just be


```
@rename_keyword(deprecated='Sage 4.6', thickness='width') 
```


My bad for not catching this in the review stage.

Issue created by migration from https://trac.sagemath.org/ticket/9912





---

archive/issue_comments_098427.json:
```json
{
    "body": "Just for the record, this then also needs to be fixed:\n\n```\nsage -t -long \"devel/sage/sage/geometry/polyhedra.py\"       \n**********************************************************************\nFile \"/home/leif/Sage/sage-4.6.alpha1/devel/sage/sage/geometry/polyhedra.py\", line 1270:\n    sage: p1.projection().show() + p2.projection().show() + p3.projection().show()\nExpected nothing\nGot:\n    doctest:4555: DeprecationWarning: (Since Sage 4.6) use the option 'width' instead of 'thickness'\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of  14 in __main__.example_66\n***Test Failed*** 1 failures.\n```\n",
    "created_at": "2010-09-16T09:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9911#issuecomment-98427",
    "user": "https://github.com/nexttime"
}
```

Just for the record, this then also needs to be fixed:

```
sage -t -long "devel/sage/sage/geometry/polyhedra.py"       
**********************************************************************
File "/home/leif/Sage/sage-4.6.alpha1/devel/sage/sage/geometry/polyhedra.py", line 1270:
    sage: p1.projection().show() + p2.projection().show() + p3.projection().show()
Expected nothing
Got:
    doctest:4555: DeprecationWarning: (Since Sage 4.6) use the option 'width' instead of 'thickness'
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_66
***Test Failed*** 1 failures.
```




---

archive/issue_comments_098428.json:
```json
{
    "body": "Leif: is that the only failure in all long doctests (i.e., ptestlong or similar?)\n\nIf not, I'll run ptestlong to check.",
    "created_at": "2010-09-16T09:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9911#issuecomment-98428",
    "user": "https://github.com/jasongrout"
}
```

Leif: is that the only failure in all long doctests (i.e., ptestlong or similar?)

If not, I'll run ptestlong to check.



---

archive/issue_comments_098429.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> Leif: is that the only failure in all long doctests (i.e., ptestlong or similar?)\n\nThe only one related to this (`DeprecationWarning`) with the *unreleased* 4.6.alpha1.\n\nIf you put the deprecation warning into the doctest (\"expected\"), don't forget to not hard-code the line number (from `ncadoctest.py`!).",
    "created_at": "2010-09-16T09:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9911#issuecomment-98429",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:2 jason]:
> Leif: is that the only failure in all long doctests (i.e., ptestlong or similar?)

The only one related to this (`DeprecationWarning`) with the *unreleased* 4.6.alpha1.

If you put the deprecation warning into the doctest ("expected"), don't forget to not hard-code the line number (from `ncadoctest.py`!).



---

archive/issue_comments_098430.json:
```json
{
    "body": "Outdated, should close",
    "created_at": "2021-09-10T06:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9911#issuecomment-98430",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should close



---

archive/issue_comments_098431.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-09-10T06:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9911#issuecomment-98431",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098432.json:
```json
{
    "body": "I agree",
    "created_at": "2021-09-10T11:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9911#issuecomment-98432",
    "user": "https://github.com/kwankyu"
}
```

I agree



---

archive/issue_comments_098433.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-09-10T11:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9911#issuecomment-98433",
    "user": "https://github.com/kwankyu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098434.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-09-10T17:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9911#issuecomment-98434",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid



---

archive/issue_events_010038.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-09-10T17:33:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9911",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9911#event-10038"
}
```
