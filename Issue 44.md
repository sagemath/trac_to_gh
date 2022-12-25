# Issue 44: customize preparsing

archive/issues_000044.json:
```json
{
    "body": "Assignee: somebody\n\n> I made the suggested changes and everything works fine.\n>\n> Thank you for replying so quickly.\n>\n> I think that modifying the preparser to meet different needs\n> sounds like a good idea as long as the underlying code didn't\n> have to change.\n\nWAIT ! -- good point.  In fact, there is code in the SAGE library\nthat assumes that the preparser replaces ^'s by **'s.  If you\ndo exactly what I suggested, you could get subtle bugs in certain\nplaces involved in moving expressions between GAP/Singular and SAGE\nthat use the SAGE preparser.\nSo at least don't make those changes to preparse.py.\n\nIt's fine to make the changes to integer.pyx that defines __xor__,\nand certainly you'll find that useful.  \n\nFor now, the best thing for you to do might be to start SAGE with\n\n    sage -ipython \n\nto get SAGE with no preparsing at all. \n\nThe solution to all this is probably to make the interactive preparser \ncustomizable and make those customizations only apply to the\ninteractive preparser.  (I.e., the preparser will have a context as input,\none for the interactive session, and the other used internally by\nthe library).  One could also have a context set at the top of a .sage\nfile.  \n\nSorry for the confusion.  \n\nwilliam\n\nIssue created by migration from https://trac.sagemath.org/ticket/44\n\n",
    "created_at": "2006-09-12T23:55:32Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "customize preparsing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/44",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

> I made the suggested changes and everything works fine.
>
> Thank you for replying so quickly.
>
> I think that modifying the preparser to meet different needs
> sounds like a good idea as long as the underlying code didn't
> have to change.

WAIT ! -- good point.  In fact, there is code in the SAGE library
that assumes that the preparser replaces ^'s by **'s.  If you
do exactly what I suggested, you could get subtle bugs in certain
places involved in moving expressions between GAP/Singular and SAGE
that use the SAGE preparser.
So at least don't make those changes to preparse.py.

It's fine to make the changes to integer.pyx that defines __xor__,
and certainly you'll find that useful.  

For now, the best thing for you to do might be to start SAGE with

    sage -ipython 

to get SAGE with no preparsing at all. 

The solution to all this is probably to make the interactive preparser 
customizable and make those customizations only apply to the
interactive preparser.  (I.e., the preparser will have a context as input,
one for the interactive session, and the other used internally by
the library).  One could also have a context set at the top of a .sage
file.  

Sorry for the confusion.  

william

Issue created by migration from https://trac.sagemath.org/ticket/44





---

archive/issue_events_000043.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-05-14T22:23:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/44",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/44#event-43"
}
```



---

archive/issue_comments_000266.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-05-14T22:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/44",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/44#issuecomment-266",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_000267.json:
```json
{
    "body": "We discussed this a lot in sage-devel.  Having a user-customizable preparser is something that has happened a little -- e.g., Bradshaw added support for implicit multiplication preparsing.  But it doesn't make any sense for \"this\" to be a trac ticket.  It is general, vague, done, and can never be finished, all at once.",
    "created_at": "2008-05-14T22:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/44",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/44#issuecomment-267",
    "user": "https://github.com/williamstein"
}
```

We discussed this a lot in sage-devel.  Having a user-customizable preparser is something that has happened a little -- e.g., Bradshaw added support for implicit multiplication preparsing.  But it doesn't make any sense for "this" to be a trac ticket.  It is general, vague, done, and can never be finished, all at once.
