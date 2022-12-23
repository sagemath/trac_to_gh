# Issue 1365: golden_ratio._algebraic_() should synthesize the value

archive/issues_001365.json:
```json
{
    "body": "Assignee: was\n\nCC:  donmorrison robertwb\n\nRobert Bradshaw points out that golden_ratio._algebraic_ might as well synthesize the value, instead of using a special-purpose function in qqbar.py (and there's a patch to do this as part of Robert's patch at #1275).  But I want to make qqbar.py a bit more efficient for that case, before making the change.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1365\n\n",
    "created_at": "2007-12-02T05:28:02Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "title": "golden_ratio._algebraic_() should synthesize the value",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1365",
    "user": "cwitty"
}
```
Assignee: was

CC:  donmorrison robertwb

Robert Bradshaw points out that golden_ratio._algebraic_ might as well synthesize the value, instead of using a special-purpose function in qqbar.py (and there's a patch to do this as part of Robert's patch at #1275).  But I want to make qqbar.py a bit more efficient for that case, before making the change.

Issue created by migration from https://trac.sagemath.org/ticket/1365





---

archive/issue_comments_008736.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-02T18:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8736",
    "user": "cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008737.json:
```json
{
    "body": "Changing assignee from was to cwitty.",
    "created_at": "2007-12-02T18:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8737",
    "user": "cwitty"
}
```

Changing assignee from was to cwitty.



---

archive/issue_comments_008738.json:
```json
{
    "body": "Has this been resolved by #1275?  This ticket has had no change for nearly two years.",
    "created_at": "2009-09-28T20:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8738",
    "user": "kcrisman"
}
```

Has this been resolved by #1275?  This ticket has had no change for nearly two years.



---

archive/issue_comments_008739.json:
```json
{
    "body": "The docstring examples look like they return RLF(1/2*sqrt(5) + 1/2).  Since phi is known to be algebraic, would it be ok to just return that?",
    "created_at": "2010-11-07T19:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8739",
    "user": "donmorrison"
}
```

The docstring examples look like they return RLF(1/2*sqrt(5) + 1/2).  Since phi is known to be algebraic, would it be ok to just return that?



---

archive/issue_comments_008740.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-11-07T19:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8740",
    "user": "donmorrison"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_008741.json:
```json
{
    "body": "I tried RLF, and it's not the correct datatype for the current doctests and/or framework.  Certainly someone familiar with the internals must know the correct datatype...the ticket is only 3 years old.  If it's straightforward, I have a spare machine...",
    "created_at": "2010-11-09T00:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8741",
    "user": "donmorrison"
}
```

I tried RLF, and it's not the correct datatype for the current doctests and/or framework.  Certainly someone familiar with the internals must know the correct datatype...the ticket is only 3 years old.  If it's straightforward, I have a spare machine...



---

archive/issue_comments_008742.json:
```json
{
    "body": "\"return (field(5).sqrt() + 1) / 2\"\n\nWorks except for one test:\n\nFile \"/home/donmorrison/sage46fromsrc/sage/devel/sage/sage/rings/qqbar.py\",\nline 135:\n   sage: AA(golden_ratio)^2 - AA(golden_ratio)\nExpected:\n   1\nGot:\n   1.000000000000000?\n\nThe doctest could be changed to \nsage: bool(1 == AA(golden_ratio)^2 - AA(golden_ratio))\nTrue\n\nbut Robert says that's not good.  What's the next step?",
    "created_at": "2010-11-09T03:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8742",
    "user": "donmorrison"
}
```

"return (field(5).sqrt() + 1) / 2"

Works except for one test:

File "/home/donmorrison/sage46fromsrc/sage/devel/sage/sage/rings/qqbar.py",
line 135:
   sage: AA(golden_ratio)^2 - AA(golden_ratio)
Expected:
   1
Got:
   1.000000000000000?

The doctest could be changed to 
sage: bool(1 == AA(golden_ratio)^2 - AA(golden_ratio))
True

but Robert says that's not good.  What's the next step?



---

archive/issue_comments_008743.json:
```json
{
    "body": "Sorry, I didn't notice there was special trac markup obscuring my last update.\n\nThe former and proposed doctests should read:\n\nFile \"/home/donmorrison/sage46fromsrc/sage/devel/sage/sage/rings/qqbar.py\",\nline 135:\n\u00a0 \u00a0sage: AA(golden_ratio)!^2 - AA(golden_ratio)\nExpected:\n\u00a0 \u00a01\nGot:\n\u00a0 \u00a01.000000000000000?\n\nvs.\n\nsage: bool(1 ==\u00a0AA(golden_ratio)!^2 - AA(golden_ratio))\n\nTrue",
    "created_at": "2010-11-09T03:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8743",
    "user": "donmorrison"
}
```

Sorry, I didn't notice there was special trac markup obscuring my last update.

The former and proposed doctests should read:

File "/home/donmorrison/sage46fromsrc/sage/devel/sage/sage/rings/qqbar.py",
line 135:
   sage: AA(golden_ratio)!^2 - AA(golden_ratio)
Expected:
   1
Got:
   1.000000000000000?

vs.

sage: bool(1 == AA(golden_ratio)!^2 - AA(golden_ratio))

True



---

archive/issue_comments_008744.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2010-11-09T07:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8744",
    "user": "robertwb"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_comments_008745.json:
```json
{
    "body": "I'm thinking this ticket could just be closed--the current way of doing things works fine (lots has changed since this ticket was opened, in particular the entire Sage symbolics system was moved to PyNaC, so this isn't very relevant anymore. In particular, I don't see any benefit to the `AA(golden_ratio)^2 - AA(golden_ratio)` regression.",
    "created_at": "2010-11-09T07:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8745",
    "user": "robertwb"
}
```

I'm thinking this ticket could just be closed--the current way of doing things works fine (lots has changed since this ticket was opened, in particular the entire Sage symbolics system was moved to PyNaC, so this isn't very relevant anymore. In particular, I don't see any benefit to the `AA(golden_ratio)^2 - AA(golden_ratio)` regression.



---

archive/issue_comments_008746.json:
```json
{
    "body": "I agree with Robert's analysis.",
    "created_at": "2011-12-17T20:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8746",
    "user": "mhansen"
}
```

I agree with Robert's analysis.



---

archive/issue_comments_008747.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-12-17T20:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1365#issuecomment-8747",
    "user": "mhansen"
}
```

Resolution: invalid
