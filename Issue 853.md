# Issue 853: Add a pslq implementation to Sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-12 00:27:12

Assignee: was

CC:  burcin robertwb


```
David Bailey's ARPREC package http://crd.lbl.gov/~dhbailey/mpdist/
includes several implementations of PSLQ, written in C++, and is
licensed under BSD. However, ARPREC raw multi arithmatic timings
don't look too favorable http://pari.math.u-bordeaux.fr/benchs/
timings-mpfr.html and one has the same fix-x86 issues as quad-double.
It looks like, however, one of the advantages of PSLQ is that it does
not require full-precision at many of the intermediate steps. (that's
what this two-level stuff is about in his package--most operations
are performed with machine-double arithmetic).

Zimmermann also has a GPL implementation, based on gmp, which is only
1000 lines long. http://www.loria.fr/~zimmerma/free/ No idea yet how
speeds compare.
```



---

Comment by zimmerma created at 2007-11-16 23:30:57

Damien Stehle did some comparisons between the PSLQ implementation of Bailey and his FPLLL, and
FPLLL was much faster. Of course it would be good to have an independent comparison, but it might
be that PSLQ does not outperform LLL when searching for linear relations.


---

Comment by wdj created at 2009-05-07 15:00:53

To be precise, Zimmerman's code is at http://www.loria.fr/~zimmerma/free/pslq-1.0.c and is licensed under the GPLv2+.


---

Comment by was created at 2009-08-10 23:03:00

I've attached the code/paper that was attached to the following email.


```
agnes.jany`@`googlemail.com>
to	wstein`@`gmail.com
date	Mon, Aug 10, 2009 at 2:16 PM
subject	PSLQ implementation
mailed-by	googlemail.com
	
hide details 2:16 PM (1 hour ago)
	
	
Reply
	
	Follow up message
Dear Mr Stein,

I'm a mathematics student at the Johannes-Gutenberg University of Mainz, Germany.
As a part of my diploma thesis, I have implemented PSLQ to SAGE. You can find
the code, a worksheet and a documentation in the attachment of this email. Maybe
you can use my work for your project.

Yours sincerely,
Agnes Jany
```



---

Attachment

Note that mpmath, which is now a standard Sage package, contains an implementation of pslq:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: import sage.libs.mpmath.all as mpmath
sage: mpmath.mp.dps = 30
sage: mpmath.pslq([sqrt(n) for n in range(2, 8+1)])
[2, 0, 0, 0, 0, 0, -1]
sage: mpmath.pslq([pi/4, acot(5), acot(239)])
[1, -4, 1]
```

| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
The examples are from the mpmath documentation, see http://mpmath.googlecode.com/svn/trunk/doc/build/identification.html

The first one says that the only integer relation between the square roots of 2,3,...,8 is `2\sqrt{2}-\sqrt{8}=0`.  The second is one of the cool formulas expressing pi as a combination of arccotangents.


---

Comment by AlexGhitza created at 2009-11-29 03:51:55

It would still be worth it to wrap Paul Zimmermann's C implementation, since it's fast.  I tried it together with the mpmath implementation on the real life example given at the top of http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node6.html

Both give the right answer (yay!).  According to timeit:

Zimmermann's C implementation:


```
25 loops, best of 3: 13.6 ms per loop
```


mpmath's implementation:


```
5 loops, best of 3: 267 ms per loop
```


So the C code is 20 times faster in this example.


---

Comment by fredrik.johansson created at 2009-11-30 16:41:43

The mpmath implementation should be correct, but it doesn't implement all the stopping criteria, and sometimes the precision, tolerance and iteration settings need fiddling with to give the right result. So even ignoring speed, it would be desirable for Sage to use an implementation that gives good control over all the settings.

The 20x difference actually sounds a bit high (though not unrealistic). I wonder if the number of iterations is the same for both implementations (it could be quite different depending just on small implementation details). Also, on my computer, PSLQ runs about twice as fast with mpmath+gmpy than mpmath+Sage.

I don't know how the other implementations compare, but I would favor adding e.g. Paul Zimmermann's implementation to Sage. It should be trivial to wrap mpmath.pslq as well, so perhaps it could be provided as an optional algorithm.


---

Comment by AlexGhitza created at 2010-02-21 12:05:33

I have created an spkg for Paul Zimmermann's C implementation of PSLQ, see

http://sage.math.washington.edu/home/ghitza/pslq-1.0.spkg

I have also started writing an interface for using this from Sage, see the attached patch `trac_853.patch`.  This is obviously not done: for one, there should be way more docstrings and doctests.  However, I would like some feedback on the interface before I put much more work into this.  If somebody has a cleaner way of using PSLQ from Sage, I'm happy to listen and throw away what I've done so far.

I'm about to ask for feedback on sage-devel.


---

Comment by AlexGhitza created at 2010-02-21 12:05:33

Changing status from needs_work to needs_info.


---

Attachment

apply after installing pslq-1.0.spkg


---

Comment by AlexGhitza created at 2010-02-21 12:21:24

PS (not LQ): I do think that we should also eventually have `implementation="mpmath"` as an option, if only for verification purposes; but I would prefer not to overload this ticket, since it's already two years old.

PPS: I'll change the milestone back to sage-wishlist until this is ready for review.


---

Comment by drkirkby created at 2010-02-21 13:17:41

It's good to see you have tested this on Solaris, though there is a potential Solaris issue:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then 
    echo "64 bit MacIntel" 
    CFLAGS="$CFLAGS -m64 "; export CFLAGS 
fi
```


should, at the very least, be replaced by 


```
if [ "x`uname`" = xyes ]; then 
    echo "Building a 64-bit version of pslq" 
    CFLAGS="$CFLAGS -m64 "; export CFLAGS 
    LDFLAGS="$LDFLAGS -m64 "; export LDFLAGS 
fi
```



It is in general safer to put an x in front of the `uname` and then test for whatever we want, with an x in front of that. (This is for maximum portability, using any shell, and is not essential, but I think a good habit to get into). There is no need to quote "xyes" as we know it has no spaces in it. 

Without removing the Darwin restriction, it would be impossible to build a 64-bit version on Solaris, OpenSolaris or other system such as HP-UX where both 32-bit and 64-bit executables are supported.

Whether LDFLAGS is necessary or not depends on the package. I've not tried building this 64-bit Solaris. I'll have a look at that later, but I do not think setting LDFLAGS ever appears to do any harm, and is sometimes essential. 

Actually, better still would be 


```
if [ -z "$CFLAG64" ] ; then
  CFLAG64=-m64
fi

if [ "x`uname`" = xyes ]; then 
    echo "Building a 64-bit of pslq" 
    CFLAGS="$CFLAGS  $CFLAG64"
    LDFLAGS="$LDFLAGS $CFLAG64"
fi

if [ "x`$SAGE_LOCAL/bin/testcc.sh`" = xGNU ] ; then
  CFLAGS="$CFLAGS -Wall -pedantic"
fi

export CFLAGS
export LDFLAGS

```


as that would 
 * Allow the variable CFLAG64 to be set to whatever compiler flag is necessary to build 64-bit code, which is not -m64 for all compilers. (CFLAG64 has been used in other packages for this purpose, to increase portability). 
 * Add the compiler options -Wall and -pedantic if using gcc. 

Compiling with the -Wall -pedantic options I get:


```
drkirkby`@`hawk:/tmp/pslq-1.0/src$ gcc -Wall -pedantic -c pslq-1.0.c 
pslq-1.0.c: In function ‘print_column’:
pslq-1.0.c:175: warning: format ‘%u’ expects type ‘unsigned int’, but argument 2 has type ‘long unsigned int’
pslq-1.0.c: In function ‘print_relation’:
pslq-1.0.c:224: warning: format ‘%u’ expects type ‘unsigned int’, but argument 3 has type ‘long unsigned int’
pslq-1.0.c: In function ‘print_matrix’:
pslq-1.0.c:240: warning: format ‘%u’ expects type ‘unsigned int’, but argument 2 has type ‘long unsigned int’
pslq-1.0.c: In function ‘pslq’:
pslq-1.0.c:855: warning: format ‘%u’ expects type ‘unsigned int’, but argument 2 has type ‘long int’
pslq-1.0.c:858: warning: format ‘%u’ expects type ‘unsigned int’, but argument 2 has type ‘long int’
pslq-1.0.c:860: warning: format ‘%d’ expects type ‘int’, but argument 2 has type ‘long int’
pslq-1.0.c:870: warning: format ‘%u’ expects type ‘unsigned int’, but argument 2 has type ‘long int’
pslq-1.0.c:892: warning: format ‘%u’ expects type ‘unsigned int’, but argument 2 has type ‘long int’
pslq-1.0.c: In function ‘main’:
pslq-1.0.c:972: warning: implicit declaration of function ‘strcmp’
pslq-1.0.c:1040: warning: format ‘%u’ expects type ‘unsigned int’, but argument 2 has type ‘long unsigned int’
pslq-1.0.c:1044: warning: format ‘%u’ expects type ‘unsigned int *’, but argument 2 has type ‘long unsigned int *’
pslq-1.0.c:1055: warning: format ‘%u’ expects type ‘unsigned int’, but argument 2 has type ‘long unsigned int’
```


Some of those warnings would lead me to believe a 64-bit build of this would not work as expected. In that case, 'unsigned int' would be 4 bytes, but 'long unsigned int' would be 8 bytes. That could go very pear shaped. 

The function strcmp() is defined in strings.h on Solaris, so I would suggest adding

```
#include <strings.h>
```


I can't comment on the maths aspect of it - I'm not a mathematician. 

Some of these issues need reporting upstream, some are problems with spkg-install. 


*I would note that all of the above code snippets I wrote were untested, so would need testing*

Dave


---

Comment by zimmerma created at 2010-02-22 20:31:28

I'd like to review that patch (now at SD20 in Marseilles) however I've downloaded sage 4.3.3.alpha1
a few days ago and compiled it on my laptop (Core 2 Duo under Fedora 12), and sage -t * gives
593 Segfaults (without any patch applied). With this, I don't see how I could seriously review
that patch. I hope the final 4.3.3 release is better (now compiling). Is this problem on Fedora 12
being analyzed currently? I can send the complete log from sage -t * with 4.3.3.alpha1 if needed.

Paul


---

Comment by AlexGhitza created at 2010-02-22 22:06:10

Hi Paul,

I'm in a similar situation, and currently having to build sage-4.3.3 on my laptop since I messed up my 4.3.3.alpha1.  I suggest you send an email to sage-devel about the Fedora 12 issues, with a link to the test log (and maybe also to the build log).

Since you're looking at reviewing this, I will try to finish up the documentation and other things today (most likely tonight...  Australian time).


---

Comment by zimmerma created at 2010-02-23 17:30:29

I did a comparison of my PSLQ implementation (within Sage) with fpLLL with a knapsack matrix.
With Bailey's "node6" example, fpLLL is 14 times faster:

```
sage: m = matrix(9,10)
sage: for i in range(9):
    m[i,i]=1
sage: for i in range(9):
    m[i,9]=ZZ(num_list[i]*RealField(200)(2)^180)//2^10

sage: L=m.LLL()
sage: L.row(0)
(-480, 1920, 0, -16, -255, -660, 840, 160, -360, 219687)
sage: p.coefficients()
(480, -1920, 0, 16, 255, 660, -840, -160, 360)

sage: %timeit L=m.LLL()
625 loops, best of 3: 1.41 ms per loop

sage: %timeit p=PSLQ(num_list, prec=167)
25 loops, best of 3: 19.8 ms per loop
```

Thus apart from historical reasons (or comparison with fpLLL) I don't see any point to add PSLQ in Sage. Or the default PSLQ mode should be to call fpLLL. However maybe I'm biased because
fpLLL was designed by a former student of mine.


---

Comment by zimmerma created at 2010-02-23 17:33:28

> Or the default PSLQ mode should be to call fpLLL. 

in fact, it would be cleaner to have a function `linear_relation`, which could have
algorithm=LLL (default) or algorithm=PSLQ.


---

Comment by zimmerma created at 2010-02-24 07:10:24

I got some more information about PSLQ by David Bailey, who agreed that I forward it to the Sage
developers (the references [1] and [2] are those from pslq-1.0.c):

```
Comments:  Reference [1] in your note is the original PSLQ paper, but
the algorithm as presented there is quite cumbersome, as it involves
(needlessly) many full-matrix operations.  Reference [2] stated an
abbreviated but equivalent version; unfortunately, however, it includes
one bug.  Thus I strongly suggest that you base your implementation on
the following paper:

David H. Bailey and David J. Broadhurst, "Parallel Integer Relation
Detection: Techniques and Applications," /Mathematics of Computation/,
vol. 70, no. 236 (Oct 2000), pg. 1719-1736.  Our preprint copy is
available at:
http://crd.lbl.gov/~dhbailey/dhbpapers/ppslq.pdf

The basic PSLQ algorithm is stated on page 2, and should work well as
stated (please let me know if you have any problems).  A two-level and a
three-level variant are also described, which are faster but quite a bit
more complicated.

However, if you are really serious, I suggest that you try the
"multi-pair" variant of PSLQ, which is presented in the above paper
beginning on page 10.  Although we devised this scheme originally to be
suitable for parallel processing, we have found that even on a single
processor system it runs significantly faster, and is significantly more
effective in recovering relations when the input data is given only to
limited precision.  Two- and a three-level variants of the multi-pair
scheme, in analogy to the two- and three-level versions of the regular
PSLQ, are also given in the paper.  These are much faster than the basic
multi-pair PSLQ scheme, because they perform most operations using
ordinary double-precision arithmetic, updating the multi-precision
arrays only occasionally when needed.

In my own work, I always use the multi-pair PSLQ.  I use the basic
multi-pair PSLQ for n up to 10 or 20 and for modest precision.  For
larger n, and, say, 500-digit or more precision, I generally use
two-level multi-pair scheme.  For truly "heroic" calculations (e.g., n >
100 and precision level > 2000 digits), I use the three-level multi-pair
scheme, since it has advantages for very large calculations and runs
well on a parallel system -- see some case studies mentioned in the
above paper.

Please let me know if it works for you.  And if you have any questions,
I would be pleased to respond.  If you wish, you can look at the
implementations of PSLQ and the multi-pair PSLQ schemes (in both C++ and
Fortran-90) that we have bundled with our ARPREC package:
http://crd.lbl.gov/~dhbailey/mpdist
```

I will try to modify my code to use the "basic PSLQ algorithm" described in the paper
mentioned above. However in the short term I won't be able to implement the multi-pair
variant. Thus if somebody wants to do it, please proceed. Alternatively, one might use
the PSLQ variants from ARPREC (if the license is ok).


---

Comment by AlexGhitza created at 2010-02-24 11:30:10

Just a note on ARPREC's license, since Paul brought it up: it is not BSD as stated in this ticket's description, rather BSD-LBNL.  However, this is apparently compatible with both GPLv2 and GPLv3, according to the table "Good licenses" at

http://fedoraproject.org/wiki/Licensing

So there should be no legal obstacles to using ARPREC.


---

Comment by hivert created at 2012-06-20 19:03:19

Hi Paul,

How much work would that be to interface your C code with Sage ? Do you have a proof of concept ?

Florent


---

Comment by zimmerma created at 2012-06-20 19:58:12

Replying to [comment:20 hivert]:
> How much work would that be to interface your C code with Sage ? Do you have a proof of concept ?

no idea. Why do you ask? See comment [comment:2]. I see no reason to interface PSLQ.

Paul


---

Comment by hivert created at 2012-06-20 21:14:44

Replying to [comment:21 zimmerma]:
> Replying to [comment:20 hivert]:
> > How much work would that be to interface your C code with Sage ? Do you have a proof of concept ?
> 
> no idea. Why do you ask? See comment [comment:2]. I see no reason to interface PSLQ.

I'm at a small workshop and there is someone which is currently using Maple and is considering to switch to Sage.. Maple has both LLL and PSLQ. He told me that, he has some stability problem with LLL, in the sense that removing some precision digits gives drastically different results. Apparently PSLQ doesn't. I've no idea if it's a problem with the algorithms or the implementation.


---

Comment by zimmerma created at 2012-06-20 21:40:27

I'm curious seeing an example with some stability problem with LLL.

Paul


---

Comment by AlexGhitza created at 2012-06-21 01:37:26

This past January, a student of mine and I have run some experiments comparing fpLLL and the PSLQ implementations from ARPREC (we wanted to take the best current implementations to get a realistic comparison).  In the examples we ran, we found almost no reason to use PSLQ instead of fpLLL for finding integer relations.  The only situation where PSLQ might be more appropriate is when it is extremely expensive to generate extra digits in the input floating point numbers.  PSLQ has a slight edge here because it tends to require fewer digits of precision than fpLLL.  Most of the time this is of no consequence because fpLLL is much faster.  We'll try to write something up describing our experiments and results, but I don't know how soon I'll find time for that.

In terms of "stability", our experiments indicate that PSLQ tends to stick with the correct answer once it finds it, as you add more digits of precision.  With fpLLL, you sometimes hit the right answer with, say 190 digits, but then you get different answers for a short while (say, 191 to 197 digits), and then it stabilises on the right answer again.  Paul, I can dig up an explicit example of this if you are interested.  Again, I don't see this as an issue from a practical point of view -- I would run the algorithm until I get the exact same answer with 3 or 5 different precisions.


---

Comment by zimmerma created at 2012-06-21 07:30:41

Alex,

> I can dig up an explicit example of this if you are interested.

yes please do! Such explicit examples are extremely useful.

Paul


---

Comment by kcrisman created at 2014-11-19 17:17:11

Any news on this ticket?


---

Comment by zimmerma created at 2014-11-19 18:42:25

> Any news on this ticket?

I don't know what information was missing in comment [comment:9], but the following reference might be useful: http://dl.acm.org/citation.cfm?id=2465936

Paul


---

Comment by kcrisman created at 2014-12-19 01:52:43

See also http://math.stackexchange.com/questions/853339/ which seems quite relevant.

Do we actually _have_ one in Sage currently, by the way?  A new user implied we might, just not a very powerful one.
