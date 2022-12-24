# Issue 220: SageX: generic power series over arbitrary ring

archive/issues_000220.json:
```json
{
    "body": "Assignee: somebody\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/220\n\n",
    "created_at": "2007-01-25T19:01:19Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.4.2",
    "title": "SageX: generic power series over arbitrary ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/220",
    "user": "was"
}
```
Assignee: somebody



Issue created by migration from https://trac.sagemath.org/ticket/220





---

archive/issue_comments_000985.json:
```json
{
    "body": "Steps to get this done:\n1. Read through the current python code and add doctests for every single function.\n2. Move the abstract base class into a SageX file.\n3. Get to compile.\n4. Make the changes needed so it works correctly, e.g., Py_ssize_t's, etc. \n \nLater on -- make some specialized classes...",
    "created_at": "2007-01-25T21:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/220#issuecomment-985",
    "user": "was"
}
```

Steps to get this done:
1. Read through the current python code and add doctests for every single function.
2. Move the abstract base class into a SageX file.
3. Get to compile.
4. Make the changes needed so it works correctly, e.g., Py_ssize_t's, etc. 
 
Later on -- make some specialized classes...



---

archive/issue_comments_000986.json:
```json
{
    "body": "Are 2-4 done?",
    "created_at": "2007-10-29T17:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/220#issuecomment-986",
    "user": "robertwb"
}
```

Are 2-4 done?



---

archive/issue_comments_000987.json:
```json
{
    "body": "I think this has already been done as evidenced by sage/rings/power_series*.pyx.  This was done around Sage 2.4.2 -- changeset 4159.",
    "created_at": "2008-11-14T08:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/220#issuecomment-987",
    "user": "mhansen"
}
```

I think this has already been done as evidenced by sage/rings/power_series*.pyx.  This was done around Sage 2.4.2 -- changeset 4159.



---

archive/issue_comments_000988.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T08:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/220#issuecomment-988",
    "user": "mhansen"
}
```

Resolution: fixed
