# Issue 9505: coeff(f,x*y) does not work

archive/issues_009505.json:
```json
{
    "body": "Assignee: malb\n\nThe following is ok:\n\n```\nsage: var('x,y,z')\nsage: f=x*y*z^2\nsage: f.coeff(z^2)\nx*y\n```\n\nHowever the following is not:\n\n```\nsage: f.coeff(x*y)\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9505\n\n",
    "created_at": "2010-07-15T09:12:14Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "title": "coeff(f,x*y) does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9505",
    "user": "zimmerma"
}
```
Assignee: malb

The following is ok:

```
sage: var('x,y,z')
sage: f=x*y*z^2
sage: f.coeff(z^2)
x*y
```

However the following is not:

```
sage: f.coeff(x*y)
0
```


Issue created by migration from https://trac.sagemath.org/ticket/9505





---

archive/issue_comments_091309.json:
```json
{
    "body": "PS: I'm sorry if this is a duplicate. The trac search for \"coeff\" gives 295 entries!",
    "created_at": "2010-07-15T09:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91309",
    "user": "zimmerma"
}
```

PS: I'm sorry if this is a duplicate. The trac search for "coeff" gives 295 entries!



---

archive/issue_comments_091310.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-09-19T15:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91310",
    "user": "burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_091311.json:
```json
{
    "body": "Changing component from commutative algebra to symbolics.",
    "created_at": "2010-09-19T15:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91311",
    "user": "burcin"
}
```

Changing component from commutative algebra to symbolics.



---

archive/issue_comments_091312.json:
```json
{
    "body": "Changing assignee from malb to burcin.",
    "created_at": "2010-09-19T15:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91312",
    "user": "burcin"
}
```

Changing assignee from malb to burcin.



---

archive/issue_comments_091313.json:
```json
{
    "body": "I'm switching the component to `symbolics` since the problem involves symbolic expressions.\n\nIt seems that we inherited this behavior from GiNaC:\n\n\n```\nginsh - GiNaC Interactive Shell (ginac V1.5.7)\n  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz,\n (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.\n  ._) i N a C | You are welcome to redistribute it under certain conditions.\n<-------------' For details type `warranty;'.\n\nType ?? for a list of help topics.\n> f = x*y*z^2;\ny*z^2*x\n> coeff(f, z^2,1);\ny*x\n> coeff(f, x*y,1);\n0\n```\n\n\nI will report this to the ginac-list.",
    "created_at": "2010-09-19T15:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91313",
    "user": "burcin"
}
```

I'm switching the component to `symbolics` since the problem involves symbolic expressions.

It seems that we inherited this behavior from GiNaC:


```
ginsh - GiNaC Interactive Shell (ginac V1.5.7)
  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz,
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.
  ._) i N a C | You are welcome to redistribute it under certain conditions.
<-------------' For details type `warranty;'.

Type ?? for a list of help topics.
> f = x*y*z^2;
y*z^2*x
> coeff(f, z^2,1);
y*x
> coeff(f, x*y,1);
0
```


I will report this to the ginac-list.



---

archive/issue_comments_091314.json:
```json
{
    "body": "Since I don't know how to fix this, at least I can point out some related facts.\n\nMaxima does exactly the same thing as GINAC (and Sage):\n\n```\nsage: !maxima\n;;; Loading #P\"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/sb-bsd-sockets.fas\"\n;;; Loading #P\"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/sockets.fas\"\n;;; Loading #P\"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/defsystem.fas\"\n;;; Loading #P\"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/cmp.fas\"\nMaxima 5.24.0 http://maxima.sourceforge.net\nusing Lisp ECL 11.1.1\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) f : x*y*z;\n(%o1)                                x y z\n(%i2) coeff(f, x);\n(%o2)                                 y z\n(%i3) coeff(f, x*y);\n(%o3)                                  0\n```\n\n\nMaple raises an error in this case:\n\n```\n> f := x*y*z \n> ;\n                                                                     f := x y z\n\n> coeff(f, x);\n                                                                         y z\n\n> coeff(f, x*y);\nError, invalid input: coeff received x*y, which is not valid for its 2nd argument, x\n```\n\n\nMathematica does what you expect:\n\n```\nIn[1]:= f := x*y*z;\n\nIn[2]:= Coefficient[f,x] \n\nOut[2]= y z\n\nIn[3]:= Coefficient[f,x*y]\n\nOut[3]= z\n```\n\n\nSage multivariate polynomials (hence Singular) do what you expect:\n\n\n```\nsage: R.<x,y,z>=QQ[]\nsage: f = x*y*z^2\nsage: f.coefficient(x)\ny*z^2\nsage: f.coefficient(x*y)\nz^2\n```\n",
    "created_at": "2012-03-21T18:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91314",
    "user": "was"
}
```

Since I don't know how to fix this, at least I can point out some related facts.

Maxima does exactly the same thing as GINAC (and Sage):

```
sage: !maxima
;;; Loading #P"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/sb-bsd-sockets.fas"
;;; Loading #P"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/sockets.fas"
;;; Loading #P"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/defsystem.fas"
;;; Loading #P"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/cmp.fas"
Maxima 5.24.0 http://maxima.sourceforge.net
using Lisp ECL 11.1.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) f : x*y*z;
(%o1)                                x y z
(%i2) coeff(f, x);
(%o2)                                 y z
(%i3) coeff(f, x*y);
(%o3)                                  0
```


Maple raises an error in this case:

```
> f := x*y*z 
> ;
                                                                     f := x y z

> coeff(f, x);
                                                                         y z

> coeff(f, x*y);
Error, invalid input: coeff received x*y, which is not valid for its 2nd argument, x
```


Mathematica does what you expect:

```
In[1]:= f := x*y*z;

In[2]:= Coefficient[f,x] 

Out[2]= y z

In[3]:= Coefficient[f,x*y]

Out[3]= z
```


Sage multivariate polynomials (hence Singular) do what you expect:


```
sage: R.<x,y,z>=QQ[]
sage: f = x*y*z^2
sage: f.coefficient(x)
y*z^2
sage: f.coefficient(x*y)
z^2
```




---

archive/issue_comments_091315.json:
```json
{
    "body": "a possible fix would be that `f.coeff(x<sup>n*y</sup>m)` automatically calls\n`f.coeff(x,n).coeff(y,m)` which gives the expected answer:\n\n```\nsage: var('x,y,z')\n(x, y, z)\nsage: f=x*y*z^2\nsage: f.coeff(x,1).coeff(y,1)\nz^2\n```\n\nPaul",
    "created_at": "2012-03-26T15:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91315",
    "user": "zimmerma"
}
```

a possible fix would be that `f.coeff(x<sup>n*y</sup>m)` automatically calls
`f.coeff(x,n).coeff(y,m)` which gives the expected answer:

```
sage: var('x,y,z')
(x, y, z)
sage: f=x*y*z^2
sage: f.coeff(x,1).coeff(y,1)
z^2
```

Paul



---

archive/issue_comments_091316.json:
```json
{
    "body": "We might need to expand the expression before doing recursive calls to `coefficient()`:\n\n\n```\nsage: var('x,y,z')\n(x, y, z)\nsage: g = x*y*(z^2 + y*z)\nsage: g.coeff(x,1).coeff(y,1)\nz\n```\n\n\nCompare to MMA:\n\n\n```\nIn[12]:= Coefficient[x*y*(z^2 + y*z), x*y]\n\n          2\nOut[12]= z\n\n```\n",
    "created_at": "2012-03-26T16:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91316",
    "user": "burcin"
}
```

We might need to expand the expression before doing recursive calls to `coefficient()`:


```
sage: var('x,y,z')
(x, y, z)
sage: g = x*y*(z^2 + y*z)
sage: g.coeff(x,1).coeff(y,1)
z
```


Compare to MMA:


```
In[12]:= Coefficient[x*y*(z^2 + y*z), x*y]

          2
Out[12]= z

```




---

archive/issue_comments_091317.json:
```json
{
    "body": "Attachment [trac_9505.patch](tarball://root/attachments/some-uuid/ticket9505/trac_9505.patch) by zimmerma created at 2013-08-23 13:00:11\n\nattached is a temporary fix that calls coeff in turn for each term `x^n` in `s`.\nIn addition it checks the extra argument `n` is only used for a single symbol.\n\nPaul",
    "created_at": "2013-08-23T13:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91317",
    "user": "zimmerma"
}
```

Attachment [trac_9505.patch](tarball://root/attachments/some-uuid/ticket9505/trac_9505.patch) by zimmerma created at 2013-08-23 13:00:11

attached is a temporary fix that calls coeff in turn for each term `x^n` in `s`.
In addition it checks the extra argument `n` is only used for a single symbol.

Paul



---

archive/issue_comments_091318.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-23T13:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91318",
    "user": "zimmerma"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091319.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-17T15:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91319",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091320.json:
```json
{
    "body": "Patch applies cleanly, looks good, tests OK in symbolics/\n\nNot sure if the stopgap is still necessary. My tests were satisfying but hey.\n----\nNew commits:",
    "created_at": "2014-02-17T15:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91320",
    "user": "rws"
}
```

Patch applies cleanly, looks good, tests OK in symbolics/

Not sure if the stopgap is still necessary. My tests were satisfying but hey.
----
New commits:



---

archive/issue_comments_091321.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2014-02-20T17:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91321",
    "user": "git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_091322.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2014-02-20T17:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91322",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_091323.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-20T17:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91323",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091324.json:
```json
{
    "body": "Documentation does not build\n\n```\n[calculus ] docstring of sage.symbolic.expression.Expression.coeff:57: WARNING: Literal block expected; none found.\n[calculus ] docstring of sage.symbolic.expression.Expression.coeff:57: WARNING: Literal block expected; none found.\nTraceback (most recent call last):\n  File \"/home/buildslave-sage/slave/sage_git/build/src/doc/common/builder.py\", line 83, in f\n    execfile(sys.argv[0])\n  File \"/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py\", line 185, in <module>\n    sphinx.cmdline.main(sys.argv)\n  File \"/home/buildslave-sage/slave/sage_git/build/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/cmdline.py\", line 206, in main\n    print >>error\n  File \"/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py\", line 165, in write\n    self._write(str)\n  File \"/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py\", line 139, in _write\n    self._log_line(line)\n  File \"/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py\", line 108, in _log_line\n    raise OSError(line)\nOSError: [calculus ] docstring of sage.symbolic.expression.Expression.coeff:57: WARNING: Literal block expected; none found.\n```\n",
    "created_at": "2014-02-21T11:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91324",
    "user": "vbraun"
}
```

Documentation does not build

```
[calculus ] docstring of sage.symbolic.expression.Expression.coeff:57: WARNING: Literal block expected; none found.
[calculus ] docstring of sage.symbolic.expression.Expression.coeff:57: WARNING: Literal block expected; none found.
Traceback (most recent call last):
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/builder.py", line 83, in f
    execfile(sys.argv[0])
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py", line 185, in <module>
    sphinx.cmdline.main(sys.argv)
  File "/home/buildslave-sage/slave/sage_git/build/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/cmdline.py", line 206, in main
    print >>error
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py", line 165, in write
    self._write(str)
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py", line 139, in _write
    self._log_line(line)
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py", line 108, in _log_line
    raise OSError(line)
OSError: [calculus ] docstring of sage.symbolic.expression.Expression.coeff:57: WARNING: Literal block expected; none found.
```




---

archive/issue_comments_091325.json:
```json
{
    "body": "sorry with the change to git I don't know how yet how to submit a patch, thus I won't be able to work on this in the near future.\n\nPaul",
    "created_at": "2014-02-21T13:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91325",
    "user": "zimmerma"
}
```

sorry with the change to git I don't know how yet how to submit a patch, thus I won't be able to work on this in the near future.

Paul



---

archive/issue_comments_091326.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2014-02-21T15:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91326",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_091327.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2014-02-21T15:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91327",
    "user": "git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_091328.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-21T15:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91328",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091329.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-22T06:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9505#issuecomment-91329",
    "user": "vbraun"
}
```

Resolution: fixed
