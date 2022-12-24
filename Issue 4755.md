# Issue 4755: CremonaDatabase().number_of_curves() should work when the optional database isn't installed.

archive/issues_004755.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nsage: CremonaDatabase().number_of_curves()\n---------------------------------------------------------------------------\nKeyError                                  Traceback (most recent call last)\n\n/home/mike/.sage/temp/mike_laptop/12400/_home_mike__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/opt/sage/local/lib/python2.5/site-packages/sage/databases/cremona.pyc in number_of_curves(self, N, i)\n    680         \"\"\"\n    681         if N == 0:\n--> 682             return self['number_of_curves']\n    683         C = self.allcurves(N)\n    684         if i == 0:\n\n/opt/sage/local/lib/python2.5/site-packages/sage/databases/cremona.pyc in __getitem__(self, N)\n    345         if isinstance(N, str) and len(N) > 0:\n    346             if N[0].isalpha():\n--> 347                 return sage.databases.db.Database.__getitem__(self, N)\n    348             else:\n    349                 return self.elliptic_curve(N)\n\n/opt/sage/local/lib/python2.5/site-packages/sage/databases/db.pyc in __getitem__(self, x)\n    258         try:\n    259             if not isinstance(x, slice):\n--> 260                 return self.root[x]\n    261             return [self[k] for k in range(x.start, x.stop, x.step)]\n    262         except AttributeError:\n\nKeyError: 'number_of_curves'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4755\n\n",
    "created_at": "2008-12-11T04:27:42Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "CremonaDatabase().number_of_curves() should work when the optional database isn't installed.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4755",
    "user": "@mwhansen"
}
```
Assignee: cwitty


```
sage: CremonaDatabase().number_of_curves()
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/mike/.sage/temp/mike_laptop/12400/_home_mike__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/opt/sage/local/lib/python2.5/site-packages/sage/databases/cremona.pyc in number_of_curves(self, N, i)
    680         """
    681         if N == 0:
--> 682             return self['number_of_curves']
    683         C = self.allcurves(N)
    684         if i == 0:

/opt/sage/local/lib/python2.5/site-packages/sage/databases/cremona.pyc in __getitem__(self, N)
    345         if isinstance(N, str) and len(N) > 0:
    346             if N[0].isalpha():
--> 347                 return sage.databases.db.Database.__getitem__(self, N)
    348             else:
    349                 return self.elliptic_curve(N)

/opt/sage/local/lib/python2.5/site-packages/sage/databases/db.pyc in __getitem__(self, x)
    258         try:
    259             if not isinstance(x, slice):
--> 260                 return self.root[x]
    261             return [self[k] for k in range(x.start, x.stop, x.step)]
    262         except AttributeError:

KeyError: 'number_of_curves'
```


Issue created by migration from https://trac.sagemath.org/ticket/4755





---

archive/issue_comments_036011.json:
```json
{
    "body": "Same issue with number_of_isogeny_classes().",
    "created_at": "2009-01-23T08:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4755#issuecomment-36011",
    "user": "@aghitza"
}
```

Same issue with number_of_isogeny_classes().



---

archive/issue_comments_036012.json:
```json
{
    "body": "The attached patch fixes the two issues, as well as a number of smaller issues that I noticed while looking through cremona.py.",
    "created_at": "2009-01-23T09:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4755#issuecomment-36012",
    "user": "@aghitza"
}
```

The attached patch fixes the two issues, as well as a number of smaller issues that I noticed while looking through cremona.py.



---

archive/issue_comments_036013.json:
```json
{
    "body": "Attachment [trac_4755.patch](tarball://root/attachments/some-uuid/ticket4755/trac_4755.patch) by @robertwb created at 2009-01-23 22:46:05\n\nLooks and works good for me. Lots of other documentation and other typo fixes too.",
    "created_at": "2009-01-23T22:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4755#issuecomment-36013",
    "user": "@robertwb"
}
```

Attachment [trac_4755.patch](tarball://root/attachments/some-uuid/ticket4755/trac_4755.patch) by @robertwb created at 2009-01-23 22:46:05

Looks and works good for me. Lots of other documentation and other typo fixes too.



---

archive/issue_comments_036014.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T19:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4755#issuecomment-36014",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael



---

archive/issue_comments_036015.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T19:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4755#issuecomment-36015",
    "user": "mabshoff"
}
```

Resolution: fixed
