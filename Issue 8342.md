# Issue 8342: Efficient Arbitrary Sequence Generator

archive/issues_008342.json:
```json
{
    "body": "Assignee: jkantor\n\nKeywords: sequence, generator\n\n```\ndef construct_sequence(base,f):\n    \"\"\"\n    Returns a function that gives sequence terms, building off past calls.\n    \n    Input:\n       - `base` -- the base case(s) of the sequence.\n       - `f`    -- the recursive description of the sequence; it takes a sequence referencing function and returns a function that will, given n, return the nth term.\n\n    Output:\n       A function that, given n, returns the nth term in the sequence.\n    \n    Examples:\n       sage: fib = construct_sequence([1,1], lambda t: lambda n : t(n-1) + t(n-2)) #The Fibonacci sequence\n\n       sage: hof = construct_sequence([1,1], lambda t: lambda n : t(n-t(n-1)) + t(n-t(n-2))) #The Hofstadter Q sequence\n       sage: [hof(n) for n in range(100)] # List of 100 terms\n    \"\"\"\n    b = {}\n    for i in range(len(base)):\n        b[i] = base[i]\n    def get_term(n):\n        if n in b.keys(): return b[n]\n        else:\n            b[n] = f(get_term)(n)\n            return b[n]\n    return get_term\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8342\n\n",
    "created_at": "2010-02-24T01:41:50Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Efficient Arbitrary Sequence Generator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8342",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```
Assignee: jkantor

Keywords: sequence, generator

```
def construct_sequence(base,f):
    """
    Returns a function that gives sequence terms, building off past calls.
    
    Input:
       - `base` -- the base case(s) of the sequence.
       - `f`    -- the recursive description of the sequence; it takes a sequence referencing function and returns a function that will, given n, return the nth term.

    Output:
       A function that, given n, returns the nth term in the sequence.
    
    Examples:
       sage: fib = construct_sequence([1,1], lambda t: lambda n : t(n-1) + t(n-2)) #The Fibonacci sequence

       sage: hof = construct_sequence([1,1], lambda t: lambda n : t(n-t(n-1)) + t(n-t(n-2))) #The Hofstadter Q sequence
       sage: [hof(n) for n in range(100)] # List of 100 terms
    """
    b = {}
    for i in range(len(base)):
        b[i] = base[i]
    def get_term(n):
        if n in b.keys(): return b[n]
        else:
            b[n] = f(get_term)(n)
            return b[n]
    return get_term
```


Issue created by migration from https://trac.sagemath.org/ticket/8342





---

archive/issue_comments_074334.json:
```json
{
    "body": "Changing assignee from jkantor to colah.",
    "created_at": "2010-02-24T03:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74334",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```

Changing assignee from jkantor to colah.



---

archive/issue_comments_074335.json:
```json
{
    "body": "You need to upload a patch. As it now stands, I cannot work out how you want to integrate your implementation into the Sage library. See [this section](http://www.sagemath.org/doc/developer/trac.html) of the Developer's Guide for more information.",
    "created_at": "2010-02-24T09:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

You need to upload a patch. As it now stands, I cannot work out how you want to integrate your implementation into the Sage library. See [this section](http://www.sagemath.org/doc/developer/trac.html) of the Developer's Guide for more information.



---

archive/issue_comments_074336.json:
```json
{
    "body": "Adds the construct_sequence function.",
    "created_at": "2010-03-14T06:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74336",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```

Adds the construct_sequence function.



---

archive/issue_comments_074337.json:
```json
{
    "body": "Attachment [construct_sequence.patch](tarball://root/attachments/some-uuid/ticket8342/construct_sequence.patch) by colah created at 2010-03-14 06:05:57",
    "created_at": "2010-03-14T06:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74337",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```

Attachment [construct_sequence.patch](tarball://root/attachments/some-uuid/ticket8342/construct_sequence.patch) by colah created at 2010-03-14 06:05:57



---

archive/issue_comments_074338.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-14T06:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74338",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074339.json:
```json
{
    "body": "Why does this function use a dictionary instead of a list? Is it done for functions that can get values for \"large\" n without computing all of the previous?\n\nSince it does use a dictionary, why does it assume ``base`` to be like [a_0, a_1, a_2]? It seems to me that it would be more reasonable then to take a dictionary as  ``base`` in case I want to give [a_1, a_2, a_3] or [a_{-2}, a_0] or even [entry_{\"a\"}, entry_{\"b\"}]. That would allow even for multidimensional sequences indexed by tuples!\n\nThe documentation is not quite clear to me. I don't understand what exactly does the description of ``f`` mean and I think that while lambda-form is probably the way to use this function (so the included examples must stay), it would be nice if examples were also written in an \"expanded\" way with each internal function having a meaningful name and some explanation what exactly should it take as an argument and what should it return. I didn't understand how to use this function until I looked at the source code.\n\nFinally, the examples test only that the function does not crush. There should be comparison with expected output. E.g. show that it is possible to compute Fibonacci numbers that were not given as input and that actually even required computing some intermediate ones!\n\nAs a possible improvement to consider (but I don't know if it should be done): what about admissible indices? What is the (-10)-th Fibonacci number? Infinite recursion? Maybe there should an optional parameter for a function that will check that there exists the corresponding element. And maybe there can be some way to see which values are already computed to determine if they will be enough to evaluate the new one or in case when it is possible to use several ways.",
    "created_at": "2010-03-14T17:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74339",
    "user": "https://github.com/novoselt"
}
```

Why does this function use a dictionary instead of a list? Is it done for functions that can get values for "large" n without computing all of the previous?

Since it does use a dictionary, why does it assume ``base`` to be like [a_0, a_1, a_2]? It seems to me that it would be more reasonable then to take a dictionary as  ``base`` in case I want to give [a_1, a_2, a_3] or [a_{-2}, a_0] or even [entry_{"a"}, entry_{"b"}]. That would allow even for multidimensional sequences indexed by tuples!

The documentation is not quite clear to me. I don't understand what exactly does the description of ``f`` mean and I think that while lambda-form is probably the way to use this function (so the included examples must stay), it would be nice if examples were also written in an "expanded" way with each internal function having a meaningful name and some explanation what exactly should it take as an argument and what should it return. I didn't understand how to use this function until I looked at the source code.

Finally, the examples test only that the function does not crush. There should be comparison with expected output. E.g. show that it is possible to compute Fibonacci numbers that were not given as input and that actually even required computing some intermediate ones!

As a possible improvement to consider (but I don't know if it should be done): what about admissible indices? What is the (-10)-th Fibonacci number? Infinite recursion? Maybe there should an optional parameter for a function that will check that there exists the corresponding element. And maybe there can be some way to see which values are already computed to determine if they will be enough to evaluate the new one or in case when it is possible to use several ways.



---

archive/issue_comments_074340.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-14T17:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74340",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074341.json:
```json
{
    "body": "> Why does this function use a dictionary instead of a list? Is it done for functions that can get values for \"large\" n without computing all of the previous?\n\n\nSparseness. Some sequences jump around... a lot. I have no clue how you could write an implementation using a list: you'd need to calculate the terms in order which is often not possible!\n\n> Since it does use a dictionary, why does it assume base to be like [a_0, a_1, a_2]? It seems to me that it would be more reasonable then to take a dictionary as base in case I want to give [a_1, a_2, a_3] or [a_{-2}, a_0] or even [entry_{\"a\"}, entry_{\"b\"}]. That would allow even for multidimensional sequences indexed by tuples!\n\n\nThis is perhaps a poor design choice. I'll make it so you can give _either_ a list of dictionary. My thought was that writing {0:1,1:1} was more tedious than [1,1]. Convenience is its own quality.\n\n> The documentation is not quite clear to me. I don't understand what exactly does the description of f mean and I think that while lambda-form is probably the way to use this function (so the included examples must stay), it would be nice if examples were also written in an \"expanded\" way with each internal function having a meaningful name and some explanation what exactly should it take as an argument and what should it return. I didn't understand how to use this function until I looked at the source code.\n\n\nOK. I'll try to make this more clear.\n\n> Finally, the examples test only that the function does not crush. There should be comparison with expected output. E.g. show that it is possible to compute Fibonacci numbers that were not given as input and that actually even required computing some intermediate ones!\n\n\nYou mean like:\n\nsage: fib = construct_sequence([1,1],lambda t: lambda n: t(n-1)+t(n-2) )\nsage: [fib(n) for n in range(50)]\n[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]\n\n\n> As a possible improvement to consider (but I don't know if it should be done): what about admissible indices?\n\n\nDepends on the sequence, ideally.\n\n> What is the (-10)-th Fibonacci number? Infinite recursion? Maybe there should an optional parameter for a function that will check that there exists the corresponding element.\n\n\nIt isn't possible to tell from the function. Testing whether a function will necessarily exit from its definition is NP. We could have an option to give the sequences domain. One nice thing about the dictionary is the flexibility it gives: the index could be reals, or just about anything else.\n\n> And maybe there can be some way to see which values are already computed to determine if they will be enough to evaluate the new one or in case when it is possible to use several ways.\n\n\nSee above.",
    "created_at": "2010-03-17T00:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74341",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```

> Why does this function use a dictionary instead of a list? Is it done for functions that can get values for "large" n without computing all of the previous?


Sparseness. Some sequences jump around... a lot. I have no clue how you could write an implementation using a list: you'd need to calculate the terms in order which is often not possible!

> Since it does use a dictionary, why does it assume base to be like [a_0, a_1, a_2]? It seems to me that it would be more reasonable then to take a dictionary as base in case I want to give [a_1, a_2, a_3] or [a_{-2}, a_0] or even [entry_{"a"}, entry_{"b"}]. That would allow even for multidimensional sequences indexed by tuples!


This is perhaps a poor design choice. I'll make it so you can give _either_ a list of dictionary. My thought was that writing {0:1,1:1} was more tedious than [1,1]. Convenience is its own quality.

> The documentation is not quite clear to me. I don't understand what exactly does the description of f mean and I think that while lambda-form is probably the way to use this function (so the included examples must stay), it would be nice if examples were also written in an "expanded" way with each internal function having a meaningful name and some explanation what exactly should it take as an argument and what should it return. I didn't understand how to use this function until I looked at the source code.


OK. I'll try to make this more clear.

> Finally, the examples test only that the function does not crush. There should be comparison with expected output. E.g. show that it is possible to compute Fibonacci numbers that were not given as input and that actually even required computing some intermediate ones!


You mean like:

sage: fib = construct_sequence([1,1],lambda t: lambda n: t(n-1)+t(n-2) )
sage: [fib(n) for n in range(50)]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]


> As a possible improvement to consider (but I don't know if it should be done): what about admissible indices?


Depends on the sequence, ideally.

> What is the (-10)-th Fibonacci number? Infinite recursion? Maybe there should an optional parameter for a function that will check that there exists the corresponding element.


It isn't possible to tell from the function. Testing whether a function will necessarily exit from its definition is NP. We could have an option to give the sequences domain. One nice thing about the dictionary is the flexibility it gives: the index could be reals, or just about anything else.

> And maybe there can be some way to see which values are already computed to determine if they will be enough to evaluate the new one or in case when it is possible to use several ways.


See above.



---

archive/issue_comments_074342.json:
```json
{
    "body": "Is there any interest in continuing work on this ticket?..",
    "created_at": "2011-08-03T19:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74342",
    "user": "https://github.com/novoselt"
}
```

Is there any interest in continuing work on this ticket?..



---

archive/issue_comments_074343.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-08-03T19:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74343",
    "user": "https://github.com/novoselt"
}
```

Changing priority from major to minor.



---

archive/issue_events_019983.json:
```json
{
    "actor": "https://github.com/novoselt",
    "created_at": "2011-08-03T19:41:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8342#event-19983"
}
```



---

archive/issue_comments_074344.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-03-15T18:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74344",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_019984.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2014-03-15T18:57:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8342#event-19984"
}
```



---

archive/issue_events_019985.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2014-03-15T18:57:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8342#event-19985"
}
```



---

archive/issue_comments_074345.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-17T18:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74345",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019986.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-03-19T04:42:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8342#event-19986"
}
```



---

archive/issue_comments_074346.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-03-19T04:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8342#issuecomment-74346",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid
