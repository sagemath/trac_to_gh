# Issue 8185: numerical noise + crash on sage/calculus/functional.py

archive/issues_008185.json:
```json
{
    "body": "Assignee: drkirkby\n\n## Build environment\nThis was built on a very old / low spec SPARC. But there are some interesting results when built on newer hardware - see later. \n\n* Sun Netra T1 UltraSPARC IIe `@` 500 MHz. \n* Solaris 10 03/05 (first Solaris release of Solaris 10)\n* Sage 4.3.0.1 (special build by Minh for Solaris SPARC. 4.3.0 source, but with #6595 added)\n* gcc 4.4.2 configured with Sun linker and Sun assembler.\n* 32-bit mode - SAGE64 was **not** set to 'yes'\n\n## The problem\n\ndrkirkby`@`kestrel:~/sage-4.3.0.1$ ./sage -t  \"devel/sage-main/build/sage/calculus/functional.py\"\ninit.sage does not exist ... creating\nsage -t  \"devel/sage-main/build/sage/calculus/functional.py\"\n\n```\n**********************************************************************\nFile \"/export/home/drkirkby/sage-4.3.0.1/devel/sage-main/build/sage/calculus/functional.py\", line 195:\n    sage: float(area)\nExpected:\n    0.85914091422952255\nGot:\n    0.85914091422952277\n********************************************************************\n```\n\n\nThis in itself looks easy to fix. \n\n## Interesting side notes\n* Copying the binary to 't2' results in the same problem - no great surprise there. \n* Building this test on a Sun Blade 2000 with gcc 4.4.1 and running it on the Sun Blade 2000, results in not just numerical noise, but a complete crash \n\n\n```\ndrkirkby@swan:[~/sage-4.3.0.1] $ ./sage -t  \"devel/sage-main/build/sage/calculus/functional.py\"\nsage -t  \"devel/sage-main/build/sage/calculus/functional.py\"\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n         [3.1 s]\nexit code: 768\n \n----------------------------------------------------------------------\nThe following tests failed:\n```\n\n\n## Conclusions\n* There is definitely an issue with numerical noise on this test due no doubt to SPARC processor having slightly different to those of an Intel. That is observed both on the Netra T1 and the T5240.\n* A crash is occurring whilst running this test on the Sun Blade 2000. This could potentially be the use of a slightly older compiler (gcc 4.4.1). The RAM is a lot more (8 GB) than on the Sun Netra T1 (1.5 GB) where there is just numerical noise, so it's not a lack of RAM causing this. \n* Copying this from a very old SPARC to the Sun T5240 results in no crashes - only the numerical noise issue. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8185\n\n",
    "created_at": "2010-02-04T16:05:54Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "numerical noise + crash on sage/calculus/functional.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8185",
    "user": "drkirkby"
}
```
Assignee: drkirkby

## Build environment
This was built on a very old / low spec SPARC. But there are some interesting results when built on newer hardware - see later. 

* Sun Netra T1 UltraSPARC IIe `@` 500 MHz. 
* Solaris 10 03/05 (first Solaris release of Solaris 10)
* Sage 4.3.0.1 (special build by Minh for Solaris SPARC. 4.3.0 source, but with #6595 added)
* gcc 4.4.2 configured with Sun linker and Sun assembler.
* 32-bit mode - SAGE64 was **not** set to 'yes'

## The problem

drkirkby`@`kestrel:~/sage-4.3.0.1$ ./sage -t  "devel/sage-main/build/sage/calculus/functional.py"
init.sage does not exist ... creating
sage -t  "devel/sage-main/build/sage/calculus/functional.py"

```
**********************************************************************
File "/export/home/drkirkby/sage-4.3.0.1/devel/sage-main/build/sage/calculus/functional.py", line 195:
    sage: float(area)
Expected:
    0.85914091422952255
Got:
    0.85914091422952277
********************************************************************
```


This in itself looks easy to fix. 

## Interesting side notes
* Copying the binary to 't2' results in the same problem - no great surprise there. 
* Building this test on a Sun Blade 2000 with gcc 4.4.1 and running it on the Sun Blade 2000, results in not just numerical noise, but a complete crash 


```
drkirkby@swan:[~/sage-4.3.0.1] $ ./sage -t  "devel/sage-main/build/sage/calculus/functional.py"
sage -t  "devel/sage-main/build/sage/calculus/functional.py"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [3.1 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:
```


## Conclusions
* There is definitely an issue with numerical noise on this test due no doubt to SPARC processor having slightly different to those of an Intel. That is observed both on the Netra T1 and the T5240.
* A crash is occurring whilst running this test on the Sun Blade 2000. This could potentially be the use of a slightly older compiler (gcc 4.4.1). The RAM is a lot more (8 GB) than on the Sun Netra T1 (1.5 GB) where there is just numerical noise, so it's not a lack of RAM causing this. 
* Copying this from a very old SPARC to the Sun T5240 results in no crashes - only the numerical noise issue. 



Issue created by migration from https://trac.sagemath.org/ticket/8185





---

archive/issue_comments_072138.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-04T19:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8185#issuecomment-72138",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072139.json:
```json
{
    "body": "Here's a Mercurial patch, which fixes the issue \n\n\n```\ndrkirkby@kestrel:~/sage-4.3.0.1$ ./sage -t devel/sage-main/build/sage/calculus/functional.py\nsage -t  \"devel/sage-main/build/sage/calculus/functional.py\"\n         [65.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 65.0 seconds\n```\n",
    "created_at": "2010-02-04T19:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8185#issuecomment-72139",
    "user": "drkirkby"
}
```

Here's a Mercurial patch, which fixes the issue 


```
drkirkby@kestrel:~/sage-4.3.0.1$ ./sage -t devel/sage-main/build/sage/calculus/functional.py
sage -t  "devel/sage-main/build/sage/calculus/functional.py"
         [65.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 65.0 seconds
```




---

archive/issue_comments_072140.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-02-04T20:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8185#issuecomment-72140",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_072141.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-04T20:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8185#issuecomment-72141",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072142.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8185#issuecomment-72142",
    "user": "mpatel"
}
```

Resolution: fixed
