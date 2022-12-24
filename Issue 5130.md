# Issue 5130: [with patch; not ready for review] create a prime_pi function that doesn't just compute len(prime_range(n))

archive/issues_005130.json:
```json
{
    "body": "Assignee: was\n\nThe goal of this ticket is to make something eventually competitive with Mathematica's PrimePi.  The first version won't do that, but it is a step in the right direction. \n\nNote that evidently the only program we know of with a fast prime_pi is Mathematica (pari, maple, etc., -- none of them have anything at all).  In contract, Mathematica can do PrimePi[10^14] in \"about a minute\", but the algorithm there doesn't allow larger input.\n\n\n```\nIn[11]:= Timing[PrimePi[ 10^13 + 10^8 +10^9]]\nOut[11]= {12., 346102281239}\n\nIn[13]:= Timing[PrimePi[10^14]]\nOut[13]= {59.53, 3204941750802}\n```\n\n\nThe attached code did `10^14` in just under an hour.   The issue is that Mathematica implements a different sublinear algorithm.\n\nIn Sage, with extra storage usage:\n\n```\nsage: k = 10^13\nsage: time print prime_pi(k,40)\n346065536839\nTime: CPU 219.44 s, Wall: 219.44 s\n```\n\n\nSo for that one mathematica is 18 times faster.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5130\n\n",
    "created_at": "2009-01-29T21:41:56Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "[with patch; not ready for review] create a prime_pi function that doesn't just compute len(prime_range(n))",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5130",
    "user": "was"
}
```
Assignee: was

The goal of this ticket is to make something eventually competitive with Mathematica's PrimePi.  The first version won't do that, but it is a step in the right direction. 

Note that evidently the only program we know of with a fast prime_pi is Mathematica (pari, maple, etc., -- none of them have anything at all).  In contract, Mathematica can do PrimePi[10^14] in "about a minute", but the algorithm there doesn't allow larger input.


```
In[11]:= Timing[PrimePi[ 10^13 + 10^8 +10^9]]
Out[11]= {12., 346102281239}

In[13]:= Timing[PrimePi[10^14]]
Out[13]= {59.53, 3204941750802}
```


The attached code did `10^14` in just under an hour.   The issue is that Mathematica implements a different sublinear algorithm.

In Sage, with extra storage usage:

```
sage: k = 10^13
sage: time print prime_pi(k,40)
346065536839
Time: CPU 219.44 s, Wall: 219.44 s
```


So for that one mathematica is 18 times faster.

Issue created by migration from https://trac.sagemath.org/ticket/5130





---

archive/issue_comments_039210.json:
```json
{
    "body": "Hi Andrew,\n\nI think the code looks pretty good.  There are two things that I'd like to see added before it goes into Sage.\n\n1. Could you add a reference for the algorithm being used?  As part of this, could you add docstrings to the two cdef functions briefly describing their purpose / maybe relating them to the algorithm in the reference?\n\n2. Could you make a note about whether or not we'll run into any issues with integer overflows or numerical accuracy as the code uses floating point arithmetic (sqrt).\n\n--Mike",
    "created_at": "2009-01-30T01:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39210",
    "user": "mhansen"
}
```

Hi Andrew,

I think the code looks pretty good.  There are two things that I'd like to see added before it goes into Sage.

1. Could you add a reference for the algorithm being used?  As part of this, could you add docstrings to the two cdef functions briefly describing their purpose / maybe relating them to the algorithm in the reference?

2. Could you make a note about whether or not we'll run into any issues with integer overflows or numerical accuracy as the code uses floating point arithmetic (sqrt).

--Mike



---

archive/issue_comments_039211.json:
```json
{
    "body": "The algorithm used is Legendre's formula, it has been around for quite a while, so there are many references on it. I used as a reference Hans Riesel's Prime \"Numbers and Computer Methods for Factorization\".\n\n--Andrew",
    "created_at": "2009-01-30T02:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39211",
    "user": "ohanar"
}
```

The algorithm used is Legendre's formula, it has been around for quite a while, so there are many references on it. I used as a reference Hans Riesel's Prime "Numbers and Computer Methods for Factorization".

--Andrew



---

archive/issue_comments_039212.json:
```json
{
    "body": "By the way, it looks easy to replace a lot of the sqrt's, and to double-check the others.  You can replace a<=sqrt(b) with a*a<=b.  For the others, if you have\n  a=<long long>sqrt(b)\nyou can follow it with:\n  if a*a > b or (a+1)*(a+1) <= b: raise an exception",
    "created_at": "2009-01-30T02:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39212",
    "user": "cwitty"
}
```

By the way, it looks easy to replace a lot of the sqrt's, and to double-check the others.  You can replace a<=sqrt(b) with a*a<=b.  For the others, if you have
  a=<long long>sqrt(b)
you can follow it with:
  if a*a > b or (a+1)*(a+1) <= b: raise an exception



---

archive/issue_comments_039213.json:
```json
{
    "body": "Andrew -- We're having a lot of trouble porting wise with code that uses sqrtl.  This code needs to be slightly rewritten to not use it.   \n\nThe sqrt must be rewritten to either use gmp directly or just use the normal sage Python sqrt, which hopefully won't be much slower for this application.",
    "created_at": "2009-02-03T04:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39213",
    "user": "was"
}
```

Andrew -- We're having a lot of trouble porting wise with code that uses sqrtl.  This code needs to be slightly rewritten to not use it.   

The sqrt must be rewritten to either use gmp directly or just use the normal sage Python sqrt, which hopefully won't be much slower for this application.



---

archive/issue_comments_039214.json:
```json
{
    "body": "It is not \"trouble porting wise\", it is that long double functions are not guaranteed by the C99 standard to have any more precision that the double version of the same function. cwitty pointed out that also double and float implementations commonly return the same result, so if you want guaranteed results use gmp or mpfr - everything else plainly sucks.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T04:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39214",
    "user": "mabshoff"
}
```

It is not "trouble porting wise", it is that long double functions are not guaranteed by the C99 standard to have any more precision that the double version of the same function. cwitty pointed out that also double and float implementations commonly return the same result, so if you want guaranteed results use gmp or mpfr - everything else plainly sucks.

Cheers,

Michael



---

archive/issue_comments_039215.json:
```json
{
    "body": "The following lines from your update are highly disturbing.\n\n\n```\n\t104\t        cdef long long m_max = <long long> sqrtl(x) + 1 \n \t105\t        while (m_max-1)*(m_max-1) > x or m_max*m_max <= x: \n \t106\t            m_max = <long long> sqrtl(x) + 1\n```\n\n\nFactoring out some noise, this simplifies to:\n\n\n```\na = b\nwhile x:\n   a = b\n```\n\n\nwhere a,b, and x will *NEVER* change *AT ALL* during the execution of the code.  So if you ever enter the while loop, boom.",
    "created_at": "2009-02-06T19:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39215",
    "user": "boothby"
}
```

The following lines from your update are highly disturbing.


```
	104	        cdef long long m_max = <long long> sqrtl(x) + 1 
 	105	        while (m_max-1)*(m_max-1) > x or m_max*m_max <= x: 
 	106	            m_max = <long long> sqrtl(x) + 1
```


Factoring out some noise, this simplifies to:


```
a = b
while x:
   a = b
```


where a,b, and x will *NEVER* change *AT ALL* during the execution of the code.  So if you ever enter the while loop, boom.



---

archive/issue_comments_039216.json:
```json
{
    "body": "> The following lines from your update are highly disturbing.\n\nI only looked at this for a second, but I suspect you're reasoning as if the numbers satisfied laws such as commutative, associativity etc.; probably the whole point is they might not since they are just floating point approximations.",
    "created_at": "2009-02-06T19:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39216",
    "user": "was"
}
```

> The following lines from your update are highly disturbing.

I only looked at this for a second, but I suspect you're reasoning as if the numbers satisfied laws such as commutative, associativity etc.; probably the whole point is they might not since they are just floating point approximations.



---

archive/issue_comments_039217.json:
```json
{
    "body": "No, boothby is right.  There's no commutativity, associativity, etc. involved here.  The only floating point at all is in `<long long>sqrtl(x)`, and that certainly ought to give the exact same result every time you call it on any particular platform (although the results from one platform to another certainly might differ).",
    "created_at": "2009-02-06T21:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39217",
    "user": "cwitty"
}
```

No, boothby is right.  There's no commutativity, associativity, etc. involved here.  The only floating point at all is in `<long long>sqrtl(x)`, and that certainly ought to give the exact same result every time you call it on any particular platform (although the results from one platform to another certainly might differ).



---

archive/issue_comments_039218.json:
```json
{
    "body": "this is rebased against 3.4.alpha0 *and* it implements sqrt for long and long long using double and float code from Bill Hart",
    "created_at": "2009-03-03T23:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39218",
    "user": "was"
}
```

this is rebased against 3.4.alpha0 *and* it implements sqrt for long and long long using double and float code from Bill Hart



---

archive/issue_comments_039219.json:
```json
{
    "body": "Attachment [trac_5130-final.patch](tarball://root/attachments/some-uuid/ticket5130/trac_5130-final.patch) by was created at 2009-03-03 23:10:26",
    "created_at": "2009-03-03T23:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39219",
    "user": "was"
}
```

Attachment [trac_5130-final.patch](tarball://root/attachments/some-uuid/ticket5130/trac_5130-final.patch) by was created at 2009-03-03 23:10:26



---

archive/issue_comments_039220.json:
```json
{
    "body": "It would be good to include a reference to the algorithm, and perhaps a bit more documentation in the code itself. For example, what is mem_mult or m_max? \n\nMaybe a the docstring should have an example of computing len(prime_range(...)) to show more explicitly what it's computing. \n\nThe second line of `prime_phi_large`, no need to write `long(N)`, just write N. \n\nI'm not sure what's going on here, but it's not deterministic. \n\n\n```\nsage: for n in range(90000, 100000, 3):\n....:     if prime_pi(n) != len(prime_range(n+1)):\n....:         print n, prime_pi(n), len(prime_range(n+1));\n....:         \n91587 8855 8855\n91848 8878 8875\n92112 8899 8896\n92373 8924 8921\n92376 8921 8921\n92637 8947 8945\n92901 8979 8976\n92904 8976 8976\n93171 8999 8999\n...\n```\n\n\n(This is on an OS X 10.4 intel.)",
    "created_at": "2009-03-18T04:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39220",
    "user": "robertwb"
}
```

It would be good to include a reference to the algorithm, and perhaps a bit more documentation in the code itself. For example, what is mem_mult or m_max? 

Maybe a the docstring should have an example of computing len(prime_range(...)) to show more explicitly what it's computing. 

The second line of `prime_phi_large`, no need to write `long(N)`, just write N. 

I'm not sure what's going on here, but it's not deterministic. 


```
sage: for n in range(90000, 100000, 3):
....:     if prime_pi(n) != len(prime_range(n+1)):
....:         print n, prime_pi(n), len(prime_range(n+1));
....:         
91587 8855 8855
91848 8878 8875
92112 8899 8896
92373 8924 8921
92376 8921 8921
92637 8947 8945
92901 8979 8976
92904 8976 8976
93171 8999 8999
...
```


(This is on an OS X 10.4 intel.)



---

archive/issue_comments_039221.json:
```json
{
    "body": "this is rebased against 3.4 and should now be deterministic",
    "created_at": "2009-04-13T14:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39221",
    "user": "ohanar"
}
```

this is rebased against 3.4 and should now be deterministic



---

archive/issue_comments_039222.json:
```json
{
    "body": "Attachment [trac_5130-final.2.patch](tarball://root/attachments/some-uuid/ticket5130/trac_5130-final.2.patch) by was created at 2009-04-14 22:43:03\n\nrebased against 3.4.1.rc2",
    "created_at": "2009-04-14T22:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39222",
    "user": "was"
}
```

Attachment [trac_5130-final.2.patch](tarball://root/attachments/some-uuid/ticket5130/trac_5130-final.2.patch) by was created at 2009-04-14 22:43:03

rebased against 3.4.1.rc2



---

archive/issue_comments_039223.json:
```json
{
    "body": "Attachment [trac_5130-rebased.patch](tarball://root/attachments/some-uuid/ticket5130/trac_5130-rebased.patch) by was created at 2009-04-14 22:43:18",
    "created_at": "2009-04-14T22:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39223",
    "user": "was"
}
```

Attachment [trac_5130-rebased.patch](tarball://root/attachments/some-uuid/ticket5130/trac_5130-rebased.patch) by was created at 2009-04-14 22:43:18



---

archive/issue_comments_039224.json:
```json
{
    "body": "Major issue: it needs to raise an exception on an invalid mem_mult, instead of giving the wrong answer:\n\n```\nsage: prime_pi(10^6)\n78498\nsage: prime_pi(10^6, 0)\n228574\n```\n\n\nMinor issues:\n`allows for use of addition memory` should be `allows for the use of additional memory`\n\nIt looks like the function bisect() is doing some variant on binary search; but it's not the standard algorithm, which makes it harder to understand and review.  Maybe it should be replaced with a real binary search (for example, following the flowchart from http://en.wikipedia.org/wiki/Binary_search).\n\nNote that I've read the code and performed lots of tests (against len(prime_range(n)) for small n, and against Mathematica for n around 2<sup>39</sup>), but I don't understand the algorithm.  With this caveat, I'd be willing to give it a positive review if the major wrong-answer issue were fixed (although fixing the minor issues too would be better, of course).",
    "created_at": "2009-04-15T04:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39224",
    "user": "cwitty"
}
```

Major issue: it needs to raise an exception on an invalid mem_mult, instead of giving the wrong answer:

```
sage: prime_pi(10^6)
78498
sage: prime_pi(10^6, 0)
228574
```


Minor issues:
`allows for use of addition memory` should be `allows for the use of additional memory`

It looks like the function bisect() is doing some variant on binary search; but it's not the standard algorithm, which makes it harder to understand and review.  Maybe it should be replaced with a real binary search (for example, following the flowchart from http://en.wikipedia.org/wiki/Binary_search).

Note that I've read the code and performed lots of tests (against len(prime_range(n)) for small n, and against Mathematica for n around 2<sup>39</sup>), but I don't understand the algorithm.  With this caveat, I'd be willing to give it a positive review if the major wrong-answer issue were fixed (although fixing the minor issues too would be better, of course).



---

archive/issue_comments_039225.json:
```json
{
    "body": "rebased against 3.4.1.rc2 and fixes the issues raised by cwitty",
    "created_at": "2009-04-15T10:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39225",
    "user": "ohanar"
}
```

rebased against 3.4.1.rc2 and fixes the issues raised by cwitty



---

archive/issue_comments_039226.json:
```json
{
    "body": "Attachment [trac_5130-rebased.2.patch](tarball://root/attachments/some-uuid/ticket5130/trac_5130-rebased.2.patch) by ohanar created at 2009-04-15 10:14:50",
    "created_at": "2009-04-15T10:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39226",
    "user": "ohanar"
}
```

Attachment [trac_5130-rebased.2.patch](tarball://root/attachments/some-uuid/ticket5130/trac_5130-rebased.2.patch) by ohanar created at 2009-04-15 10:14:50



---

archive/issue_comments_039227.json:
```json
{
    "body": "Code looks good, doctests pass.  I still don't understand the algorithm, but I'm giving it a positive review anyway.",
    "created_at": "2009-04-18T15:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39227",
    "user": "cwitty"
}
```

Code looks good, doctests pass.  I still don't understand the algorithm, but I'm giving it a positive review anyway.



---

archive/issue_comments_039228.json:
```json
{
    "body": "Well, I am not too happy that there are special long long sqrt() work around function in this file. Since the code is by Bill I think they should be somewhat reliable and they seems to detect numerical precision issues, but I still do not trust them to work reliably, i.e. Sparc. \n\nAnyway, I would like them to be moved to its own file and I would like to see a test that compares and verifies their output for a wide range of inputs against MPFR for example. Even nicer would be the ability to switch away from this function and use MPFR functionality in its place. This is not something that will prevent this code from going in unless the current doctests will get broken on something like Sparc/Solaris where I have detected problems with the number_of_partitions() test that also relies on some sqrtl() function. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-21T23:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39228",
    "user": "mabshoff"
}
```

Well, I am not too happy that there are special long long sqrt() work around function in this file. Since the code is by Bill I think they should be somewhat reliable and they seems to detect numerical precision issues, but I still do not trust them to work reliably, i.e. Sparc. 

Anyway, I would like them to be moved to its own file and I would like to see a test that compares and verifies their output for a wide range of inputs against MPFR for example. Even nicer would be the ability to switch away from this function and use MPFR functionality in its place. This is not something that will prevent this code from going in unless the current doctests will get broken on something like Sparc/Solaris where I have detected problems with the number_of_partitions() test that also relies on some sqrtl() function. 

Cheers,

Michael



---

archive/issue_comments_039229.json:
```json
{
    "body": "I wouldn't worry about the correctness/portability of sqrt_longlong.  It uses sqrt() (not sqrtl()), which is exactly specified by IEEE floating point (no room for implementation differences in the spec), so it should be portable; and it has a built-in self-test, so if something goes wrong we'll get exceptions.",
    "created_at": "2009-04-22T00:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39229",
    "user": "cwitty"
}
```

I wouldn't worry about the correctness/portability of sqrt_longlong.  It uses sqrt() (not sqrtl()), which is exactly specified by IEEE floating point (no room for implementation differences in the spec), so it should be portable; and it has a built-in self-test, so if something goes wrong we'll get exceptions.



---

archive/issue_comments_039230.json:
```json
{
    "body": "Replying to [comment:19 cwitty]:\n> I wouldn't worry about the correctness/portability of sqrt_longlong.  It uses sqrt() (not sqrtl()),\n\nYes, I know. I complained initially about sqrtl() in one of the early patches which was the reason long long sqrt() was defined. \n\n>  which is exactly specified by IEEE floating point (no room for implementation differences in the spec), so it should be portable; and it has a built-in self-test, so if something goes wrong we'll get exceptions.\n\nI think my points still stand, i.e.\n \n* There is no reason for the long long sqrt() to be in this file since it will come in useful in some other places, i.e. the number_of_partitions() code since that code currently fails doctests on Sparc/Solaris (it might be completely unrelated to sqrtl(), but as it the code does not compile on FreeBSD 8 due to the use of sqrtl() there)\n* There should be some extensive testing done for that function. I am sure someone using the function and getting back some error message will not be happy that an error was detected, but complain and not see the advantage of detecting the issue in the first place :)\n* If some doctest here fails on Sparc/Solaris for example I will not merge this patch since I don't need any more bugs introduced that in the end someone else (i.e. William or me has to fix). Some of the fixes took a long, long time to hunt down (and we are still not done **now**), so the attitude that someone else will clean up such a mess is not something I am willing to accept, not that any person involved in this ticket has this attitude ;). \n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T00:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39230",
    "user": "mabshoff"
}
```

Replying to [comment:19 cwitty]:
> I wouldn't worry about the correctness/portability of sqrt_longlong.  It uses sqrt() (not sqrtl()),

Yes, I know. I complained initially about sqrtl() in one of the early patches which was the reason long long sqrt() was defined. 

>  which is exactly specified by IEEE floating point (no room for implementation differences in the spec), so it should be portable; and it has a built-in self-test, so if something goes wrong we'll get exceptions.

I think my points still stand, i.e.
 
* There is no reason for the long long sqrt() to be in this file since it will come in useful in some other places, i.e. the number_of_partitions() code since that code currently fails doctests on Sparc/Solaris (it might be completely unrelated to sqrtl(), but as it the code does not compile on FreeBSD 8 due to the use of sqrtl() there)
* There should be some extensive testing done for that function. I am sure someone using the function and getting back some error message will not be happy that an error was detected, but complain and not see the advantage of detecting the issue in the first place :)
* If some doctest here fails on Sparc/Solaris for example I will not merge this patch since I don't need any more bugs introduced that in the end someone else (i.e. William or me has to fix). Some of the fixes took a long, long time to hunt down (and we are still not done **now**), so the attitude that someone else will clean up such a mess is not something I am willing to accept, not that any person involved in this ticket has this attitude ;). 

Cheers,

Michael



---

archive/issue_comments_039231.json:
```json
{
    "body": "Hi,\n\nI did extensive testing comparing Solaris/Sparc with Linux x86-64, tried to break it some other way, but I failed :). It also builds fine on Solaris 10.\n\nOne question: What is the credit situation here?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T22:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39231",
    "user": "mabshoff"
}
```

Hi,

I did extensive testing comparing Solaris/Sparc with Linux x86-64, tried to break it some other way, but I failed :). It also builds fine on Solaris 10.

One question: What is the credit situation here?

Cheers,

Michael



---

archive/issue_comments_039232.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T22:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39232",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_039233.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-22T22:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5130#issuecomment-39233",
    "user": "mabshoff"
}
```

Resolution: fixed
