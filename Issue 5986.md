# Issue 5986: [with patch, needs review] Workaround mishandled nested classes in Python and cPickle

archive/issues_005986.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat cwitty\n\nKeywords: pickling, nested classes\n\nWith the python code below::\n    class A:\n        class B:\n            pass\nPython 2.6 erroneously set the B.__name__ to \"B\" instead of \"A.B\".\n\nFurthermore, upon pickling (here in save_global)\n*and* unpickling (in load_global) a class\nwith name \"A.B\" in a module mod, the standard\ncPickle module searches for \"A.B\" in mod.__dict__\ninstead of looking up \"A\" and then \"B\" in the result.\n\nThis patch works around this by a patch to cPickle.c which fixes the\nname for B to its appropriate value A.B, and inserts 'A.B' = A.B in\nmod.__dict__ (hacky, but seems to work) the first time A.B is pickled,\nand fixes load_global to implement a proper lookup upon unpickling.\n\nIt also ensures that sage/interfaces/sage0.py uses loads/dumps from\nsage_object rather than calling directly cPickle.loads/dumps\n(+1 by cwitty on this change)\n\nDepends on #5483 and #5985\n\nIssue created by migration from https://trac.sagemath.org/ticket/5986\n\n",
    "created_at": "2009-05-05T07:14:13Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, needs review] Workaround mishandled nested classes in Python and cPickle",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5986",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat cwitty

Keywords: pickling, nested classes

With the python code below::
    class A:
        class B:
            pass
Python 2.6 erroneously set the B.__name__ to "B" instead of "A.B".

Furthermore, upon pickling (here in save_global)
*and* unpickling (in load_global) a class
with name "A.B" in a module mod, the standard
cPickle module searches for "A.B" in mod.__dict__
instead of looking up "A" and then "B" in the result.

This patch works around this by a patch to cPickle.c which fixes the
name for B to its appropriate value A.B, and inserts 'A.B' = A.B in
mod.__dict__ (hacky, but seems to work) the first time A.B is pickled,
and fixes load_global to implement a proper lookup upon unpickling.

It also ensures that sage/interfaces/sage0.py uses loads/dumps from
sage_object rather than calling directly cPickle.loads/dumps
(+1 by cwitty on this change)

Depends on #5483 and #5985

Issue created by migration from https://trac.sagemath.org/ticket/5986





---

archive/issue_comments_047569.json:
```json
{
    "body": "Attachment [cPickle-5986-nested-classes-submitted.patch](tarball://root/attachments/some-uuid/ticket5986/cPickle-5986-nested-classes-submitted.patch) by nthiery created at 2009-05-06 06:56:46",
    "created_at": "2009-05-06T06:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47569",
    "user": "nthiery"
}
```

Attachment [cPickle-5986-nested-classes-submitted.patch](tarball://root/attachments/some-uuid/ticket5986/cPickle-5986-nested-classes-submitted.patch) by nthiery created at 2009-05-06 06:56:46



---

archive/issue_comments_047570.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-18T03:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47570",
    "user": "nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047571.json:
```json
{
    "body": "This workaround it a bit to hackish for my taste, but it's been implemented and tested. Followup at #6121.",
    "created_at": "2009-05-22T23:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47571",
    "user": "robertwb"
}
```

This workaround it a bit to hackish for my taste, but it's been implemented and tested. Followup at #6121.



---

archive/issue_comments_047572.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> This workaround it a bit to hackish for my taste, but it's been implemented and tested. Followup at #6121. \n\nDoes that mean that this ticket can be closed?",
    "created_at": "2009-09-22T17:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47572",
    "user": "jason"
}
```

Replying to [comment:4 robertwb]:
> This workaround it a bit to hackish for my taste, but it's been implemented and tested. Followup at #6121. 

Does that mean that this ticket can be closed?



---

archive/issue_comments_047573.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> Replying to [comment:4 robertwb]:\n> > This workaround it a bit to hackish for my taste, but it's been implemented and tested. Followup at #6121. \n> \n> Does that mean that this ticket can be closed?\n\nNot before Robert or someone else writes a proof of concept patch upon the category code proving that #6121 is a usable replacement for this one to get pickling to work for parents and categories.\nSee discussion on Sage devel.",
    "created_at": "2009-09-22T20:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47573",
    "user": "nthiery"
}
```

Replying to [comment:5 jason]:
> Replying to [comment:4 robertwb]:
> > This workaround it a bit to hackish for my taste, but it's been implemented and tested. Followup at #6121. 
> 
> Does that mean that this ticket can be closed?

Not before Robert or someone else writes a proof of concept patch upon the category code proving that #6121 is a usable replacement for this one to get pickling to work for parents and categories.
See discussion on Sage devel.



---

archive/issue_comments_047574.json:
```json
{
    "body": "Attachment [trac_5986-use-nested_class_metaclass.patch](tarball://root/attachments/some-uuid/ticket5986/trac_5986-use-nested_class_metaclass.patch) by nthiery created at 2009-10-11 08:47:16\n\nApply only this one",
    "created_at": "2009-10-11T08:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47574",
    "user": "nthiery"
}
```

Attachment [trac_5986-use-nested_class_metaclass.patch](tarball://root/attachments/some-uuid/ticket5986/trac_5986-use-nested_class_metaclass.patch) by nthiery created at 2009-10-11 08:47:16

Apply only this one



---

archive/issue_comments_047575.json:
```json
{
    "body": "The newly attached patch implements a completely different fix, using #6110 and #6121.\n\nWilliam is ok integrating this in 4.1.2 if it's ready on time (see IRC).\n\nRobert: please review! (unless you feel you should be an author, and get someone else to review it :-))",
    "created_at": "2009-10-11T08:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47575",
    "user": "nthiery"
}
```

The newly attached patch implements a completely different fix, using #6110 and #6121.

William is ok integrating this in 4.1.2 if it's ready on time (see IRC).

Robert: please review! (unless you feel you should be an author, and get someone else to review it :-))



---

archive/issue_comments_047576.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-11T08:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47576",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047577.json:
```json
{
    "body": "Much less intrusive--too bad we didn't pursue this just a bit more back in June.",
    "created_at": "2009-10-11T08:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47577",
    "user": "robertwb"
}
```

Much less intrusive--too bad we didn't pursue this just a bit more back in June.



---

archive/issue_comments_047578.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T07:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5986#issuecomment-47578",
    "user": "mhansen"
}
```

Resolution: fixed
