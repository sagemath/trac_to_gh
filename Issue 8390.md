# Issue 8390: Find all roots of a trigonometric equation

Issue created by migration from Trac.

Original creator: olazo

Original creation time: 2010-02-27 19:07:36

Assignee: olazo

CC:  robert.marik kcrisman mhansen

Keywords: trigonometric, roots

When using


```
x,y=var('x,y')
solve([sin(2*x-pi/6)==1/2],x)
```


sage returns [x == 1/6*pi]. Which is correct, but we would wish to have all roots. This can be done with:


```
solve([sin(2*x-pi/6)==y,y==1/2],[x,y])
```


which returns [[x == 1/2*pi + pi*z5, y == (1/2)], [x == 1/6*pi + pi*z7, y == (1/2)]]

But this is a very weird way to do things. Surely solve([sin(2*x-pi/6)==y,y==1/2],[x,y]) should also give all roots.


---

Comment by jason created at 2010-02-27 19:33:45

CCing our maxima experts--this looks like it might be a problem with maxima.


---

Comment by robert.marik created at 2010-02-27 21:08:43

Sage interface for Maxima's solver works like this:

We try Maxima's solve function first. It we get empty answer, we try the to_poly_solve for the same equation.

If the answer is not empty, we pass the answer of solve command to Maxima's to_poly_solve.

For our equation, solve command in Maxima gives only one solution pi/6 (and probably writes something like "SOLVE is using arc-trig functions to get a solution. Some solutions will be lost." on terminal).


```
[marik`@`um-bc107 /opt/sage]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: eq = sin(2*x-pi/6) == 1/2
sage: eq._maxima_().solve(x)
[x=%pi/6]
sage: eq._maxima_().to_poly_solve(x)
%union([x=-(-2*%pi*%z6-%pi)/2],[x=-(-2*%pi*%z8-%pi/3)/2])
sage:
```

| Sage Version 4.3.2, Release Date: 2010-02-06                       |
| Type notebook() for the GUI, and license() for information.        |
I hope this is an explanation. I do not have enough experiences with to_poly_solve, so my questions are: Is it good idea to skip solve and use to_poly_solve immediatelly when to_poly_sole = True? Or is it posssible to check from within Sage, that the warning about arc-trig functions has been printed? Or introduce to_poly_solve = 'force' to omit solve command?

Now you can use 

```
sage: eq._maxima_().to_poly_solve(x).sage()
[[x == 1/2*pi + pi*z16], [x == 1/6*pi + pi*z18]]
```



---

Comment by robert.marik created at 2010-02-28 15:17:23

temporary patch:

```
diff -r 799f70320d89 sage/symbolic/expression.pyx
--- a/sage/symbolic/expression.pyx      Thu Feb 11 09:03:17 2010 -0800
+++ b/sage/symbolic/expression.pyx      Sun Feb 28 16:16:33 2010 +0100
`@``@` -6501,7 +6501,7 `@``@`
         # solutions being returned.                            #
         ########################################################
         if to_poly_solve and not multiplicities:
-            if len(X)==0: # if Maxima's solve gave no solutions, only try it
+            if len(X)==0 or to_poly_solve == 'force': # if Maxima's solve gave no solutions, only try it
                 try:
                     s = m.to_poly_solve(x)
                     T = string_to_list_of_solutions(repr(s))
```


allows this

```
[marik`@`taxus ../sage-4.3.3.alpha0]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: solve(sin(x)==1/2,x)
[x == 1/6*pi]
sage: solve(sin(x)==1/2,x,to_poly_solve = 'force')
[x == 5/6*pi + 2*pi*z8, x == 1/6*pi + 2*pi*z6]
sage:
```



---

Comment by robert.marik created at 2010-02-28 23:42:07

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-02-28 23:42:07

The patch is attached. Code starts at line 6564. The rest is from reindent.py (I got memory error when testing).

The patch introduces option to_poly_solve='force'. Perhaps, could be done automatically in future when invcerse trigonometric functions appear. Needs some coding in Lisp and changes in Maxima, see [Maxima forum](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/29966/focus=29974).


---

Attachment

rebased for Sage 4.3.5


---

Comment by was created at 2010-04-07 14:07:10

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-07 14:07:10

The code looks fine to me. I agree that the interface is not so elegant, since it's somewhat tied to Maxima, and it's uncomfortable to have an input (to_poly_solve) be either bool or string.  However, I can't really think of anything better given the design decisions we've already made. 

All tests pass.


---

Comment by jhpalmieri created at 2010-04-15 20:11:34

Merged trac-8390.patch in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-15 20:11:34

Resolution: fixed
