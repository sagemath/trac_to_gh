# Issue 2387: Create a _sage_init_ function for all objects

Issue created by migration from https://trac.sagemath.org/ticket/2387

Original creator: jason

Original creation time: 2008-03-04 20:45:45

Assignee: was

Create a _sage_init_ function that behaves like the _maxima_init_, _magma_init_, etc., functions which returns a string sufficient to construct the given object in Sage.

For example:


```
sage: a=matrix([[1,2,3],[4,5,6],[7,8,9]])
sage: a._sage_init_
'matrix([[1,2,3],[4,5,6],[7,8,9]])'
```




---

Comment by jason created at 2008-03-05 19:07:57

I've posted a stab at it by searching for _magma_init_ functions and implementing _sage_init_ next to it for most cases.

How should we deal with:


```
sage: R.<y>=ZZ[]                                           
sage: a=matrix(R, [[y,1],[1,y^2]])                         
sage: a._sage_init_()                                      
"matrix(PolynomialRing(ZZ, 'y'), [[y, 1], [1, y^2]])"
```


The string returned will not construct the object usually since y is not a variable in a new session.  However, putting in the parent of y would make things much uglier.  How would you handle this situation?


---

Attachment

Also, there aren't any doctests...I'll be adding those.  If anyone wants to comment on something I did, please do so!  I'm not very familiar with the coercion system and did the above mainly by searching for _magma_init_ and copying where it made sense.


---

Comment by was created at 2008-03-05 23:12:25

> However, putting in the parent of y would make things much 
> uglier. How would you handle this situation?

I don't think it is possible without changing _sage_init_'s protocol
as suggested by carl witty (either allow a sequence of semicolon separated statements or have two blocks, an initialization block and a eval block).  I think I prefer the latter solution, since it can be used to do the former and more, but not conversely.


---

Comment by craigcitro created at 2008-06-20 04:44:12

Changing keywords from "" to "editor_wstein".


---

Comment by mabshoff created at 2008-08-25 19:34:57

Resolution: wontfix


---

Comment by mabshoff created at 2008-08-25 19:34:57

Closed as wontfix due to #3484 and #3485.

```
[12:29pm] jason-: mabshoff_, cwitty: I believe that 3484 and 3485 make 2387 obsolete.  Comments?
[12:29pm] mabshoff_: let me check
[12:29pm] jason-: (it's the sage_input stuff; I made a simple sage_init patch a long time ago)
[12:30pm] cwitty: I agree.
[12:30pm] mabshoff_: Ok, let's close it as "wontfix" then.
[12:30pm] mabshoff_: objections?
[12:30pm] You are now known as mabshoff.
[12:31pm] jason-: hehe, *another* ticket that is < 0.61*(current ticket number) down!
```


Cheers,

Michael
