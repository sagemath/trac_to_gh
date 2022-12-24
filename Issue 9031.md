# Issue 9031: algebraic_dependency with algorithm=fpLLL

archive/issues_009031.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe algebraic_dependency function currently calls Pari/GP.\nFor big problems fpLLL should be faster, thus there should be\nan option to call fpLLL instead.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9031\n\n",
    "created_at": "2010-05-24T07:53:30Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "algebraic_dependency with algorithm=fpLLL",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9031",
    "user": "@zimmermann6"
}
```
Assignee: @aghitza

The algebraic_dependency function currently calls Pari/GP.
For big problems fpLLL should be faster, thus there should be
an option to call fpLLL instead.

Issue created by migration from https://trac.sagemath.org/ticket/9031





---

archive/issue_comments_083580.json:
```json
{
    "body": "Sage's command does call fpLLL.  This ticket should be closed. \n\nType \n\n```\nsage: algdep??\n```\n\nto see...",
    "created_at": "2014-11-06T23:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9031#issuecomment-83580",
    "user": "@williamstein"
}
```

Sage's command does call fpLLL.  This ticket should be closed. 

Type 

```
sage: algdep??
```

to see...



---

archive/issue_comments_083581.json:
```json
{
    "body": ">  Sage's command does call fpLLL. This ticket should be closed. \n\nok, but the documentation should be fixed:\n\n```\n   Note that \"algebraic_dependency\" is a synonym for \"algdep\".\nsage: a=sqrt(2)+sqrt(3);algebraic_dependency(a,4)\n---------------------------------------------------------------------------\nNameError                                Traceback (most recent call last)\n<ipython-input-10-0409cbaa7642> in <module>()\n----> 1 a=sqrt(Integer(2))+sqrt(Integer(3));algebraic_dependency(a,Integer(4))\n\nNameError: name 'algebraic_dependency' is not defined\n```\n\nand:\n\n```\n   You can specify the number of known bits or digits of z with\n   \"known_bits=k\" or \"known_digits=k\". PARI is then told to compute\n   the result using 0.8k of these bits/digits.\n```\n\nIf fpLLL is used now, `PARI` should be removed or replaced here.\n\nPaul",
    "created_at": "2014-11-07T06:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9031#issuecomment-83581",
    "user": "@zimmermann6"
}
```

>  Sage's command does call fpLLL. This ticket should be closed. 

ok, but the documentation should be fixed:

```
   Note that "algebraic_dependency" is a synonym for "algdep".
sage: a=sqrt(2)+sqrt(3);algebraic_dependency(a,4)
---------------------------------------------------------------------------
NameError                                Traceback (most recent call last)
<ipython-input-10-0409cbaa7642> in <module>()
----> 1 a=sqrt(Integer(2))+sqrt(Integer(3));algebraic_dependency(a,Integer(4))

NameError: name 'algebraic_dependency' is not defined
```

and:

```
   You can specify the number of known bits or digits of z with
   "known_bits=k" or "known_digits=k". PARI is then told to compute
   the result using 0.8k of these bits/digits.
```

If fpLLL is used now, `PARI` should be removed or replaced here.

Paul



---

archive/issue_comments_083582.json:
```json
{
    "body": "Early today, I coincidentally opened a ticket about algebraic_dependency vanishing: http://trac.sagemath.org/ticket/17302",
    "created_at": "2014-11-07T06:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9031#issuecomment-83582",
    "user": "@williamstein"
}
```

Early today, I coincidentally opened a ticket about algebraic_dependency vanishing: http://trac.sagemath.org/ticket/17302



---

archive/issue_comments_083583.json:
```json
{
    "body": "ok, then I agree we should close this one. I will add the `known_bits` issue to the other ticket. What should one do to close?\n\nPaul",
    "created_at": "2014-11-07T07:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9031#issuecomment-83583",
    "user": "@zimmermann6"
}
```

ok, then I agree we should close this one. I will add the `known_bits` issue to the other ticket. What should one do to close?

Paul



---

archive/issue_comments_083584.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-11-07T14:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9031#issuecomment-83584",
    "user": "@vbraun"
}
```

Resolution: invalid



---

archive/issue_comments_083585.json:
```json
{
    "body": "You are supposed to set milestone to duplicate/invalid/wontfix and then positive review...",
    "created_at": "2014-11-07T14:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9031#issuecomment-83585",
    "user": "@vbraun"
}
```

You are supposed to set milestone to duplicate/invalid/wontfix and then positive review...
