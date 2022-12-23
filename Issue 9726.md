# Issue 9726: An educational RSA crpytosystem

Issue created by migration from https://trac.sagemath.org/ticket/9726

Original creator: gauravluthra

Original creation time: 2010-08-11 19:09:43

Assignee: mvngu

CC:  kcrisman

Keywords: RSA, educational

A stand alone function srsa.py to implement an educational version of the RSA cryptosystem.This is the first native version of the RSA in SAGE.


---

Attachment


---

Comment by gauravluthra created at 2010-08-11 19:12:11

Changing status from new to needs_review.


---

Comment by wdj created at 2010-08-11 19:25:40

I am really happy that this is here. Although RSA is almost trivial to implement, it is nice to have a version that anyone (eg, a very lazy or tired student) can just use without having to set up anything. However, I would prefer that Minh eventually comment on this since he knows the crypto class structure of sage better than I do. 

Note that examples are completely missing from the docstrings, so this cannot go in "as is" and I am marking this as "needs work".

However, thank you for creating this!


---

Comment by wdj created at 2010-08-11 19:25:40

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-08-12 12:24:52

Rather than listing what needs to be done, let me try to write a reviewer patch that would bring gauravluthra's implementation up to the standard that is expected of any code that goes into the Sage library. In case you haven't done so, please refer to the [Developer's Guide](http://www.sagemath.org/doc/developer/index.html) for guidelines on contributing to Sage.



The name `RSA` for the class is misleading because the stated purpose of this class is to be an implementation of RSA for educational purposes. We don't want to give the misleading impression that `srsa.py` can be used for industrial purposes. I'll change that name to `ToyRSA` in my reviewer patch. By the way, what does the letter "s" in "srsa.py" mean?



PS: There's a simplified version of RSA called Kid RSA that is suitable for teaching cryptography to high school students. See [this book](http://code.google.com/p/high-school-sage/) (which is in progress) for details.


---

Attachment

The patch [attachment:trac_9726-srsa.patch] is the same as [attachment:srsa.patch], but here are the crucial differences:

 * Put the ticket number in the commit message.
 * Get rid of Windows newline convention. Use Unix style end of line characters.


---

Attachment


---

Comment by wdj created at 2010-08-12 18:18:07

Is this ready for review? If so. what patches should be applied in what order?


---

Comment by mvngu created at 2010-08-14 12:04:06

Some problems with [attachment:srsa.2.patch]:

 * What if I want `n` to be odd? In that case, I get an error:
 {{{#!python
sage: from sage.crypto.public_key.srsa import RSA
sage: RSA(11, 2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/dev/shm/mvngu/sage-4.5.3.alpha0/<ipython console> in <module>()

/dev/shm/mvngu/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/crypto/public_key/srsa.pyc in __init__(self, n, e)
    152             1234567890
    153         """
--> 154         p = random_prime(2**((n/2)-1), 2**(n/2))
    155         q = random_prime(2**((n/2)-1), 2**(n/2))
    156         while( q == p ):

/dev/shm/mvngu/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/rings/arith.pyc in random_prime(n, proof, lbound)
   1139     from sage.structure.proof.proof import get_flag
   1140     proof = get_flag(proof, "arithmetic")
-> 1141     n = ZZ(n)
   1142     if n < lbound:
   1143         raise ValueError, "n must be greater than lbound: %s"%(lbound)

/dev/shm/mvngu/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/dev/shm/mvngu/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4053)()

/dev/shm/mvngu/sage-4.5.3.alpha0/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._integer_ (sage/symbolic/expression.cpp:4034)()

TypeError: unable to convert x (=16*sqrt(2)) to an integer
 }}}
 
 * Running doctests over `srsa.py` fails with the following message:
 {{{#!sh
[mvngu`@`sage sage-4.5.3.alpha0]$ ./sage -t -long devel/sage-main/sage/crypto/public_key/srsa.py 
sage -t -long "devel/sage-main/sage/crypto/public_key/srsa.py"
Exception raised by doctesting framework. Use -verbose for details.
	 [1.8 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage-main/sage/crypto/public_key/srsa.py" # Exception from doctest framework
Total time for all tests: 1.8 seconds
 }}}
 
This patch needs a lot of work and a lot of redesign.
