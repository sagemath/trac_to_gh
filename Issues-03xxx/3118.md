# Issue 3118: [with new patch, positive review] update LCM (easy-to-fix buglet)

archive/issues_003118.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @JohnCremona\n\n```\n\n\nOn Tue, May 6, 2008 at 8:49 PM, schmmd <schmmd@gmail.com> wrote:\n> \n>  lcm? gives the following output:\n>  \n>  Type:           function\n>  Base Class:     <type 'function'>\n>  String Form:    <function lcm at 0x879087c>\n>  Namespace:      Interactive\n>  File:           /home/michael/downloads/sage-3.0/local/lib/python2.5/\n>  site-packages/sage/rings/arith.py\n>  Definition:     lcm(a, b=None, integer=False)\n>  Docstring:\n>  \n>         The least common multiple of a and b, or if a is a list and b\n>  is\n>         omitted the least common multiple of all elements of a.\n>  \n>         NOTE: Use integer=True to make this vastly faster if you are\n>         working with lists of integers.\n>  \n>         INPUT:\n>             a -- number\n>             b -- number (optional)\n>             integer -- (default: False); if True, do an integer LCM\n>         or\n>   *           a -- vector\n>             integer -- (default: False); if True, do an integer LCM\n>                 NOTE -- this is *vastly* faster than doing the generic\n>  LCM\n>  \n>  Note the starred line.  I believe that the lcm method takes a list and\n>  not a vector.  At least, I seem to get errors when I pass a vector.\n>  \n>  \n\nI fully agree that this is a bug.\n\nIncidentally I wrote the LCM function a while before I implemented vectors,\nso I think when I wrote those docs \"vector\" and \"list\" were the same\nthing in my mind.  \n\nThe fix should be to change the docs to replace \"vector\" by any itterable.\nThen the LCM code should iterate over the object calling LCM \nif it doesn't have an LCM method.   \n\nProbably similar fixes need to be made for GCD.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3118\n\n",
    "closed_at": "2008-10-25T22:41:19Z",
    "created_at": "2008-05-07T04:00:56Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with new patch, positive review] update LCM (easy-to-fix buglet)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3118",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

CC:  @JohnCremona

```


On Tue, May 6, 2008 at 8:49 PM, schmmd <schmmd@gmail.com> wrote:
> 
>  lcm? gives the following output:
>  
>  Type:           function
>  Base Class:     <type 'function'>
>  String Form:    <function lcm at 0x879087c>
>  Namespace:      Interactive
>  File:           /home/michael/downloads/sage-3.0/local/lib/python2.5/
>  site-packages/sage/rings/arith.py
>  Definition:     lcm(a, b=None, integer=False)
>  Docstring:
>  
>         The least common multiple of a and b, or if a is a list and b
>  is
>         omitted the least common multiple of all elements of a.
>  
>         NOTE: Use integer=True to make this vastly faster if you are
>         working with lists of integers.
>  
>         INPUT:
>             a -- number
>             b -- number (optional)
>             integer -- (default: False); if True, do an integer LCM
>         or
>   *           a -- vector
>             integer -- (default: False); if True, do an integer LCM
>                 NOTE -- this is *vastly* faster than doing the generic
>  LCM
>  
>  Note the starred line.  I believe that the lcm method takes a list and
>  not a vector.  At least, I seem to get errors when I pass a vector.
>  
>  

I fully agree that this is a bug.

Incidentally I wrote the LCM function a while before I implemented vectors,
so I think when I wrote those docs "vector" and "list" were the same
thing in my mind.  

The fix should be to change the docs to replace "vector" by any itterable.
Then the LCM code should iterate over the object calling LCM 
if it doesn't have an LCM method.   

Probably similar fixes need to be made for GCD.
```

Issue created by migration from https://trac.sagemath.org/ticket/3118





---

archive/issue_comments_021537.json:
```json
{
    "body": "Attachment [trac_3118_gcd.patch](tarball://root/attachments/some-uuid/ticket3118/trac_3118_gcd.patch) by @zimmermann6 created at 2008-10-19 13:34:50",
    "created_at": "2008-10-19T13:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21537",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_3118_gcd.patch](tarball://root/attachments/some-uuid/ticket3118/trac_3118_gcd.patch) by @zimmermann6 created at 2008-10-19 13:34:50



---

archive/issue_comments_021538.json:
```json
{
    "body": "Both attachments fix that problem. Btw, I wonder why integer=True is not the default,\nat least for integer inputs. I guess there are many calls to gcd with integers in the\nSage library without Integer=True:\n\n```\nbash-3.00$ pwd\n/usr/local/sage-3.1.4/sage/devel/sage/sage\nbash-3.00$ find . -type f -name \"*.py\" -exec grep \\-iw GCD {} \\; | wc -l\n297\n```",
    "created_at": "2008-10-19T13:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21538",
    "user": "https://github.com/zimmermann6"
}
```

Both attachments fix that problem. Btw, I wonder why integer=True is not the default,
at least for integer inputs. I guess there are many calls to gcd with integers in the
Sage library without Integer=True:

```
bash-3.00$ pwd
/usr/local/sage-3.1.4/sage/devel/sage/sage
bash-3.00$ find . -type f -name "*.py" -exec grep \-iw GCD {} \; | wc -l
297
```



---

archive/issue_comments_021539.json:
```json
{
    "body": "Attachment [sage-trac_3118.patch](tarball://root/attachments/some-uuid/ticket3118/sage-trac_3118.patch) by @JohnCremona created at 2008-10-21 21:54:00\n\nMy patch applies _instead_ of the previous two.  It implements Paul's suggested behaviour.\n\nThere's one problem left (I tested all of sage.rings and had to make one change in the multiploynomial polynomial code which actually used the integers=True flag which is now redundant).  But:\n\n```\nsage: P.<x,y,z> = ZZ[]\nsage: gcd(2*(x+y),3*y)\n2\n```\nwhich of course should give 1.  This leads to one doctest failure, but I cannot track it down at the moment.\n\nI (or someone) should also doctest all the rest of Sage as there are ceratinly places where gcd/lcm are used outside of sage/rings.",
    "created_at": "2008-10-21T21:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21539",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [sage-trac_3118.patch](tarball://root/attachments/some-uuid/ticket3118/sage-trac_3118.patch) by @JohnCremona created at 2008-10-21 21:54:00

My patch applies _instead_ of the previous two.  It implements Paul's suggested behaviour.

There's one problem left (I tested all of sage.rings and had to make one change in the multiploynomial polynomial code which actually used the integers=True flag which is now redundant).  But:

```
sage: P.<x,y,z> = ZZ[]
sage: gcd(2*(x+y),3*y)
2
```
which of course should give 1.  This leads to one doctest failure, but I cannot track it down at the moment.

I (or someone) should also doctest all the rest of Sage as there are ceratinly places where gcd/lcm are used outside of sage/rings.



---

archive/issue_comments_021540.json:
```json
{
    "body": "Apply after previous one",
    "created_at": "2008-10-22T14:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21540",
    "user": "https://github.com/JohnCremona"
}
```

Apply after previous one



---

archive/issue_comments_021541.json:
```json
{
    "body": "Attachment [sage-trac_3118-2.patch](tarball://root/attachments/some-uuid/ticket3118/sage-trac_3118-2.patch) by @JohnCremona created at 2008-10-22 14:20:13\n\nThe second patch does three things:\n\n1. After running -testall a couple of small things elsewhere needed fixing;\n2. Fixed a bug in integer.pyx introduced in 3.1.2.alpha0 (in #4286)\n3. Cleaner use of sequences as a method of coercing a list to have a coherent universe.\n\nIn view of item 2, which corrected this:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.2.alpha0, Release Date: 2008-10-20                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage.rings.integer.GCD_list([2,2,3])\n2\n```\nand the fact that I really did do a -testall, I am hoping for a quick positive review!  I think that Paul Z is eligible to do that although the initial patches here were his.",
    "created_at": "2008-10-22T14:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21541",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [sage-trac_3118-2.patch](tarball://root/attachments/some-uuid/ticket3118/sage-trac_3118-2.patch) by @JohnCremona created at 2008-10-22 14:20:13

The second patch does three things:

1. After running -testall a couple of small things elsewhere needed fixing;
2. Fixed a bug in integer.pyx introduced in 3.1.2.alpha0 (in #4286)
3. Cleaner use of sequences as a method of coercing a list to have a coherent universe.

In view of item 2, which corrected this:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.2.alpha0, Release Date: 2008-10-20                  |
| Type notebook() for the GUI, and license() for information.        |
sage: sage.rings.integer.GCD_list([2,2,3])
2
```
and the fact that I really did do a -testall, I am hoping for a quick positive review!  I think that Paul Z is eligible to do that although the initial patches here were his.



---

archive/issue_comments_021542.json:
```json
{
    "body": "I tried to apply both patches to 3.1.4 but the 2nd one failed:\n\n```\nfleur% hg import sage-trac_3118.patch \napplying sage-trac_3118.patch\nfleur% hg import sage-trac_3118-2.patch\napplying sage-trac_3118-2.patch\npatching file sage/rings/integer.pyx\nHunk #1 FAILED at 3595\nHunk #3 FAILED at 3649\n2 out of 3 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej\nabort: patch failed to apply\n```\nShould I apply another patch before?",
    "created_at": "2008-10-23T16:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21542",
    "user": "https://github.com/zimmermann6"
}
```

I tried to apply both patches to 3.1.4 but the 2nd one failed:

```
fleur% hg import sage-trac_3118.patch 
applying sage-trac_3118.patch
fleur% hg import sage-trac_3118-2.patch
applying sage-trac_3118-2.patch
patching file sage/rings/integer.pyx
Hunk #1 FAILED at 3595
Hunk #3 FAILED at 3649
2 out of 3 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej
abort: patch failed to apply
```
Should I apply another patch before?



---

archive/issue_comments_021543.json:
```json
{
    "body": "Hi Paul,\n\nthis patch series requires at least #4286. It should apply fine on top of 3.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-23T16:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21543",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Paul,

this patch series requires at least #4286. It should apply fine on top of 3.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_021544.json:
```json
{
    "body": "Hi,\n\npositive review for the \"integer.pyx\" corrections in \"sage-trac_3118-2.patch\", which heal two issues introduced in #4286.\n(One horrible bug with a new doctest to show it is fixed now, and one for beauty: make the gcd of a list consisting of one single negative number be a positive number, so that all resulting integers of a gcd calculation are non-negative now --- as long as this holds for the underlying GMP algorithm used.)\n\nCheers,\ngsw",
    "created_at": "2008-10-23T18:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21544",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hi,

positive review for the "integer.pyx" corrections in "sage-trac_3118-2.patch", which heal two issues introduced in #4286.
(One horrible bug with a new doctest to show it is fixed now, and one for beauty: make the gcd of a list consisting of one single negative number be a positive number, so that all resulting integers of a gcd calculation are non-negative now --- as long as this holds for the underlying GMP algorithm used.)

Cheers,
gsw



---

archive/issue_comments_021545.json:
```json
{
    "body": "Georg is right -- I made that change so that gcd((-2,)) returns 2 and similarly for lcm.  And the patches were based on 3.2.alpha0 -- sorry Paul.",
    "created_at": "2008-10-23T22:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21545",
    "user": "https://github.com/JohnCremona"
}
```

Georg is right -- I made that change so that gcd((-2,)) returns 2 and similarly for lcm.  And the patches were based on 3.2.alpha0 -- sorry Paul.



---

archive/issue_comments_021546.json:
```json
{
    "body": "I tried all the above examples which work as expected, and also did sage -t in the rings\ndirectory. Since John already did sage -testall, I give a positive review.",
    "created_at": "2008-10-24T16:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21546",
    "user": "https://github.com/zimmermann6"
}
```

I tried all the above examples which work as expected, and also did sage -t in the rings
directory. Since John already did sage -testall, I give a positive review.



---

archive/issue_events_007042.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-25T22:41:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3118#event-7042"
}
```



---

archive/issue_comments_021547.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-25T22:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21547",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021548.json:
```json
{
    "body": "Merged sage-trac_3118.patch and sage-trac_3118-2.patch in Sage 3.2.alpha1",
    "created_at": "2008-10-25T22:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3118#issuecomment-21548",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-trac_3118.patch and sage-trac_3118-2.patch in Sage 3.2.alpha1
