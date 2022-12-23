# Issue 4599: sage/schemes/elliptic_curves/ell_rational_field.py doctest failure due to missing "#optional"

archive/issues_004599.json:
```json
{
    "body": "Assignee: mabshoff\n\nJaap reported:\n\n```\nsage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\n************** ******************************************************** \nFile \"/home/jaap/downloads/sage-3.2.1.alpha0/devel/sage/sage/schemes/elliptic_cu rves/ell_rational_field.py\", line 1183: \n     sage: EllipticCurve('14a1').three_selmer_rank() \nException raised: \n[...] \n     TypeError: Unable to start magma because the command 'magma -n' failed. \n********************************************************************** \n1 items had failures: \n    1 of   3 in __main__.example_29 \n***Test Failed*** 1 failures. \nFor whitespace errors, see the file /home/jaap/downloads/sage-3.2.1.alpha0/tmp/.doctest_ell_rational_field.py \n         [79.8 s] \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4599\n\n",
    "created_at": "2008-11-23T22:12:06Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "sage/schemes/elliptic_curves/ell_rational_field.py doctest failure due to missing \"#optional\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4599",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Jaap reported:

```
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
************** ******************************************************** 
File "/home/jaap/downloads/sage-3.2.1.alpha0/devel/sage/sage/schemes/elliptic_cu rves/ell_rational_field.py", line 1183: 
     sage: EllipticCurve('14a1').three_selmer_rank() 
Exception raised: 
[...] 
     TypeError: Unable to start magma because the command 'magma -n' failed. 
********************************************************************** 
1 items had failures: 
    1 of   3 in __main__.example_29 
***Test Failed*** 1 failures. 
For whitespace errors, see the file /home/jaap/downloads/sage-3.2.1.alpha0/tmp/.doctest_ell_rational_field.py 
         [79.8 s] 
```


Issue created by migration from https://trac.sagemath.org/ticket/4599





---

archive/issue_comments_034481.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-23T22:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4599#issuecomment-34481",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034482.json:
```json
{
    "body": "Mmh, with #4600 the problem seems to disappear, but I am still posting a patch here.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T23:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4599#issuecomment-34482",
    "user": "mabshoff"
}
```

Mmh, with #4600 the problem seems to disappear, but I am still posting a patch here.

Cheers,

Michael



---

archive/issue_comments_034483.json:
```json
{
    "body": "Attachment\n\nThe patch worked for me:\n\n\n\n```\n[jaap@paix sage-3.2.1.alpha0]$ ./sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\nsage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\n\t [86.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 86.9 seconds\n\n```\n",
    "created_at": "2008-11-24T23:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4599#issuecomment-34483",
    "user": "jsp"
}
```

Attachment

The patch worked for me:



```
[jaap@paix sage-3.2.1.alpha0]$ ./sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
	 [86.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 86.9 seconds

```




---

archive/issue_comments_034484.json:
```json
{
    "body": "Thanks Jaap. My previous comment about #4600 fixing this ticket is plain wrong since I did have the real Magma in $PATH.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T23:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4599#issuecomment-34484",
    "user": "mabshoff"
}
```

Thanks Jaap. My previous comment about #4600 fixing this ticket is plain wrong since I did have the real Magma in $PATH.

Cheers,

Michael



---

archive/issue_comments_034485.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1",
    "created_at": "2008-11-24T23:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4599#issuecomment-34485",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha1



---

archive/issue_comments_034486.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-24T23:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4599#issuecomment-34486",
    "user": "mabshoff"
}
```

Resolution: fixed
