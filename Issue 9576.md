# Issue 9576: Allow the operator & for submodule intersections.

archive/issues_009576.json:
```json
{
    "body": "Assignee: jason, was\n\nKeywords: operator & for submodule intersection\n\nThere is already the operatror & for Sets intersections : S1 & S2.\n\nThere is also the operator + for submodules sum : F+G.\n\nI propose to expand the operator & over submodules and subspaces,\nand add theses lines in free_modules.py\n\n\n```\n## allow the \"intersection\" operator & for submodules.\n \n     def __and__ (self, other) : return self.intersection (other)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9576\n\n",
    "created_at": "2010-07-22T07:45:59Z",
    "labels": [
        "linear algebra",
        "trivial",
        "enhancement"
    ],
    "title": "Allow the operator & for submodule intersections.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9576",
    "user": "fmaltey"
}
```
Assignee: jason, was

Keywords: operator & for submodule intersection

There is already the operatror & for Sets intersections : S1 & S2.

There is also the operator + for submodules sum : F+G.

I propose to expand the operator & over submodules and subspaces,
and add theses lines in free_modules.py


```
## allow the "intersection" operator & for submodules.
 
     def __and__ (self, other) : return self.intersection (other)
```


Issue created by migration from https://trac.sagemath.org/ticket/9576





---

archive/issue_comments_092480.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-10-16T07:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9576#issuecomment-92480",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_092481.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-10-16T07:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9576#issuecomment-92481",
    "user": "pmenegat"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092482.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-10-16T07:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9576#issuecomment-92482",
    "user": "sbrandhorst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092483.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-10-22T17:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9576#issuecomment-92483",
    "user": "vbraun"
}
```

Resolution: fixed
