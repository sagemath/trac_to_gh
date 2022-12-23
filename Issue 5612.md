# Issue 5612: docs for solving a system of linear equations symbolically using symbolic matrices

Issue created by migration from https://trac.sagemath.org/ticket/5612

Original creator: jason

Original creation time: 2009-03-25 23:42:55

Assignee: was

This should go into some docs somewhere.  Maybe under solve_right or in a primer?

It's to solve the linear system a*x+b*y=3, c*x+d*y=5.


```
sage: var('a,b,c,d,x,y')
(a, b, c, d, x, y)
sage: A=matrix(2,[a,b,c,d]); A
[a b]
[c d]
sage: result=vector([3,5]); result
(3, 5)
sage: soln=A.solve_right(result) # you could also do soln=A\result
sage: soln
(3/a - b*(5 - 3*c/a)/(a*(d - b*c/a)), (5 - 3*c/a)/(d - b*c/a))


Now, checking our answers:


sage: (a*x+b*y).subs(x=soln[0],y=soln[1]).simplify_full()
3
sage: (c*x+d*y).subs(x=soln[0],y=soln[1]).simplify_full()
5


Or just checking it with matrix multiplication:

sage: A*soln
(a*(3/a - b*(5 - 3*c/a)/(a*(d - b*c/a))) + b*(5 - 3*c/a)/(d - b*c/a), 
c*(3/a - b*(5 - 3*c/a)/(a*(d - b*c/a))) + (5 - 3*c/a)*d/(d - b*c/a))

Let's simplify each entry by applying the "simplify_full" function to 
each entry:

sage: (A*soln).apply_map(lambda x: x.simplify_full())
(3, 5)
```




---

Comment by was created at 2009-03-26 15:22:25

Make sure to change 

```
matrix(2,[a,b,c,d])
vector([3,5])
```


to


```
matrix(SR,2,[a,b,c,d])
vector(SR,[3,5])
```


since otherwise people get really confused when slight changes lead to breakage (e.g., see sage-support).

Also, I'm concerned about the large number of wishlist-style trac tickets you've been creating lately, like this one.  If everybody made tickets like you're doing it about similar things, trac would soon become unusable.


---

Comment by jason created at 2009-03-26 17:43:01

Well, we're told to make a trac ticket for every item, so I'm also using it as a to-do list for when I have a few minutes.  In reality, I just made this a trac ticket because of the specific request on the sage lists; I wasn't planning on making it a trac ticket originally.  When I have a few minutes, I can just go to tickets that I've created, pick one that fits into the time I have, and make a patch.

I can make them all attached to the wishlist milestone, if that's better.

I was going to make all the color items a single ticket, but then I remembered the rebukes I've received about lumping too much together on a ticket...


---

Comment by jason created at 2010-09-03 21:24:29

Changing keywords from "" to "beginner".


---

Comment by JoalHeagney created at 2012-04-12 13:24:37

Guys, when I try this out, I get to the following line and get the following error (both ways):



```
soln=A.solve_right(result) # you could also do soln=A\result
```



```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_15.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("c29sbj1BLnNvbHZlX3JpZ2h0KHJlc3VsdCkgIyB5b3UgY291bGQgYWxzbyBkbyBzb2xuPUFccmVzdWx0"),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpJ1xbYN/___code___.py", line 2, in <module>
    exec compile(u'soln=A.solve_right(result) # you could also do soln=A\\result
  File "", line 1, in <module>
    
  File "matrix2.pyx", line 281, in sage.matrix.matrix2.Matrix.solve_right (sage/matrix/matrix2.c:3796)
  File "ring.pyx", line 835, in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:6410)
NotImplementedError
```


This is in 4.8.

Joal Heagney


---

Attachment

I added the example of symbolic matrix to the doc and fixed the bug reported by Joal Heagney. The error came from is_integral_domain() function in ring.pyx. Since a field is a specific type of integral domain, I just added a if clause.


---

Comment by mmasdeu created at 2012-06-08 16:00:03

Changing assignee from was to mmasdeu.


---

Comment by mmasdeu created at 2012-06-08 16:00:03

Looks good to me. It does what the ticked asked and fixed a bug with SR.


---

Comment by JoalHeagney created at 2012-06-09 04:37:43

Well the patch works fine on the example problems in sage 5.0. Haven't checked to see if it has other consequences elsewhere though.


---

Comment by benjaminfjones created at 2012-07-23 16:32:15

I just ran into the error reported by JoalHeagney while going through some Sage demo worksheets from past talks. This bug must have been introduced sometime after the talk was given because I remember solving symbolic matrix equations just fine. It would be great if this got doctested and into Sage ASAP.


---

Comment by benjaminfjones created at 2012-07-23 16:32:15

Changing status from new to needs_review.


---

Comment by benjaminfjones created at 2012-07-23 16:32:22

Changing status from needs_review to needs_work.


---

Comment by benjaminfjones created at 2012-07-23 16:33:32

Oops, sorry. I saw the doctests in the patch and then promptly forgot about them. The patch looks very good to me. I'll do some more extensive testing and if all looks good, positive review.


---

Comment by benjaminfjones created at 2012-07-23 16:33:32

Changing status from needs_work to needs_review.


---

Comment by benjaminfjones created at 2012-07-23 16:44:58

Changing priority from minor to major.


---

Comment by benjaminfjones created at 2012-07-23 22:13:05

Changing status from needs_review to positive_review.


---

Comment by benjaminfjones created at 2012-07-23 22:13:05

Changing type from enhancement to defect.


---

Comment by benjaminfjones created at 2012-07-23 22:13:05

The patch applies cleanly to 5.2.rc0 and passes all tests. It looks good to go. Thanks for the contribution (and the bug report, Joel).


---

Comment by jdemeyer created at 2012-08-01 12:09:03

Resolution: fixed
