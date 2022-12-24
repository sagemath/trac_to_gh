# Issue 3718: calculus -- sage treats limits involving floor and ceil completely wrong

archive/issues_003718.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n\n```\nHi,\n\nThis email is about the fact that Sage (and Maxima and sympy)\nall give the wrong answer for a certain limit, at least if one follows\nthe standard definition given at wikipedia of limit.  The limit in question\nis\n\n   lim_{x --> 0 from below}   floor(x)\n\nThis problem was reported two weeks ago by John Perry (my old\noffice might from Northern Arizona Univeristy 14 years ago, by\nthe way...)\n\nSee below for full details.\n\n> That looks to me like a bug caused by an underlying bug in maxima.\n> maxima: limit(floor(x),x,0,`minus')\n> does not finish,\n> while\n> maxima: limit(floor(x),x,0)\n> 0\n> John Cremona\n\nIn maxima it would be limit(floor(x),x,0,minus) -- i.e., no quotes, and\nthat does finish.   However the output directly from maxima\nis still 0.   I've cc'd this email to maxima-devel and Robert\nDodier, in case they have a comment.  I've also sent it to\nthe sympy list since sympy also gives the wrong answer\n(see below).\n\n\n---------------------------------------------------\nteragon-2:doc was$ sage -maxima\nMaxima 5.13.0 http://maxima.sourceforge.net\nUsing Lisp CLISP 2.46 (2008-07-02)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) limit(floor(x),x,0,minus);\n(%o1)                                  0\n(%i4) limit(ceiling(x),x,0,plus);\n(%o4)                                  0\n-------------------------------------------------\n\nIf you read the formal definition of limit, e.g., as given at\n\n     http://en.wikipedia.org/wiki/Limit_of_a_function\n\nyou'll see the output of Maxima (and sage) is just plain wrong.\n\n\n-----\n\nHere's sympy (also wrong):\n\nsage: import sympy\nsage: x = sympy.var('x')\nsage: f = sympy.floor(x)\nsage: f.limit(x, 0, '<')\n0\nsage: f.limit(x, 0, '>')\n0\n\n\n\n-----\n\nMaple does exactly the right thing of course, and uses\nbetter names -- left and right -- (imho) than Sage's \n\"minus\" and \"plus\":\n\nsage: maple('limit(floor(x),x=0,left)')\n-1\nsage: maple('limit(floor(x),x=0,right)')\n0\nsage: maple('limit(floor(x),x=0)')\nundefined\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3718\n\n",
    "created_at": "2008-07-24T10:26:47Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "calculus -- sage treats limits involving floor and ceil completely wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3718",
    "user": "@williamstein"
}
```
Assignee: @garyfurnish


```
Hi,

This email is about the fact that Sage (and Maxima and sympy)
all give the wrong answer for a certain limit, at least if one follows
the standard definition given at wikipedia of limit.  The limit in question
is

   lim_{x --> 0 from below}   floor(x)

This problem was reported two weeks ago by John Perry (my old
office might from Northern Arizona Univeristy 14 years ago, by
the way...)

See below for full details.

> That looks to me like a bug caused by an underlying bug in maxima.
> maxima: limit(floor(x),x,0,`minus')
> does not finish,
> while
> maxima: limit(floor(x),x,0)
> 0
> John Cremona

In maxima it would be limit(floor(x),x,0,minus) -- i.e., no quotes, and
that does finish.   However the output directly from maxima
is still 0.   I've cc'd this email to maxima-devel and Robert
Dodier, in case they have a comment.  I've also sent it to
the sympy list since sympy also gives the wrong answer
(see below).


---------------------------------------------------
teragon-2:doc was$ sage -maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.46 (2008-07-02)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) limit(floor(x),x,0,minus);
(%o1)                                  0
(%i4) limit(ceiling(x),x,0,plus);
(%o4)                                  0
-------------------------------------------------

If you read the formal definition of limit, e.g., as given at

     http://en.wikipedia.org/wiki/Limit_of_a_function

you'll see the output of Maxima (and sage) is just plain wrong.


-----

Here's sympy (also wrong):

sage: import sympy
sage: x = sympy.var('x')
sage: f = sympy.floor(x)
sage: f.limit(x, 0, '<')
0
sage: f.limit(x, 0, '>')
0



-----

Maple does exactly the right thing of course, and uses
better names -- left and right -- (imho) than Sage's 
"minus" and "plus":

sage: maple('limit(floor(x),x=0,left)')
-1
sage: maple('limit(floor(x),x=0,right)')
0
sage: maple('limit(floor(x),x=0)')
undefined

```


Issue created by migration from https://trac.sagemath.org/ticket/3718





---

archive/issue_comments_026380.json:
```json
{
    "body": "This is fixed by the spkg and patch at #6699.  I will post a patch with a docstring showing this when #6699 gets merged.",
    "created_at": "2009-08-24T09:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3718#issuecomment-26380",
    "user": "@aghitza"
}
```

This is fixed by the spkg and patch at #6699.  I will post a patch with a docstring showing this when #6699 gets merged.



---

archive/issue_comments_026381.json:
```json
{
    "body": "Changing assignee from @garyfurnish to @aghitza.",
    "created_at": "2009-08-24T09:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3718#issuecomment-26381",
    "user": "@aghitza"
}
```

Changing assignee from @garyfurnish to @aghitza.



---

archive/issue_comments_026382.json:
```json
{
    "body": "Here is the patch.",
    "created_at": "2009-09-29T14:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3718#issuecomment-26382",
    "user": "@kcrisman"
}
```

Here is the patch.



---

archive/issue_comments_026383.json:
```json
{
    "body": "Attachment [trac_3718-floor-limit.patch](tarball://root/attachments/some-uuid/ticket3718/trac_3718-floor-limit.patch) by @kcrisman created at 2009-09-29 14:43:45\n\nBased on 4.1.2.alpha4",
    "created_at": "2009-09-29T14:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3718#issuecomment-26383",
    "user": "@kcrisman"
}
```

Attachment [trac_3718-floor-limit.patch](tarball://root/attachments/some-uuid/ticket3718/trac_3718-floor-limit.patch) by @kcrisman created at 2009-09-29 14:43:45

Based on 4.1.2.alpha4



---

archive/issue_comments_026384.json:
```json
{
    "body": "Tests pass. Seems alright.",
    "created_at": "2009-10-01T13:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3718#issuecomment-26384",
    "user": "@TimDumol"
}
```

Tests pass. Seems alright.



---

archive/issue_comments_026385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T05:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3718#issuecomment-26385",
    "user": "@mwhansen"
}
```

Resolution: fixed
