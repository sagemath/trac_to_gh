# Issue 2419: Gap interface and resultant destroy the Singular interface on some machines

archive/issues_002419.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @wdjoyner @williamstein\n\nKeywords: gap singular resultant\n\nI consider the following bug critical, because it completely corrupts the Singular interface. However, it seems that the error only occurs on very few machines - so far, only one other person can reproduce the bug - see discussions at http://groups.google.com/group/sage-support/browse_thread/thread/5006f9a839723e27?hl=en\n\nCreating a univariate polynomial ring R over the rationals, computing the resultant of two polynomials in that ring and using the gap interface for the Integers makes the singular interface fail on R (on some machines). To be precise:\n\n```\nsage: R.<x> = QQ[]\nsage: f = x^3 + x + 1;  g = x^3 - x - 1\nsage: r = f.resultant(g)\nsage: gap(ZZ)\nIntegers\nsage: singular(R).typeof()    # this should yield 'ring' !\nprint(sage8);\nsage: singular(R).name()   # this is correct ...\n'sage0'\nsage: singular('sage0')   # ... hence, this should return a ring - but it doesn't\nprint(sage9);\nsage: singular('sage0')\nprint(sage10);\nsage: singular('sage0')\nprint(sage11);\n```\n\n\nNote that computing the resultant is important. If i replace it with, say, `singular(R)`, then the error does not occur. Also, if `gap(ZZ)` is done *before* computing the resultant, the error does not occur.\n\nDavid Joyner observed that on both machines showing that error, there is an rpm based Linux. However, i know a machine with the same Linux that does not show that error.\nAgain, see http://groups.google.com/group/sage-support/browse_thread/thread/5006f9a839723e27?hl=en\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2419\n\n",
    "created_at": "2008-03-07T08:10:10Z",
    "labels": [
        "component: interfaces",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Gap interface and resultant destroy the Singular interface on some machines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2419",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @williamstein

CC:  @wdjoyner @williamstein

Keywords: gap singular resultant

I consider the following bug critical, because it completely corrupts the Singular interface. However, it seems that the error only occurs on very few machines - so far, only one other person can reproduce the bug - see discussions at http://groups.google.com/group/sage-support/browse_thread/thread/5006f9a839723e27?hl=en

Creating a univariate polynomial ring R over the rationals, computing the resultant of two polynomials in that ring and using the gap interface for the Integers makes the singular interface fail on R (on some machines). To be precise:

```
sage: R.<x> = QQ[]
sage: f = x^3 + x + 1;  g = x^3 - x - 1
sage: r = f.resultant(g)
sage: gap(ZZ)
Integers
sage: singular(R).typeof()    # this should yield 'ring' !
print(sage8);
sage: singular(R).name()   # this is correct ...
'sage0'
sage: singular('sage0')   # ... hence, this should return a ring - but it doesn't
print(sage9);
sage: singular('sage0')
print(sage10);
sage: singular('sage0')
print(sage11);
```


Note that computing the resultant is important. If i replace it with, say, `singular(R)`, then the error does not occur. Also, if `gap(ZZ)` is done *before* computing the resultant, the error does not occur.

David Joyner observed that on both machines showing that error, there is an rpm based Linux. However, i know a machine with the same Linux that does not show that error.
Again, see http://groups.google.com/group/sage-support/browse_thread/thread/5006f9a839723e27?hl=en


Issue created by migration from https://trac.sagemath.org/ticket/2419





---

archive/issue_comments_016284.json:
```json
{
    "body": "Replying to [ticket:2419 SimonKing]:\n> I consider the following bug critical, because it completely corrupts the Singular interface. However, it seems that the error only occurs on very few machines ...\n\nMeanwhile, i found a very similar error that even occurs on sage.math with sage 2.10.2:\n\n```\nsage: R.<x> = QQ[] \nsage: f = x^3 + x + 1;  g = x^3 - x - 1 \nsage:  r = f.resultant(g) \nsage: gap(ZZ) \nIntegers \nsage: singular(R) \n\nsage: singular(R) \n//   characteristic : 0 \n//   number of vars : 1 \n//        block   1 : ordering lp \n//                  : names    x \n//        block   2 : ordering C \nsage: singular(R).typeof() \n\nsage: singular(R).typeof() \n\nsage: singular(R).name() \n'sage0' \nsage: singular('sage0') \n\nsage: singular('sage0') \n\n```\n\nSo, after computing resultant and calling gap, the first singular(R) has empty output, but the second (and following) display a ring. Calling typeof on that ring repeatedly has empty output. And although `sage0` is the name of singular(R), calling singular('sage0') has empty output.\n\nI hope this is sufficiently reproducible for tracking down the problem.",
    "created_at": "2008-03-08T22:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16284",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [ticket:2419 SimonKing]:
> I consider the following bug critical, because it completely corrupts the Singular interface. However, it seems that the error only occurs on very few machines ...

Meanwhile, i found a very similar error that even occurs on sage.math with sage 2.10.2:

```
sage: R.<x> = QQ[] 
sage: f = x^3 + x + 1;  g = x^3 - x - 1 
sage:  r = f.resultant(g) 
sage: gap(ZZ) 
Integers 
sage: singular(R) 

sage: singular(R) 
//   characteristic : 0 
//   number of vars : 1 
//        block   1 : ordering lp 
//                  : names    x 
//        block   2 : ordering C 
sage: singular(R).typeof() 

sage: singular(R).typeof() 

sage: singular(R).name() 
'sage0' 
sage: singular('sage0') 

sage: singular('sage0') 

```

So, after computing resultant and calling gap, the first singular(R) has empty output, but the second (and following) display a ring. Calling typeof on that ring repeatedly has empty output. And although `sage0` is the name of singular(R), calling singular('sage0') has empty output.

I hope this is sufficiently reproducible for tracking down the problem.



---

archive/issue_comments_016285.json:
```json
{
    "body": "Replying to [comment:2 SimonKing]:\n\nI was just trying the above example that used to fail on sage.math with sage-2.10.2\n\nIt works on sage.math with sage-2.10.3!! So, many thanks to the person who did (accidentally?) fix the bug.\n\nNow i am looking forward to test it on my machine, but this will take a while.",
    "created_at": "2008-03-12T08:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16285",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:2 SimonKing]:

I was just trying the above example that used to fail on sage.math with sage-2.10.2

It works on sage.math with sage-2.10.3!! So, many thanks to the person who did (accidentally?) fix the bug.

Now i am looking forward to test it on my machine, but this will take a while.



---

archive/issue_comments_016286.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n>\n> Now i am looking forward to test it on my machine, but this will take a while.\n\nAlthough the problem vanished on sage.math, it is still present on my machine. Is there anyone out there who can reproduce it?",
    "created_at": "2008-03-12T12:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16286",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:3 SimonKing]:
>
> Now i am looking forward to test it on my machine, but this will take a while.

Although the problem vanished on sage.math, it is still present on my machine. Is there anyone out there who can reproduce it?



---

archive/issue_comments_016287.json:
```json
{
    "body": "This is what I get on an amd64 ubuntu 7.10:\n\nwdj`@`wooster:~/wdj/sagefiles/sage-2.10.3$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.3, Release Date: 2008-03-11                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: R.<x> = QQ[]\nsage: sage: f = x^3 + x + 1;  g = x^3 - x - 1\nsage: sage: r = f.resultant(g)\nsage: sage: gap(ZZ)\nIntegers\nsage: Integers\n<function IntegerModRing at 0xf95ed8>\nsage: sage: singular(R).typeof()\nprint(sage8);\nsage: singular(R).name()\n'sage0'\nsage: singular('sage0')\nprint(sage9);\nsage: singular('sage0')\nprint(sage10);\nsage: singular('sage0')\nprint(sage11);\nsage: singular(R)\n\n//   number of vars : 1\n//        block   1 : ordering lp\n//                  : names    x\n//        block   2 : ordering C\nsage: singular(R).typeof()\nprint(sage12);\nsage: singular(R).name()\n'sage0'\nsage: singular(R).name()\n'sage0'\nsage: singular('sage0')\nprint(sage13);\nsage:",
    "created_at": "2008-03-12T13:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16287",
    "user": "https://github.com/wdjoyner"
}
```

This is what I get on an amd64 ubuntu 7.10:

wdj`@`wooster:~/wdj/sagefiles/sage-2.10.3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.3, Release Date: 2008-03-11                      |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: R.<x> = QQ[]
sage: sage: f = x^3 + x + 1;  g = x^3 - x - 1
sage: sage: r = f.resultant(g)
sage: sage: gap(ZZ)
Integers
sage: Integers
<function IntegerModRing at 0xf95ed8>
sage: sage: singular(R).typeof()
print(sage8);
sage: singular(R).name()
'sage0'
sage: singular('sage0')
print(sage9);
sage: singular('sage0')
print(sage10);
sage: singular('sage0')
print(sage11);
sage: singular(R)

//   number of vars : 1
//        block   1 : ordering lp
//                  : names    x
//        block   2 : ordering C
sage: singular(R).typeof()
print(sage12);
sage: singular(R).name()
'sage0'
sage: singular(R).name()
'sage0'
sage: singular('sage0')
print(sage13);
sage:



---

archive/issue_comments_016288.json:
```json
{
    "body": "Sorry, forgot the wikiformatting, so reposted:\n\n\n```\nwdj@wooster:~/wdj/sagefiles/sage-2.10.3$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.3, Release Date: 2008-03-11                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: R.<x> = QQ[]\nsage: sage: f = x^3 + x + 1;  g = x^3 - x - 1\nsage: sage: r = f.resultant(g)\nsage: sage: gap(ZZ)\nIntegers\nsage: Integers\n<function IntegerModRing at 0xf95ed8>\nsage: sage: singular(R).typeof()\nprint(sage8);\nsage: singular(R).name()\n'sage0'\nsage: singular('sage0')\nprint(sage9);\nsage: singular('sage0')\nprint(sage10);\nsage: singular('sage0')\nprint(sage11);\nsage: singular(R)\n\n//   number of vars : 1\n//        block   1 : ordering lp\n//                  : names    x\n//        block   2 : ordering C\nsage: singular(R).typeof()\nprint(sage12);\nsage: singular(R).name()\n'sage0'\nsage: singular(R).name()\n'sage0'\nsage: singular('sage0')\nprint(sage13);\nsage:                              \n```\n",
    "created_at": "2008-03-12T13:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16288",
    "user": "https://github.com/wdjoyner"
}
```

Sorry, forgot the wikiformatting, so reposted:


```
wdj@wooster:~/wdj/sagefiles/sage-2.10.3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.3, Release Date: 2008-03-11                      |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: R.<x> = QQ[]
sage: sage: f = x^3 + x + 1;  g = x^3 - x - 1
sage: sage: r = f.resultant(g)
sage: sage: gap(ZZ)
Integers
sage: Integers
<function IntegerModRing at 0xf95ed8>
sage: sage: singular(R).typeof()
print(sage8);
sage: singular(R).name()
'sage0'
sage: singular('sage0')
print(sage9);
sage: singular('sage0')
print(sage10);
sage: singular('sage0')
print(sage11);
sage: singular(R)

//   number of vars : 1
//        block   1 : ordering lp
//                  : names    x
//        block   2 : ordering C
sage: singular(R).typeof()
print(sage12);
sage: singular(R).name()
'sage0'
sage: singular(R).name()
'sage0'
sage: singular('sage0')
print(sage13);
sage:                              
```




---

archive/issue_comments_016289.json:
```json
{
    "body": "Replying to [comment:6 wdj]:\n\nExactly the same happens on my machine, with AMD Athlon 64 and openSUSE 10.2.\n\nSomething different happens on sage.math, but it is still nonsense:\n\n```\nsage: R.<x> = QQ[]\nsage: f = x^3 + x + 1;  g = x^3 - x - 1\nsage: r = f.resultant(g)\nsage: gap(ZZ)\nIntegers\nsage: singular(R).typeof()\n\nsage: singular(R).name()\n'sage0'\nsage: singular('sage0')\n\nsage: singular('sage0')\n\nsage: singular(R)\n\n//   characteristic : 0\n//   number of vars : 1\n//        block   1 : ordering lp\n//                  : names    x\n//        block   2 : ordering C\n```\n\n\nHence, singular('sage0') and singular(R).typeof() have no visible output.",
    "created_at": "2008-03-12T13:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16289",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:6 wdj]:

Exactly the same happens on my machine, with AMD Athlon 64 and openSUSE 10.2.

Something different happens on sage.math, but it is still nonsense:

```
sage: R.<x> = QQ[]
sage: f = x^3 + x + 1;  g = x^3 - x - 1
sage: r = f.resultant(g)
sage: gap(ZZ)
Integers
sage: singular(R).typeof()

sage: singular(R).name()
'sage0'
sage: singular('sage0')

sage: singular('sage0')

sage: singular(R)

//   characteristic : 0
//   number of vars : 1
//        block   1 : ordering lp
//                  : names    x
//        block   2 : ordering C
```


Hence, singular('sage0') and singular(R).typeof() have no visible output.



---

archive/issue_comments_016290.json:
```json
{
    "body": "\n```\nperhaps you noticed that i had found a version of the weird bug\n\"resultant+gap+singular=nonsense\" even on sage.math, as i reported in\nticket #2419.\n\nThat was for sage-2.10.2; but the problem has vanished for sage-2.10.3 --\nat least on sage.math, i am curious what will happen on my machine. [[it survives there]]\n\nDo you have any idea how the problem was fixed (or whom i should ask)?\n```\n",
    "created_at": "2008-03-12T14:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16290",
    "user": "https://github.com/williamstein"
}
```


```
perhaps you noticed that i had found a version of the weird bug
"resultant+gap+singular=nonsense" even on sage.math, as i reported in
ticket #2419.

That was for sage-2.10.2; but the problem has vanished for sage-2.10.3 --
at least on sage.math, i am curious what will happen on my machine. [[it survives there]]

Do you have any idea how the problem was fixed (or whom i should ask)?
```




---

archive/issue_comments_016291.json:
```json
{
    "body": "Replying to [comment:8 was]:\n> perhaps you noticed that i had found a version of the weird bug\n> \"resultant+gap+singular=nonsense\" even on sage.math, as i reported in\n> ticket #2419.\n> \n> That was for sage-2.10.2; but the problem has vanished for sage-2.10.3 --\n> at least on sage.math, i am curious what will happen on my machine. [This is the Trac macro *it survives there* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#it survives there-macro)\n> \n> Do you have any idea how the problem was fixed (or whom i should ask)?\n\nThat was my message off trac to William. Apparently i was too optimistic: What i posted above *did* (and still does) happen on sage.math *after* writing my message to William. \n\nHopefully it is reproducible for you.",
    "created_at": "2008-03-12T15:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16291",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:8 was]:
> perhaps you noticed that i had found a version of the weird bug
> "resultant+gap+singular=nonsense" even on sage.math, as i reported in
> ticket #2419.
> 
> That was for sage-2.10.2; but the problem has vanished for sage-2.10.3 --
> at least on sage.math, i am curious what will happen on my machine. [This is the Trac macro *it survives there* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#it survives there-macro)
> 
> Do you have any idea how the problem was fixed (or whom i should ask)?

That was my message off trac to William. Apparently i was too optimistic: What i posted above *did* (and still does) happen on sage.math *after* writing my message to William. 

Hopefully it is reproducible for you.



---

archive/issue_comments_016292.json:
```json
{
    "body": "Attachment [sage-2419-singular_synch.patch](tarball://root/attachments/some-uuid/ticket2419/sage-2419-singular_synch.patch) by @williamstein created at 2008-03-12 15:33:10",
    "created_at": "2008-03-12T15:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16292",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2419-singular_synch.patch](tarball://root/attachments/some-uuid/ticket2419/sage-2419-singular_synch.patch) by @williamstein created at 2008-03-12 15:33:10



---

archive/issue_comments_016293.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-03-12T15:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16293",
    "user": "https://github.com/williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_016294.json:
```json
{
    "body": "The patch sage-2419-singular_synch.patch did not apply cleanly against my version\nof 2.10.3 using the command \nhg_doc.apply(\"/home/wdj/wdj/sagefiles/sage-2419-singular_synch.patch\")",
    "created_at": "2008-03-12T16:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16294",
    "user": "https://github.com/wdjoyner"
}
```

The patch sage-2419-singular_synch.patch did not apply cleanly against my version
of 2.10.3 using the command 
hg_doc.apply("/home/wdj/wdj/sagefiles/sage-2419-singular_synch.patch")



---

archive/issue_comments_016295.json:
```json
{
    "body": "> The patch sage-2419-singular_synch.patch did not apply cleanly \n> against my version of 2.10.3 using the command\n> hg_doc.apply(\"/home/wdj/wdj/sagefiles/sage-2419-singular_synch.patch\")\n\nAgh!  hg_doc??  Why are you using hg_doc?",
    "created_at": "2008-03-12T16:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16295",
    "user": "https://github.com/williamstein"
}
```

> The patch sage-2419-singular_synch.patch did not apply cleanly 
> against my version of 2.10.3 using the command
> hg_doc.apply("/home/wdj/wdj/sagefiles/sage-2419-singular_synch.patch")

Agh!  hg_doc??  Why are you using hg_doc?



---

archive/issue_comments_016296.json:
```json
{
    "body": "Hi William!\n\nThe patch applies cleanly, and it solves the problem on my machine!\n\nSo, many thanks for the great job!\n\nOn sage-support you mentioned that the patch would slow down the interface considerably. Is there a way to know when synchronization is really needed? Perhaps, if the synchronization would not be done before *each* command, it were faster.",
    "created_at": "2008-03-12T18:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16296",
    "user": "https://github.com/simon-king-jena"
}
```

Hi William!

The patch applies cleanly, and it solves the problem on my machine!

So, many thanks for the great job!

On sage-support you mentioned that the patch would slow down the interface considerably. Is there a way to know when synchronization is really needed? Perhaps, if the synchronization would not be done before *each* command, it were faster.



---

archive/issue_comments_016297.json:
```json
{
    "body": "> On sage-support you mentioned that the patch would slow down the \n> interface considerably. Is there a way to know when synchronization \n\n30% isn't so bad, and it's only a LATENCY issue really, i.e., if you\ndo \n\n```\n  singular('something that takes some actual time on the singular side')\n```\n\nthen it makes almost no difference.  \n\n> is really needed? Perhaps, if the synchronization would not be done \n> before each command, it were faster.\n\nBut then it wouldn't always work, which defeats the whole purpose, which\nis \"rock solid robustness\".\n\n -- William",
    "created_at": "2008-03-12T18:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16297",
    "user": "https://github.com/williamstein"
}
```

> On sage-support you mentioned that the patch would slow down the 
> interface considerably. Is there a way to know when synchronization 

30% isn't so bad, and it's only a LATENCY issue really, i.e., if you
do 

```
  singular('something that takes some actual time on the singular side')
```

then it makes almost no difference.  

> is really needed? Perhaps, if the synchronization would not be done 
> before each command, it were faster.

But then it wouldn't always work, which defeats the whole purpose, which
is "rock solid robustness".

 -- William



---

archive/issue_comments_016298.json:
```json
{
    "body": "Just to be clear: that \"30%\" refers only to the extra time if you do almost nothing in singular.eval('...').  If you actually do something that takes time, then the overhead of synchronizing should be way less.  Also, the 30% is for maxima.  I didn't benchmark the singular overhead yet.",
    "created_at": "2008-03-12T18:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16298",
    "user": "https://github.com/williamstein"
}
```

Just to be clear: that "30%" refers only to the extra time if you do almost nothing in singular.eval('...').  If you actually do something that takes time, then the overhead of synchronizing should be way less.  Also, the 30% is for maxima.  I didn't benchmark the singular overhead yet.



---

archive/issue_comments_016299.json:
```json
{
    "body": "Replying to [comment:16 was]:\n> Just to be clear: that \"30%\" refers only to the extra time if you do almost nothing in singular.eval('...').  If you actually do something that takes time, then the overhead of synchronizing should be way less.  Also, the 30% is for maxima.  I didn't benchmark the singular overhead yet.  \n\nThank you for the explanation! \n\nSince the problem vanishes with the patch (at least for me), I give a positive review, although you may know better than i if further and more extensive tests are needed.",
    "created_at": "2008-03-12T18:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16299",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:16 was]:
> Just to be clear: that "30%" refers only to the extra time if you do almost nothing in singular.eval('...').  If you actually do something that takes time, then the overhead of synchronizing should be way less.  Also, the 30% is for maxima.  I didn't benchmark the singular overhead yet.  

Thank you for the explanation! 

Since the problem vanishes with the patch (at least for me), I give a positive review, although you may know better than i if further and more extensive tests are needed.



---

archive/issue_comments_016300.json:
```json
{
    "body": "Replying to [comment:15 was]:\n> > is really needed? Perhaps, if the synchronization would not be done \n> > before each command, it were faster.\n> \n> But then it wouldn't always work, which defeats the whole purpose, which\n> is \"rock solid robustness\".\n\nWhat i meant was: Is there a *fast* test that tells us whether or not the interface needs synchronization? If the test is faster than actually doing the synchronization, it would be faster and still rock solid.",
    "created_at": "2008-03-12T18:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16300",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:15 was]:
> > is really needed? Perhaps, if the synchronization would not be done 
> > before each command, it were faster.
> 
> But then it wouldn't always work, which defeats the whole purpose, which
> is "rock solid robustness".

What i meant was: Is there a *fast* test that tells us whether or not the interface needs synchronization? If the test is faster than actually doing the synchronization, it would be faster and still rock solid.



---

archive/issue_comments_016301.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-12T19:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16301",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_comments_016302.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-12T19:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16302",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002595.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-12T19:45:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2419#event-2595"
}
```



---

archive/issue_comments_016303.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-12T19:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16303",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002596.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-03-12T19:47:46Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2419#event-2596"
}
```



---

archive/issue_comments_016304.json:
```json
{
    "body": "Wow, this was a 15-minute test patch, not a finished solution.\nIt should be have been rejected based on lack of doctests if nothing\nelse.  Anyways, reopened.",
    "created_at": "2008-03-12T19:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16304",
    "user": "https://github.com/williamstein"
}
```

Wow, this was a 15-minute test patch, not a finished solution.
It should be have been rejected based on lack of doctests if nothing
else.  Anyways, reopened.



---

archive/issue_comments_016305.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-03-12T19:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16305",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_016306.json:
```json
{
    "body": "ok, for the record: I reverted the patch in my tree, i.e. once doctests are added and the patch has been given a positive review it needs to be reapplied.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-12T19:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16306",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

ok, for the record: I reverted the patch in my tree, i.e. once doctests are added and the patch has been given a positive review it needs to be reapplied.

Cheers,

Michael



---

archive/issue_comments_016307.json:
```json
{
    "body": "Replying to [comment:21 mabshoff]:\n> ok, for the record: I reverted the patch in my tree, i.e. once doctests are added and the patch has been given a positive review it needs to be reapplied.\n\nSorry that i confused you by using the notion \"positive review\" in my post. What i meant was \"positive feedback, since the original problem was solved\", where \"positive feedback\" means that it appears to go in a good direction.",
    "created_at": "2008-03-12T19:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16307",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:21 mabshoff]:
> ok, for the record: I reverted the patch in my tree, i.e. once doctests are added and the patch has been given a positive review it needs to be reapplied.

Sorry that i confused you by using the notion "positive review" in my post. What i meant was "positive feedback, since the original problem was solved", where "positive feedback" means that it appears to go in a good direction.



---

archive/issue_comments_016308.json:
```json
{
    "body": "Oops. The hg_doc was stupid. With hg_sage.apply, it applies cleanly and fixes the problem.\nPasses sage -testall.",
    "created_at": "2008-03-12T22:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16308",
    "user": "https://github.com/wdjoyner"
}
```

Oops. The hg_doc was stupid. With hg_sage.apply, it applies cleanly and fixes the problem.
Passes sage -testall.



---

archive/issue_comments_016309.json:
```json
{
    "body": "Hi!\n\nSince my premature hooray was causing some trouble, i try to excuse with a few doc tests: See the patch that i am about to attach, which should be applied after William's patch. Also i have a couple of questions/remarks.\n\nQuestions/Remarks:\n* Example for _crash_msg: I don't know if that example is platform dependent, since i use os.kill(singular.pid(),9) -- probably you know a more elegant way to kill singular on purpose. Also, it fails on `sage -t` because the error message \"Singular crashed -- automatically restarting.\" is considered as output. \n  - I'd like to show the error message to the user, but i don't want that `sage -t` expects it as output. How can i do so?\n* I didn't find out what _expect_expr is supposed to do. Similarly to what is done in _synchronize, I tried without success:\n\n```\nsage: singular._sendstr('2+3;')\nsage: singular._expect_expr(timeout=0.5)\n```\n \n* Also i don't find a reasonable example for _interrupt.",
    "created_at": "2008-03-13T09:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16309",
    "user": "https://github.com/simon-king-jena"
}
```

Hi!

Since my premature hooray was causing some trouble, i try to excuse with a few doc tests: See the patch that i am about to attach, which should be applied after William's patch. Also i have a couple of questions/remarks.

Questions/Remarks:
* Example for _crash_msg: I don't know if that example is platform dependent, since i use os.kill(singular.pid(),9) -- probably you know a more elegant way to kill singular on purpose. Also, it fails on `sage -t` because the error message "Singular crashed -- automatically restarting." is considered as output. 
  - I'd like to show the error message to the user, but i don't want that `sage -t` expects it as output. How can i do so?
* I didn't find out what _expect_expr is supposed to do. Similarly to what is done in _synchronize, I tried without success:

```
sage: singular._sendstr('2+3;')
sage: singular._expect_expr(timeout=0.5)
```
 
* Also i don't find a reasonable example for _interrupt.



---

archive/issue_comments_016310.json:
```json
{
    "body": "Adding some doctests to singular synchronization. To be applied after William's patch",
    "created_at": "2008-03-13T09:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16310",
    "user": "https://github.com/simon-king-jena"
}
```

Adding some doctests to singular synchronization. To be applied after William's patch



---

archive/issue_comments_016311.json:
```json
{
    "body": "Attachment [sage-2419-singular_synch_doctest.patch](tarball://root/attachments/some-uuid/ticket2419/sage-2419-singular_synch_doctest.patch) by @simon-king-jena created at 2008-03-13 10:40:04\n\nI found that bug since doc tests for my patch from #2420 failed. Thus i expected that William's synchronization patch would fix #2420 as well, but it didn't -- see my comments there.\n\nI'll try to boil down the new problem, but i suspect that a synchronization will be needed for the gap interface as well.",
    "created_at": "2008-03-13T10:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16311",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [sage-2419-singular_synch_doctest.patch](tarball://root/attachments/some-uuid/ticket2419/sage-2419-singular_synch_doctest.patch) by @simon-king-jena created at 2008-03-13 10:40:04

I found that bug since doc tests for my patch from #2420 failed. Thus i expected that William's synchronization patch would fix #2420 as well, but it didn't -- see my comments there.

I'll try to boil down the new problem, but i suspect that a synchronization will be needed for the gap interface as well.



---

archive/issue_comments_016312.json:
```json
{
    "body": "Hi!\n\nSo far, there was no feedback on my doc-tests, and no explanation about what _expect_expr is supposed to do. \n\nConcerning testing: I used Williams patch for extensive computations in a program that makes (small) use of the gap interface and *heavy* use of the singular interface. It didn't crash, which indicates that it may work. \n\nI am not sure: Is this enough for giving a \"positive review pending; more doctests needed\"?",
    "created_at": "2008-03-20T12:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16312",
    "user": "https://github.com/simon-king-jena"
}
```

Hi!

So far, there was no feedback on my doc-tests, and no explanation about what _expect_expr is supposed to do. 

Concerning testing: I used Williams patch for extensive computations in a program that makes (small) use of the gap interface and *heavy* use of the singular interface. It didn't crash, which indicates that it may work. 

I am not sure: Is this enough for giving a "positive review pending; more doctests needed"?



---

archive/issue_comments_016313.json:
```json
{
    "body": "> I am not sure: Is this enough for giving a \"positive review \n> pending; more doctests needed\"? \n\nYes.  Given how the patch is written if it works in practice it\nis definitely worth including in Sage.  \n\nI can't work on this now unfortunately due to lack of time.",
    "created_at": "2008-03-20T23:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16313",
    "user": "https://github.com/williamstein"
}
```

> I am not sure: Is this enough for giving a "positive review 
> pending; more doctests needed"? 

Yes.  Given how the patch is written if it works in practice it
is definitely worth including in Sage.  

I can't work on this now unfortunately due to lack of time.



---

archive/issue_comments_016314.json:
```json
{
    "body": "Sorry, i have not been at work for a while. According to William's remark, i give a \"positive review pending; more doctests needed\". However, i could only provide more doctests if someone tells me about the use of _expect_expr. Also, i don't know how to deal with printed output in a doctest -- this concerns my example for _crash_msg.",
    "created_at": "2008-04-08T07:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16314",
    "user": "https://github.com/simon-king-jena"
}
```

Sorry, i have not been at work for a while. According to William's remark, i give a "positive review pending; more doctests needed". However, i could only provide more doctests if someone tells me about the use of _expect_expr. Also, i don't know how to deal with printed output in a doctest -- this concerns my example for _crash_msg.



---

archive/issue_comments_016315.json:
```json
{
    "body": "This *really* ought to be looked at. It seems ready.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-18T20:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This *really* ought to be looked at. It seems ready.

Cheers,

Michael



---

archive/issue_comments_016316.json:
```json
{
    "body": "Attachment [sage-2419-refactor.patch](tarball://root/attachments/some-uuid/ticket2419/sage-2419-refactor.patch) by @williamstein created at 2008-04-20 19:50:30\n\napply *all three* patches in order.",
    "created_at": "2008-04-20T19:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16316",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2419-refactor.patch](tarball://root/attachments/some-uuid/ticket2419/sage-2419-refactor.patch) by @williamstein created at 2008-04-20 19:50:30

apply *all three* patches in order.



---

archive/issue_comments_016317.json:
```json
{
    "body": "It said \"[positive review pending; more doctests needed]\", so I wrote more doctests and did the\nrefactoring suggested in my comments.   So now -- [with patch; needs review]",
    "created_at": "2008-04-20T19:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16317",
    "user": "https://github.com/williamstein"
}
```

It said "[positive review pending; more doctests needed]", so I wrote more doctests and did the
refactoring suggested in my comments.   So now -- [with patch; needs review]



---

archive/issue_comments_016318.json:
```json
{
    "body": "Applies and passes tests against 3.0alpha5.  Looks good to me.",
    "created_at": "2008-04-20T20:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16318",
    "user": "https://github.com/mwhansen"
}
```

Applies and passes tests against 3.0alpha5.  Looks good to me.



---

archive/issue_events_002597.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-21T00:41:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2419#event-2597"
}
```



---

archive/issue_comments_016319.json:
```json
{
    "body": "Merged all three patches in Sage 3.0.rc1",
    "created_at": "2008-04-21T00:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16319",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.0.rc1



---

archive/issue_comments_016320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T00:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16320",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016321.json:
```json
{
    "body": "Mmh, after merging this patch I see:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.rc1$ ./sage -t  devel/sage/sage/interfaces/expect.py\nsage -t  devel/sage/sage/interfaces/expect.py               **********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/expect.py\", line 835:\n    sage: singular('2+3')\nExpected:\n    Singular crashed -- automatically restarting.\n    5\nGot:\n    5\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/expect.py\", line 860:\n    sage: R.<x> = QQ[]; f = x^3 + x + 1;  g = x^3 - x - 1; r = f.resultant(g); gap(ZZ); singular(R)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_17[2]>\", line 1, in <module>\n        R = QQ['x']; (x,) = R._first_ngens(Integer(1)); f = x**Integer(3) + x + Integer(1);  g = x**Integer(3) - x - Integer(1); r = f.resultant(g); gap(ZZ); singular(R)###line 860:\n    sage: R.<x> = QQ[]; f = x^3 + x + 1;  g = x^3 - x - 1; r = f.resultant(g); gap(ZZ); singular(R)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 288, in resultant\n        return resultant_func(self, other, variable)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 438, in resultant_func\n        rt = self._singular_().resultant(other._singular_(), variable._singular_())\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 282, in _singular_\n        return _singular_func(self, singular, have_ring, force)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 334, in _singular_func\n        self.parent()._singular_(singular,force=force).set_ring() #this is expensive\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 174, in _singular_\n        return self._singular_init_(singular, force)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 217, in _singular_init_\n        self.__singular = singular.ring(self.characteristic(), _vars, order=order, check=False)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 681, in ring\n        R = self('%s,%s,%s'%(char, vars, order), 'ring')\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 502, in __call__\n        return SingularElement(self, type, x, False)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 825, in __init__\n        raise TypeError, x\n    TypeError: End Of File (EOF) in read_nonblocking(). Braindead platform.\n    <pexpect.spawn instance at 0x2abf554371b8>\n    version: 2.0 ($Revision: 1.151 $)\n    command: /scratch/mabshoff/release-cycle/sage-3.0.rc1/local/bin/Singular\n    args: ['/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/bin/Singular', '-t', '--ticks-per-sec', '1000']\n    patterns:\n        >\n    buffer (last 100 chars):\n    before (last 100 chars): ring sage4=0,x,lp;\n\n    after: <class 'pexpect.EOF'>\n    match: None\n    match_index: None\n    exitstatus: None\n    flag_eof: 1\n    pid: 19207\n    child_fd: 3\n    timeout: None\n    delimiter: <class 'pexpect.EOF'>\n    logfile: None\n    maxread: 1000\n    searchwindowsize: None\n    delaybeforesend: 0\n    Singular crashed executing ring sage4=0,x,lp;\n**********************************************************************\n2 items had failures:\n   1 of   7 in __main__.example_16\n   1 of   3 in __main__.example_17\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/.doctest_expect.py\n         [7.5 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage/sage/interfaces/expect.py\nTotal time for all tests: 7.5 seconds\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.rc1$   \n```\n\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T01:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16321",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mmh, after merging this patch I see:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.rc1$ ./sage -t  devel/sage/sage/interfaces/expect.py
sage -t  devel/sage/sage/interfaces/expect.py               **********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/expect.py", line 835:
    sage: singular('2+3')
Expected:
    Singular crashed -- automatically restarting.
    5
Got:
    5
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/expect.py", line 860:
    sage: R.<x> = QQ[]; f = x^3 + x + 1;  g = x^3 - x - 1; r = f.resultant(g); gap(ZZ); singular(R)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[2]>", line 1, in <module>
        R = QQ['x']; (x,) = R._first_ngens(Integer(1)); f = x**Integer(3) + x + Integer(1);  g = x**Integer(3) - x - Integer(1); r = f.resultant(g); gap(ZZ); singular(R)###line 860:
    sage: R.<x> = QQ[]; f = x^3 + x + 1;  g = x^3 - x - 1; r = f.resultant(g); gap(ZZ); singular(R)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 288, in resultant
        return resultant_func(self, other, variable)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 438, in resultant_func
        rt = self._singular_().resultant(other._singular_(), variable._singular_())
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 282, in _singular_
        return _singular_func(self, singular, have_ring, force)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 334, in _singular_func
        self.parent()._singular_(singular,force=force).set_ring() #this is expensive
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 174, in _singular_
        return self._singular_init_(singular, force)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 217, in _singular_init_
        self.__singular = singular.ring(self.characteristic(), _vars, order=order, check=False)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 681, in ring
        R = self('%s,%s,%s'%(char, vars, order), 'ring')
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 502, in __call__
        return SingularElement(self, type, x, False)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 825, in __init__
        raise TypeError, x
    TypeError: End Of File (EOF) in read_nonblocking(). Braindead platform.
    <pexpect.spawn instance at 0x2abf554371b8>
    version: 2.0 ($Revision: 1.151 $)
    command: /scratch/mabshoff/release-cycle/sage-3.0.rc1/local/bin/Singular
    args: ['/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/bin/Singular', '-t', '--ticks-per-sec', '1000']
    patterns:
        >
    buffer (last 100 chars):
    before (last 100 chars): ring sage4=0,x,lp;

    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 1
    pid: 19207
    child_fd: 3
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 1000
    searchwindowsize: None
    delaybeforesend: 0
    Singular crashed executing ring sage4=0,x,lp;
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_16
   1 of   3 in __main__.example_17
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/.doctest_expect.py
         [7.5 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/interfaces/expect.py
Total time for all tests: 7.5 seconds
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.rc1$   
```


Thoughts?

Cheers,

Michael



---

archive/issue_comments_016322.json:
```json
{
    "body": "Attachment [sage-2419-followup.patch](tarball://root/attachments/some-uuid/ticket2419/sage-2419-followup.patch) by @williamstein created at 2008-04-21 01:52:26",
    "created_at": "2008-04-21T01:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16322",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2419-followup.patch](tarball://root/attachments/some-uuid/ticket2419/sage-2419-followup.patch) by @williamstein created at 2008-04-21 01:52:26



---

archive/issue_comments_016323.json:
```json
{
    "body": "Merged sage-2419-followup.patch in Sage 3.0.rc1",
    "created_at": "2008-04-21T02:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2419#issuecomment-16323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-2419-followup.patch in Sage 3.0.rc1
