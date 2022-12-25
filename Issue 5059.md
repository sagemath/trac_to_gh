# Issue 5059: [with patch, needs review] Fix a bunch of broken pickles

archive/issues_005059.json:
```json
{
    "body": "Assignee: @craigcitro\n\nAt a workshop in Seattle last June, a **massive** number of spaces of modular symbols were computed. However, the pickles were broken in shortly thereafter by a refactoring of some code in Sage. \n\nThe attached patch fixes this -- now the old pickles can be loaded, and new pickles still work fine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5059\n\n",
    "created_at": "2009-01-22T23:57:16Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] Fix a bunch of broken pickles",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5059",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

At a workshop in Seattle last June, a **massive** number of spaces of modular symbols were computed. However, the pickles were broken in shortly thereafter by a refactoring of some code in Sage. 

The attached patch fixes this -- now the old pickles can be loaded, and new pickles still work fine.

Issue created by migration from https://trac.sagemath.org/ticket/5059





---

archive/issue_comments_038460.json:
```json
{
    "body": "Attachment [trac-5059.patch](tarball://root/attachments/some-uuid/ticket5059/trac-5059.patch) by @craigcitro created at 2009-01-22 23:58:41",
    "created_at": "2009-01-22T23:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38460",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-5059.patch](tarball://root/attachments/some-uuid/ticket5059/trac-5059.patch) by @craigcitro created at 2009-01-22 23:58:41



---

archive/issue_comments_038461.json:
```json
{
    "body": "Are there some example broken pickles that this fixes?",
    "created_at": "2009-01-23T02:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38461",
    "user": "https://github.com/robertwb"
}
```

Are there some example broken pickles that this fixes?



---

archive/issue_comments_038462.json:
```json
{
    "body": "Some examples: http://sage.math.washington.edu/home/wstein/db/modsym/data/\n\nLooks good and works great.",
    "created_at": "2009-01-23T04:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38462",
    "user": "https://github.com/robertwb"
}
```

Some examples: http://sage.math.washington.edu/home/wstein/db/modsym/data/

Looks good and works great.



---

archive/issue_comments_038463.json:
```json
{
    "body": "Unfortunately this patch breaks two doctests:\n\n```\n        sage -t -long devel/sage/sage/modular/congroup.py # 5 doctests failed\n        sage -t -long devel/sage/sage/modular/congroup_element.py # 1 doctests failed\n```\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T09:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38463",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Unfortunately this patch breaks two doctests:

```
        sage -t -long devel/sage/sage/modular/congroup.py # 5 doctests failed
        sage -t -long devel/sage/sage/modular/congroup_element.py # 1 doctests failed
```

Cheers,

Michael



---

archive/issue_comments_038464.json:
```json
{
    "body": "Attachment [trac-5059-2.patch](tarball://root/attachments/some-uuid/ticket5059/trac-5059-2.patch) by @robertwb created at 2009-01-23 09:22:55\n\nThat seems to have addressed those doctest failures.",
    "created_at": "2009-01-23T09:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38464",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac-5059-2.patch](tarball://root/attachments/some-uuid/ticket5059/trac-5059-2.patch) by @robertwb created at 2009-01-23 09:22:55

That seems to have addressed those doctest failures.



---

archive/issue_comments_038465.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0

Cheers,

Michael



---

archive/issue_events_011660.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T10:02:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5059#event-11660"
}
```



---

archive/issue_comments_038466.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
