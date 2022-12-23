# Issue 8374: Numerical noise in devel/sage/sage/symbolic/constants_c.pyx

archive/issues_008374.json:
```json
{
    "body": "Assignee: drkirkby\n\n## The computer hardware & software\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM \n* Solaris 10 03/2005 - the first release of Solaris 10. \n\n == The Sage software ==\nSage 4.3.3 with various patches to get it to compile on Solaris. (The notebook is not working properly though). \n\n == The test failure == \n\n```\n****************************************************************\nFile \"/export/home/drkirkby/sage-4.3.3/devel/sage/sage/symbolic/constants_c.pyx\", line 197:\n    sage: e.__float__()\nExpected:\n    2.7182818284590451\nGot:\n    2.7182818284590455\n****************************************************************\n```\n \n \nThis failure on SPARC when displaying E has been seen before.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8374\n\n",
    "created_at": "2010-02-26T08:56:12Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "Numerical noise in devel/sage/sage/symbolic/constants_c.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8374",
    "user": "drkirkby"
}
```
Assignee: drkirkby

## The computer hardware & software
* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM 
* Solaris 10 03/2005 - the first release of Solaris 10. 

 == The Sage software ==
Sage 4.3.3 with various patches to get it to compile on Solaris. (The notebook is not working properly though). 

 == The test failure == 

```
****************************************************************
File "/export/home/drkirkby/sage-4.3.3/devel/sage/sage/symbolic/constants_c.pyx", line 197:
    sage: e.__float__()
Expected:
    2.7182818284590451
Got:
    2.7182818284590455
****************************************************************
```
 
 
This failure on SPARC when displaying E has been seen before.

Issue created by migration from https://trac.sagemath.org/ticket/8374





---

archive/issue_comments_074878.json:
```json
{
    "body": "The attached patch fixes these two failures. \n\n\n```\nkirkby@redstart:~/sage-4.3.3$ ./sage -t devel/sage/sage/symbolic/constants_c.p\nsage -t  \"devel/sage/sage/symbolic/constants_c.pyx\"\n         [65.4 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 65.4 seconds\ndrkirkby@redstart:~/sage-4.3.3$\nyxkirkby@redstart:~/sage-4.3.3$ ./sage -t devel/sage/sage/symbolic/constants_c.py\nsage -t  \"devel/sage/sage/symbolic/constants_c.pyx\"\n         [77.5 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 77.5 seconds\n```\n\n\nAn optional test, which currently expoects the same value of e has also been changed.\n\nThe patch, which will be attached shortly, also has some notes showing\n\n* A high precision value of e\n* The IEEE 754 value\n* The correctly rounded result\n* The value given on a Sun Blade 1000 with SPARC processors.\n\nDave",
    "created_at": "2010-02-26T15:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74878",
    "user": "drkirkby"
}
```

The attached patch fixes these two failures. 


```
kirkby@redstart:~/sage-4.3.3$ ./sage -t devel/sage/sage/symbolic/constants_c.p
sage -t  "devel/sage/sage/symbolic/constants_c.pyx"
         [65.4 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 65.4 seconds
drkirkby@redstart:~/sage-4.3.3$
yxkirkby@redstart:~/sage-4.3.3$ ./sage -t devel/sage/sage/symbolic/constants_c.py
sage -t  "devel/sage/sage/symbolic/constants_c.pyx"
         [77.5 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 77.5 seconds
```


An optional test, which currently expoects the same value of e has also been changed.

The patch, which will be attached shortly, also has some notes showing

* A high precision value of e
* The IEEE 754 value
* The correctly rounded result
* The value given on a Sun Blade 1000 with SPARC processors.

Dave



---

archive/issue_comments_074879.json:
```json
{
    "body": "Mercurial patch",
    "created_at": "2010-02-26T15:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74879",
    "user": "drkirkby"
}
```

Mercurial patch



---

archive/issue_comments_074880.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-02-26T15:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74880",
    "user": "drkirkby"
}
```

Attachment



---

archive/issue_comments_074881.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-26T15:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74881",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074882.json:
```json
{
    "body": "I've left a [comment:ticket:8375:2 review comment] at #8375.",
    "created_at": "2010-03-03T09:25:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74882",
    "user": "mpatel"
}
```

I've left a [comment:ticket:8375:2 review comment] at #8375.



---

archive/issue_comments_074883.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-03T12:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74883",
    "user": "drkirkby"
}
```

Attachment



---

archive/issue_comments_074884.json:
```json
{
    "body": "I've addressed the spelling & grammar errors in 8374-numerical-noise.2.patch  I forgot to overwrite the old one, so there is now a second patch. \n\nSee also comments at #8375",
    "created_at": "2010-03-03T12:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74884",
    "user": "drkirkby"
}
```

I've addressed the spelling & grammar errors in 8374-numerical-noise.2.patch  I forgot to overwrite the old one, so there is now a second patch. 

See also comments at #8375



---

archive/issue_comments_074885.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> I've addressed the spelling & grammar errors in 8374-numerical-noise.2.patch  I forgot to overwrite the old one, so there is now a second patch. \n> \n> See also comments at #8375\n\nSo a positive review.\n\nJaap",
    "created_at": "2010-03-03T20:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74885",
    "user": "jsp"
}
```

Replying to [comment:5 drkirkby]:
> I've addressed the spelling & grammar errors in 8374-numerical-noise.2.patch  I forgot to overwrite the old one, so there is now a second patch. 
> 
> See also comments at #8375

So a positive review.

Jaap



---

archive/issue_comments_074886.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T20:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74886",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074887.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8374#issuecomment-74887",
    "user": "mhansen"
}
```

Resolution: fixed
