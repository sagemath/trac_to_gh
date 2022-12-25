# Issue 8896: 0.0000000000000000000000000000 is parsed completely differently than 1.0000000000000000000000000000 for no good reason

archive/issues_008896.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @jasongrout\n\nKeywords: sd32\n\nIn Sage 0.0 and 0.00000000000000000000000000000000000000 denote exactly the same thing (a zero with the same precision).  However, that 1.0 and 1.00000000000000000000000000000000000000 are different in Sage:\n\n```\nsage: 0.0\n0.000000000000000\nsage: 0.00000000000000000000000000000000000000\n0.000000000000000\nsage: parent(0.00000000000000000000000000000000000000)\nReal Field with 53 bits of precision\nsage: 1.00000000000000000000000000000000000000\n1.0000000000000000000000000000000000000\nsage: 1.0\n1.00000000000000\nsage: parent(1.00000000000000000000000000000000000000)\nReal Field with 130 bits of precision\nsage: parent(1.0)\nReal Field with 53 bits of precision\n```\n\nSome people consider the above inconsistency a bug.\nSee the discussion below and at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/73d513e2c55d4601).\n\nApply [attachment:8896-rebased.patch]\n\nIssue created by migration from https://trac.sagemath.org/ticket/8896\n\n",
    "created_at": "2010-05-05T20:17:53Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-pending",
    "title": "0.0000000000000000000000000000 is parsed completely differently than 1.0000000000000000000000000000 for no good reason",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8896",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza

CC:  @jasongrout

Keywords: sd32

In Sage 0.0 and 0.00000000000000000000000000000000000000 denote exactly the same thing (a zero with the same precision).  However, that 1.0 and 1.00000000000000000000000000000000000000 are different in Sage:

```
sage: 0.0
0.000000000000000
sage: 0.00000000000000000000000000000000000000
0.000000000000000
sage: parent(0.00000000000000000000000000000000000000)
Real Field with 53 bits of precision
sage: 1.00000000000000000000000000000000000000
1.0000000000000000000000000000000000000
sage: 1.0
1.00000000000000
sage: parent(1.00000000000000000000000000000000000000)
Real Field with 130 bits of precision
sage: parent(1.0)
Real Field with 53 bits of precision
```

Some people consider the above inconsistency a bug.
See the discussion below and at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/73d513e2c55d4601).

Apply [attachment:8896-rebased.patch]

Issue created by migration from https://trac.sagemath.org/ticket/8896





---

archive/issue_comments_081653.json:
```json
{
    "body": "This is because 0.00000000000000000000000000000000005 is not considered to have \"high precision.\" We should special-case 0.",
    "created_at": "2010-05-05T22:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81653",
    "user": "https://github.com/robertwb"
}
```

This is because 0.00000000000000000000000000000000005 is not considered to have "high precision." We should special-case 0.



---

archive/issue_comments_081654.json:
```json
{
    "body": "Btw, Sage does not distinguish +0.0 and -0.0 (and 0.0).\n\nNice how trac interprets long decimal fractions of floats. :D",
    "created_at": "2010-05-06T01:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81654",
    "user": "https://github.com/nexttime"
}
```

Btw, Sage does not distinguish +0.0 and -0.0 (and 0.0).

Nice how trac interprets long decimal fractions of floats. :D



---

archive/issue_comments_081655.json:
```json
{
    "body": "Attachment [8896-highprec-zero.patch](tarball://root/attachments/some-uuid/ticket8896/8896-highprec-zero.patch) by @robertwb created at 2010-05-15 22:36:34",
    "created_at": "2010-05-15T22:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81655",
    "user": "https://github.com/robertwb"
}
```

Attachment [8896-highprec-zero.patch](tarball://root/attachments/some-uuid/ticket8896/8896-highprec-zero.patch) by @robertwb created at 2010-05-15 22:36:34



---

archive/issue_comments_081656.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-15T22:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81656",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081657.json:
```json
{
    "body": "Looks okay in general, but the last block \n\n```\nelse: \n        # Must be 0.00000000000000...0 \n        sigfigs = len(mantissa) \n```\nneeds to be indented, n'est pas?\n\nIn the tests, there should be (brief) words to the effect that the first two have the default minimum precision and that is what is being tested for, while in the new tests we are testing for getting high precision.",
    "created_at": "2010-05-26T18:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81657",
    "user": "https://github.com/kcrisman"
}
```

Looks okay in general, but the last block 

```
else: 
        # Must be 0.00000000000000...0 
        sigfigs = len(mantissa) 
```
needs to be indented, n'est pas?

In the tests, there should be (brief) words to the effect that the first two have the default minimum precision and that is what is being tested for, while in the new tests we are testing for getting high precision.



---

archive/issue_comments_081658.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-26T18:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81658",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081659.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> Looks okay in general, but the last block \n> \n> ```\n> else: \n>         # Must be 0.00000000000000...0 \n>         sigfigs = len(mantissa) \n> ```\n> needs to be indented, n'est pas?\n\n\nNo, the `else` belongs to the `for` statement.\nBut currently, *leading* zeros contribute to the precision, too: :)\n\n```\nsage: RealNumber(0.000000000000000000).prec()\n67\nsage: RealNumber(00.000000000000000000).prec()\n70\nsage: RealNumber(.000000000000000000).prec()\n64\n```\nI'm not sure if this is intentional, it's at least uncommon.\n(And a leading `+` also increases the precision.)\n\nIt looks as if a decimal point is counted as a significant digit.\n\nAnd, sorry, the code is extremely ugly (not due to the patch) and inefficient.\nExamples and parameter description can be improved as well.\n\nI'm not quite sure what kind of strings actually get in (i.e., where/if illegal syntax is catched, it seems all is left to `RealNumber._set()` if not already handled by the parser), this should perhaps be documented, too.",
    "created_at": "2010-05-27T13:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81659",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:5 kcrisman]:
> Looks okay in general, but the last block 
> 
> ```
> else: 
>         # Must be 0.00000000000000...0 
>         sigfigs = len(mantissa) 
> ```
> needs to be indented, n'est pas?


No, the `else` belongs to the `for` statement.
But currently, *leading* zeros contribute to the precision, too: :)

```
sage: RealNumber(0.000000000000000000).prec()
67
sage: RealNumber(00.000000000000000000).prec()
70
sage: RealNumber(.000000000000000000).prec()
64
```
I'm not sure if this is intentional, it's at least uncommon.
(And a leading `+` also increases the precision.)

It looks as if a decimal point is counted as a significant digit.

And, sorry, the code is extremely ugly (not due to the patch) and inefficient.
Examples and parameter description can be improved as well.

I'm not quite sure what kind of strings actually get in (i.e., where/if illegal syntax is catched, it seems all is left to `RealNumber._set()` if not already handled by the parser), this should perhaps be documented, too.



---

archive/issue_comments_081660.json:
```json
{
    "body": "Also, is it intentional that the exponent is ignored when computing the required precision?\nE.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.",
    "created_at": "2010-05-27T15:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81660",
    "user": "https://github.com/nexttime"
}
```

Also, is it intentional that the exponent is ignored when computing the required precision?
E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.



---

archive/issue_comments_081661.json:
```json
{
    "body": "`sage.rings.complex_number.create_ComplexNumber()` also needs work.\n\n(It doesn't \"strip\" trailing/fractional zeros, but also doesn't treat a given exponent correctly. Bases (other than 10) aren't supported; perhaps it should just call `create_RealNumber()` or use the same code to compute the necessary precision once this operates as desired.)",
    "created_at": "2010-05-27T16:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81661",
    "user": "https://github.com/nexttime"
}
```

`sage.rings.complex_number.create_ComplexNumber()` also needs work.

(It doesn't "strip" trailing/fractional zeros, but also doesn't treat a given exponent correctly. Bases (other than 10) aren't supported; perhaps it should just call `create_RealNumber()` or use the same code to compute the necessary precision once this operates as desired.)



---

archive/issue_comments_081662.json:
```json
{
    "body": "apply on top of previous",
    "created_at": "2010-05-27T18:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81662",
    "user": "https://github.com/robertwb"
}
```

apply on top of previous



---

archive/issue_comments_081663.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-27T18:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81663",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081664.json:
```json
{
    "body": "Attachment [8896-part2.patch](tarball://root/attachments/some-uuid/ticket8896/8896-part2.patch) by @robertwb created at 2010-05-27 18:51:01\n\nReplying to [comment:6 leif]:\n> No, the `else` belongs to the `for` statement.\n\n\nExactly. \n\n> But currently, *leading* zeros contribute to the precision, too: :)\n> \n> ```\n> sage: RealNumber(0.000000000000000000).prec()\n> 67\n> sage: RealNumber(00.000000000000000000).prec()\n> 70\n> sage: RealNumber(.000000000000000000).prec()\n> 64\n> ```\n> I'm not sure if this is intentional, it's at least uncommon.\n\n\nThat's the point of this ticket. For 0, all zeros are leading. \n\n> (And a leading `+` also increases the precision.)\n> \n> It looks as if a decimal point is counted as a significant digit.\n\n\nGood catch, fixed. That required some adjustment to keep the input/str in sync. \n\n> And, sorry, the code is extremely ugly (not due to the patch) and inefficient.\n> Examples and parameter description can be improved as well.\n> \n> I'm not quite sure what kind of strings actually get in (i.e., where/if illegal syntax is catched, it seems all is left to `RealNumber._set()` if not already handled by the parser), this should perhaps be documented, too. \n\n\nUpdated the docstring a bit. This is mostly for use by the preparser, though of course it gets used directly as well.",
    "created_at": "2010-05-27T18:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81664",
    "user": "https://github.com/robertwb"
}
```

Attachment [8896-part2.patch](tarball://root/attachments/some-uuid/ticket8896/8896-part2.patch) by @robertwb created at 2010-05-27 18:51:01

Replying to [comment:6 leif]:
> No, the `else` belongs to the `for` statement.


Exactly. 

> But currently, *leading* zeros contribute to the precision, too: :)
> 
> ```
> sage: RealNumber(0.000000000000000000).prec()
> 67
> sage: RealNumber(00.000000000000000000).prec()
> 70
> sage: RealNumber(.000000000000000000).prec()
> 64
> ```
> I'm not sure if this is intentional, it's at least uncommon.


That's the point of this ticket. For 0, all zeros are leading. 

> (And a leading `+` also increases the precision.)
> 
> It looks as if a decimal point is counted as a significant digit.


Good catch, fixed. That required some adjustment to keep the input/str in sync. 

> And, sorry, the code is extremely ugly (not due to the patch) and inefficient.
> Examples and parameter description can be improved as well.
> 
> I'm not quite sure what kind of strings actually get in (i.e., where/if illegal syntax is catched, it seems all is left to `RealNumber._set()` if not already handled by the parser), this should perhaps be documented, too. 


Updated the docstring a bit. This is mostly for use by the preparser, though of course it gets used directly as well.



---

archive/issue_comments_081665.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> Also, is it intentional that the exponent is ignored when computing the required precision?\n> E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.\n\n\nYes, of course. The size of the exponent is completely orthogonal to the number of significant figures. I made create_ComplexNumber defer to create_RealNumber as well.",
    "created_at": "2010-05-27T18:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81665",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:7 leif]:
> Also, is it intentional that the exponent is ignored when computing the required precision?
> E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.


Yes, of course. The size of the exponent is completely orthogonal to the number of significant figures. I made create_ComplexNumber defer to create_RealNumber as well.



---

archive/issue_comments_081666.json:
```json
{
    "body": "> > No, the `else` belongs to the `for` statement.\n\n> \n> Exactly. \n\n\n[Here](http://docs.python.org/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) is the reference for this - I hadn't seen that before.  Thanks for the additional docstring.",
    "created_at": "2010-05-27T19:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81666",
    "user": "https://github.com/kcrisman"
}
```

> > No, the `else` belongs to the `for` statement.

> 
> Exactly. 


[Here](http://docs.python.org/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) is the reference for this - I hadn't seen that before.  Thanks for the additional docstring.



---

archive/issue_comments_081667.json:
```json
{
    "body": "Just took a first glance:\n\n* `create_ComplexNumber()` now looks nice\n* in the above function, it's `len<15` instead of `len<=15`\n* `min_prec` can be smaller than 53 (if specified)\n* `pad` should be (tested to be) non-negative\n* (`min_prec` perhaps too, or `min_prec+pad>=0`) \n* compare against `min_prec+pad` rather than individually for the \"common\" case\n* `rnd` description in `create_RealNumber()` is slightly messed up\n* IMHO leading zeros **left to the decimal point** should be stripped/ignored\n\nMore to come... ;-)\n\n(I've only looked at the patch to the patch.)",
    "created_at": "2010-05-27T23:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81667",
    "user": "https://github.com/nexttime"
}
```

Just took a first glance:

* `create_ComplexNumber()` now looks nice
* in the above function, it's `len<15` instead of `len<=15`
* `min_prec` can be smaller than 53 (if specified)
* `pad` should be (tested to be) non-negative
* (`min_prec` perhaps too, or `min_prec+pad>=0`) 
* compare against `min_prec+pad` rather than individually for the "common" case
* `rnd` description in `create_RealNumber()` is slightly messed up
* IMHO leading zeros **left to the decimal point** should be stripped/ignored

More to come... ;-)

(I've only looked at the patch to the patch.)



---

archive/issue_comments_081668.json:
```json
{
    "body": "Replying to [comment:9 robertwb]:\n> Replying to [comment:6 leif]:\n> > But currently, *leading* zeros contribute to the precision, too: :)\n> > \n> > ```\n> > sage: RealNumber(0.000000000000000000).prec()\n> > 67\n> > sage: RealNumber(00.000000000000000000).prec()\n> > 70\n> > sage: RealNumber(.000000000000000000).prec()\n> > 64\n> > ```\n> > I'm not sure if this is intentional, it's at least uncommon.\n\n> \n> That's the point of this ticket. For 0, all zeros are leading. \n\n\nNot really. We were (only I think) considering zeros of the **fractional** part.\n\nTruncation only makes sense from the right; and you don't express precision by padding zeros to the left. Stating that the earth's diameter is about 013 million meters doesn't give more information than stating it is about 13 million meters.\n\n> Updated the docstring a bit. This is mostly for use by the preparser, though of course it gets used directly as well. \n\n\nI was thinking of scientific notation syntax, too. (Also the examples do not contain that form.)",
    "created_at": "2010-05-27T23:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81668",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:9 robertwb]:
> Replying to [comment:6 leif]:
> > But currently, *leading* zeros contribute to the precision, too: :)
> > 
> > ```
> > sage: RealNumber(0.000000000000000000).prec()
> > 67
> > sage: RealNumber(00.000000000000000000).prec()
> > 70
> > sage: RealNumber(.000000000000000000).prec()
> > 64
> > ```
> > I'm not sure if this is intentional, it's at least uncommon.

> 
> That's the point of this ticket. For 0, all zeros are leading. 


Not really. We were (only I think) considering zeros of the **fractional** part.

Truncation only makes sense from the right; and you don't express precision by padding zeros to the left. Stating that the earth's diameter is about 013 million meters doesn't give more information than stating it is about 13 million meters.

> Updated the docstring a bit. This is mostly for use by the preparser, though of course it gets used directly as well. 


I was thinking of scientific notation syntax, too. (Also the examples do not contain that form.)



---

archive/issue_comments_081669.json:
```json
{
    "body": "Replying to [comment:13 leif]:\n> Not really. We were (only I think) considering zeros of the **fractional** part.\n\n\nTo be more precise, 0.0 and 00.0 denote the same \"thing\", i.e. have the same meaning, while 0.0 and 0.00 do not.",
    "created_at": "2010-05-27T23:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81669",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:13 leif]:
> Not really. We were (only I think) considering zeros of the **fractional** part.


To be more precise, 0.0 and 00.0 denote the same "thing", i.e. have the same meaning, while 0.0 and 0.00 do not.



---

archive/issue_comments_081670.json:
```json
{
    "body": "For those interested in printing real numbers in general, I'll just plug #7682, which could use just a bit of polishing work, I believe, and makes printing real/complex numbers much more consistent and easy to adjust.",
    "created_at": "2010-05-28T00:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81670",
    "user": "https://github.com/jasongrout"
}
```

For those interested in printing real numbers in general, I'll just plug #7682, which could use just a bit of polishing work, I believe, and makes printing real/complex numbers much more consistent and easy to adjust.



---

archive/issue_comments_081671.json:
```json
{
    "body": "Replying to [comment:10 robertwb]:\n> Replying to [comment:7 leif]:\n> > Also, is it intentional that the exponent is ignored when computing the required precision?\n> > E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.\n\n> \n> Yes, of course. The size of the exponent is completely orthogonal to the number of significant figures.\n\n\nI don't agree either. If the \"effective\" exponent (the one in normalized form) exceeds the maximum, one should either increase `prec` accordingly or - more practical - raise an exception.\n\nIf not, this could be a pitfall. But **I** don't mind... ;-)",
    "created_at": "2010-05-28T01:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81671",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:10 robertwb]:
> Replying to [comment:7 leif]:
> > Also, is it intentional that the exponent is ignored when computing the required precision?
> > E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.

> 
> Yes, of course. The size of the exponent is completely orthogonal to the number of significant figures.


I don't agree either. If the "effective" exponent (the one in normalized form) exceeds the maximum, one should either increase `prec` accordingly or - more practical - raise an exception.

If not, this could be a pitfall. But **I** don't mind... ;-)



---

archive/issue_comments_081672.json:
```json
{
    "body": "Replying to [comment:13 leif]:\n> Replying to [comment:9 robertwb]:\n> > That's the point of this ticket. For 0, all zeros are leading. \n\n> \n> Not really. We were (only I think) considering zeros of the **fractional** part.\n> \n> Truncation only makes sense from the right; and you don't express precision by padding zeros to the left. Stating that the earth's diameter is about 013 million meters doesn't give more information than stating it is about 13 million meters.\n\n\nWhich has the same information as saying the Earth's diameter is about 0.000013 trillion meters. Whether or not a digit is significant is not a function of whether it is on the left or right of the decimal. \n\nWould you then say that `0.00e9` and `00.0e8` and `.000e10` have different precisions?",
    "created_at": "2010-05-28T06:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81672",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:13 leif]:
> Replying to [comment:9 robertwb]:
> > That's the point of this ticket. For 0, all zeros are leading. 

> 
> Not really. We were (only I think) considering zeros of the **fractional** part.
> 
> Truncation only makes sense from the right; and you don't express precision by padding zeros to the left. Stating that the earth's diameter is about 013 million meters doesn't give more information than stating it is about 13 million meters.


Which has the same information as saying the Earth's diameter is about 0.000013 trillion meters. Whether or not a digit is significant is not a function of whether it is on the left or right of the decimal. 

Would you then say that `0.00e9` and `00.0e8` and `.000e10` have different precisions?



---

archive/issue_comments_081673.json:
```json
{
    "body": "Replying to [comment:12 leif]:\n> Just took a first glance:\n> \n> * `create_ComplexNumber()` now looks nice\n> * in the above function, it's `len<15` instead of `len<=15`\n\n\nAh, oops.\n\n>  * `min_prec` can be smaller than 53 (if specified)\n\n\nYes, but I'm not following what you're trying to say here. \n\n>  * `pad` should be (tested to be) non-negative\n>  * (`min_prec` perhaps too, or `min_prec+pad>=0`) \n>  * compare against `min_prec+pad` rather than individually for the \"common\" case\n\n\nI don't care if pad is negative (I'll fix the docstring). Same with min_prec, I just pass whatever I get onto the RealField constructor which will raise a perfectly fine exception if the precision is not valid (as defined by MPFR_MIN_PREC and MPFR_MAX_PREC).\n\n>  * `rnd` description in `create_RealNumber()` is slightly messed up\n\n\nAh, I'll fix that. \n\n\n> > > E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.\n\n> > \n> > Yes, of course. The size of the exponent is completely orthogonal to the number of significant figures.\n\n> \n> I don't agree either. If the \"effective\" exponent (the one in normalized form) exceeds the maximum, one should either increase `prec` accordingly or - more practical - raise an exception.\n> \n> If not, this could be a pitfall. But **I** don't mind... ;-)\n\n\nWell, I'd say the above has only two significant digits of precision, no matter what the exponent, which is all this function tries to deduce. The fact that it's subnormal is outside of the scope of this ticket--if an exception should be raise it's not here. (And in this case you can't raise the precision enough, due to memory/library limitations.)",
    "created_at": "2010-05-28T06:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81673",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:12 leif]:
> Just took a first glance:
> 
> * `create_ComplexNumber()` now looks nice
> * in the above function, it's `len<15` instead of `len<=15`


Ah, oops.

>  * `min_prec` can be smaller than 53 (if specified)


Yes, but I'm not following what you're trying to say here. 

>  * `pad` should be (tested to be) non-negative
>  * (`min_prec` perhaps too, or `min_prec+pad>=0`) 
>  * compare against `min_prec+pad` rather than individually for the "common" case


I don't care if pad is negative (I'll fix the docstring). Same with min_prec, I just pass whatever I get onto the RealField constructor which will raise a perfectly fine exception if the precision is not valid (as defined by MPFR_MIN_PREC and MPFR_MAX_PREC).

>  * `rnd` description in `create_RealNumber()` is slightly messed up


Ah, I'll fix that. 


> > > E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.

> > 
> > Yes, of course. The size of the exponent is completely orthogonal to the number of significant figures.

> 
> I don't agree either. If the "effective" exponent (the one in normalized form) exceeds the maximum, one should either increase `prec` accordingly or - more practical - raise an exception.
> 
> If not, this could be a pitfall. But **I** don't mind... ;-)


Well, I'd say the above has only two significant digits of precision, no matter what the exponent, which is all this function tries to deduce. The fact that it's subnormal is outside of the scope of this ticket--if an exception should be raise it's not here. (And in this case you can't raise the precision enough, due to memory/library limitations.)



---

archive/issue_comments_081674.json:
```json
{
    "body": "Replying to [comment:18 robertwb]:\n> Replying to [comment:12 leif]:\n> >  * `min_prec` can be smaller than 53 (if specified)\n \n> \n> Yes, but I'm not following what you're trying to say here. \n> \n> >  * `pad` should be (tested to be) non-negative\n> >  * (`min_prec` perhaps too, or `min_prec+pad>=0`) \n> >  * compare against `min_prec+pad` rather than individually for the \"common\" case\n \n> \n> I don't care if pad is negative (I'll fix the docstring). Same with min_prec, I just pass whatever I get onto the RealField constructor which will raise a perfectly fine exception if the precision is not valid (as defined by MPFR_MIN_PREC and MPFR_MAX_PREC).\n\n\nIf you test for `min_prec+pad==53 and ...`, more inputs fall into the simple common case (`RR`).\n(Using `RR`, i.e. 53 bit mantissa, if the sum is *less* than 53 is perhaps not desired.)",
    "created_at": "2010-05-28T09:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81674",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:18 robertwb]:
> Replying to [comment:12 leif]:
> >  * `min_prec` can be smaller than 53 (if specified)
 
> 
> Yes, but I'm not following what you're trying to say here. 
> 
> >  * `pad` should be (tested to be) non-negative
> >  * (`min_prec` perhaps too, or `min_prec+pad>=0`) 
> >  * compare against `min_prec+pad` rather than individually for the "common" case
 
> 
> I don't care if pad is negative (I'll fix the docstring). Same with min_prec, I just pass whatever I get onto the RealField constructor which will raise a perfectly fine exception if the precision is not valid (as defined by MPFR_MIN_PREC and MPFR_MAX_PREC).


If you test for `min_prec+pad==53 and ...`, more inputs fall into the simple common case (`RR`).
(Using `RR`, i.e. 53 bit mantissa, if the sum is *less* than 53 is perhaps not desired.)



---

archive/issue_comments_081675.json:
```json
{
    "body": "Replying to [comment:19 leif]:\n> (Using `RR`, i.e. 53 bit mantissa, if the sum is *less* than 53 is perhaps not desired.)\n> \n\n\nMust have been some spot on the screen that covered `min_`... ;-)\n\nOf course it's pretty ok to return `RR` in that case, too. (If someone really wants *less* precision, he can use `RealField(prec)(\"...\")` directly.)",
    "created_at": "2010-05-28T12:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81675",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:19 leif]:
> (Using `RR`, i.e. 53 bit mantissa, if the sum is *less* than 53 is perhaps not desired.)
> 


Must have been some spot on the screen that covered `min_`... ;-)

Of course it's pretty ok to return `RR` in that case, too. (If someone really wants *less* precision, he can use `RealField(prec)("...")` directly.)



---

archive/issue_comments_081676.json:
```json
{
    "body": "Attachment [8896-doctests.patch](tarball://root/attachments/some-uuid/ticket8896/8896-doctests.patch) by @robertwb created at 2011-01-26 06:44:11\n\nDoctest fixes for 4.6.1.",
    "created_at": "2011-01-26T06:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81676",
    "user": "https://github.com/robertwb"
}
```

Attachment [8896-doctests.patch](tarball://root/attachments/some-uuid/ticket8896/8896-doctests.patch) by @robertwb created at 2011-01-26 06:44:11

Doctest fixes for 4.6.1.



---

archive/issue_comments_081677.json:
```json
{
    "body": "Folded and rebased on 4.7. Apply only this patch.",
    "created_at": "2011-05-31T07:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81677",
    "user": "https://github.com/robertwb"
}
```

Folded and rebased on 4.7. Apply only this patch.



---

archive/issue_comments_081678.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-06T17:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81678",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081679.json:
```json
{
    "body": "Attachment [8896-rebased.patch](tarball://root/attachments/some-uuid/ticket8896/8896-rebased.patch) by mariah created at 2011-06-06 17:38:28\n\nPatch fixes problem.  Ran 'make testlong'.  All tests passed.  Positive review!",
    "created_at": "2011-06-06T17:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81679",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Attachment [8896-rebased.patch](tarball://root/attachments/some-uuid/ticket8896/8896-rebased.patch) by mariah created at 2011-06-06 17:38:28

Patch fixes problem.  Ran 'make testlong'.  All tests passed.  Positive review!



---

archive/issue_comments_081680.json:
```json
{
    "body": "Thanks!",
    "created_at": "2011-06-06T17:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81680",
    "user": "https://github.com/robertwb"
}
```

Thanks!



---

archive/issue_comments_081681.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-06-08T07:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81681",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_081682.json:
```json
{
    "body": "In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 **should** be treated differently than 0.0000000000000.\n\nI really think the current behaviour of Sage is what makes the most sense (mathematically) so I am not in favour of this ticket.  Of course, if the majority thinks this patch is a good idea then I'm all for it.\n\nOne thing about the patch which is very unclear is why zero is treated differently from other numbers.  Consider::\n\n```\nsage: (0.0).prec()\n53\nsage: (0.1).prec()\n53\nsage: (000000000000000000000.0).prec()\n77\nsage: (000000000000000000000.1).prec()\n53\nsage: (0.000000000000000000000).prec()\n77\nsage: (0.000000000000000000001).prec()\n53\n```",
    "created_at": "2011-06-08T07:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81682",
    "user": "https://github.com/jdemeyer"
}
```

In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 **should** be treated differently than 0.0000000000000.

I really think the current behaviour of Sage is what makes the most sense (mathematically) so I am not in favour of this ticket.  Of course, if the majority thinks this patch is a good idea then I'm all for it.

One thing about the patch which is very unclear is why zero is treated differently from other numbers.  Consider::

```
sage: (0.0).prec()
53
sage: (0.1).prec()
53
sage: (000000000000000000000.0).prec()
77
sage: (000000000000000000000.1).prec()
53
sage: (0.000000000000000000000).prec()
77
sage: (0.000000000000000000001).prec()
53
```



---

archive/issue_comments_081683.json:
```json
{
    "body": "Replying to [comment:25 jdemeyer]:\n> In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 **should** be treated differently than 0.0000000000000.\n\n\nIt's exactly the same reason that 1.0 is treated differently than 1.0000000000000000000000. The (value-preserving) trailing zeros indicate higher precision. \n\n> I really think the current behaviour of Sage is what makes the most sense (mathematically) so I am not in favour of this ticket.  Of course, if the majority thinks this patch is a good idea then I'm all for it.\n> \n> One thing about the patch which is very unclear is why zero is treated differently from other numbers.  \n\n\nBecause otherwise there's now way to write a high-precision zero (in fact I can't think of any other interpretation of a large number of trailing zeros). \n\n> Consider::\n> \n> ```\n> sage: (0.0).prec()\n> 53\n> sage: (0.1).prec()\n> 53\n> sage: (000000000000000000000.0).prec()\n> 77\n> sage: (000000000000000000000.1).prec()\n> 53\n> sage: (0.000000000000000000000).prec()\n> 77\n> sage: (0.000000000000000000001).prec()\n> 53\n> ```",
    "created_at": "2011-06-08T15:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81683",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:25 jdemeyer]:
> In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 **should** be treated differently than 0.0000000000000.


It's exactly the same reason that 1.0 is treated differently than 1.0000000000000000000000. The (value-preserving) trailing zeros indicate higher precision. 

> I really think the current behaviour of Sage is what makes the most sense (mathematically) so I am not in favour of this ticket.  Of course, if the majority thinks this patch is a good idea then I'm all for it.
> 
> One thing about the patch which is very unclear is why zero is treated differently from other numbers.  


Because otherwise there's now way to write a high-precision zero (in fact I can't think of any other interpretation of a large number of trailing zeros). 

> Consider::
> 
> ```
> sage: (0.0).prec()
> 53
> sage: (0.1).prec()
> 53
> sage: (000000000000000000000.0).prec()
> 77
> sage: (000000000000000000000.1).prec()
> 53
> sage: (0.000000000000000000000).prec()
> 77
> sage: (0.000000000000000000001).prec()
> 53
> ```



---

archive/issue_comments_081684.json:
```json
{
    "body": "Another argument is that the BDFL suggested this change fairly strongly when opening this ticket :)\n\nMore seriously, I do have a question here.\nRobert's reasoning seems sound in the following example - we want a high-precision zero, and this is the best way to acquire it.\n\n```\n> sage: (0.000000000000000000000).prec()\n> 77\n> sage: (0.000000000000000000001).prec()\n> 53\n```\nBut I agree with Jeroen that the following seems problematic.  Didn't you say yourself (robertwb) that leading zeros *before* the decimal point shouldn't make a difference?  So in the case here maybe we should have the default precision...\n\n```\n> sage: (000000000000000000000.0).prec()\n> 77\n> sage: (000000000000000000000.1).prec()\n> 53\n```\nKeeping in mind that I have very little invested in either outcome for now, so take these only as observations.",
    "created_at": "2011-06-08T15:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81684",
    "user": "https://github.com/kcrisman"
}
```

Another argument is that the BDFL suggested this change fairly strongly when opening this ticket :)

More seriously, I do have a question here.
Robert's reasoning seems sound in the following example - we want a high-precision zero, and this is the best way to acquire it.

```
> sage: (0.000000000000000000000).prec()
> 77
> sage: (0.000000000000000000001).prec()
> 53
```
But I agree with Jeroen that the following seems problematic.  Didn't you say yourself (robertwb) that leading zeros *before* the decimal point shouldn't make a difference?  So in the case here maybe we should have the default precision...

```
> sage: (000000000000000000000.0).prec()
> 77
> sage: (000000000000000000000.1).prec()
> 53
```
Keeping in mind that I have very little invested in either outcome for now, so take these only as observations.



---

archive/issue_comments_081685.json:
```json
{
    "body": "Replying to [comment:26 robertwb]:\n> Replying to [comment:25 jdemeyer]:\n> > In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 **should** be treated differently than 0.0000000000000.\n\n> \n> It's exactly the same reason that 1.0 is treated differently than 1.0000000000000000000000. The (value-preserving) trailing zeros indicate higher precision. \n\nIt is absolutely *not the same* because with non-zero numbers only digits **after** a non-zero digit contribute to the precision.  Indeed, `0.437` and `0.00000000000437` have exactly the same precision.\n\n> Because otherwise there's now way to write a high-precision zero (in fact I can't think of any other interpretation of a large number of trailing zeros). \n\nWell, you can always do:\n\n```\nsage: zero = RealField(1000)(0)\nsage: zero.prec()\n1000\n```\n\nAn other way to demonstrate the problem with this patch is that truncating decimal numbers (i.e. removing digits from the right) can *increase* the precision, which is very unlogical::\n\n```\nsage: (0.000000000000000000001234567890123456789).prec()\n67\nsage: (0.00000000000000000000123456789012345678).prec()\n64\nsage: (0.000000000000000000001).prec()\n53\nsage: (0.00000000000000000000).prec()\n74\n```",
    "created_at": "2011-06-08T16:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81685",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:26 robertwb]:
> Replying to [comment:25 jdemeyer]:
> > In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 **should** be treated differently than 0.0000000000000.

> 
> It's exactly the same reason that 1.0 is treated differently than 1.0000000000000000000000. The (value-preserving) trailing zeros indicate higher precision. 

It is absolutely *not the same* because with non-zero numbers only digits **after** a non-zero digit contribute to the precision.  Indeed, `0.437` and `0.00000000000437` have exactly the same precision.

> Because otherwise there's now way to write a high-precision zero (in fact I can't think of any other interpretation of a large number of trailing zeros). 

Well, you can always do:

```
sage: zero = RealField(1000)(0)
sage: zero.prec()
1000
```

An other way to demonstrate the problem with this patch is that truncating decimal numbers (i.e. removing digits from the right) can *increase* the precision, which is very unlogical::

```
sage: (0.000000000000000000001234567890123456789).prec()
67
sage: (0.00000000000000000000123456789012345678).prec()
64
sage: (0.000000000000000000001).prec()
53
sage: (0.00000000000000000000).prec()
74
```



---

archive/issue_comments_081686.json:
```json
{
    "body": "Replying to [comment:28 jdemeyer]:\n> Replying to [comment:26 robertwb]:\n> > Replying to [comment:25 jdemeyer]:\n> > > In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 **should** be treated differently than 0.0000000000000.\n\n> > \n> > It's exactly the same reason that 1.0 is treated differently than 1.0000000000000000000000. The (value-preserving) trailing zeros indicate higher precision. \n\n> It is absolutely *not the same* because with non-zero numbers only digits **after** a non-zero digit contribute to the precision.  Indeed, `0.437` and `0.00000000000437` have exactly the same precision.\n\nThis hinges on the ambiguity of the term \"trialing zero.\" Sage interprets trailing zeros after the decimal point as additional precision. To me, trailing zeros are those that are not followed by a non-zero digit, to you trailing zeros must also follow a non-zero digit. \n\n> > Because otherwise there's now way to write a high-precision zero (in fact I can't think of any other interpretation of a large number of trailing zeros). \n\n> Well, you can always do:\n> {{{\n> sage: zero = RealField(1000)(0)\n> sage: zero.prec()\n> 1000\n> }}}\n\n\nYeah, but that's a pain, but to me the fact that 0.00000000000000000000000000000000 is not high precision is more surprising, as it has many significant digits. \n\n> An other way to demonstrate the problem with this patch is that truncating decimal numbers (i.e. removing digits from the right) can *increase* the precision, which is very unlogical::\n> \n> ```\n> sage: (0.000000000000000000001234567890123456789).prec()\n> 67\n> sage: (0.00000000000000000000123456789012345678).prec()\n> 64\n> sage: (0.000000000000000000001).prec()\n> 53\n> sage: (0.00000000000000000000).prec()\n> 74\n> ```\n\n\nIt also changes the relative value by a huge amount :) \n\nIs it worth taking this discussion to sage-devel?",
    "created_at": "2011-06-08T16:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81686",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:28 jdemeyer]:
> Replying to [comment:26 robertwb]:
> > Replying to [comment:25 jdemeyer]:
> > > In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 **should** be treated differently than 0.0000000000000.

> > 
> > It's exactly the same reason that 1.0 is treated differently than 1.0000000000000000000000. The (value-preserving) trailing zeros indicate higher precision. 

> It is absolutely *not the same* because with non-zero numbers only digits **after** a non-zero digit contribute to the precision.  Indeed, `0.437` and `0.00000000000437` have exactly the same precision.

This hinges on the ambiguity of the term "trialing zero." Sage interprets trailing zeros after the decimal point as additional precision. To me, trailing zeros are those that are not followed by a non-zero digit, to you trailing zeros must also follow a non-zero digit. 

> > Because otherwise there's now way to write a high-precision zero (in fact I can't think of any other interpretation of a large number of trailing zeros). 

> Well, you can always do:
> {{{
> sage: zero = RealField(1000)(0)
> sage: zero.prec()
> 1000
> }}}


Yeah, but that's a pain, but to me the fact that 0.00000000000000000000000000000000 is not high precision is more surprising, as it has many significant digits. 

> An other way to demonstrate the problem with this patch is that truncating decimal numbers (i.e. removing digits from the right) can *increase* the precision, which is very unlogical::
> 
> ```
> sage: (0.000000000000000000001234567890123456789).prec()
> 67
> sage: (0.00000000000000000000123456789012345678).prec()
> 64
> sage: (0.000000000000000000001).prec()
> 53
> sage: (0.00000000000000000000).prec()
> 74
> ```


It also changes the relative value by a huge amount :) 

Is it worth taking this discussion to sage-devel?



---

archive/issue_comments_081687.json:
```json
{
    "body": "Replying to [comment:29 robertwb]:\n> to me the fact that 0.00000000000000000000000000000000 is not high precision is more surprising, as it has many significant digits.\n\nI would say that it does have a lot of *digits* but that none of them is a *significant digit*.",
    "created_at": "2011-06-08T19:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81687",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:29 robertwb]:
> to me the fact that 0.00000000000000000000000000000000 is not high precision is more surprising, as it has many significant digits.

I would say that it does have a lot of *digits* but that none of them is a *significant digit*.



---

archive/issue_events_021706.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-08-02T19:32:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8896#event-21706"
}
```



---

archive/issue_comments_081688.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8896#issuecomment-81688",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".
