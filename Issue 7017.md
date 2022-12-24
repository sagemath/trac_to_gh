# Issue 7017: prime_range problem

archive/issues_007017.json:
```json
{
    "body": "Assignee: kevin.stueve\n\nCC:  @craigcitro\n\nKeywords: prime_range, primes, prime number theory, prime\n\nI am having trouble with the following lines.  I am on a \nMacBook pro. kevin.stueve\n\nfrom sage.rings.fast_arith import prime_range \nprint prime_range(10<sup>16,10</sup>16+100) \n\nTraceback (most recent call last): \n File \"<stdin>\", line 1, in <module> \n File \"/Users/guestadmin/.sage/sage_notebook/worksheets/admin/3/code/ \n22.py\", \nline 8, in <module> \n   print prime_range(_sage_const_10 **_sage_const_16 ,_sage_const_10 \n**_sage_const_16 +_sage_const_100 ) \n File \"\", line 1, in <module> \n\n File \"fast_arith.pyx\", line 56, in sage.rings.fast_arith.prime_range \n(sage/rings/fast_arith.c:3813) \n File \"fast_arith.pyx\", line 105, in \nsage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3580) \n File \"gen.pyx\", line 8629, in \nsage.libs.pari.gen.PariInstance.primes_up_to_n \n(sage/libs/pari/gen.c:40808) \nOverflowError: long int too large to convert to int\n\n\n\n\nThose two lines gave me a segfault on sage.math: \n\n\n```\n[mvngu@sage ~]$ sage \n---------------------------------------------------------------------- \n---------------------------------------------------------------------- \nsage: from sage.rings.fast_arith import prime_range \nsage: print prime_range(10^16,10^16+100) \n/usr/local/sage/local/bin/sage-sage: line 199:  9892 Segmentation \nfault      sage-ipython \"$@\" -i \n| Sage Version 4.1.1, Release Date: 2009-08-14                       | \n| Type notebook() for the GUI, and license() for information.        | \n```\n\n\nMinh Van Nguyen\n\nIssue created by migration from https://trac.sagemath.org/ticket/7017\n\n",
    "created_at": "2009-09-26T03:16:02Z",
    "labels": [
        "number theory",
        "critical",
        "bug"
    ],
    "title": "prime_range problem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7017",
    "user": "kevin.stueve"
}
```
Assignee: kevin.stueve

CC:  @craigcitro

Keywords: prime_range, primes, prime number theory, prime

I am having trouble with the following lines.  I am on a 
MacBook pro. kevin.stueve

from sage.rings.fast_arith import prime_range 
print prime_range(10<sup>16,10</sup>16+100) 

Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
 File "/Users/guestadmin/.sage/sage_notebook/worksheets/admin/3/code/ 
22.py", 
line 8, in <module> 
   print prime_range(_sage_const_10 **_sage_const_16 ,_sage_const_10 
**_sage_const_16 +_sage_const_100 ) 
 File "", line 1, in <module> 

 File "fast_arith.pyx", line 56, in sage.rings.fast_arith.prime_range 
(sage/rings/fast_arith.c:3813) 
 File "fast_arith.pyx", line 105, in 
sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3580) 
 File "gen.pyx", line 8629, in 
sage.libs.pari.gen.PariInstance.primes_up_to_n 
(sage/libs/pari/gen.c:40808) 
OverflowError: long int too large to convert to int




Those two lines gave me a segfault on sage.math: 


```
[mvngu@sage ~]$ sage 
---------------------------------------------------------------------- 
---------------------------------------------------------------------- 
sage: from sage.rings.fast_arith import prime_range 
sage: print prime_range(10^16,10^16+100) 
/usr/local/sage/local/bin/sage-sage: line 199:  9892 Segmentation 
fault      sage-ipython "$@" -i 
| Sage Version 4.1.1, Release Date: 2009-08-14                       | 
| Type notebook() for the GUI, and license() for information.        | 
```


Minh Van Nguyen

Issue created by migration from https://trac.sagemath.org/ticket/7017





---

archive/issue_comments_058082.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T06:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58082",
    "user": "kevin.stueve"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058083.json:
```json
{
    "body": "I haven't looked closely at the patch. The one quick note I can make is that it looks like a few uses of double-quotes should be changed to backquotes, i.e. everything that should appear as `code`.\n\nMore important to me is the segfault. The problem is this: when I wrote this, I clearly only tested with large input on my 32-bit machine, where I'm getting the same behavior as Kevin -- the code converts the input to an int, which is sufficient to stop overly large input on a 32-bit machine, but fails horribly on a 64-bit machine. I think the segfault is coming from Pari trying to double its stack appropriately, maybe?\n\nThere are a number of easy solutions, but I think the most robust would be to just hardcode an upper bound: if the user asks for a range with one of the parameters larger than our fixed bound, we should just fall back to a different method. The docs already say something about not using this with large input -- we just need to change that to say that it automatically switches algorithms for sufficiently large input. In fact, I think that if we do this, we don't even need the `algorithm` argument to `prime_range` ... Then the only question left is to decide what the bound should be. Just computing the primes in pari for `10^10` takes ~40s on my laptop; maybe `5*10^10` is a reasonable bound? I'm trying `10^11` right now, and my machine isn't loving it ... we should see what a reasonable bound is on, say, sage.math.",
    "created_at": "2010-01-17T08:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58083",
    "user": "@craigcitro"
}
```

I haven't looked closely at the patch. The one quick note I can make is that it looks like a few uses of double-quotes should be changed to backquotes, i.e. everything that should appear as `code`.

More important to me is the segfault. The problem is this: when I wrote this, I clearly only tested with large input on my 32-bit machine, where I'm getting the same behavior as Kevin -- the code converts the input to an int, which is sufficient to stop overly large input on a 32-bit machine, but fails horribly on a 64-bit machine. I think the segfault is coming from Pari trying to double its stack appropriately, maybe?

There are a number of easy solutions, but I think the most robust would be to just hardcode an upper bound: if the user asks for a range with one of the parameters larger than our fixed bound, we should just fall back to a different method. The docs already say something about not using this with large input -- we just need to change that to say that it automatically switches algorithms for sufficiently large input. In fact, I think that if we do this, we don't even need the `algorithm` argument to `prime_range` ... Then the only question left is to decide what the bound should be. Just computing the primes in pari for `10^10` takes ~40s on my laptop; maybe `5*10^10` is a reasonable bound? I'm trying `10^11` right now, and my machine isn't loving it ... we should see what a reasonable bound is on, say, sage.math.



---

archive/issue_comments_058084.json:
```json
{
    "body": "Attachment [7017.patch](tarball://root/attachments/some-uuid/ticket7017/7017.patch) by kevin.stueve created at 2010-01-17 18:25:58\n\nchanged some double quotes to double backquotes",
    "created_at": "2010-01-17T18:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58084",
    "user": "kevin.stueve"
}
```

Attachment [7017.patch](tarball://root/attachments/some-uuid/ticket7017/7017.patch) by kevin.stueve created at 2010-01-17 18:25:58

changed some double quotes to double backquotes



---

archive/issue_comments_058085.json:
```json
{
    "body": "Changed some double quotes to double backquotes.",
    "created_at": "2010-01-17T18:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58085",
    "user": "kevin.stueve"
}
```

Changed some double quotes to double backquotes.



---

archive/issue_comments_058086.json:
```json
{
    "body": "On my atom netbook with 1GB RAM I can't even use prime_range near 4*10**8 (and my virtual memory was thrashing for 3*10**8).  I don't think a hard-coded limit is appropriate if what values are possible depends on how much RAM is available (should the limit be configurable?).\n\nSebastian Pancratz suggested having the algorithm default be None, which would cause the algorithm to be automatically chosen.\n\nYes, it would be better if it automatically selected the appropriate algorithm for the input.\n\nAt a minimum, when prime_range with pari_primes fails, a message should be printed saying that the other algorithm is available.  Unfortunately assuming the user will read the doc string when a function fails is not realistic.\n\nThe patch I made also includes fixing a typo in a doc string in line 8605 (primes_up_to_n) of gen.pyx in the sage pari lib.\n\nCurrently prime_range in fast_arith.pyx calls primes_up_to_n in gen.pyx, which calls pari(n).primepi().  I think this should be replaced with Sage's prime_pi, which is faster and works for larger input.\n\nAnother bug, regarding Sage trac.  I put the traceback in a special box.  Yet this text above does not wrap.  This text above should still be word wrapped.\n\n\n```\nsage: prime_range(10**10,10**10+100)\n---------------------------------------------------------------------------\nOverflowError                             Traceback (most recent call last)\n\n/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/devel/sage-ticket_7017/<ipython console> in <module>()\n\n/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3968)()\n\n/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3640)()\n\n/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.PariInstance.primes_up_to_n (sage/libs/pari/gen.c:40686)()\n\nOverflowError: long int too large to convert to int\nsage: prime_range(4*10**8,4*10**8+100)\n---------------------------------------------------------------------------\nPariError                                 Traceback (most recent call last)\n\n/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/devel/sage-ticket_7017/<ipython console> in <module>()\n\n/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3968)()\n\n/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3640)()\n\n/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.PariInstance.primes_up_to_n (sage/libs/pari/gen.c:40789)()\n\n/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44110)()\n\nPariError: length (lg) overflow (26)\nsage: prime_range(3*10**8,3*10**8+100)\n[300000007, 300000031, 300000047, 300000089]\n```\n",
    "created_at": "2010-01-17T19:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58086",
    "user": "kevin.stueve"
}
```

On my atom netbook with 1GB RAM I can't even use prime_range near 4*10**8 (and my virtual memory was thrashing for 3*10**8).  I don't think a hard-coded limit is appropriate if what values are possible depends on how much RAM is available (should the limit be configurable?).

Sebastian Pancratz suggested having the algorithm default be None, which would cause the algorithm to be automatically chosen.

Yes, it would be better if it automatically selected the appropriate algorithm for the input.

At a minimum, when prime_range with pari_primes fails, a message should be printed saying that the other algorithm is available.  Unfortunately assuming the user will read the doc string when a function fails is not realistic.

The patch I made also includes fixing a typo in a doc string in line 8605 (primes_up_to_n) of gen.pyx in the sage pari lib.

Currently prime_range in fast_arith.pyx calls primes_up_to_n in gen.pyx, which calls pari(n).primepi().  I think this should be replaced with Sage's prime_pi, which is faster and works for larger input.

Another bug, regarding Sage trac.  I put the traceback in a special box.  Yet this text above does not wrap.  This text above should still be word wrapped.


```
sage: prime_range(10**10,10**10+100)
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/devel/sage-ticket_7017/<ipython console> in <module>()

/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3968)()

/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3640)()

/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.PariInstance.primes_up_to_n (sage/libs/pari/gen.c:40686)()

OverflowError: long int too large to convert to int
sage: prime_range(4*10**8,4*10**8+100)
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/devel/sage-ticket_7017/<ipython console> in <module>()

/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3968)()

/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/rings/fast_arith.so in sage.rings.fast_arith.prime_range (sage/rings/fast_arith.c:3640)()

/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.PariInstance.primes_up_to_n (sage/libs/pari/gen.c:40789)()

/home/kstueve/Desktop/sage-4.3-ubuntu9.10-AtomN270-i686-Linux/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44110)()

PariError: length (lg) overflow (26)
sage: prime_range(3*10**8,3*10**8+100)
[300000007, 300000031, 300000047, 300000089]
```




---

archive/issue_comments_058087.json:
```json
{
    "body": "My attachment description is incomplete.  I accidentally overwrote my old description.",
    "created_at": "2010-01-18T07:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58087",
    "user": "kevin.stueve"
}
```

My attachment description is incomplete.  I accidentally overwrote my old description.



---

archive/issue_comments_058088.json:
```json
{
    "body": "I should construct ValueError(somestring), for Python 3 compatibility.",
    "created_at": "2010-01-18T07:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58088",
    "user": "kevin.stueve"
}
```

I should construct ValueError(somestring), for Python 3 compatibility.



---

archive/issue_comments_058089.json:
```json
{
    "body": "Adds some docstring formatting and does a little Python 3 preparation.",
    "created_at": "2010-01-18T07:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58089",
    "user": "@TimDumol"
}
```

Adds some docstring formatting and does a little Python 3 preparation.



---

archive/issue_comments_058090.json:
```json
{
    "body": "Attachment [trac_7017-referee.patch](tarball://root/attachments/some-uuid/ticket7017/trac_7017-referee.patch) by @TimDumol created at 2010-01-18 07:48:23\n\nGood job. Looks good to me. This referee patch does a little bit of formatting tweaks. Please feel free to review or ignore the patch.",
    "created_at": "2010-01-18T07:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58090",
    "user": "@TimDumol"
}
```

Attachment [trac_7017-referee.patch](tarball://root/attachments/some-uuid/ticket7017/trac_7017-referee.patch) by @TimDumol created at 2010-01-18 07:48:23

Good job. Looks good to me. This referee patch does a little bit of formatting tweaks. Please feel free to review or ignore the patch.



---

archive/issue_comments_058091.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T07:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58091",
    "user": "@TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058092.json:
```json
{
    "body": "So I'm happy for the code with the alternate algorithm to go in -- but it doesn't seem to address the segfault mentioned in the description. I'm happy to fix that soon, but can someone open a new ticket for it so we don't forget? \n\nAlso, unless I'm missing something, the second hunk in the referee patch seems erroneous. I like the referee patch otherwise -- pretty documentation is always great. :)\n\nKevin: for the record, we put human-readable names in Author: and Reviewer:, not trac usernames. (Did William review this, or was he intending to?)",
    "created_at": "2010-01-18T08:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58092",
    "user": "@craigcitro"
}
```

So I'm happy for the code with the alternate algorithm to go in -- but it doesn't seem to address the segfault mentioned in the description. I'm happy to fix that soon, but can someone open a new ticket for it so we don't forget? 

Also, unless I'm missing something, the second hunk in the referee patch seems erroneous. I like the referee patch otherwise -- pretty documentation is always great. :)

Kevin: for the record, we put human-readable names in Author: and Reviewer:, not trac usernames. (Did William review this, or was he intending to?)



---

archive/issue_comments_058093.json:
```json
{
    "body": "Attachment [trac_7017-referee.2.patch](tarball://root/attachments/some-uuid/ticket7017/trac_7017-referee.2.patch) by @TimDumol created at 2010-01-18 08:16:19\n\nFixes a transposed word. Apply this referee patch on top of original patch (7017.patch)",
    "created_at": "2010-01-18T08:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58093",
    "user": "@TimDumol"
}
```

Attachment [trac_7017-referee.2.patch](tarball://root/attachments/some-uuid/ticket7017/trac_7017-referee.2.patch) by @TimDumol created at 2010-01-18 08:16:19

Fixes a transposed word. Apply this referee patch on top of original patch (7017.patch)



---

archive/issue_comments_058094.json:
```json
{
    "body": "Sorry about that. Here's the fix.",
    "created_at": "2010-01-18T08:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58094",
    "user": "@TimDumol"
}
```

Sorry about that. Here's the fix.



---

archive/issue_comments_058095.json:
```json
{
    "body": "Positive review on Tim's patch.  Great job!",
    "created_at": "2010-01-18T08:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58095",
    "user": "kevin.stueve"
}
```

Positive review on Tim's patch.  Great job!



---

archive/issue_comments_058096.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T01:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58096",
    "user": "@rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_058097.json:
```json
{
    "body": "Attachment [trac_7017-ref3.patch](tarball://root/attachments/some-uuid/ticket7017/trac_7017-ref3.patch) by @rlmill created at 2010-01-19 01:14:26",
    "created_at": "2010-01-19T01:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58097",
    "user": "@rlmill"
}
```

Attachment [trac_7017-ref3.patch](tarball://root/attachments/some-uuid/ticket7017/trac_7017-ref3.patch) by @rlmill created at 2010-01-19 01:14:26



---

archive/issue_comments_058098.json:
```json
{
    "body": "It looks like this ticket was closed without resolving the segfault issue. I suppose that is valid because that issue is still open at #5943?",
    "created_at": "2011-06-18T13:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7017#issuecomment-58098",
    "user": "@kedlaya"
}
```

It looks like this ticket was closed without resolving the segfault issue. I suppose that is valid because that issue is still open at #5943?
