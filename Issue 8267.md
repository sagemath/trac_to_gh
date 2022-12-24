# Issue 8267: cygwin: ratpoints is broken again

archive/issues_008267.json:
```json
{
    "body": "Assignee: tbd\n\nI just tried building the ratpoints package on Cygwin, and \n\n```\ngcc main.c -o ratpoints -I/home/wstein/build/sage-4.3.3.alpha0/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -L/home/wstein/build/sage-4.3.3.alpha0/local/lib -lgmp -lm -L. -lratpoints                                     \nmain.c:1: warning: -fPIC ignored for target (all code is position independent)                                             \n./libratpoints.a(find_points.o):find_points.c:(.text+0x170): undefined reference to `__imp____gmpz_mul_si' \nBOOM!\n```\n\n\nThus the fixed that got in from #7015 has been broken before it ever really got to live :-(. \n\nSo this ticket is to implement that fix again. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8267\n\n",
    "created_at": "2010-02-15T00:09:00Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "cygwin: ratpoints is broken again",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8267",
    "user": "was"
}
```
Assignee: tbd

I just tried building the ratpoints package on Cygwin, and 

```
gcc main.c -o ratpoints -I/home/wstein/build/sage-4.3.3.alpha0/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -L/home/wstein/build/sage-4.3.3.alpha0/local/lib -lgmp -lm -L. -lratpoints                                     
main.c:1: warning: -fPIC ignored for target (all code is position independent)                                             
./libratpoints.a(find_points.o):find_points.c:(.text+0x170): undefined reference to `__imp____gmpz_mul_si' 
BOOM!
```


Thus the fixed that got in from #7015 has been broken before it ever really got to live :-(. 

So this ticket is to implement that fix again. 

Issue created by migration from https://trac.sagemath.org/ticket/8267





---

archive/issue_comments_073178.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-15T00:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8267#issuecomment-73178",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073179.json:
```json
{
    "body": "Please review this:\n\n   http://sage.math.washington.edu/home/wstein/ports/cygwin/ratpoints-2.1.3.p1.spkg",
    "created_at": "2010-02-15T00:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8267#issuecomment-73179",
    "user": "was"
}
```

Please review this:

   http://sage.math.washington.edu/home/wstein/ports/cygwin/ratpoints-2.1.3.p1.spkg



---

archive/issue_comments_073180.json:
```json
{
    "body": "Here are a few changes to William's spkg:\n\n* I renamed it to `ratpoints-2.1.3.p0`, which is the patch level that comes after `ratpoints-2.1.3`.\n* Turned on the executable bits of `spkg-install`.\n* Separate the changelog for `ratpoints-2.1.3.p0` and `ratpoints-2.1.3`. The changelog now reads:\n {{{\n### ratpoints-2.1.3.p0 (William Stein, 14 Feb 2010)\n* Include change to spkg-install so that build works on Cygwin,\n  a fix that was in (trac #7015), and somehow got list.  See\n  trac #8267.\n\n### ratpoints-2.1.3 (William Stein, 14 Feb 2010)\n* Evidently somebody updated ratpoints to 2.1.3 and didn't\n  update the SPKG.txt.  Oops.\n }}}\n\nAn updated spkg with the above changes is available at\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/ratpoint/ratpoints-2.1.3.p0.spkg",
    "created_at": "2010-02-15T05:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8267#issuecomment-73180",
    "user": "mvngu"
}
```

Here are a few changes to William's spkg:

* I renamed it to `ratpoints-2.1.3.p0`, which is the patch level that comes after `ratpoints-2.1.3`.
* Turned on the executable bits of `spkg-install`.
* Separate the changelog for `ratpoints-2.1.3.p0` and `ratpoints-2.1.3`. The changelog now reads:
 {{{
### ratpoints-2.1.3.p0 (William Stein, 14 Feb 2010)
* Include change to spkg-install so that build works on Cygwin,
  a fix that was in (trac #7015), and somehow got list.  See
  trac #8267.

### ratpoints-2.1.3 (William Stein, 14 Feb 2010)
* Evidently somebody updated ratpoints to 2.1.3 and didn't
  update the SPKG.txt.  Oops.
 }}}

An updated spkg with the above changes is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/ratpoint/ratpoints-2.1.3.p0.spkg



---

archive/issue_comments_073181.json:
```json
{
    "body": "The package [ratpoints-2.1.3.p0.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/ratpoint/ratpoints-2.1.3.p0.spkg) includes some cosmetic changes on top of William's spkg. Building ratpoints-2.1.3.p0.spkg went OK on Cygwin (winxp1 on boxen.math).",
    "created_at": "2010-02-16T05:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8267#issuecomment-73181",
    "user": "mvngu"
}
```

The package [ratpoints-2.1.3.p0.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/ratpoint/ratpoints-2.1.3.p0.spkg) includes some cosmetic changes on top of William's spkg. Building ratpoints-2.1.3.p0.spkg went OK on Cygwin (winxp1 on boxen.math).



---

archive/issue_comments_073182.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-16T05:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8267#issuecomment-73182",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073183.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-16T05:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8267#issuecomment-73183",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_073184.json:
```json
{
    "body": "Merged in the standard spkg repository.",
    "created_at": "2010-02-16T05:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8267#issuecomment-73184",
    "user": "mvngu"
}
```

Merged in the standard spkg repository.
