# Issue 7828: There should be a top-level sign() function.

archive/issues_007828.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7828\n\n",
    "created_at": "2010-01-03T05:34:19Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "There should be a top-level sign() function.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7828",
    "user": "robertwb"
}
```
Assignee: AlexGhitza



Issue created by migration from https://trac.sagemath.org/ticket/7828





---

archive/issue_comments_067767.json:
```json
{
    "body": "Apparently, it's called `sgn`, but perhaps we should have sign as an alias.",
    "created_at": "2010-01-03T06:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67767",
    "user": "robertwb"
}
```

Apparently, it's called `sgn`, but perhaps we should have sign as an alias.



---

archive/issue_comments_067768.json:
```json
{
    "body": "Especially, if some of the methods are .sign().",
    "created_at": "2010-01-03T18:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67768",
    "user": "mhansen"
}
```

Especially, if some of the methods are .sign().



---

archive/issue_comments_067769.json:
```json
{
    "body": "Okay, this makes lots of sense, and in fact we should check hasattr with that first.  Patch coming up, which should work but will also allow (perhaps this is not good):\n\n```\n            sage: p = PermutationGroupElement('(3,4,8,7,9)')\n            sage: p.sign()\n            1\n            sage: sign(p)\n            1\n```\n",
    "created_at": "2010-05-26T19:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67769",
    "user": "kcrisman"
}
```

Okay, this makes lots of sense, and in fact we should check hasattr with that first.  Patch coming up, which should work but will also allow (perhaps this is not good):

```
            sage: p = PermutationGroupElement('(3,4,8,7,9)')
            sage: p.sign()
            1
            sage: sign(p)
            1
```




---

archive/issue_comments_067770.json:
```json
{
    "body": "Based on 4.4.2",
    "created_at": "2010-05-26T19:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67770",
    "user": "kcrisman"
}
```

Based on 4.4.2



---

archive/issue_comments_067771.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-26T19:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67771",
    "user": "kcrisman"
}
```

Attachment



---

archive/issue_comments_067772.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-26T19:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67772",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067773.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-27T21:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67773",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067774.json:
```json
{
    "body": "Looks good, applies fine to 4.4.3.alpha0 and tests pass.\n\nI did wonder whether it would be better to return a Sage integer rather than an int?\n\nAlso, I looked for places where sgn() was used/defined and found a redundant  definition of sgn() in quadratic_forms/extras.py, which I am removing in another ticket (#9068).",
    "created_at": "2010-05-27T21:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67774",
    "user": "cremona"
}
```

Looks good, applies fine to 4.4.3.alpha0 and tests pass.

I did wonder whether it would be better to return a Sage integer rather than an int?

Also, I looked for places where sgn() was used/defined and found a redundant  definition of sgn() in quadratic_forms/extras.py, which I am removing in another ticket (#9068).



---

archive/issue_comments_067775.json:
```json
{
    "body": "> I did wonder whether it would be better to return a Sage integer rather than an int?\n\nHmm, that is an interesting thing I should have considered but did not.  As long as we are consistent, that's probably the main thing, though it is often helpful to return something that has the Integer methods... Are there any current sign()/sgn() methods that return something other than an int?  \n\nUsually one just adds or multiplies it with Integers, but I could imagine that sometimes the output itself would be important and that it should also then be an Integer.  If so... another ticket, or on this one?",
    "created_at": "2010-05-28T00:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67775",
    "user": "kcrisman"
}
```

> I did wonder whether it would be better to return a Sage integer rather than an int?

Hmm, that is an interesting thing I should have considered but did not.  As long as we are consistent, that's probably the main thing, though it is often helpful to return something that has the Integer methods... Are there any current sign()/sgn() methods that return something other than an int?  

Usually one just adds or multiplies it with Integers, but I could imagine that sometimes the output itself would be important and that it should also then be an Integer.  If so... another ticket, or on this one?



---

archive/issue_comments_067776.json:
```json
{
    "body": "Well, I did look for other places where methods sgn() or sign() were defined;  since in fact I have another comment, which is that as well as looking to see if x has a method sign() you should also look for a method sgn().  The only thing I found was that function in quadratic_forms, and that distracted me from making this comment.\n\nI will do the following now, and report back:\n\n1. Apply both your patch and mine at #9068\n2. Change the function you changed in two ways: making the return type Integer and also checking for x.sgn()\n3. Test the whole library.\n\nFor the moment I have reverted this to \"needs work\".",
    "created_at": "2010-05-28T08:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67776",
    "user": "cremona"
}
```

Well, I did look for other places where methods sgn() or sign() were defined;  since in fact I have another comment, which is that as well as looking to see if x has a method sign() you should also look for a method sgn().  The only thing I found was that function in quadratic_forms, and that distracted me from making this comment.

I will do the following now, and report back:

1. Apply both your patch and mine at #9068
2. Change the function you changed in two ways: making the return type Integer and also checking for x.sgn()
3. Test the whole library.

For the moment I have reverted this to "needs work".



---

archive/issue_comments_067777.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-05-28T08:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67777",
    "user": "cremona"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_067778.json:
```json
{
    "body": "Attachment\n\nApply after previous",
    "created_at": "2010-05-28T09:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67778",
    "user": "cremona"
}
```

Attachment

Apply after previous



---

archive/issue_comments_067779.json:
```json
{
    "body": "Changing keywords from \"\" to \"sign sgn\".",
    "created_at": "2010-05-28T09:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67779",
    "user": "cremona"
}
```

Changing keywords from "" to "sign sgn".



---

archive/issue_comments_067780.json:
```json
{
    "body": "Changing component from algebra to basic arithmetic.",
    "created_at": "2010-05-28T09:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67780",
    "user": "cremona"
}
```

Changing component from algebra to basic arithmetic.



---

archive/issue_comments_067781.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-28T09:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67781",
    "user": "cremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067782.json:
```json
{
    "body": "OK, I did that (see the reviewer patch).  All tests pass (note that I also had my patch from #9068 applied).\n\nI think we need an independent reviewer of the combined changes (preferably of #9068 also) so I have put it back to \"needs review\".",
    "created_at": "2010-05-28T09:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67782",
    "user": "cremona"
}
```

OK, I did that (see the reviewer patch).  All tests pass (note that I also had my patch from #9068 applied).

I think we need an independent reviewer of the combined changes (preferably of #9068 also) so I have put it back to "needs review".



---

archive/issue_comments_067783.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-28T17:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67783",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067784.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-05-28T17:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67784",
    "user": "robertwb"
}
```

Looks good to me.



---

archive/issue_comments_067785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T08:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67785",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_067786.json:
```json
{
    "body": "Was there a concious decision in this ticket (or elsewhere) not to standardize on either `sign()` or `sgn()`. I just saw the relevant part of `sage/functions/generalized.py`, and thought one of these is redundant.",
    "created_at": "2010-09-09T09:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67786",
    "user": "burcin"
}
```

Was there a concious decision in this ticket (or elsewhere) not to standardize on either `sign()` or `sgn()`. I just saw the relevant part of `sage/functions/generalized.py`, and thought one of these is redundant.



---

archive/issue_comments_067787.json:
```json
{
    "body": "I think the point was that not everyone would think of `sign()` or `sgn()` automatically; depending on where you come from mathematically, one or the other is more natural.  This doesn't seem to me to be a problem; we have lots of aliases, and it seems very unlikely that there would be confusion once someone saw both of them, as sgn is clearly short for sign.\n\nOr maybe you mean we should pick one and leave the other one as an unspoken alias.  \n\nHowever, I guess in this ticket and #9068 there is an implicit assumption that the methods (as opposed to functions) should be called `.sign()`.  Is that bad?",
    "created_at": "2010-09-09T13:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67787",
    "user": "kcrisman"
}
```

I think the point was that not everyone would think of `sign()` or `sgn()` automatically; depending on where you come from mathematically, one or the other is more natural.  This doesn't seem to me to be a problem; we have lots of aliases, and it seems very unlikely that there would be confusion once someone saw both of them, as sgn is clearly short for sign.

Or maybe you mean we should pick one and leave the other one as an unspoken alias.  

However, I guess in this ticket and #9068 there is an implicit assumption that the methods (as opposed to functions) should be called `.sign()`.  Is that bad?



---

archive/issue_comments_067788.json:
```json
{
    "body": "I suggest we choose `sign()` as the convention and make `sgn()` an alias where necessary. Then we don't need to check for the existence of both `.sign()` and `.sgn()` methods. That code (around line 474 of `sage/functions/generalized.py`) suggests we encourage sloppy programming.\n\nShall I open a ticket to look through the library for `sgn()` and `sign()` functions and change them appropriately?",
    "created_at": "2010-09-13T09:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67788",
    "user": "burcin"
}
```

I suggest we choose `sign()` as the convention and make `sgn()` an alias where necessary. Then we don't need to check for the existence of both `.sign()` and `.sgn()` methods. That code (around line 474 of `sage/functions/generalized.py`) suggests we encourage sloppy programming.

Shall I open a ticket to look through the library for `sgn()` and `sign()` functions and change them appropriately?



---

archive/issue_comments_067789.json:
```json
{
    "body": "I think that cremona already did this, but put this in there just in case there was another one.   So are you suggesting that the reviewer patch should be modified?  I think that the fear is that someone will put in a `.sgn()` method and won't realize it won't work; on the other hand, one could check for `.sgn()` and raise an error, but that also would make it look weird.  Though I wouldn't say sloppy, but rather decentralized programming.",
    "created_at": "2010-09-13T14:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7828#issuecomment-67789",
    "user": "kcrisman"
}
```

I think that cremona already did this, but put this in there just in case there was another one.   So are you suggesting that the reviewer patch should be modified?  I think that the fear is that someone will put in a `.sgn()` method and won't realize it won't work; on the other hand, one could check for `.sgn()` and raise an error, but that also would make it look weird.  Though I wouldn't say sloppy, but rather decentralized programming.
