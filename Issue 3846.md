# Issue 3846: bug in the sage preparser -- vector(v)[3] = 5 slips by!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-14 03:35:27

Assignee: cwitty

CC:  robertwb boothby

The Sage preparser stupidly doesn't raise an error when the input is `vector(v)[3] = 5`.  Instead
it does something very confusing.    This was found by Franco Saliola.


```
sage: vector(v)[3] = 5
sage: preparse('vector(v)[3] = 5')
'_=var("v");vector=symbolic_expression(Integer(5)).function(v)'
sage: vector(10)
5
```



---

Comment by was created at 2008-08-14 03:36:05

Here's another funny example:

```
sage: foo(x,y)hithere fred wuz up?!  how is going = x+y
sage: foo(2,3)
5
```



---

Comment by mabshoff created at 2009-02-11 07:57:17

I can no longer reproduce this example in Sage 3.3.rc0. Can someone decide what needs to happen with this bug?

Cheers,

Michael


---

Comment by mhansen created at 2009-06-04 23:08:11

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 23:08:11

This looks fixed to me in 4.0.1:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 'vector(v)[Integer(3)] = Integer(5)'
'vector(v)[Integer(3)] = Integer(5)'
sage: sage: foo(x,y)hithere fred wuz up?!  how is going = x+y
------------------------------------------------------------
   File "<ipython console>", line 1
     foo(x,y)hithere fred wuz up?!  how is going = x+y
                   ^
SyntaxError: invalid syntax
| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |
| Type notebook() for the GUI, and license() for information.        |
```

