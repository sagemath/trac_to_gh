# Issue 9261: RealIntervalField: enable option style='bracket'

archive/issues_009261.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @williamstein cwitty @mwhansen\n\nCurrently, the option style='bracket' (to display intervals as\n[1.1 ... 1.2]) is only available in the `str` method, so that\none has to provide it each time one calls str.\n\nIt would be nice to have an option style=... in the *creation* of the\nfield, to override the default style. For example one would have:\n\n```\nsage: R = RealIntervalField(42, style='brackets')\nsage: R(pi)\n[3.1415926535892 .. 3.1415926535902]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9261\n\n",
    "created_at": "2010-06-18T10:01:29Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "RealIntervalField: enable option style='bracket'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9261",
    "user": "@zimmermann6"
}
```
Assignee: @aghitza

CC:  @williamstein cwitty @mwhansen

Currently, the option style='bracket' (to display intervals as
[1.1 ... 1.2]) is only available in the `str` method, so that
one has to provide it each time one calls str.

It would be nice to have an option style=... in the *creation* of the
field, to override the default style. For example one would have:

```
sage: R = RealIntervalField(42, style='brackets')
sage: R(pi)
[3.1415926535892 .. 3.1415926535902]
```


Issue created by migration from https://trac.sagemath.org/ticket/9261





---

archive/issue_comments_087151.json:
```json
{
    "body": "This is almost implemented in #7682.  The patch there is probably ready for review, but it's been a while since I looked at the patch, so it should probably have doctests run and possibly have a bit more documentation written.  And it would be nice to implement this ticket either on top of #7682, or just by adding a few lines to #7682.",
    "created_at": "2010-06-18T16:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9261#issuecomment-87151",
    "user": "@jasongrout"
}
```

This is almost implemented in #7682.  The patch there is probably ready for review, but it's been a while since I looked at the patch, so it should probably have doctests run and possibly have a bit more documentation written.  And it would be nice to implement this ticket either on top of #7682, or just by adding a few lines to #7682.



---

archive/issue_comments_087152.json:
```json
{
    "body": "I don't like the idea of putting the print style in the parent.  (I think the current sci_not is a design error that shouldn't be perpetuated.)\n\nOne problem is that if you have objects like `RealIntervalField(42, style='brackets')(pi)` and `RealIntervalField(42)(pi)`, then arithmetic between them is slower than between objects with the same parent.  Also, there are several parts of Sage that create their own `RealIntervalField` parents and return elements to the user, so the option you suggest would not suffice to hide question-mark printing from the user.\n\nIMHO a global setting is a more sensible option; would that be all right, or do you really want the setting to be per-parent?\n\nIf a global setting is acceptable, then we're in luck, because it already exists: :)\n\n```\nsage: a = RIF(pi)\nsage: a\n3.141592653589794?\nsage: sage.rings.real_mpfi.printing_style = 'brackets'\nsage: a\n[3.1415926535897931 .. 3.1415926535897936]\n```\n\n\nWe could certainly document this global setting (I think it's entirely undocumented now), if that would help.",
    "created_at": "2010-07-20T21:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9261#issuecomment-87152",
    "user": "cwitty"
}
```

I don't like the idea of putting the print style in the parent.  (I think the current sci_not is a design error that shouldn't be perpetuated.)

One problem is that if you have objects like `RealIntervalField(42, style='brackets')(pi)` and `RealIntervalField(42)(pi)`, then arithmetic between them is slower than between objects with the same parent.  Also, there are several parts of Sage that create their own `RealIntervalField` parents and return elements to the user, so the option you suggest would not suffice to hide question-mark printing from the user.

IMHO a global setting is a more sensible option; would that be all right, or do you really want the setting to be per-parent?

If a global setting is acceptable, then we're in luck, because it already exists: :)

```
sage: a = RIF(pi)
sage: a
3.141592653589794?
sage: sage.rings.real_mpfi.printing_style = 'brackets'
sage: a
[3.1415926535897931 .. 3.1415926535897936]
```


We could certainly document this global setting (I think it's entirely undocumented now), if that would help.



---

archive/issue_comments_087153.json:
```json
{
    "body": "> We could certainly document this global setting (I think it's entirely undocumented now), if that would help. \n\nI strongly support this. This global setting was something I was missing since a long time, it is\nnow in my init.sage file.",
    "created_at": "2010-07-21T07:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9261#issuecomment-87153",
    "user": "@zimmermann6"
}
```

> We could certainly document this global setting (I think it's entirely undocumented now), if that would help. 

I strongly support this. This global setting was something I was missing since a long time, it is
now in my init.sage file.



---

archive/issue_comments_087154.json:
```json
{
    "body": "Replying to [comment:2 cwitty]:\n\n> IMHO a global setting is a more sensible option; would that be all right, or do you really want the setting to be per-parent?\n\n+1 to making such things (and keeping such things) global settings.",
    "created_at": "2010-07-21T08:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9261#issuecomment-87154",
    "user": "@jasongrout"
}
```

Replying to [comment:2 cwitty]:

> IMHO a global setting is a more sensible option; would that be all right, or do you really want the setting to be per-parent?

+1 to making such things (and keeping such things) global settings.



---

archive/issue_comments_087155.json:
```json
{
    "body": "I'm OK with this, because it only impacts the *appearance* (not the mathematics) of the elements.",
    "created_at": "2010-07-21T10:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9261#issuecomment-87155",
    "user": "@williamstein"
}
```

I'm OK with this, because it only impacts the *appearance* (not the mathematics) of the elements.
