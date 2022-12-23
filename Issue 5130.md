# Issue 5130: [with patch; not ready for review] create a prime_pi function that doesn't just compute len(prime_range(n))

Issue created by migration from https://trac.sagemath.org/ticket/5130

Original creator: was

Original creation time: 2009-01-29 21:41:56

Assignee: was

The goal of this ticket is to make something eventually competitive with Mathematica's PrimePi.  The first version won't do that, but it is a step in the right direction. 

Note that evidently the only program we know of with a fast prime_pi is Mathematica (pari, maple, etc., -- none of them have anything at all).  In contract, Mathematica can do PrimePi[10^14] in "about a minute", but the algorithm there doesn't allow larger input.


```
In[11]:= Timing[PrimePi[ 10^13 + 10^8 +10^9]]
Out[11]= {12., 346102281239}

In[13]:= Timing[PrimePi[10^14]]
Out[13]= {59.53, 3204941750802}
```


The attached code did `10^14` in just under an hour.   The issue is that Mathematica implements a different sublinear algorithm.

In Sage, with extra storage usage:

```
sage: k = 10^13
sage: time print prime_pi(k,40)
346065536839
Time: CPU 219.44 s, Wall: 219.44 s
```


So for that one mathematica is 18 times faster.


---

Comment by mhansen created at 2009-01-30 01:39:31

Hi Andrew,

I think the code looks pretty good.  There are two things that I'd like to see added before it goes into Sage.

1. Could you add a reference for the algorithm being used?  As part of this, could you add docstrings to the two cdef functions briefly describing their purpose / maybe relating them to the algorithm in the reference?

2. Could you make a note about whether or not we'll run into any issues with integer overflows or numerical accuracy as the code uses floating point arithmetic (sqrt).

--Mike


---

Comment by ohanar created at 2009-01-30 02:04:38

The algorithm used is Legendre's formula, it has been around for quite a while, so there are many references on it. I used as a reference Hans Riesel's Prime "Numbers and Computer Methods for Factorization".

--Andrew


---

Comment by cwitty created at 2009-01-30 02:18:57

By the way, it looks easy to replace a lot of the sqrt's, and to double-check the others.  You can replace a<=sqrt(b) with a*a<=b.  For the others, if you have
  a=<long long>sqrt(b)
you can follow it with:
  if a*a > b or (a+1)*(a+1) <= b: raise an exception


---

Comment by was created at 2009-02-03 04:48:58

Andrew -- We're having a lot of trouble porting wise with code that uses sqrtl.  This code needs to be slightly rewritten to not use it.   

The sqrt must be rewritten to either use gmp directly or just use the normal sage Python sqrt, which hopefully won't be much slower for this application.


---

Comment by mabshoff created at 2009-02-03 04:51:23

It is not "trouble porting wise", it is that long double functions are not guaranteed by the C99 standard to have any more precision that the double version of the same function. cwitty pointed out that also double and float implementations commonly return the same result, so if you want guaranteed results use gmp or mpfr - everything else plainly sucks.

Cheers,

Michael


---

Comment by boothby created at 2009-02-06 19:55:49

The following lines from your update are highly disturbing.


```
	104	        cdef long long m_max = <long long> sqrtl(x) + 1 
 	105	        while (m_max-1)*(m_max-1) > x or m_max*m_max <= x: 
 	106	            m_max = <long long> sqrtl(x) + 1
```


Factoring out some noise, this simplifies to:


```
a = b
while x:
   a = b
```


where a,b, and x will *NEVER* change *AT ALL* during the execution of the code.  So if you ever enter the while loop, boom.


---

Comment by was created at 2009-02-06 19:58:34

> The following lines from your update are highly disturbing.

I only looked at this for a second, but I suspect you're reasoning as if the numbers satisfied laws such as commutative, associativity etc.; probably the whole point is they might not since they are just floating point approximations.


---

Comment by cwitty created at 2009-02-06 21:29:39

No, boothby is right.  There's no commutativity, associativity, etc. involved here.  The only floating point at all is in `<long long>sqrtl(x)`, and that certainly ought to give the exact same result every time you call it on any particular platform (although the results from one platform to another certainly might differ).


---

Comment by was created at 2009-03-03 23:09:22

this is rebased against 3.4.alpha0 *and* it implements sqrt for long and long long using double and float code from Bill Hart


---

Attachment


---

Comment by robertwb created at 2009-03-18 04:44:46

It would be good to include a reference to the algorithm, and perhaps a bit more documentation in the code itself. For example, what is mem_mult or m_max? 

Maybe a the docstring should have an example of computing len(prime_range(...)) to show more explicitly what it's computing. 

The second line of `prime_phi_large`, no need to write `long(N)`, just write N. 

I'm not sure what's going on here, but it's not deterministic. 


```
sage: for n in range(90000, 100000, 3):
....:     if prime_pi(n) != len(prime_range(n+1)):
....:         print n, prime_pi(n), len(prime_range(n+1));
....:         
91587 8855 8855
91848 8878 8875
92112 8899 8896
92373 8924 8921
92376 8921 8921
92637 8947 8945
92901 8979 8976
92904 8976 8976
93171 8999 8999
...
```


(This is on an OS X 10.4 intel.)


---

Comment by ohanar created at 2009-04-13 14:32:53

this is rebased against 3.4 and should now be deterministic


---

Attachment

rebased against 3.4.1.rc2


---

Attachment


---

Comment by cwitty created at 2009-04-15 04:38:34

Major issue: it needs to raise an exception on an invalid mem_mult, instead of giving the wrong answer:

```
sage: prime_pi(10^6)
78498
sage: prime_pi(10^6, 0)
228574
```


Minor issues:
`allows for use of addition memory` should be `allows for the use of additional memory`

It looks like the function bisect() is doing some variant on binary search; but it's not the standard algorithm, which makes it harder to understand and review.  Maybe it should be replaced with a real binary search (for example, following the flowchart from http://en.wikipedia.org/wiki/Binary_search).

Note that I've read the code and performed lots of tests (against len(prime_range(n)) for small n, and against Mathematica for n around 2<sup>39</sup>), but I don't understand the algorithm.  With this caveat, I'd be willing to give it a positive review if the major wrong-answer issue were fixed (although fixing the minor issues too would be better, of course).


---

Comment by ohanar created at 2009-04-15 10:14:21

rebased against 3.4.1.rc2 and fixes the issues raised by cwitty


---

Attachment


---

Comment by cwitty created at 2009-04-18 15:37:15

Code looks good, doctests pass.  I still don't understand the algorithm, but I'm giving it a positive review anyway.


---

Comment by mabshoff created at 2009-04-21 23:34:20

Well, I am not too happy that there are special long long sqrt() work around function in this file. Since the code is by Bill I think they should be somewhat reliable and they seems to detect numerical precision issues, but I still do not trust them to work reliably, i.e. Sparc. 

Anyway, I would like them to be moved to its own file and I would like to see a test that compares and verifies their output for a wide range of inputs against MPFR for example. Even nicer would be the ability to switch away from this function and use MPFR functionality in its place. This is not something that will prevent this code from going in unless the current doctests will get broken on something like Sparc/Solaris where I have detected problems with the number_of_partitions() test that also relies on some sqrtl() function. 

Cheers,

Michael


---

Comment by cwitty created at 2009-04-22 00:27:57

I wouldn't worry about the correctness/portability of sqrt_longlong.  It uses sqrt() (not sqrtl()), which is exactly specified by IEEE floating point (no room for implementation differences in the spec), so it should be portable; and it has a built-in self-test, so if something goes wrong we'll get exceptions.


---

Comment by mabshoff created at 2009-04-22 00:37:06

Replying to [comment:19 cwitty]:
> I wouldn't worry about the correctness/portability of sqrt_longlong.  It uses sqrt() (not sqrtl()),

Yes, I know. I complained initially about sqrtl() in one of the early patches which was the reason long long sqrt() was defined. 

>  which is exactly specified by IEEE floating point (no room for implementation differences in the spec), so it should be portable; and it has a built-in self-test, so if something goes wrong we'll get exceptions.

I think my points still stand, i.e.
 
 * There is no reason for the long long sqrt() to be in this file since it will come in useful in some other places, i.e. the number_of_partitions() code since that code currently fails doctests on Sparc/Solaris (it might be completely unrelated to sqrtl(), but as it the code does not compile on FreeBSD 8 due to the use of sqrtl() there)
 * There should be some extensive testing done for that function. I am sure someone using the function and getting back some error message will not be happy that an error was detected, but complain and not see the advantage of detecting the issue in the first place :)
 * If some doctest here fails on Sparc/Solaris for example I will not merge this patch since I don't need any more bugs introduced that in the end someone else (i.e. William or me has to fix). Some of the fixes took a long, long time to hunt down (and we are still not done *now*), so the attitude that someone else will clean up such a mess is not something I am willing to accept, not that any person involved in this ticket has this attitude ;). 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 22:18:41

Hi,

I did extensive testing comparing Solaris/Sparc with Linux x86-64, tried to break it some other way, but I failed :). It also builds fine on Solaris 10.

One question: What is the credit situation here?

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 22:18:58

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 22:18:58

Resolution: fixed
