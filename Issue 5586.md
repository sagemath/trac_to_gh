# Issue 5586: [with patch, needs review]

archive/issues_005586.json:
```json
{
    "body": "Assignee: malb\n\nCC:  burcin rpw\n\nKeywords: crypto, aes\n\n**Before**:\n\n```\nsage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)\nsage: %time F,s = sr.polynomial_system()\nCPU times: user 23.46 s, sys: 0.07 s, total: 23.52 s\nWall time: 23.61 s\n```\n\n\n**After**:\n\n```\nsage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)\nsage: %time F,s = sr.polynomial_system()\nCPU times: user 3.58 s, sys: 0.04 s, total: 3.62 s\nWall time: 3.63 s\nsage: %time F,s = sr.polynomial_system()\nCPU times: user 2.05 s, sys: 0.00 s, total: 2.05 s\nWall time: 2.05 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5586\n\n",
    "created_at": "2009-03-22T17:54:03Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5586",
    "user": "malb"
}
```
Assignee: malb

CC:  burcin rpw

Keywords: crypto, aes

**Before**:

```
sage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)
sage: %time F,s = sr.polynomial_system()
CPU times: user 23.46 s, sys: 0.07 s, total: 23.52 s
Wall time: 23.61 s
```


**After**:

```
sage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)
sage: %time F,s = sr.polynomial_system()
CPU times: user 3.58 s, sys: 0.04 s, total: 3.62 s
Wall time: 3.63 s
sage: %time F,s = sr.polynomial_system()
CPU times: user 2.05 s, sys: 0.00 s, total: 2.05 s
Wall time: 2.05 s
```


Issue created by migration from https://trac.sagemath.org/ticket/5586





---

archive/issue_comments_043532.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-22T17:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43532",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_043533.json:
```json
{
    "body": "allows symbols for plaintext/ciphertext bits",
    "created_at": "2009-03-25T14:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43533",
    "user": "malb"
}
```

allows symbols for plaintext/ciphertext bits



---

archive/issue_comments_043534.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-25T14:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43534",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_043535.json:
```json
{
    "body": "Does attachment:sr_symbolic.patch depend on anything?\n\nI get this while trying to apply to a clean 3.4 tree, or after applying attachment:faster_sr.patch:\n\n\n```\napplying sr_symbolic.patch\npatching file sage/crypto/mq/sr.py\nHunk #3 succeeded at 1618 with fuzz 1 (offset 29 lines).\nHunk #4 FAILED at 1925\n1 out of 7 hunks FAILED -- saving rejects to file sage/crypto/mq/sr.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh sr_symbolic.patch\n```\n",
    "created_at": "2009-03-25T18:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43535",
    "user": "burcin"
}
```

Does attachment:sr_symbolic.patch depend on anything?

I get this while trying to apply to a clean 3.4 tree, or after applying attachment:faster_sr.patch:


```
applying sr_symbolic.patch
patching file sage/crypto/mq/sr.py
Hunk #3 succeeded at 1618 with fuzz 1 (offset 29 lines).
Hunk #4 FAILED at 1925
1 out of 7 hunks FAILED -- saving rejects to file sage/crypto/mq/sr.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh sr_symbolic.patch
```




---

archive/issue_comments_043536.json:
```json
{
    "body": "Uh, it seems this ticket depends on #5493 and #5527.",
    "created_at": "2009-03-25T18:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43536",
    "user": "malb"
}
```

Uh, it seems this ticket depends on #5493 and #5527.



---

archive/issue_comments_043537.json:
```json
{
    "body": "OK, I applied the patches against Sage 3.4 in this order:\n1. the patch at #5493\n2. that patch at #5527\n3. finally the patches on this ticket\nBut I got doctest failure:\n\n```\n[mvngu@sage sage-3.4]$ ./sage -t -long devel/sage-5586/sage/crypto/mq/sr.py \nsage -t -long \"devel/sage-5586/sage/crypto/mq/sr.py\"        \n**********************************************************************\nFile \"/home/mvngu/sage-3.4/devel/sage-5586/sage/crypto/mq/sr.py\", line 2002:\n    sage: F.round(0)\nExpected:\n    (P000 + w100 + k000, P001 + w101 + k001, P002 + w102 + k002, P003 + w103 + k003)\nGot:\n    [P000 + w100 + k000, P001 + w101 + k001, P002 + w102 + k002, P003 + w103 + k003]\n**********************************************************************\nFile \"/home/mvngu/sage-3.4/devel/sage-5586/sage/crypto/mq/sr.py\", line 2004:\n    sage: F.round(-2)\nExpected:\n    (k100 + x100 + x102 + x103 + C000, k101 + x100 + x101 + x103 + C001 + 1, ...)\nGot:\n    [k100 + x100 + x102 + x103 + C000, k101 + x100 + x101 + x103 + C001 + 1, k102 + x100 + x101 + x102 + C002 + 1, k103 + x101 + x102 + x103 + C003, x100*w100 + x100*w103 + x101*w102 + x102*w101 + x103*w100, x100*w100 + x100*w101 + x101*w100 + x101*w103 + x102*w102 + x103*w101, x100*w101 + x100*w102 + x101*w100 + x101*w101 + x102*w100 + x102*w103 + x103*w102, x100*w100 + x100*w102 + x100*w103 + x100 + x101*w100 + x101*w101 + x102*w102 + x103*w100, x100*w101 + x100*w103 + x101*w101 + x101*w102 + x101 + x102*w100 + x102*w103 + x103*w101, x100*w100 + x100*w102 + x101*w100 + x101*w102 + x101*w103 + x102*w100 + x102*w101 + x102 + x103*w102, x100*w101 + x100*w102 + x101*w100 + x101*w103 + x102*w101 + x103*w103 + x103, x100*w100 + x100*w101 + x100*w103 + x101*w101 + x102*w100 + x102*w102 + x103*w100 + w100, x100*w102 + x101*w100 + x101*w101 + x101*w103 + x102*w101 + x103*w100 + x103*w102 + w101, x100*w100 + x100*w101 + x100*w102 + x101*w102 + x102*w100 + x102*w101 + x102*w103 + x103*w101 + w102, x100*w101 + x101*w100 + x101*w102 + x102*w100 + x103*w101 + x103*w103 + w103, x100*w102 + x101*w101 + x102*w100 + x103*w103 + 1]\n**********************************************************************\n1 items had failures:\n   2 of  25 in __main__.example_35\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/mvngu/sage-3.4/tmp/.doctest_sr.py\n         [73.1 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage-5586/sage/crypto/mq/sr.py\"\nTotal time for all tests: 73.1 seconds\n```\n",
    "created_at": "2009-03-27T06:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43537",
    "user": "mvngu"
}
```

OK, I applied the patches against Sage 3.4 in this order:
1. the patch at #5493
2. that patch at #5527
3. finally the patches on this ticket
But I got doctest failure:

```
[mvngu@sage sage-3.4]$ ./sage -t -long devel/sage-5586/sage/crypto/mq/sr.py 
sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"        
**********************************************************************
File "/home/mvngu/sage-3.4/devel/sage-5586/sage/crypto/mq/sr.py", line 2002:
    sage: F.round(0)
Expected:
    (P000 + w100 + k000, P001 + w101 + k001, P002 + w102 + k002, P003 + w103 + k003)
Got:
    [P000 + w100 + k000, P001 + w101 + k001, P002 + w102 + k002, P003 + w103 + k003]
**********************************************************************
File "/home/mvngu/sage-3.4/devel/sage-5586/sage/crypto/mq/sr.py", line 2004:
    sage: F.round(-2)
Expected:
    (k100 + x100 + x102 + x103 + C000, k101 + x100 + x101 + x103 + C001 + 1, ...)
Got:
    [k100 + x100 + x102 + x103 + C000, k101 + x100 + x101 + x103 + C001 + 1, k102 + x100 + x101 + x102 + C002 + 1, k103 + x101 + x102 + x103 + C003, x100*w100 + x100*w103 + x101*w102 + x102*w101 + x103*w100, x100*w100 + x100*w101 + x101*w100 + x101*w103 + x102*w102 + x103*w101, x100*w101 + x100*w102 + x101*w100 + x101*w101 + x102*w100 + x102*w103 + x103*w102, x100*w100 + x100*w102 + x100*w103 + x100 + x101*w100 + x101*w101 + x102*w102 + x103*w100, x100*w101 + x100*w103 + x101*w101 + x101*w102 + x101 + x102*w100 + x102*w103 + x103*w101, x100*w100 + x100*w102 + x101*w100 + x101*w102 + x101*w103 + x102*w100 + x102*w101 + x102 + x103*w102, x100*w101 + x100*w102 + x101*w100 + x101*w103 + x102*w101 + x103*w103 + x103, x100*w100 + x100*w101 + x100*w103 + x101*w101 + x102*w100 + x102*w102 + x103*w100 + w100, x100*w102 + x101*w100 + x101*w101 + x101*w103 + x102*w101 + x103*w100 + x103*w102 + w101, x100*w100 + x100*w101 + x100*w102 + x101*w102 + x102*w100 + x102*w101 + x102*w103 + x103*w101 + w102, x100*w101 + x101*w100 + x101*w102 + x102*w100 + x103*w101 + x103*w103 + w103, x100*w102 + x101*w101 + x102*w100 + x103*w103 + 1]
**********************************************************************
1 items had failures:
   2 of  25 in __main__.example_35
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/sage-3.4/tmp/.doctest_sr.py
         [73.1 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"
Total time for all tests: 73.1 seconds
```




---

archive/issue_comments_043538.json:
```json
{
    "body": "Sorry 'bout this: you'll also need to apply the patch from #5576 (`mpolynomialsystem_rest.patch`). I kept working on too many things in parallel and thus the mess:\n\nHere's what I've applied locally:\n* sr_sphinx.patch #5493\n* weil_restriction.patch #5569\n* mpolynomialsystem_rest.patch #5576\n* trac_5527_sr-sphinx.patch #5527\n* faster_sr.patch #5586\n* sr_symbolic.patch #5586",
    "created_at": "2009-03-27T10:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43538",
    "user": "malb"
}
```

Sorry 'bout this: you'll also need to apply the patch from #5576 (`mpolynomialsystem_rest.patch`). I kept working on too many things in parallel and thus the mess:

Here's what I've applied locally:
* sr_sphinx.patch #5493
* weil_restriction.patch #5569
* mpolynomialsystem_rest.patch #5576
* trac_5527_sr-sphinx.patch #5527
* faster_sr.patch #5586
* sr_symbolic.patch #5586



---

archive/issue_comments_043539.json:
```json
{
    "body": "Again, I see timed out errors. With Sage 3.4, I applied patches in this order:\n1. sr_sphinx.patch at #5493\n2. weil_restriction.patch at #5569\n3. mpolynomialsystem_rest.patch at #5576\n4. trac_5527_sr-sphinx.patch at #5527\n5. faster_sr.patch at #5586 (this ticket)\n6. sr_symbolic.patch at #5586  (this ticket)\nDoctesting gave me this:\n\n```\n[mvngu@sage sage-3.4-sage.math-only-x86_64-Linux]$ ./sage -t -long devel/sage-5586/sage/crypto/mq/sr.py \nsage -t -long \"devel/sage-5586/sage/crypto/mq/sr.py\"        \n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [1800.2 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage-5586/sage/crypto/mq/sr.py\"\nTotal time for all tests: 1800.2 seconds\n```\n\n\n\n\nAs for Sage 3.4.1.alph0, I applied patches in this order:\n1. mpolynomialsystem_rest.patch at #5576\n2. faster_sr.patch at #5586 (this ticket)\n3. sr_symbolic.patch at #5586  (this ticket)\nDoctesting gave me timed out errors as well:\n\n```\n[mvngu@sage sage-3.4.1.alpha0-sage.math-only-x86_64-Linux]$ ./sage -t -long devel/sage-5586/sage/crypto/mq/sr.py\nsage -t -long \"devel/sage-5586/sage/crypto/mq/sr.py\"        \n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [1800.1 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage-5586/sage/crypto/mq/sr.py\"\nTotal time for all tests: 1800.1 seconds\n```\n",
    "created_at": "2009-03-31T04:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43539",
    "user": "mvngu"
}
```

Again, I see timed out errors. With Sage 3.4, I applied patches in this order:
1. sr_sphinx.patch at #5493
2. weil_restriction.patch at #5569
3. mpolynomialsystem_rest.patch at #5576
4. trac_5527_sr-sphinx.patch at #5527
5. faster_sr.patch at #5586 (this ticket)
6. sr_symbolic.patch at #5586  (this ticket)
Doctesting gave me this:

```
[mvngu@sage sage-3.4-sage.math-only-x86_64-Linux]$ ./sage -t -long devel/sage-5586/sage/crypto/mq/sr.py 
sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"        
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [1800.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"
Total time for all tests: 1800.2 seconds
```




As for Sage 3.4.1.alph0, I applied patches in this order:
1. mpolynomialsystem_rest.patch at #5576
2. faster_sr.patch at #5586 (this ticket)
3. sr_symbolic.patch at #5586  (this ticket)
Doctesting gave me timed out errors as well:

```
[mvngu@sage sage-3.4.1.alpha0-sage.math-only-x86_64-Linux]$ ./sage -t -long devel/sage-5586/sage/crypto/mq/sr.py
sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"        
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [1800.1 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"
Total time for all tests: 1800.1 seconds
```




---

archive/issue_comments_043540.json:
```json
{
    "body": "I hope you don't mind me asking, but are you sure you applied the correct mpolynomialsystem_rest.patch? Can you check that the `test_consistency()` function sr.py has the line \n\n```\nF = F.subs(s)\n```\n\ninstead of\n\n```\nF.subs(s)\n```\n\n\nCheers,\nMartin",
    "created_at": "2009-03-31T08:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43540",
    "user": "malb"
}
```

I hope you don't mind me asking, but are you sure you applied the correct mpolynomialsystem_rest.patch? Can you check that the `test_consistency()` function sr.py has the line 

```
F = F.subs(s)
```

instead of

```
F.subs(s)
```


Cheers,
Martin



---

archive/issue_comments_043541.json:
```json
{
    "body": "Replying to [comment:8 malb]:\n> I hope you don't mind me asking, but are you sure you applied the correct mpolynomialsystem_rest.patch? Can you check that the `test_consistency()` function sr.py has the line \n> {{{\n> F = F.subs(s)\n> }}}\n> instead of\n> {{{\n> F.subs(s)\n> }}}\n\n\nYep, you're right. I downloaded `mpolynomialsystem_rest.patch` again and then proceeded with applying patches against Sage 3.4.1.alpha0 in this order:\n1. mpolynomialsystem_rest.patch at #5576\n2. faster_sr.patch at #5586 (this ticket)\n3. sr_symbolic.patch at #5586 (this ticket) \nThis time doctests didn't reveal any timed out errors. I don't feel qualified to review the math content of the patches; I was only trying to apply patches and run doctests to see if they succeed or fail.",
    "created_at": "2009-04-02T08:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43541",
    "user": "mvngu"
}
```

Replying to [comment:8 malb]:
> I hope you don't mind me asking, but are you sure you applied the correct mpolynomialsystem_rest.patch? Can you check that the `test_consistency()` function sr.py has the line 
> {{{
> F = F.subs(s)
> }}}
> instead of
> {{{
> F.subs(s)
> }}}


Yep, you're right. I downloaded `mpolynomialsystem_rest.patch` again and then proceeded with applying patches against Sage 3.4.1.alpha0 in this order:
1. mpolynomialsystem_rest.patch at #5576
2. faster_sr.patch at #5586 (this ticket)
3. sr_symbolic.patch at #5586 (this ticket) 
This time doctests didn't reveal any timed out errors. I don't feel qualified to review the math content of the patches; I was only trying to apply patches and run doctests to see if they succeed or fail.



---

archive/issue_comments_043542.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-05-12T14:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43542",
    "user": "burcin"
}
```

Looks good to me.



---

archive/issue_comments_043543.json:
```json
{
    "body": "Attachment\n\napply last",
    "created_at": "2009-05-12T17:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43543",
    "user": "malb"
}
```

Attachment

apply last



---

archive/issue_comments_043544.json:
```json
{
    "body": "fix_long_doctest.patch fixes the timeout problem.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T17:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43544",
    "user": "mabshoff"
}
```

fix_long_doctest.patch fixes the timeout problem.

Cheers,

Michael



---

archive/issue_comments_043545.json:
```json
{
    "body": "Merged all three patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T17:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43545",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_043546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T17:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5586#issuecomment-43546",
    "user": "mabshoff"
}
```

Resolution: fixed
