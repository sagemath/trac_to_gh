# Issue 4333: bernoulli_python doesn't work

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-10-21 02:18:19

Assignee: was

Keywords: bernoulli

I was considering adding doctests to sage/rings/bernoulli.py and discovered that the code has probably not been used much and is broken.  For example, bernoulli_python gives different answers starting from the 28th Bernoulli number, and returns errors for some small positive integers (such as 2 and 4).  For example:


```
q = 28
print bernoulli(q, algorithm='gap')   
print bernoulli(q, algorithm='gp')
print bernoulli(q, algorithm='pari')    
print bernoulli(q, algorithm='python')
print bernoulli(q, algorithm='bernmm')

-23749461029/870
-23749461029/870
-23749461029/870
-818946929/30
-23749461029/870
```


It seems like it would be easiest to delete this file.


---

Comment by mhampton created at 2008-10-22 16:03:12

Changing assignee from was to mhampton.


---

Attachment

based against 3.2 alpha0


---

Comment by mhampton created at 2008-10-22 19:06:13

The patch removes the file bernoulli.py entirely, since it is broken and redundant, and removes the corresponding option from the bernoulli function in rings/arith.py.

I also added some long tests.  I noticed, but did not fix, a problem with the GAP version of bernoulli, that affects computations of B_{2256} and higher:

```
sage: bernoulli(2256, algorithm = 'gap')

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mh/sagetest-notebook/worksheets/admin/65/code/18.py", line 7, in <module>
    bernoulli(_sage_const_2256 , algorithm = \u0027gap\u0027)
  File "/Volumes/D/sage-3.1.3/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/Volumes/D/sage-3.1.3/local/lib/python2.5/site-packages/sage/rings/arith.py", line 212, in bernoulli
    return Rational(x)
  File "rational.pyx", line 189, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:4035)
  File "rational.pyx", line 284, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4742)
  File "/Volumes/D/sage-3.1.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1533, in _rational_
    return sage.rings.all.Rational(repr(self))
  File "rational.pyx", line 189, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:4035)
  File "rational.pyx", line 280, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4708)
TypeError: unable to convert <<an integer too large to be printed>>/14828319870 to a rational

```



---

Comment by was created at 2008-10-24 03:19:16

Looks good and breaks no doctests.


---

Comment by mabshoff created at 2008-10-26 00:49:01

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 00:49:01

Merged in Sage 3.2.alpha1
