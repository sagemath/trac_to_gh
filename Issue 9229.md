# Issue 9229: Bring doctests for databases/cremona.py up to 100% (from  42% (17 of 40) )

archive/issues_009229.json:
```json
{
    "body": "Assignee: cremona\n\n\n```\n\ndevel/sage-main/sage/databases/cremona.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE devel/sage-main/sage/databases/cremona.py: 42% (17 of 40)\n\nMissing documentation:\n* _init(self, ftpdata):\n* __repr__(self):\n* CremonaDatabase():\n\n\nMissing doctests:\n* rebuild(data_tgz, largest_conductor, decompress=True):\n* __init__(self, read_only=True):\n* __iter__(self):\n* __getitem__(self, N):\n* __repr__(self):\n* allbsd(self, N):\n* allcurves(self, N):\n* allgens(self, N):\n* degphi(self, N):\n* elliptic_curve_from_ainvs(self, N, ainvs):\n* elliptic_curve(self, label):\n* iter(self, conductors):\n* isogeny_classes(self, conductor):\n* isogeny_class(self, label):\n* list(self, conductors):\n* _init_allcurves(self, ftpdata, largest_conductor=0):\n* _init_degphi(self, ftpdata, largest_conductor=0):\n* _init_allbsd(self, ftpdata, largest_conductor=0):\n* _init_allgens(self, ftpdata, largest_conductor=0):\n* __init__(self, read_only=True):\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9229\n\n",
    "created_at": "2010-06-12T13:43:32Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Bring doctests for databases/cremona.py up to 100% (from  42% (17 of 40) )",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9229",
    "user": "cremona"
}
```
Assignee: cremona


```

devel/sage-main/sage/databases/cremona.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-main/sage/databases/cremona.py: 42% (17 of 40)

Missing documentation:
* _init(self, ftpdata):
* __repr__(self):
* CremonaDatabase():


Missing doctests:
* rebuild(data_tgz, largest_conductor, decompress=True):
* __init__(self, read_only=True):
* __iter__(self):
* __getitem__(self, N):
* __repr__(self):
* allbsd(self, N):
* allcurves(self, N):
* allgens(self, N):
* degphi(self, N):
* elliptic_curve_from_ainvs(self, N, ainvs):
* elliptic_curve(self, label):
* iter(self, conductors):
* isogeny_classes(self, conductor):
* isogeny_class(self, label):
* list(self, conductors):
* _init_allcurves(self, ftpdata, largest_conductor=0):
* _init_degphi(self, ftpdata, largest_conductor=0):
* _init_allbsd(self, ftpdata, largest_conductor=0):
* _init_allgens(self, ftpdata, largest_conductor=0):
* __init__(self, read_only=True):
```



Issue created by migration from https://trac.sagemath.org/ticket/9229





---

archive/issue_comments_086615.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-06-12T18:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9229#issuecomment-86615",
    "user": "cremona"
}
```

Changing priority from major to minor.



---

archive/issue_comments_086616.json:
```json
{
    "body": "This is a duplicate of #9223 and should be deleted.",
    "created_at": "2010-06-12T18:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9229#issuecomment-86616",
    "user": "cremona"
}
```

This is a duplicate of #9223 and should be deleted.



---

archive/issue_comments_086617.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-06-12T21:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9229#issuecomment-86617",
    "user": "drkirkby"
}
```

Resolution: duplicate
