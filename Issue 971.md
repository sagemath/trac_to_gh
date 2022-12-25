# Issue 971: [with spkg, patch] update the sympy package

archive/issues_000971.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nHi,\n\nI finally found time to write those _sage_ methods in SymPy we\ndiscussed earlier.\nThe code is here:\n\nhttp://dakol.hopto.org/sympy-sage/\n\n(we are in the state of moving from Subversion to Mercurial in SymPy).\nI created a new sympy spkg, by updating it's hg repository:\n\nhttp://dakol.hopto.org/sympy-spkg/\n\n(the change is trivial, because the src is not included). The spkg can\nbe downloaded from:\n\nhttp://dakol.fsik.cvut.cz/~ondra/sympy-0.5.5.spkg\n\nInstall with:\n\n./sage -i sympy-0.5.5.spkg\n\nNow test it. Run this in sage:\n\n---------------------------------------------\n\n#!/usr/bin/env sage\n#import sys\n#sys.path.insert(0,\"/home/ondra/ext/sympy-sage/\")\nfrom sympy import __version__\nprint __version__\n\nprint \"SAGE:\"\n\ne = 1/cos(x)**3\nprint e\nf = e.taylor(x, 0, 8)\nprint f\n\nprint \"SymPy:\"\nfrom sympy import Symbol, cos, sympify, pprint\nfrom sympy.abc import x\n\ne = sympify(1)/cos(x)**3\nprint e\nf = e.series(x, 10)\nprint f\nprint \"\\nSymPy pretty printer:\"\npprint(e)\npprint(f)\n\nprint \"\\nSymPy -> SAGE:\"\nprint e._sage_()\nprint f._sage_()\n\n-------------------------------------------\n\nit will produce the following output (I put the code above into example.sage):\n\nondra@fuji:~/ext/sage-2.8.7-debian32-i686-Linux$ ./sage example.sage\n0.5.5-svn\nSAGE:\n                                      1\n                                   -------\n                                      3\n                                   cos (x)\n                           8        6       4      2\n                     8651 x    241 x    11 x    3 x\n                     ------- + ------ + ----- + ---- + 1\n                      13440     240       8      2\nSymPy:\ncos(x)**(-3)\n1 + (3/2)*x**2 + (11/8)*x**4 + (241/240)*x**6 + (8651/13440)*x**8 + O(x**10)\n\nSymPy pretty printer:\n  -3\ncos  (x)\n      2       4        6         8\n   3*x    11*x    241*x    8651*x\n1 + ---- + ----- + ------ + ------- + O(x**10)\n    2       8      240      13440\n\nSymPy -> SAGE:\n                                      1\n                                   -------\n                                      3\n                                   cos (x)\n                           8        6       4      2\n                     8651 x    241 x    11 x    3 x\n                     ------- + ------ + ----- + ---- + 1\n                      13440     240       8      2\n\n\n\nCurrently only the Add, Mul, Pow, Rational, Integer, sin, cos classes\nhave the _sage_ method, but that is enough for some basic playing.\nLet's now implement the corresponding _sympy_ method in SAGE and maybe\na few more iterations to see if we like it. And if so, I'll implement\nthe _sage_() for more SymPy classes.\n\nI'd like to achieve a state, where the same code in SAGE could be run\non both backends (Maxima and SymPy). That way we could easily see\nwhere Maxima is better than SymPy and vice versa.\n\nCould you William please create a trac login for me? I'd like to open\nand discuss a new ticket for it. Also so that I can attach any bundles\nin there.\n\nAre you planning to make another SAGE release before SD 6? If so, it\nwould be good if we could make it before it, then we'll release SymPy,\ncreate spkg, you'll release SAGE, include the spkg, so that it's\nworking out of the box for everyone at SD6 and we can discuss some new\nmore exciting things to do in Bristol.\n\nI am sorry it has taken me so long, I was really busy.\n\nOndrej\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/971\n\n",
    "closed_at": "2007-11-01T09:37:20Z",
    "created_at": "2007-10-23T01:36:18Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "[with spkg, patch] update the sympy package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/971",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
Hi,

I finally found time to write those _sage_ methods in SymPy we
discussed earlier.
The code is here:

http://dakol.hopto.org/sympy-sage/

(we are in the state of moving from Subversion to Mercurial in SymPy).
I created a new sympy spkg, by updating it's hg repository:

http://dakol.hopto.org/sympy-spkg/

(the change is trivial, because the src is not included). The spkg can
be downloaded from:

http://dakol.fsik.cvut.cz/~ondra/sympy-0.5.5.spkg

Install with:

./sage -i sympy-0.5.5.spkg

Now test it. Run this in sage:

---------------------------------------------

#!/usr/bin/env sage
#import sys
#sys.path.insert(0,"/home/ondra/ext/sympy-sage/")
from sympy import __version__
print __version__

print "SAGE:"

e = 1/cos(x)**3
print e
f = e.taylor(x, 0, 8)
print f

print "SymPy:"
from sympy import Symbol, cos, sympify, pprint
from sympy.abc import x

e = sympify(1)/cos(x)**3
print e
f = e.series(x, 10)
print f
print "\nSymPy pretty printer:"
pprint(e)
pprint(f)

print "\nSymPy -> SAGE:"
print e._sage_()
print f._sage_()

-------------------------------------------

it will produce the following output (I put the code above into example.sage):

ondra@fuji:~/ext/sage-2.8.7-debian32-i686-Linux$ ./sage example.sage
0.5.5-svn
SAGE:
                                      1
                                   -------
                                      3
                                   cos (x)
                           8        6       4      2
                     8651 x    241 x    11 x    3 x
                     ------- + ------ + ----- + ---- + 1
                      13440     240       8      2
SymPy:
cos(x)**(-3)
1 + (3/2)*x**2 + (11/8)*x**4 + (241/240)*x**6 + (8651/13440)*x**8 + O(x**10)

SymPy pretty printer:
  -3
cos  (x)
      2       4        6         8
   3*x    11*x    241*x    8651*x
1 + ---- + ----- + ------ + ------- + O(x**10)
    2       8      240      13440

SymPy -> SAGE:
                                      1
                                   -------
                                      3
                                   cos (x)
                           8        6       4      2
                     8651 x    241 x    11 x    3 x
                     ------- + ------ + ----- + ---- + 1
                      13440     240       8      2



Currently only the Add, Mul, Pow, Rational, Integer, sin, cos classes
have the _sage_ method, but that is enough for some basic playing.
Let's now implement the corresponding _sympy_ method in SAGE and maybe
a few more iterations to see if we like it. And if so, I'll implement
the _sage_() for more SymPy classes.

I'd like to achieve a state, where the same code in SAGE could be run
on both backends (Maxima and SymPy). That way we could easily see
where Maxima is better than SymPy and vice versa.

Could you William please create a trac login for me? I'd like to open
and discuss a new ticket for it. Also so that I can attach any bundles
in there.

Are you planning to make another SAGE release before SD 6? If so, it
would be good if we could make it before it, then we'll release SymPy,
create spkg, you'll release SAGE, include the spkg, so that it's
working out of the box for everyone at SD6 and we can discuss some new
more exciting things to do in Bristol.

I am sorry it has taken me so long, I was really busy.

Ondrej
```

Issue created by migration from https://trac.sagemath.org/ticket/971





---

archive/issue_comments_005906.json:
```json
{
    "body": "```\nJust a note that the spkg above is just a preliminary unreleased\nversion and contains some other minor bugs. But I want to settle on\nsome interface to SAGE now. And then we'll fix the bugs and make a\nrelease and then you can include it in SAGE officially.\n```\nso I push it back to 2.9.",
    "created_at": "2007-10-23T21:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/971#issuecomment-5906",
    "user": "https://github.com/malb"
}
```

```
Just a note that the spkg above is just a preliminary unreleased
version and contains some other minor bugs. But I want to settle on
some interface to SAGE now. And then we'll fix the bugs and make a
release and then you can include it in SAGE officially.
```
so I push it back to 2.9.



---

archive/issue_events_002684.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-23T21:17:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/971",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/971#event-2684"
}
```



---

archive/issue_comments_005907.json:
```json
{
    "body": "From Ondrej, via sage-devel:\n\n```\nWe made a new  release of SymPy with those _sage_() methods so that it\ncan be integrated in SAGE more systematically. If some suggestions\narise now, we'll simply change it and release again. \n```\nand\n\n```\nI don't have access to the tracker, but here is how you can generate\nthe sympy spkg:\n\nhg clone http://hgsympy.hopto.org/sympy-spkg/\ncd sympy-spkg\n./get-orig-sources\ncd ..\n/path/to/sage -pkg sympy-spkg\n\nThis will generate sympy-spkg.spkg. So you may want to rename the\nsympy-spkg dir to the version of sympy. Generally I think the name of\nthe package shouldn't be inferred from the name of the directory,\nsince the directory doesn't change, but the version of the package\ndoes.\n```",
    "created_at": "2007-10-30T16:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/971#issuecomment-5907",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

From Ondrej, via sage-devel:

```
We made a new  release of SymPy with those _sage_() methods so that it
can be integrated in SAGE more systematically. If some suggestions
arise now, we'll simply change it and release again. 
```
and

```
I don't have access to the tracker, but here is how you can generate
the sympy spkg:

hg clone http://hgsympy.hopto.org/sympy-spkg/
cd sympy-spkg
./get-orig-sources
cd ..
/path/to/sage -pkg sympy-spkg

This will generate sympy-spkg.spkg. So you may want to rename the
sympy-spkg dir to the version of sympy. Generally I think the name of
the package shouldn't be inferred from the name of the directory,
since the directory doesn't change, but the version of the package
does.
```



---

archive/issue_events_002685.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-11-01T01:23:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/971",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/971#event-2685"
}
```



---

archive/issue_events_002686.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-11-01T01:23:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/971",
    "milestone": "sage-2.8.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/971#event-2686"
}
```



---

archive/issue_comments_005908.json:
```json
{
    "body": "Attachment [971.patch](tarball://root/attachments/some-uuid/ticket971/971.patch) by cwitty created at 2007-11-01 01:23:17\n\nThere's a new sympy spkg, generated according to the above instructions, at http://sage.math.washington.edu/home/cwitty/sympy-0.5.6.hg\n\nAlso, I've added a patch that does some minor doctesting of the new sympy.",
    "created_at": "2007-11-01T01:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/971#issuecomment-5908",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [971.patch](tarball://root/attachments/some-uuid/ticket971/971.patch) by cwitty created at 2007-11-01 01:23:17

There's a new sympy spkg, generated according to the above instructions, at http://sage.math.washington.edu/home/cwitty/sympy-0.5.6.hg

Also, I've added a patch that does some minor doctesting of the new sympy.



---

archive/issue_comments_005909.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T09:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/971#issuecomment-5909",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002687.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-01T09:37:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/971",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/971#event-2687"
}
```



---

archive/issue_comments_005910.json:
```json
{
    "body": "spkg updated, patch applied to 2.8.11.alpha0",
    "created_at": "2007-11-01T09:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/971#issuecomment-5910",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

spkg updated, patch applied to 2.8.11.alpha0
