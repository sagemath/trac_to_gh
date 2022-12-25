# Issue 6672: Elliptic curve isogeny coercion of output to codomain curve takes too long

archive/issues_006672.json:
```json
{
    "body": "Assignee: shumow\n\nCC:  shumow@gmail.com\n\nAs per William's debugging, the correct behavior is to coerce the tuple with check=False.\n\nOn Mon, Aug 3, 2009 at 6:10 PM, VictorMiller<victorsmiller`@`gmail.com> wrote:\n>\n> Sorry, here's the definition of Q:\n>\n> Q = E.random_element()\n>\n> Victor\n>\n> On Aug 3, 8:45 pm, Simon King <simon.k...`@`nuigalway.ie> wrote:\n>> Hi!\n\n>>\n>> On 4 Aug., 02:31, VictorMiller <victorsmil...`@`gmail.com> wrote:\n\n>>\n>> > Here are the commands I used:\n\n>>\n>> > qq = [z for z in primes(100000,100000+100) if (z%12) == 11]\n>> > E = EllipticCurve(j=GF(qq[0])(1728))\n>> > # E has qq[0]+1 points over GF(qq[0])\n>> > factor(qq[0]+1)\n>> > P = ((qq[0]+1)//3)*E.random_element()\n>> > K = [E(0),P,-P]\n>> > phi = E.isogeny(K)\n\n\nThere appears to be a memory leak -- or some sort of caching (!) -- in\nthe code to evaluate phi.  This is likely impacting the complexity of\nthe some code that is run during the computation of phi(P).  The log\nbelow shows that memory usage increases upon evaluation of phi(P):\n\n```\nsage: get_memory_usage()\n210.109375\nsage: timeit('phi(P)')\n125 loops, best of 3: 7.13 ms per loop\nsage: get_memory_usage()\n210.609375\nsage: timeit('phi(P)')\n125 loops, best of 3: 7.3 ms per loop\nsage: get_memory_usage()\n211.109375\nsage: timeit('phi(P)')\n125 loops, best of 3: 7.49 ms per loop\nsage: get_memory_usage()\n211.609375\nsage: timeit('phi(P)')\n125 loops, best of 3: 7.69 ms per loop\nsage: get_memory_usage()\n212.109375\n```\n\nNow I looked at the source code for the function phi(P) =\nphi.__call__(P) and bisected by putting early returns in.  If you\nchange\n\n```\n       else:\n           outP = self.__E2(outP)\n```\nto\n\n```\n       else:\n           return outP\n           outP = self.__E2(outP)\n```\n\nin that function in ell_curve_isogeny.py (around line 875), then the\nleak and slowdown vanishes.\n\nThus the real problem is in the \"trivial\" line \"self.__E2(outP)\",\nwhich by the way takes even in good cases like 10 times as long as the\nrest of the whole function put together.  Indeed, coercing a point\ninto a curve is a horrendous disaster (this is the real problem,\nforget the isogeny stuff):\n\n```\nsage: get_memory_usage()\n195.81640625\nsage: timeit('E(P)')\n625 loops, best of 3: 4.24 ms per loop\nsage: get_memory_usage()\n201.31640625\n```\n\nIn fact, the function E.point is to blame, evidently:\n\n```\nsage: timeit('E.point(P)')\n125 loops, best of 3: 4.13 ms per loop\nsage: get_memory_usage()\n202.08984375\nsage: timeit('E.point(P)')\n125 loops, best of 3: 4.4 ms per loop\nsage: get_memory_usage()\n203.08984375\n```\n\n... but *ONLY* with check=True (the default):\n\n```\nsage: timeit('E.point(P,check=False)')\n625 loops, best of 3: 8.26 \u00b5s per loop\nsage: get_memory_usage()\n203.08984375\nsage: timeit('E.point(P,check=False)')\n625 loops, best of 3: 7.29 \u00b5s per loop\nsage: get_memory_usage()\n203.08984375\n```\n\nI.e., we get a speedup of a factor of nearly 1000 by using\ncheck=False, plus the leak goes away.    So in the check -- which\ninvolves arithmetic -- maybe the coercion model is surely being\ninvoked at some point (I guess), and that is perhaps caching\ninformation, thus memory usage goes up and performance goes down.  I\ndon't know, I'm not looking further.\n\nGoing back to your original problem, if I change in ell_curve_isogeny.py\n\n```\n       else:\n           outP = self.__E2(outP)\n```\n\nto\n\n```\n       else:\n           outP = self.__E2.point(outP,check=False)\n```\n\nthen we have the following, which is exactly what you would hope for\n(things are fast,  no slowdown).\n\n```\nsage: qq = [z for z in primes(100000,100000+100) if (z%12) == 11]\nsage: E = EllipticCurve(j=GF(qq[0])(1728))\nsage: # E has qq[0]+1 points over GF(qq[0])\nsage: factor(qq[0]+1)\n2^2 * 3 * 5 * 1667\nsage: P = ((qq[0]+1)//3)*E.random_element()\nsage: K = [E(0),P,-P]\nsage: phi = E.isogeny(K)\nsage: get_memory_usage()\n190.56640625\nsage: timeit('phi(P)')\n625 loops, best of 3: 69.8 \u00b5s per loop\nsage: for i in xrange(20): timeit('phi(P)')\n\n....:\n625 loops, best of 3: 69.3 \u00b5s per loop\n625 loops, best of 3: 69.3 \u00b5s per loop\n625 loops, best of 3: 69.6 \u00b5s per loop\n625 loops, best of 3: 69.9 \u00b5s per loop\n625 loops, best of 3: 69.8 \u00b5s per loop\n625 loops, best of 3: 70 \u00b5s per loop\n625 loops, best of 3: 71.2 \u00b5s per loop\n625 loops, best of 3: 69.3 \u00b5s per loop\n625 loops, best of 3: 70.8 \u00b5s per loop\n625 loops, best of 3: 69.2 \u00b5s per loop\n625 loops, best of 3: 70.2 \u00b5s per loop\n625 loops, best of 3: 70.7 \u00b5s per loop\n625 loops, best of 3: 70 \u00b5s per loop\n625 loops, best of 3: 71 \u00b5s per loop\n625 loops, best of 3: 70 \u00b5s per loop\n625 loops, best of 3: 70.2 \u00b5s per loop\n625 loops, best of 3: 70.1 \u00b5s per loop\n625 loops, best of 3: 70 \u00b5s per loop\n625 loops, best of 3: 70.1 \u00b5s per loop\n625 loops, best of 3: 70.1 \u00b5s per loop\n```\n\nThe above change is very sensible, since we know that outP is on\nself.__E2, so should directly create a point on E2 and not check again\nthat our point is really on E2 (which is very expensive).\n\nI hope the above is helpful and that somebody opens a trac ticket and\nsubmits a patch.    I have to get back to what I was doing...   I also\nhope the above email provides some ideas as to how to quickly get to\nthe bottom of questions like this.  Note that I did all this in < 10\nminutes by using ?? to see where relevant source code is, putting in\nsome return statements (often better than print statements), and\nknowing that P(...) means P.__call__.\n\n -- William\n\nIssue created by migration from https://trac.sagemath.org/ticket/6672\n\n",
    "created_at": "2009-08-04T02:21:57Z",
    "labels": [
        "component: elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Elliptic curve isogeny coercion of output to codomain curve takes too long",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6672",
    "user": "https://trac.sagemath.org/admin/accounts/users/shumow"
}
```
Assignee: shumow

CC:  shumow@gmail.com

As per William's debugging, the correct behavior is to coerce the tuple with check=False.

On Mon, Aug 3, 2009 at 6:10 PM, VictorMiller<victorsmiller`@`gmail.com> wrote:
>
> Sorry, here's the definition of Q:
>
> Q = E.random_element()
>
> Victor
>
> On Aug 3, 8:45 pm, Simon King <simon.k...`@`nuigalway.ie> wrote:
>> Hi!

>>
>> On 4 Aug., 02:31, VictorMiller <victorsmil...`@`gmail.com> wrote:

>>
>> > Here are the commands I used:

>>
>> > qq = [z for z in primes(100000,100000+100) if (z%12) == 11]
>> > E = EllipticCurve(j=GF(qq[0])(1728))
>> > # E has qq[0]+1 points over GF(qq[0])
>> > factor(qq[0]+1)
>> > P = ((qq[0]+1)//3)*E.random_element()
>> > K = [E(0),P,-P]
>> > phi = E.isogeny(K)


There appears to be a memory leak -- or some sort of caching (!) -- in
the code to evaluate phi.  This is likely impacting the complexity of
the some code that is run during the computation of phi(P).  The log
below shows that memory usage increases upon evaluation of phi(P):

```
sage: get_memory_usage()
210.109375
sage: timeit('phi(P)')
125 loops, best of 3: 7.13 ms per loop
sage: get_memory_usage()
210.609375
sage: timeit('phi(P)')
125 loops, best of 3: 7.3 ms per loop
sage: get_memory_usage()
211.109375
sage: timeit('phi(P)')
125 loops, best of 3: 7.49 ms per loop
sage: get_memory_usage()
211.609375
sage: timeit('phi(P)')
125 loops, best of 3: 7.69 ms per loop
sage: get_memory_usage()
212.109375
```

Now I looked at the source code for the function phi(P) =
phi.__call__(P) and bisected by putting early returns in.  If you
change

```
       else:
           outP = self.__E2(outP)
```
to

```
       else:
           return outP
           outP = self.__E2(outP)
```

in that function in ell_curve_isogeny.py (around line 875), then the
leak and slowdown vanishes.

Thus the real problem is in the "trivial" line "self.__E2(outP)",
which by the way takes even in good cases like 10 times as long as the
rest of the whole function put together.  Indeed, coercing a point
into a curve is a horrendous disaster (this is the real problem,
forget the isogeny stuff):

```
sage: get_memory_usage()
195.81640625
sage: timeit('E(P)')
625 loops, best of 3: 4.24 ms per loop
sage: get_memory_usage()
201.31640625
```

In fact, the function E.point is to blame, evidently:

```
sage: timeit('E.point(P)')
125 loops, best of 3: 4.13 ms per loop
sage: get_memory_usage()
202.08984375
sage: timeit('E.point(P)')
125 loops, best of 3: 4.4 ms per loop
sage: get_memory_usage()
203.08984375
```

... but *ONLY* with check=True (the default):

```
sage: timeit('E.point(P,check=False)')
625 loops, best of 3: 8.26 µs per loop
sage: get_memory_usage()
203.08984375
sage: timeit('E.point(P,check=False)')
625 loops, best of 3: 7.29 µs per loop
sage: get_memory_usage()
203.08984375
```

I.e., we get a speedup of a factor of nearly 1000 by using
check=False, plus the leak goes away.    So in the check -- which
involves arithmetic -- maybe the coercion model is surely being
invoked at some point (I guess), and that is perhaps caching
information, thus memory usage goes up and performance goes down.  I
don't know, I'm not looking further.

Going back to your original problem, if I change in ell_curve_isogeny.py

```
       else:
           outP = self.__E2(outP)
```

to

```
       else:
           outP = self.__E2.point(outP,check=False)
```

then we have the following, which is exactly what you would hope for
(things are fast,  no slowdown).

```
sage: qq = [z for z in primes(100000,100000+100) if (z%12) == 11]
sage: E = EllipticCurve(j=GF(qq[0])(1728))
sage: # E has qq[0]+1 points over GF(qq[0])
sage: factor(qq[0]+1)
2^2 * 3 * 5 * 1667
sage: P = ((qq[0]+1)//3)*E.random_element()
sage: K = [E(0),P,-P]
sage: phi = E.isogeny(K)
sage: get_memory_usage()
190.56640625
sage: timeit('phi(P)')
625 loops, best of 3: 69.8 µs per loop
sage: for i in xrange(20): timeit('phi(P)')

....:
625 loops, best of 3: 69.3 µs per loop
625 loops, best of 3: 69.3 µs per loop
625 loops, best of 3: 69.6 µs per loop
625 loops, best of 3: 69.9 µs per loop
625 loops, best of 3: 69.8 µs per loop
625 loops, best of 3: 70 µs per loop
625 loops, best of 3: 71.2 µs per loop
625 loops, best of 3: 69.3 µs per loop
625 loops, best of 3: 70.8 µs per loop
625 loops, best of 3: 69.2 µs per loop
625 loops, best of 3: 70.2 µs per loop
625 loops, best of 3: 70.7 µs per loop
625 loops, best of 3: 70 µs per loop
625 loops, best of 3: 71 µs per loop
625 loops, best of 3: 70 µs per loop
625 loops, best of 3: 70.2 µs per loop
625 loops, best of 3: 70.1 µs per loop
625 loops, best of 3: 70 µs per loop
625 loops, best of 3: 70.1 µs per loop
625 loops, best of 3: 70.1 µs per loop
```

The above change is very sensible, since we know that outP is on
self.__E2, so should directly create a point on E2 and not check again
that our point is really on E2 (which is very expensive).

I hope the above is helpful and that somebody opens a trac ticket and
submits a patch.    I have to get back to what I was doing...   I also
hope the above email provides some ideas as to how to quickly get to
the bottom of questions like this.  Note that I did all this in < 10
minutes by using ?? to see where relevant source code is, putting in
some return statements (often better than print statements), and
knowing that P(...) means P.__call__.

 -- William

Issue created by migration from https://trac.sagemath.org/ticket/6672





---

archive/issue_comments_054720.json:
```json
{
    "body": "Attachment [trac_6672.patch](tarball://root/attachments/some-uuid/ticket6672/trac_6672.patch) by shumow created at 2009-08-04 07:44:25",
    "created_at": "2009-08-04T07:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6672#issuecomment-54720",
    "user": "https://trac.sagemath.org/admin/accounts/users/shumow"
}
```

Attachment [trac_6672.patch](tarball://root/attachments/some-uuid/ticket6672/trac_6672.patch) by shumow created at 2009-08-04 07:44:25



---

archive/issue_comments_054721.json:
```json
{
    "body": "Apply after previous",
    "created_at": "2009-08-16T17:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6672#issuecomment-54721",
    "user": "https://github.com/JohnCremona"
}
```

Apply after previous



---

archive/issue_comments_054722.json:
```json
{
    "body": "Attachment [trac_6672-point_construction2.patch](tarball://root/attachments/some-uuid/ticket6672/trac_6672-point_construction2.patch) by @JohnCremona created at 2009-08-16 17:54:07\n\nApply after previous",
    "created_at": "2009-08-16T17:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6672#issuecomment-54722",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6672-point_construction2.patch](tarball://root/attachments/some-uuid/ticket6672/trac_6672-point_construction2.patch) by @JohnCremona created at 2009-08-16 17:54:07

Apply after previous



---

archive/issue_comments_054723.json:
```json
{
    "body": "Trac just lost my long comment, explaining what I did complete with test data and timings.  Reviewer can ask me if they want to know.",
    "created_at": "2009-08-16T17:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6672#issuecomment-54723",
    "user": "https://github.com/JohnCremona"
}
```

Trac just lost my long comment, explaining what I did complete with test data and timings.  Reviewer can ask me if they want to know.



---

archive/issue_comments_054724.json:
```json
{
    "body": "Positive review.  Apply the three patches in order.\n\nTested on some random examples such as:\n\nBEFORE THE PATCHES:\n\n```\nsage: E = EllipticCurve('109a').change_ring(GF(71))\nsage: lis = E.rational_points()\nsage: P = lis[20]\nsage: timeit('E(P)')\n625 loops, best of 3: 840 \u00b5s per loop\n```\n\nAFTER THE PATCHES:\n\n```\nsage: E = EllipticCurve('109a').change_ring(GF(71))\nsage: lis = E.rational_points()\nsage: P = lis[20]\nsage: timeit('E(P)')\n625 loops, best of 3: 191 \u00b5s per loop\n```",
    "created_at": "2009-08-17T12:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6672#issuecomment-54724",
    "user": "https://github.com/aghitza"
}
```

Positive review.  Apply the three patches in order.

Tested on some random examples such as:

BEFORE THE PATCHES:

```
sage: E = EllipticCurve('109a').change_ring(GF(71))
sage: lis = E.rational_points()
sage: P = lis[20]
sage: timeit('E(P)')
625 loops, best of 3: 840 µs per loop
```

AFTER THE PATCHES:

```
sage: E = EllipticCurve('109a').change_ring(GF(71))
sage: lis = E.rational_points()
sage: P = lis[20]
sage: timeit('E(P)')
625 loops, best of 3: 191 µs per loop
```



---

archive/issue_events_015743.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2009-08-17T12:34:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6672",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6672#event-15743"
}
```



---

archive/issue_events_015744.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-23T14:25:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6672",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6672#event-15744"
}
```



---

archive/issue_comments_054725.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-23T14:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6672#issuecomment-54725",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
