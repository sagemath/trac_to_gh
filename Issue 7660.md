# Issue 7660: arithmetic with inequalities confusing

archive/issues_007660.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  kcrisman\n\nFrom the following sage-devel thread:\n\nhttp://groups.google.com/group/sage-devel/t/951d510c814f894f\n\n\nArithmetic with inequalities can be confusing, since Sage does nothing to keep the inequality ``correct``. For example:\n\n\n```\nOn Thu, 10 Dec 2009 00:37:10 -0800 (PST)\n\"marik@mendelu.cz\" <marik@mendelu.cz> wrote:\n\n> sage: f = x + 3 < y - 2\n> sage: f*(-1)\n> -x - 3 < -y + 2\n```\n\n\nIt seems MMA doesn't apply any automatic simplification in this case:\n\n\n```\nOn Thu, 10 Dec 2009 09:54:36 -0800\nWilliam Stein <wstein@gmail.com> wrote:\n\n> Mathematica does something weird and formal:\n> \n> In[1]:= f := x+3 < y-2;\n> In[3]:= f*(-1)\n> Out[3]= -(3 + x < -2 + y)\n```\n\n\nMaple acts more intuitively, though the way ``formal products`` are printed leaves something to be desired, IMHO:\n\n\n```\nOn Thu, 10 Dec 2009 14:15:53 -0800\nWilliam Stein <wstein@gmail.com> wrote:\n\n> Here is what Maple does:\n> \n> flat:release_notes wstein$ maple\n>     |\\^/|     Maple 13 (APPLE UNIVERSAL OSX)\n> ._|\\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple\n> Inc. 2009 \\  MAPLE  /  All rights reserved. Maple is a trademark of\n>  <____ ____>  Waterloo Maple Inc.\n>       |       Type ? for help.\n> > f := x < y;  \n>                                   f := x < y\n> \n> > f*(-3);  \n>                                   -3 y < -3 x\n> \n> > f*z;  \n>                                   *(x < y, z)\n> \n> > f*a;  \n>                                   *(x < y, a)\n```\n\n\n\nWe should multiply both sides of the inequality only if the argument is a real number (as opposed to a symbol with real domain), and invert the relation when the argument is negative.\n\nNote that GiNaC leaves everything formal, like MMA, by default:\n\n\n```\nginsh - GiNaC Interactive Shell (ginac V1.5.3)\n  __,  _______  Copyright (C) 1999-2009 Johannes Gutenberg University Mainz,\n (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.\n  ._) i N a C | You are welcome to redistribute it under certain conditions.\n<-------------' For details type `warranty;'.\n\nType ?? for a list of help topics.\n> f= x < y;\nx<y\n> f*-1;\n-(x<y)\n> f*-5;\n-5*(x<y)\n> f*-z;\n-z*(x<y)\n> f*z;\nz*(x<y)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7660\n\n",
    "created_at": "2009-12-11T13:55:02Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "arithmetic with inequalities confusing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7660",
    "user": "burcin"
}
```
Assignee: burcin

CC:  kcrisman

From the following sage-devel thread:

http://groups.google.com/group/sage-devel/t/951d510c814f894f


Arithmetic with inequalities can be confusing, since Sage does nothing to keep the inequality ``correct``. For example:


```
On Thu, 10 Dec 2009 00:37:10 -0800 (PST)
"marik@mendelu.cz" <marik@mendelu.cz> wrote:

> sage: f = x + 3 < y - 2
> sage: f*(-1)
> -x - 3 < -y + 2
```


It seems MMA doesn't apply any automatic simplification in this case:


```
On Thu, 10 Dec 2009 09:54:36 -0800
William Stein <wstein@gmail.com> wrote:

> Mathematica does something weird and formal:
> 
> In[1]:= f := x+3 < y-2;
> In[3]:= f*(-1)
> Out[3]= -(3 + x < -2 + y)
```


Maple acts more intuitively, though the way ``formal products`` are printed leaves something to be desired, IMHO:


```
On Thu, 10 Dec 2009 14:15:53 -0800
William Stein <wstein@gmail.com> wrote:

> Here is what Maple does:
> 
> flat:release_notes wstein$ maple
>     |\^/|     Maple 13 (APPLE UNIVERSAL OSX)
> ._|\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple
> Inc. 2009 \  MAPLE  /  All rights reserved. Maple is a trademark of
>  <____ ____>  Waterloo Maple Inc.
>       |       Type ? for help.
> > f := x < y;  
>                                   f := x < y
> 
> > f*(-3);  
>                                   -3 y < -3 x
> 
> > f*z;  
>                                   *(x < y, z)
> 
> > f*a;  
>                                   *(x < y, a)
```



We should multiply both sides of the inequality only if the argument is a real number (as opposed to a symbol with real domain), and invert the relation when the argument is negative.

Note that GiNaC leaves everything formal, like MMA, by default:


```
ginsh - GiNaC Interactive Shell (ginac V1.5.3)
  __,  _______  Copyright (C) 1999-2009 Johannes Gutenberg University Mainz,
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.
  ._) i N a C | You are welcome to redistribute it under certain conditions.
<-------------' For details type `warranty;'.

Type ?? for a list of help topics.
> f= x < y;
x<y
> f*-1;
-(x<y)
> f*-5;
-5*(x<y)
> f*-z;
-z*(x<y)
> f*z;
z*(x<y)
```


Issue created by migration from https://trac.sagemath.org/ticket/7660





---

archive/issue_comments_065521.json:
```json
{
    "body": "\n```\nsage: -1*(x < y)\n-x < -y\n\n```\n\nthis is quite dangerous (I encountered it as a bug in a project).  Hopefully someone will try to fix this soon.  Could it be related to this  http://trac.sagemath.org/sage_trac/ticket/11309 ?",
    "created_at": "2011-06-16T23:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65521",
    "user": "tnv"
}
```


```
sage: -1*(x < y)
-x < -y

```

this is quite dangerous (I encountered it as a bug in a project).  Hopefully someone will try to fix this soon.  Could it be related to this  http://trac.sagemath.org/sage_trac/ticket/11309 ?



---

archive/issue_comments_065522.json:
```json
{
    "body": "I propose the following: `a*(x<y)` should not be simplified, ever, other than simplifying `a`, `x`, or `y` individually. Are there any problems with this?",
    "created_at": "2012-06-01T21:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65522",
    "user": "kini"
}
```

I propose the following: `a*(x<y)` should not be simplified, ever, other than simplifying `a`, `x`, or `y` individually. Are there any problems with this?



---

archive/issue_comments_065523.json:
```json
{
    "body": "Given the ticket description details above and the discussion at #11309 and here, I think that Burcin's original proposal of \n* keeping the same if we know `a` is positive\n* reversing if we know `a` is negative (presumably in both of these cases only if `a` is coerced to the reals successfully, as Burcin says)\n* (not in original but reasonable) return something like `False` for `<` and `=` for `<=` if `a=0`?\n* returning something formal otherwise\nseems best.  It does seem reasonable to multiply by `-1`, after all, and tnv is right that this should either reverse the inequality or remain formal.",
    "created_at": "2012-06-02T01:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65523",
    "user": "kcrisman"
}
```

Given the ticket description details above and the discussion at #11309 and here, I think that Burcin's original proposal of 
* keeping the same if we know `a` is positive
* reversing if we know `a` is negative (presumably in both of these cases only if `a` is coerced to the reals successfully, as Burcin says)
* (not in original but reasonable) return something like `False` for `<` and `=` for `<=` if `a=0`?
* returning something formal otherwise
seems best.  It does seem reasonable to multiply by `-1`, after all, and tnv is right that this should either reverse the inequality or remain formal.



---

archive/issue_comments_065524.json:
```json
{
    "body": "It doesn't seem at all reasonable to me to distribute multiplication over a relation. When you distribute multiplication over addition, the addition expression `(a+b)` lives in the same space as `a` and `b` individually. This is not the case with `(x<y)` and `x` and `y`. \n\nThere is no mathematical rationale for saying that `(-1)*(x<y)` is `-x < -y` or `-x > -y` or anything other than just `(-1)*(x<y)`. I'm sure many can recall when they first learned basic algebra that their teacher was careful to say \"we multiply *both sides of* the equation by c\", not \"we multiply the equation by c\", just as he or she was careful to say \"we multiply both the numerator and denominator of the fraction by c\", rather than the dangerous \"we multiply the fraction by c\"!\n\nIf we allow multiplication to distribute over `x<y` as if it were a two-coordinate vector, do we want other similarities with vector arithmetic to come into play? Should `(a+b)*(x<y)` be equal to `a*(x<y) + b*(x<y)`? Now we have addition and presumably subtraction of relational expressions. What is `0*(x<y)`? What is `(x<y) + (z>y)`? Should we attempt to reverse inequalities to make them match up when adding them? Do we then end up with `(x+y<y+z)`, or `(y+z>x+y)`? Or, do we conclude that `(z>y)` is equal to `(-1)*(-z<-y)`, and so `(x<y) + (z>y) == (x<y) - (-z<-y) == (x+z<2y)`? Going beyond vector-like arithmetic, what happens when you add a scalar to a relational expression? What is `(x<y) + 3`?\n\nI think the most sensible answer to all the above questions is the following: we should not perform arithmetic on relational expressions; when asked to do so, we should return a purely formal expression.\n\nIf the title of this ticket disagrees with that answer, I can make another ticket to implement it, but I'm just wondering if anyone disagrees with me strongly about this.",
    "created_at": "2012-06-02T02:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65524",
    "user": "kini"
}
```

It doesn't seem at all reasonable to me to distribute multiplication over a relation. When you distribute multiplication over addition, the addition expression `(a+b)` lives in the same space as `a` and `b` individually. This is not the case with `(x<y)` and `x` and `y`. 

There is no mathematical rationale for saying that `(-1)*(x<y)` is `-x < -y` or `-x > -y` or anything other than just `(-1)*(x<y)`. I'm sure many can recall when they first learned basic algebra that their teacher was careful to say "we multiply *both sides of* the equation by c", not "we multiply the equation by c", just as he or she was careful to say "we multiply both the numerator and denominator of the fraction by c", rather than the dangerous "we multiply the fraction by c"!

If we allow multiplication to distribute over `x<y` as if it were a two-coordinate vector, do we want other similarities with vector arithmetic to come into play? Should `(a+b)*(x<y)` be equal to `a*(x<y) + b*(x<y)`? Now we have addition and presumably subtraction of relational expressions. What is `0*(x<y)`? What is `(x<y) + (z>y)`? Should we attempt to reverse inequalities to make them match up when adding them? Do we then end up with `(x+y<y+z)`, or `(y+z>x+y)`? Or, do we conclude that `(z>y)` is equal to `(-1)*(-z<-y)`, and so `(x<y) + (z>y) == (x<y) - (-z<-y) == (x+z<2y)`? Going beyond vector-like arithmetic, what happens when you add a scalar to a relational expression? What is `(x<y) + 3`?

I think the most sensible answer to all the above questions is the following: we should not perform arithmetic on relational expressions; when asked to do so, we should return a purely formal expression.

If the title of this ticket disagrees with that answer, I can make another ticket to implement it, but I'm just wondering if anyone disagrees with me strongly about this.



---

archive/issue_comments_065525.json:
```json
{
    "body": "Well, we could go to the !Ginac/Mathematica way too, instead of the Maple way.  But now that #11309 is on the way in, probably it's time to deal with this.  FWIW, Maxima seems to go that way as well.\n\n```\n(%i1) x<y;\n(%o1)                                x < y\n(%i2) a:x<y;\n(%o2)                                x < y\n(%i3) a;\n(%o3)                                x < y\n(%i4) -1*a;\n(%o4)                              - (x < y)\n(%i5) b*a;\n(%o5)                              b (x < y)\n```\n\nMaybe Burcin has a comment; I don't have that strong of feelings, though I'm partial to \n* `(x<y)+3 == x+3<y+3`\n* `0*(x<y) is False`\nbut those may just be sentimental, as you suggest.",
    "created_at": "2012-06-02T02:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65525",
    "user": "kcrisman"
}
```

Well, we could go to the !Ginac/Mathematica way too, instead of the Maple way.  But now that #11309 is on the way in, probably it's time to deal with this.  FWIW, Maxima seems to go that way as well.

```
(%i1) x<y;
(%o1)                                x < y
(%i2) a:x<y;
(%o2)                                x < y
(%i3) a;
(%o3)                                x < y
(%i4) -1*a;
(%o4)                              - (x < y)
(%i5) b*a;
(%o5)                              b (x < y)
```

Maybe Burcin has a comment; I don't have that strong of feelings, though I'm partial to 
* `(x<y)+3 == x+3<y+3`
* `0*(x<y) is False`
but those may just be sentimental, as you suggest.



---

archive/issue_comments_065526.json:
```json
{
    "body": "Honestly I thought the most likely response would be `0*(x<y) == 0`. `False` is an even stranger result because now you have `(x<y) == (1+0)*(x<y) == (x<y) + False`, so either `False` is now another additive identity (on relations, anyway), thus breaking the universality of `? - ? = 0`, or `False == 0`, which is another can of worms...\n\nAnd if `(x<y)+3 == (x+3<y+3)`, then presumably `3 == (3<3) == False`...?\n\nNone of this makes any sense, IMHO. I think it would be best to go the Mathematica/GiNaC/Maxima way, as shown in your Maxima output, rather than the Maple way.",
    "created_at": "2012-06-02T02:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65526",
    "user": "kini"
}
```

Honestly I thought the most likely response would be `0*(x<y) == 0`. `False` is an even stranger result because now you have `(x<y) == (1+0)*(x<y) == (x<y) + False`, so either `False` is now another additive identity (on relations, anyway), thus breaking the universality of `? - ? = 0`, or `False == 0`, which is another can of worms...

And if `(x<y)+3 == (x+3<y+3)`, then presumably `3 == (3<3) == False`...?

None of this makes any sense, IMHO. I think it would be best to go the Mathematica/GiNaC/Maxima way, as shown in your Maxima output, rather than the Maple way.



---

archive/issue_comments_065527.json:
```json
{
    "body": "For the record, Maxima has a share package which implements arithmetic on inequalities.\n\n```\n(%i1) load (ineq);\n(%o1) /home/robert/maxima/maxima-git/maxima-code/share/simplification/ineq.mac\n(%i2) e:a < b;\n(%o2)                                a < b\n(%i3) x*e;\nIs  x  positive, negative, or zero?\np;\n(%o3)                              a x < b x\n(%i4) x*e;\nIs  x  positive, negative, or zero?\nn;\n(%o4)                              a x > b x\n(%i5) x*e;\nIs  x  positive, negative, or zero?\nz;\n(%o5)                              (a < b) x\n```\n\nI gather that's similar to what Maple does.",
    "created_at": "2013-01-08T02:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65527",
    "user": "robert_dodier"
}
```

For the record, Maxima has a share package which implements arithmetic on inequalities.

```
(%i1) load (ineq);
(%o1) /home/robert/maxima/maxima-git/maxima-code/share/simplification/ineq.mac
(%i2) e:a < b;
(%o2)                                a < b
(%i3) x*e;
Is  x  positive, negative, or zero?
p;
(%o3)                              a x < b x
(%i4) x*e;
Is  x  positive, negative, or zero?
n;
(%o4)                              a x > b x
(%i5) x*e;
Is  x  positive, negative, or zero?
z;
(%o5)                              (a < b) x
```

I gather that's similar to what Maple does.



---

archive/issue_comments_065528.json:
```json
{
    "body": "prototype patch",
    "created_at": "2013-01-09T11:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65528",
    "user": "burcin"
}
```

prototype patch



---

archive/issue_comments_065529.json:
```json
{
    "body": "Attachment [trac_7660-inequality_arithmetic.patch](tarball://root/attachments/some-uuid/ticket7660/trac_7660-inequality_arithmetic.patch) by burcin created at 2013-01-09 11:09:14\n\nattachment:trac_7660-inequality_arithmetic.patch comments out a few lines in `_add_`, `_mul_`, etc., methods of symbolic expressions to pass the arithmetic on to GiNaC directly. I don't have time to test this and verify that it returns sensible answers, however we decide to define \"sensible\". Please test, see what doctests fail and try to produce horrific wrong results.\n\nQuite a few doctests and some documentation will have to change to match this new design decision. I'd like to make sure we agree on the behavior before trying to produce a clean patch. Of course, I'd appreciate help with the documentation in any case.",
    "created_at": "2013-01-09T11:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65529",
    "user": "burcin"
}
```

Attachment [trac_7660-inequality_arithmetic.patch](tarball://root/attachments/some-uuid/ticket7660/trac_7660-inequality_arithmetic.patch) by burcin created at 2013-01-09 11:09:14

attachment:trac_7660-inequality_arithmetic.patch comments out a few lines in `_add_`, `_mul_`, etc., methods of symbolic expressions to pass the arithmetic on to GiNaC directly. I don't have time to test this and verify that it returns sensible answers, however we decide to define "sensible". Please test, see what doctests fail and try to produce horrific wrong results.

Quite a few doctests and some documentation will have to change to match this new design decision. I'd like to make sure we agree on the behavior before trying to produce a clean patch. Of course, I'd appreciate help with the documentation in any case.



---

archive/issue_comments_065530.json:
```json
{
    "body": "OK that patch applies cleanly with `patch -l`. It results in\n\n\n```\nsage: var('x')\nx\nsage: x>1\nx > 1\nsage: ie=_\nsage: ie*-1\n-(x > 1)\nsage: solve(_,x)\n...\nRuntimeError: ECL says: THROW: The catch MACSYMA-QUIT is undefined.\n```\n\nI refrained from starting any doctests.",
    "created_at": "2014-02-17T15:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65530",
    "user": "rws"
}
```

OK that patch applies cleanly with `patch -l`. It results in


```
sage: var('x')
x
sage: x>1
x > 1
sage: ie=_
sage: ie*-1
-(x > 1)
sage: solve(_,x)
...
RuntimeError: ECL says: THROW: The catch MACSYMA-QUIT is undefined.
```

I refrained from starting any doctests.



---

archive/issue_comments_065531.json:
```json
{
    "body": "Changing keywords from \"\" to \"inequality, solver, maxima\".",
    "created_at": "2014-02-17T15:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65531",
    "user": "rws"
}
```

Changing keywords from "" to "inequality, solver, maxima".



---

archive/issue_comments_065532.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-02-17T15:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65532",
    "user": "rws"
}
```

New commits:



---

archive/issue_comments_065533.json:
```json
{
    "body": "Here are the statements sent via `maxima_eval(\"#$%s$\"%statement)`:\n\nBefore:\n\n```\nsage: solve(-(x > 1),x)\nsage0 : (x)*(-1) > -1\nsage1 : solve_rat_ineq(sage0)\n_tmp_ : sage1\nkill(sage1)\nkill(sage0)\n[[x < 1]]\n```\n\nAfter:\n\n```\nsage: solve(-(x > 1),x)\nsage12 : (x > 1)*(-1) = 0\nsage13 : x\nsage14 : solve(sage12,sage13)\nkill(sage13)\nkill(sage14)\n_tmp_ : [x>1=0]          <---------?\nkill(sage12)\n```\n\nApparently, Sage's last statement sent is the result itself (no idea why), and maxima then barfs because it can't digest its own output. In maxima:\n\n```\n(%i11) solve((x > 1)*(-1) = 0,x);\n(%o11)                            [x > 1 = 0]\n(%i12) [x>1=0];\nincorrect syntax: Found logical expression where algebraic expression expected\n[x>1=\n   ^\n```\n\nIn summary there are three problems:\n* 46 doctests fail in symbolic alone\n* maxima can't handle the formal expressions generated via this patch, and `solve()` will fail because it uses maxima solve() and not solve_rat_ineq() (probably because the expression looks like an algebraic). However:\n\n```\nsage: solve_ineq((x>1)*(-1),[x,y])\n#0: solve_rat_ineq(ineq=-(x > 1))\n...\nTypeError: ECL says: Error executing code in Maxima: solve_rat_ineq:  -(x > 1)  is not an inequality.\n```\n\nSo maxima refuses to handle the formal expression generated by this patch, and this means they cannot be solved, regardless of method called. So, in addition, `solve()` should be changed to do simplification of these expressions before handing them on. This special simplification avoids all issues raised in comment:10. It can be implemented after this ticket (#15906).\n* `calculus.py:symbolic_expression_from_maxima_string()` should catch maxima `RuntimeError`s from `ecl.c` and rethrow them with meaningful information. (#15902)\n`",
    "created_at": "2014-03-06T16:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65533",
    "user": "rws"
}
```

Here are the statements sent via `maxima_eval("#$%s$"%statement)`:

Before:

```
sage: solve(-(x > 1),x)
sage0 : (x)*(-1) > -1
sage1 : solve_rat_ineq(sage0)
_tmp_ : sage1
kill(sage1)
kill(sage0)
[[x < 1]]
```

After:

```
sage: solve(-(x > 1),x)
sage12 : (x > 1)*(-1) = 0
sage13 : x
sage14 : solve(sage12,sage13)
kill(sage13)
kill(sage14)
_tmp_ : [x>1=0]          <---------?
kill(sage12)
```

Apparently, Sage's last statement sent is the result itself (no idea why), and maxima then barfs because it can't digest its own output. In maxima:

```
(%i11) solve((x > 1)*(-1) = 0,x);
(%o11)                            [x > 1 = 0]
(%i12) [x>1=0];
incorrect syntax: Found logical expression where algebraic expression expected
[x>1=
   ^
```

In summary there are three problems:
* 46 doctests fail in symbolic alone
* maxima can't handle the formal expressions generated via this patch, and `solve()` will fail because it uses maxima solve() and not solve_rat_ineq() (probably because the expression looks like an algebraic). However:

```
sage: solve_ineq((x>1)*(-1),[x,y])
#0: solve_rat_ineq(ineq=-(x > 1))
...
TypeError: ECL says: Error executing code in Maxima: solve_rat_ineq:  -(x > 1)  is not an inequality.
```

So maxima refuses to handle the formal expression generated by this patch, and this means they cannot be solved, regardless of method called. So, in addition, `solve()` should be changed to do simplification of these expressions before handing them on. This special simplification avoids all issues raised in comment:10. It can be implemented after this ticket (#15906).
* `calculus.py:symbolic_expression_from_maxima_string()` should catch maxima `RuntimeError`s from `ecl.c` and rethrow them with meaningful information. (#15902)
`



---

archive/issue_comments_065534.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-06T16:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65534",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065535.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-07T16:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65535",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065536.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-07T16:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65536",
    "user": "rws"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065537.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-12T08:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65537",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065538.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-02T13:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65538",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065539.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-11-02T22:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65539",
    "user": "aapitzsch"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065540.json:
```json
{
    "body": "Please use python3 compatible `raise TypeError` syntax.",
    "created_at": "2014-11-02T22:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65540",
    "user": "aapitzsch"
}
```

Please use python3 compatible `raise TypeError` syntax.



---

archive/issue_comments_065541.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-03T08:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65541",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065542.json:
```json
{
    "body": "Replying to [comment:26 aapitzsch]:\n> Please use python3 compatible `raise TypeError` syntax.\nDone. Still, doctests fail in `expression.pyx`.",
    "created_at": "2014-11-03T08:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65542",
    "user": "rws"
}
```

Replying to [comment:26 aapitzsch]:
> Please use python3 compatible `raise TypeError` syntax.
Done. Still, doctests fail in `expression.pyx`.



---

archive/issue_comments_065543.json:
```json
{
    "body": "This came up again in http://ask.sagemath.org/question/25217/how-to-do-operations-that-change-a-relation/",
    "created_at": "2014-12-11T14:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65543",
    "user": "rws"
}
```

This came up again in http://ask.sagemath.org/question/25217/how-to-do-operations-that-change-a-relation/



---

archive/issue_comments_065544.json:
```json
{
    "body": "I'm just now looking at this ticket and personally I don't like to lose the ability to compute with relations. I think that the fact that `(a == b)^2` returns `a^2 == b^2` is a feature, not a bug. I'd say it's up to the user to ensure that the operation makes sense.\n\nWould it be possible to keep the old behaviour for equalities `==` at least?",
    "created_at": "2014-12-11T16:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65544",
    "user": "jdemeyer"
}
```

I'm just now looking at this ticket and personally I don't like to lose the ability to compute with relations. I think that the fact that `(a == b)^2` returns `a^2 == b^2` is a feature, not a bug. I'd say it's up to the user to ensure that the operation makes sense.

Would it be possible to keep the old behaviour for equalities `==` at least?



---

archive/issue_comments_065545.json:
```json
{
    "body": "Let's start this fresh. To summarize, what's wanted is the following:\n\nequations:\n* `(a==b) +-*/ c` same as:\n  - `(a==b).add_to_both_sides(c)`\n  - `(a==b).subtract_from_both_sides(c)`\n  - `(a==b).multiply_both_sides(c)`\n  - `(a==b).divide_both_sides(c)`\n  - `False` if `*/0`\n* `(a==b)^c` --> `a^c == b^c`\n* `f(a==b)` --> `f(a==b)`\nrelations:\n* `(a<b) +- c` same as:\n  - `(a<b).add_to_both_sides(c)`\n  - `(a<b).subtract_from_both_sides(c)`\n* `(a<b) */ c` same as:\n  - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative\n  - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive\n  - `False` if `c=0`\n* `(a<b)^c` --> `(a<b)^c`\n* `f(a<b)`  --> `f(a<b)`\n\nQuestion: Real or: if coerced to the reals successfully?\nA followup extension would be like Maxima's ineq package, i.e., ask before doing a sign switch.",
    "created_at": "2015-02-12T08:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65545",
    "user": "rws"
}
```

Let's start this fresh. To summarize, what's wanted is the following:

equations:
* `(a==b) +-*/ c` same as:
  - `(a==b).add_to_both_sides(c)`
  - `(a==b).subtract_from_both_sides(c)`
  - `(a==b).multiply_both_sides(c)`
  - `(a==b).divide_both_sides(c)`
  - `False` if `*/0`
* `(a==b)^c` --> `a^c == b^c`
* `f(a==b)` --> `f(a==b)`
relations:
* `(a<b) +- c` same as:
  - `(a<b).add_to_both_sides(c)`
  - `(a<b).subtract_from_both_sides(c)`
* `(a<b) */ c` same as:
  - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative
  - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive
  - `False` if `c=0`
* `(a<b)^c` --> `(a<b)^c`
* `f(a<b)`  --> `f(a<b)`

Question: Real or: if coerced to the reals successfully?
A followup extension would be like Maxima's ineq package, i.e., ask before doing a sign switch.



---

archive/issue_comments_065546.json:
```json
{
    "body": "Replying to [comment:31 rws]:\n>  * `f(a==b)` --> `f(a==b)`\nWhat does `f(a==b)` even mean? I would go for `f(a) == f(b)`.\n\n> relations:\n>  * `(a<b) */ c` same as:\n>    - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative\n>    - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive\n>    - `False` if `c=0`\n\nWhat if neither of the above conditions is true? `raise ArithmeticError` in that case?",
    "created_at": "2015-02-12T09:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65546",
    "user": "jdemeyer"
}
```

Replying to [comment:31 rws]:
>  * `f(a==b)` --> `f(a==b)`
What does `f(a==b)` even mean? I would go for `f(a) == f(b)`.

> relations:
>  * `(a<b) */ c` same as:
>    - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative
>    - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive
>    - `False` if `c=0`

What if neither of the above conditions is true? `raise ArithmeticError` in that case?



---

archive/issue_comments_065547.json:
```json
{
    "body": "Replying to [comment:32 jdemeyer]:\n> >  * `(a<b) */ c`\n> What if neither of the above conditions is true? `raise ArithmeticError` in that case?\nNot if `c` contains variables. Is there even a way of determining this?",
    "created_at": "2015-02-12T09:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65547",
    "user": "rws"
}
```

Replying to [comment:32 jdemeyer]:
> >  * `(a<b) */ c`
> What if neither of the above conditions is true? `raise ArithmeticError` in that case?
Not if `c` contains variables. Is there even a way of determining this?



---

archive/issue_comments_065548.json:
```json
{
    "body": "Replying to [comment:33 rws]:\n> Not if `c` contains variables.\n\nWhat would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?",
    "created_at": "2015-02-12T09:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65548",
    "user": "jdemeyer"
}
```

Replying to [comment:33 rws]:
> Not if `c` contains variables.

What would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?



---

archive/issue_comments_065549.json:
```json
{
    "body": "Replying to [comment:34 jdemeyer]:\n> What would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?\nSince this ticket will check for assumptions, if there is none we should raise an `ArithmeticError` demanding one.",
    "created_at": "2015-02-12T09:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65549",
    "user": "rws"
}
```

Replying to [comment:34 jdemeyer]:
> What would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?
Since this ticket will check for assumptions, if there is none we should raise an `ArithmeticError` demanding one.



---

archive/issue_comments_065550.json:
```json
{
    "body": "So my statement to `raise ArithmeticError` if neither condition is true still remains.",
    "created_at": "2015-02-12T09:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65550",
    "user": "jdemeyer"
}
```

So my statement to `raise ArithmeticError` if neither condition is true still remains.



---

archive/issue_comments_065551.json:
```json
{
    "body": "Replying to [ticket:7660 burcin]:\n>    - if `c` contains variables (and no assumptions exist about it) raise `ArithmeticError: missing assumption: is ...>0?`\n>    - if `c` contains no variables `ArithmeticError: multiplication of inequality with irreal`\n\nI think it will be easier if these are just one case.",
    "created_at": "2015-02-12T09:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65551",
    "user": "jdemeyer"
}
```

Replying to [ticket:7660 burcin]:
>    - if `c` contains variables (and no assumptions exist about it) raise `ArithmeticError: missing assumption: is ...>0?`
>    - if `c` contains no variables `ArithmeticError: multiplication of inequality with irreal`

I think it will be easier if these are just one case.



---

archive/issue_comments_065552.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-02-12T16:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65552",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065553.json:
```json
{
    "body": "Since the `f()` stuff requires changes in function base classes, and assumptions are also an involvement, I'll leave both to followup tickets. Please review.\n----\nNew commits:",
    "created_at": "2015-02-12T16:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65553",
    "user": "rws"
}
```

Since the `f()` stuff requires changes in function base classes, and assumptions are also an involvement, I'll leave both to followup tickets. Please review.
----
New commits:



---

archive/issue_comments_065554.json:
```json
{
    "body": "Why convert to `RR`? I would simply use\n\n```\nif right == 0:\n    ...\nelif right >= 0:\n    ...\nelif right <= 0:\n    ...\nelse:\n    raise ArithmeticError(...)\n```\n\nThis handles non-constant symbolic expressions also.",
    "created_at": "2015-02-12T16:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65554",
    "user": "jdemeyer"
}
```

Why convert to `RR`? I would simply use

```
if right == 0:
    ...
elif right >= 0:
    ...
elif right <= 0:
    ...
else:
    raise ArithmeticError(...)
```

This handles non-constant symbolic expressions also.



---

archive/issue_comments_065555.json:
```json
{
    "body": "Replying to [comment:42 jdemeyer]:\n> Why convert to `RR`? I would simply use\n> {{{\n> if right == 0:\n>     ...\n> elif right >= 0:\n>     ...\n> elif right <= 0:\n>     ...\n> else:\n>     raise ArithmeticError(...)\n> }}}\n> This handles non-constant symbolic expressions also.\nSeems we have to open a ticket?\n\n```\nsage: def f(ex):\n    if ex==0:\n        print 'zero'\n    elif ex<0:\n        print 'minus'\n    else:\n        print 'else'\n....:         \nsage: ex=-I\nsage: f(ex)\nminus\nsage: bool(-I<0)\nTrue\nsage: bool(I>0)\nTrue\n```\n",
    "created_at": "2015-02-13T14:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65555",
    "user": "rws"
}
```

Replying to [comment:42 jdemeyer]:
> Why convert to `RR`? I would simply use
> {{{
> if right == 0:
>     ...
> elif right >= 0:
>     ...
> elif right <= 0:
>     ...
> else:
>     raise ArithmeticError(...)
> }}}
> This handles non-constant symbolic expressions also.
Seems we have to open a ticket?

```
sage: def f(ex):
    if ex==0:
        print 'zero'
    elif ex<0:
        print 'minus'
    else:
        print 'else'
....:         
sage: ex=-I
sage: f(ex)
minus
sage: bool(-I<0)
True
sage: bool(I>0)
True
```




---

archive/issue_comments_065556.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-13T14:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65556",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065557.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-05T14:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65557",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065558.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-19T05:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65558",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065559.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-03T06:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65559",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065560.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-20T13:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65560",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065561.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-01-10T21:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65561",
    "user": "aapitzsch"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065562.json:
```json
{
    "body": "`@`aapitzsch Are you willing to review this issue?",
    "created_at": "2016-01-11T07:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65562",
    "user": "rws"
}
```

`@`aapitzsch Are you willing to review this issue?



---

archive/issue_comments_065563.json:
```json
{
    "body": "Replying to [comment:53 rws]:\n> `@`aapitzsch Are you willing to review this issue?\nNo. Sorry for the noise.",
    "created_at": "2016-01-11T18:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65563",
    "user": "aapitzsch"
}
```

Replying to [comment:53 rws]:
> `@`aapitzsch Are you willing to review this issue?
No. Sorry for the noise.



---

archive/issue_comments_065564.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-10-06T13:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65564",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065565.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-10-06T13:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65565",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065566.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-10-06T14:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65566",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065567.json:
```json
{
    "body": "Relevant doctest fail in `src/sage/misc/sageinspect.py`",
    "created_at": "2017-01-14T08:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65567",
    "user": "rws"
}
```

Relevant doctest fail in `src/sage/misc/sageinspect.py`



---

archive/issue_comments_065568.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-01-14T08:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65568",
    "user": "rws"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065569.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-01-15T07:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65569",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065570.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-01-15T07:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65570",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065571.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-02-27T18:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65571",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065572.json:
```json
{
    "body": "does not apply",
    "created_at": "2017-02-27T18:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65572",
    "user": "chapoton"
}
```

does not apply



---

archive/issue_comments_065573.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-02-28T07:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65573",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065574.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-02-28T07:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65574",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065575.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-06-16T07:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65575",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065576.json:
```json
{
    "body": "does not apply",
    "created_at": "2017-06-16T07:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65576",
    "user": "chapoton"
}
```

does not apply



---

archive/issue_comments_065577.json:
```json
{
    "body": "In the course of this ticket already 12 merge commits were added. The branch has 8 so I'm doing a squash.",
    "created_at": "2017-06-16T07:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65577",
    "user": "rws"
}
```

In the course of this ticket already 12 merge commits were added. The branch has 8 so I'm doing a squash.



---

archive/issue_comments_065578.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-06-16T08:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65578",
    "user": "rws"
}
```

New commits:



---

archive/issue_comments_065579.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-06-16T08:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65579",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065580.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-10-04T07:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65580",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065581.json:
```json
{
    "body": "does not apply",
    "created_at": "2017-10-04T07:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65581",
    "user": "chapoton"
}
```

does not apply



---

archive/issue_comments_065582.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-10-04T08:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65582",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:
