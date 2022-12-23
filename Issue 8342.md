# Issue 8342: Efficient Arbitrary Sequence Generator

Issue created by migration from https://trac.sagemath.org/ticket/8342

Original creator: colah

Original creation time: 2010-02-24 01:41:50

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




---

Comment by colah created at 2010-02-24 03:29:17

Changing assignee from jkantor to colah.


---

Comment by mvngu created at 2010-02-24 09:20:36

You need to upload a patch. As it now stands, I cannot work out how you want to integrate your implementation into the Sage library. See [this section](http://www.sagemath.org/doc/developer/trac.html) of the Developer's Guide for more information.


---

Comment by colah created at 2010-03-14 06:05:35

Adds the construct_sequence function.


---

Attachment


---

Comment by colah created at 2010-03-14 06:05:57

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-03-14 17:29:59

Why does this function use a dictionary instead of a list? Is it done for functions that can get values for "large" n without computing all of the previous?

Since it does use a dictionary, why does it assume ``base`` to be like [a_0, a_1, a_2]? It seems to me that it would be more reasonable then to take a dictionary as  ``base`` in case I want to give [a_1, a_2, a_3] or [a_{-2}, a_0] or even [entry_{"a"}, entry_{"b"}]. That would allow even for multidimensional sequences indexed by tuples!

The documentation is not quite clear to me. I don't understand what exactly does the description of ``f`` mean and I think that while lambda-form is probably the way to use this function (so the included examples must stay), it would be nice if examples were also written in an "expanded" way with each internal function having a meaningful name and some explanation what exactly should it take as an argument and what should it return. I didn't understand how to use this function until I looked at the source code.

Finally, the examples test only that the function does not crush. There should be comparison with expected output. E.g. show that it is possible to compute Fibonacci numbers that were not given as input and that actually even required computing some intermediate ones!

As a possible improvement to consider (but I don't know if it should be done): what about admissible indices? What is the (-10)-th Fibonacci number? Infinite recursion? Maybe there should an optional parameter for a function that will check that there exists the corresponding element. And maybe there can be some way to see which values are already computed to determine if they will be enough to evaluate the new one or in case when it is possible to use several ways.


---

Comment by novoselt created at 2010-03-14 17:29:59

Changing status from needs_review to needs_work.


---

Comment by colah created at 2010-03-17 00:55:26

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

Comment by novoselt created at 2011-08-03 19:41:44

Is there any interest in continuing work on this ticket?..


---

Comment by novoselt created at 2011-08-03 19:41:44

Changing priority from major to minor.


---

Comment by mmezzarobba created at 2014-03-15 18:57:53

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2014-03-17 18:56:47

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-19 04:42:36

Resolution: invalid
