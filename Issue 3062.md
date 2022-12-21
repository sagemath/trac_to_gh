# Issue 3062: implement __oct__ special method for the integers

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-30 14:35:57

Assignee: somebody


```
>  oct(2345) fails in Sage (but works in Python)
>  oct(int(2345)) works
>  hex(2345) works
>  
>  Irc said it was the preparser. Why would the input of oct be preparsed
>  correctly and not that of hex ?

I think you asked this question backwards.  Anyway, the problem
is that nobody implemented __oct__ for Sage integers, but they
did implement __hex__.  Note that oct(...) calls __oct__:

sage: a = 2345
sage: a.__hex__()
'929'
sage: a.__oct__()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.integer.Integer' object has no attribute '__oct__'

In the meantime you can do either

sage: oct(int(a))
'04451'

or

sage: a.digits(8)
[1, 5, 4, 4]

or

sage: a.str(base=8)
'4451'
```



---

Comment by dmharvey created at 2008-05-01 05:32:56

Code looks okay to me but the documentation could do with improvement. "Numerial" is not a word. Also I'd like some explanation that the behaviour is *different* from the behaviour on python ints and doctests illustrating the difference, since this is likely to be confusing (i.e. for python ints you get a prepended 0, but not for sage ints). See the documentation of `Integer.__hex__` for an example. Also I want to see an example with negative numbers.


---

Comment by TimothyClemans created at 2008-05-01 05:44:25

Improved documentation per David's review.


---

Comment by dmharvey created at 2008-05-01 05:52:09

Tim, there are still no examples showing what happens with plain python ints. I mean like


```
sage: oct(int(10))
'012'
```


vs oct(Integer(10))


---

Comment by TimothyClemans created at 2008-05-01 06:03:50

Added examples showing difference between int and Integer oct behavior per David's request.


---

Comment by dmharvey created at 2008-05-01 06:10:47

Tim... I don't understand now why you have *two* EXAMPLES blocks, and moreover one of them is contained inside the latex \note block! Why not just keep it simple? Just one block of examples, showing all the key issues, and don't put them inside the latex tags! :-)


---

Attachment


---

Comment by TimothyClemans created at 2008-05-01 06:30:48

Flatten the patches and merged the two example blocks per David's review.


---

Comment by dmharvey created at 2008-05-01 15:30:56

Ok this is fine.

Note to release manager: only apply the last patch (3062_flatten.patch).


---

Comment by mabshoff created at 2008-05-02 12:57:11

Merged in Sage 3.0.1.rc0


---

Comment by mabshoff created at 2008-05-02 12:57:11

Resolution: fixed
