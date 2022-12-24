# Issue 8375: Numerical noise in devel/sage/sage/symbolic/pynac.pyx

archive/issues_008375.json:
```json
{
    "body": "Assignee: drkirkby\n\n == The computer hardware & software ==\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM \n* Solaris 10 03/2005 - the first release of Solaris 10. \n\n == The Sage software ==\nSage 4.3.3 with various patches to get it to compile on Solaris. (The notebook is not working properly though). \n\n == The test failure == \n\n\n```\n**********************************************************************\nFile \"/export/home/drkirkby/sage-4.3.3/devel/sage/sage/symbolic/pynac.pyx\", line 1282:\n    sage: py_exp(float(1))\nExpected:\n    2.7182818284590451\nGot:\n    2.7182818284590455\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8375\n\n",
    "created_at": "2010-02-26T09:00:54Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Numerical noise in devel/sage/sage/symbolic/pynac.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8375",
    "user": "drkirkby"
}
```
Assignee: drkirkby

 == The computer hardware & software ==
* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM 
* Solaris 10 03/2005 - the first release of Solaris 10. 

 == The Sage software ==
Sage 4.3.3 with various patches to get it to compile on Solaris. (The notebook is not working properly though). 

 == The test failure == 


```
**********************************************************************
File "/export/home/drkirkby/sage-4.3.3/devel/sage/sage/symbolic/pynac.pyx", line 1282:
    sage: py_exp(float(1))
Expected:
    2.7182818284590451
Got:
    2.7182818284590455
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/8375





---

archive/issue_comments_074888.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-26T14:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8375#issuecomment-74888",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074889.json:
```json
{
    "body": "The attached patch fixes this. It also has some notes showing \n\n* A high precision value of e\n* The IEEE 754 value \n* The correctly rounded result\n* The value given on the SPARC processor. \n\n\n```\ndrkirkby@redstart:~/sage-4.3.3$ ./sage -t devel/sage/sage/symbolic/pynac.pyx\nsage -t  \"devel/sage/sage/symbolic/pynac.pyx\"\n         [156.7 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 156.7 seconds\nsage/sage/symbolic/pynac.pyx.3$ drkirkby@redstart:~/sage-4.3.3$ ./sage -t devel/\n-bash: drkirkby@redstart:~/sage-4.3.3$: No such file or directory\nsage -t  \"devel/sage/sage/symbolic/pynac.pyx\"\n         [156.7 s]\n\n```\n",
    "created_at": "2010-02-26T14:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8375#issuecomment-74889",
    "user": "drkirkby"
}
```

The attached patch fixes this. It also has some notes showing 

* A high precision value of e
* The IEEE 754 value 
* The correctly rounded result
* The value given on the SPARC processor. 


```
drkirkby@redstart:~/sage-4.3.3$ ./sage -t devel/sage/sage/symbolic/pynac.pyx
sage -t  "devel/sage/sage/symbolic/pynac.pyx"
         [156.7 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 156.7 seconds
sage/sage/symbolic/pynac.pyx.3$ drkirkby@redstart:~/sage-4.3.3$ ./sage -t devel/
-bash: drkirkby@redstart:~/sage-4.3.3$: No such file or directory
sage -t  "devel/sage/sage/symbolic/pynac.pyx"
         [156.7 s]

```




---

archive/issue_comments_074890.json:
```json
{
    "body": "The patches at #8374 and here fix the corresponding doctest failures in 4.3.0.1 on t2 and still pass in 4.3.3 on sage.math.\n\nJust to check: Did \"sage-devel\" agree that this was the best approach to the problem? \n\nI'm not sure if Minh is already reviewing these tickets.  To the extent it counts, my review is positive, provided that you fix the [minor, admittedly] spelling / grammatical errors.",
    "created_at": "2010-03-03T09:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8375#issuecomment-74890",
    "user": "mpatel"
}
```

The patches at #8374 and here fix the corresponding doctest failures in 4.3.0.1 on t2 and still pass in 4.3.3 on sage.math.

Just to check: Did "sage-devel" agree that this was the best approach to the problem? 

I'm not sure if Minh is already reviewing these tickets.  To the extent it counts, my review is positive, provided that you fix the [minor, admittedly] spelling / grammatical errors.



---

archive/issue_comments_074891.json:
```json
{
    "body": "Attachment [numerical-noise-on-SPARC.patch](tarball://root/attachments/some-uuid/ticket8375/numerical-noise-on-SPARC.patch) by drkirkby created at 2010-03-03 11:45:14\n\nWith grammer/spelling corrections.",
    "created_at": "2010-03-03T11:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8375#issuecomment-74891",
    "user": "drkirkby"
}
```

Attachment [numerical-noise-on-SPARC.patch](tarball://root/attachments/some-uuid/ticket8375/numerical-noise-on-SPARC.patch) by drkirkby created at 2010-03-03 11:45:14

With grammer/spelling corrections.



---

archive/issue_comments_074892.json:
```json
{
    "body": "There was only one comment from Robert as to whether there was another way to get the SPARC processor to produce the same output as Intel. I mentioned there was, but it would require  very significant changes. \n\nThe exact same correction for 'e' was made once before for the SPARC processor. It has been implemented numerous time for other processors. \n\nI've corrected the grammar/spelling.",
    "created_at": "2010-03-03T11:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8375#issuecomment-74892",
    "user": "drkirkby"
}
```

There was only one comment from Robert as to whether there was another way to get the SPARC processor to produce the same output as Intel. I mentioned there was, but it would require  very significant changes. 

The exact same correction for 'e' was made once before for the SPARC processor. It has been implemented numerous time for other processors. 

I've corrected the grammar/spelling.



---

archive/issue_comments_074893.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T20:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8375#issuecomment-74893",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074894.json:
```json
{
    "body": "Replying to [comment:3 drkirkby]:\n> There was only one comment from Robert as to whether there was another way to get the SPARC processor to produce the same output as Intel. I mentioned there was, but it would require  very significant changes. \n> \n> The exact same correction for 'e' was made once before for the SPARC processor. It has been implemented numerous time for other processors. \n> \n> I've corrected the grammar/spelling. \n\n\nFrom me a positive review.\n\nJaap",
    "created_at": "2010-03-03T20:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8375#issuecomment-74894",
    "user": "jsp"
}
```

Replying to [comment:3 drkirkby]:
> There was only one comment from Robert as to whether there was another way to get the SPARC processor to produce the same output as Intel. I mentioned there was, but it would require  very significant changes. 
> 
> The exact same correction for 'e' was made once before for the SPARC processor. It has been implemented numerous time for other processors. 
> 
> I've corrected the grammar/spelling. 


From me a positive review.

Jaap



---

archive/issue_comments_074895.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8375#issuecomment-74895",
    "user": "mhansen"
}
```

Resolution: fixed
