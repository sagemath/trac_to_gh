# Issue 2079: /= does not work for univariate polynomials

archive/issues_002079.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @robertwb\n\n\n```\nsage: R.<x> = QQ[]\nsage: a = 2*x^2+2; a\n2*x^2 + 2\nsage: a /= 2\nsage: a\n2*x^2 + 2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2079\n\n",
    "created_at": "2008-02-07T05:24:30Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "/= does not work for univariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2079",
    "user": "https://github.com/mwhansen"
}
```
Assignee: somebody

CC:  @robertwb


```
sage: R.<x> = QQ[]
sage: a = 2*x^2+2; a
2*x^2 + 2
sage: a /= 2
sage: a
2*x^2 + 2
```


Issue created by migration from https://trac.sagemath.org/ticket/2079





---

archive/issue_comments_013420.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-02-07T10:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13420",
    "user": "https://github.com/mwhansen"
}
```

Changing priority from major to critical.



---

archive/issue_comments_013421.json:
```json
{
    "body": "Lines 938-946 of polynomial_element.pyx seem to be at fault.  This might help:\n\n\n```\nsage: R.<x> = QQ[]\nsage: a = 2*x^2+2; a\n2*x^2 + 2\nsage: a/=2; a\n2*x^2 + 2\nsage: a/=Integer(2); a\n2*x^2 + 2\nsage: a/=QQ(2); a\nx^2 + 1\n```\n\n\nI note the comment there:\n\n```\n        Be careful about coercions (this used to be broken):\n            sage: R.<x> = ZZ['x']\n            sage: f = x / Mod(2,5); f\n            3*x\n            sage: f.parent()\n            Univariate Polynomial Ring in x over Ring of integers modulo 5\n```\n\n\nPersonally I would prefer that to be broken than to allow division of a ZZ polynomial by an integer mod 5.  I think the coercion model which says \"if there is anything conceivable which could be done to make sense of the input, the do it, even if it makes little or no mathematical sense\", has something wrong with it.\n\nBut someone with more knowledge of the coercion code will have to deal with this one, which is certainly very serious.",
    "created_at": "2008-02-18T11:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13421",
    "user": "https://github.com/JohnCremona"
}
```

Lines 938-946 of polynomial_element.pyx seem to be at fault.  This might help:


```
sage: R.<x> = QQ[]
sage: a = 2*x^2+2; a
2*x^2 + 2
sage: a/=2; a
2*x^2 + 2
sage: a/=Integer(2); a
2*x^2 + 2
sage: a/=QQ(2); a
x^2 + 1
```


I note the comment there:

```
        Be careful about coercions (this used to be broken):
            sage: R.<x> = ZZ['x']
            sage: f = x / Mod(2,5); f
            3*x
            sage: f.parent()
            Univariate Polynomial Ring in x over Ring of integers modulo 5
```


Personally I would prefer that to be broken than to allow division of a ZZ polynomial by an integer mod 5.  I think the coercion model which says "if there is anything conceivable which could be done to make sense of the input, the do it, even if it makes little or no mathematical sense", has something wrong with it.

But someone with more knowledge of the coercion code will have to deal with this one, which is certainly very serious.



---

archive/issue_comments_013422.json:
```json
{
    "body": "> I think the coercion model which says \"if there is anything \n> conceivable which could be done to make sense of the input, \n> the do it, even if it makes little or no mathematical sense\",\n> has something wrong with it.\n\nThat (=PARI, Mathematica, etc) is definitely *not* supposed \nto be Sage's coercion model.\n\nThat said, dividing a ZZ poly by an integer mod 5 does make perfectz\nsense in the coercion model.  There is a natural map from ZZ to ZZ/5ZZ,\nhence a natural map `ZZ[x] --> (ZZ/5ZZ)[x]`.  The poly is mapped\nto (ZZ/5ZZ)[x] and then the division takes place.  It is well defined,\nnatural, canonical, and certainly not ad hoc.\n\nWilliam",
    "created_at": "2008-02-19T00:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13422",
    "user": "https://github.com/williamstein"
}
```

> I think the coercion model which says "if there is anything 
> conceivable which could be done to make sense of the input, 
> the do it, even if it makes little or no mathematical sense",
> has something wrong with it.

That (=PARI, Mathematica, etc) is definitely *not* supposed 
to be Sage's coercion model.

That said, dividing a ZZ poly by an integer mod 5 does make perfectz
sense in the coercion model.  There is a natural map from ZZ to ZZ/5ZZ,
hence a natural map `ZZ[x] --> (ZZ/5ZZ)[x]`.  The poly is mapped
to (ZZ/5ZZ)[x] and then the division takes place.  It is well defined,
natural, canonical, and certainly not ad hoc.

William



---

archive/issue_comments_013423.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-02-19T00:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13423",
    "user": "https://github.com/williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_013424.json:
```json
{
    "body": "This is a really really serious bug somewhere in the actions part of the coercion model.  I've promoted it to a blocker.",
    "created_at": "2008-02-19T00:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13424",
    "user": "https://github.com/williamstein"
}
```

This is a really really serious bug somewhere in the actions part of the coercion model.  I've promoted it to a blocker.



---

archive/issue_comments_013425.json:
```json
{
    "body": "The problem is around line 869 of coerce.pyx, where if we put:\n\n```\n        if self.connecting is not None:\n            print \"g before = \", g\n            g = self.connecting._call_c(g)\n            print \"g after = \", g\n```\n\n\nthen run the sample code:\n\n```\nsage: R.<x> = QQ[]; a = 2*x^2+2\nsage: a /= 2\ng before =  1/2\ng after =  1\n3 2*x^2 + 2 1\n```\n\n\nyou see that self.connecting._call_c is somehow replacing 1/2 by 1.  Not good.",
    "created_at": "2008-02-19T01:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13425",
    "user": "https://github.com/williamstein"
}
```

The problem is around line 869 of coerce.pyx, where if we put:

```
        if self.connecting is not None:
            print "g before = ", g
            g = self.connecting._call_c(g)
            print "g after = ", g
```


then run the sample code:

```
sage: R.<x> = QQ[]; a = 2*x^2+2
sage: a /= 2
g before =  1/2
g after =  1
3 2*x^2 + 2 1
```


you see that self.connecting._call_c is somehow replacing 1/2 by 1.  Not good.



---

archive/issue_comments_013426.json:
```json
{
    "body": "I'm about to attach a patch that adds several functions related to making the coercion model a little more user friendly (for debugging), fixes/adds more documentation, and MOST IMPORTANTLY, re-enables some disabled type checking that lead to some potentially seriously bugs in the basic arithmetic in Sage.   I also put some commented out code that doesn't look right to me that would fix the above problem.  I hope that Robert will: \n\n1. look at the above patch;\n \n2. Make some changes to genuinely fixes the action.pyx file;\n\n3. Make a patch over the above patch that incorporates those fixes, and probably disables the type checking that I enabled. \n\nAnyway, again, the core root cause of this problem is that InverseAction in action.pyx is not implemented correctly and/or makes invalid assumptions, and ends up calling this bit of code in rational.pyx with an x that is of type Rational:\n\n\n```\n    cdef Element _call_c_impl(self, Element x):\n        cdef Rational rat\n        rat = <Rational> PY_NEW(Rational)\n        mpq_set_z(rat.value, (<integer.Integer>x).value)\n        return rat\n```\n\n\nThe result is wrong answers. \n\nWilliam",
    "created_at": "2008-02-19T01:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13426",
    "user": "https://github.com/williamstein"
}
```

I'm about to attach a patch that adds several functions related to making the coercion model a little more user friendly (for debugging), fixes/adds more documentation, and MOST IMPORTANTLY, re-enables some disabled type checking that lead to some potentially seriously bugs in the basic arithmetic in Sage.   I also put some commented out code that doesn't look right to me that would fix the above problem.  I hope that Robert will: 

1. look at the above patch;
 
2. Make some changes to genuinely fixes the action.pyx file;

3. Make a patch over the above patch that incorporates those fixes, and probably disables the type checking that I enabled. 

Anyway, again, the core root cause of this problem is that InverseAction in action.pyx is not implemented correctly and/or makes invalid assumptions, and ends up calling this bit of code in rational.pyx with an x that is of type Rational:


```
    cdef Element _call_c_impl(self, Element x):
        cdef Rational rat
        rat = <Rational> PY_NEW(Rational)
        mpq_set_z(rat.value, (<integer.Integer>x).value)
        return rat
```


The result is wrong answers. 

William



---

archive/issue_comments_013427.json:
```json
{
    "body": "fixes the problem, but needs an additional patch from Robert.",
    "created_at": "2008-02-19T01:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13427",
    "user": "https://github.com/williamstein"
}
```

fixes the problem, but needs an additional patch from Robert.



---

archive/issue_comments_013428.json:
```json
{
    "body": "Attachment [sage-2079.patch](tarball://root/attachments/some-uuid/ticket2079/sage-2079.patch) by @robertwb created at 2008-02-19 04:09:48\n\nI figured out what the issue is. I will post a fix tonight (after making sure it breaks nothing else, and adding more doctests/consistency checks.)",
    "created_at": "2008-02-19T04:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13428",
    "user": "https://github.com/robertwb"
}
```

Attachment [sage-2079.patch](tarball://root/attachments/some-uuid/ticket2079/sage-2079.patch) by @robertwb created at 2008-02-19 04:09:48

I figured out what the issue is. I will post a fix tonight (after making sure it breaks nothing else, and adding more doctests/consistency checks.)



---

archive/issue_comments_013429.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> > I think the coercion model which says \"if there is anything \n> > conceivable which could be done to make sense of the input, \n> > the do it, even if it makes little or no mathematical sense\",\n> > has something wrong with it.\n> \n> That (=PARI, Mathematica, etc) is definitely *not* supposed \n> to be Sage's coercion model.\n> \n> That said, dividing a ZZ poly by an integer mod 5 does make perfectz\n> sense in the coercion model.  There is a natural map from ZZ to ZZ/5ZZ,\n> hence a natural map `ZZ[x] --> (ZZ/5ZZ)[x]`.  The poly is mapped\n> to (ZZ/5ZZ)[x] and then the division takes place.  It is well defined,\n> natural, canonical, and certainly not ad hoc.\n> \n> William\n> \n\n OK, I admit that this does make sense.  Just after posting that I realised that for many years,  in pari, if I ever wanted to input a polynomial mod 5 I would type something like \n\n```\nf = (x^2+1) * Mod(1,5)\n```\n\n which -- apart from being a multiplication and not a division -- shows that I do know that this makes sense.\n\n Trying to understand what was going wrong in this case got me into very deep water in the coercion mode;  I look forward to seeing the patches which make that easier to understand what is going on.  The notes at http://wiki.sagemath.org/days7/coercion will be very helpful.  ARe they a description of what is currently in place, or a wish list for what should be, or somewhere between the two?",
    "created_at": "2008-02-19T09:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13429",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 was]:
> > I think the coercion model which says "if there is anything 
> > conceivable which could be done to make sense of the input, 
> > the do it, even if it makes little or no mathematical sense",
> > has something wrong with it.
> 
> That (=PARI, Mathematica, etc) is definitely *not* supposed 
> to be Sage's coercion model.
> 
> That said, dividing a ZZ poly by an integer mod 5 does make perfectz
> sense in the coercion model.  There is a natural map from ZZ to ZZ/5ZZ,
> hence a natural map `ZZ[x] --> (ZZ/5ZZ)[x]`.  The poly is mapped
> to (ZZ/5ZZ)[x] and then the division takes place.  It is well defined,
> natural, canonical, and certainly not ad hoc.
> 
> William
> 

 OK, I admit that this does make sense.  Just after posting that I realised that for many years,  in pari, if I ever wanted to input a polynomial mod 5 I would type something like 

```
f = (x^2+1) * Mod(1,5)
```

 which -- apart from being a multiplication and not a division -- shows that I do know that this makes sense.

 Trying to understand what was going wrong in this case got me into very deep water in the coercion mode;  I look forward to seeing the patches which make that easier to understand what is going on.  The notes at http://wiki.sagemath.org/days7/coercion will be very helpful.  ARe they a description of what is currently in place, or a wish list for what should be, or somewhere between the two?



---

archive/issue_comments_013430.json:
```json
{
    "body": "Attachment [2079-coerce.patch](tarball://root/attachments/some-uuid/ticket2079/2079-coerce.patch) by @robertwb created at 2008-02-19 10:26:36",
    "created_at": "2008-02-19T10:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13430",
    "user": "https://github.com/robertwb"
}
```

Attachment [2079-coerce.patch](tarball://root/attachments/some-uuid/ticket2079/2079-coerce.patch) by @robertwb created at 2008-02-19 10:26:36



---

archive/issue_comments_013431.json:
```json
{
    "body": "Attachment [2079-coerce3.patch](tarball://root/attachments/some-uuid/ticket2079/2079-coerce3.patch) by @robertwb created at 2008-02-19 10:28:14",
    "created_at": "2008-02-19T10:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13431",
    "user": "https://github.com/robertwb"
}
```

Attachment [2079-coerce3.patch](tarball://root/attachments/some-uuid/ticket2079/2079-coerce3.patch) by @robertwb created at 2008-02-19 10:28:14



---

archive/issue_comments_013432.json:
```json
{
    "body": "This code now works correctly instead of giving invalid results (really bad) or throwing an error (undesirable). I have also added code to verify any actions created in the coercion model conform to the expected specifications, to forestall something like this from coming up again (and had to fix things in a couple of other places, though nothing else that gave erroneous results). \n\nIn response to the question above, the Sage Days 7 wiki page is a wishlist and guide for how things should and will be, some of which has already been implemented in a (still very broken) branch. Most of what is there concerns how the user/developer will interact with the coercion model, rather than how the model itself works.",
    "created_at": "2008-02-19T10:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13432",
    "user": "https://github.com/robertwb"
}
```

This code now works correctly instead of giving invalid results (really bad) or throwing an error (undesirable). I have also added code to verify any actions created in the coercion model conform to the expected specifications, to forestall something like this from coming up again (and had to fix things in a couple of other places, though nothing else that gave erroneous results). 

In response to the question above, the Sage Days 7 wiki page is a wishlist and guide for how things should and will be, some of which has already been implemented in a (still very broken) branch. Most of what is there concerns how the user/developer will interact with the coercion model, rather than how the model itself works.



---

archive/issue_comments_013433.json:
```json
{
    "body": "REFEREE REPORT: \n\nI've read through and tested the code and it (1) looks good, and (2) fixes a critical bug in basic arithmetic in Sage that would lead to basic wrong answers.  The code looks good and adds a lot of nice documentation.  Thus this should definitely be applied!\n\nI really think documenting the heck out of all the coercion model related files should be the absolute number one priority in all the coercion model stuff you guys are doing.  If that code were documented and the coercion model itself were way friendly wrt introspection (i.e., understanding it interactively from the command line and/or graphically), then people would be VASTLY more likely to dive in and help with revamping things according to your vision.  At least, I would be.   The value of knowing you can dive into the core and understand it yourself when the going gets rough is not to be underestimated, and is why we all like open source so much.",
    "created_at": "2008-02-19T14:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13433",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT: 

I've read through and tested the code and it (1) looks good, and (2) fixes a critical bug in basic arithmetic in Sage that would lead to basic wrong answers.  The code looks good and adds a lot of nice documentation.  Thus this should definitely be applied!

I really think documenting the heck out of all the coercion model related files should be the absolute number one priority in all the coercion model stuff you guys are doing.  If that code were documented and the coercion model itself were way friendly wrt introspection (i.e., understanding it interactively from the command line and/or graphically), then people would be VASTLY more likely to dive in and help with revamping things according to your vision.  At least, I would be.   The value of knowing you can dive into the core and understand it yourself when the going gets rough is not to be underestimated, and is why we all like open source so much.



---

archive/issue_comments_013434.json:
```json
{
    "body": "One more comment: ALL the patches attached to this ticket should be applied in order.",
    "created_at": "2008-02-19T14:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13434",
    "user": "https://github.com/williamstein"
}
```

One more comment: ALL the patches attached to this ticket should be applied in order.



---

archive/issue_comments_013435.json:
```json
{
    "body": "All four patches merge in Sage 2.10.2.alpha1",
    "created_at": "2008-02-19T14:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13435",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

All four patches merge in Sage 2.10.2.alpha1



---

archive/issue_events_002240.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-19T14:56:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2079#event-2240"
}
```



---

archive/issue_comments_013436.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-19T14:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2079#issuecomment-13436",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
