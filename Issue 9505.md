# Issue 9505: coeff(f,x*y) does not work

Issue created by migration from https://trac.sagemath.org/ticket/9505

Original creator: zimmerma

Original creation time: 2010-07-15 09:12:14

Assignee: malb

The following is ok:

```
sage: var('x,y,z')
sage: f=x*y*z^2
sage: f.coeff(z^2)
x*y
```

However the following is not:

```
sage: f.coeff(x*y)
0
```



---

Comment by zimmerma created at 2010-07-15 09:12:59

PS: I'm sorry if this is a duplicate. The trac search for "coeff" gives 295 entries!


---

Comment by burcin created at 2010-09-19 15:00:30

Changing keywords from "" to "pynac".


---

Comment by burcin created at 2010-09-19 15:00:30

Changing component from commutative algebra to symbolics.


---

Comment by burcin created at 2010-09-19 15:00:30

Changing assignee from malb to burcin.


---

Comment by burcin created at 2010-09-19 15:00:30

I'm switching the component to `symbolics` since the problem involves symbolic expressions.

It seems that we inherited this behavior from GiNaC:


```
ginsh - GiNaC Interactive Shell (ginac V1.5.7)
  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz,
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.
  ._) i N a C | You are welcome to redistribute it under certain conditions.
<-------------' For details type `warranty;'.

Type ?? for a list of help topics.
> f = x*y*z^2;
y*z^2*x
> coeff(f, z^2,1);
y*x
> coeff(f, x*y,1);
0
```


I will report this to the ginac-list.


---

Comment by was created at 2012-03-21 18:34:34

Since I don't know how to fix this, at least I can point out some related facts.

Maxima does exactly the same thing as GINAC (and Sage):

```
sage: !maxima
;;; Loading #P"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/sb-bsd-sockets.fas"
;;; Loading #P"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/sockets.fas"
;;; Loading #P"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/defsystem.fas"
;;; Loading #P"/Users/wstein/sage/install/sage-5.0.beta2/local/lib/ecl/cmp.fas"
Maxima 5.24.0 http://maxima.sourceforge.net
using Lisp ECL 11.1.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) f : x*y*z;
(%o1)                                x y z
(%i2) coeff(f, x);
(%o2)                                 y z
(%i3) coeff(f, x*y);
(%o3)                                  0
```


Maple raises an error in this case:

```
> f := x*y*z 
> ;
                                                                     f := x y z

> coeff(f, x);
                                                                         y z

> coeff(f, x*y);
Error, invalid input: coeff received x*y, which is not valid for its 2nd argument, x
```


Mathematica does what you expect:

```
In[1]:= f := x*y*z;

In[2]:= Coefficient[f,x] 

Out[2]= y z

In[3]:= Coefficient[f,x*y]

Out[3]= z
```


Sage multivariate polynomials (hence Singular) do what you expect:


```
sage: R.<x,y,z>=QQ[]
sage: f = x*y*z^2
sage: f.coefficient(x)
y*z^2
sage: f.coefficient(x*y)
z^2
```



---

Comment by zimmerma created at 2012-03-26 15:36:28

a possible fix would be that `f.coeff(x<sup>n*y</sup>m)` automatically calls
`f.coeff(x,n).coeff(y,m)` which gives the expected answer:

```
sage: var('x,y,z')
(x, y, z)
sage: f=x*y*z^2
sage: f.coeff(x,1).coeff(y,1)
z^2
```

Paul


---

Comment by burcin created at 2012-03-26 16:01:53

We might need to expand the expression before doing recursive calls to `coefficient()`:


```
sage: var('x,y,z')
(x, y, z)
sage: g = x*y*(z^2 + y*z)
sage: g.coeff(x,1).coeff(y,1)
z
```


Compare to MMA:


```
In[12]:= Coefficient[x*y*(z^2 + y*z), x*y]

          2
Out[12]= z

```



---

Attachment

attached is a temporary fix that calls coeff in turn for each term `x^n` in `s`.
In addition it checks the extra argument `n` is only used for a single symbol.

Paul


---

Comment by zimmerma created at 2013-08-23 13:00:11

Changing status from new to needs_review.


---

Comment by rws created at 2014-02-17 15:58:56

Changing status from needs_review to positive_review.


---

Comment by rws created at 2014-02-17 15:58:56

Patch applies cleanly, looks good, tests OK in symbolics/

Not sure if the stopgap is still necessary. My tests were satisfying but hey.
----
New commits:


---

Comment by git created at 2014-02-20 17:26:42

Changing status from positive_review to needs_review.


---

Comment by git created at 2014-02-20 17:26:42

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by rws created at 2014-02-20 17:46:07

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-21 11:26:46

Documentation does not build

```
[calculus ] docstring of sage.symbolic.expression.Expression.coeff:57: WARNING: Literal block expected; none found.
[calculus ] docstring of sage.symbolic.expression.Expression.coeff:57: WARNING: Literal block expected; none found.
Traceback (most recent call last):
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/builder.py", line 83, in f
    execfile(sys.argv[0])
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py", line 185, in <module>
    sphinx.cmdline.main(sys.argv)
  File "/home/buildslave-sage/slave/sage_git/build/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/cmdline.py", line 206, in main
    print >>error
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py", line 165, in write
    self._write(str)
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py", line 139, in _write
    self._log_line(line)
  File "/home/buildslave-sage/slave/sage_git/build/src/doc/common/custom-sphinx-build.py", line 108, in _log_line
    raise OSError(line)
OSError: [calculus ] docstring of sage.symbolic.expression.Expression.coeff:57: WARNING: Literal block expected; none found.
```



---

Comment by zimmerma created at 2014-02-21 13:04:18

sorry with the change to git I don't know how yet how to submit a patch, thus I won't be able to work on this in the near future.

Paul


---

Comment by git created at 2014-02-21 15:05:45

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by git created at 2014-02-21 15:05:45

Changing status from positive_review to needs_review.


---

Comment by rws created at 2014-02-21 15:06:48

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-22 06:45:52

Resolution: fixed
