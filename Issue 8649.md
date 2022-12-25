# Issue 8649: to_tableau method broken for crystals of type B

archive/issues_008649.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: crystals\n\n- For type B_n the to_tableau method in crystals is wrong: 00 in the list should give a column and not a row\n\n- Changed __call__ function in both TensorProductOfCrystals and CrystalOfTableau x to _element_constructor_ to make automatic tests pass (before element constructor was not an idempotent)\n\n- Fixed subsequent bug of empty tableau in CrystalOfTableau and empty highest weight crystal\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8649\n\n",
    "created_at": "2010-04-03T15:56:10Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "to_tableau method broken for crystals of type B",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8649",
    "user": "https://github.com/anneschilling"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: crystals

- For type B_n the to_tableau method in crystals is wrong: 00 in the list should give a column and not a row

- Changed __call__ function in both TensorProductOfCrystals and CrystalOfTableau x to _element_constructor_ to make automatic tests pass (before element constructor was not an idempotent)

- Fixed subsequent bug of empty tableau in CrystalOfTableau and empty highest weight crystal


Issue created by migration from https://trac.sagemath.org/ticket/8649





---

archive/issue_comments_078340.json:
```json
{
    "body": "Attachment [trac_8649_crystal-as.patch](tarball://root/attachments/some-uuid/ticket8649/trac_8649_crystal-as.patch) by @anneschilling created at 2010-04-03 17:29:16",
    "created_at": "2010-04-03T17:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78340",
    "user": "https://github.com/anneschilling"
}
```

Attachment [trac_8649_crystal-as.patch](tarball://root/attachments/some-uuid/ticket8649/trac_8649_crystal-as.patch) by @anneschilling created at 2010-04-03 17:29:16



---

archive/issue_comments_078341.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-03T17:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78341",
    "user": "https://github.com/anneschilling"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078342.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-18T15:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78342",
    "user": "https://github.com/dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078343.json:
```json
{
    "body": "Before the patch, the to_tableau method of crystals of tableaux could return a tableau with the wrong shape. I did a lot of testing of the fix. I found that there were problems with type B crystals, but also for type G2. (Crystal of letters, and hence crystals of tableaux are implemented for Type G2 even though this method of producing crystals may not be appropriate for other exceptional types.)\n\nAfter the patch I found no problems after testing a lot of crystals of various Cartan types. In order to test a crystal, I simply verified that all elements v have the same `v.to_tableau().shape()`.\n\nI also ran sage -testall and all tests pass.\n\nThe `__call__` method is also changed to `_element_constructor_` for the reason given in the patch description. This does not seem to break anything.\n\nMy conclusion is that the patch is correct and fixes a bad book. It should be merged.",
    "created_at": "2010-04-18T15:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78343",
    "user": "https://github.com/dwbump"
}
```

Before the patch, the to_tableau method of crystals of tableaux could return a tableau with the wrong shape. I did a lot of testing of the fix. I found that there were problems with type B crystals, but also for type G2. (Crystal of letters, and hence crystals of tableaux are implemented for Type G2 even though this method of producing crystals may not be appropriate for other exceptional types.)

After the patch I found no problems after testing a lot of crystals of various Cartan types. In order to test a crystal, I simply verified that all elements v have the same `v.to_tableau().shape()`.

I also ran sage -testall and all tests pass.

The `__call__` method is also changed to `_element_constructor_` for the reason given in the patch description. This does not seem to break anything.

My conclusion is that the patch is correct and fixes a bad book. It should be merged.



---

archive/issue_comments_078344.json:
```json
{
    "body": "Ah, we did a simultaneous review :-) Well, for the record, here were my comments:\n\nAll test pass on 4.3.5, and the changes are technically good (crystals are far more coercion friendly now). Thanks Anne for handling this!\n\nI am just not very comfortable with the special casing with 0 to handle type B, which sounds more like a workaround than a mathematically meaningful rule.\n\nDan: what do you think? If that's fine with you, please set a positive review.",
    "created_at": "2010-04-18T15:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78344",
    "user": "https://github.com/nthiery"
}
```

Ah, we did a simultaneous review :-) Well, for the record, here were my comments:

All test pass on 4.3.5, and the changes are technically good (crystals are far more coercion friendly now). Thanks Anne for handling this!

I am just not very comfortable with the special casing with 0 to handle type B, which sounds more like a workaround than a mathematically meaningful rule.

Dan: what do you think? If that's fine with you, please set a positive review.



---

archive/issue_comments_078345.json:
```json
{
    "body": "I wrote:\n\n> My conclusion is that the patch is correct and fixes a bad book. It should be merged.\n\n\nI meant a bad *bug*.\n\nReplying to Nicolas:\n\nIt was news to me that Type B tableaux (which were first invented I think by Kashiwara) do not have to be column strict when 0 is involved. That is, Type A tableaux are the classical ones and every column is strict. It looks to me as if there actually is something different about 0.\nI don't understand this as a mathematical point, but I did enough testing that I am sure\nthe patch is right.",
    "created_at": "2010-04-18T16:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78345",
    "user": "https://github.com/dwbump"
}
```

I wrote:

> My conclusion is that the patch is correct and fixes a bad book. It should be merged.


I meant a bad *bug*.

Replying to Nicolas:

It was news to me that Type B tableaux (which were first invented I think by Kashiwara) do not have to be column strict when 0 is involved. That is, Type A tableaux are the classical ones and every column is strict. It looks to me as if there actually is something different about 0.
I don't understand this as a mathematical point, but I did enough testing that I am sure
the patch is right.



---

archive/issue_comments_078346.json:
```json
{
    "body": "Dear Dan and Nicolas,\n\nThank you for the review. The mathematical reason why in type B the 0 is special,\nis that it sits in a string of length 2:\n\n1 -> 2 -> 0 -> -2 -> -1\n\nHence a column of height 2 for example can become\n\n2      0      0      0\n1 -2-> 1 -1-> 2 -2-> 0\n\nsince in the tensor product always the rightmost unbracketed element is changed.\nFor similar reasons, in the row case there cannot be two 0s.\n\nSo this is really due to the string of length 2 which the other crystal of letters\ndo not have. Nicolas, how else should the code be written to detect this?\nThe paper by Kashiwara-Nakashima on tableaux for other types is also pretty\ncase specific.\n\nBest wishes,\n\nAnne  \n\nReplying to [comment:4 bump]:\n> I wrote:\n> \n> > My conclusion is that the patch is correct and fixes a bad book. It should be merged.\n\n> \n> I meant a bad *bug*.\n> \n> Replying to Nicolas:\n> \n> It was news to me that Type B tableaux (which were first invented I think by Kashiwara) do not have to be column strict when 0 is involved. That is, Type A tableaux are the classical ones and every column is strict. It looks to me as if there actually is something different about 0.\n> I don't understand this as a mathematical point, but I did enough testing that I am sure\n> the patch is right.\n\n>",
    "created_at": "2010-04-18T16:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78346",
    "user": "https://github.com/anneschilling"
}
```

Dear Dan and Nicolas,

Thank you for the review. The mathematical reason why in type B the 0 is special,
is that it sits in a string of length 2:

1 -> 2 -> 0 -> -2 -> -1

Hence a column of height 2 for example can become

2      0      0      0
1 -2-> 1 -1-> 2 -2-> 0

since in the tensor product always the rightmost unbracketed element is changed.
For similar reasons, in the row case there cannot be two 0s.

So this is really due to the string of length 2 which the other crystal of letters
do not have. Nicolas, how else should the code be written to detect this?
The paper by Kashiwara-Nakashima on tableaux for other types is also pretty
case specific.

Best wishes,

Anne  

Replying to [comment:4 bump]:
> I wrote:
> 
> > My conclusion is that the patch is correct and fixes a bad book. It should be merged.

> 
> I meant a bad *bug*.
> 
> Replying to Nicolas:
> 
> It was news to me that Type B tableaux (which were first invented I think by Kashiwara) do not have to be column strict when 0 is involved. That is, Type A tableaux are the classical ones and every column is strict. It looks to me as if there actually is something different about 0.
> I don't understand this as a mathematical point, but I did enough testing that I am sure
> the patch is right.

>



---

archive/issue_comments_078347.json:
```json
{
    "body": "Replying to [comment:5 aschilling]:\n> Thank you for the review. The mathematical reason why in type B the 0 is special,\n> is that it sits in a string of length 2:\n> \n> 1 -> 2 -> 0 -> -2 -> -1\n> \n> Hence a column of height 2 for example can become\n> \n> 2      0      0      0\n> 1 -2-> 1 -1-> 2 -2-> 0\n> \n> since in the tensor product always the rightmost unbracketed element is changed.\n> For similar reasons, in the row case there cannot be two 0s.\n> \n> So this is really due to the string of length 2 which the other crystal of letters\n> do not have. Nicolas, how else should the code be written to detect this?\n> The paper by Kashiwara-Nakashima on tableaux for other types is also pretty\n> case specific.\n\n\nIn a perfect world, a crystal of letter would have a method which\nwould take two letters a and b, and say whether b can be above a in a\ncolumn. There would be a default implementation (returning a<b in the\ncrystal of letters), and the type B crystal of letter would override\nthis default implementation appropriately.\n\nIf we are sure that no crystal of letter (or more generally crystal\nthat we want to use as letter in a tableau) will ever have a letter\ncalled `0`, except for type `B`, or if we are willing to take the\nrisk, then I guess we can be lazy, and just leave things as they are.",
    "created_at": "2010-04-18T17:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78347",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:5 aschilling]:
> Thank you for the review. The mathematical reason why in type B the 0 is special,
> is that it sits in a string of length 2:
> 
> 1 -> 2 -> 0 -> -2 -> -1
> 
> Hence a column of height 2 for example can become
> 
> 2      0      0      0
> 1 -2-> 1 -1-> 2 -2-> 0
> 
> since in the tensor product always the rightmost unbracketed element is changed.
> For similar reasons, in the row case there cannot be two 0s.
> 
> So this is really due to the string of length 2 which the other crystal of letters
> do not have. Nicolas, how else should the code be written to detect this?
> The paper by Kashiwara-Nakashima on tableaux for other types is also pretty
> case specific.


In a perfect world, a crystal of letter would have a method which
would take two letters a and b, and say whether b can be above a in a
column. There would be a default implementation (returning a<b in the
crystal of letters), and the type B crystal of letter would override
this default implementation appropriately.

If we are sure that no crystal of letter (or more generally crystal
that we want to use as letter in a tableau) will ever have a letter
called `0`, except for type `B`, or if we are willing to take the
risk, then I guess we can be lazy, and just leave things as they are.



---

archive/issue_comments_078348.json:
```json
{
    "body": "Replying to [comment:6 nthiery]:\n> Replying to [comment:5 aschilling]:\n> > Thank you for the review. The mathematical reason why in type B the 0 is special,\n> > is that it sits in a string of length 2:\n> > \n> > 1 -> 2 -> 0 -> -2 -> -1\n> > \n> > Hence a column of height 2 for example can become\n> > \n> > 2      0      0      0\n> > 1 -2-> 1 -1-> 2 -2-> 0\n> > \n> > since in the tensor product always the rightmost unbracketed element is changed.\n> > For similar reasons, in the row case there cannot be two 0s.\n> > \n> > So this is really due to the string of length 2 which the other crystal of letters\n> > do not have. Nicolas, how else should the code be written to detect this?\n> > The paper by Kashiwara-Nakashima on tableaux for other types is also pretty\n> > case specific.\n\n> \n> In a perfect world, a crystal of letter would have a method which\n> would take two letters a and b, and say whether b can be above a in a\n> column. There would be a default implementation (returning a<b in the\n> crystal of letters), and the type B crystal of letter would override\n> this default implementation appropriately.\n> \n> If we are sure that no crystal of letter (or more generally crystal\n> that we want to use as letter in a tableau) will ever have a letter\n> called `0`, except for type `B`, or if we are willing to take the\n> risk, then I guess we can be lazy, and just leave things as they are.\n\n\nFor the classical types ABCD, only type B has a 0. My plan was to implement the exceptional types in a generic way at some point using Littelmann paths or the alcove model and then possibly the HighestWeightCrystal environment. The tableaux method is rather type specific. \n\nFor type D, one can have columns of the form n-bar n n-bar n .... since they are not comparable, so I think a<b for columns might not be the right point of view.  Rather not(a>=b) with the exception of a=b=0. But in any case, one has to distinguish cases. Right now the tableaux method for crystals is only supposed to work for type ABCD.",
    "created_at": "2010-04-18T19:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78348",
    "user": "https://github.com/anneschilling"
}
```

Replying to [comment:6 nthiery]:
> Replying to [comment:5 aschilling]:
> > Thank you for the review. The mathematical reason why in type B the 0 is special,
> > is that it sits in a string of length 2:
> > 
> > 1 -> 2 -> 0 -> -2 -> -1
> > 
> > Hence a column of height 2 for example can become
> > 
> > 2      0      0      0
> > 1 -2-> 1 -1-> 2 -2-> 0
> > 
> > since in the tensor product always the rightmost unbracketed element is changed.
> > For similar reasons, in the row case there cannot be two 0s.
> > 
> > So this is really due to the string of length 2 which the other crystal of letters
> > do not have. Nicolas, how else should the code be written to detect this?
> > The paper by Kashiwara-Nakashima on tableaux for other types is also pretty
> > case specific.

> 
> In a perfect world, a crystal of letter would have a method which
> would take two letters a and b, and say whether b can be above a in a
> column. There would be a default implementation (returning a<b in the
> crystal of letters), and the type B crystal of letter would override
> this default implementation appropriately.
> 
> If we are sure that no crystal of letter (or more generally crystal
> that we want to use as letter in a tableau) will ever have a letter
> called `0`, except for type `B`, or if we are willing to take the
> risk, then I guess we can be lazy, and just leave things as they are.


For the classical types ABCD, only type B has a 0. My plan was to implement the exceptional types in a generic way at some point using Littelmann paths or the alcove model and then possibly the HighestWeightCrystal environment. The tableaux method is rather type specific. 

For type D, one can have columns of the form n-bar n n-bar n .... since they are not comparable, so I think a<b for columns might not be the right point of view.  Rather not(a>=b) with the exception of a=b=0. But in any case, one has to distinguish cases. Right now the tableaux method for crystals is only supposed to work for type ABCD.



---

archive/issue_comments_078349.json:
```json
{
    "body": "> Right now the tableaux method for crystals is only supposed to work for type ABCD.\n\n\nThe tableaux method does work with Sage for G2. This *may* be an accident\nin that this would not be a good approach for other exceptional groups. Or\nmaybe not. Anyway we have a crystal of letters for G2 and it has a 0. And after the\npatch, crystals of tableaux for G2 produce correct tableaux output.\n\nI tend to think this is *not* an accident and take it as evidence that 0 is\nreally special. I guess the case where things might break in a worse way  is F4.\n\n> If we are sure that no crystal of letter (or more generally crystal that we want to use as letter in a tableau) will ever have a letter called 0, except for type B, or if we are willing to take the risk, then I guess we can be lazy, and just leave things as they are.\n\n\nI think the positive review should stand. It's not just a matter of laziness, unless\nwe have an alternative approach.",
    "created_at": "2010-04-18T19:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78349",
    "user": "https://github.com/dwbump"
}
```

> Right now the tableaux method for crystals is only supposed to work for type ABCD.


The tableaux method does work with Sage for G2. This *may* be an accident
in that this would not be a good approach for other exceptional groups. Or
maybe not. Anyway we have a crystal of letters for G2 and it has a 0. And after the
patch, crystals of tableaux for G2 produce correct tableaux output.

I tend to think this is *not* an accident and take it as evidence that 0 is
really special. I guess the case where things might break in a worse way  is F4.

> If we are sure that no crystal of letter (or more generally crystal that we want to use as letter in a tableau) will ever have a letter called 0, except for type B, or if we are willing to take the risk, then I guess we can be lazy, and just leave things as they are.


I think the positive review should stand. It's not just a matter of laziness, unless
we have an alternative approach.



---

archive/issue_comments_078350.json:
```json
{
    "body": "Replying to [comment:8 bump]:\n> The tableaux method does work with Sage for G2. This *may* be an accident\n> in that this would not be a good approach for other exceptional groups. Or\n> maybe not. Anyway we have a crystal of letters for G2 and it has a 0. And after the\n> patch, crystals of tableaux for G2 produce correct tableaux output.\n> \n> I tend to think this is *not* an accident and take it as evidence that 0 is\n> really special. I guess the case where things might break in a worse way  is F4.\n\n\nThat's an interesting point!\n\n> > If we are sure that no crystal of letter (or more generally crystal that we want to use as letter in a tableau) will ever have a letter called 0, except for type B, or if we are willing to take the risk, then I guess we can be lazy, and just leave things as they are.\n\n> \n> I think the positive review should stand. It's not just a matter of laziness, unless\n> we have an alternative approach.\n\n\nI still think it is laziness until we have a proof that 0 is special in all types. But I agree that the positive review should stand.",
    "created_at": "2010-04-18T19:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78350",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:8 bump]:
> The tableaux method does work with Sage for G2. This *may* be an accident
> in that this would not be a good approach for other exceptional groups. Or
> maybe not. Anyway we have a crystal of letters for G2 and it has a 0. And after the
> patch, crystals of tableaux for G2 produce correct tableaux output.
> 
> I tend to think this is *not* an accident and take it as evidence that 0 is
> really special. I guess the case where things might break in a worse way  is F4.


That's an interesting point!

> > If we are sure that no crystal of letter (or more generally crystal that we want to use as letter in a tableau) will ever have a letter called 0, except for type B, or if we are willing to take the risk, then I guess we can be lazy, and just leave things as they are.

> 
> I think the positive review should stand. It's not just a matter of laziness, unless
> we have an alternative approach.


I still think it is laziness until we have a proof that 0 is special in all types. But I agree that the positive review should stand.



---

archive/issue_comments_078351.json:
```json
{
    "body": "Replying to [comment:8 bump]:\n> > Right now the tableaux method for crystals is only supposed to work for type ABCD.\n\n> \n> The tableaux method does work with Sage for G2. This *may* be an accident\n> in that this would not be a good approach for other exceptional groups. Or\n> maybe not. Anyway we have a crystal of letters for G2 and it has a 0. And after the\n> patch, crystals of tableaux for G2 produce correct tableaux output.\n> \n> I tend to think this is *not* an accident and take it as evidence that 0 is\n> really special. I guess the case where things might break in a worse way  is F4.\n\n\nHi Dan,\n\nThank you for this comment! Yes, for G_2 0 is again the only letter that sits\nin a string of length 2. I suppose the letter 0 is chosen in crystal of letters since the weight is zero (and hence the element sits in the middle of a string).\nPerhaps Nicolas accepts this as \"proof\" that 0 is special?\n\nAnne",
    "created_at": "2010-04-19T05:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78351",
    "user": "https://github.com/anneschilling"
}
```

Replying to [comment:8 bump]:
> > Right now the tableaux method for crystals is only supposed to work for type ABCD.

> 
> The tableaux method does work with Sage for G2. This *may* be an accident
> in that this would not be a good approach for other exceptional groups. Or
> maybe not. Anyway we have a crystal of letters for G2 and it has a 0. And after the
> patch, crystals of tableaux for G2 produce correct tableaux output.
> 
> I tend to think this is *not* an accident and take it as evidence that 0 is
> really special. I guess the case where things might break in a worse way  is F4.


Hi Dan,

Thank you for this comment! Yes, for G_2 0 is again the only letter that sits
in a string of length 2. I suppose the letter 0 is chosen in crystal of letters since the weight is zero (and hence the element sits in the middle of a string).
Perhaps Nicolas accepts this as "proof" that 0 is special?

Anne



---

archive/issue_comments_078352.json:
```json
{
    "body": "Merged \"trac_8649_crystal-as.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78352",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8649_crystal-as.patch" into 4.4.alpha1.



---

archive/issue_comments_078353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8649#issuecomment-78353",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_020933.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-19T05:21:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8649",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8649#event-20933"
}
```
