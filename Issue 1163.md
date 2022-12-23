# Issue 1163: assume seems to have some undesired side-effects

archive/issues_001163.json:
```json
{
    "body": "Assignee: was\n\nCC:  burcin robertwb jason robert.marik\n\n\n```\nsage: assume(x > 0)\nsage: sqrt(x^2)\nx\nsage: assume(x < 0)\nsage: sqrt(x^2)\nx\n```\n\n\nMaybe it is not allowed to make two assumptions on the same variable, without any forget inbetween, anyway the documentation should be clear about this, or a warning should be issued.\nAlso, is there a way to know which assumptions were made on a given variable (like about in\nMaple)?\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1163\n\n",
    "created_at": "2007-11-13T11:58:31Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "assume seems to have some undesired side-effects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1163",
    "user": "zimmerma"
}
```
Assignee: was

CC:  burcin robertwb jason robert.marik


```
sage: assume(x > 0)
sage: sqrt(x^2)
x
sage: assume(x < 0)
sage: sqrt(x^2)
x
```


Maybe it is not allowed to make two assumptions on the same variable, without any forget inbetween, anyway the documentation should be clear about this, or a warning should be issued.
Also, is there a way to know which assumptions were made on a given variable (like about in
Maple)?



Issue created by migration from https://trac.sagemath.org/ticket/1163





---

archive/issue_comments_007116.json:
```json
{
    "body": "A couple of notes:\n\nThe \"assumptions()\" command lists assumptions.  See assumptions? for documentation.\n\nIt seems that the order in which the assumptions are made matters (only the first assumption is used below).  \n\nShould assume complain if we say that x>0 and x<0?\n\n\n```\nsage: assumptions()\n[]\nsage: assume(x<0)\nsage: sqrt(x^2)\n-x\nsage: assume(x>0)\nsage: sqrt(x^2)\n-x\nsage: assumptions()\n[x < 0, x > 0]\nsage: forget()\nsage: assumptions()\n[]\nsage: assume(x>0)\nsage: assume(x<0)\nsage: assumptions()\n[x > 0, x < 0]\nsage: sqrt(x^2)\nx\n```\n",
    "created_at": "2007-11-13T20:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7116",
    "user": "jason"
}
```

A couple of notes:

The "assumptions()" command lists assumptions.  See assumptions? for documentation.

It seems that the order in which the assumptions are made matters (only the first assumption is used below).  

Should assume complain if we say that x>0 and x<0?


```
sage: assumptions()
[]
sage: assume(x<0)
sage: sqrt(x^2)
-x
sage: assume(x>0)
sage: sqrt(x^2)
-x
sage: assumptions()
[x < 0, x > 0]
sage: forget()
sage: assumptions()
[]
sage: assume(x>0)
sage: assume(x<0)
sage: assumptions()
[x > 0, x < 0]
sage: sqrt(x^2)
x
```




---

archive/issue_comments_007117.json:
```json
{
    "body": "Sorry I did not know about the assumptions() command. Maybe assume? should point to it.\nIs a SEE ALSO section possible in the documentation? Also consider (from Wester's test suite):\n\n\n```\nsage: assume(x>=y, y>=z,z>=x)\nsage: assumptions()\n[x >= y, y >= z, z >= x]\nsage: print bool(x==z)\nFalse\n```\n\n\nYes assume should complain if we say that x>0 and x<0 (at least if it can lead to wrong results).",
    "created_at": "2007-11-13T22:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7117",
    "user": "zimmerma"
}
```

Sorry I did not know about the assumptions() command. Maybe assume? should point to it.
Is a SEE ALSO section possible in the documentation? Also consider (from Wester's test suite):


```
sage: assume(x>=y, y>=z,z>=x)
sage: assumptions()
[x >= y, y >= z, z >= x]
sage: print bool(x==z)
False
```


Yes assume should complain if we say that x>0 and x<0 (at least if it can lead to wrong results).



---

archive/issue_comments_007118.json:
```json
{
    "body": "More strange results:\n\n```\nsage: assume(x > 0)\nsage: bool (x <> 1)\nTrue\n```\n\nand:\n\n```\nsage: assume(x <= 1, x >= 1)\nsage: bool(x==1)\nFalse\n```\n",
    "created_at": "2007-11-13T22:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7118",
    "user": "zimmerma"
}
```

More strange results:

```
sage: assume(x > 0)
sage: bool (x <> 1)
True
```

and:

```
sage: assume(x <= 1, x >= 1)
sage: bool(x==1)
False
```




---

archive/issue_comments_007119.json:
```json
{
    "body": "Those are some unsettling results.  I don't know if this is the easiest route, but it seems like QEPCAD could handle some of these if it were integrated into SAGE.  For example, we can ask QEPCAD the following questions.  In these, (Ex) means \"there exists an x\" and (Ax) means \"For all x\" and \"/=\" means  \"not equal\".\n\n* `(Ex)(Ey)(Ez) [ x>=y /\\ y>=z /\\ z>=x /\\ x/=z]` (returns False)\n* `(Ex) [ x>0 /\\ x/= 1]` (returns True)\n* `(Ex) [ x>0 /\\ x=1]` (returns True)\n* `(Ex) [ x<=1 /\\ x>=1 /\\ x /= 1]` (returns False)\n\nHere's another example:\n\n* `(Ax)(Ay) [x<sup>2+y</sup>2>=0]` (returns True).\n\nWe could ask much more general questions too.\n\nI've been (very slowly) working on interfacing QEPCAD to SAGE, but lack of time and the learning process of making an interface is slowing me down.  Also, we need to follow up on the license issue.  For progress in this interface, see #772 )",
    "created_at": "2007-11-14T00:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7119",
    "user": "jason"
}
```

Those are some unsettling results.  I don't know if this is the easiest route, but it seems like QEPCAD could handle some of these if it were integrated into SAGE.  For example, we can ask QEPCAD the following questions.  In these, (Ex) means "there exists an x" and (Ax) means "For all x" and "/=" means  "not equal".

* `(Ex)(Ey)(Ez) [ x>=y /\ y>=z /\ z>=x /\ x/=z]` (returns False)
* `(Ex) [ x>0 /\ x/= 1]` (returns True)
* `(Ex) [ x>0 /\ x=1]` (returns True)
* `(Ex) [ x<=1 /\ x>=1 /\ x /= 1]` (returns False)

Here's another example:

* `(Ax)(Ay) [x<sup>2+y</sup>2>=0]` (returns True).

We could ask much more general questions too.

I've been (very slowly) working on interfacing QEPCAD to SAGE, but lack of time and the learning process of making an interface is slowing me down.  Also, we need to follow up on the license issue.  For progress in this interface, see #772 )



---

archive/issue_comments_007120.json:
```json
{
    "body": "Apparently Maxima complains (behind the scenes?):\n\n\n```\nMaxima 5.12.0 http://maxima.sourceforge.net\nUsing Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) assume(x<0);\n(%o1)                               [x < 0]\n(%i2) assume(x>0);\n(%o2)                           [inconsistent]\n```\n",
    "created_at": "2007-11-14T00:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7120",
    "user": "jason"
}
```

Apparently Maxima complains (behind the scenes?):


```
Maxima 5.12.0 http://maxima.sourceforge.net
Using Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x<0);
(%o1)                               [x < 0]
(%i2) assume(x>0);
(%o2)                           [inconsistent]
```




---

archive/issue_comments_007121.json:
```json
{
    "body": "More results from Maxima:\n\n\n```\n\nMaxima 5.12.0 http://maxima.sourceforge.net\nUsing Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) assume(x>=y,y>=z,z>=x);\n(%o1)                      [x >= y, y >= z, z >= x]\n(%i2) is(x=z);\n(%o2)                                false\n```\n\n\n\n```\nMaxima 5.12.0 http://maxima.sourceforge.net\nUsing Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) assume(x>0);\n(%o1)                               [x > 0]\n(%i2) is(x#1);\n(%o2)                                true\n```\n\n\nand\n\n\n```\n\nMaxima 5.12.0 http://maxima.sourceforge.net\nUsing Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) assume(x<=1);\n(%o1)                              [x <= 1]\n(%i2) assume(x>=1);\n(%o2)                              [x >= 1]\n(%i3) is(x=1);\n(%o3)                                false\n```\n\n\nSo it seems like the problem is the Maxima assumptions engine.  According to the documentation at  http://maxima.sourceforge.net/docs/manual/en/maxima_11.html \n\n```\nMaxima's deduction mechanism is not very strong; there are many obvious consequences which cannot be determined by is. This is a known weakness.\n```\n",
    "created_at": "2007-11-14T00:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7121",
    "user": "jason"
}
```

More results from Maxima:


```

Maxima 5.12.0 http://maxima.sourceforge.net
Using Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x>=y,y>=z,z>=x);
(%o1)                      [x >= y, y >= z, z >= x]
(%i2) is(x=z);
(%o2)                                false
```



```
Maxima 5.12.0 http://maxima.sourceforge.net
Using Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x>0);
(%o1)                               [x > 0]
(%i2) is(x#1);
(%o2)                                true
```


and


```

Maxima 5.12.0 http://maxima.sourceforge.net
Using Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x<=1);
(%o1)                              [x <= 1]
(%i2) assume(x>=1);
(%o2)                              [x >= 1]
(%i3) is(x=1);
(%o3)                                false
```


So it seems like the problem is the Maxima assumptions engine.  According to the documentation at  http://maxima.sourceforge.net/docs/manual/en/maxima_11.html 

```
Maxima's deduction mechanism is not very strong; there are many obvious consequences which cannot be determined by is. This is a known weakness.
```




---

archive/issue_comments_007122.json:
```json
{
    "body": "One more note: \n\nQEPCAD also simplifies the expression [x>=y /\\ y>=z /\\ z>= x] to [y-x=0 /\\ z-y = 0].",
    "created_at": "2007-11-14T01:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7122",
    "user": "jason"
}
```

One more note: 

QEPCAD also simplifies the expression [x>=y /\ y>=z /\ z>= x] to [y-x=0 /\ z-y = 0].



---

archive/issue_comments_007123.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-03-16T20:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7123",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_007124.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T20:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7124",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007125.json:
```json
{
    "body": "At the very least this ticket should upgrade the documentation for assume? and assumptions?  to point out that one should always forget() before assuming something new about a variable.\n\nA related ticket is #3277, which would implement a block to automatically call assume and forget if desired.  Also, #772 is now an experimental spkg.",
    "created_at": "2009-01-29T16:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7125",
    "user": "kcrisman"
}
```

At the very least this ticket should upgrade the documentation for assume? and assumptions?  to point out that one should always forget() before assuming something new about a variable.

A related ticket is #3277, which would implement a block to automatically call assume and forget if desired.  Also, #772 is now an experimental spkg.



---

archive/issue_comments_007126.json:
```json
{
    "body": "A very interesting exchange on the Maxima list indicates that Maxima isn't so much at fault as Sage's use of it, even in the sketchy-looking cases.  This is Robert Dodier's response:\n\n```\nWell, it's true that assume isn't very strong, but at least Maxima\nseems to be able to figure out these examples.\nWhat you want is equal(x, z) instead of x = z.\n\"=\" is essentially identity (i.e. are the left and right-hand sides\nthe same expression), while equal is equivalence (equal value).\nLikewise the distinction between \"#\" and notequal.\n\nHere's what I get with Maxima 5.19.2.\n\n(%i2)  assume(x>=y,y>=z,z>=x);\n(%o2)                      [x >= y, y >= z, z >= x]\n(%i3) is(equal(x,z));\n(%o3)                                true\n(%i4) assume(a>=1,1>=a);\n(%o4)                          [a >= 1, a <= 1]\n(%i5) is(equal(a,1));\n(%o5)                                true\n(%i6) assume(b>1);\n(%o6)                               [b > 1]\n(%i7) is(equal(b,1));\n(%o7)                                false\n(%i8) is(notequal(b,1));\n(%o8)                                true\n\nI think %o3, %o5, %o7, and %o8 are all as expected, right?\n```\n\n\nSo the real issue is that Sage's \"==\" is more at Maxima's equal(), while Sage's \"is\" is more at Maxima's \"=\".  Fixing this will probably require some interesting futzing with the Maxima parser, though, since usually we want == to become =, I think.",
    "created_at": "2009-09-28T18:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7126",
    "user": "kcrisman"
}
```

A very interesting exchange on the Maxima list indicates that Maxima isn't so much at fault as Sage's use of it, even in the sketchy-looking cases.  This is Robert Dodier's response:

```
Well, it's true that assume isn't very strong, but at least Maxima
seems to be able to figure out these examples.
What you want is equal(x, z) instead of x = z.
"=" is essentially identity (i.e. are the left and right-hand sides
the same expression), while equal is equivalence (equal value).
Likewise the distinction between "#" and notequal.

Here's what I get with Maxima 5.19.2.

(%i2)  assume(x>=y,y>=z,z>=x);
(%o2)                      [x >= y, y >= z, z >= x]
(%i3) is(equal(x,z));
(%o3)                                true
(%i4) assume(a>=1,1>=a);
(%o4)                          [a >= 1, a <= 1]
(%i5) is(equal(a,1));
(%o5)                                true
(%i6) assume(b>1);
(%o6)                               [b > 1]
(%i7) is(equal(b,1));
(%o7)                                false
(%i8) is(notequal(b,1));
(%o8)                                true

I think %o3, %o5, %o7, and %o8 are all as expected, right?
```


So the real issue is that Sage's "==" is more at Maxima's equal(), while Sage's "is" is more at Maxima's "=".  Fixing this will probably require some interesting futzing with the Maxima parser, though, since usually we want == to become =, I think.



---

archive/issue_comments_007127.json:
```json
{
    "body": "Another comment:\nWith Pynac symbolics, we do not (unfortunately?) simplify sqrt(x^2) even when we assume things about it.  Interestingly, that is not true for other things, such as a neat example in the documentation.\n\n```\nsage: assume(x<0)\nsage: sqrt(x^2)\nsqrt(x^2)\nsage: sqrt(x^2).simplify() # doesn't simplify this\nsqrt(x^2)\nsage: sqrt(x^2).simplify_full()  # does what used to happen\n-x\nsage: assumptions()\n[x < 0]\nsage: forget()\nsage: assume(x,'integer')\nsage: sin(x*pi)\nsin(pi*x)\nsage: sin(x*pi).simplify() # nice simplification\n0\nsage: assumptions()\n[x is integer]\nsage: forget()\n```\n\nSo it's good the bug was discovered when it was.",
    "created_at": "2009-10-01T14:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7127",
    "user": "kcrisman"
}
```

Another comment:
With Pynac symbolics, we do not (unfortunately?) simplify sqrt(x^2) even when we assume things about it.  Interestingly, that is not true for other things, such as a neat example in the documentation.

```
sage: assume(x<0)
sage: sqrt(x^2)
sqrt(x^2)
sage: sqrt(x^2).simplify() # doesn't simplify this
sqrt(x^2)
sage: sqrt(x^2).simplify_full()  # does what used to happen
-x
sage: assumptions()
[x < 0]
sage: forget()
sage: assume(x,'integer')
sage: sin(x*pi)
sin(pi*x)
sage: sin(x*pi).simplify() # nice simplification
0
sage: assumptions()
[x is integer]
sage: forget()
```

So it's good the bug was discovered when it was.



---

archive/issue_comments_007128.json:
```json
{
    "body": "Okay, the following patch (which depends on #7084, I think), resolves **most** of the issues in this ticket.  See below for the one it doesn't, and comments.\n\n```\nsage: assume(x<=1)\nsage: assume(x>=1)\nsage: assumptions()\n[x <= 1, x >= 1]  # so far, so good\nsage: b = x!=1\nsage: b.__nonzero__() \nTrue # WRONG\nsage: bool(b) \nTrue # WRONG\nsage: bool(x==1)\nTrue # right!\nsage: forget()\nsage: var('x,y,z')\n(x, y, z)\nsage: assume(x>=y,y>=z,z>=x)\nsage: assumptions()\n[x >= y, y >= z, z >= x]\nsage: bool(x==z)\nTrue # right!\nsage: forget()\nsage: assume(x>0)\nsage: bool(x<>1) # NO!\nTrue\nsage: bool(x!=1) # NO!  And note that Python considers <> and != to be identical\nTrue\nsage: bool(x==1)\nFalse # right!\n```\n\nI've narrowed the problem down to the fact that __nonzero__ has the following lines:\n\n```\n            res = relational_to_bool(self._gobj)\n            if res:\n                return True\n```\n\nIf you put this code after determining whether you need assumptions, practically every evaluation of bool() yields an infinite loop.  But for some reason the function relational_to_bool (like all these Ginac functions, completely unsearchable because they live somewhere outside of devel/sage) doesn't send (at least) != to the assumptions.  Here is the wrapper code, in c_lib/include/ginac_wrap.h:\n\n```\nbool relational_to_bool(const ex& e) {\n    if (ex_to<relational>(e))\n\treturn 1;\n    else\n\treturn 0;\n}\n```\n\nNow what?  The documentation of ex_to in Ginac, even when I found it on their website, really only will make sense to someone with good C++ knowledge.",
    "created_at": "2009-10-01T15:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7128",
    "user": "kcrisman"
}
```

Okay, the following patch (which depends on #7084, I think), resolves **most** of the issues in this ticket.  See below for the one it doesn't, and comments.

```
sage: assume(x<=1)
sage: assume(x>=1)
sage: assumptions()
[x <= 1, x >= 1]  # so far, so good
sage: b = x!=1
sage: b.__nonzero__() 
True # WRONG
sage: bool(b) 
True # WRONG
sage: bool(x==1)
True # right!
sage: forget()
sage: var('x,y,z')
(x, y, z)
sage: assume(x>=y,y>=z,z>=x)
sage: assumptions()
[x >= y, y >= z, z >= x]
sage: bool(x==z)
True # right!
sage: forget()
sage: assume(x>0)
sage: bool(x<>1) # NO!
True
sage: bool(x!=1) # NO!  And note that Python considers <> and != to be identical
True
sage: bool(x==1)
False # right!
```

I've narrowed the problem down to the fact that __nonzero__ has the following lines:

```
            res = relational_to_bool(self._gobj)
            if res:
                return True
```

If you put this code after determining whether you need assumptions, practically every evaluation of bool() yields an infinite loop.  But for some reason the function relational_to_bool (like all these Ginac functions, completely unsearchable because they live somewhere outside of devel/sage) doesn't send (at least) != to the assumptions.  Here is the wrapper code, in c_lib/include/ginac_wrap.h:

```
bool relational_to_bool(const ex& e) {
    if (ex_to<relational>(e))
	return 1;
    else
	return 0;
}
```

Now what?  The documentation of ex_to in Ginac, even when I found it on their website, really only will make sense to someone with good C++ knowledge.



---

archive/issue_comments_007129.json:
```json
{
    "body": "Attachment\n\nBased on 4.1.2.alpha4, depends on #7084",
    "created_at": "2009-10-01T15:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7129",
    "user": "kcrisman"
}
```

Attachment

Based on 4.1.2.alpha4, depends on #7084



---

archive/issue_comments_007130.json:
```json
{
    "body": "Oh, and just for the record, continuing in the same session, where we assumed x>0:\n\n```\nsage: bool(x>1)\nFalse # right!\nsage: bool(x>-1)\nTrue # right!\n```\n\nSo the problem really does seem to be the Ginac handling of !=, not something else.",
    "created_at": "2009-10-01T15:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7130",
    "user": "kcrisman"
}
```

Oh, and just for the record, continuing in the same session, where we assumed x>0:

```
sage: bool(x>1)
False # right!
sage: bool(x>-1)
True # right!
```

So the problem really does seem to be the Ginac handling of !=, not something else.



---

archive/issue_comments_007131.json:
```json
{
    "body": "Attachment\n\nBased on 4.1.2.alpha4, depends on #7084",
    "created_at": "2009-10-02T15:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7131",
    "user": "kcrisman"
}
```

Attachment

Based on 4.1.2.alpha4, depends on #7084



---

archive/issue_comments_007132.json:
```json
{
    "body": "The non-experimental patch resolves all but one of the issues above (about which more below).   It also fixes a SLEW of subtle problems and provides better checking in the assumptions code, and fixes a variety of doctests which are improvements (!) based on making assumptions better.   I didn't end up changing the documentation to tell people to use forget, but instead gave lots of examples of what Errors you get if you assume something redundant or inconsistent.\n\nThe one \"problem\" which is still extant is the following:\n\n```\nsage: assume(x>0)\nsage: bool(x!=1) \nTrue\n```\n\n\nThis is something to which Maxima replies 'unknown', which is a lot better than True or False.  However, Sage doesn't currently have that as an option (that would be a separate ticket, and not necessarily a desirable one).   Further, since anytime one compares a symbolic variable, e.g.\n\n```\ndef func(x,y):\n    if x is not y:\n        do something great\n    else:\n        blow a gasket\n```\n\nExpression.__nonzero__ is called, we are forced to have x!=1 be True, since x==1 is False, seeing as != and == have opposite truth tables.  For an example of what can go wrong, see the change made in this patch to desolvers.py, where having x!=1 be False originally meant there was no dependent variable; this one was fixable, but the fact that symbolic matrices essentially all go to zero (!) after making that change was much worse.  \n\nSo I have left it alone after checking as many cases as I could, and we'll just have to live with it, unless someone can figure out how to get around this.  I think it's really just a conflict between wanting to say that x!=1 is True unless you are sure that x==1, and wanting to say that x!=1 is False unless you are sure that x!=1; there is no nonstandard logic option for Python.",
    "created_at": "2009-10-02T16:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7132",
    "user": "kcrisman"
}
```

The non-experimental patch resolves all but one of the issues above (about which more below).   It also fixes a SLEW of subtle problems and provides better checking in the assumptions code, and fixes a variety of doctests which are improvements (!) based on making assumptions better.   I didn't end up changing the documentation to tell people to use forget, but instead gave lots of examples of what Errors you get if you assume something redundant or inconsistent.

The one "problem" which is still extant is the following:

```
sage: assume(x>0)
sage: bool(x!=1) 
True
```


This is something to which Maxima replies 'unknown', which is a lot better than True or False.  However, Sage doesn't currently have that as an option (that would be a separate ticket, and not necessarily a desirable one).   Further, since anytime one compares a symbolic variable, e.g.

```
def func(x,y):
    if x is not y:
        do something great
    else:
        blow a gasket
```

Expression.__nonzero__ is called, we are forced to have x!=1 be True, since x==1 is False, seeing as != and == have opposite truth tables.  For an example of what can go wrong, see the change made in this patch to desolvers.py, where having x!=1 be False originally meant there was no dependent variable; this one was fixable, but the fact that symbolic matrices essentially all go to zero (!) after making that change was much worse.  

So I have left it alone after checking as many cases as I could, and we'll just have to live with it, unless someone can figure out how to get around this.  I think it's really just a conflict between wanting to say that x!=1 is True unless you are sure that x==1, and wanting to say that x!=1 is False unless you are sure that x!=1; there is no nonstandard logic option for Python.



---

archive/issue_comments_007133.json:
```json
{
    "body": "Okay, with respect to [this discussion](http://groups.google.com/group/sage-devel/browse_thread/thread/ae7d15985d4735cb) on this update adds correct parsing of Maxima output with #, thus:\n\n```\nsage: a = maxima(\"x#0\")\nsage: a.sage()\nx != 0\n```\n\nApply only 'final' patch.",
    "created_at": "2009-11-10T02:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7133",
    "user": "kcrisman"
}
```

Okay, with respect to [this discussion](http://groups.google.com/group/sage-devel/browse_thread/thread/ae7d15985d4735cb) on this update adds correct parsing of Maxima output with #, thus:

```
sage: a = maxima("x#0")
sage: a.sage()
x != 0
```

Apply only 'final' patch.



---

archive/issue_comments_007134.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-10T02:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7134",
    "user": "kcrisman"
}
```

Attachment



---

archive/issue_comments_007135.json:
```json
{
    "body": "The code looks good and gives important improvements in Sage. The patch should be installed on the top of #385 (which has been merged in 4.2.1).\n\nPases tests in sage/calculus and sage/symbolic\n\nMore changes in desolvers.py should be done, if the patch is applied on the top of patch #6479, which already got positive review and introduces another lines like \n\n```\nivars = [t for t in ivars if t != dvar] \n```\n\nwhich now became problematic.\n\nIf it passes all tests and builds documentation (runnning now, takes a long time on my PC) I'll switch the status to posistive review.",
    "created_at": "2009-11-10T07:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7135",
    "user": "robert.marik"
}
```

The code looks good and gives important improvements in Sage. The patch should be installed on the top of #385 (which has been merged in 4.2.1).

Pases tests in sage/calculus and sage/symbolic

More changes in desolvers.py should be done, if the patch is applied on the top of patch #6479, which already got positive review and introduces another lines like 

```
ivars = [t for t in ivars if t != dvar] 
```

which now became problematic.

If it passes all tests and builds documentation (runnning now, takes a long time on my PC) I'll switch the status to posistive review.



---

archive/issue_comments_007136.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-10T08:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7136",
    "user": "robert.marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_007137.json:
```json
{
    "body": "When running \"make test\" I got \n\n```\nsage -t  \"/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx\"\n**********************************************************************\nFile \"/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx\", line 72:\n    sage: v.stats_skew()\nExpected:\n    0.0\nGot:\n    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?\n    0.0\n**********************************************************************\n```\n\nBut if I run doctesting by hand to this file only, everything is O.K.\n\nSince this is syntax warinng and not error, I give positiev review. But this should be fiexd as well.",
    "created_at": "2009-11-10T08:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7137",
    "user": "robert.marik"
}
```

When running "make test" I got 

```
sage -t  "/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx"
**********************************************************************
File "/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx", line 72:
    sage: v.stats_skew()
Expected:
    0.0
Got:
    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    0.0
**********************************************************************
```

But if I run doctesting by hand to this file only, everything is O.K.

Since this is syntax warinng and not error, I give positiev review. But this should be fiexd as well.



---

archive/issue_comments_007138.json:
```json
{
    "body": "Replying to [comment:17 robert.marik]:\n> When running \"make test\" I got \n> {{{\n> sage -t  \"/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx\"\n> **********************************************************************\n> File \"/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx\", line 72:\n>     sage: v.stats_skew()\n> Expected:\n>     0.0\n> Got:\n>     doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?\n>     0.0\n> **********************************************************************\n> }}}\n> But if I run doctesting by hand to this file only, everything is O.K.\n> \n> Since this is syntax warinng and not error, I give positiev review. But this should be fiexd as well.\n> \n\nThis is actually #6825, so it's unrelated.\n\nDepending on how the release manager does things, we'll see which patch to resolve the != thing on; it shouldn't be a big deal.",
    "created_at": "2009-11-10T14:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7138",
    "user": "kcrisman"
}
```

Replying to [comment:17 robert.marik]:
> When running "make test" I got 
> {{{
> sage -t  "/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx"
> **********************************************************************
> File "/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx", line 72:
>     sage: v.stats_skew()
> Expected:
>     0.0
> Got:
>     doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?
>     0.0
> **********************************************************************
> }}}
> But if I run doctesting by hand to this file only, everything is O.K.
> 
> Since this is syntax warinng and not error, I give positiev review. But this should be fiexd as well.
> 

This is actually #6825, so it's unrelated.

Depending on how the release manager does things, we'll see which patch to resolve the != thing on; it shouldn't be a big deal.



---

archive/issue_comments_007139.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1163#issuecomment-7139",
    "user": "mhansen"
}
```

Resolution: fixed
