# Issue 4744: [with patch, needs review] congruence number for elliptic curves

archive/issues_004744.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  was\n\n\n```\n            sage: E = EllipticCurve('37a')\n            sage: E.congruence_number()\n            2\n            sage: E = EllipticCurve('54b')\n            sage: E.congruence_number()\n            6\n            sage: E.modular_degree()\n            2\n            sage: E = EllipticCurve('242a1')\n            sage: E.modular_degree()\n            16\n            sage: E.congruence_number()  # long time\n            176\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4744\n\n",
    "created_at": "2008-12-08T22:44:35Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] congruence number for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4744",
    "user": "robertwb"
}
```
Assignee: tbd

CC:  was


```
            sage: E = EllipticCurve('37a')
            sage: E.congruence_number()
            2
            sage: E = EllipticCurve('54b')
            sage: E.congruence_number()
            6
            sage: E.modular_degree()
            2
            sage: E = EllipticCurve('242a1')
            sage: E.modular_degree()
            16
            sage: E.congruence_number()  # long time
            176
```


Issue created by migration from https://trac.sagemath.org/ticket/4744





---

archive/issue_comments_035883.json:
```json
{
    "body": "Changing component from algebra to number theory.",
    "created_at": "2008-12-09T00:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35883",
    "user": "wuthrich"
}
```

Changing component from algebra to number theory.



---

archive/issue_comments_035884.json:
```json
{
    "body": "I think that the docstring should at least contain the definition of congruence_number, not only a conjecture of what it should be and some examples.",
    "created_at": "2008-12-09T00:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35884",
    "user": "wuthrich"
}
```

I think that the docstring should at least contain the definition of congruence_number, not only a conjecture of what it should be and some examples.



---

archive/issue_comments_035885.json:
```json
{
    "body": "Changing assignee from tbd to was.",
    "created_at": "2008-12-09T00:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35885",
    "user": "wuthrich"
}
```

Changing assignee from tbd to was.



---

archive/issue_comments_035886.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-12-09T00:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35886",
    "user": "wuthrich"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_035887.json:
```json
{
    "body": "Get rid of \"$0 \\le \" in the conjecture, since that part of the inequality is an old theorem of ribet, i.e., that modular degree divides congruence modulus.",
    "created_at": "2008-12-09T22:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35887",
    "user": "was"
}
```

Get rid of "$0 \le " in the conjecture, since that part of the inequality is an old theorem of ribet, i.e., that modular degree divides congruence modulus.



---

archive/issue_comments_035888.json:
```json
{
    "body": "I updated the patch as per both of your recommendations. I also fixed a bug that prevented one from computing the (trivial) congruence_number when E was the only thing in the decomposition of J_0(N).",
    "created_at": "2008-12-10T03:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35888",
    "user": "robertwb"
}
```

I updated the patch as per both of your recommendations. I also fixed a bug that prevented one from computing the (trivial) congruence_number when E was the only thing in the decomposition of J_0(N).



---

archive/issue_comments_035889.json:
```json
{
    "body": "With this patch applied there is one tiny cosmetic doctest failure:\n\n```\nsage -t  \"devel/sage/sage/modular/modsym/space.py\"          \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/modular/modsym/space.py\", line 784, in __main__.example_27\nFailed example:\n    V._q_expansion_module_integral(Integer(5))###line 905:_sage_    >>> V._q_expansion_module_integral(5)\nExpected:\n    Free module of degree 5 and rank 0 over Integer Ring\n    Echelon basis matrix:\n    [ ]\nGot:\n    Free module of degree 5 and rank 0 over Integer Ring\n    Echelon basis matrix:\n    []\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T09:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35889",
    "user": "mabshoff"
}
```

With this patch applied there is one tiny cosmetic doctest failure:

```
sage -t  "devel/sage/sage/modular/modsym/space.py"          
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/modular/modsym/space.py", line 784, in __main__.example_27
Failed example:
    V._q_expansion_module_integral(Integer(5))###line 905:_sage_    >>> V._q_expansion_module_integral(5)
Expected:
    Free module of degree 5 and rank 0 over Integer Ring
    Echelon basis matrix:
    [ ]
Got:
    Free module of degree 5 and rank 0 over Integer Ring
    Echelon basis matrix:
    []
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_035890.json:
```json
{
    "body": "Since the modular degree is insanely fast to compute, maybe you could also throw in a check that it divides the congruence number?  I.e., in the code, right after computing the congruence number, actually compute the modular degree and check divisibility. \n\nAlso, in the square-free case, since it is *theorem* that the modular degree equals the congruence modulus, and the modular degree can be computed a bazillion times faster, maybe just return it instead?  I.e., don't do the modular symbols computation at all in the non-square-free case.  One could have an optional algorithm= flag that could force doing the super-slow modular symbols calculation in all cases, but it is silly to have it as the default.",
    "created_at": "2008-12-10T12:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35890",
    "user": "was"
}
```

Since the modular degree is insanely fast to compute, maybe you could also throw in a check that it divides the congruence number?  I.e., in the code, right after computing the congruence number, actually compute the modular degree and check divisibility. 

Also, in the square-free case, since it is *theorem* that the modular degree equals the congruence modulus, and the modular degree can be computed a bazillion times faster, maybe just return it instead?  I.e., don't do the modular symbols computation at all in the non-square-free case.  One could have an optional algorithm= flag that could force doing the super-slow modular symbols calculation in all cases, but it is silly to have it as the default.



---

archive/issue_comments_035891.json:
```json
{
    "body": "Attachment [4744-congruence-number.patch](tarball://root/attachments/some-uuid/ticket4744/4744-congruence-number.patch) by robertwb created at 2008-12-12 01:29:22\n\nOK, I've updated the patch again.",
    "created_at": "2008-12-12T01:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35891",
    "user": "robertwb"
}
```

Attachment [4744-congruence-number.patch](tarball://root/attachments/some-uuid/ticket4744/4744-congruence-number.patch) by robertwb created at 2008-12-12 01:29:22

OK, I've updated the patch again.



---

archive/issue_comments_035892.json:
```json
{
    "body": "REFEREE REPORT:\n\nPerfect, aside from one typo, where \"Ribit\" should be \"Ribet\".\n\nOnce that typo is fixed, \"positive review\"!",
    "created_at": "2008-12-12T17:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35892",
    "user": "was"
}
```

REFEREE REPORT:

Perfect, aside from one typo, where "Ribit" should be "Ribet".

Once that typo is fixed, "positive review"!



---

archive/issue_comments_035893.json:
```json
{
    "body": "Attachment [4744-congruence-number.2.patch](tarball://root/attachments/some-uuid/ticket4744/4744-congruence-number.2.patch) by mabshoff created at 2008-12-12 17:45:04\n\nThe only change to this patch vs. Robert's is fixing the typo. All credit still goes to RobertWB",
    "created_at": "2008-12-12T17:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35893",
    "user": "mabshoff"
}
```

Attachment [4744-congruence-number.2.patch](tarball://root/attachments/some-uuid/ticket4744/4744-congruence-number.2.patch) by mabshoff created at 2008-12-12 17:45:04

The only change to this patch vs. Robert's is fixing the typo. All credit still goes to RobertWB



---

archive/issue_comments_035894.json:
```json
{
    "body": "I fixed the typo in 4744-congruence-number.2.patch, so positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-12T17:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35894",
    "user": "mabshoff"
}
```

I fixed the typo in 4744-congruence-number.2.patch, so positive review.

Cheers,

Michael



---

archive/issue_comments_035895.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-12T17:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35895",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035896.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-12T17:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35896",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha2



---

archive/issue_comments_035897.json:
```json
{
    "body": "One more small typo: it's Petersson, not Peterson.",
    "created_at": "2008-12-13T10:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35897",
    "user": "craigcitro"
}
```

One more small typo: it's Petersson, not Peterson.



---

archive/issue_comments_035898.json:
```json
{
    "body": "Typo fix by Craig Citro",
    "created_at": "2008-12-13T10:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35898",
    "user": "mabshoff"
}
```

Typo fix by Craig Citro



---

archive/issue_comments_035899.json:
```json
{
    "body": "Attachment [trac_4744-typo-fix.patch](tarball://root/attachments/some-uuid/ticket4744/trac_4744-typo-fix.patch) by mabshoff created at 2008-12-13 10:34:13\n\nMerged trac_4744-typo-fix.patch in Sage 3.2.2 to fix the typo pointed out by Craig Citro.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T10:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4744#issuecomment-35899",
    "user": "mabshoff"
}
```

Attachment [trac_4744-typo-fix.patch](tarball://root/attachments/some-uuid/ticket4744/trac_4744-typo-fix.patch) by mabshoff created at 2008-12-13 10:34:13

Merged trac_4744-typo-fix.patch in Sage 3.2.2 to fix the typo pointed out by Craig Citro.

Cheers,

Michael
