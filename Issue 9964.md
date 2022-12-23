# Issue 9964: Make SYMPOW not write to files under global Sage installations

archive/issues_009964.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  cschwan fbissey lftabera\n\nSYMPOW-related doctests can in\n\n```\nsage/lfunctions/sympow.py\nsage/modular/abvar/abvar.py\nsage/modular/hecke/submodule.py\nsage/schemes/elliptic_curves/ell_rational_field.py\n```\n\ncan fail if users who do not have write access under `SAGE_ROOT` runs these tests before a user who does have this access.\n\nSee [comment:ticket:9703:8 comments 8 and 9] at #9703 for background and a suggested solution.\n\nThis is the likely cause of the non-qepcad failures [reported by Luis Felipe Tabera on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a56d4fbaad2dcce3).\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9965\n\n",
    "created_at": "2010-09-21T22:23:39Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Make SYMPOW not write to files under global Sage installations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9964",
    "user": "mpatel"
}
```
Assignee: GeorgSWeber

CC:  cschwan fbissey lftabera

SYMPOW-related doctests can in

```
sage/lfunctions/sympow.py
sage/modular/abvar/abvar.py
sage/modular/hecke/submodule.py
sage/schemes/elliptic_curves/ell_rational_field.py
```

can fail if users who do not have write access under `SAGE_ROOT` runs these tests before a user who does have this access.

See [comment:ticket:9703:8 comments 8 and 9] at #9703 for background and a suggested solution.

This is the likely cause of the non-qepcad failures [reported by Luis Felipe Tabera on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a56d4fbaad2dcce3).



Issue created by migration from https://trac.sagemath.org/ticket/9965





---

archive/issue_comments_099810.json:
```json
{
    "body": "This is fixed by #11920.",
    "created_at": "2012-09-27T08:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9964#issuecomment-99810",
    "user": "jdemeyer"
}
```

This is fixed by #11920.



---

archive/issue_comments_099811.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-09-27T08:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9964#issuecomment-99811",
    "user": "jdemeyer"
}
```

Resolution: duplicate
