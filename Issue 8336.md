# Issue 8336: round(x) <> x.round() for x in RealField

archive/issues_008336.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  was jason robertwb ncalexan craigcitro mabshoff\n\nThis is related to #188 and #2899.\n\n```\nsage: R=RealField(150)\nsage: x=R(3493274823748475345934875398475345349.9343498375)\nsage: y=round(x)\nsage: y, type(y)\n(3.49327482375e+36, <type 'sage.rings.real_double.RealDoubleElement'>)\nsage: z=x.round()\nsage: z, type(z)\n(3493274823748475345934875398475345350, <type 'sage.rings.integer.Integer'>)\n```\n\nIf one performs `ZZ(y)` to convert `y` to an integer, one\nhas a huge loss of accuracy.\n\nI see no point of forcing coercion to RDF, which has limited precision and exponent range.\n\nI would expect `round(x)` to return the same value as `z`,\neither as Integer or RealField.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8336\n\n",
    "created_at": "2010-02-23T18:00:50Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "round(x) <> x.round() for x in RealField",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8336",
    "user": "zimmerma"
}
```
Assignee: AlexGhitza

CC:  was jason robertwb ncalexan craigcitro mabshoff

This is related to #188 and #2899.

```
sage: R=RealField(150)
sage: x=R(3493274823748475345934875398475345349.9343498375)
sage: y=round(x)
sage: y, type(y)
(3.49327482375e+36, <type 'sage.rings.real_double.RealDoubleElement'>)
sage: z=x.round()
sage: z, type(z)
(3493274823748475345934875398475345350, <type 'sage.rings.integer.Integer'>)
```

If one performs `ZZ(y)` to convert `y` to an integer, one
has a huge loss of accuracy.

I see no point of forcing coercion to RDF, which has limited precision and exponent range.

I would expect `round(x)` to return the same value as `z`,
either as Integer or RealField.

Issue created by migration from https://trac.sagemath.org/ticket/8336





---

archive/issue_comments_074419.json:
```json
{
    "body": "+1 I was bitten by this myself recently.",
    "created_at": "2010-02-23T20:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74419",
    "user": "robertwb"
}
```

+1 I was bitten by this myself recently.



---

archive/issue_comments_074420.json:
```json
{
    "body": "I removed my name as \"author\" since I only reported that problem.",
    "created_at": "2010-03-13T21:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74420",
    "user": "zimmerma"
}
```

I removed my name as "author" since I only reported that problem.



---

archive/issue_comments_074421.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-11-09T01:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74421",
    "user": "donmorrison"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_074422.json:
```json
{
    "body": "With much help from Robert Bradshaw, I wrote some code for this ticket, that does the rounding, though it leaves trailing zeros in the destination type.  Robert: Is the latter not a separate (display) issue?  You noted off-list that the return type should have the same precision.  If so, I don't think they will uniformly display without treating the issues separately.  (If so, the one issue per ticket rule applies.)  Much thanks.",
    "created_at": "2010-11-09T01:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74422",
    "user": "donmorrison"
}
```

With much help from Robert Bradshaw, I wrote some code for this ticket, that does the rounding, though it leaves trailing zeros in the destination type.  Robert: Is the latter not a separate (display) issue?  You noted off-list that the return type should have the same precision.  If so, I don't think they will uniformly display without treating the issues separately.  (If so, the one issue per ticket rule applies.)  Much thanks.



---

archive/issue_comments_074423.json:
```json
{
    "body": "Changing assignee from AlexGhitza to robertwb.",
    "created_at": "2010-11-09T07:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74423",
    "user": "robertwb"
}
```

Changing assignee from AlexGhitza to robertwb.



---

archive/issue_comments_074424.json:
```json
{
    "body": "Patch? I think \n\nsage: round(2.5)\n2.500000000000\n\nis just fine for elements of RR.",
    "created_at": "2010-11-09T07:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74424",
    "user": "robertwb"
}
```

Patch? I think 

sage: round(2.5)
2.500000000000

is just fine for elements of RR.



---

archive/issue_comments_074425.json:
```json
{
    "body": "Correction: \n\n\n```\nsage: round(2.5)\n3\nsage: round(2.5, ndigits=1)\n2.500000000000\n```\n",
    "created_at": "2010-11-09T07:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74425",
    "user": "robertwb"
}
```

Correction: 


```
sage: round(2.5)
3
sage: round(2.5, ndigits=1)
2.500000000000
```




---

archive/issue_comments_074426.json:
```json
{
    "body": "Replying to [comment:5 robertwb]:\n> Correction: \n> \n> {{{\n> sage: round(2.5)\n> 3\n> sage: round(2.5, ndigits=1)\n> 2.500000000000\n> }}}\n\nit is fine for me that `round(x)` returns a float, however I don't understand why it returns\na float of fixed precision (RDF). It should then be called `RDF_round`. It would be more\nnatural to return a float with the same precision as the input.\n\nPaul",
    "created_at": "2010-11-09T09:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74426",
    "user": "zimmerma"
}
```

Replying to [comment:5 robertwb]:
> Correction: 
> 
> {{{
> sage: round(2.5)
> 3
> sage: round(2.5, ndigits=1)
> 2.500000000000
> }}}

it is fine for me that `round(x)` returns a float, however I don't understand why it returns
a float of fixed precision (RDF). It should then be called `RDF_round`. It would be more
natural to return a float with the same precision as the input.

Paul



---

archive/issue_comments_074427.json:
```json
{
    "body": "I don't think it should return a float of fixed precision, it just so happened that the input was 53 bits. \n\nWhat I want is round(x) to call x.round() and possibly x.round(ndigits=ndigits), if available. Thus\n\n\n```\nsage: L = [RDF(pi), RealField(100)(pi), float(pi)]\nsage: [x.round() for x in L if hasattr(x, 'round')]\n[3, 3]\nsage: [round(x) for x in L]\n[3, 3, 3]\n\nsage: [x.round(ndigits=2) for x in L if hasattr(x, 'round')]\n[3.14, 3.1400000000000000000000000000]\nsage: [round(x, ndigits=2) for x in L]\n[3.14, 3.1400000000000000000000000000, 3.1400000000000001]\nsage: [parent(round(x, ndigits=2)) is parent(x) for x in L]\n[True, True, True]\n```\n\n\nSometimes it seems it'd be quicker to just code this up than keep talking about it :).",
    "created_at": "2010-11-09T21:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74427",
    "user": "robertwb"
}
```

I don't think it should return a float of fixed precision, it just so happened that the input was 53 bits. 

What I want is round(x) to call x.round() and possibly x.round(ndigits=ndigits), if available. Thus


```
sage: L = [RDF(pi), RealField(100)(pi), float(pi)]
sage: [x.round() for x in L if hasattr(x, 'round')]
[3, 3]
sage: [round(x) for x in L]
[3, 3, 3]

sage: [x.round(ndigits=2) for x in L if hasattr(x, 'round')]
[3.14, 3.1400000000000000000000000000]
sage: [round(x, ndigits=2) for x in L]
[3.14, 3.1400000000000000000000000000, 3.1400000000000001]
sage: [parent(round(x, ndigits=2)) is parent(x) for x in L]
[True, True, True]
```


Sometimes it seems it'd be quicker to just code this up than keep talking about it :).



---

archive/issue_comments_074428.json:
```json
{
    "body": "patch for release \"barnacle\" ;)",
    "created_at": "2010-11-09T22:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74428",
    "user": "donmorrison"
}
```

patch for release "barnacle" ;)



---

archive/issue_comments_074429.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-11-09T22:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74429",
    "user": "donmorrison"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_074430.json:
```json
{
    "body": "Attachment [bug8336-almost-a-patch.txt](tarball://root/attachments/some-uuid/ticket8336/bug8336-almost-a-patch.txt) by donmorrison created at 2010-11-09 22:28:25\n\nWhoops, I didn't realize uploading the patch would end my comments. \u00a0I wanted to say, you didn't like that patch Robert. \u00a0What's the next step?",
    "created_at": "2010-11-09T22:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74430",
    "user": "donmorrison"
}
```

Attachment [bug8336-almost-a-patch.txt](tarball://root/attachments/some-uuid/ticket8336/bug8336-almost-a-patch.txt) by donmorrison created at 2010-11-09 22:28:25

Whoops, I didn't realize uploading the patch would end my comments.  I wanted to say, you didn't like that patch Robert.  What's the next step?



---

archive/issue_comments_074431.json:
```json
{
    "body": "> What I want is round(x) to call x.round() and possibly x.round(ndigits=ndigits), if available. \n\nthis would be ok for me.\n\nPaul\n\nPS: donmorrison, your patch is missing some examples checking the new behaviour.",
    "created_at": "2010-11-10T08:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74431",
    "user": "zimmerma"
}
```

> What I want is round(x) to call x.round() and possibly x.round(ndigits=ndigits), if available. 

this would be ok for me.

Paul

PS: donmorrison, your patch is missing some examples checking the new behaviour.



---

archive/issue_comments_074432.json:
```json
{
    "body": "Thanks Paul.  The patch I sent is incomplete because it breaks doctests for the following:\n\n./sage -t  -force_lib \"devel/sage/doc/en/thematic_tutorials/linear_programming.rst\";\n\n./sage -t  -force_lib \"devel/sage/sage/misc/functional.py\";\n\n./sage -t  -force_lib \"devel/sage/sage/numerical/mip.pyx\";",
    "created_at": "2010-11-10T14:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74432",
    "user": "donmorrison"
}
```

Thanks Paul.  The patch I sent is incomplete because it breaks doctests for the following:

./sage -t  -force_lib "devel/sage/doc/en/thematic_tutorials/linear_programming.rst";

./sage -t  -force_lib "devel/sage/sage/misc/functional.py";

./sage -t  -force_lib "devel/sage/sage/numerical/mip.pyx";



---

archive/issue_comments_074433.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-12-18T15:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74433",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_074434.json:
```json
{
    "body": "I'm going to close this as invalid now since we have the following behavior:\n\n\n```\nsage: R = RealField(150)\nsage: x = R(3493274823748475345934875398475345349.9343498375)\nsage: y = round(x)\nsage: y, type(y)\n(3493274823748475345934875398475345350, <type 'sage.rings.integer.Integer'>)\nsage: z = x.round()\nsage: z, type(z)\n(3493274823748475345934875398475345350, <type 'sage.rings.integer.Integer'>)\n```\n",
    "created_at": "2011-12-18T15:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74434",
    "user": "mhansen"
}
```

I'm going to close this as invalid now since we have the following behavior:


```
sage: R = RealField(150)
sage: x = R(3493274823748475345934875398475345349.9343498375)
sage: y = round(x)
sage: y, type(y)
(3493274823748475345934875398475345350, <type 'sage.rings.integer.Integer'>)
sage: z = x.round()
sage: z, type(z)
(3493274823748475345934875398475345350, <type 'sage.rings.integer.Integer'>)
```




---

archive/issue_comments_074435.json:
```json
{
    "body": "I agree to close that ticket. Just for the record, it would be nice to track down which patch did\nfix that issue.\n\nPaul",
    "created_at": "2011-12-19T11:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8336",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8336#issuecomment-74435",
    "user": "zimmerma"
}
```

I agree to close that ticket. Just for the record, it would be nice to track down which patch did
fix that issue.

Paul
