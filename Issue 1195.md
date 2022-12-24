# Issue 1195: The "len" function for lists and sequences

archive/issues_001195.json:
```json
{
    "body": "Assignee: cwitty\n\nCurrently, the method to obtain the length of a list or sequence is:\n\n{{my_list=Sequence([1,2,3,4])\nlen(my_list)}}\n\nThis is not consistent with either MAGMA or PARI, and there is no method attached to the sequence or list which gives the length.\n\nI would like to suggest that a method be added so that\n\n{{my_list.length()}}\n\nwould give the answer ``4''.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1195\n\n",
    "created_at": "2007-11-17T23:01:18Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "The \"len\" function for lists and sequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1195",
    "user": "ljpk"
}
```
Assignee: cwitty

Currently, the method to obtain the length of a list or sequence is:

{{my_list=Sequence([1,2,3,4])
len(my_list)}}

This is not consistent with either MAGMA or PARI, and there is no method attached to the sequence or list which gives the length.

I would like to suggest that a method be added so that

{{my_list.length()}}

would give the answer ``4''.

Issue created by migration from https://trac.sagemath.org/ticket/1195





---

archive/issue_comments_007415.json:
```json
{
    "body": "On the other hand, len() is the standard Python way of doing things.",
    "created_at": "2007-11-18T05:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1195#issuecomment-7415",
    "user": "@mwhansen"
}
```

On the other hand, len() is the standard Python way of doing things.



---

archive/issue_comments_007416.json:
```json
{
    "body": "This is not quite true -- there is a `.__len__()` function that `len()` calls.\n\nPerhaps this should be at the level of `SageObject`: `.length()` calls `.__len__()?`  This is irritating but not idiomatic python, so I vote to keep it as is.",
    "created_at": "2007-11-24T21:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1195#issuecomment-7416",
    "user": "@ncalexan"
}
```

This is not quite true -- there is a `.__len__()` function that `len()` calls.

Perhaps this should be at the level of `SageObject`: `.length()` calls `.__len__()?`  This is irritating but not idiomatic python, so I vote to keep it as is.



---

archive/issue_comments_007417.json:
```json
{
    "body": "I vote against the proposal in this ticket, `len(Foo)` is the Python way.",
    "created_at": "2008-02-27T00:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1195#issuecomment-7417",
    "user": "@malb"
}
```

I vote against the proposal in this ticket, `len(Foo)` is the Python way.



---

archive/issue_comments_007418.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-02-27T12:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1195#issuecomment-7418",
    "user": "@williamstein"
}
```

Resolution: wontfix



---

archive/issue_comments_007419.json:
```json
{
    "body": "> Perhaps this should be at the level of SageObject: .length() calls .__len__()? \n> This is irritating but not idiomatic python, so I vote to keep it as is.\n\nI think this would be annoying.  It also adds to the clutter when one does X.[tab]\non a sage object X.  And everybody learns about len(...) in Python pretty soon.",
    "created_at": "2008-02-27T12:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1195#issuecomment-7419",
    "user": "@williamstein"
}
```

> Perhaps this should be at the level of SageObject: .length() calls .__len__()? 
> This is irritating but not idiomatic python, so I vote to keep it as is.

I think this would be annoying.  It also adds to the clutter when one does X.[tab]
on a sage object X.  And everybody learns about len(...) in Python pretty soon.
