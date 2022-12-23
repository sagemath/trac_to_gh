# Issue 3704: diagonal_matrix does not accept vectors

Issue created by migration from https://trac.sagemath.org/ticket/3704

Original creator: jkantor

Original creation time: 2008-07-22 04:35:52

Assignee: was

So I think this is a bug 

```
sage: w=vector(RR,[1,2,3])
sage: d=diagonal_matrix(w)
UnboundLocalError: local variable 'v' referenced before assignment
```

The following fails as well

```
sage: d=diagonal_matrix(RR,w) 
```

the only thing that works is 

```
sage: d=diagonal_matrix(RR,list(w))
```

A stupid but easy fix is to try to turn any argument to diagonal_matrix into a list before bailing out (its in matrix/constructor.py), but there should probably be logic actually expecting vectors and analyzing the parents?


---

Comment by jason created at 2008-07-22 14:52:58

Would it be easy as taking the argument to diagonal_matrix and sending it through Sequence?

```
sage: v=vector(QQ,[1,2,3/4])
sage: v
(1, 2, 3/4)
sage: b=diagonal_matrix(Sequence(v)); b

[  1   0   0]
[  0   2   0]
[  0   0 3/4]
sage: b.parent()
Full MatrixSpace of 3 by 3 dense matrices over Rational Field
```



---

Comment by jason created at 2008-07-22 16:37:39

Changing priority from minor to major.


---

Comment by jason created at 2008-07-22 16:37:39

The attached patch is a complete rewrite of diagonal_matrix which now does the following:

1. If the first argument is a ring, pop it off the argument list
2. If the next thing can be made into a Sequence, do so and use those elements as the diagonal elements.  If the next thing cannot be made into a sequence, then take the remainder of the argument list and use those things as the diagonal elements.
3. Prepend the ring if one was specified and send everything to the matrix() function.

This changes the syntax slightly; in order to get a matrix of a specific size, you need to pass an nrows and/or ncols option.  But it is very nice in that it allows diagonal_matrix(1,2,3) or, as mentioned in this ticket, diagonal_matrix(v) where v is a vector.

All doctests in sage/matrix/* pass and all doctests elsewhere that I found using diagonal_matrix also pass.


---

Comment by jason created at 2008-07-22 16:37:50

Changing type from defect to enhancement.


---

Comment by jason created at 2008-07-22 16:38:13

I guess it really is a defect, as pointed about above; there is a bug that is fixed.


---

Comment by jason created at 2008-07-22 16:38:13

Changing type from enhancement to defect.


---

Comment by cremona created at 2008-07-29 01:58:01

I generally like this patch, and it provides useful functionality.

I applied th patch to 3.0.4 with no problem and all tests in
sage/matrix pass.

Two things seemed strange to me:

    1. I cannot see a reason for the provided facility for padding
    with zeros when nrows is given explicitly.  I just cannot think of
    a time when anyone would need this!

    2. The example  diagonal_matrix(GF(2),GF(5))  is really crazy.
    [It returns a diagonal matrix of size 5 and entries 0,1,0,1,0,
    using a list of the elements of GF(5) coerced into GF(2)!]

    This is surely a weird side-effect rather than a useful example.
    the same result would come from diagonal_matrix(GF(2),range(5))
    which is a little more sane.

That last example would not even work if it were not possible to
coerce from GF(5) to GF(2).  And I really think that should not be
possible.  Does it still happen in the "new coercion model", I wonder?


---

Comment by robertwb created at 2008-07-29 08:41:19

The patch looks mostly good, but I heartily agree with points (1) and (2). Also, the following gives an undesired result: 


```
sage: diagonal_matrix(x^3+3, x+1)
```


If a ring is specified, it is converted even if there is no coercion. This allows stuff like


```
sage: matrix(GF(101), 2, [1, 1/2, 1/3, 1/4])
[ 1 51]
[34 76]
```


despite there being no coercion QQ -> GF(101).


---

Comment by robertwb created at 2008-07-29 08:42:27

The patch looks mostly good, but I heartily agree with points (1) and (2). Also, the following gives an undesired result: 


```
sage: diagonal_matrix(x^3+3, x+1)
```


If a ring is specified, it is converted even if there is no coercion. This allows stuff like


```
sage: matrix(GF(101), 2, [1, 1/2, 1/3, 1/4])
[ 1 51]
[34 76]
```


despite there being no coercion QQ -> GF(101).


---

Comment by jason created at 2008-07-30 09:33:11

Thanks for the feedback!  I'm at a conference now, so I won't have time to address point 2 for a few days.  However, to address point 1: the previous version of diagonal_matrix allowed for the rows to be specified and padded with zeros.  I was providing an example which showed how to achieve this effect.  Basically, I'm also showing that behavior is like the matrix() command (to which I am just blindly passing all keyword arguments, except for some special behavior about the sparse keyword).  So: the behavior is a result of the behavior of matrix() and shows how to achieve a former behavior of diagonal_matrix.  Whether or not it is actually useful is another issue: if anyone did use this feature, though, it might be nice to have an example of how to do it with the new diagonal_matrix.

I also agree that coercion should play a role, as pointed out in point 2.  I'll look at that early next week, hopefully.

Thanks again!


---

Comment by jason created at 2008-08-02 14:41:45

Okay, with the example: 

```
sage: matrix(GF(101), 2, [1, 1/2, 1/3, 1/4])
[ 1 51]
[34 76]
```

that comes from `GF(101)(1/2)` giving 51, etc.  I just hand it off to the matrix() constructor, which in turn hands the job off to the MatrixSpace constructor.

As to another point, I get:

```
sage: diagonal_matrix(x^3+3, x+1)

[x^3 + 3       0]
[      0   x + 1]
```

so with x being a symbolic variable, things work fine.

However, if we have an iterable object, then things are not so good.  In that case, the patch tries to construct a Sequence object from the iterable object, which is where you get your weird results.

I'm changing the patch so that if a list or tuple is passed in, then it tries to construct Sequence object from that list or tuple.  Note that this is only for backwards-compatibility, so we can still pass a list into diagonal_matrix and have it return what it used to return.


---

Attachment

Okay, new patch is up which should take of the issues in my previous post.


---

Comment by cremona created at 2008-08-09 16:34:56

I successfully applied the patch to 3.1.alpha0 and all seems to work as advertised.  All tests in sage.matrix pass.  Publish!


---

Comment by mabshoff created at 2008-08-11 00:43:19

Patches at #2577 seem to do something very close to this patch, so someone ought to sort out if there are any differences that could be resolved into one unified patch.

Cheers,

Michael


---

Comment by jason created at 2008-08-15 23:38:40

I looked at the patch at #2577 and like the patch here better.  I can't see any extra functionality in #2577 that I would want to merge to this patch, but I'm open to suggestions.


---

Attachment

I just added a patch, to be applied on top of the first patch, which does two things:

1. Makes a trivial simplification in the code

2. Adds a doctest illustrating the sparse keyword.


---

Comment by mabshoff created at 2008-09-02 11:26:15

Hmm, can we sort out this mess, i.e. what to do about #2577? The consensus seems to be to merge theses patches and close #2577?

An final positive review will also be good since Jason did add a second patch.

Cheers,

Michael


---

Attachment


---

Comment by cremona created at 2008-09-02 12:01:44

Let's agree to kill #2577 since it does nothing which these patches do not do, and these are now a lot better.

I applied both patches to 3.1.2.alpha3 with no problems.  All the above examples now work and give sensible answers.  They are not all included as doctests though.

I hit a doctest error in sage/matrix/matrix_integer_dense_hnf.py:

```
sage -t  devel/sage/sage/matrix/matrix_integer_dense_hnf.py **********************************************************************
File "/home/john/sage-3.1.2.alpha3/tmp/matrix_integer_dense_hnf.py", line 132:
    sage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[17]>", line 1, in <module>
        m = diagonal_matrix(ZZ, Integer(68), [Integer(2)]*Integer(66) + [Integer(1),Integer(1)])###line 132:
    sage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py", line 736, in diagonal_matrix
        return matrix(*args, **kwds)
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py", line 524, in matrix
        entries, entry_ring = prepare_dict(args[0])
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py", line 619, in prepare_dict
        entries, ring = prepare(X)
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py", line 613, in prepare
        raise TypeError, "unable to find a common ring for all elements"
    TypeError: unable to find a common ring for all elements
```

This is trivial to fix, and I added a trivial patch which fixes it.

Conclusion:  kill #2577 and merge this one (all three patches).  I assume mabshoff can take on the responsibility of reviewing the final mini-patch!


---

Attachment

PS Forgot to add that doctest: 4th patch does that too.


---

Comment by mhansen created at 2008-09-02 23:28:50

Is there a reason that we got rid of this construction?


```
 	        4. matrix(ring, nrows, diagonal_entries, [sparse=True]): 
	               matrix with given number of rows and flat list of entries  
```


It should at least be deprecated first.


---

Comment by cremona created at 2008-09-03 08:29:14

There was exactly one doctest which stopped working with that construction missing, and the fix was just to delete the nrows parameter.

I don't have strong feelings about deprecating things like this.  I think the point of having nrows in there was so that diagonal_entries could be shorter than nrows and then would be padded out by zeroes.  I feel happier requiring the user to provide the whole list of diagonal entries, but if someone wants to put this construction back I don't mind either.


---

Comment by mabshoff created at 2008-09-19 03:30:05

There was some extended discussion on sage-devel and the consensus is that the new non-list constructor will break if more than 255 elements are passed. So this needs work :)

Cheers,

Michael


---

Comment by rlm created at 2009-01-23 12:40:18

I'm attaching a new patch which takes a much lower level approach to solving the problem. If a complete rewrite is really necessary, I propose we open a new ticket for it, since this ticket is just about constructing a diagonal matrix from a vector.


---

Attachment

Independent of the other patches found here.


---

Comment by jason created at 2009-01-27 03:55:24

Positive review for rlm's patch.  It fixes the problem mentioned in the ticket.  The new ticket rlm mentioned is #5110.


---

Comment by jason created at 2009-01-27 03:55:56

(because of #5110, do not delete the other patches on this ticket.)


---

Comment by mabshoff created at 2009-01-28 14:12:34

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 14:12:34

Merged trac-3704.patch only in Sage 3.3.alpha3.

Cheers,

Michael
