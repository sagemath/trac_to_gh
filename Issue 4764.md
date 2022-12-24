# Issue 4764: Error in computing compliment of modular symbol space

archive/issues_004764.json:
```json
{
    "body": "Assignee: @craigcitro\n\n\n```\nsage: f = EllipticCurve('128a').modular_symbol_space()\nsage: f.complement()\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/Users/robert/.sage/sage_notebook/worksheets/admin/110/code/7.py\", line 7, in <module>\n    f.complement()\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py\", line 202, in complement\n    raise RuntimeError, \"Computation of complementary space failed (cut down to rank %s, but should have cut down to rank %s).\"%(V.rank(), self.rank())\nRuntimeError: Computation of complementary space failed (cut down to rank 18, but should have cut down to rank 1).\n```\n\n\nNote that the error is wrong, as \n\n\n```\nsage: ModularSymbols(128, sign=1)\n          \t\n\nModular Symbols space of dimension 18 for Gamma_0(128) of weight 2 with sign 1 over Rational Field\n```\n\n\nhowever, it should have cut the rank down to 17.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4764\n\n",
    "created_at": "2008-12-12T01:50:28Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Error in computing compliment of modular symbol space",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4764",
    "user": "@robertwb"
}
```
Assignee: @craigcitro


```
sage: f = EllipticCurve('128a').modular_symbol_space()
sage: f.complement()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/robert/.sage/sage_notebook/worksheets/admin/110/code/7.py", line 7, in <module>
    f.complement()
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 202, in complement
    raise RuntimeError, "Computation of complementary space failed (cut down to rank %s, but should have cut down to rank %s)."%(V.rank(), self.rank())
RuntimeError: Computation of complementary space failed (cut down to rank 18, but should have cut down to rank 1).
```


Note that the error is wrong, as 


```
sage: ModularSymbols(128, sign=1)
          	

Modular Symbols space of dimension 18 for Gamma_0(128) of weight 2 with sign 1 over Rational Field
```


however, it should have cut the rank down to 17.

Issue created by migration from https://trac.sagemath.org/ticket/4764





---

archive/issue_comments_036107.json:
```json
{
    "body": "This seems to be the same error as #1127 ...\n\nI'm curious whether my (still unfinished) patch from #2535 might help. I don't know that I ever checked ...",
    "created_at": "2008-12-12T02:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4764#issuecomment-36107",
    "user": "@craigcitro"
}
```

This seems to be the same error as #1127 ...

I'm curious whether my (still unfinished) patch from #2535 might help. I don't know that I ever checked ...



---

archive/issue_comments_036108.json:
```json
{
    "body": "You're right, it is exactly #1127. I searched before making a ticket, but I guess I didn't go far enough back in time. Hopefully you've already fixed it :). \n\nI'm closing this as a dupe.",
    "created_at": "2008-12-12T02:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4764#issuecomment-36108",
    "user": "@robertwb"
}
```

You're right, it is exactly #1127. I searched before making a ticket, but I guess I didn't go far enough back in time. Hopefully you've already fixed it :). 

I'm closing this as a dupe.



---

archive/issue_comments_036109.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-12-12T02:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4764#issuecomment-36109",
    "user": "@robertwb"
}
```

Resolution: duplicate
