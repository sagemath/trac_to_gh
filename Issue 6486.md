# Issue 6486: minimum distance of all 0 code raised mysterious error message

archive/issues_006486.json:
```json
{
    "body": "Assignee: @rlmill\n\nThis should return a more useful error message:\n\n\n```\nsage: G = matrix(GF(2),[[0,0,0]])\nsage: C = LinearCode(G)\nsage: C.list()\n[(0, 0, 0)]\nsage: C.minimum_distance()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/home/wdj/.sage/temp/tinah/7902/_home_wdj__sage_init_sage_0.py in <module>()\n\n/home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/coding/linear_code.pyc in minimum_distance(self, method)\n   1681             return ZZ(d)\n   1682         Gstr = \"%s*Z(%s)^0\"%(gapG, q)\n-> 1683         return hamming_weight(min_wt_vec_gap(Gstr,n,k,F))\n   1684\n   1685     def module_composition_factors(self,gp):\n\n/home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/coding/linear_code.pyc in min_wt_vec_gap(Gmat, n, k, F, method)\n    379         #print [gap.eval(\"v[\"+str(i+1)+\"]\") for i in range(n)]\n    380         all.append([v._matrix_(F),m._matrix_(F),int(dist)])\n--> 381     ans = all[0]\n    382     for x in all:\n    383         if x[2]<ans[2] and x[2]>0:\n\nIndexError: list index out of range\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6486\n\n",
    "created_at": "2009-07-08T18:40:40Z",
    "labels": [
        "coding theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "minimum distance of all 0 code raised mysterious error message",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6486",
    "user": "@wdjoyner"
}
```
Assignee: @rlmill

This should return a more useful error message:


```
sage: G = matrix(GF(2),[[0,0,0]])
sage: C = LinearCode(G)
sage: C.list()
[(0, 0, 0)]
sage: C.minimum_distance()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/wdj/.sage/temp/tinah/7902/_home_wdj__sage_init_sage_0.py in <module>()

/home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/coding/linear_code.pyc in minimum_distance(self, method)
   1681             return ZZ(d)
   1682         Gstr = "%s*Z(%s)^0"%(gapG, q)
-> 1683         return hamming_weight(min_wt_vec_gap(Gstr,n,k,F))
   1684
   1685     def module_composition_factors(self,gp):

/home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/coding/linear_code.pyc in min_wt_vec_gap(Gmat, n, k, F, method)
    379         #print [gap.eval("v["+str(i+1)+"]") for i in range(n)]
    380         all.append([v._matrix_(F),m._matrix_(F),int(dist)])
--> 381     ans = all[0]
    382     for x in all:
    383         if x[2]<ans[2] and x[2]>0:

IndexError: list index out of range
```


Issue created by migration from https://trac.sagemath.org/ticket/6486





---

archive/issue_comments_052455.json:
```json
{
    "body": "Attachment [trac6486.patch](tarball://root/attachments/some-uuid/ticket6486/trac6486.patch) by spancratz created at 2010-01-19 23:46:38\n\nAdds some documentation and handles the min distance problem",
    "created_at": "2010-01-19T23:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6486#issuecomment-52455",
    "user": "spancratz"
}
```

Attachment [trac6486.patch](tarball://root/attachments/some-uuid/ticket6486/trac6486.patch) by spancratz created at 2010-01-19 23:46:38

Adds some documentation and handles the min distance problem



---

archive/issue_comments_052456.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T23:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6486#issuecomment-52456",
    "user": "spancratz"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_052457.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T22:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6486#issuecomment-52457",
    "user": "@craigcitro"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_052458.json:
```json
{
    "body": "This looks good. **Tons** of nice cleanup, and it's clearly the right fix for the bug on the ticket.",
    "created_at": "2010-01-20T22:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6486#issuecomment-52458",
    "user": "@craigcitro"
}
```

This looks good. **Tons** of nice cleanup, and it's clearly the right fix for the bug on the ticket.



---

archive/issue_comments_052459.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T06:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6486#issuecomment-52459",
    "user": "mvngu"
}
```

Resolution: fixed
