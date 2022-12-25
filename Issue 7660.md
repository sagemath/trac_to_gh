# Issue 7660: arithmetic with equations and inequalities confusing

archive/issues_007660.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman\n\nKeywords: inequality, solver, maxima\n\nEquations and relations should behave like this:\nequations:\n* `(a==b) +-*/ c` same as:\n  - `(a==b).add_to_both_sides(c)`\n  - `(a==b).subtract_from_both_sides(c)`\n  - `(a==b).multiply_both_sides(c)`\n  - `(a==b).divide_both_sides(c)`\n  - `False` if `*/0`\n* `(a==b)^c` --> `a^c == b^c`\n* `f(a==b)` --> `f(a)==f(b)`\nrelations:\n* `(a<b) +- c` same as:\n  - `(a<b).add_to_both_sides(c)`\n  - `(a<b).subtract_from_both_sides(c)`\n* `(a<b) */ c` same as:\n  - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative\n  - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive\n  - `False` if `c=0` or assumed zero\n  - if `c` contains variables (and no assumptions exist about it) raise `ArithmeticError: missing assumption: is ...>0?`\n  - if `c` contains no variables `ArithmeticError: multiplication of inequality with irreal`\n* `(a<b)^c` --> `(a<b)^c`\n* `f(a<b)`  --> `f(a<b)`\n\nOriginal description:\n\nFrom the following sage-devel thread: \n\n\nhttp://groups.google.com/group/sage-devel/t/951d510c814f894f \n\n\n \nArithmetic with inequalities can be confusing, since Sage does nothing to keep the inequality ``correct``. For example: \n\n\n``` \nOn Thu, 10 Dec 2009 00:37:10 -0800 (PST) \n     \"marik@mendelu.cz\" <marik@mendelu.cz> wrote: \n      \n     > sage: f = x + 3 < y - 2 \n     > sage: f*(-1) \n     > -x - 3 < -y + 2 \n     }}} \n      \n     It seems MMA doesn't apply any automatic simplification in this case: \n      \n     {{{ \n     On Thu, 10 Dec 2009 09:54:36 -0800 \n     William Stein <wstein@gmail.com> wrote: \n      \n     > Mathematica does something weird and formal: \n     >  \n     > In[1]:= f := x+3 < y-2; \n     > In[3]:= f*(-1) \n     > Out[3]= -(3 + x < -2 + y) \n     }}} \n      \n     Maple acts more intuitively, though the way ``formal products`` are printed leaves something to be desired, IMHO: \n      \n     {{{ \n     On Thu, 10 Dec 2009 14:15:53 -0800 \n     William Stein <wstein@gmail.com> wrote: \n      \n     > Here is what Maple does: \n     >  \n     > flat:release_notes wstein$ maple \n     >     |\\^/|     Maple 13 (APPLE UNIVERSAL OSX) \n     > ._|\\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple \n     > Inc. 2009 \\  MAPLE  /  All rights reserved. Maple is a trademark of \n     >  <____ ____>  Waterloo Maple Inc. \n     >       |       Type ? for help. \n     > > f := x < y;   \n     >                                   f := x < y \n     >  \n     > > f*(-3);   \n     >                                   -3 y < -3 x \n     >  \n     > > f*z;   \n     >                                   *(x < y, z) \n     >  \n     > > f*a;   \n     >                                   *(x < y, a) \n     }}} \n      \n      \n     We should multiply both sides of the inequality only if the argument is a real number (as opposed to a symbol with real domain), and invert the relation when the argument is negative. \n      \n     Note that GiNaC leaves everything formal, like MMA, by default: \n      \n     {{{ \n     ginsh - GiNaC Interactive Shell (ginac V1.5.3) \n       __,  _______  Copyright (C) 1999-2009 Johannes Gutenberg University Mainz, \n      (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY. \n       ._) i N a C | You are welcome to redistribute it under certain conditions. \n     <-------------' For details type `warranty;'. \n      \n     Type ?? for a list of help topics. \n     > f= x < y; \n     x<y \n     > f*-1; \n     -(x<y) \n     > f*-5; \n     -5*(x<y) \n     > f*-z; \n     -z*(x<y) \n     > f*z; \n     z*(x<y) \n     }}}\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7660\n\n",
    "created_at": "2009-12-11T13:55:02Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "arithmetic with equations and inequalities confusing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7660",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @kcrisman

Keywords: inequality, solver, maxima

Equations and relations should behave like this:
equations:
* `(a==b) +-*/ c` same as:
  - `(a==b).add_to_both_sides(c)`
  - `(a==b).subtract_from_both_sides(c)`
  - `(a==b).multiply_both_sides(c)`
  - `(a==b).divide_both_sides(c)`
  - `False` if `*/0`
* `(a==b)^c` --> `a^c == b^c`
* `f(a==b)` --> `f(a)==f(b)`
relations:
* `(a<b) +- c` same as:
  - `(a<b).add_to_both_sides(c)`
  - `(a<b).subtract_from_both_sides(c)`
* `(a<b) */ c` same as:
  - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative
  - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive
  - `False` if `c=0` or assumed zero
  - if `c` contains variables (and no assumptions exist about it) raise `ArithmeticError: missing assumption: is ...>0?`
  - if `c` contains no variables `ArithmeticError: multiplication of inequality with irreal`
* `(a<b)^c` --> `(a<b)^c`
* `f(a<b)`  --> `f(a<b)`

Original description:

From the following sage-devel thread: 


http://groups.google.com/group/sage-devel/t/951d510c814f894f 


 
Arithmetic with inequalities can be confusing, since Sage does nothing to keep the inequality ``correct``. For example: 


``` 
On Thu, 10 Dec 2009 00:37:10 -0800 (PST) 
     "marik@mendelu.cz" <marik@mendelu.cz> wrote: 
      
     > sage: f = x + 3 < y - 2 
     > sage: f*(-1) 
     > -x - 3 < -y + 2 
     }}} 
      
     It seems MMA doesn't apply any automatic simplification in this case: 
      
     {{{ 
     On Thu, 10 Dec 2009 09:54:36 -0800 
     William Stein <wstein@gmail.com> wrote: 
      
     > Mathematica does something weird and formal: 
     >  
     > In[1]:= f := x+3 < y-2; 
     > In[3]:= f*(-1) 
     > Out[3]= -(3 + x < -2 + y) 
     }}} 
      
     Maple acts more intuitively, though the way ``formal products`` are printed leaves something to be desired, IMHO: 
      
     {{{ 
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
     }}} 
      
      
     We should multiply both sides of the inequality only if the argument is a real number (as opposed to a symbol with real domain), and invert the relation when the argument is negative. 
      
     Note that GiNaC leaves everything formal, like MMA, by default: 
      
     {{{ 
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
     }}}


Issue created by migration from https://trac.sagemath.org/ticket/7660





---

archive/issue_comments_065405.json:
```json
{
    "body": "```\nsage: -1*(x < y)\n-x < -y\n\n```\nthis is quite dangerous (I encountered it as a bug in a project).  Hopefully someone will try to fix this soon.  Could it be related to this  http://trac.sagemath.org/sage_trac/ticket/11309 ?",
    "created_at": "2011-06-16T23:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65405",
    "user": "https://trac.sagemath.org/admin/accounts/users/tnv"
}
```

```
sage: -1*(x < y)
-x < -y

```
this is quite dangerous (I encountered it as a bug in a project).  Hopefully someone will try to fix this soon.  Could it be related to this  http://trac.sagemath.org/sage_trac/ticket/11309 ?



---

archive/issue_comments_065406.json:
```json
{
    "body": "I propose the following: `a*(x<y)` should not be simplified, ever, other than simplifying `a`, `x`, or `y` individually. Are there any problems with this?",
    "created_at": "2012-06-01T21:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65406",
    "user": "https://github.com/kini"
}
```

I propose the following: `a*(x<y)` should not be simplified, ever, other than simplifying `a`, `x`, or `y` individually. Are there any problems with this?



---

archive/issue_comments_065407.json:
```json
{
    "body": "Given the ticket description details above and the discussion at #11309 and here, I think that Burcin's original proposal of \n* keeping the same if we know `a` is positive\n* reversing if we know `a` is negative (presumably in both of these cases only if `a` is coerced to the reals successfully, as Burcin says)\n* (not in original but reasonable) return something like `False` for `<` and `=` for `<=` if `a=0`?\n* returning something formal otherwise\nseems best.  It does seem reasonable to multiply by `-1`, after all, and tnv is right that this should either reverse the inequality or remain formal.",
    "created_at": "2012-06-02T01:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65407",
    "user": "https://github.com/kcrisman"
}
```

Given the ticket description details above and the discussion at #11309 and here, I think that Burcin's original proposal of 
* keeping the same if we know `a` is positive
* reversing if we know `a` is negative (presumably in both of these cases only if `a` is coerced to the reals successfully, as Burcin says)
* (not in original but reasonable) return something like `False` for `<` and `=` for `<=` if `a=0`?
* returning something formal otherwise
seems best.  It does seem reasonable to multiply by `-1`, after all, and tnv is right that this should either reverse the inequality or remain formal.



---

archive/issue_comments_065408.json:
```json
{
    "body": "It doesn't seem at all reasonable to me to distribute multiplication over a relation. When you distribute multiplication over addition, the addition expression `(a+b)` lives in the same space as `a` and `b` individually. This is not the case with `(x<y)` and `x` and `y`. \n\nThere is no mathematical rationale for saying that `(-1)*(x<y)` is `-x < -y` or `-x > -y` or anything other than just `(-1)*(x<y)`. I'm sure many can recall when they first learned basic algebra that their teacher was careful to say \"we multiply *both sides of* the equation by c\", not \"we multiply the equation by c\", just as he or she was careful to say \"we multiply both the numerator and denominator of the fraction by c\", rather than the dangerous \"we multiply the fraction by c\"!\n\nIf we allow multiplication to distribute over `x<y` as if it were a two-coordinate vector, do we want other similarities with vector arithmetic to come into play? Should `(a+b)*(x<y)` be equal to `a*(x<y) + b*(x<y)`? Now we have addition and presumably subtraction of relational expressions. What is `0*(x<y)`? What is `(x<y) + (z>y)`? Should we attempt to reverse inequalities to make them match up when adding them? Do we then end up with `(x+y<y+z)`, or `(y+z>x+y)`? Or, do we conclude that `(z>y)` is equal to `(-1)*(-z<-y)`, and so `(x<y) + (z>y) == (x<y) - (-z<-y) == (x+z<2y)`? Going beyond vector-like arithmetic, what happens when you add a scalar to a relational expression? What is `(x<y) + 3`?\n\nI think the most sensible answer to all the above questions is the following: we should not perform arithmetic on relational expressions; when asked to do so, we should return a purely formal expression.\n\nIf the title of this ticket disagrees with that answer, I can make another ticket to implement it, but I'm just wondering if anyone disagrees with me strongly about this.",
    "created_at": "2012-06-02T02:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65408",
    "user": "https://github.com/kini"
}
```

It doesn't seem at all reasonable to me to distribute multiplication over a relation. When you distribute multiplication over addition, the addition expression `(a+b)` lives in the same space as `a` and `b` individually. This is not the case with `(x<y)` and `x` and `y`. 

There is no mathematical rationale for saying that `(-1)*(x<y)` is `-x < -y` or `-x > -y` or anything other than just `(-1)*(x<y)`. I'm sure many can recall when they first learned basic algebra that their teacher was careful to say "we multiply *both sides of* the equation by c", not "we multiply the equation by c", just as he or she was careful to say "we multiply both the numerator and denominator of the fraction by c", rather than the dangerous "we multiply the fraction by c"!

If we allow multiplication to distribute over `x<y` as if it were a two-coordinate vector, do we want other similarities with vector arithmetic to come into play? Should `(a+b)*(x<y)` be equal to `a*(x<y) + b*(x<y)`? Now we have addition and presumably subtraction of relational expressions. What is `0*(x<y)`? What is `(x<y) + (z>y)`? Should we attempt to reverse inequalities to make them match up when adding them? Do we then end up with `(x+y<y+z)`, or `(y+z>x+y)`? Or, do we conclude that `(z>y)` is equal to `(-1)*(-z<-y)`, and so `(x<y) + (z>y) == (x<y) - (-z<-y) == (x+z<2y)`? Going beyond vector-like arithmetic, what happens when you add a scalar to a relational expression? What is `(x<y) + 3`?

I think the most sensible answer to all the above questions is the following: we should not perform arithmetic on relational expressions; when asked to do so, we should return a purely formal expression.

If the title of this ticket disagrees with that answer, I can make another ticket to implement it, but I'm just wondering if anyone disagrees with me strongly about this.



---

archive/issue_comments_065409.json:
```json
{
    "body": "Well, we could go to the !Ginac/Mathematica way too, instead of the Maple way.  But now that #11309 is on the way in, probably it's time to deal with this.  FWIW, Maxima seems to go that way as well.\n\n```\n(%i1) x<y;\n(%o1)                                x < y\n(%i2) a:x<y;\n(%o2)                                x < y\n(%i3) a;\n(%o3)                                x < y\n(%i4) -1*a;\n(%o4)                              - (x < y)\n(%i5) b*a;\n(%o5)                              b (x < y)\n```\nMaybe Burcin has a comment; I don't have that strong of feelings, though I'm partial to \n* `(x<y)+3 == x+3<y+3`\n* `0*(x<y) is False`\nbut those may just be sentimental, as you suggest.",
    "created_at": "2012-06-02T02:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65409",
    "user": "https://github.com/kcrisman"
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

archive/issue_comments_065410.json:
```json
{
    "body": "Honestly I thought the most likely response would be `0*(x<y) == 0`. `False` is an even stranger result because now you have `(x<y) == (1+0)*(x<y) == (x<y) + False`, so either `False` is now another additive identity (on relations, anyway), thus breaking the universality of `? - ? = 0`, or `False == 0`, which is another can of worms...\n\nAnd if `(x<y)+3 == (x+3<y+3)`, then presumably `3 == (3<3) == False`...?\n\nNone of this makes any sense, IMHO. I think it would be best to go the Mathematica/GiNaC/Maxima way, as shown in your Maxima output, rather than the Maple way.",
    "created_at": "2012-06-02T02:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65410",
    "user": "https://github.com/kini"
}
```

Honestly I thought the most likely response would be `0*(x<y) == 0`. `False` is an even stranger result because now you have `(x<y) == (1+0)*(x<y) == (x<y) + False`, so either `False` is now another additive identity (on relations, anyway), thus breaking the universality of `? - ? = 0`, or `False == 0`, which is another can of worms...

And if `(x<y)+3 == (x+3<y+3)`, then presumably `3 == (3<3) == False`...?

None of this makes any sense, IMHO. I think it would be best to go the Mathematica/GiNaC/Maxima way, as shown in your Maxima output, rather than the Maple way.



---

archive/issue_comments_065411.json:
```json
{
    "body": "For the record, Maxima has a share package which implements arithmetic on inequalities.\n\n```\n(%i1) load (ineq);\n(%o1) /home/robert/maxima/maxima-git/maxima-code/share/simplification/ineq.mac\n(%i2) e:a < b;\n(%o2)                                a < b\n(%i3) x*e;\nIs  x  positive, negative, or zero?\np;\n(%o3)                              a x < b x\n(%i4) x*e;\nIs  x  positive, negative, or zero?\nn;\n(%o4)                              a x > b x\n(%i5) x*e;\nIs  x  positive, negative, or zero?\nz;\n(%o5)                              (a < b) x\n```\nI gather that's similar to what Maple does.",
    "created_at": "2013-01-08T02:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65411",
    "user": "https://trac.sagemath.org/admin/accounts/users/robert_dodier"
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

archive/issue_comments_065412.json:
```json
{
    "body": "prototype patch",
    "created_at": "2013-01-09T11:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65412",
    "user": "https://github.com/burcin"
}
```

prototype patch



---

archive/issue_comments_065413.json:
```json
{
    "body": "Attachment [trac_7660-inequality_arithmetic.patch](tarball://root/attachments/some-uuid/ticket7660/trac_7660-inequality_arithmetic.patch) by @burcin created at 2013-01-09 11:09:14\n\nattachment:trac_7660-inequality_arithmetic.patch comments out a few lines in `_add_`, `_mul_`, etc., methods of symbolic expressions to pass the arithmetic on to GiNaC directly. I don't have time to test this and verify that it returns sensible answers, however we decide to define \"sensible\". Please test, see what doctests fail and try to produce horrific wrong results.\n\nQuite a few doctests and some documentation will have to change to match this new design decision. I'd like to make sure we agree on the behavior before trying to produce a clean patch. Of course, I'd appreciate help with the documentation in any case.",
    "created_at": "2013-01-09T11:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65413",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7660-inequality_arithmetic.patch](tarball://root/attachments/some-uuid/ticket7660/trac_7660-inequality_arithmetic.patch) by @burcin created at 2013-01-09 11:09:14

attachment:trac_7660-inequality_arithmetic.patch comments out a few lines in `_add_`, `_mul_`, etc., methods of symbolic expressions to pass the arithmetic on to GiNaC directly. I don't have time to test this and verify that it returns sensible answers, however we decide to define "sensible". Please test, see what doctests fail and try to produce horrific wrong results.

Quite a few doctests and some documentation will have to change to match this new design decision. I'd like to make sure we agree on the behavior before trying to produce a clean patch. Of course, I'd appreciate help with the documentation in any case.



---

archive/issue_events_018238.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18238"
}
```



---

archive/issue_events_018239.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18239"
}
```



---

archive/issue_events_018240.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18240"
}
```



---

archive/issue_comments_065414.json:
```json
{
    "body": "OK that patch applies cleanly with `patch -l`. It results in\n\n```\nsage: var('x')\nx\nsage: x>1\nx > 1\nsage: ie=_\nsage: ie*-1\n-(x > 1)\nsage: solve(_,x)\n...\nRuntimeError: ECL says: THROW: The catch MACSYMA-QUIT is undefined.\n```\nI refrained from starting any doctests.",
    "created_at": "2014-02-17T15:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65414",
    "user": "https://github.com/rwst"
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

archive/issue_comments_065415.json:
```json
{
    "body": "Changing keywords from \"\" to \"inequality, solver, maxima\".",
    "created_at": "2014-02-17T15:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65415",
    "user": "https://github.com/rwst"
}
```

Changing keywords from "" to "inequality, solver, maxima".



---

archive/issue_comments_065416.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-02-17T15:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65416",
    "user": "https://github.com/rwst"
}
```

New commits:



---

archive/issue_comments_065417.json:
```json
{
    "body": "Here are the statements sent via `maxima_eval(\"#$%s$\"%statement)`:\n\nBefore:\n\n```\nsage: solve(-(x > 1),x)\nsage0 : (x)*(-1) > -1\nsage1 : solve_rat_ineq(sage0)\n_tmp_ : sage1\nkill(sage1)\nkill(sage0)\n[[x < 1]]\n```\nAfter:\n\n```\nsage: solve(-(x > 1),x)\nsage12 : (x > 1)*(-1) = 0\nsage13 : x\nsage14 : solve(sage12,sage13)\nkill(sage13)\nkill(sage14)\n_tmp_ : [x>1=0]          <---------?\nkill(sage12)\n```\nApparently, Sage's last statement sent is the result itself (no idea why), and maxima then barfs because it can't digest its own output. In maxima:\n\n```\n(%i11) solve((x > 1)*(-1) = 0,x);\n(%o11)                            [x > 1 = 0]\n(%i12) [x>1=0];\nincorrect syntax: Found logical expression where algebraic expression expected\n[x>1=\n   ^\n```\nIn summary there are three problems:\n* 46 doctests fail in symbolic alone\n* maxima can't handle the formal expressions generated via this patch, and `solve()` will fail because it uses maxima solve() and not solve_rat_ineq() (probably because the expression looks like an algebraic). However:\n\n```\nsage: solve_ineq((x>1)*(-1),[x,y])\n#0: solve_rat_ineq(ineq=-(x > 1))\n...\nTypeError: ECL says: Error executing code in Maxima: solve_rat_ineq:  -(x > 1)  is not an inequality.\n```\nSo maxima refuses to handle the formal expression generated by this patch, and this means they cannot be solved, regardless of method called. So, in addition, `solve()` should be changed to do simplification of these expressions before handing them on. This special simplification avoids all issues raised in comment:10. It can be implemented after this ticket (#15906).\n* `calculus.py:symbolic_expression_from_maxima_string()` should catch maxima `RuntimeError`s from `ecl.c` and rethrow them with meaningful information. (#15902)\n`",
    "created_at": "2014-03-06T16:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65417",
    "user": "https://github.com/rwst"
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

archive/issue_comments_065418.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-06T16:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65418",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065419.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-07T16:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65419",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065420.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-07T16:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65420",
    "user": "https://github.com/rwst"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065421.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-12T08:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65421",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065422.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-02T13:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65422",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_018241.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18241"
}
```



---

archive/issue_events_018242.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18242"
}
```



---

archive/issue_events_018243.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18243"
}
```



---

archive/issue_events_018244.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18244"
}
```



---

archive/issue_comments_065423.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-11-02T22:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65423",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065424.json:
```json
{
    "body": "Please use python3 compatible `raise TypeError` syntax.",
    "created_at": "2014-11-02T22:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65424",
    "user": "https://github.com/a-andre"
}
```

Please use python3 compatible `raise TypeError` syntax.



---

archive/issue_comments_065425.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-03T08:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65425",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065426.json:
```json
{
    "body": "Replying to [comment:26 aapitzsch]:\n> Please use python3 compatible `raise TypeError` syntax.\nDone. Still, doctests fail in `expression.pyx`.",
    "created_at": "2014-11-03T08:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65426",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:26 aapitzsch]:
> Please use python3 compatible `raise TypeError` syntax.
Done. Still, doctests fail in `expression.pyx`.



---

archive/issue_comments_065427.json:
```json
{
    "body": "This came up again in http://ask.sagemath.org/question/25217/how-to-do-operations-that-change-a-relation/",
    "created_at": "2014-12-11T14:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65427",
    "user": "https://github.com/rwst"
}
```

This came up again in http://ask.sagemath.org/question/25217/how-to-do-operations-that-change-a-relation/



---

archive/issue_comments_065428.json:
```json
{
    "body": "I'm just now looking at this ticket and personally I don't like to lose the ability to compute with relations. I think that the fact that `(a == b)^2` returns `a^2 == b^2` is a feature, not a bug. I'd say it's up to the user to ensure that the operation makes sense.\n\nWould it be possible to keep the old behaviour for equalities `==` at least?",
    "created_at": "2014-12-11T16:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65428",
    "user": "https://github.com/jdemeyer"
}
```

I'm just now looking at this ticket and personally I don't like to lose the ability to compute with relations. I think that the fact that `(a == b)^2` returns `a^2 == b^2` is a feature, not a bug. I'd say it's up to the user to ensure that the operation makes sense.

Would it be possible to keep the old behaviour for equalities `==` at least?



---

archive/issue_comments_065429.json:
```json
{
    "body": "Let's start this fresh. To summarize, what's wanted is the following:\n\nequations:\n* `(a==b) +-*/ c` same as:\n  - `(a==b).add_to_both_sides(c)`\n  - `(a==b).subtract_from_both_sides(c)`\n  - `(a==b).multiply_both_sides(c)`\n  - `(a==b).divide_both_sides(c)`\n  - `False` if `*/0`\n* `(a==b)^c` --> `a^c == b^c`\n* `f(a==b)` --> `f(a==b)`\nrelations:\n* `(a<b) +- c` same as:\n  - `(a<b).add_to_both_sides(c)`\n  - `(a<b).subtract_from_both_sides(c)`\n* `(a<b) */ c` same as:\n  - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative\n  - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive\n  - `False` if `c=0`\n* `(a<b)^c` --> `(a<b)^c`\n* `f(a<b)`  --> `f(a<b)`\n\nQuestion: Real or: if coerced to the reals successfully?\nA followup extension would be like Maxima's ineq package, i.e., ask before doing a sign switch.",
    "created_at": "2015-02-12T08:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65429",
    "user": "https://github.com/rwst"
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

archive/issue_comments_065430.json:
```json
{
    "body": "Replying to [comment:31 rws]:\n>  * `f(a==b)` --> `f(a==b)`\n \nWhat does `f(a==b)` even mean? I would go for `f(a) == f(b)`.\n\n> relations:\n> * `(a<b) */ c` same as:\n>   - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative\n>   - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive\n>   - `False` if `c=0`\n\n\nWhat if neither of the above conditions is true? `raise ArithmeticError` in that case?",
    "created_at": "2015-02-12T09:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65430",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:31 rws]:
>  * `f(a==b)` --> `f(a==b)`
 
What does `f(a==b)` even mean? I would go for `f(a) == f(b)`.

> relations:
> * `(a<b) */ c` same as:
>   - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative
>   - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive
>   - `False` if `c=0`


What if neither of the above conditions is true? `raise ArithmeticError` in that case?



---

archive/issue_comments_065431.json:
```json
{
    "body": "Replying to [comment:32 jdemeyer]:\n> >  * `(a<b) */ c`\n \n> What if neither of the above conditions is true? `raise ArithmeticError` in that case?\nNot if `c` contains variables. Is there even a way of determining this?",
    "created_at": "2015-02-12T09:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65431",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:32 jdemeyer]:
> >  * `(a<b) */ c`
 
> What if neither of the above conditions is true? `raise ArithmeticError` in that case?
Not if `c` contains variables. Is there even a way of determining this?



---

archive/issue_comments_065432.json:
```json
{
    "body": "Replying to [comment:33 rws]:\n> Not if `c` contains variables.\n\n\nWhat would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?",
    "created_at": "2015-02-12T09:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65432",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:33 rws]:
> Not if `c` contains variables.


What would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?



---

archive/issue_comments_065433.json:
```json
{
    "body": "Replying to [comment:34 jdemeyer]:\n> What would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?\n\nSince this ticket will check for assumptions, if there is none we should raise an `ArithmeticError` demanding one.",
    "created_at": "2015-02-12T09:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65433",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:34 jdemeyer]:
> What would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?

Since this ticket will check for assumptions, if there is none we should raise an `ArithmeticError` demanding one.



---

archive/issue_comments_065434.json:
```json
{
    "body": "So my statement to `raise ArithmeticError` if neither condition is true still remains.",
    "created_at": "2015-02-12T09:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65434",
    "user": "https://github.com/jdemeyer"
}
```

So my statement to `raise ArithmeticError` if neither condition is true still remains.



---

archive/issue_comments_065435.json:
```json
{
    "body": "Replying to [ticket:7660 burcin]:\n>    - if `c` contains variables (and no assumptions exist about it) raise `ArithmeticError: missing assumption: is ...>0?`\n>    - if `c` contains no variables `ArithmeticError: multiplication of inequality with irreal`\n\n\nI think it will be easier if these are just one case.",
    "created_at": "2015-02-12T09:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65435",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [ticket:7660 burcin]:
>    - if `c` contains variables (and no assumptions exist about it) raise `ArithmeticError: missing assumption: is ...>0?`
>    - if `c` contains no variables `ArithmeticError: multiplication of inequality with irreal`


I think it will be easier if these are just one case.



---

archive/issue_comments_065436.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-02-12T16:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65436",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065437.json:
```json
{
    "body": "Since the `f()` stuff requires changes in function base classes, and assumptions are also an involvement, I'll leave both to followup tickets. Please review.\n\n---\nNew commits:",
    "created_at": "2015-02-12T16:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65437",
    "user": "https://github.com/rwst"
}
```

Since the `f()` stuff requires changes in function base classes, and assumptions are also an involvement, I'll leave both to followup tickets. Please review.

---
New commits:



---

archive/issue_comments_065438.json:
```json
{
    "body": "Why convert to `RR`? I would simply use\n\n```\nif right == 0:\n    ...\nelif right >= 0:\n    ...\nelif right <= 0:\n    ...\nelse:\n    raise ArithmeticError(...)\n```\nThis handles non-constant symbolic expressions also.",
    "created_at": "2015-02-12T16:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65438",
    "user": "https://github.com/jdemeyer"
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

archive/issue_comments_065439.json:
```json
{
    "body": "Replying to [comment:42 jdemeyer]:\n> Why convert to `RR`? I would simply use\n> \n> ```\n> if right == 0:\n>     ...\n> elif right >= 0:\n>     ...\n> elif right <= 0:\n>     ...\n> else:\n>     raise ArithmeticError(...)\n> ```\n> This handles non-constant symbolic expressions also.\n\nSeems we have to open a ticket?\n\n```\nsage: def f(ex):\n    if ex==0:\n        print 'zero'\n    elif ex<0:\n        print 'minus'\n    else:\n        print 'else'\n....:         \nsage: ex=-I\nsage: f(ex)\nminus\nsage: bool(-I<0)\nTrue\nsage: bool(I>0)\nTrue\n```",
    "created_at": "2015-02-13T14:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65439",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:42 jdemeyer]:
> Why convert to `RR`? I would simply use
> 
> ```
> if right == 0:
>     ...
> elif right >= 0:
>     ...
> elif right <= 0:
>     ...
> else:
>     raise ArithmeticError(...)
> ```
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

archive/issue_comments_065440.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-13T14:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65440",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065441.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-05T14:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65441",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_018245.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-04-15T06:37:34Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18245"
}
```



---

archive/issue_events_018246.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-04-15T06:37:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18246"
}
```



---

archive/issue_comments_065442.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-19T05:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65442",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_018247.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-05-27T19:27:23Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18247"
}
```



---

archive/issue_events_018248.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-05-27T19:27:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18248"
}
```



---

archive/issue_comments_065443.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-03T06:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65443",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065444.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-20T13:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65444",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065445.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-01-10T21:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65445",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065446.json:
```json
{
    "body": "`@`aapitzsch Are you willing to review this issue?",
    "created_at": "2016-01-11T07:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65446",
    "user": "https://github.com/rwst"
}
```

`@`aapitzsch Are you willing to review this issue?



---

archive/issue_comments_065447.json:
```json
{
    "body": "Replying to [comment:53 rws]:\n> `@`aapitzsch Are you willing to review this issue?\nNo. Sorry for the noise.",
    "created_at": "2016-01-11T18:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65447",
    "user": "https://github.com/a-andre"
}
```

Replying to [comment:53 rws]:
> `@`aapitzsch Are you willing to review this issue?
No. Sorry for the noise.



---

archive/issue_comments_065448.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-10-06T13:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65448",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065449.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-10-06T13:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65449",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_018249.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2016-10-06T13:55:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18249"
}
```



---

archive/issue_events_018250.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2016-10-06T13:55:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-7.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18250"
}
```



---

archive/issue_comments_065450.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-10-06T14:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65450",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065451.json:
```json
{
    "body": "Relevant doctest fail in `src/sage/misc/sageinspect.py`",
    "created_at": "2017-01-14T08:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65451",
    "user": "https://github.com/rwst"
}
```

Relevant doctest fail in `src/sage/misc/sageinspect.py`



---

archive/issue_comments_065452.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-01-14T08:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65452",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065453.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-01-15T07:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65453",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_018251.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2017-01-15T07:53:31Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-7.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18251"
}
```



---

archive/issue_events_018252.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2017-01-15T07:53:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-7.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18252"
}
```



---

archive/issue_comments_065454.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-01-15T07:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65454",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065455.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-02-27T18:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65455",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065456.json:
```json
{
    "body": "does not apply",
    "created_at": "2017-02-27T18:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65456",
    "user": "https://github.com/fchapoton"
}
```

does not apply



---

archive/issue_comments_065457.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-02-28T07:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65457",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065458.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-02-28T07:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65458",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065459.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-06-16T07:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65459",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065460.json:
```json
{
    "body": "does not apply",
    "created_at": "2017-06-16T07:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65460",
    "user": "https://github.com/fchapoton"
}
```

does not apply



---

archive/issue_comments_065461.json:
```json
{
    "body": "In the course of this ticket already 12 merge commits were added. The branch has 8 so I'm doing a squash.",
    "created_at": "2017-06-16T07:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65461",
    "user": "https://github.com/rwst"
}
```

In the course of this ticket already 12 merge commits were added. The branch has 8 so I'm doing a squash.



---

archive/issue_comments_065462.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-06-16T08:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65462",
    "user": "https://github.com/rwst"
}
```

New commits:



---

archive/issue_comments_065463.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-06-16T08:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65463",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_018253.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2017-06-16T08:25:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-7.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18253"
}
```



---

archive/issue_events_018254.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2017-06-16T08:25:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-8.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18254"
}
```



---

archive/issue_comments_065464.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-10-04T07:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65464",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_events_018255.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-10-04T07:43:23Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-8.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18255"
}
```



---

archive/issue_events_018256.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-10-04T07:43:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "milestone": "sage-8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7660#event-18256"
}
```



---

archive/issue_comments_065465.json:
```json
{
    "body": "does not apply",
    "created_at": "2017-10-04T07:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65465",
    "user": "https://github.com/fchapoton"
}
```

does not apply



---

archive/issue_comments_065466.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-10-04T08:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7660#issuecomment-65466",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:
