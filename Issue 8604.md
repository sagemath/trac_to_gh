# Issue 8604: Add a class for factor-enumerable words

archive/issues_008604.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  abmasse jleroy\n\nAdd a class for factor-enumerable words, i.e. having an algorithm that enumerates the factor of length n which includes finite words and some family of infinite words. The new file gathers methods (e.g. ``rauzy_graph``) that depends only on the existence of such an algorithm.\n\nIt also adds some method about left,right and bi special words:\n\n\n```\n    sage: f = words.FibonacciWord()[:30]\n    sage: f.number_of_left_special_factors(7)\n    8\n```\n\n\nThe new class ``Word_nfactor_enumerable`` inherits from the abstract ``Word_class`` and `FiniteWord_class` now inherits from this ``Word_nfactor_enumerable`` class. Later, inifinite words having a such an algorithm will inherit also from this new class (in some other ticket).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8604\n\n",
    "created_at": "2010-03-25T12:00:26Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Add a class for factor-enumerable words",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8604",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  abmasse jleroy

Add a class for factor-enumerable words, i.e. having an algorithm that enumerates the factor of length n which includes finite words and some family of infinite words. The new file gathers methods (e.g. ``rauzy_graph``) that depends only on the existence of such an algorithm.

It also adds some method about left,right and bi special words:


```
    sage: f = words.FibonacciWord()[:30]
    sage: f.number_of_left_special_factors(7)
    8
```


The new class ``Word_nfactor_enumerable`` inherits from the abstract ``Word_class`` and `FiniteWord_class` now inherits from this ``Word_nfactor_enumerable`` class. Later, inifinite words having a such an algorithm will inherit also from this new class (in some other ticket).

Issue created by migration from https://trac.sagemath.org/ticket/8604





---

archive/issue_comments_077940.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-25T12:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77940",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077941.json:
```json
{
    "body": "Very interesting ! I'll try to review this patch as soon as I have some time.\n\nI took a quick look at it and I have a question, though. Why aren't the iterator functions (on the left special, bispecial and right special factor) public ? Since they are used only in the public functions that return the result as a list, I think it would be better either to make the iterator functions public, or to merge the two functions in one. Unless you've a reason to do so ?",
    "created_at": "2010-03-25T12:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77941",
    "user": "abmasse"
}
```

Very interesting ! I'll try to review this patch as soon as I have some time.

I took a quick look at it and I have a question, though. Why aren't the iterator functions (on the left special, bispecial and right special factor) public ? Since they are used only in the public functions that return the result as a list, I think it would be better either to make the iterator functions public, or to merge the two functions in one. Unless you've a reason to do so ?



---

archive/issue_comments_077942.json:
```json
{
    "body": "Hi S\u00e9bastien.\n\nI agree with Alex about the iterators on special factors. The only thing you need is the factor set to define them, right? I will try to review it next week but as I already know what are the functions it would probably be quick.",
    "created_at": "2010-04-02T12:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77942",
    "user": "jleroy"
}
```

Hi Sébastien.

I agree with Alex about the iterators on special factors. The only thing you need is the factor set to define them, right? I will try to review it next week but as I already know what are the functions it would probably be quick.



---

archive/issue_comments_077943.json:
```json
{
    "body": "> Very interesting ! I'll try to review this patch as soon as I have some time.\n\nGreat!\n\n> I took a quick look at it and I have a question, though. Why aren't the\n> iterator functions (on the left special, bispecial and right special factor)\n> public ? \n\nI would not say that they are not public since anybody can use it and access it with tab completion by adding the underscore first.\n\nWell because many of the iterator functions are already hidden this way in sage words. We might want to change this convention. Or maybe, like `factor_iterator`, you think it would be more practicable if those were not hidden as well?\n\n> Since they are used only in the public functions that return the\n> result as a list, I think it would be better either to make the iterator\n> functions public, or to merge the two functions in one. Unless you've a\n> reason to do so ?\n\nI am against merging those two functions in one since both functions can be very usefull in different situations. The only question I see is (I don't like using the word public) :\n\nDo we want the iterator functions of this patch to appear in the default listing of the tab completion on a word?\n\nS\u00e9bastien",
    "created_at": "2010-04-11T13:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77943",
    "user": "slabbe"
}
```

> Very interesting ! I'll try to review this patch as soon as I have some time.

Great!

> I took a quick look at it and I have a question, though. Why aren't the
> iterator functions (on the left special, bispecial and right special factor)
> public ? 

I would not say that they are not public since anybody can use it and access it with tab completion by adding the underscore first.

Well because many of the iterator functions are already hidden this way in sage words. We might want to change this convention. Or maybe, like `factor_iterator`, you think it would be more practicable if those were not hidden as well?

> Since they are used only in the public functions that return the
> result as a list, I think it would be better either to make the iterator
> functions public, or to merge the two functions in one. Unless you've a
> reason to do so ?

I am against merging those two functions in one since both functions can be very usefull in different situations. The only question I see is (I don't like using the word public) :

Do we want the iterator functions of this patch to appear in the default listing of the tab completion on a word?

Sébastien



---

archive/issue_comments_077944.json:
```json
{
    "body": "Attachment\n\nDepends on #8429.",
    "created_at": "2010-04-13T18:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77944",
    "user": "slabbe"
}
```

Attachment

Depends on #8429.



---

archive/issue_comments_077945.json:
```json
{
    "body": "I just updated the patch. There was issue with the ordering of many list of factors. I added many ``sorted`` which should fix uniformize the results of doctests and not depend on the machine used anymore.",
    "created_at": "2010-04-13T18:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77945",
    "user": "slabbe"
}
```

I just updated the patch. There was issue with the ordering of many list of factors. I added many ``sorted`` which should fix uniformize the results of doctests and not depend on the machine used anymore.



---

archive/issue_comments_077946.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-15T21:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77946",
    "user": "abmasse"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077947.json:
```json
{
    "body": "Replying to [comment:4 slabbe]:\n> > Very interesting ! I'll try to review this patch as soon as I have some time.\n> \n> Great!\n> \n> > I took a quick look at it and I have a question, though. Why aren't the\n> > iterator functions (on the left special, bispecial and right special factor)\n> > public ? \n> \n> I would not say that they are not public since anybody can use it and access it with tab completion by adding the underscore first.\n> \n> Well because many of the iterator functions are already hidden this way in sage words. We might want to change this convention. Or maybe, like `factor_iterator`, you think it would be more practicable if those were not hidden as well?\n>\nI understand your point, but I still think that since the class of factor-enumerable words was introduced in particular to deal with infinite words, one will probably need iterators to handle, say, left special factors. For instance, assume I want to enumerate all right special factors of a given Sturmian word. I'll need to use an iterator (the list won't be built since it's infinite). And I would like the function to appear when I hit `TAB` when calling a function on an infinite word.\n\nWhat I suggest is to remove the underscore character in front of the iterators and even add a warning for the functions `right_special_factors`, etc. that tells the user that this function could not stop. \n \n> > Since they are used only in the public functions that return the\n> > result as a list, I think it would be better either to make the iterator\n> > functions public, or to merge the two functions in one. Unless you've a\n> > reason to do so ?\n> \n> I am against merging those two functions in one since both functions can be very usefull in different situations. The only question I see is (I don't like using the word public) :\n>\nI agree with you on this one, that was a bad idea.\n \n> Do we want the iterator functions of this patch to appear in the default listing of the tab completion on a word?\n>\nI say yes! I know one of your argument about that was that it would reduce the number of functions appearing when you hit `TAB`. On the other hand, there are not so many of them in the case of infinite words.\n \n> S\u00e9bastien\n>",
    "created_at": "2010-04-15T21:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77947",
    "user": "abmasse"
}
```

Replying to [comment:4 slabbe]:
> > Very interesting ! I'll try to review this patch as soon as I have some time.
> 
> Great!
> 
> > I took a quick look at it and I have a question, though. Why aren't the
> > iterator functions (on the left special, bispecial and right special factor)
> > public ? 
> 
> I would not say that they are not public since anybody can use it and access it with tab completion by adding the underscore first.
> 
> Well because many of the iterator functions are already hidden this way in sage words. We might want to change this convention. Or maybe, like `factor_iterator`, you think it would be more practicable if those were not hidden as well?
>
I understand your point, but I still think that since the class of factor-enumerable words was introduced in particular to deal with infinite words, one will probably need iterators to handle, say, left special factors. For instance, assume I want to enumerate all right special factors of a given Sturmian word. I'll need to use an iterator (the list won't be built since it's infinite). And I would like the function to appear when I hit `TAB` when calling a function on an infinite word.

What I suggest is to remove the underscore character in front of the iterators and even add a warning for the functions `right_special_factors`, etc. that tells the user that this function could not stop. 
 
> > Since they are used only in the public functions that return the
> > result as a list, I think it would be better either to make the iterator
> > functions public, or to merge the two functions in one. Unless you've a
> > reason to do so ?
> 
> I am against merging those two functions in one since both functions can be very usefull in different situations. The only question I see is (I don't like using the word public) :
>
I agree with you on this one, that was a bad idea.
 
> Do we want the iterator functions of this patch to appear in the default listing of the tab completion on a word?
>
I say yes! I know one of your argument about that was that it would reduce the number of functions appearing when you hit `TAB`. On the other hand, there are not so many of them in the case of infinite words.
 
> Sébastien
>



---

archive/issue_comments_077948.json:
```json
{
    "body": "Attachment\n\nApplies over the precedent patch",
    "created_at": "2010-04-18T19:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77948",
    "user": "slabbe"
}
```

Attachment

Applies over the precedent patch



---

archive/issue_comments_077949.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-18T19:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77949",
    "user": "slabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077950.json:
```json
{
    "body": "I agree with your suggestions. I changed the patch accordingly (see new patch attached).\n\nNeeds review!",
    "created_at": "2010-04-18T19:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77950",
    "user": "slabbe"
}
```

I agree with your suggestions. I changed the patch accordingly (see new patch attached).

Needs review!



---

archive/issue_comments_077951.json:
```json
{
    "body": "Changing keywords from \"\" to \"Words, factors, enumeration\".",
    "created_at": "2010-06-23T20:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77951",
    "user": "abmasse"
}
```

Changing keywords from "" to "Words, factors, enumeration".



---

archive/issue_comments_077952.json:
```json
{
    "body": "Hello, S\u00e9bastien and Julien !\n\n\nSorry about the delay, I've been very busy lately. I retested the patch on sage-4.4.3. All tests passed and the documentation built fine too. Therefore, I'm giving this patch a positive review.",
    "created_at": "2010-06-23T20:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77952",
    "user": "abmasse"
}
```

Hello, Sébastien and Julien !


Sorry about the delay, I've been very busy lately. I retested the patch on sage-4.4.3. All tests passed and the documentation built fine too. Therefore, I'm giving this patch a positive review.



---

archive/issue_comments_077953.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T20:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77953",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077954.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77954",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_077955.json:
```json
{
    "body": "Please see #9589 for doctest failures that may stem from this ticket.",
    "created_at": "2010-07-24T02:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8604#issuecomment-77955",
    "user": "mpatel"
}
```

Please see #9589 for doctest failures that may stem from this ticket.
