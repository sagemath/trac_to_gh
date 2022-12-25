# Issue 7496: symbolic variable names should be valid identifiers, or ridiculousness follows

archive/issues_007496.json:
```json
{
    "body": "Assignee: @burcin\n\nWTF?\n\n\n```\nsage: var('1')\n1\nsage: var('1')+1\n1 + 1\nsage: expand((var('2')+var('2'))^2)\n4*2^2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7496\n\n",
    "created_at": "2009-11-20T02:16:09Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "symbolic variable names should be valid identifiers, or ridiculousness follows",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7496",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin

WTF?


```
sage: var('1')
1
sage: var('1')+1
1 + 1
sage: expand((var('2')+var('2'))^2)
4*2^2
```


Issue created by migration from https://trac.sagemath.org/ticket/7496





---

archive/issue_comments_063243.json:
```json
{
    "body": "This would be really easy to implement once we have python 3. Apparently, valid identifiers got extended:\n\nhttp://www.python.org/dev/peps/pep-3131/\n\nString literals also got an `isidentifier()` method.\n\nI don't know how to do this efficiently, while still allowing people to just use \u03b1 (alpha) as a variable name.",
    "created_at": "2010-01-17T08:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63243",
    "user": "https://github.com/burcin"
}
```

This would be really easy to implement once we have python 3. Apparently, valid identifiers got extended:

http://www.python.org/dev/peps/pep-3131/

String literals also got an `isidentifier()` method.

I don't know how to do this efficiently, while still allowing people to just use α (alpha) as a variable name.



---

archive/issue_comments_063244.json:
```json
{
    "body": "As long as we don't have Python 3, I would try to find a regular expression that does what we need. It is of course easy to write a regular expression that works for ascii strings. But as soon as '\u00e4' or other language-specific letters are supposed to be considered a variable name, things will become difficult.\n\nI tried\n\n```\nsage: import re\nsage: _identifiers = re.compile(\"(?!\\d)\\w*\\Z\", re.LOCALE|re.UNICODE)\n```\n\n\nIt works for simple cases:\n\n```\nsage: _identifiers.match('k_1')\n<_sre.SRE_Match object at 0x50d1030>\nsage: _identifiers.match('1k')\nsage: _identifiers.match('_1k')\n<_sre.SRE_Match object at 0x50d1238>\n```\n\n\nBut it ignores other letters:\n\n```\nsage: print _identifiers.match('\u00e4')\nNone\n```\n\n\nPerhaps I have misunderstood the effect of `re.LOCALE`? What value should `re.LOCALE` have in order to work with accented letters?",
    "created_at": "2011-03-03T10:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63244",
    "user": "https://github.com/simon-king-jena"
}
```

As long as we don't have Python 3, I would try to find a regular expression that does what we need. It is of course easy to write a regular expression that works for ascii strings. But as soon as 'ä' or other language-specific letters are supposed to be considered a variable name, things will become difficult.

I tried

```
sage: import re
sage: _identifiers = re.compile("(?!\d)\w*\Z", re.LOCALE|re.UNICODE)
```


It works for simple cases:

```
sage: _identifiers.match('k_1')
<_sre.SRE_Match object at 0x50d1030>
sage: _identifiers.match('1k')
sage: _identifiers.match('_1k')
<_sre.SRE_Match object at 0x50d1238>
```


But it ignores other letters:

```
sage: print _identifiers.match('ä')
None
```


Perhaps I have misunderstood the effect of `re.LOCALE`? What value should `re.LOCALE` have in order to work with accented letters?



---

archive/issue_comments_063245.json:
```json
{
    "body": "Whatever we do, let's be sure to avoid locality dependance on what a valid symbol is. Let's look into back-porting whatever Python3 does, and then falling back to that once we make the transition.",
    "created_at": "2011-03-03T21:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63245",
    "user": "https://github.com/robertwb"
}
```

Whatever we do, let's be sure to avoid locality dependance on what a valid symbol is. Let's look into back-porting whatever Python3 does, and then falling back to that once we make the transition.



---

archive/issue_comments_063246.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-18T04:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63246",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063247.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd31\".",
    "created_at": "2011-06-18T04:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63247",
    "user": "https://github.com/vbraun"
}
```

Changing keywords from "" to "sd31".



---

archive/issue_comments_063248.json:
```json
{
    "body": "This code should be correct - nice to learn something about the parser and bytecode.  Is this how it's implemented in Python 3 (presumably that's written in C, though)?  I couldn't find it, anyway.\n\nThis needs doctests just to document that `var('3')` and `var(' ')` (see #9724) fail, though of course the tests already here document this indirectly.  I'll post a reviewer patch momentarily, assuming I didn't miss something and the patch doesn't actually work.",
    "created_at": "2011-06-24T01:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63248",
    "user": "https://github.com/kcrisman"
}
```

This code should be correct - nice to learn something about the parser and bytecode.  Is this how it's implemented in Python 3 (presumably that's written in C, though)?  I couldn't find it, anyway.

This needs doctests just to document that `var('3')` and `var(' ')` (see #9724) fail, though of course the tests already here document this indirectly.  I'll post a reviewer patch momentarily, assuming I didn't miss something and the patch doesn't actually work.



---

archive/issue_comments_063249.json:
```json
{
    "body": "Ok, I think this is still ok, though I am a little concerned about both of the following being bad:\n\n```\nsage: var(' x')\n(, x)\n```\n\nnot good because an empty string is a variable\n\n```\nsage: var(' x')\n---------------------------------------------------------------------------\nValueError: The name \"\" is not a valid Python identifier.\n```\n\nnot good because the intent is clear to make precisely x the variable.  \n\nSo is this breaking incorrect but usable behavior? \n\n```\nsage: var(\"x y  z\")\n(x, y, , z)\nsage: \n```\n\nis similar.\n\nAnyway, I withhold judgment on this.  Reviewer patch attached, but 'needs info' on this.  At the least it seems reasonable to open a new ticket to allow the above behavior - one could easily remove empty strings from the list `names_list` and then complain if there are none left, for instance.",
    "created_at": "2011-06-24T03:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63249",
    "user": "https://github.com/kcrisman"
}
```

Ok, I think this is still ok, though I am a little concerned about both of the following being bad:

```
sage: var(' x')
(, x)
```

not good because an empty string is a variable

```
sage: var(' x')
---------------------------------------------------------------------------
ValueError: The name "" is not a valid Python identifier.
```

not good because the intent is clear to make precisely x the variable.  

So is this breaking incorrect but usable behavior? 

```
sage: var("x y  z")
(x, y, , z)
sage: 
```

is similar.

Anyway, I withhold judgment on this.  Reviewer patch attached, but 'needs info' on this.  At the least it seems reasonable to open a new ticket to allow the above behavior - one could easily remove empty strings from the list `names_list` and then complain if there are none left, for instance.



---

archive/issue_comments_063250.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-06-24T03:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63250",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_063251.json:
```json
{
    "body": "Attachment [trac_7496-reviewer.patch](tarball://root/attachments/some-uuid/ticket7496/trac_7496-reviewer.patch) by @kcrisman created at 2011-06-24 03:08:43\n\nApply after initial patch",
    "created_at": "2011-06-24T03:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63251",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_7496-reviewer.patch](tarball://root/attachments/some-uuid/ticket7496/trac_7496-reviewer.patch) by @kcrisman created at 2011-06-24 03:08:43

Apply after initial patch



---

archive/issue_comments_063252.json:
```json
{
    "body": "Apply [attachment:trac_7496_check_symbolic_variable_names.patch] and [attachment:trac_7496-reviewer.patch].",
    "created_at": "2011-06-24T03:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63252",
    "user": "https://github.com/kcrisman"
}
```

Apply [attachment:trac_7496_check_symbolic_variable_names.patch] and [attachment:trac_7496-reviewer.patch].



---

archive/issue_comments_063253.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-06-24T05:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63253",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_063254.json:
```json
{
    "body": "Updated patch splits with any white space and not only on single space:\n\n```\n    sage: var(' x y  z    ')\n    (x, y, z)\n    sage: var(' x  ,  y ,  z    ') \n    (x, y, z)\n```\n\nI'm giving the reviewer patch a positive review.",
    "created_at": "2011-06-24T05:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63254",
    "user": "https://github.com/vbraun"
}
```

Updated patch splits with any white space and not only on single space:

```
    sage: var(' x y  z    ')
    (x, y, z)
    sage: var(' x  ,  y ,  z    ') 
    (x, y, z)
```

I'm giving the reviewer patch a positive review.



---

archive/issue_comments_063255.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-24T11:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63255",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063256.json:
```json
{
    "body": "Thanks.  So far it looks good.\n\nBut with the original version of the patch (and almost certainly the new one) we get the following doctest error (was letting them run overnight, my apologies):\n\n```\nsage -t -long \"devel/sage/sage/calculus/desolvers.py\"       \n**********************************************************************\nFile \"/Users/.../sage-4.7.1.alpha2/devel/sage/sage/calculus/desolvers.py\", line 1430:\n    sage: sol=desolve_odeint(f,[0.5,2],srange(0,10,0.1),[x,y])\nException raised:\n        sol=desolve_odeint(f,[RealNumber('0.5'),Integer(2)],srange(Integer(0),Integer(10),RealNumber('0.1')),[x,y])###line 1430:\n    sage: sol=desolve_odeint(f,[0.5,2],srange(0,10,0.1),[x,y])\n      File \"/Users/.../sage-4.7.1.alpha2/local/lib/python/site-packages/sage/calculus/desolvers.py\", line 1501, in desolve_odeint\n        ivar = var(safe_name)\n      File \"ring.pyx\", line 798, in sage.symbolic.ring.var (sage/symbolic/ring.cpp:7745)\n      File \"ring.pyx\", line 506, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6272)\n      File \"ring.pyx\", line 534, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6044)\n    ValueError: The name \"t_[x\" is not a valid Python identifier.\n**********************************************************************\n<snip two failures that result from sol not being defined>\n**********************************************************************\nFile \"/Users/.../sage-4.7.1.alpha2/devel/sage/sage/calculus/desolvers.py\", line 1446:\n    sage: sol=desolve_odeint(lorenz,ics,times,[x,y,z],rtol=1e-13,atol=1e-14)\nException raised:\n      File \"<doctest __main__.example_12[15]>\", line 1, in <module>\n        sol=desolve_odeint(lorenz,ics,times,[x,y,z],rtol=RealNumber('1e-13'),atol=RealNumber('1e-14'))###line 1446:\n    sage: sol=desolve_odeint(lorenz,ics,times,[x,y,z],rtol=1e-13,atol=1e-14)\n      File \"/Users/.../sage-4.7.1.alpha2/local/lib/python/site-packages/sage/calculus/desolvers.py\", line 1501, in desolve_odeint\n        ivar = var(safe_name)\n      File \"ring.pyx\", line 798, in sage.symbolic.ring.var (sage/symbolic/ring.cpp:7745)\n      File \"ring.pyx\", line 506, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6272)\n      File \"ring.pyx\", line 534, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6044)\n    ValueError: The name \"t_[x\" is not a valid Python identifier.\n**********************************************************************\nFile \"/Users/.../sage-4.7.1.alpha2/devel/sage/sage/calculus/desolvers.py\", line 1470:\n    sage: sol=desolve_odeint(f,ci,t,v,rtol=1e-3,atol=1e-4,h0=0.1,hmax=1,hmin=1e-4,mxstep=1000,mxords=17)\nException raised:\n      File \"<doctest __main__.example_12[32]>\", line 1, in <module>\n        sol=desolve_odeint(f,ci,t,v,rtol=RealNumber('1e-3'),atol=RealNumber('1e-4'),h0=RealNumber('0.1'),hmax=Integer(1),hmin=RealNumber('1e-4'),mxstep=Integer(1000),mxords=Integer(17))###line 1470:\n    sage: sol=desolve_odeint(f,ci,t,v,rtol=1e-3,atol=1e-4,h0=0.1,hmax=1,hmin=1e-4,mxstep=1000,mxords=17)\n      File \"/Users/.../sage-4.7.1.alpha2/local/lib/python/site-packages/sage/calculus/desolvers.py\", line 1501, in desolve_odeint\n        ivar = var(safe_name)\n      File \"ring.pyx\", line 798, in sage.symbolic.ring.var (sage/symbolic/ring.cpp:7745)\n      File \"ring.pyx\", line 506, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6272)\n      File \"ring.pyx\", line 534, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6044)\n    ValueError: The name \"t_[y1\" is not a valid Python identifier.\n**********************************************************************\n```\n",
    "created_at": "2011-06-24T11:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63256",
    "user": "https://github.com/kcrisman"
}
```

Thanks.  So far it looks good.

But with the original version of the patch (and almost certainly the new one) we get the following doctest error (was letting them run overnight, my apologies):

```
sage -t -long "devel/sage/sage/calculus/desolvers.py"       
**********************************************************************
File "/Users/.../sage-4.7.1.alpha2/devel/sage/sage/calculus/desolvers.py", line 1430:
    sage: sol=desolve_odeint(f,[0.5,2],srange(0,10,0.1),[x,y])
Exception raised:
        sol=desolve_odeint(f,[RealNumber('0.5'),Integer(2)],srange(Integer(0),Integer(10),RealNumber('0.1')),[x,y])###line 1430:
    sage: sol=desolve_odeint(f,[0.5,2],srange(0,10,0.1),[x,y])
      File "/Users/.../sage-4.7.1.alpha2/local/lib/python/site-packages/sage/calculus/desolvers.py", line 1501, in desolve_odeint
        ivar = var(safe_name)
      File "ring.pyx", line 798, in sage.symbolic.ring.var (sage/symbolic/ring.cpp:7745)
      File "ring.pyx", line 506, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6272)
      File "ring.pyx", line 534, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6044)
    ValueError: The name "t_[x" is not a valid Python identifier.
**********************************************************************
<snip two failures that result from sol not being defined>
**********************************************************************
File "/Users/.../sage-4.7.1.alpha2/devel/sage/sage/calculus/desolvers.py", line 1446:
    sage: sol=desolve_odeint(lorenz,ics,times,[x,y,z],rtol=1e-13,atol=1e-14)
Exception raised:
      File "<doctest __main__.example_12[15]>", line 1, in <module>
        sol=desolve_odeint(lorenz,ics,times,[x,y,z],rtol=RealNumber('1e-13'),atol=RealNumber('1e-14'))###line 1446:
    sage: sol=desolve_odeint(lorenz,ics,times,[x,y,z],rtol=1e-13,atol=1e-14)
      File "/Users/.../sage-4.7.1.alpha2/local/lib/python/site-packages/sage/calculus/desolvers.py", line 1501, in desolve_odeint
        ivar = var(safe_name)
      File "ring.pyx", line 798, in sage.symbolic.ring.var (sage/symbolic/ring.cpp:7745)
      File "ring.pyx", line 506, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6272)
      File "ring.pyx", line 534, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6044)
    ValueError: The name "t_[x" is not a valid Python identifier.
**********************************************************************
File "/Users/.../sage-4.7.1.alpha2/devel/sage/sage/calculus/desolvers.py", line 1470:
    sage: sol=desolve_odeint(f,ci,t,v,rtol=1e-3,atol=1e-4,h0=0.1,hmax=1,hmin=1e-4,mxstep=1000,mxords=17)
Exception raised:
      File "<doctest __main__.example_12[32]>", line 1, in <module>
        sol=desolve_odeint(f,ci,t,v,rtol=RealNumber('1e-3'),atol=RealNumber('1e-4'),h0=RealNumber('0.1'),hmax=Integer(1),hmin=RealNumber('1e-4'),mxstep=Integer(1000),mxords=Integer(17))###line 1470:
    sage: sol=desolve_odeint(f,ci,t,v,rtol=1e-3,atol=1e-4,h0=0.1,hmax=1,hmin=1e-4,mxstep=1000,mxords=17)
      File "/Users/.../sage-4.7.1.alpha2/local/lib/python/site-packages/sage/calculus/desolvers.py", line 1501, in desolve_odeint
        ivar = var(safe_name)
      File "ring.pyx", line 798, in sage.symbolic.ring.var (sage/symbolic/ring.cpp:7745)
      File "ring.pyx", line 506, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6272)
      File "ring.pyx", line 534, in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6044)
    ValueError: The name "t_[y1" is not a valid Python identifier.
**********************************************************************
```




---

archive/issue_comments_063257.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-24T12:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63257",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063258.json:
```json
{
    "body": "Somehow I'm not surprised that somebody used invalid identifiers as variable names ;-)\n\nUpdated patch follows.",
    "created_at": "2011-06-24T12:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63258",
    "user": "https://github.com/vbraun"
}
```

Somehow I'm not surprised that somebody used invalid identifiers as variable names ;-)

Updated patch follows.



---

archive/issue_comments_063259.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-24T13:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63259",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063260.json:
```json
{
    "body": "Replying to [comment:11 vbraun]:\n> Somehow I'm not surprised that somebody used invalid identifiers as variable names ;-)\n\nSo this actually found a bug of sorts - nice.  Though I have to say that trying to go between the Maxima way of all variables automatic and the Sage way of (nearly) none gave the folks who put that file together quite a challenge, so I don't blame them too much.  But the code is not so elegant, in retrospect.\n\nWhat's particularly bizarre about this is that in the old and the new cases, `fast_float` is being passed something with three arguments, so it still behaves properly - even though the third thing is an iterable in both cases!  Probably the \"right\" fix is to just do `'t_'+str(dvar)` for the first dvar only; fast_float just needs something different from the dependent variables.  But I think that would be another ticket, as this doesn't break anything (and the plots still look the same).\n\nAnyway, it fixes the test, doesn't seem to introduce any new bugs.\n\nHowever, the update to allowing whitespace probably still needs work. Maybe we need to special-case the situation where there is only whitespace in the string passed to `var`:\n\n```\nsage: var(' ')\n \nsage: a = var(' ')\nsage: a\n \nsage: type(a)\n<type 'sage.symbolic.expression.Expression'>\n```\n\n\nSorry :(",
    "created_at": "2011-06-24T13:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63260",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:11 vbraun]:
> Somehow I'm not surprised that somebody used invalid identifiers as variable names ;-)

So this actually found a bug of sorts - nice.  Though I have to say that trying to go between the Maxima way of all variables automatic and the Sage way of (nearly) none gave the folks who put that file together quite a challenge, so I don't blame them too much.  But the code is not so elegant, in retrospect.

What's particularly bizarre about this is that in the old and the new cases, `fast_float` is being passed something with three arguments, so it still behaves properly - even though the third thing is an iterable in both cases!  Probably the "right" fix is to just do `'t_'+str(dvar)` for the first dvar only; fast_float just needs something different from the dependent variables.  But I think that would be another ticket, as this doesn't break anything (and the plots still look the same).

Anyway, it fixes the test, doesn't seem to introduce any new bugs.

However, the update to allowing whitespace probably still needs work. Maybe we need to special-case the situation where there is only whitespace in the string passed to `var`:

```
sage: var(' ')
 
sage: a = var(' ')
sage: a
 
sage: type(a)
<type 'sage.symbolic.expression.Expression'>
```


Sorry :(



---

archive/issue_comments_063261.json:
```json
{
    "body": "Oh yes good catch, the elements of the empty set (no variable after stripping whitespace) satisfy every property!\n\nFixed in the updated patch.",
    "created_at": "2011-06-24T14:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63261",
    "user": "https://github.com/vbraun"
}
```

Oh yes good catch, the elements of the empty set (no variable after stripping whitespace) satisfy every property!

Fixed in the updated patch.



---

archive/issue_comments_063262.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-24T14:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63262",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063263.json:
```json
{
    "body": "Updated patch",
    "created_at": "2011-06-24T14:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63263",
    "user": "https://github.com/vbraun"
}
```

Updated patch



---

archive/issue_comments_063264.json:
```json
{
    "body": "Attachment [trac_7496-reviewer.2.patch](tarball://root/attachments/some-uuid/ticket7496/trac_7496-reviewer.2.patch) by @vbraun created at 2011-06-24 15:33:16\n\nUpdated patch",
    "created_at": "2011-06-24T15:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63264",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_7496-reviewer.2.patch](tarball://root/attachments/some-uuid/ticket7496/trac_7496-reviewer.2.patch) by @vbraun created at 2011-06-24 15:33:16

Updated patch



---

archive/issue_comments_063265.json:
```json
{
    "body": "The error message for the \"empty variable\" case changed in my patch, I just updated the reviewer patch to take that into account.",
    "created_at": "2011-06-24T15:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63265",
    "user": "https://github.com/vbraun"
}
```

The error message for the "empty variable" case changed in my patch, I just updated the reviewer patch to take that into account.



---

archive/issue_comments_063266.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-24T19:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63266",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063267.json:
```json
{
    "body": "Okay, I think that this is finally in shape.  Thanks for the back and forth on this.",
    "created_at": "2011-06-24T19:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63267",
    "user": "https://github.com/kcrisman"
}
```

Okay, I think that this is finally in shape.  Thanks for the back and forth on this.



---

archive/issue_events_007725.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-07-22T12:48:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7496#event-7725"
}
```



---

archive/issue_comments_063268.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-22T12:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7496#issuecomment-63268",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
