# Issue 5059: [with patch, needs review] Fix a bunch of broken pickles

archive/issues_005059.json:
```json
{
    "body": "Assignee: @craigcitro\n\nAt a workshop in Seattle last June, a **massive** number of spaces of modular symbols were computed. However, the pickles were broken in shortly thereafter by a refactoring of some code in Sage. \n\nThe attached patch fixes this -- now the old pickles can be loaded, and new pickles still work fine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5059\n\n",
    "created_at": "2009-01-22T23:57:16Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] Fix a bunch of broken pickles",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5059",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

At a workshop in Seattle last June, a **massive** number of spaces of modular symbols were computed. However, the pickles were broken in shortly thereafter by a refactoring of some code in Sage. 

The attached patch fixes this -- now the old pickles can be loaded, and new pickles still work fine.

Issue created by migration from https://trac.sagemath.org/ticket/5059





---

archive/issue_comments_038533.json:
```json
{
    "body": "Attachment [trac-5059.patch](tarball://root/attachments/some-uuid/ticket5059/trac-5059.patch) by @craigcitro created at 2009-01-22 23:58:41",
    "created_at": "2009-01-22T23:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38533",
    "user": "@craigcitro"
}
```

Attachment [trac-5059.patch](tarball://root/attachments/some-uuid/ticket5059/trac-5059.patch) by @craigcitro created at 2009-01-22 23:58:41



---

archive/issue_comments_038534.json:
```json
{
    "body": "Are there some example broken pickles that this fixes?",
    "created_at": "2009-01-23T02:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38534",
    "user": "@robertwb"
}
```

Are there some example broken pickles that this fixes?



---

archive/issue_comments_038535.json:
```json
{
    "body": "Some examples: http://sage.math.washington.edu/home/wstein/db/modsym/data/\n\nLooks good and works great.",
    "created_at": "2009-01-23T04:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38535",
    "user": "@robertwb"
}
```

Some examples: http://sage.math.washington.edu/home/wstein/db/modsym/data/

Looks good and works great.



---

archive/issue_comments_038536.json:
```json
{
    "body": "Unfortunately this patch breaks two doctests:\n\n```\n        sage -t -long devel/sage/sage/modular/congroup.py # 5 doctests failed\n        sage -t -long devel/sage/sage/modular/congroup_element.py # 1 doctests failed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T09:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38536",
    "user": "mabshoff"
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

archive/issue_comments_038537.json:
```json
{
    "body": "Attachment [trac-5059-2.patch](tarball://root/attachments/some-uuid/ticket5059/trac-5059-2.patch) by @robertwb created at 2009-01-23 09:22:55\n\nThat seems to have addressed those doctest failures.",
    "created_at": "2009-01-23T09:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38537",
    "user": "@robertwb"
}
```

Attachment [trac-5059-2.patch](tarball://root/attachments/some-uuid/ticket5059/trac-5059-2.patch) by @robertwb created at 2009-01-23 09:22:55

That seems to have addressed those doctest failures.



---

archive/issue_comments_038538.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38538",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0

Cheers,

Michael



---

archive/issue_comments_038539.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5059#issuecomment-38539",
    "user": "mabshoff"
}
```

Resolution: fixed
