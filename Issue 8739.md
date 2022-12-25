# Issue 8739: Addition of Kolakoski word

archive/issues_008739.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @seblabbe tmonteil\n\nKeywords: Kolakoski, words\n\nThe Kolakoski words are important in combinatorics on words and there are many interesting conjectures that one would like to solve using Sage.\n\nThis ticket intends to add a constructor of such words.\n\nBy definition, the Kolakoski word is the infinite word `K = 22112122...` fixed under the `Delta` operator. The `Delta` of a word is simply the word describing its runs. For instance, if `w = 122112 = 1^1 2^2 1^2 2^1`, then `Delta(w) = 1221`. One can see that over the alphabet '{1,2}', the unique words fixed by `Delta` are `K` and `1K`. Moreover, this notion is naturally generalized to any alphabet `{a,b}` where `a` and `b` are two distinct positive integers.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8739\n\n",
    "created_at": "2010-04-21T17:20:15Z",
    "labels": [
        "component: combinatorics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Addition of Kolakoski word",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8739",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```
Assignee: sage-combinat

CC:  @seblabbe tmonteil

Keywords: Kolakoski, words

The Kolakoski words are important in combinatorics on words and there are many interesting conjectures that one would like to solve using Sage.

This ticket intends to add a constructor of such words.

By definition, the Kolakoski word is the infinite word `K = 22112122...` fixed under the `Delta` operator. The `Delta` of a word is simply the word describing its runs. For instance, if `w = 122112 = 1^1 2^2 1^2 2^1`, then `Delta(w) = 1221`. One can see that over the alphabet '{1,2}', the unique words fixed by `Delta` are `K` and `1K`. Moreover, this notion is naturally generalized to any alphabet `{a,b}` where `a` and `b` are two distinct positive integers.



Issue created by migration from https://trac.sagemath.org/ticket/8739





---

archive/issue_comments_079801.json:
```json
{
    "body": "I'll upload a patch very soon.",
    "created_at": "2010-04-21T17:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79801",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

I'll upload a patch very soon.



---

archive/issue_comments_079802.json:
```json
{
    "body": "Attachment [trac_8739_kolakoski_word-abm.patch](tarball://root/attachments/some-uuid/ticket8739/trac_8739_kolakoski_word-abm.patch) by abmasse created at 2010-04-23 15:03:09\n\nAdds a generator of the Kolakoski sequences",
    "created_at": "2010-04-23T15:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79802",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Attachment [trac_8739_kolakoski_word-abm.patch](tarball://root/attachments/some-uuid/ticket8739/trac_8739_kolakoski_word-abm.patch) by abmasse created at 2010-04-23 15:03:09

Adds a generator of the Kolakoski sequences



---

archive/issue_comments_079803.json:
```json
{
    "body": "Needs review !",
    "created_at": "2010-04-23T15:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79803",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Needs review !



---

archive/issue_comments_079804.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-23T15:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79804",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079805.json:
```json
{
    "body": "Looks nice ! :-)\n\nSeveral remarks though, that I do not dare implement myself :\n\n* You specify in the private function `_KolakoskiWord_iterator` that the alphabet must be composed of two positive integers, but not in `KolakoskiWord`. Are the users supposed to know they should not use anything else ? (honest question, Words are not my field at all even if I can understand the construction :-) )\n\n* You write `current_letter = bar(w[-1])`, thus accessing the -1'th element. What about writing `current_letter = bar(current_letter)` at the end of the loop ?\n\n* You maintain a variable named `current_run`, and keep in memory a list of letters you already used (`w[:current_run]`). Wouldn't it be easier to forget about the current run variable, and just use your list as a queue with append() and pop(0) operations ? :-)\n\nAs I did not know the construction, I thought a bit about how I would write the algorithm and could not find any way to do it without keeping a lot of things in memory, what your `w` variable actually contains. Do you know if there exists a way to get rid of it ? I'm just being curious :-)\n\nNathann",
    "created_at": "2010-04-24T10:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79805",
    "user": "https://github.com/nathanncohen"
}
```

Looks nice ! :-)

Several remarks though, that I do not dare implement myself :

* You specify in the private function `_KolakoskiWord_iterator` that the alphabet must be composed of two positive integers, but not in `KolakoskiWord`. Are the users supposed to know they should not use anything else ? (honest question, Words are not my field at all even if I can understand the construction :-) )

* You write `current_letter = bar(w[-1])`, thus accessing the -1'th element. What about writing `current_letter = bar(current_letter)` at the end of the loop ?

* You maintain a variable named `current_run`, and keep in memory a list of letters you already used (`w[:current_run]`). Wouldn't it be easier to forget about the current run variable, and just use your list as a queue with append() and pop(0) operations ? :-)

As I did not know the construction, I thought a bit about how I would write the algorithm and could not find any way to do it without keeping a lot of things in memory, what your `w` variable actually contains. Do you know if there exists a way to get rid of it ? I'm just being curious :-)

Nathann



---

archive/issue_comments_079806.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-04-24T10:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79806",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_079807.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> Looks nice ! :-)\n> \n> Several remarks though, that I do not dare implement myself :\n> \n> * You specify in the private function `_KolakoskiWord_iterator` that the alphabet must be composed of two positive integers, but not in `KolakoskiWord`. Are the users supposed to know they should not use anything else ? (honest question, Words are not my field at all even if I can understand the construction :-) )\n> \nYou're right, I forgot to document it in the main function. \n\n> * You write `current_letter = bar(w[-1])`, thus accessing the -1'th element. What about writing `current_letter = bar(current_letter)` at the end of the loop ?\n> \n\nRight again. I think I did it to avoid initializing `current_letter` in the basis, but this is less readable and we're not sure if `w[-1]` is performed in constant time. Is it ?\n\n> * You maintain a variable named `current_run`, and keep in memory a list of letters you already used (`w[:current_run]`). Wouldn't it be easier to forget about the current run variable, and just use your list as a queue with append() and pop(0) operations ? :-)\n>\n\nOnce again right. When I first wrote the function, I did as you say, but there was a mistake I couldn't solve. Then I simplified by keeping the complete prefix of the word, but now that it is working, it shouldn't be hard to modify.\n \n> As I did not know the construction, I thought a bit about how I would write the algorithm and could not find any way to do it without keeping a lot of things in memory, what your `w` variable actually contains. Do you know if there exists a way to get rid of it ? I'm just being curious :-)\n> \n\nI feel it would be hard, but I don't have any proof. On the other hand, I can get rid of all values of `w` that have already been read by the `current_run` cursor, as you mentionned above.\n\n> Nathann\n\nThank you for your comment. I'll upload a new patch soon.",
    "created_at": "2010-04-24T15:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79807",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Replying to [comment:3 ncohen]:
> Looks nice ! :-)
> 
> Several remarks though, that I do not dare implement myself :
> 
> * You specify in the private function `_KolakoskiWord_iterator` that the alphabet must be composed of two positive integers, but not in `KolakoskiWord`. Are the users supposed to know they should not use anything else ? (honest question, Words are not my field at all even if I can understand the construction :-) )
> 
You're right, I forgot to document it in the main function. 

> * You write `current_letter = bar(w[-1])`, thus accessing the -1'th element. What about writing `current_letter = bar(current_letter)` at the end of the loop ?
> 

Right again. I think I did it to avoid initializing `current_letter` in the basis, but this is less readable and we're not sure if `w[-1]` is performed in constant time. Is it ?

> * You maintain a variable named `current_run`, and keep in memory a list of letters you already used (`w[:current_run]`). Wouldn't it be easier to forget about the current run variable, and just use your list as a queue with append() and pop(0) operations ? :-)
>

Once again right. When I first wrote the function, I did as you say, but there was a mistake I couldn't solve. Then I simplified by keeping the complete prefix of the word, but now that it is working, it shouldn't be hard to modify.
 
> As I did not know the construction, I thought a bit about how I would write the algorithm and could not find any way to do it without keeping a lot of things in memory, what your `w` variable actually contains. Do you know if there exists a way to get rid of it ? I'm just being curious :-)
> 

I feel it would be hard, but I don't have any proof. On the other hand, I can get rid of all values of `w` that have already been read by the `current_run` cursor, as you mentionned above.

> Nathann

Thank you for your comment. I'll upload a new patch soon.



---

archive/issue_comments_079808.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-04-24T15:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79808",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_079809.json:
```json
{
    "body": "I couldn't tell you whether it is performed in constant time, but even if it is, from the point of view of complexity, I expect bar(your variable) to be faster than using a dictionnary's structure :-)\n\nI'll ask google whether there is anything around about generating this word without needing an increasing amount of memory :-)\n\nNathann",
    "created_at": "2010-04-24T15:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79809",
    "user": "https://github.com/nathanncohen"
}
```

I couldn't tell you whether it is performed in constant time, but even if it is, from the point of view of complexity, I expect bar(your variable) to be faster than using a dictionnary's structure :-)

I'll ask google whether there is anything around about generating this word without needing an increasing amount of memory :-)

Nathann



---

archive/issue_comments_079810.json:
```json
{
    "body": "Applies on top of the main patch",
    "created_at": "2010-11-14T03:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79810",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Applies on top of the main patch



---

archive/issue_comments_079811.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-14T03:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79811",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079812.json:
```json
{
    "body": "Attachment [trac_8739_after_review-abm.patch](tarball://root/attachments/some-uuid/ticket8739/trac_8739_after_review-abm.patch) by abmasse created at 2010-11-14 03:09:53\n\nI uploaded a patch that applies on top of the main one. It takes into account the three points mentionned by Nathann above. Needs review again! (Sorry for the seven months delay)",
    "created_at": "2010-11-14T03:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79812",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Attachment [trac_8739_after_review-abm.patch](tarball://root/attachments/some-uuid/ticket8739/trac_8739_after_review-abm.patch) by abmasse created at 2010-11-14 03:09:53

I uploaded a patch that applies on top of the main one. It takes into account the three points mentionned by Nathann above. Needs review again! (Sorry for the seven months delay)



---

archive/issue_comments_079813.json:
```json
{
    "body": "Attachment [trac_8739-review-sl.patch](tarball://root/attachments/some-uuid/ticket8739/trac_8739-review-sl.patch) by @seblabbe created at 2010-11-14 06:03:22\n\nApplies over the precedent 2 patches",
    "created_at": "2010-11-14T06:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79813",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8739-review-sl.patch](tarball://root/attachments/some-uuid/ticket8739/trac_8739-review-sl.patch) by @seblabbe created at 2010-11-14 06:03:22

Applies over the precedent 2 patches



---

archive/issue_comments_079814.json:
```json
{
    "body": "I just added a new patch which applies on the two precedent. All tests passed. Documentation builds fine. The Kolakoski word satisfies its definition for prefixes up to 100000.\n\nTo me it is a positive review. I let Alexandre change the status of the ticket to positive review if he agrees with my changes.\n\nMaybe Nathann wants to take a look?",
    "created_at": "2010-11-14T06:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79814",
    "user": "https://github.com/seblabbe"
}
```

I just added a new patch which applies on the two precedent. All tests passed. Documentation builds fine. The Kolakoski word satisfies its definition for prefixes up to 100000.

To me it is a positive review. I let Alexandre change the status of the ticket to positive review if he agrees with my changes.

Maybe Nathann wants to take a look?



---

archive/issue_comments_079815.json:
```json
{
    "body": "Hi S\u00e9bastien and Nathann!\n\nThank you for the review. I agree with S\u00e9bastien's changes. I retested all of it on sage-4.6 and all tests still pass. I also took a look at the documentation, which builds fine and is clearer than before. I'll wait for Nathann to see if he agrees with both our modifications and if he's satisfied with my answers to his comments.",
    "created_at": "2010-11-14T16:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79815",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Hi Sébastien and Nathann!

Thank you for the review. I agree with Sébastien's changes. I retested all of it on sage-4.6 and all tests still pass. I also took a look at the documentation, which builds fine and is clearer than before. I'll wait for Nathann to see if he agrees with both our modifications and if he's satisfied with my answers to his comments.



---

archive/issue_comments_079816.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-16T06:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79816",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079817.json:
```json
{
    "body": "Hello !! \n\nSame result for me : all is nice on the doctest's side, and the documentation has no fault that I could spot `:-)`... Nothing to add for the code either, and so this patch is good to go `:-)`\n\nNathann",
    "created_at": "2010-11-16T06:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79817",
    "user": "https://github.com/nathanncohen"
}
```

Hello !! 

Same result for me : all is nice on the doctest's side, and the documentation has no fault that I could spot `:-)`... Nothing to add for the code either, and so this patch is good to go `:-)`

Nathann



---

archive/issue_events_008909.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-12T06:31:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8739#event-8909"
}
```



---

archive/issue_comments_079818.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79818",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_079819.json:
```json
{
    "body": "Hi,\n\nsince the Kolakoski sequence can also be seen as a sequence of integers, it appears in Sloane : http://oeis.org/A000002\n\nHence, it could be a good idea to integrate this in `sage/combinat/sloane_functions.py` and create the class A000002.",
    "created_at": "2011-01-27T23:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8739#issuecomment-79819",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

Hi,

since the Kolakoski sequence can also be seen as a sequence of integers, it appears in Sloane : http://oeis.org/A000002

Hence, it could be a good idea to integrate this in `sage/combinat/sloane_functions.py` and create the class A000002.
