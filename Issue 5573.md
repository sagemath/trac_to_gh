# Issue 5573: [with patch; positive review] genus2reduction interface has at least two problems

archive/issues_005573.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nOn Thu, Mar 19, 2009 at 6:14 PM, ARMAND BRUMER wrote:\n> Hi William,\n>\n> This is my first attempt to use sage. I have OSX 10.4.11 \n> and just downloaded it.\n>\n> I wanted to use liu's program. After trying out your \n> examples and getting the same result, I tried the example \n> I was curious about and here is the output. Can you do better. \n> Did I screw up?\n>\n> Thanks,\n> armand\n```\nThe code:\n\n```\nsage: genus2reduction(x^3 + x^2 + x,-2*x^5 + 3*x^4 - x^3 - x^2 - 6*x - 2)\n--------------------------------------------------------------------------- \nValueError                                \nTraceback (most recent call last)\n```\nWilliam replies:  You have found a bug in Sage.    When I try the above by directly using Liu's program (note that i have to remove the spaces in the polynomials and use an explanation point to run the program), I get the following problem:\n\n```\nsage: !genus2reduction\nenter Q(x) : x^3+x^2+x        \nenter P(x) : -2*x^5+3*x^4-x^3-x^2-6*x-2\n \nfactorization CPU time = 5\na minimal equation over Z[1/2] is : \ny^2 = x^6+18*x^3+36*x^2-27\n \nfactorization of the minimal (away from 2) discriminant : \n[2,1;3,15;53,1]\n \np=2\n(potential) stable reduction :  (II), j=1\nreduction at p : [I{1-0-0}] page 170, (1), f=1\np=3\n(potential) stable reduction :  (I)\nreduction at p :   ***   expected character: ',' instead of: mod(y,y^2-3)\n```\nI don't know if this ever worked, but I bet it did, and PARI changed from 2004 or whatever, until now, and we just didn't pick up the change because we didn't test genus2reduction enough.  \n\n2. A second problem is that if genus2reduction works once, then fails, then it fails to work again:\n\n```\nsage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)\nsage: R.conductor\n1416875\nsage: R = genus2reduction(x^3 + x^2 + x,-2*x^5 + 3*x^4 - x^3 - x^2 - 6*x - 2)\nTraceback (most recent call last):\nValueError: error in input; possibly singular curve? \n(Q=x^3 + x^2 + x, P=-2*x^5 + 3*x^4 - x^3 - x^2 - 6*x - 2)\nsage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)  # just worked above\nTraceback (most recent call last):\n...\nValueError: error in input; possibly singular curve? \n(Q=x^3 - 2*x^2 - 2*x + 1, P=-5*x^5)\n```\n\nWhen we fix this, we will of course have to write code to run through random curves and verify that genus2reduction works sensibly on millions of inputs.\n\nLiu's program genus2reduction, included with Sage, is a C program that is written to use the Pari C library. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5573\n\n",
    "closed_at": "2009-04-06T05:47:27Z",
    "created_at": "2009-03-20T03:54:25Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch; positive review] genus2reduction interface has at least two problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5573",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
On Thu, Mar 19, 2009 at 6:14 PM, ARMAND BRUMER wrote:
> Hi William,
>
> This is my first attempt to use sage. I have OSX 10.4.11 
> and just downloaded it.
>
> I wanted to use liu's program. After trying out your 
> examples and getting the same result, I tried the example 
> I was curious about and here is the output. Can you do better. 
> Did I screw up?
>
> Thanks,
> armand
```
The code:

```
sage: genus2reduction(x^3 + x^2 + x,-2*x^5 + 3*x^4 - x^3 - x^2 - 6*x - 2)
--------------------------------------------------------------------------- 
ValueError                                
Traceback (most recent call last)
```
William replies:  You have found a bug in Sage.    When I try the above by directly using Liu's program (note that i have to remove the spaces in the polynomials and use an explanation point to run the program), I get the following problem:

```
sage: !genus2reduction
enter Q(x) : x^3+x^2+x        
enter P(x) : -2*x^5+3*x^4-x^3-x^2-6*x-2
 
factorization CPU time = 5
a minimal equation over Z[1/2] is : 
y^2 = x^6+18*x^3+36*x^2-27
 
factorization of the minimal (away from 2) discriminant : 
[2,1;3,15;53,1]
 
p=2
(potential) stable reduction :  (II), j=1
reduction at p : [I{1-0-0}] page 170, (1), f=1
p=3
(potential) stable reduction :  (I)
reduction at p :   ***   expected character: ',' instead of: mod(y,y^2-3)
```
I don't know if this ever worked, but I bet it did, and PARI changed from 2004 or whatever, until now, and we just didn't pick up the change because we didn't test genus2reduction enough.  

2. A second problem is that if genus2reduction works once, then fails, then it fails to work again:

```
sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)
sage: R.conductor
1416875
sage: R = genus2reduction(x^3 + x^2 + x,-2*x^5 + 3*x^4 - x^3 - x^2 - 6*x - 2)
Traceback (most recent call last):
ValueError: error in input; possibly singular curve? 
(Q=x^3 + x^2 + x, P=-2*x^5 + 3*x^4 - x^3 - x^2 - 6*x - 2)
sage: R = genus2reduction(x^3 - 2*x^2 - 2*x + 1, -5*x^5)  # just worked above
Traceback (most recent call last):
...
ValueError: error in input; possibly singular curve? 
(Q=x^3 - 2*x^2 - 2*x + 1, P=-5*x^5)
```

When we fix this, we will of course have to write code to run through random curves and verify that genus2reduction works sensibly on millions of inputs.

Liu's program genus2reduction, included with Sage, is a C program that is written to use the Pari C library. 


Issue created by migration from https://trac.sagemath.org/ticket/5573





---

archive/issue_comments_043357.json:
```json
{
    "body": "Attachment [trac_5573.patch](tarball://root/attachments/some-uuid/ticket5573/trac_5573.patch) by @williamstein created at 2009-04-05 22:30:54\n\nNew spkg here:\n\nhttp://sage.math.washington.edu/home/wstein/patches/genus2reduction-0.3.p5.spkg",
    "created_at": "2009-04-05T22:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5573#issuecomment-43357",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5573.patch](tarball://root/attachments/some-uuid/ticket5573/trac_5573.patch) by @williamstein created at 2009-04-05 22:30:54

New spkg here:

http://sage.math.washington.edu/home/wstein/patches/genus2reduction-0.3.p5.spkg



---

archive/issue_comments_043358.json:
```json
{
    "body": "```\n Basically you should just do (make sure lines don't break when the shouldn't):\n\n$ sage -f http://sage.math.washington.edu/home/wstein/patches/genus2reduction-0.3.p5.spkg \n\n$ sage\n...\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/5573/trac_5573.patch')\nsage: quit\n\n$ sage -br\n...\n```",
    "created_at": "2009-04-05T22:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5573#issuecomment-43358",
    "user": "https://github.com/williamstein"
}
```

```
 Basically you should just do (make sure lines don't break when the shouldn't):

$ sage -f http://sage.math.washington.edu/home/wstein/patches/genus2reduction-0.3.p5.spkg 

$ sage
...
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/5573/trac_5573.patch')
sage: quit

$ sage -br
...
```



---

archive/issue_comments_043359.json:
```json
{
    "body": "Patch looks good, I need to have the changes in the spkg explained to me to review this :). William hinted about a change in the pari library.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T22:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5573#issuecomment-43359",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good, I need to have the changes in the spkg explained to me to review this :). William hinted about a change in the pari library.

Cheers,

Michael



---

archive/issue_comments_043360.json:
```json
{
    "body": "Spkg and patch look good. Positive review. William did explain the mod/Mod change that fixed the issue in the spkg.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T05:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5573#issuecomment-43360",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg and patch look good. Positive review. William did explain the mod/Mod change that fixed the issue in the spkg.

Cheers,

Michael



---

archive/issue_comments_043361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-06T05:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5573#issuecomment-43361",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043362.json:
```json
{
    "body": "Reviewed in Sage 3.4.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T05:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5573#issuecomment-43362",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Reviewed in Sage 3.4.1.rc1.

Cheers,

Michael



---

archive/issue_events_013118.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-06T05:47:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5573",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5573#event-13118"
}
```
