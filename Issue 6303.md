# Issue 6303: sage-4.0.2.rc0 test failure

archive/issues_006303.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nBuilt fine, 2 test failyres on 32-bit Suse:  the singular.pyx issue\nalready reported, and\n\n**********************************************************************\nFile \"/local/jec/sage-4.0.2.rc0/devel/sage/sage/rings/number_field/number_field_element.pyx\",\nline 2092:\n   sage: [L(6).valuation(P) for P in L.primes_above(6)]\nExpected:\n   [2, 2, 4]\nGot:\n   [4, 2, 2]\n**********************************************************************\n\nThat is on old issue: L.primes_above(6) tries to sort the primes but\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6303\n\n",
    "created_at": "2009-06-15T17:04:45Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "sage-4.0.2.rc0 test failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6303",
    "user": "was"
}
```
Assignee: tbd


```
Built fine, 2 test failyres on 32-bit Suse:  the singular.pyx issue
already reported, and

**********************************************************************
File "/local/jec/sage-4.0.2.rc0/devel/sage/sage/rings/number_field/number_field_element.pyx",
line 2092:
   sage: [L(6).valuation(P) for P in L.primes_above(6)]
Expected:
   [2, 2, 4]
Got:
   [4, 2, 2]
**********************************************************************

That is on old issue: L.primes_above(6) tries to sort the primes but
```


Issue created by migration from https://trac.sagemath.org/ticket/6303





---

archive/issue_comments_050285.json:
```json
{
    "body": "A patch is on its way...\n\nJohn",
    "created_at": "2009-06-15T17:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50285",
    "user": "cremona"
}
```

A patch is on its way...

John



---

archive/issue_comments_050286.json:
```json
{
    "body": "Applies to 4.0.2.rc0",
    "created_at": "2009-06-15T19:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50286",
    "user": "cremona"
}
```

Applies to 4.0.2.rc0



---

archive/issue_comments_050287.json:
```json
{
    "body": "Attachment\n\nAs I said on sage-devel, this patch does two things: (1) fix the doctest so it does not depend on the ordering of primes_above() output; (2) fix primes_above to it (partially) orders its output as its docstring describes.",
    "created_at": "2009-06-15T19:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50287",
    "user": "cremona"
}
```

Attachment

As I said on sage-devel, this patch does two things: (1) fix the doctest so it does not depend on the ordering of primes_above() output; (2) fix primes_above to it (partially) orders its output as its docstring describes.



---

archive/issue_comments_050288.json:
```json
{
    "body": "Good for me on sage.math and OS X 10.5.",
    "created_at": "2009-06-15T19:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50288",
    "user": "ncalexan"
}
```

Good for me on sage.math and OS X 10.5.



---

archive/issue_comments_050289.json:
```json
{
    "body": "Note that this failure was reported on 32 bit linux. So I don't see it is any good to report it good for sage.math or OS X 10.5.\n\n\n```\nsage -t  \"devel/sage/sage/rings/number_field/number_field_element.pyx\"\n\t [24.4 s]\n \n----------------------------------------------------------------------\nAll tests passed!\n```\n\n\nOn Fedora 9, 32 bit.\n\nSo also a positive review from here.\n\nJaap",
    "created_at": "2009-06-15T19:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50289",
    "user": "jsp"
}
```

Note that this failure was reported on 32 bit linux. So I don't see it is any good to report it good for sage.math or OS X 10.5.


```
sage -t  "devel/sage/sage/rings/number_field/number_field_element.pyx"
	 [24.4 s]
 
----------------------------------------------------------------------
All tests passed!
```


On Fedora 9, 32 bit.

So also a positive review from here.

Jaap



---

archive/issue_comments_050290.json:
```json
{
    "body": "Thanks Jaap -- I did test my patch on both 32-bit and 64-bit linuxes!",
    "created_at": "2009-06-15T20:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50290",
    "user": "cremona"
}
```

Thanks Jaap -- I did test my patch on both 32-bit and 64-bit linuxes!



---

archive/issue_comments_050291.json:
```json
{
    "body": "Sure John, I didn't expect less :-)!\n\nJaap",
    "created_at": "2009-06-15T20:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50291",
    "user": "jsp"
}
```

Sure John, I didn't expect less :-)!

Jaap



---

archive/issue_comments_050292.json:
```json
{
    "body": "merged into 4.0.2.rc1",
    "created_at": "2009-06-15T23:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50292",
    "user": "was"
}
```

merged into 4.0.2.rc1



---

archive/issue_comments_050293.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-15T23:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50293",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_050294.json:
```json
{
    "body": "Actually this patch breaks several doctests in `devel/sage/sage/schemes/elliptic_curves/ell_number_field.py`.",
    "created_at": "2009-06-16T00:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50294",
    "user": "was"
}
```

Actually this patch breaks several doctests in `devel/sage/sage/schemes/elliptic_curves/ell_number_field.py`.



---

archive/issue_comments_050295.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-06-16T00:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50295",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_050296.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-06-16T00:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50296",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_050297.json:
```json
{
    "body": "The failures in `ell_number_field.py` are just coming from the new sort order for the `primes_above` method. I'm attaching a second patch which fixes these doctests.",
    "created_at": "2009-06-16T07:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50297",
    "user": "craigcitro"
}
```

The failures in `ell_number_field.py` are just coming from the new sort order for the `primes_above` method. I'm attaching a second patch which fixes these doctests.



---

archive/issue_comments_050298.json:
```json
{
    "body": "Unfortunately, the output order varies from system to system. So the second patch above won't help ... deleting it now.",
    "created_at": "2009-06-16T07:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50298",
    "user": "craigcitro"
}
```

Unfortunately, the output order varies from system to system. So the second patch above won't help ... deleting it now.



---

archive/issue_comments_050299.json:
```json
{
    "body": "Apologies sine it was my \"trivial\" patch which caused the problems.  The whole point of the ordering of the output of ideals_above was to make it machine-independent!  Hence by dismay when I saw that my earlier code had been removed - -perhaps by someone who noted that it was not perfect yet.  I'm working on it!",
    "created_at": "2009-06-16T08:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50299",
    "user": "cremona"
}
```

Apologies sine it was my "trivial" patch which caused the problems.  The whole point of the ordering of the output of ideals_above was to make it machine-independent!  Hence by dismay when I saw that my earlier code had been removed - -perhaps by someone who noted that it was not perfect yet.  I'm working on it!



---

archive/issue_comments_050300.json:
```json
{
    "body": "Attachment\n\nActually, I just tried this again on two different machines (32 bit OSX and sage.math), and it seems to work fine with the second patch. (Nick tried this on 32 bit OSX and had trouble, but I can't reproduce that.) If someone gets this to fail, let me know what arch/OS.",
    "created_at": "2009-06-16T08:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50300",
    "user": "craigcitro"
}
```

Attachment

Actually, I just tried this again on two different machines (32 bit OSX and sage.math), and it seems to work fine with the second patch. (Nick tried this on 32 bit OSX and had trouble, but I can't reproduce that.) If someone gets this to fail, let me know what arch/OS.



---

archive/issue_comments_050301.json:
```json
{
    "body": "Applied both patches ok to 4.0.2.rc0, all tests pass in both elliptic_curves and number_fields directories, on both 32 and 64 bit linux.",
    "created_at": "2009-06-16T08:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50301",
    "user": "cremona"
}
```

Applied both patches ok to 4.0.2.rc0, all tests pass in both elliptic_curves and number_fields directories, on both 32 and 64 bit linux.



---

archive/issue_comments_050302.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-17T23:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6303#issuecomment-50302",
    "user": "craigcitro"
}
```

Resolution: fixed
