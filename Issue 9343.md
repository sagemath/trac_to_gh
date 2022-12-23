# Issue 9343: upgrade pari to version 2.4.3

Issue created by migration from https://trac.sagemath.org/ticket/9343

Original creator: was

Original creation time: 2010-06-26 05:52:42

Assignee: tbd

CC:  robertwb davidloeffler cremona jdemeyer

See #7736 (a bug this will fix), #8453 (last pari upgrade).

After doing this, we also need to remove sea.gp, since it is included in pari now.


---

Comment by was created at 2010-06-26 05:53:18

NOTE: According to http://pari.math.u-bordeaux.fr/packages.html, there are now two seadata tarballs; we'll have to make one standard, and one optional.


---

Comment by was created at 2010-06-26 06:48:12

The new ellap (which replaces the sea.gp script in sage) is seriously buggy, evidently.  Sometimes it works, but the first example I tried fails miserably.  

```

? ellap(ellinit([1,2,7,4,3]),nextprime(10^20))
%1 = -4070602678
? ellap(ellinit([1,2,3,4,5]),nextprime(10^20))
  ***   at top-level: ellap(ellinit([1,2,3
  ***                 ^--------------------
  *** ellap: bug in PARI/GP (Segmentation Fault), please report
  ***   Break loop: type 'break' to go back to GP
break> 

? ellap(ellinit([1,2,3,4,5]),nextprime(10^25))
%2 = 1231939791654
? ellap(ellinit([1,2,3,4,5]),nextprime(10^30))
%3 = 1790178944607137
? ellap(ellinit([1,2,3,4,5]),nextprime(10^35))
  ***   at top-level: ellap(ellinit([1,2,3
  ***                 ^--------------------
  *** ellap: bug in PARI/GP (Segmentation Fault), please report
  ***   Break loop: type 'break' to go back to GP
break> 
```


NOTE: To use ellap for big p, you *must* put the extracted data from seadata.tgz/data/*  in local/share/pari, as explained here: http://pari.math.u-bordeaux.fr/packages.html

I'm reporting this bug upstream now.


---

Comment by mhansen created at 2010-06-26 17:47:26

This could hopefully fix the SEA segfault in Cygwin.


---

Comment by robertwb created at 2010-06-26 19:42:19

`pari.listcreate` no longer pre-allocates the entire list, so can't be used in the _pari_trap (out of memory) tests.


---

Attachment


---

Comment by was created at 2010-06-26 19:54:13

My spkg is here:

    http://sage.math.washington.edu/home/wstein/build/sd22/pari/sage-4.5.alpha0/pari-2.4.3.svn.spkg


---

Attachment


---

Attachment


---

Comment by robertwb created at 2010-06-26 21:37:40

Here is a list of functions from decl.pxi that show up nowhere in the pari sources (using grep): http://sage.math.washington.edu/home/robertwb/scratch/robertwb/sage-4.4.4/missing_functions.txt


---

Comment by fbissey created at 2010-06-26 22:33:37

Just as a practicality could we put a date in the spkg's name?
It is a svn snapshot so we really want to know when it has been taken.


---

Attachment


---

Attachment

New spkg location:

   http://sage.math.washington.edu/home/wstein/build/sd22/pari/pari-2.4.3.svn.spkg


---

Comment by robertwb created at 2010-06-27 01:56:59

New spkg at http://sage.math.washington.edu/home/robertwb/pari-2.4.3.svn.p1.spkg (updated patch files).


---

Attachment

Suspiciousness when installing pari-2.4.3.svn.p1.spkg:

```

0 --with-gxx-include-dir=/include/c++/4.2.1
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5659)
****************************************************
./spkg-install: line 1: B1: command not found
./spkg-install: line 1: 2000: command not found
./spkg-install: line 1: 0c#!/bin/sh: No such file or directory
Configuring pari-2.4.3 (DEVELOPMENT VERSION) 
Checking echo to see how to suppress newlines...
...using \c
Looking for some tools first ...
```



---

Comment by was created at 2010-06-27 03:06:53

Polynomial factorization over number fields is broken:

```
?  nffactor(nfinit(y^2-5), x^5 - x^4 - 7*x^3 + x^2 + 7*x - 3)
%6 = 
[x - 3 1]

[x + Mod(-1/2*y + 1/2, y^2 - 5) 4]

[x + Mod(1/2*y + 1/2, y^2 - 5) 0]

? factor                 
factor        factorcantor  factorial     factormod     factorpadic   
factorback    factorff      factorint     factornf      
? factornf(x^5 - x^4 - 7*x^3 + x^2 + 7*x - 3, y^2-5)
%7 = 
[x - 3 1]

[x + Mod(-1/2*y + 1/2, y^2 - 5) 0]

[x + Mod(1/2*y + 1/2, y^2 - 5) 4]

```


Here's what used to happen:

```
? nffactor(nfinit(y^2-5), x^5 - x^4 - 7*x^3 + x^2 + 7*x - 3)
%7 = 
[x - 3 1]
[x + Mod(-1/2*y + 1/2, y^2 - 5) 2]
[x + Mod(1/2*y + 1/2, y^2 - 5) 2]
```



---

Comment by was created at 2010-06-27 03:11:19

Above "Polynomial factorization over number fields is broken" has now been reported upstream by me to submit`@`pari.math.u-bordeaux.fr


---

Comment by robertwb created at 2010-06-27 05:25:47

Here's a link to the doctest failures: http://sage.math.washington.edu/home/robertwb/scratch/robertwb/sage-4.4.4/doctests.log


---

Comment by was created at 2010-06-27 05:28:53

New spkg:

     http://sage.math.washington.edu/home/wstein/patches/pari-2.4.3.svn.p2.spkg


---

Comment by was created at 2010-06-27 06:07:28

New version

    http://sage.math.washington.edu/home/wstein/patches/pari-2.4.3.svn.p3.spkg


---

Comment by was created at 2010-06-27 06:10:29

NOTE: pari-2.4.3.svn.p3.spkg fixes the polynomial factorization bug mentioned above.


---

Attachment


---

Comment by robertwb created at 2010-06-27 06:38:49

I've updated http://sage.math.washington.edu/home/robertwb/scratch/robertwb/sage-4.4.4/doctests.log


---

Attachment


---

Attachment


---

Attachment

a couple more doctest fixes


---

Comment by cremona created at 2010-06-27 16:36:36

Replying to [comment:21 cremona]:

I nearly finished sorting out extcode/pari/cremona and elliptic_curves/gp_cremona.py and will finish that today (Sunday) and post a patch for it.


---

Comment by cremona created at 2010-06-27 19:36:44

Replying to [comment:22 cremona]:
> Replying to [comment:21 cremona]:
> 
> I nearly finished sorting out extcode/pari/cremona and elliptic_curves/gp_cremona.py and will finish that today (Sunday) and post a patch for it.

I had to make one chenge to extcode/pari/simon/ell.gp (removing one comma!) and have reported it upstream.


---

Attachment


---

Comment by was created at 2010-06-28 21:53:51

As of right now, you can install this into 4.4.4 by doing:

1.

```
  ./sage -f -m http://sage.math.washington.edu/home/wstein/patches/pari-2.4.3.svn.p3.spkg
```


2. import the patch called sagelib_9343.patch to the main Sage repo.

3. import the patch extcode_9343.patch into the SAGE_ROOT/data extcode.


---

Attachment


---

Attachment

this flattens all extcode patches above


---

Comment by was created at 2010-06-28 22:17:56

flattening of *all* sagelib patches above.


---

Attachment

Thanks!


---

Comment by fbissey created at 2010-07-03 22:14:17

Are there any separate entry for patching problems with:
eclib
lcalc
genus2reduction
Or has no one tried to to see if these were broken by this version
of pari?


---

Comment by cremona created at 2010-07-04 13:38:18

I will compile eclib with pari 2.4.3;  if any changes are needed, I will change the source at source, so patches will not be needed.


---

Comment by cremona created at 2010-07-04 14:12:46

Replying to [comment:27 cremona]:
> I will compile eclib with pari 2.4.3;  if any changes are needed, I will change the source at source, so patches will not be needed.

eclib compiles and runs fine with 2.4.3.  It even now compiles with -ansi (which was not true before) and almost with -pedantic (just 4 extraneous semicolons need deleting;  not worth a new spkg version).


---

Comment by fbissey created at 2010-07-06 10:05:42

lcalc has some problems with pari-2.4. I am not sure yet if they are minor
or major.


```
Lcommandline_elliptic.cc: In function ‘void data_E(char*, char*, char*, char*, char*, int, Double*)’:
Lcommandline_elliptic.cc:124: error: ‘lgeti’ was not declared in this scope
make[1]: *** [Lcommandline_elliptic.o] Error 1
```

I'll be checking genus2reduction next.


---

Comment by fbissey created at 2010-07-06 11:03:43

lcalc problem is minor. Not sure why pariold.h is not properly included
when it should be sourced from pari.h (in pari-2.3 it was sourced from paricom.h
itself included from pari.h).
Anyway replacing lgeti by (long)cgeti as would be done by pariold.h works
like a charm.


---

Comment by fbissey created at 2010-07-07 04:35:01

genus2reduction suffer the same kind of problems. But it is more serious:

```
genus2reduction.c: In function ‘main’:
genus2reduction.c:476: error: ‘polun’ undeclared (first use in this function)
genus2reduction.c:476: error: (Each undeclared identifier is reported only once
genus2reduction.c:476: error: for each function it appears in.)
genus2reduction.c:600: error: ‘polx’ undeclared (first use in this function)
genus2reduction.c:96: warning: ignoring return value of ‘scanf’, declared with attribute warn_unused_result
genus2reduction.c:98: warning: ignoring return value of ‘scanf’, declared with attribute warn_unused_result
genus2reduction.c: In function ‘factorpadicnonun’:
genus2reduction.c:1676: error: ‘polx’ undeclared (first use in this function)
genus2reduction.c: In function ‘polymini’:
genus2reduction.c:1701: error: ‘polx’ undeclared (first use in this function)
genus2reduction.c:1712: error: ‘zero’ undeclared (first use in this function)
genus2reduction.c:1731: error: ‘un’ undeclared (first use in this function)
genus2reduction.c: In function ‘discpart’:
genus2reduction.c:1818: error: ‘polun’ undeclared (first use in this function)
genus2reduction.c: In function ‘polyminizi’:
genus2reduction.c:1856: error: ‘gi’ undeclared (first use in this function)
genus2reduction.c:1859: error: ‘polx’ undeclared (first use in this function)
genus2reduction.c: In function ‘polyminizi2’:
genus2reduction.c:1939: error: ‘polx’ undeclared (first use in this function)
genus2reduction.c:1942: error: ‘gi’ undeclared (first use in this function)
genus2reduction.c: In function ‘zi2mod’:
genus2reduction.c:2001: error: ‘gi’ undeclared (first use in this function)
```

polun, polx, zero and un were all defined in pariold.h but are not anywhere
anymore in pari-2.4. I cannot track the definition of gi in anything from 
pari-2.3, anyone knows where that come from and what it should be replaced with?
There is a line in pari-2.3 headers mentioning it but not a definition of it 
as far as I can see:

```
#define is_universal_constant(x) ((GEN)(x) >= gen_0 && (GEN)(x) <= gi)
```

this is in paristio.h form pari-2.3.5.


---

Comment by cremona created at 2010-07-09 11:48:00

I just noticed that the .p3.spkg compiles pari with flag -O1.  Surely this is not a sensible choice?


---

Comment by cremona created at 2010-07-09 11:53:37

I have fixed a bug in Simon's extcode and am currently fixing doctest failures in sage/schemes/elliptic_curves -- so no-one else should work on thar dir without contacting me first!  John C


---

Comment by was created at 2010-07-09 11:56:00

Replying to [comment:33 cremona]:
> I just noticed that the .p3.spkg compiles pari with flag -O1.  Surely this is not a sensible choice?

Surely it was done on purpose, because with a bigger optimization flag PARI must have exhibited some bugs.  The question is how/why/if this is still needed.


---

Comment by jdemeyer created at 2010-07-09 13:47:51

Can somebody please have a look at this:

```
RR(gp(exp(1)))
```


This just hangs sage, in a way which can not even be interrupted.


---

Comment by jdemeyer created at 2010-07-10 11:24:57

Replying to [comment:35 was]:
> Replying to [comment:33 cremona]:
> > I just noticed that the .p3.spkg compiles pari with flag -O1.  Surely this is not a sensible choice?
> 
> Surely it was done on purpose, because with a bigger optimization flag PARI must have exhibited some bugs.  The question is how/why/if this is still needed. 

I always compile my own copy of PARI/GP with -O3 -fomit-frame-pointer -march=core2 using the latest gcc and that seems to work fine.


---

Comment by jdemeyer created at 2010-07-10 11:30:07

I found a bug in PARI's nfbasis() command: [PARI bug 1072](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1072).  Now that it has been fixed, maybe somebody should make a new spkg with the latest pari?


---

Comment by was created at 2010-07-10 11:56:12

Replying to [comment:37 jdemeyer]:
> Replying to [comment:35 was]:
> > Replying to [comment:33 cremona]:
> > > I just noticed that the .p3.spkg compiles pari with flag -O1.  Surely this is not a sensible choice?
> > 
> > Surely it was done on purpose, because with a bigger optimization flag PARI must have exhibited some bugs.  The question is how/why/if this is still needed. 
> 
> I always compile my own copy of PARI/GP with -O3 -fomit-frame-pointer -march=core2 using the latest gcc and that seems to work fine.

"Seems to"?   The Sage test suite is a much better test suite for PARI than pari's own, IMHO.


---

Comment by was created at 2010-07-10 11:56:42

Replying to [comment:38 jdemeyer]:
> I found a bug in PARI's nfbasis() command: [PARI bug 1072](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1072).  Now that it has been fixed, maybe somebody should make a new spkg with the latest pari?

Yes, definitely. It is nontrivial to make a new spkg though -- see spkg-dist...


---

Comment by jdemeyer created at 2010-07-10 12:03:11

I am working on the number field code in sage/rings/number_field/*
Lots of doctests simply fail because ideals have different generators:
"Fractional Ideal (a)" is the same ideal as "Fractional Ideal (-a)" but of course this makes doctests fail.


---

Comment by cremona created at 2010-07-10 20:06:52

I just reported another bug in nffactor to pari's bug-tracker:

```
sage -gp
...
f = polcyclo(21,y)
nf = nfinit(f);
b = Mod(y^7,f)
nffactor(nf, x^2-b)
```

gives

```

  ***   at top-level: nffactor(nf,x^2-b)
  ***                 ^------------------
  *** nffactor: not enough precomputed primes
  ***   Break loop: type 'break' to go back to GP
```

This breaks a doctest in ell_generic.py


---

Comment by cremona created at 2010-07-10 20:09:15

It's at http://pari.math.u-bordeaux.fr/cgi-bin/pkgreport.cgi?pkg=pari (#1075)


---

Comment by cremona created at 2010-07-11 09:18:55

Replying to [comment:43 cremona]:
> It's at http://pari.math.u-bordeaux.fr/cgi-bin/pkgreport.cgi?pkg=pari (#1075)

Karim Belabas writes:

```
Simpler symptom:
 nffactor(polcyclo(21,y), x^2-y^7);

This is actually unrelated to #1070. It was due to an nf being replaced
by nf.pol --- because we use Trager's trick in that range instead of a
direct relative factorization, and don't need the nf data ---.
Unfortunately, a branch of the code later tried to acces nf.index, thus
accessing a random coefficient of the defining t_POL instead of the
relevant nf data.

Fixed in svn.

Cheers,

   K.B.
```

so we now have another reason for upgrading the source in the spkg.


---

Comment by was created at 2010-07-11 09:29:19

Please don't move stuff to sage-5.0.     There will be a sage between sage-4.5 and sage-5.0, and *that* is what you should move the ticket to. Otherwise it could much more easily get lost....  I'll make such a roadmap entry now.


---

Attachment


---

Comment by jdemeyer created at 2010-07-11 10:27:54

I attached a small patch for integer discrete logarithms.  Note that the result in the doctest has always been wrong, but will now be corrected (so this is really a bug in the current version of Sage).


---

Comment by was created at 2010-07-11 10:32:20

Replying to [comment:47 jdemeyer]:
> I attached a small patch for integer discrete logarithms.  Note that the result in the doctest has 
> always been wrong, but will now be corrected (so this is really a bug in the current version of Sage).

Great work!  I'm really glad we taught you Sage development last week!!!!


---

Comment by davidloeffler created at 2010-07-11 10:43:09

Sorry to disrupt this little love-in here, but that bug has already been found (#9205) and fixed, and the patch has a positive review, and will probably be merged in the next alpha. 

There are about a hundred patches with positive review waiting on trac, many of which have something to do with number fields (as a consequence of the big number theory Sage days at MSRI). I'm disappointed to realise that you folks haven't taken this into account, which will most likely mean that your work getting the number theory code to pass doctests with the new Pari version will be reduced to complete junk when all your patches fail to apply to the next alpha.


---

Comment by cremona created at 2010-07-11 11:16:03

No need to be quite so negative.  Jeroen, I'm not sure why you thought that this ticket was the right place to add your patch anyway -- what does it have to do with the pari upgrade?


---

Comment by jdemeyer created at 2010-07-11 11:43:58

Replying to [comment:50 cremona]:
> No need to be quite so negative.  Jeroen, I'm not sure why you thought that this ticket was the right place to add your patch anyway -- what does it have to do with the pari upgrade?

It is related to the PARI upgrade because the new version of PARI fixes discrete logs (so, it fixes also #9205).  Doing the upgrade of PARI made a doctest fail, because the "expected" result from the doctest was wrong.


---

Comment by jdemeyer created at 2010-07-11 11:46:47

Regarding the issue of

```
RR(gp(exp(1)))
```

or

```
ZZ(gp(1))
```


This makes Sage hang but without using CPU time.  So it does not go into an infinite loop, it literally does nothing.


---

Comment by was created at 2010-07-11 12:12:25

Replying to [comment:49 davidloeffler]:
> Sorry to disrupt this little love-in here, but that bug has already been found (#9205) and fixed, and
> the patch has a positive review, and will probably be merged in the next alpha. 

We *really* need to release sage-4.5, so that somebody can get started with the next alpha (4.5.1). 

> There are about a hundred patches with positive review waiting on trac, many of which have something 
> to do with number fields (as a consequence of the big number theory Sage days at MSRI). I'm disappointed 
> to realise that you folks haven't taken this into account, which will most likely mean that your work
> getting the number theory code to pass doctests with the new Pari version will be reduced to 
> complete junk when all your patches fail to apply to the next alpha.

That's pretty harsh.   Anyway, the pari upgrade is higher priority, so in fact it will be the other way around. 

William


---

Comment by was created at 2010-07-11 12:13:23

Replying to [comment:52 jdemeyer]:
> Regarding the issue of
> {{{
> RR(gp(exp(1)))
> }}}
> or
> {{{
> ZZ(gp(1))
> }}}
> 

When you use `gp` it is running the command in a subprocess.  Thus you'll never see any (nontrivial) CPU time.  
> This makes Sage hang but without using CPU time.  So it does not go into an infinite loop, it literally does nothing.


---

Comment by jdemeyer created at 2010-07-11 13:46:56

I think I just had a small break-through:

The gp command now has the so-called "breakloop" on by default.  This means the following: if Sage executes a command through the gp interface which gives errors, the following will be displayed in the pseudo-tty (invisible to the Sage user):

```
? 1/0
  ***   at top-level: 1/0
  ***                  ^--
  *** _/_: division by zero
  ***   Break loop: type 'break' to go back to GP
break>
```


Now gp just waits for user input.  Since that input will never come, it just sits there forever.

I have a temporary workaround for this:
in the directory SAGE_ROOT/local/bin, move "gp" to "gp-real".  Then create the following shell script called "gp":

```
!/bin/bash

mkdir -p $HOME/sage_debug
export HOME=$HOME/sage_debug
echo "breakloop = 0" >$HOME/.gprc

# Remove --fast option
exec $SAGE_ROOT/local/bin/gp-real --emacs --quiet --stacksize 100000000
```


This changes $HOME and makes a .gprc file in it which disables the break loop.  It then runs gp without --fast, so that the .gprc file is read.


---

Attachment

Jeroen:  I was surprised to see your dokchitser patch since I thought I was working on that -- and I have been in correspondence with Tim D all morning trying to sort out the use of global variables.  So, does you patch sort out all those issues (as well as the easy defult() ones)?  If so, I clearly have wasted a lot of time today.  This example makes it clear how extremely important it is that people say clearly what tey are working on.  And I DID say clearly that I was working on everythin the elliptic_curves directory, which includes all the code which calls the Dokchiter script.

On your other point, well spotted.  But would it not be simpler to send to the gp process on initialization the command gp._eval_line('breakloop=0;') ?

Now I will go out and enjoy my Sunday, since my efforts seem to be not needed.


---

Comment by jdemeyer created at 2010-07-11 14:42:53

Replying to [comment:56 cremona]:
> Jeroen:  I was surprised to see your dokchitser patch since I thought I was working on that -- and I have been in correspondence with Tim D all morning trying to sort out the use of global variables.  So, does you patch sort out all those issues (as well as the easy defult() ones)?  If so, I clearly have wasted a lot of time today.  This example makes it clear how extremely important it is that people say clearly what tey are working on.  And I DID say clearly that I was working on everythin the elliptic_curves directory, which includes all the code which calls the Dokchiter script.
> Now I will go out and enjoy my Sunday, since my efforts seem to be not needed.

Well, I fixed the dokchitser script so it would pass some doctests in number_field.py.  But my fixes are very trivial (it took me no more than 5 minutes), so maybe you are making more serious changes to the file.  In that case, you can safely ignore my patch.


---

Comment by jdemeyer created at 2010-07-11 14:47:26

Replying to [comment:56 cremona]:
> On your other point, well spotted.  But would it not be simpler to send to the gp process on initialization the command gp._eval_line('breakloop=0;') ?

Certainly, yes.  That's why I called my solution a "work-around".  What you want to do is every time a gp process gets started, the first line should be

```
default(breakloop,0);
```


But I don't know how to do this.


---

Comment by was created at 2010-07-11 14:53:03

> But I don't know how to do this.

Look in interfaces/gp.py and/or expect.py.


---

Comment by jdemeyer created at 2010-07-11 16:28:16

I will stop working on this for now (at least for the coming week), so I uploaded what I have done so far.  There are still many things to be done, though.

One thing which I looked at but did not manage to fix was factorization of polynomials over number fields in sage/rings/polynomial/polynomial_element.pyx


---

Attachment


---

Comment by jdemeyer created at 2010-07-11 16:44:46

Another PARI/GP bug found thanks to Sage: [PARI bug 1076](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1076)


---

Comment by jdemeyer created at 2010-07-12 06:09:36

TODO: add more doctests for factoring polynomials over number fields.  Various cases:
 * non-monic polynomials
 * number fields defined by a non-monic polynomial
 * relative number fields: given a polynomial with coefficients in K, factor it over L


---

Comment by cremona created at 2010-07-12 09:44:27

Replying to [comment:59 was]:
> > But I don't know how to do this.
> 
> Look in interfaces/gp.py and/or expect.py.  

Sorted,  I added one line (line 170) in sage/interfaces/gp.py which says

```
        self._eval_line('default(breakloop,0);')
```

to get the command run everytime a new gp instance is created.  Now we get

```
sage: gp.eval('1/0')
'  ***   at top-level: 1/0\n  ***                  ^--\n  *** _/_: division by zero'
```

(followed by a new sage: prompt) and also

```
RR(gp(exp(1)))
2.71828182845905
sage: 
```

with no problems.


---

Comment by cremona created at 2010-07-12 09:56:00

apply instead of previous extcode-dokchitser patch


---

Attachment

I replaced Jeroen's 9343_extcode-dokchitser.patch with a new one which also fixes the test scripts in extcode/pari/dokchitser;  and fixes one line in extcode/pari/simon/ellQ.gp which is all that is required for that set of scripts.


---

Comment by cremona created at 2010-07-12 09:59:40

Replying to [comment:56 cremona]:
> Jeroen:  I was surprised to see your dokchitser patch since I thought I was working on that -- and I have been in correspondence with Tim D all morning trying to sort out the use of global variables.  So, does you patch sort out all those issues (as well as the easy defult() ones)?  If so, I clearly have wasted a lot of time today.  This example makes it clear how extremely important it is that people say clearly what tey are working on.  And I DID say clearly that I was working on everythin the elliptic_curves directory, which includes all the code which calls the Dokchiter script.

Apologies for this outburst.  I did waste time, but only because of my inferior gp-script debugging skills.  Thanks to Jeroen there is a much simpler fix for what was troubling me!

> 
> On your other point, well spotted.  But would it not be simpler to send to the gp process on initialization the command gp._eval_line('breakloop=0;') ?
> 
> Now I will go out and enjoy my Sunday, since my efforts seem to be not needed.


---

Comment by cremona created at 2010-07-13 13:18:23

Replying to [comment:37 jdemeyer]:
> Replying to [comment:35 was]:
> > Replying to [comment:33 cremona]:
> > > I just noticed that the .p3.spkg compiles pari with flag -O1.  Surely this is not a sensible choice?
> > 
> > Surely it was done on purpose, because with a bigger optimization flag PARI must have exhibited some bugs.  The question is how/why/if this is still needed. 
> 
> I always compile my own copy of PARI/GP with -O3 -fomit-frame-pointer -march=core2 using the latest gcc and that seems to work fine.

The answer is at #7092:  because of a failure to build pari with gcc-4.4.1 as distributed by Fedora 11, on ALL Linux systems the OPTFLAG is set to -O1 instead of -O3.  Is there not a way to detect that particular compiler-distro combination?  Otherwise all Linux users suffer!


---

Comment by was created at 2010-07-13 21:31:05

>  Is there not a way to detect that particular compiler-distro combination? Otherwise all Linux users suffer!

It was a big mistake that #7092 got a positive review (from Jaap), and another mistake that the release manager (me) didn't reject that review.  Anyway, thanks for tracking this down -- we should definitely make that -O1 hack only Fedora 11.

 -- William


---

Comment by was created at 2010-07-13 21:31:32

Also, we don't have to support fedora 11 -- it's like 2 versions out of date, and we only claim to support the latest Linux versions, out of the box.


---

Comment by cremona created at 2010-07-16 16:20:12

fixes most doctests in elliptic_curves and interfaces/gp


---

Attachment

trac_9343-elliptic-curve.patch + http://www.warwick.ac.uk/staff/J.E.Cremona/pari-2.4.3.svn.p4.spkg  (which upgrades to svn 12533)   do the following:

    1. All doctests in schemes/elliptic_curves pass except heegner.py
    2. All doctests in interfaces/* pass except for two issues in gp.py marked not tested" for now
    3. All in libs/ pass except some remaining issues in gen.pyx, mostly just fuzz but including one SIGSEGV

 I thought this worth posting despite there still being issues in some of the files it touches.


---

Comment by drkirkby created at 2010-07-16 18:08:53

I'm attaching a `spkg-check` file. I originally created #9518 to add the `spkg-check`, but John said to leave it, and let the changes be made as part of this ticket. When this ticket gets closed, so can #9518

Note there is an error in spkg-install on the first line, which displays as:

`B1;2000;0c#!/bin/sh` 

In fact, I'm surprised that works at all. 

Dave


---

Attachment

spkg-check for Pari


---

Comment by drkirkby created at 2010-07-18 14:04:40

Replying to [comment:69 cremona]:
> trac_9343-elliptic-curve.patch + http://www.warwick.ac.uk/staff/J.E.Cremona/pari-2.4.3.svn.p4.spkg  

This will not install for me.

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 
 * 12 GB RAM
 * OpenSolaris 2009.06 snv_134 X86
 * Sage 4.5
 * gcc 4.4.4

One likely cause of a problem is the `Dynamic Lib linker` does not include the -m64 flag (it should be included if SAGE64 is "yes"). 


```
pari-2.4.3.svn.p4/.hgignore
pari-2.4.3.svn.p4/spkg-install
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: /export/home/drkirkby/gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4-multilib --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.4.4-multilib --with-mpfr=/usr/local/gcc-4.4.4-multilib --disable-nls --enable-checking=release --enable-werror=no --enable-multilib --with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld
Thread model: posix
gcc version 4.4.4 (GCC) 
****************************************************
./spkg-install: line 1: B1: command not found
./spkg-install: line 1: 2000: command not found
./spkg-install: line 1: 0c#!/bin/sh: No such file or directory
Configuring pari-2.4.3 (DEVELOPMENT VERSION) 
Checking echo to see how to suppress newlines...
...using \c
Looking for some tools first ...
...ld is /usr/bin/ld
...zcat is /usr/bin/zcat
...gzip is /usr/bin/gzip
...ranlib is /usr/bin/ranlib
...perl is /usr/bin/perl
GNU compiler version 4.4.4 (GCC)
Given the previous choices, sizeof(long) is 8 chars.
The internal word representation of a double is not needed (64bit).
==========================================================================
Building for: ix86 running solaris (x86-64/GMP kernel) 64-bit version
==========================================================================
C compiler is          gcc -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer -fPIC  -g -m64   
Executable linker is   gcc  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer -fPIC  -g -m64   
Dynamic Lib linker is  gcc  -shared  $(CFLAGS) $(DLCFLAGS) -Wl,-G,-h,$(LIBPARI_SONAME) 
Looking in C lib for some symbols...
...Found exp2.
...Found log2.
...Found strftime.
...Found getrusage.
...Found sigaction.
...Found TIOCGWINSZ.
...Found getrlimit.
...Found stat.
...Found vsnprintf.
...Found waitpid.
...Found setsid.
...Found getenv.
...Found isatty.
...Found alarm.
...Found dlopen.
Checking for optional libraries and headers...
...Found libgmp in /export/home/drkirkby/sage-4.5/local/lib
...Found gmp header in /export/home/drkirkby/sage-4.5/local/include
ld.so.1: solaris-ix86-rlv23868: fatal: libgmp.so.10: open failed: No such file or directory
./Configure[79]: .: line 38: 24072: Killed
### Your version of GMP is too old for PARI. Please upgrade
### Building without GNU MP support
Hi-Res Graphics: none
...Found libreadline in /export/home/drkirkby/sage-4.5/local/lib
...Found readline header in /export/home/drkirkby/sage-4.5/local/include/readline
...Found history header in /export/home/drkirkby/sage-4.5/local/include/readline
...Found libtermcap in /export/home/drkirkby/sage-4.5/local/lib/
...Library termcap needed by readline
###
### Readline library detected, but does not seem to work
###
### Building without GNU readline support
Installation prefix ? [/export/home/drkirkby/sage-4.5/local]
...for architecture-independent files (share-prefix) ? [/export/home/drkirkby/sage-4.5/local/share]
Installation directories for:
...executables (gp, gphelp) ? [/export/home/drkirkby/sage-4.5/local/bin]
...libraries (libpari) ? [/export/home/drkirkby/sage-4.5/local/lib]
...include files ? [/export/home/drkirkby/sage-4.5/local/include]
...manual pages ? [/export/home/drkirkby/sage-4.5/local/share/man/man1]
...other system-dependent data ? [/export/home/drkirkby/sage-4.5/local/lib/pari]
...other system-independent data ? [/export/home/drkirkby/sage-4.5/local/share/pari]
Default is dynamic executable and shared library
==========================================================================
Extracting examples/Makefile.solaris-ix86
Extracting Osolaris-ix86/Makefile
Extracting Makefile
Extracting Osolaris-ix86/paricfg.h
Extracting Osolaris-ix86/../Odos/paricfg.h
Extracting scripts and macros
...in doc
...in misc
==========================================================================
Shall we try to build pari 2.4.3 (development) now (y/n)? [n]
Ok. Type "make install" when you are ready
Bye !
Building and install PARI
Making gp in Osolaris-ix86
make[1]: Entering directory `/export/home/drkirkby/sage-4.5/spkg/build/pari-2.4.3.svn.p4/src/Osolaris-ix86'
make[1]: warning: -jN forced in submake: disabling jobserver mode.
../config/genkernel ../src/kernel/x86_64/asm0.h > parilvl0.h
if test -r ./tune.h; then d=.; else d=../src/kernel/none; fi;          cat $d/tune.h ../src/kernel/none/int.h ../src/kernel/none/level1.h > parilvl1.h
cd ../src/desc && /usr/bin/perl whatnow > whatnow-solaris-ix86-23868.tmp
cat ../src/kernel/none/mp.c ../src/kernel/none/cmp.c ../src/kernel/none/gcdll.c ../src/kernel/none/ratlift.c  ../src/kernel/none/invmod.c ../src/kernel/none/gcd.c ../src/kernel/none/gcdext.c ../src/kernel/none/mp_indep.c ../src/kernel/none/add.c > mp.c
bison -d ../src/language/parse.y -o ../src/language/parse.c
make[1]: bison: Command not found
make[1]: *** [../src/language/parse.h] Error 127
make[1]: *** Waiting for unfinished jobs....
mv ../src/desc/whatnow-solaris-ix86-23868.tmp ../src/gp/whatnow.h
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5/spkg/build/pari-2.4.3.svn.p4/src/Osolaris-ix86'
make: *** [gp] Error 2
Error building GP

real	0m1.203s
user	0m0.551s
sys	0m0.640s
sage: An error occurred while installing pari-2.4.3.svn.p4
```



---

Comment by cremona created at 2010-07-18 15:11:55

Is this something wrong with pari's Configure script -- in which case should be reported upstream?  Or something which could be fixed by a change in the spkg-install script?


---

Comment by cremona created at 2010-07-18 15:21:28

Replying to [comment:70 drkirkby]:
> I'm attaching a `spkg-check` file. I originally created #9518 to add the `spkg-check`, but John said to leave it, and let the changes be made as part of this ticket. When this ticket gets closed, so can #9518

I found out how to exclude a test from being run with test-all (there's a list in src/config/get_test) and the next version of the spkg will patch that file appropriately.

> 
> Note there is an error in spkg-install on the first line, which displays as:
> 
> `B1;2000;0c#!/bin/sh` 
> 

Fixed.  Probably a finger-blunder by me.

> In fact, I'm surprised that works at all. 
> 
> Dave


---

Comment by drkirkby created at 2010-07-19 00:01:25

Replying to [comment:72 cremona]:
> Is this something wrong with pari's Configure script -- in which case should be reported upstream?  Or something which could be fixed by a change in the spkg-install script?
The type at the start of spkg-install is in the current version of pari. I'm puzzled it works at all, but it seems to. 

I was mistaken on the LINKER FLAGS, as that include CFLAGS, so the -m64 will get there from that. 

However, this still thinks gmp is broken. The version of Pari in Sage at the moment reports:


```
Checking for optional libraries and headers...
...Found libgmp in /rootpool2/local/kirkby/sage-4.5-hacked-for-64-bit-solaris/local/lib
...Found gmp header in /rootpool2/local/kirkby/sage-4.5-hacked-for-64-bit-solaris/local/include
Using GNU MP, version 4.3.1
...Found libX11 in /usr/openwin/lib
...Found X11 header files in /usr/openwin/include/X11
```


compared to this version, where I see: 


```
Checking for optional libraries and headers...
...Found libgmp in /export/home/drkirkby/sage-4.5/local/lib
...Found gmp header in /export/home/drkirkby/sage-4.5/local/include
ld.so.1: solaris-ix86-rlv23868: fatal: libgmp.so.10: open failed: No such file or directory
./Configure[79]: .: line 38: 24072: Killed
### Your version of GMP is too old for PARI. Please upgrade
### Building without GNU MP support
Hi-Res Graphics: none
...Found libreadline in /export/home/drkirkby/sage-4.5/local/lib
```


So something has changed for the worst. 

This version from svn wants bison too, so you will have to generate the files, since bison is not a prerequisite for Sage, and is not included in Sage. 

Dave


---

Comment by jdemeyer created at 2010-07-19 21:45:36

Replying to [comment:69 cremona]:
> trac_9343-elliptic-curve.patch + http://www.warwick.ac.uk/staff/J.E.Cremona/pari-2.4.3.svn.p4.spkg  (which upgrades to svn 12533)   do the following:
> 
>     1. All doctests in schemes/elliptic_curves pass except heegner.py
>     2. All doctests in interfaces/* pass except for two issues in gp.py marked not tested" for now
>     3. All in libs/ pass except some remaining issues in gen.pyx, mostly just fuzz but including one SIGSEGV
> 
>  I thought this worth posting despite there still being issues in some of the files it touches.

Nice work John!  Please let me know what you're working on, since I also plan to continue working on this ticket.


---

Comment by drkirkby created at 2010-07-20 02:13:52

Hi, 
John or someone else can perhaps convey this to the Pari developers. Would it be possible for them to add the -fPIC option on at least all Solaris systems. (Both SPARC and x86). If code goes into a shared library, it should be compiled position independent. It is unreliable if this is not done. There's some relevant information about this here. 

http://gcc.gnu.org/onlinedocs/gcc-4.5.0/gcc/Code-Gen-Options.html#Code-Gen-Options
http://gcc.gnu.org/onlinedocs/gcc-4.5.0/gcc/Link-Options.html#Link-Options

I believe it would be more reliable to build with -fPIC when the code is going into a shared library - irrespective of the platform. What one should ensure though is there is not a mixture of PIC and non-PIC code, as that can be unreliable too. 

I've not had a chance to look at the other issues, but as far as I can see, this update completely breaks a 64-bit build on Solaris or OpenSolaris. 

I've also noticed that Pari reports that _readline_ is not working on Solaris systems. Yet the _readline_ is definitely working in my Sage builds on Solaris. Several parts of Sage link against readline (Pari, gap, Singular, ECL, Python ...). None of them believe that _readline_ is broken, but Pari does. 

Dave


---

Comment by drkirkby created at 2010-07-20 02:30:08

Looking at the error message above:


```
ld.so.1: solaris-ix86-rlv23868: fatal: libgmp.so.10: open failed: No such file or directory
./Configure[79]: .: line 38: 24072: Killed
```


and comparing it to the GMP libraries that were installed, the version numbers do not match. Pari is looking for `libgmp.so.10` but I have the following GMP related files:


```
drkirkby@hawk:~/sage-4.5/local/lib$ ls -ld libgmp*
-rwxr-xr-x+  1 drkirkby staff        803 Jul 16 13:10 libgmp.la
lrwxrwxrwx   1 drkirkby staff         15 Jul 16 13:10 libgmp.so -> libgmp.so.3.4.6
lrwxrwxrwx   1 drkirkby staff         15 Jul 16 13:10 libgmp.so.3 -> libgmp.so.3.4.6
-rwxr-xr-x+  1 drkirkby staff     549536 Jul 16 13:10 libgmp.so.3.4.6
-rwxr-xr-x+  1 drkirkby staff        919 Jul 16 13:10 libgmpxx.la
lrwxrwxrwx   1 drkirkby staff         17 Jul 16 13:10 libgmpxx.so -> libgmpxx.so.3.1.6
lrwxrwxrwx   1 drkirkby staff         17 Jul 16 13:10 libgmpxx.so.3 -> libgmpxx.so.3.1.6
-rwxr-xr-x+  1 drkirkby staff      26712 Jul 16 13:10 libgmpxx.so.3.1.6
```


i.e. there is nothing like a version 10. The installed libraries have a 3.x in them, but Pari is looking for a .10. 

I've installed bison on the system, so the error message about a missing bison is not appearing any more, but that has not resolve either 
 * The _readline_ issue, which I've had for ages. OR
 * The _gmp_ library issue, which is unique to this update, and does not show up in the version in Sage. 

Dave


---

Comment by cremona created at 2010-07-20 08:28:55

> 
> Nice work John!  Please let me know what you're working on, since I also plan to continue working on this ticket.

Thanks.  I finished fixing the interfaces/gp and very nearly finished libs/pari/ .  The serious issues are gone now.  I fear that the flood of newly merged tickets for 4.5.2 will require some rebasing, so as soon as I have tidied up I will post the revised patches and a new spkg (p5).  I have not touched anything in number_fields since you did, but it still might be a good idea to wait until I have posted what I have done.


---

Comment by cremona created at 2010-07-20 08:35:10

Replying to [comment:76 drkirkby]:
> Hi, 
> John or someone else can perhaps convey this to the Pari developers. Would it be possible for them to add the -fPIC option on at least all Solaris systems. (Both SPARC and x86). If code goes into a shared library, it should be compiled position independent. It is unreliable if this is not done. There's some relevant information about this here. 
> 
> http://gcc.gnu.org/onlinedocs/gcc-4.5.0/gcc/Code-Gen-Options.html#Code-Gen-Options
> http://gcc.gnu.org/onlinedocs/gcc-4.5.0/gcc/Link-Options.html#Link-Options
> 
> I believe it would be more reliable to build with -fPIC when the code is going into a shared library - irrespective of the platform. What one should ensure though is there is not a mixture of PIC and non-PIC code, as that can be unreliable too. 
> 
> I've not had a chance to look at the other issues, but as far as I can see, this update completely breaks a 64-bit build on Solaris or OpenSolaris. 
> 
> I've also noticed that Pari reports that _readline_ is not working on Solaris systems. Yet the _readline_ is definitely working in my Sage builds on Solaris. Several parts of Sage link against readline (Pari, gap, Singular, ECL, Python ...). None of them believe that _readline_ is broken, but Pari does. 
> 
> Dave 


I was planning to do this (report upstream).  On the positive side, they just put in a patch which obviates the need for 2/3 of our patch to the header files paripriv/paridecl.h.

I think we will have a better chance of a positive reaction if we could report to pari a failure to build of pari as such and not pari-in-Sage, since they would reasonably reposond that as we patch some files they cannot be responsible.  For this, just copy the src directory of the most recent spkg (or wait until I put up p5 later today) and try it directly, after ./Configure <whatever-params> and make whatever.


---

Comment by fbissey created at 2010-07-20 09:18:42

Am I the only one seeing problems with lcalc and genus2reduction?


---

Comment by cremona created at 2010-07-20 09:32:47

Replying to [comment:80 fbissey]:
> Am I the only one seeing problems with lcalc and genus2reduction?

I don't think you are.  I have been sorting out other things!  I have just finished with the (rather important) sage/libs/pari and sage/intergaces/gp, with everything working except (bizarrely) the hyperbolic tangent function.


---

Comment by fbissey created at 2010-07-20 10:00:29

Replying to [comment:81 cremona]:
> Replying to [comment:80 fbissey]:
> > Am I the only one seeing problems with lcalc and genus2reduction?
> 
> I don't think you are.  I have been sorting out other things!  I have just finished with the (rather important) sage/libs/pari and sage/intergaces/gp, with everything working except (bizarrely) the hyperbolic tangent function.

OK. I can attach some fixes for lcalc later, but I am stuck for genus2reduction.


---

Comment by drkirkby created at 2010-07-20 10:15:55

Replying to [comment:79 cremona]:

> I think we will have a better chance of a positive reaction if we could report to pari a failure to build of pari as such and not pari-in-Sage, since they would reasonably reposond that as we patch some files they cannot be responsible.  For this, just copy the src directory of the most recent spkg (or wait until I put up p5 later today) and try it directly, after ./Configure <whatever-params> and make whatever.
> 

John,
 
I'm going to attach to the ticket a failure observed with the Pari source code directly - outside of Sage. No compiler flags were set. 

The hack of mine in Sage (adding `-fPIC`) resolves this, but it would be better if it could be fixed upstream. The file was actually 5.1 MB in size, as there are over 95,000 error messages. I've reduce the filed to 23 KB, but removing tons of very similar looking messages. See the file:

`Pari-trunk-failure-on-OpenSolaris_x64.log.txt`

There are similar issues on Solaris 10 SPARC. I can attach a log if needed, or someone can just try to build on 't2' outside of Pari. You will see very similar. 

I believe this should be applied on all platforms, as it will be more reliable. The code should be position independent if you are building shared libraries. 

Dave 

Dave


---

Comment by drkirkby created at 2010-07-20 10:22:41

Failure of Pari source code to build outside of Sage on an OpenSolaris machine


---

Attachment

Replying to [comment:83 drkirkby]:

> There are similar issues on Solaris 10 SPARC. I can attach a log if needed, or someone can just try to build on 't2' outside of Pari. You will see very similar. 
> 
> I believe this should be applied on all platforms, as it will be more reliable. The code should be position independent if you are building shared libraries. 
> 
> Dave 

I mean someone could try this on 't2.math.washington.edu' without using Sage. I'm sure William would set up an account for a Pari developer. They only need the Pari source - no Sage code to reproduce this error. 

Dave


---

Comment by jdemeyer created at 2010-07-20 11:05:09

I have sent a bug report to the PARI people about Solaris: [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1078](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1078)


---

Comment by cremona created at 2010-07-20 11:20:26

Replying to [comment:82 fbissey]:
> Replying to [comment:81 cremona]:
> > Replying to [comment:80 fbissey]:
> > > Am I the only one seeing problems with lcalc and genus2reduction?
> > 
> > I don't think you are.  I have been sorting out other things!  I have just finished with the (rather important) sage/libs/pari and sage/intergaces/gp, with everything working except (bizarrely) the hyperbolic tangent function.
> 
> OK. I can attach some fixes for lcalc later, but I am stuck for genus2reduction.

In my current setup, sage/interfaces/genus2reduction passes, as does sage/lfunctions/lcalc. 

I did not need to make any changes to lcalc!


---

Comment by fbissey created at 2010-07-20 11:29:55

I am not talking about any tests. I didn't check that.
I was talking about building them.
And from what I am just digging, the failure for genus2reduction
is not just my set up.


---

Comment by cremona created at 2010-07-20 11:41:21

Replying to [comment:87 fbissey]:
> I am not talking about any tests. I didn't check that.
> I was talking about building them.
> And from what I am just digging, the failure for genus2reduction
> is not just my set up.

OK, I misunderstood.  I am working on sage-4.5 + the p4 spkg + all patches on this ticket (to both sage lib and extcode) + what I have done since then.  While you are working on building spkgs which use pari, right? That's an entirely different set of problems to solve.  Have you tried asking the authors of those spkgs (or rather, of the packages themselves) to help out?


---

Comment by fbissey created at 2010-07-20 11:50:46

Replying to [comment:88 cremona]:
> Replying to [comment:87 fbissey]:
> > I am not talking about any tests. I didn't check that.
> > I was talking about building them.
> > And from what I am just digging, the failure for genus2reduction
> > is not just my set up.
> 
> OK, I misunderstood.  I am working on sage-4.5 + the p4 spkg + all patches on this ticket (to both sage lib and extcode) + what I have done since then.  While you are working on building spkgs which use pari, right? That's an entirely different set of problems to solve.  Have you tried asking the authors of those spkgs (or rather, of the packages themselves) to help out?

Not yet. I think William is upstream for genus2reduction. 


I thought it should be attached to that ticket. I haven't seen any other
ticket about converting those spkg to pari-2.4.


you are probably right that they should have separate ticket but they should
block this one then. No use upgrading pari if it breaks other spkgs.


eclib builds fine. OK now I should go what was Dave acronym,
MWWKM (my wife will kill me or something :) ).


---

Comment by jdemeyer created at 2010-07-20 13:07:22

This trac is finding a continuous stream of PARI bugs.  Another one: [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079)


---

Comment by cremona created at 2010-07-20 13:36:06

Replying to [comment:89 fbissey]:
> Replying to [comment:88 cremona]:
> > Replying to [comment:87 fbissey]:
> > > I am not talking about any tests. I didn't check that.
> > > I was talking about building them.
> > > And from what I am just digging, the failure for genus2reduction
> > > is not just my set up.
> > 
> > OK, I misunderstood.  I am working on sage-4.5 + the p4 spkg + all patches on this ticket (to both sage lib and extcode) + what I have done since then.  While you are working on building spkgs which use pari, right? That's an entirely different set of problems to solve.  Have you tried asking the authors of those spkgs (or rather, of the packages themselves) to help out?
> 
> Not yet. I think William is upstream for genus2reduction. 


Good.

> 
> I thought it should be attached to that ticket. I haven't seen any other
> ticket about converting those spkg to pari-2.4.

> 
> you are probably right that they should have separate ticket but they should
> block this one then. No use upgrading pari if it breaks other spkgs.

> 

I agree -- if other spkgs need their source fixing they should on other tickets, one each, and we should have a list here.

> eclib builds fine.

Of course it does!

 OK now I should go what was Dave acronym,
> MWWKM (my wife will kill me or something :) ).


---

Comment by cremona created at 2010-07-20 13:38:23

Replying to [comment:90 jdemeyer]:
> This trac is finding a continuous stream of PARI bugs.  Another one: [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079)

Good work!  I am down to 10 files (only!) in sage library with failing doctests, including 7 in rings.number_fields which I am leaving to you.  I will try to fix the other three before quitting for a bit (after uploading a patch of course -- currently 1768 lines since the ones posted here, and counting).


---

Attachment

Apply to 4.5: replaces ALL previous sagelib patches


---

Comment by cremona created at 2010-07-20 14:49:36

sagelib_9343-combined-new.patch replaces all previous sagelib patches.  With this and the *two* extcode patches (extcode_9343.patch and 9343_extcode_dokchitser-1.patch) I get only the following doctest failures:

6 in number_fields:


```
	sage -t  devel/sage-main/sage/rings/number_field/maps.py # 34 doctests failed
	sage -t  devel/sage-main/sage/rings/number_field/number_field_ideal_rel.py # 17 doctests failed
	sage -t  devel/sage-main/sage/rings/number_field/number_field_ideal.py # 17 doctests failed
	sage -t  devel/sage-main/sage/rings/number_field/number_field_rel.py # 20 doctests failed
	sage -t  devel/sage-main/sage/rings/number_field/number_field_element.pyx # 2 doctests failed
	sage -t  devel/sage-main/sage/rings/number_field/number_field.py # 47 doctests failed
```

which I think Jeroen is looking after, and  1 in elliptic_curves (rlm informed and passed buck to was):

```
	sage -t  devel/sage-main/sage/schemes/elliptic_curves/heegner.py # 6 doctests failed
```

There is also a failing doctest for tanh in libs/pari/gen.pyx which I disabled temporarily.  And there may be some doctests needing different 32-bit output;  but I have done enough for now.

Independently of this I have upgraded the spkg to the latest svn,  made the relavant changes to the patches in it, and added a spkg-test (with help from David Kirkby).  I will put up a link to that when I have succeeded in spkg-ing it.


---

Comment by cremona created at 2010-07-20 16:04:54

Amazing discovery -- the script spkg-install is VERY broken, even the one currently distributed with sage 4.5!

There are several lines like 

```
# pjeremy: fix for FreeBSD: #7825
cp "$TOP"/patches/get_kernel config/
```

which should say

```
# pjeremy: fix for FreeBSD: #7825
cp "$TOP"/patches/get_kernel src/config/
```

(note the missing "src").

If I am right, how come anything works?  I mean, if these patches are supposedly essential, but are in effect not being applied, maybe they are not so essential after all?

I can change these to be "correct";  but am more tempted to delete them and see what happens...thoughts?


---

Comment by cremona created at 2010-07-20 16:45:08

There is a new version of the spkg here: http://www.warwick.ac.uk/staff/J.E.Cremona/pari-2.4.3.svn.p5.spkg

It includes the spkg-check which now works (i.e. it runs iff SAGE_CHECK is 'yes', and the tests pass.  On my machine at least).


---

Comment by mhansen created at 2010-07-20 17:16:48

I get the following error in Cygwin:


```

gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers  -o trans3.o ../src/basemath/trans3.c
bison -d ../src/language/parse.y -o ../src/language/parse.c
make[1]: bison: Command not found
make[1]: *** [../src/language/parse.h] Error 127
make[1]: Leaving directory `/home/mhansen/sage-4.3.5/spkg/build/pari-2.4.3.svn.p5/src/Ocygwin-i686'
make: *** [gp] Error 2
```


I don't believe that we require bison to be installed.


---

Comment by drkirkby created at 2010-07-20 17:27:07

Replying to [comment:94 cremona]:
> Amazing discovery -- the script spkg-install is VERY broken, even the one currently distributed with sage 4.5!
> 
> There are several lines like 
> {{{
> # pjeremy: fix for FreeBSD: #7825
> cp "$TOP"/patches/get_kernel config/
> }}}
> which should say
> {{{
> # pjeremy: fix for FreeBSD: #7825
> cp "$TOP"/patches/get_kernel src/config/
> }}}
> (note the missing "src").
> 
> If I am right, how come anything works?  I mean, if these patches are supposedly essential, but are in effect not being applied, maybe they are not so essential after all?
> 
> I can change these to be "correct";  but am more tempted to delete them and see what happens...thoughts?

I think you are mistaken John. Further up the script is 


```
cd src
```


so another `src` would be an error. 

I do sometimes think it is better to perhaps consider deleting all patches. I have just updated 'GSL' (#9533). GSL is a much simpler package I admit. I removed all patches. The new GSL package has built and passed all self-tests on Cygwin, Linux, HP-UX, OpenSolaris, OS X and Solaris. (Sage does not build fully on HP-UX, but enough of it builds to prove that GSL passes all tests). 

I hope at some point you are going to test on 't2'. I simply do not have the time to test everyones updates on 't2'. 

Dave


---

Comment by cremona created at 2010-07-20 17:37:42

Replying to [comment:97 drkirkby]:
>
> I think you are mistaken John. Further up the script is 
> 
> {{{
> cd src
> }}}
> 
> so another `src` would be an error. 
> 

You are right -- I cross-poseted to sage-devel where this was pointed out to me.

> I do sometimes think it is better to perhaps consider deleting all patches. I have just updated 'GSL' (#9533). GSL is a much simpler package I admit. I removed all patches. The new GSL package has built and passed all self-tests on Cygwin, Linux, HP-UX, OpenSolaris, OS X and Solaris. (Sage does not build fully on HP-UX, but enough of it builds to prove that GSL passes all tests). 
> 
> I hope at some point you are going to test on 't2'. I simply do not have the time to test everyones updates on 't2'. 
> 

Well I hope someone is, but I'm busy with other things for the next 2 days and then away for 3 weeks without opportunity to do Sage stuff.

> Dave


---

Attachment

Some fixes in sage/rings/number_fields and doctest changes in sage/rings/polynomial/polynomial_element.pyx


---

Comment by jdemeyer created at 2010-07-21 13:00:16

I did a complete from scratch build of sage-4.5.1 with the new patches and did a long doctest.  I got some more errors than John:


```
        sage -t -long devel/sage-test/sage/schemes/elliptic_curves/heegner.py # 7 doctests failed
        sage -t -long devel/sage-test/sage/rings/number_field/number_field.py # 18 doctests failed
        sage -t -long devel/sage-test/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed
        sage -t -long devel/sage-test/sage/schemes/elliptic_curves/ell_generic.py # 1 doctests failed
        sage -t -long devel/sage-test/sage/rings/number_field/number_field_rel.py # 3 doctests failed
        sage -t -long devel/sage-test/sage/rings/number_field/number_field_element.pyx # 2 doctests failed
        sage -t -long devel/sage-test/sage/rings/number_field/number_field_ideal.py # 17 doctests failed
        sage -t -long devel/sage-test/sage/rings/number_field/number_field_ideal_rel.py # 3 doctests failed
        sage -t -long devel/sage-test/doc/en/constructions/algebraic_geometry.rst # 2 doctests failed
        sage -t -long devel/sage-test/sage/interfaces/gp.py # 2 doctests failed
        sage -t -long devel/sage-test/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed
```


Some are probably because John did not do "long" doctests, but also in some cases I get PariError: not enough memory.  For example:

```
File "/usr/local/src/sage-newpari-4.5.1/devel/sage-test/sage/schemes/elliptic_curves/ell_generic.py", line 2646:
    sage: [t[1] for t in EllipticCurve(GF(10^60+3201),[0,a,0,b,0])._p_primary_torsion_basis(2)]
Exception raised:
[...]
    PariError: not enough memory (28)
```


I will have a look at these errors and see what I can fix.


---

Comment by jdemeyer created at 2010-07-21 15:15:19

Fixes all doctests in sage/rings/number_fields (except for PARI bug 1079)


---

Attachment

All doctests are now fixed, except for some which hit [PARI bug 1079](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079) and some in sage/schemes/elliptic_curves.  Apparently, the PARI update increased the memory requirements of some of the doctests, making them fail on my machine with 3GB RAM.  However, these doctests already take a lot of memory with the vanilla sage 4.5.1, see also [my post at sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/4d4b9a8203b13f22).


---

Comment by cremona created at 2010-07-21 15:54:49

For more on the bison issue see the pari-dev thread here: http://pari.math.u-bordeaux.fr/archives/pari-dev-1007/msg00011.html

It seems that we should not use an svn source grad in our distribution but a "proper PARI tarball".  An explanation of how to create such a thing is I hope forthcoming on that thread.

Secondly, the thread http://pari.math.u-bordeaux.fr/archives/pari-dev-1007/msg00015.html makes some releavnt comments (and asks a question) on Dave's other points.


---

Comment by drkirkby created at 2010-07-21 16:31:25

Replying to [comment:102 cremona]:
> For more on the bison issue see the pari-dev thread here: http://pari.math.u-bordeaux.fr/archives/pari-dev-1007/msg00011.html
> 
> It seems that we should not use an svn source grad in our distribution but a "proper PARI tarball".  An explanation of how to create such a thing is I hope forthcoming on that thread.
> 
> Secondly, the thread http://pari.math.u-bordeaux.fr/archives/pari-dev-1007/msg00015.html makes some releavnt comments (and asks a question) on Dave's other points.

Bison, like autoconf and automake should not be necessary for end-users. Often developer additions don't have a 'configure' script - they rely on other developers making that from configure.ac. It is the same with bison - some files only need to be geneated and passed to the end users. As long as the timestamp on the files generated by bison is more recent than the files they were generated from, bison should not be necessary. 

With regard to my own Solaris issue with -fPCI, shared libraries and Pari, I'm not sure how to observe what is happening, or where I can follow the Pari bug numbers referenced. Essentially one of the Pari developers disagreed with me, and said it is not necessary to use -fPIC when compiling 32-bit shared libraries on Solaris - only 64-bit ones. I responded that this is not so, and provided a link to something written by Casper Dik (a very knowledge Sun employee), that -fPIC is necessary. I gather that was passed on, but I don't see any record of it. 

There's also the point I made that Pari is looking for a different version of GMP to what is in Sage when building a 64-bit version of Pari. The Pari developer believes it is finding another version before that one in Sage. *IF* that is so, that needs fixing in Sage. Somehow we need to ensure Pari first looks for the libraries in $SAGE_LOCAL/lib, and not in /usr/lib, /usr/local, or wherever else Pari may chose to look. The whole point of shipping a bunch of standard libraries with Sage is we know what ones are are used by Sage. 

Dave


---

Comment by cremona created at 2010-07-21 17:01:02

Note that there are two relevant threads since I posted to pari-dev (a mailing list linked to a couple of comments above this) but Jeroen posted directly to the PARI bug tracking system.  I suggested on pari-dev that the discussion should take place on the tracking system.


---

Comment by jdemeyer created at 2010-07-22 16:57:35

I have made a new version of the spkg:
[http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p6.spkg](http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p6.spkg)

It contains a patch for PARI bug 1079, fixing all doctest failures in sage/rings/number_fields.

I also added a script "spkg-make" which automates the process of building the spkg (it downloads the svn sources and so on).  It *should* also fix the bison issue.  This spkg-make is highly experimental, but it works for me.  By all means, go ahead and tell me what you think of it.


---

Comment by cremona created at 2010-07-22 17:39:46

Replying to [comment:105 jdemeyer]:
> I have made a new version of the spkg:
> [http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p6.spkg](http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p6.spkg)
> 
> It contains a patch for PARI bug 1079, fixing all doctest failures in sage/rings/number_fields.
> 
> I also added a script "spkg-make" which automates the process of building the spkg (it downloads the svn sources and so on).  It *should* also fix the bison issue.  This spkg-make is highly experimental, but it works for me.  By all means, go ahead and tell me what you think of it.

I'll try it if I get a chance over the next couple of days.

As I see it there are now two main issues:

   1. Make sure that the other spkgs which use the pari library still work.  I think someone said that genus2reduction and lcalc have problems.
   2. Rebase to 4.5.2.


---

Comment by drkirkby created at 2010-07-22 18:50:34

I just got an email from Karim Belabas, a Pari developer, that they are going to change Pari so it compiles with -fPIC on all platforms. (This is Pari bug 1078)

I've no idea how long it will take them to integrate that patch, but hopefully not too long. Once integrated, the patches for Linux PPC and Solaris in Sage that add -fPIC can be removed. 

Dave


---

Comment by drkirkby created at 2010-07-22 19:13:23

Replying to [comment:105 jdemeyer]:
> I have made a new version of the spkg:
> [http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p6.spkg](http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p6.spkg)
> 
> It contains a patch for PARI bug 1079, fixing all doctest failures in sage/rings/number_fields.
> 
> I also added a script "spkg-make" which automates the process of building the spkg (it downloads the svn sources and so on).  It *should* also fix the bison issue.  This spkg-make is highly experimental, but it works for me.  By all means, go ahead and tell me what you think of it.

I tried it on OpenSolaris. There are a few error messages:


Here's the first

```
Checking for optional libraries and headers...
...Found libgmp in /export/home/drkirkby/sage-4.5/local/lib
...Found gmp header in /export/home/drkirkby/sage-4.5/local/include
ld.so.1: solaris-ix86-rlv10703: fatal: libgmp.so.10: open failed: No such file or directory
./Configure[79]: .: line 38: 10904: Killed
### Your version of GMP is too old for PARI. Please upgrade
### Building without GNU MP support
```


*This is a new bug first seen in Pari 2.4.3 and does not appear in Pari 2.3.5*

And another. 

```
Checking for optional libraries and headers...
...Found libgmp in /export/home/drkirkby/sage-4.5/local/lib
...Found gmp header in /export/home/drkirkby/sage-4.5/local/include
ld.so.1: solaris-ix86-rlv10703: fatal: libgmp.so.10: open failed: No such file or directory
./Configure[79]: .: line 38: 10904: Killed
### Your version of GMP is too old for PARI. Please upgrade
### Building without GNU MP support
```


I've seen this before, but it is very odd, as other packages in Sage use the readline, and clearly readline is used when Sage runs - i.e. I have edit the command line, recall previous commands etc. 

And another problem with that package. 


```
../src/test/dotest[30]: cat: /../patches/status: cannot open [No such file or directory]
```


* This is new to pari-2.4.3.svn.p6.log and does not appear in earlier pari 2.4.3 packages which have been posted on this ticket*


IMHO, it would be good if the package number included the snv snapshot - in this case 12541. 

Dave


---

Comment by drkirkby created at 2010-07-22 19:15:49

I wrote the same bug twice there. Here's the second bug:


```
Hi-Res Graphics: none
...Found libreadline in /export/home/drkirkby/sage-4.5/local/lib
...Found readline header in /export/home/drkirkby/sage-4.5/local/include/readline
...Found history header in /export/home/drkirkby/sage-4.5/local/include/readline
...Found libtermcap in /export/home/drkirkby/sage-4.5/local/lib/
...Library termcap needed by readline
###
### Readline library detected, but does not seem to work
###
### Building without GNU readline support
```


I've seen this before, but it is very odd, as other packages in Sage use the readline, and clearly readline is used when Sage runs - i.e. I have edit the command line, recall previous commands etc.

Dave


---

Comment by drkirkby created at 2010-07-22 19:32:37

Have the other issues that are circumvented by hacks to spkg-install been reported upstream? Such as:


```
# These two are needed so that Sage can catch pari's error signals. 
cp "$PATCHED/init.c"  src/language/init.c
cp "$PATCHED/mp.c"    src/kernel/gmp/mp.c 
```


Then's these this not very clearly documented patch

```
cp "$PATCHED/get_dlld" config/
```


And another, this time a bit better documented, though no trac number. 

```
# mabshoff: This patch is to get around problem in PPC 32-bit Linux build
# (but it is ok on any other machine)
cp "$PATCHED/get_dlcflags" config/
```

(That is probably the -fPIC issue which will soon be able to be removed)


```
# pjeremy: fix for FreeBSD: #7825
cp "$PATCHED/get_kernel" config/
```


Then this. 

```
# cwitty: disable -rpath
cp "$PATCHED/get_ld" config/
```


And another. 

```
# This is needed or there are weird locale problems involving rpath
# with building Sage.
LC_ALL=C
export LC_ALL
LANG=C
export LANG
```


And another


```
    if [ "$UNAME" = "CYGWIN" ]; then
        # There are weird bugs in PARI's build process on Windows XP
        # under Cygwin.
        # Passing in this extra flag gets around the bug.
        $MAKE GMPINCLUDE=-I$SAGE_LOCAL/include EXTRADLLDFLAGS=-lgmp gp
    else
        $MAKE gp
    fi
```


And another



```
        # Also another patch since paripriv.h won't compile right on OS X
        # when used by client Sage code.  So we replace it by a slightly
        # modified version.
        cp -pf "$PATCHED/paripriv.h" "$SAGE_LOCAL/include/pari/paripriv.h"
```


That's a lot of patches to one program. How many of these issues have been raised? Personally, I would be very tempted to remove these, and find what fails. Otherwise maintenance of the package is going to be very difficult. 

Dave


---

Comment by fbissey created at 2010-07-22 20:30:47

Hi Dave we have some of these patch as well in Gentoo (and I mean in the distro
itself not just sage-on-gentoo). So I can fill in some gaps.


get_dlld: we have this

```
	# propagate ldflags
	sed -i \
		-e 's/-shared $extra/-shared $extra \\$(LDFLAGS)/' \
		config/get_dlld || die "Failed to fix LDFLAGS"
```

We add -fpic on all platforms when building the library but not gp or static libraries. 

But we have a patch I think originating from Debian to add support 
for linux ppc 32 bits.

get_ld: when gp is compiled it uses libpari and is compiled -rpath to hardcode the libray location. I am not sure this is strictly necessary.



Not sure about the CYGWIN and OS X stuff.


---

Comment by cremona created at 2010-07-22 20:33:07

It's worth remembering too that Bill Alombert is (or was) a debian developer so should know a lot of these issues.


---

Comment by jdemeyer created at 2010-07-22 21:02:52

Replying to [comment:110 drkirkby]:
> Have the other issues that are circumvented by hacks to spkg-install been reported upstream?

> That's a lot of patches to one program. How many of these issues have been raised? Personally, I would be very tempted to remove these, and find what fails. Otherwise maintenance of the package is going to be very difficult. 

I agree that all the patches in config/* dealing with compiling PARI/GP really are upstream issues and should be fixed there.  Also, now that we upgrade PARI to 2.4.3, it is not at all clear whether these patches are still needed.


---

Comment by jdemeyer created at 2010-07-22 21:05:29

Replying to [comment:108 drkirkby]:
> And another problem with that package. 
> 
> {{{
> ../src/test/dotest[30]: cat: /../patches/status: cannot open [No such file or directory]
> }}}

My fault.  I uploaded a new [http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p6.spkg](http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p6.spkg) which should fix this.  (This is a small hack I added such that the SVN version is saved in patches/status such that it can appear in gp.version() for example).


---

Comment by drkirkby created at 2010-07-22 21:20:12

Replying to [comment:113 jdemeyer]:
> Replying to [comment:110 drkirkby]:
> > Have the other issues that are circumvented by hacks to spkg-install been reported upstream?
> 
> > That's a lot of patches to one program. How many of these issues have been raised? Personally, I would be very tempted to remove these, and find what fails. Otherwise maintenance of the package is going to be very difficult. 
> 
> I agree that all the patches in config/* dealing with compiling PARI/GP really are upstream issues and should be fixed there.  Also, now that we upgrade PARI to 2.4.3, it is not at all clear whether these patches are still needed.

I got this email  from Bill Allombert on the `Bug#1078: Pari, -fPIC and Solaris` thread:


```
On 07/22/10 09:46 PM, Bill Allombert wrote:
> On Thu, Jul 22, 2010 at 07:33:45PM +0100, Dr. David Kirkby wrote:
>> The Sage developers will look forward to a snapshot were we can
>> disable the patches for Solaris and PPC.
> 
> Well, the Sage PPC fix is wrong and the correct fix is in PARI 2.3.5 which was released
> in February, so I do not see why sage still carry it.
> 
> Cheers,
> Bill.
> 
```


So it seems we should remove the -fPIC patch for PPC Linux, and the -fPIC patch for Solaris will be able to be removed later, but not yet. 

IMHO, it would be better to remove all the patch (or just comment them out for now), and put them back as and when they are needed, taking care (where possible), to check if the bugs they are supposed to fix reoccur. This is one of the more messy spkg-install files I've seen - though the ATLAS one is pretty messy too!

Dave


---

Attachment

Combined sagelib patch against sage-4.5.2.alpha0, removes discrete log patch


---

Comment by drkirkby created at 2010-07-23 11:02:34

I'm told by Bill Allombert, a Pari developer, that they have now enabled -fPIC on all platforms in build 12542. So all hacks in Sage to add -fPIC on Linux PPC and Solaris can be removed if that build or later is used. 

Dave


---

Comment by jdemeyer created at 2010-07-23 13:08:13

New spkg version: [http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p7.spkg](http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p7.spkg), PARI build 12543.  The only changes are in the build process.  I also removed several patches, 
since the fixes should be upstream now.

But we need to test building this spkg on many different machines!

There are some new doctest failures with sage-4.5.2.alpha0, nothing very troublesome though.  I can probably fix them (except for elliptic_curves, which I will leave to John).


---

Comment by cremona created at 2010-07-23 17:19:51

Perhaps spkg-check should do one of "make dyntest-all" or "make statest-all" instead of "make test-all" (which does both and takes twice as long)?  Since we are only installing one copy of the binary gp (which is what is run in the tests) there's no need to make and test the other.


---

Comment by cremona created at 2010-07-23 17:46:51

Replying to [comment:117 jdemeyer]:
> New spkg version: [http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p7.spkg](http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p7.spkg), PARI build 12543.  The only changes are in the build process.  I also removed several patches, 
> since the fixes should be upstream now.
> 
> But we need to test building this spkg on many different machines!
> 
> There are some new doctest failures with sage-4.5.2.alpha0, nothing very troublesome though.  I can probably fix them (except for elliptic_curves, which I will leave to John).

I applied the p7 spkg fine to 4.5.2.alpha0, and the (two) extcode patches above, and the new sagelib_9343_combined3.patch .

Very impressed that the latter applied without any merge problems -- thanks, Jeroen.  I will test and fix what I find in elliptic_curves (except perhaps the failures in heegner.py).


---

Comment by drkirkby created at 2010-07-23 20:33:18

Replying to [comment:117 jdemeyer]:
> New spkg version: [http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p7.spkg](http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p7.spkg),

Why do you chose that name? The .p7 should only be integrated into Sage where there are 7 previous versions of 2.4.3. Since the software says 


```
Shall we try to build pari 2.4.3 (development svn-12543) now (y/n)? [n]
```


I think a better name would be


```
pari-2.4.3.svn-12543
```


as that is the version of Pari that it is based upon. Then, assuming this version was merged, subsequent updates in Sage would be called pari-2.4.3.svn-12543.p0, pari-2.4.3.svn-12543.p1, pari-2.4.3.svn-12543.p2 etc. 

Certainly, the first revision put into Sage should not have a patch level of 7. 

http://www.sagemath.org/doc/developer/patching_spkgs.html

says _If the upstream package is taken from some revision other than a stable version, you need to append the date at which the revision is made, e.g. the Singular package singular-3-1-0-4-20090818.p3.spkg is made with the revision as of 2009-08-18. _

However, I think in this case, the fact the upstream does have a version number (in this case 2.4.3.svn-12543), that should be used rather than a date. 

Dave 
Dave


---

Comment by cremona created at 2010-07-23 21:04:09

Replying to [comment:119 cremona]:
> Replying to [comment:117 jdemeyer]:
> > New spkg version: [http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p7.spkg](http://cage.ugent.be/~jdemeyer/pari-2.4.3.svn.p7.spkg), PARI build 12543.  The only changes are in the build process.  I also removed several patches, 
> > since the fixes should be upstream now.
> > 
> > But we need to test building this spkg on many different machines!
> > 
> > There are some new doctest failures with sage-4.5.2.alpha0, nothing very troublesome though.  I can probably fix them (except for elliptic_curves, which I will leave to John).
> 
> I applied the p7 spkg fine to 4.5.2.alpha0, and the (two) extcode patches above, and the new sagelib_9343_combined3.patch .
> 
> Very impressed that the latter applied without any merge problems -- thanks, Jeroen.  I will test and fix what I find in elliptic_curves (except perhaps the failures in heegner.py).

There's one test failure in ell_rational_field (extraneous warning output from eclib) which will go away if the patches from #9247 are applied, so I think there is no need to do anything about this at present.

>


---

Attachment

fixes doctests in elliptic_curves/ell_number_field


---

Comment by drkirkby created at 2010-07-24 11:55:12

Replying to [comment:119 cremona]:
> Very impressed that the latter applied without any merge problems -- thanks, Jeroen. 

I wish I could say I was as impressed with the installation on OpenSolaris:


```
Checking for optional libraries and headers...
...Found libgmp in /export/home/drkirkby/sage-4.5.2.alpha0/local/lib
...Found gmp header in /export/home/drkirkby/sage-4.5.2.alpha0/local/include
ld.so.1: solaris-ix86-rlv7589: fatal: libgmp.so.10: open failed: No such file or directory
./Configure[79]: .: line 38: 8207: Killed
### Your version of GMP is too old for PARI. Please upgrade
### Building without GNU MP support
```


The version currently in Sage works fine - this is broken. 

This does not seem an upstream problem, as it builds fine outside of the Sage environment. 

Dave


---

Comment by jdemeyer created at 2010-07-24 11:58:43

I created tickets for genus2reduction (#9591) and lcalc (#9592).


---

Comment by jdemeyer created at 2010-07-24 12:19:29

genus2reduction (#9591) is fixed, download from [http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg](http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg)


---

Comment by drkirkby created at 2010-07-24 12:20:44

Currently in Sage with Pari 2.3.5 there is 

 * `patches/paripriv-osx.h` which gets copied on only OS X 
 * `patches/paripriv-Solaris.h` which gets copied on both Solaris and Cygwin. 


The new version has just patches/files/paripriv.h which gets copied on all 3 operating systems. IIRC, the changes needed on Solaris (and I guess Cygwin, as it uses the Solaris patch) were quite small. The changes needed on OS X were much more significant. Was this an oversight to remove the OS X patch, or a deliberate decision?


---

Comment by jdemeyer created at 2010-07-24 13:12:04

lcalc (#9592) is fixed, download from [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg)


---

Comment by cremona created at 2010-07-24 13:16:41

Replying to [comment:125 jdemeyer]:
> genus2reduction (#9591) is fixed, download from [http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg](http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg)


The bit still in the description about removing sea.gp is redundant since it is already removed in one of the extcode patches. I see that in my patched extcode directory, pari/SEA is still there with empty directories doc and test. Funny, I thought mercurial automatically removed empty directories.

I successfully installed the new genus2reduction spkg and the tests in sage/interfaces/genus2reduction pass. BUT in the spkg directory the changes to SPKG.txt and the src file are not checked in -- better do that!


---

Comment by cremona created at 2010-07-24 13:23:11

Replying to [comment:127 jdemeyer]:
> lcalc (#9592) is fixed, download from [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg)

Did you forget to update SPKG.txt?  This installed OK for me (but there are so many warnings!).  Also, rishi should be kept up-to-date on this, since there are several outstanding lcalc-related tickets (#8621, #8623, #5396, ...)


---

Comment by jdemeyer created at 2010-07-24 13:29:50

> I successfully installed the new genus2reduction spkg and the tests in sage/interfaces/genus2reduction pass. BUT in the spkg directory the changes to SPKG.txt and the src file are not checked in -- better do that!

> Did you forget to update SPKG.txt?

Allright, maybe I was a bit too quick by the excitement of having fixed these!  I just uploaded new versions (with the same filenames).

Now I am doing a complete from-scratch build of Sage with the new spkg's.  This will be a build without any trace of an old version of PARI.  Let's wait and see...


---

Comment by drkirkby created at 2010-07-24 13:49:42

I've found what the problem with the GMP and Readline are on Solaris. Setting CFLAGS to include -m64 flag is not sufficient, but setting 

CC="$CC -m64"

works. 

I also made a few other improvements to spkg-install. 
 * Allow one to set SAGE_DEBUG=yes to set no optimisation. Primarily for debugging purposes, but would also be useful if people (like on Fedora once) found gcc mis-compiled Pari. 
 * Check SAGE_ROOT actually exists as is required in the Sage Developers guide
 * Allow the setting SAGE_TUNE_pari=yes to get increased performance, at a cost of letting Pari do the tuning. 

I changed the filename to show the actual svn version - you can see this reported when you run configure. 

New package at 

http://boxen.math.washington.edu/home/kirkby/patches/pari-2.4.3svn-12543.spkg

That now does build properly on OpenSolaris. 

Dave


---

Comment by drkirkby created at 2010-07-24 13:51:02

Allows GMP and Readline to be found on 64-bit OpenSolaris. Also allows one to tune Pari (using SAGE_TUNE_pari=yes) and compile without optimisation (with SAGE_DEBUG=yes)


---

Attachment


---

Comment by cremona created at 2010-07-24 14:40:37

Replying to [comment:131 drkirkby]:
>
> 
> I changed the filename to show the actual svn version - you can see this reported when you run configure. 
> 
> New package at 
> 
> http://boxen.math.washington.edu/home/kirkby/patches/pari-2.4.3svn-12543.spkg
> 

What I had been planning to say about the spkg's name is:  All the various pari-2.4.3.svn.p?.spkg on this ticket up to now have been alpha things which were never intended for anyone other than those working on this ticket;  and we should give the spkg a proper name (to which further patch levels could be applied later, after this becomes the Sage standard spkg) once we reached something like a beta level, or even after the authors on this ticket were all happy with it.

The latest version may or may not be the final one!  But it gets better every time.

[I may have a little time later today but then I'll be travelling.  In any case, it will soon be time to mark the ticket "needs review" and prod likely suspects to thoroughly test it!]


---

Comment by drkirkby created at 2010-07-24 15:00:34

Replying to [comment:133 cremona]:
> What I had been planning to say about the spkg's name is:  

I would think it worth keeping the svn snapshot number in there at all times. Even for alpha releases, as it's obvious then if its based on a different version of the upstream source code. Those editing this ticket will be in no doubt if the source has changed or not. 

For actual packages in Sage, the Developers Guide says to have the date on SVN snapshots, but since we can get an actual number, that seems more sensible to me. Also, I've found if one puts a date, what often happens is someone updates the package and instead of putting .p0, then just change the date. At that point, the date bears no resemblance to what's in the upstream code on that date. 

Anyway, http://boxen.math.washington.edu/home/kirkby/patches/pari-2.4.3svn-12543.spkg 

will build properly on OpenSolaris. 

I managed to get a core dump when tuning it, but that's less of an issue. I will report that upstream. I've found Bill very helpful. I've just reported the CC/CFLAGS bug upstream, though have got no feedback yet. 

I can see tuning Pari is slow. I can build Pari in 33 seconds on this machine, but it was 24 minutes until I got a core dump when tuning. So I don't know how long tuning would take. But it seems sensible to give the user that option if they are blessed with lots of computer power or lots of patience. Looking at some of the timing data, it looked like the differences in algorithms was significant, and so worth optimising if you want to make a lot of use of Pari. 

BTW, the source code in that package is the same as created by jdemeyer, and is not the latest upstream code as I write. But I chose not to change the source code - just spkg-install, so it will work properly on OpenSolaris. 

Dave 
Dave


---

Comment by drkirkby created at 2010-07-24 15:09:28

I just noticed this error in spkg-install:


```
cp: cannot access /export/home/drkirkby/sage-4.5.2.alpha0/spkg/build/pari-2.4.3svn-12543/patches/files/get_dlld
```


That's nothing I've touched - it appears in the previous version too. Seems like a patch that one tries to apply does not actually exist. 

Dave


---

Attachment

Minor improvements to spkg-check. Correct list of dependancies in SPKG.txt - they are MPIR, readline and termcap.


---

Comment by drkirkby created at 2010-07-24 21:58:44

As noted, I improved spkg-check a bit. I just overwrote the package here

http://boxen.math.washington.edu/home/kirkby/patches/pari-2.4.3svn-12543.spkg

SPKG.txt needs to have all the changes made put into the file. It previously said the dependancy was GMP, but in fact it depends on MPIR, termcap and readline. Luckily `spkg/standard/deps` does have the dependencies correctly listed.


---

Comment by jdemeyer created at 2010-07-24 21:59:10

Flattening of all extcode patches against sage-4.5.2.alpha0


---

Attachment

drkirkby: is there a reason you always put the "-g" flag with CFLAGS?  I assume it is a mistake, but I'm asking just in case it isn't.


---

Comment by drkirkby created at 2010-07-24 22:13:28

Replying to [comment:137 jdemeyer]:
> drkirkby: is there a reason you always put the "-g" flag with CFLAGS?  I assume it is a mistake, but I'm asking just in case it isn't.
It was agreed long ago on sage-devel that packages would be built with debugging information by default, since it makes finding bugs a lot easier. I initially thought that was a bad idea, as it increases the size of the objects. But it is negligible, and it makes no difference to run-time, so I concede it is sensible. That's the reason for the -g

Some software packages add -g anyway, in which case it could be removed, though I'm not sure its a good idea, since if the software changes that behaviour, we have lost the ability to easily debug problems. 

Dave


---

Comment by jdemeyer created at 2010-07-24 23:11:13

New version of the PARI spkg: [http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3svn-12549.spkg](http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3svn-12549.spkg).

Removed the non-existent get_dlld patching.
Cleaned up patches/README.txt


---

Comment by jdemeyer created at 2010-07-24 23:18:00

Breaking news: I have succesfully built Sage 4.5.2.alpha0 from scratch with all the updates so far (without any trace of the old PARI package).  This means that no other spkg's have to be fixed.

So I think the TODO list reduces to:
 1. Fixing the remaining doctest failures.
 2. Testing on as many platforms as possible.
 3. Reviewing everything and cleaning up.

I can help with the first and third of these, but not really the second.


---

Comment by drkirkby created at 2010-07-24 23:31:46

Replying to [comment:139 jdemeyer]:
> New version of the PARI spkg: [http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3svn-12549.spkg](http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3svn-12549.spkg).
> 
> Removed the non-existent get_dlld patching.
> Cleaned up patches/README.txt
I assumed you updated the source code, since the svn number is incremented. This unfortunately fails for me now


```
* Testing zn 	for gp-sta..TIME=2	for gp-dyn..TIME=3
+++ [BUG] Total bench for gp-sta is 164083
+++ [BUG] Total bench for gp-dyn is 171336

PROBLEMS WERE NOTED. The following files list them in diff format: 
Directory: /export/home/drkirkby/sage-4.5.2.alpha0/spkg/build/pari-2.4.3svn-12549/src/Osolaris-ix86
	compat-sta.dif
	trans-sta.dif
	compat-dyn.dif
	trans-dyn.dif
make[1]: *** [test-all] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5.2.alpha0/spkg/build/pari-2.4.3svn-12549/src/Osolaris-ix86'
make: *** [test-all] Error 2
Pari failed the self-tests when running 'make test-all'
*************************************
Error testing package ** pari-2.4.3svn-12549 **
*************************************
```

That is on a Sun Ultra 27 running OpenSolaris. Pari builds fine, but fails the self-tests. 

http://boxen.math.washington.edu/home/kirkby/patches/pari-2.4.3svn-12543.spkg passes all tests. Could the issue be that John's patches which stop a couple of the tests running, are no longer integrated? (I believe he added them as there is no database here, so some tests will fail). 

Dave


---

Comment by jdemeyer created at 2010-07-25 08:40:38

> http://boxen.math.washington.edu/home/kirkby/patches/pari-2.4.3svn-12543.spkg passes all tests. Could the issue be that John's patches which stop a couple of the tests running, are no longer integrated? (I believe he added them as there is no database here, so some tests will fail). 

No, the problem is upstream.  Building PARI from SVN (outside of Sage, that is) now fails make test-all.  I am reverting to 12546, that seems to work.


---

Comment by drkirkby created at 2010-07-25 08:56:55

Replying to [comment:142 jdemeyer]:

> No, the problem is upstream.  Building PARI from SVN (outside of Sage, that is) now fails make test-all.  I am reverting to 12546, that seems to work.

`make test-all`

will always fail with just the upstream source unless some of the tests are disabled, since they rely on one or more databased that are not in Sage unless optional components are installed. 

Dave


---

Comment by jdemeyer created at 2010-07-25 10:17:11

Working version: [http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12546.spkg](http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12546.spkg).  The failures really are upstream, since PARI svn-12546 built outside of Sage passes all tests (note that I have installed the optional PARI databases).


---

Comment by jdemeyer created at 2010-07-26 17:54:07

Fix RR(0.0), clean up


---

Attachment

The last patch fixes the tanh() issue, it was caused by RR(0.0)._pari_() creating an invalid GEN (it took me a very long time to figure this out).

I added a debug() function to gen objects calling dbgGEN() from the pari library, example:

```
sage: pari('[1/2, 1.0*I]').debug()  # random addresses
[&=0000000004c5f010] VEC(lg=3):2200000000000003 0000000004c5eff8 0000000004c5efb0
  1st component = [&=0000000004c5eff8] FRAC(lg=3):0800000000000003 0000000004c5efe0 0000000004c5efc8
    num = [&=0000000004c5efe0] INT(lg=3):0200000000000003 (+,lgefint=3):4000000000000003 0000000000000001
    den = [&=0000000004c5efc8] INT(lg=3):0200000000000003 (+,lgefint=3):4000000000000003 0000000000000002
  2nd component = [&=0000000004c5efb0] COMPLEX(lg=3):0c00000000000003 00007fae8a2eb840 0000000004c5ef90
    real = gen_0
    imag = [&=0000000004c5ef90] REAL(lg=4):0400000000000004 (+,expo=0):6000000000000000 8000000000000000 0000000000000000
```


Apart from that, a lot of cleanups, and some more doctests.

As far as I can tell, everything works now on my system, apart from some doctest failures in elliptic_curves (again, I do not plan to look at this).


---

Attachment

Disables failing doctests in elliptic_curves


---

Comment by jdemeyer created at 2010-07-26 21:32:27

I believe now we are ready to test this enormous patch.  Since there are 5 spkg's involved (sage, extcode, pari, genus2reduction, lcalc), the only sensible way to test this is to do a complete build from scratch.  To make that process easier, I have uploaded a full Sage distribution with the patches applied to [http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.alpha0-9343.tar](http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.alpha0-9343.tar).  Just doing `make` should be enough to build it.

The following tickets are included:
 * #9343
 * #9591
 * #9592
 * #9595

I invite you all to test it!


---

Comment by jdemeyer created at 2010-07-26 21:36:09

Changing assignee from tbd to jdemeyer.


---

Comment by jdemeyer created at 2010-07-27 07:47:33

Fix pari(...).sizebyte(), add pari(...).sizeword()


---

Attachment

Flattening of all the above sagelib patches


---

Comment by drkirkby created at 2010-07-27 11:57:05

Replying to [comment:147 jdemeyer]:
> I believe now we are ready to test this enormous patch.  Since there are 5 spkg's involved (sage, extcode, pari, genus2reduction, lcalc), the only sensible way to test this is to do a complete build from scratch.  To make that process easier, I have uploaded a full Sage distribution with the patches applied to [http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.alpha0-9343.tar](http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.alpha0-9343.tar).  Just doing `make` should be enough to build it.

This built OK on Solaris 10 (SPARC) using t2.math. A quick check showed Sage functioned - i.e. did not do something stupid like segfault. I am running ` make ptestlong`

Dave


---

Comment by jdemeyer created at 2010-07-27 12:36:37

I am testing on a 32-bit Linux system.  The build went fine, there seem to be a few doctest errors though: we might need to special-case 32 vs. 64 bits in some places.

Now that sage-4.5.2alpha1 is released, I will check whether the patches still apply properly.


---

Comment by cremona created at 2010-07-27 12:44:17

Great work Jeroen.  I am testing on a 64-bit Linux system and will report back (but not very soon, I am in a hotel inNew Jersey and will not be back till late this evening Eastern Time).

Shall we suggest via sage-release that after 4,5,2 is out, a whole release is devoted to this upgrade?  It makes sense to me.  If you agree, do it.


---

Comment by jdemeyer created at 2010-07-27 12:51:58

Replying to [comment:151 cremona]:
> Shall we suggest via sage-release that after 4,5,2 is out, a whole release is devoted to this upgrade?  It makes sense to me.  If you agree, do it.

Excellent idea.  I especially like it because there are so many things depending on PARI.  I expect for example several doctest failures in the 4.5.2alpha0 -> 4.5.2alpha1 upgrade.


---

Comment by drkirkby created at 2010-07-27 15:25:58

There were several failures on  t2.math.washington.edu. I've put details of the hardware here, since over time hardware changes, so anyone looking back in a couple of years will be able to know the exact conditions. 

## Hardware and software configuration of t2.math.washington.edu
 * [Sun SPARC Enterprise T5240 Server](http://www.oracle.com/us/products/servers-storage/servers/sparc-enterprise/t-series/031584.htm) 
 * 2 x 1167 MHz [UltraSPARC T2 PLUS](http://www.oracle.com/us/products/servers-storage/microelectronics/031459.htm) processors. (16 cores and 128 hardware threads in total). 
 * 32 GB RAM
 * No swap devices configured. 
 * Solaris 10 update 7 (5/09)
 * gcc 4.4.1 configured to use the Sun linker and Sun assembler. 
 * Sage was built in on a local ZFS file system as a 32-bit application.

See the file Solaris-10-SPARC-ptestlong-failures.log


```
The following tests failed:

        sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py # 1 doctests failed
        sage -t  -long devel/sage/sage/lfunctions/dokchitser.py # 4 doctests failed
        sage -t  -long devel/sage/sage/symbolic/expression.pyx # 1 doctests failed
        sage -t  -long devel/sage/sage/geometry/toric_lattice_element.pyx # 1 doctests failed
        sage -t  -long devel/sage/sage/geometry/cone.py # 1 doctests failed
        sage -t  -long devel/sage/sage/misc/randstate.pyx # 15 doctests failed
        sage -t  -long devel/sage/sage/libs/pari/gen.pyx # 11 doctests failed
        sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py # 1 doctests failed
        sage -t  -long devel/sage/sage/rings/residue_field.pyx # 1 doctests failed
        sage -t  -long devel/sage/sage/rings/number_field/class_group.py # 2 doctests failed
        sage -t  -long devel/sage/sage/rings/polynomial/multi_polynomial_element.py # 1 doctests failed
        sage -t  -long devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py # 2 doctests failed
        sage -t  -long devel/sage/sage/rings/qqbar.py # 1 doctests failed
        sage -t  -long devel/sage/sage/rings/number_field/number_field.py # 2 doctests failed
----------------------------------------------------------------------
Total time for all tests: 6622.9 seconds
```



---

Attachment

Failures observed on a Sun T5240 (SPARC processors) running Solaris 10 update 7.


---

Comment by jdemeyer created at 2010-07-27 19:43:57

Thanks for the test.  I will now upgrade to sage-4.5.2alpha1, do some tests on my own system and in the mean time fix the SPARC failures.  Note that some are simply bugs in sage-4.5.2alpha0 (see the sage-release mailing list).

For the moment, we don't really need more tests until I have put up sage-4.5.2alpha1-9343.


---

Comment by cremona created at 2010-07-27 22:06:26

Replying to [comment:154 jdemeyer]:
> Thanks for the test.  I will now upgrade to sage-4.5.2alpha1, do some tests on my own system and in the mean time fix the SPARC failures.  Note that some are simply bugs in sage-4.5.2alpha0 (see the sage-release mailing list).
> 
> For the moment, we don't really need more tests until I have put up sage-4.5.2alpha1-9343.

Fair enough, but I may as well report that all was good on 64-bit ubuntu except 

```

        sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py # 1 doctests failed
```

which seems irrelevant.


---

Comment by leif created at 2010-07-28 20:05:29

Replying to [comment:155 cremona]:
> Replying to [comment:154 jdemeyer]:
> > For the moment, we don't really need more tests until I have put up sage-4.5.2alpha1-9343.
> 
> Fair enough, but I may as well report that all was good on 64-bit ubuntu except 

```

        sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py # 1 doctests failed
```

> which seems irrelevant.

This is also a 4.5.2.alpha0 bug and fixed in alpha1 (SageNB 0.8.2).


---

Comment by jdemeyer created at 2010-07-29 08:28:13

New version to be tested: [http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.alpha1-9343.tar](http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.alpha1-9343.tar).  I am testing it on 32-bit Linux, 64-bit Linux and 64-bit OS X.


---

Attachment

Fixes doctest failures on 32-bit machines


---

Comment by mpatel created at 2010-08-01 22:50:15

Will [part of] the PARI upgrade fix #9659?  I'm wondering whether to keep #9659 as a blocker for 4.5.2.


---

Comment by jdemeyer created at 2010-08-02 07:21:19

Replying to [comment:159 mpatel]:
> Will [part of] the PARI upgrade fix #9659?
I don't know but probably not.  So I would keep #9659 seperate from this.


---

Comment by jdemeyer created at 2010-08-02 09:56:54

I consider this ticket to be essentially finished.  There are just a few elliptic curve doctests marked with "9343 not tested" which should be fixed (John?).  Other than that, I would not make any further changes to this ticket.


---

Comment by cremona created at 2010-08-02 11:53:56

Replying to [comment:161 jdemeyer]:
> I consider this ticket to be essentially finished.  There are just a few elliptic curve doctests marked with "9343 not tested" which should be fixed (John?).  Other than that, I would not make any further changes to this ticket.

Can you make a list of these?  Last time I looked the only ones were in heegner.py, and I do not know what the problem is with those.


---

Comment by jdemeyer created at 2010-08-02 12:06:45

Replying to [comment:162 cremona]:
> Can you make a list of these?  Last time I looked the only ones were in heegner.py, and I do not know what the problem is with those.

Look at this patch: [http://trac.sagemath.org/sage_trac/attachment/ticket/9343/9343_remove_ell_doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9343/9343_remove_ell_doctests.patch).  Just invert that patch: in a shell, in $SAGE_ROOT/devel/sage, do:

```
patch -p1 --reverse <9343_remove_ell_doctests.patch
```



---

Comment by cremona created at 2010-08-02 12:39:03

OK, so apart from heegner.py there's just one other thing.  A different LLL reduced basis would give different points in that example, that would be harmless. No time now...


---

Attachment

Combined patch against sage-4.5.2.rc1


---

Comment by jdemeyer created at 2010-08-06 09:14:25

I updated to PARI svn 12577 (some more bugs have been fixed), did a long doctest on a 32-bit and a 64-bit Intel Linux system.  There were a few failures appearing, I will add a patch soon (this patch is not included in the sage distribution [http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.rc1.newpari.v0.tar](http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.rc1.newpari.v0.tar))


---

Comment by jdemeyer created at 2010-08-06 09:15:21

Needed to fix doctests appearing because of PARI svn-12577


---

Attachment

Replying to [comment:167 jdemeyer]:
> I updated to PARI svn 12577 (some more bugs have been fixed), did a long doctest on a 32-bit and a 64-bit Intel Linux system.  There were a few failures appearing, I will add a patch soon (this patch is not included in the sage distribution [http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.rc1.newpari.v0.tar](http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.rc1.newpari.v0.tar))

With the [Weber patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9343/9343_weber.patch) applied, all long tests pass on Ubuntu 9.04 x86 (Pentium 4 Prescott, gcc 4.3.3, native code; parallel build from scratch; no explicit/extra optimization specified).

(Note that trac does _not_ send notifications for file uploads.)


---

Comment by drkirkby created at 2010-08-07 11:52:27

Replying to [comment:167 jdemeyer]:
> I updated to PARI svn 12577 (some more bugs have been fixed), did a long doctest on a 32-bit and a 64-bit Intel Linux system.  There were a few failures appearing, I will add a patch soon (this patch is not included in the sage distribution [http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.rc1.newpari.v0.tar](http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.rc1.newpari.v0.tar))

What concerns me, is all this updating of svn. Sure some bugs might be fixed, but others are getting introduced. It would be nice if there was a stable version. Every time you update, so the testing needs to be done again. There was an earlier case I evaluated which it was ok, then someone updated and it was broken. 

There's no point keep testing the code, if the source gets updated. 

Personally, I'd revert to the svn which underwent a fair amount of testing.


---

Comment by drkirkby created at 2010-08-07 12:30:50

Replying to [comment:169 drkirkby]:
> Replying to [comment:167 jdemeyer]:
> > I updated to PARI svn 12577 (some more bugs have been fixed), did a long doctest on a 32-bit and a 64-bit Intel Linux system.  There were a few failures appearing, I will add a patch soon (this patch is not included in the sage distribution [http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.rc1.newpari.v0.tar](http://cage.ugent.be/~jdemeyer/sage/sage-4.5.2.rc1.newpari.v0.tar))
> 
> What concerns me, is all this updating of svn. Sure some bugs might be fixed, but others are getting introduced. It would be nice if there was a stable version. Every time you update, so the testing needs to be done again. There was an earlier case I evaluated which it was ok, then someone updated and it was broken. 
> 
> There's no point keep testing the code, if the source gets updated. 
> 
> Personally, I'd revert to the svn which underwent a fair amount of testing. 

To be more precise, 12543 was ok, 12549 failed all tests. What bugs has 12577 introduced? 

Is there any chance of convincing the Pari developers to actually make a well-tested stable release? The Pari developers can make commits to svn more rapidly than Sage developers can test the code. That's 34 different source versions in 13 days. Would anyone like to try to convince me these are well tested? 

Dave


---

Comment by leif created at 2010-08-07 12:39:31

Replying to [comment:169 drkirkby]:
> What concerns me, is all this updating of svn. Sure some bugs might be fixed, but others are getting introduced.

True. <ignore> But why then update at all...? </ignore>

(_"Release often, release early."_)

> It would be nice if there was a stable version. Every time you update, so the testing needs to be done again. There was an earlier case I evaluated which it was ok, then someone updated and it was broken. 
> 
> There's no point keep testing the code, if the source gets updated.

We might discover bugs in PARI itself as well, which hopefully would get fixed upstream (quickly in the svn, but probably not immediately in a [new] stable version). I though would prefer to base the new spkg on an "official", i.e. stable version, too.

> Personally, I'd revert to the svn which underwent a fair amount of testing. 

I think since it seems a whole release will be dedicated to updating PARI, there will be enough testing anyway. But of course we'll have to freeze our snapshot at some point, when the appointed Sage release date/cycle comes close(r).


---

Comment by jdemeyer created at 2010-08-09 21:00:35

Replying to [comment:169 drkirkby]:
> What concerns me, is all this updating of svn. Sure some bugs might be fixed, but others are getting introduced. It would be nice if there was a stable version. Every time you update, so the testing needs to be done again. There was an earlier case I evaluated which it was ok, then someone updated and it was broken. 
> 
> There's no point keep testing the code, if the source gets updated.
Well, I agree that we shouldn't upgrade the source all too often.  But if the PARI developers fix a bug that we found, that is a good reason to update (and that is also why I updated to 12577).


---

Comment by drkirkby created at 2010-08-10 13:15:14

Replying to [comment:172 jdemeyer]:
> Replying to [comment:169 drkirkby]:
> > There's no point keep testing the code, if the source gets updated.
> Well, I agree that we shouldn't upgrade the source all too often.  But if the PARI developers fix a bug that we found, that is a good reason to update (and that is also why I updated to 12577).

I've changed the title to reflect more accurately what the ticket is. It's *not* an update to version 2.4.3 of Pari. Version 2.4.2 has not even been released - only an alpha of that is available

http://pari.math.u-bordeaux.fr/pub/pari/testing/pari-2.4.2.alpha.tar.gz

This is an svn snapshot, but the ticket title implied something quite different. 

Note the developers guide says the date the snapshot was downloaded should be in the package name. However, that seems to cause confusion to me, as when people update the package, they keep changing the date, rather than adding .p0, .p1, .p2 etc. In any case, different snapshots can exist on the same day. Putting the actual snapshot number seems more sensible to me. So I think it would be better if this was called pari-svn12577.spkg, to reflect that fact it is a snapshot, and not a stable release as the package name would imply. Otherwise follow the developers guide. IMHO, this should not be called pari-2.4.3. 

When 2.4.3 is released, it would seem sensible Pari is updated to a stable release. But that's less likely to happen if people see from the package name that we already have the latest release. 

Of course, if the snapshot that's used gets updated, then that should be reflected in the ticket title! 

BTW, before thinking about updating the snapshot once again, take a read of of the book [The Mythical Man-Month](http://en.wikipedia.org/wiki/The_Mythical_Man-Month) in particular one of the authors points [that in a suitably complex system there is a certain irreducible number of errors. Any attempt to fix observed errors tends to result in the introduction of other errors.](http://en.wikipedia.org/wiki/The_Mythical_Man-Month#The_tendency_towards_irreducible_number_of_errors) I've certainly experienced this before many times - including a previous snapshot on this very ticket. 

Dave


---

Comment by cremona created at 2010-08-11 16:07:13

I suggest that when we are close to having a version of all this which we want to release (as 4.6.alpha0 or whatever), which is soon now, we (William or me probably) let the two lead Pari developers know that this is happening, and tell them which svn version we are considering going with.  It may be that they recommend waiting for some bugs they know about and have nearly fixed.  (But we cannot wait for ever, of course.)   

It is also possible that they may be  pleased that a certain Pari version has had extensive testing through being part of a Sage release (and they may even say so, though that is slightly less likely).  In any case, when the new spkg and all the related patches are in Sage then it will be very easy to upgrade to to a new Pari svn for new bug fixes.


---

Comment by leif created at 2010-08-11 16:26:36

We have a new(?) issue with PARI 2.3.5(.p2) on Fedora 13 if libfltk-dev (or even libfltk, i.e. just the library, without the necessary headers) is installed: #9722

Does anyone know if this is already fixed here? (Otherwise I'd try to provide a simple patch at the other ticket.)


---

Comment by cremona created at 2010-08-12 19:38:13

Could someone who is up to date on this post a list of which patches now need applying, and a link to the latest spkg?  The list at the top is just too long, and I don't have a recent working version of this.  Also, does what we have so far apply to 4.5.2?  or 4.5.3.alpha0?  If not, it should...


---

Comment by jdemeyer created at 2010-08-12 21:36:00

Flattening of the above sagelib patches against sage-4.5.3.alpha0


---

Attachment

Replying to [comment:176 cremona]:
> Could someone who is up to date on this post a list of which patches now need applying, and a link to the latest spkg?  The list at the top is just too long, and I don't have a recent working version of this.  Also, does what we have so far apply to 4.5.2?  or 4.5.3.alpha0?  If not, it should...

I rebased the patch to sage-4.5.3.alpha0, but I did not yet have time to test it.  I also tried to clarify the instructions in the ticket description, hope it clears things up...


---

Comment by cremona created at 2010-08-12 22:06:20

Replying to [comment:178 jdemeyer]:
> Replying to [comment:176 cremona]:
> > Could someone who is up to date on this post a list of which patches now need applying, and a link to the latest spkg?  The list at the top is just too long, and I don't have a recent working version of this.  Also, does what we have so far apply to 4.5.2?  or 4.5.3.alpha0?  If not, it should...
> 
> I rebased the patch to sage-4.5.3.alpha0, but I did not yet have time to test it.  I also tried to clarify the instructions in the ticket description, hope it clears things up...

Thanks -- I'll spend some time on this on Friday.


---

Comment by cremona created at 2010-08-13 10:47:38

Following the detailed instructions in the ticket description, starting with a  fresh build of 4.5.3.alpha0, I successfully installed the three spkgs (with SAGE_CHECK='yes') and both patches (sagelib and extcode) with no issues -- except that when I tried to install the lcalc spkg, it said "already installed", which I do not really understand.  Jeroen?

Then, sage -tp 10 -long passed everything!  So the rebase to 4.5.3.alpha0 is fine.

elliptic_curves/ell_rational_field.py:  I checked that the new output from the doctest is as valid as the old one (there is just a slightly different LLL-reduced basis, which is a reasonable side-effect of changes to the pari library which does the LLL reduction).

I am uploading an extra little patch fixing that.  Which just leaves heegner,py.


---

Comment by cremona created at 2010-08-13 10:50:53

apply to sagelib after sagelib_9343_combined6.patch


---

Attachment

PS to review just above: I also tested with "make ptestlong" and there were no problems.


---

Comment by leif created at 2010-08-13 11:50:55

Replying to [comment:180 cremona]:
> ... except that when I tried to install the lcalc spkg, it said "already installed", which I do not really understand.

This is because the package at #9592 has the wrong name (it should be rebased on #9665 which is p1, and renamed to p2.)


---

Comment by cremona created at 2010-08-13 11:59:14

Replying to [comment:182 leif]:
> Replying to [comment:180 cremona]:
> > ... except that when I tried to install the lcalc spkg, it said "already installed", which I do not really understand.
> 
> This is because the package at #9592 has the wrong name (it should be rebased on #9665 which is p1, and renamed to p2.)
> 
Ahah!  Well, as I said, everything worked and passed, so perhaps this means that no upgrade of lcalc is required after all?


---

Comment by leif created at 2010-08-13 15:13:28

Replying to [comment:183 cremona]:
> Replying to [comment:182 leif]:
> > Replying to [comment:180 cremona]:
> > > ... except that when I tried to install the lcalc spkg, it said "already installed", which I do not really understand.
> > 
> > This is because the package at #9592 has the wrong name (it should be rebased on #9665 which is p1, and renamed to p2.)
> > 
> Ahah!  Well, as I said, everything worked and passed, so perhaps this means that no upgrade of lcalc is required after all?

John, could you try reinstalling the "old" lcalc p1 package (by `./sage -f ...`)?

Perhaps this would show the error #9592 (Jeroen's new lcalc spkg) is intended to fix.


---

Comment by cremona created at 2010-08-13 15:31:01

Replying to [comment:184 leif]:
> Replying to [comment:183 cremona]:
> > Replying to [comment:182 leif]:
> > > Replying to [comment:180 cremona]:
> > > > ... except that when I tried to install the lcalc spkg, it said "already installed", which I do not really understand.
> > > 
> > > This is because the package at #9592 has the wrong name (it should be rebased on #9665 which is p1, and renamed to p2.)
> > > 
> > Ahah!  Well, as I said, everything worked and passed, so perhaps this means that no upgrade of lcalc is required after all?
> 
> John, could you try reinstalling the "old" lcalc p1 package (by `./sage -f ...`)?
> 
> Perhaps this would show the error #9592 (Jeroen's new lcalc spkg) is intended to fix.

I did that and it does not show the error.  Note that Jeroen's patch at #9592 just changes one source file (src/Lcommand_line_elliptic.cc) and in that file changes 

```
    F[1] = lgeti(BIGDEFAULTPREC);
```

to

```
    F[1] = (long)cgeti(BIGDEFAULTPREC);
```

and 4 similar lines.  It is possible that during our work on this ticket some change in Pari means that old version works again.  So I think that we can cancel #9592 and remove the new spkg from the instruction on this ticket.  I will try that and report back.


---

Comment by cremona created at 2010-08-13 15:57:29

OK, I see what is happening now.  Applying JD's version of the lcalc patch does not work since there is a different p1 version of that which is now in the standard distribution (for 4.5.3.alpha0) so it does nothing when you try to install it since the name is the same.

I will take the real p1 from #9685 and add JD's extra patch to Lcommandline_elliptic.cc (being careful, since there's already a patch for that file) and make a p2 from it, then post a link to that here.


---

Comment by cremona created at 2010-08-13 16:06:03

Replying to [comment:186 cremona]:

> 
> I will take the real p1 from #9685 and add JD's extra patch to Lcommandline_elliptic.cc (being careful, since there's already a patch for that file) and make a p2 from it, then post a link to that here.

That should have said #9665;  and in fact I can take it from SAGE_ROOT/spkg/standard from 4.5.3.alpha0.


---

Comment by cremona created at 2010-08-13 16:42:05

See related discussions at #9665.  The new lcalc spkg should be replaced by the one there.[Jeroen's p1 has been superceded by the p1 at #9665 which has now been merged.  There's a suitable p2 at that ticket which can be linked to here after testing.]

I checked that the lcalc p2 spkg from #9665 builds fine (and really does build!), and am re-testing everything.


---

Comment by cremona created at 2010-08-13 16:43:02

Replying to [comment:188 cremona]:
> See related discussions at #9665.  The new lcalc spkg should be replaced by the one there.[Jeroen's p1 has been superceded by the p1 at #9665 which has now been merged.  There's a suitable p2 at that ticket which can be linked to here after testing.]
> 
> I checked that the lcalc p2 spkg from #9665 builds fine (and really does build!), and am re-testing everything.

The first and third references should be to #9592, sorry.


---

Comment by cremona created at 2010-08-13 16:59:17

All tests passed.  (This is with my extra patch  trac_9343-review.patch).

So now the confusion over the lcalc spkg has been sorted, we are back on track....


---

Comment by leif created at 2010-08-13 20:43:07

Replying to [comment:190 cremona]:
> All tests passed.  (This is with my extra patch  trac_9343-review.patch).

Yes, passed (without the new lcalc spkg) `ptestlong` with Sage 4.5.3.alpha0 + #9475 + #9717 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4, native code, O2; I just installed the new spkgs and applied the two patches, i.e. did not build from scratch).

After that, I applied John's reviewer patch, and all (long) tests in `sage/schemes/elliptic_curves/ell_rational_field.py` also passed.

> So now the confusion over the lcalc spkg has been sorted, we are back on track....

Yes. I could reproduce the build error of the old lcalc spkg with new PARI; John's new one (p2) at #9592 (Jeroen's p1 rebased on Sage's current one) builds.

The number (and type) of warnings I get by doing so (building lcalc) though is IMHO a shame. Besides other annoying warnings, there are twelve deprecation warnings (with gcc 4.4.4). (Of course many warnings have the same origin, but that makes fixing them even easier. This isn't meant as an offense, but rather a suggestion.)


---

Comment by leif created at 2010-08-13 21:14:29

Replying to [comment:191 leif]:
> Replying to [comment:190 cremona]:
> > All tests passed.  (This is with my extra patch  trac_9343-review.patch).
> 
> Yes, passed (without the new lcalc spkg) `ptestlong` with Sage 4.5.3.alpha0 + #9475 + #9717 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4, native code, O2; I just installed the new spkgs and applied the two patches, i.e. did not build from scratch).
> 
> After that, I applied John's reviewer patch, and all (long) tests in `sage/schemes/elliptic_curves/ell_rational_field.py` also passed.

Exactly the same on Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3, native code, O2), except that I did run `testlong` instead of `ptestlong` because the machine was already heavily loaded.

(The lcalc build warnings are the same, too, btw.)


---

Comment by cremona created at 2010-08-13 21:41:06

My guess is that if one of us were to fix the warnings in compiling lcalc and give Mike R the result, he would gratefully accept it, if he does not have time to do it himself.
But that's not for this ticket.


---

Comment by leif created at 2010-08-13 21:57:44

Replying to [comment:193 cremona]:
> My guess is that if one of us were to fix the warnings in compiling lcalc and give Mike R the result, he would gratefully accept it, if he does not have time to do it himself.
> But that's not for this ticket.

Perhaps for #9592. If only all (severe) warnings originated from upstream...


P.S. to the build and test reports:

I do get a Sphinx warning:

```
docstring of sage.libs.pari.gen.PariInstance.read:8: (WARNING/2) Literal block expected; none found.
```



---

Comment by leif created at 2010-08-14 03:35:28

Replying to [comment:191 leif]:
> ... passed (without the new lcalc spkg) `ptestlong` with Sage 4.5.3.alpha0 + #9475 + #9717 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4, native code, O2; I just installed the new spkgs and applied the two patches, i.e. did not build from scratch).

Also passed `ptestlong` with John's rebased lcalc p2 (from #9592).


---

Comment by was created at 2010-08-14 03:36:30

I looked into the failures in heegner.py in extreme detail, and the problem is entirely because of the following.  

```
CURRENT SAGE:

sage: Q = QuadraticForm(QQ,3,[ 8657345368, 12759737420, 29300965980,4701524895, 21592798720, 24792432640 ])
sage: n = 11767
sage: time Q.representation_vector_list(n+1)[-1]
CPU times: user 1.96 s, sys: 0.00 s, total: 1.97 s
Wall time: 1.97 s
[(5207, -2829, -1845), (-5207, 2829, 1845)]

NEW SAGE (with NEW PARI):

sage: Q = QuadraticForm(QQ,3,[ 8657345368, 12759737420, 29300965980,4701524895, 21592798720, 24792432640 ])
sage: n = 11767
sage: time Q.representation_vector_list(n+1)[-1]
CPU times: user 1.85 s, sys: 0.00 s, total: 1.85 s
Wall time: 1.85 s
[(-5207, 2829, 1845), (5207, -2829, -1845)]

```


---
The difference is just that the vectors with given norm output by pari are now in a different order.  This causes some output to be slightly different in Sage, but is not a bug.   So it is 100% safe to change the output in heegner.py to match what gets output now. 

---

Regarding the error in ell_rational_field.py -- the *only* remaining issue -- this is a doctest that John Cremona introduced for trac 4525: http://trac.sagemath.org/sage_trac/ticket/4525

The difference is that "a" LLL reduced basis is now slightly different.  This seems extremely plausible, since PARI's LLL code was completely changed in this new version (I recall Bill A. telling me they incorporated a version of fplll into PARI).  So very likely that doctest is fine too.  John C is the one who should sign off on it though, not Robert B (you're in the clear).

I've taken the liberty of posting a patch that fixes the heegner.py tests, and also the one LLL test in ell_rational_field.py (though I'd like to hear from John C. about that).


---

Attachment

this fixes the issues with heegner.py and ell_rational_field.py, which were the last remaining after sagelib_9343_combined6.patch


---

Comment by jdemeyer created at 2010-08-14 11:10:29

After this is merged, we should have a closer look at pickling of PARI and GP elements, see #9745.


---

Comment by cremona created at 2010-08-14 11:43:00

William, I had already posted a patch for the LLL-reduced basis thing (see a few comments up) but you can be forgiven for not noticing it in this crowded ticket!  Yours does the same as mine and also fixes the heegner stuff, so mine could be deleted.  [Your diagnosis is 100% correct]

Perhaps we need a manager for this ticket to get it all ready for the release manager?


---

Comment by drkirkby created at 2010-08-14 13:02:48

#9591 (genus2reduction) still needs to be resolved I believe. That's not even marked for review. 

I wish I knew why people keep putting tickets related to this being due to a upgrade to pari 2.4.3, when not even 2.4.2 has ever been released. 

Dave


---

Comment by jdemeyer created at 2010-08-14 15:40:37

I made some more changes, including removing gp_cremona.py.  I have not yet tested this completely, hang on...


---

Comment by leif created at 2010-08-14 17:01:45

Replying to [comment:203 jdemeyer]:
> I made some more changes, including removing gp_cremona.py.  I have not yet tested this completely, hang on...

I do... ;-)

Can you also fix the Sphinx warning?

In case this ticket gets merged soon, we should also address #9722 (Fedora 13 FLTK issue, at least the linker error) _here_. (Though I haven't yet checked if it is still present in our current svn snapshot; will do that later.)


William, Dave said on sage-release you want this merged into 4.5.3 (rather than 4.6, which is the current milestone)?


---

Comment by leif created at 2010-08-14 17:27:58

Replying to [comment:203 jdemeyer]:
> I made some more changes ...

`s/optinal/optional/`

There are some back-ticks (and double back-ticks, e.g around `True`) missing in docstrings.

Normalizing "PARI"/"Pari"/"pari" (and e.g. ``L`-function` vs. `L-function`) would be nice, too... :)


---

Comment by jdemeyer created at 2010-08-14 19:07:57

Replying to [comment:205 leif]:
> Normalizing "PARI"/"Pari"/"pari" would be nice, too... :)

The official name seems to be "PARI" but "Pari" and "pari" are all over the place in Sage.  It wouldn't be too hard to do a search-and-replace-all if you want...


---

Comment by cremona created at 2010-08-14 19:43:49

Replying to [comment:206 jdemeyer]:
> Replying to [comment:205 leif]:
> > Normalizing "PARI"/"Pari"/"pari" would be nice, too... :)
> 
> The official name seems to be "PARI" but "Pari" and "pari" are all over the place in Sage.  It wouldn't be too hard to do a search-and-replace-all if you want...

Yes: from http://pari.math.u-bordeaux.fr/ we see:


```
    * PARI is a C library, allowing fast computations.
    * gp is an easy-to-use interactive shell giving access to the PARI functions.
    * GP is the name of gp's scripting language.
```



---

Comment by drkirkby created at 2010-08-14 20:23:17

Replying to [comment:206 jdemeyer]:
> Replying to [comment:205 leif]:
> > Normalizing "PARI"/"Pari"/"pari" would be nice, too... :)
> 
> The official name seems to be "PARI" but "Pari" and "pari" are all over the place in Sage.  It wouldn't be too hard to do a search-and-replace-all if you want...

The official name of MATLAB is MATLAB, but still the Sage has:

_Mission: Creating a viable free open source alternative to Magma, Maple, Mathematica and Matlab._

I've tried suggesting we call MATLAB by its official name, but that fell on deaf ears. 

In general, I'd rather call programs by their official name, though in same cases, the programs themselves are not consistent!


---

Comment by leif created at 2010-08-14 20:36:10

Replying to [comment:196 was]:
> I've taken the liberty of posting a patch that fixes the heegner.py tests, and also the one LLL test in ell_rational_field.py (though I'd like to hear from John C. about that).   

Also passed `ptestlong` on Fedora 13 x86 (Pentium 4 Prescott), with and without optimization (i.e. `O2` in "global" `CFLAGS`), native code.

The version prior to this, i.e. without William's patches (but John's reviewer patch), passed all long tests on Ubuntu 7.10 x86 (Pentium 4, gcc 4.2.1, native code, O2), too.


---

Comment by jdemeyer created at 2010-08-14 20:38:47

Changing status from new to needs_review.


---

Comment by leif created at 2010-08-14 20:43:17

Replying to [comment:209 leif]:
> The version prior to this, i.e. without William's patches (but John's reviewer patch), passed all long tests on Ubuntu 7.10 x86 (Pentium 4, gcc 4.2.1, native code, O2), too.

... and just passed `ptestlong` _with_ these, too. :)


---

Comment by leif created at 2010-08-14 21:16:39

Replying to [comment:210 jdemeyer]:

In case somebody missed it, we have a new genus2reduction spkg (p8 instead of p7).


---

Comment by cremona created at 2010-08-14 21:30:26

Good work on 9343_jd_review.patch:  you completed the job I left unfinished (using the pari library for analytic ranks, making gp_cremona.py finally completely redundant), and I also see that you wrapped some other useful pari library functions.

I am now doing a fresh test of everything and will report back on Sunday.


---

Attachment

Various fixes, remove gp_cremona.py


---

Comment by jdemeyer created at 2010-08-14 22:27:58

I updated my last patch to fix the analytic_rank doctests on 32-bit.


---

Comment by leif created at 2010-08-14 22:41:19

Replying to [comment:204 leif]:
> In case this ticket gets merged soon, we should also address #9722 (Fedora 13 FLTK issue, at least the linker error) _here_. (Though I haven't yet checked if it is still present in our current svn snapshot; will do that later.)

#9722 seems to be a non-issue with our PARI snapshot. (At least I cannot reproduce it on 32-bit Fedora 13.)


---

Comment by drkirkby created at 2010-08-15 02:07:12

I just tried the steps outlined at the top. 

 * Pari installed ok
 * genus2reduction installed ok
 * lcalc installed ok. 
 * extcode_9343_combined3.patch patch to data/extcode installed ok. 
 
Then when I tried to apply the library patches, I was less than successful. I'm not sure though if the 


```
hg qpush -a
```

was the right thing to do after `hg qimport` of the library patches. So I could have made a mistake, but this is what I did, and this is what results I got. (This is an OpenSolaris system, which apart from some numerical noise issues, and a totally busted `sympow` otherwise passes all the doc tests.)


```
drkirkby@hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg status
drkirkby@hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9343/sagelib_9343_combined6.patch
adding sagelib_9343_combined6.patch to series file
drkirkby@hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9343/sagelib_9343-heegner_ell_ratioanal.patch
adding sagelib_9343-heegner_ell_ratioanal.patch to series file
drkirkby@hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9343/9343_jd_review.patch
adding 9343_jd_review.patch to series file
drkirkby@hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg qpush -a
applying 9343_jd_review.patch
patching file sage/interfaces/gp.py
Hunk #1 FAILED at 599
Hunk #2 FAILED at 613
Hunk #3 FAILED at 889
Hunk #4 FAILED at 990
Hunk #5 FAILED at 1003
5 out of 5 hunks FAILED -- saving rejects to file sage/interfaces/gp.py.rej
patching file sage/libs/pari/decl.pxi
Hunk #1 FAILED at 35
Hunk #2 FAILED at 94
Hunk #3 FAILED at 279
Hunk #4 FAILED at 298
Hunk #5 FAILED at 313
Hunk #6 FAILED at 325
Hunk #7 FAILED at 372
Hunk #8 succeeded at 871 with fuzz 2 (offset 198 lines).
Hunk #9 succeeded at 945 with fuzz 2 (offset 217 lines).
Hunk #10 succeeded at 968 with fuzz 1 (offset 218 lines).
Hunk #11 FAILED at 1041
8 out of 11 hunks FAILED -- saving rejects to file sage/libs/pari/decl.pxi.rej
patching file sage/rings/number_field/number_field.py
Hunk #2 FAILED at 7533
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/number_field/number_field.py.rej
patching file sage/rings/real_mpfr.pyx
Hunk #2 FAILED at 2588
Hunk #3 FAILED at 2607
Hunk #4 succeeded at 2618 with fuzz 1 (offset -8 lines).
Hunk #5 FAILED at 2631
3 out of 5 hunks FAILED -- saving rejects to file sage/rings/real_mpfr.pyx.rej
patching file sage/schemes/elliptic_curves/ell_finite_field.py
Hunk #1 FAILED at 36
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_finite_field.py.rej
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #2 FAILED at 1271
Hunk #4 FAILED at 1347
2 out of 4 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
patching file sage/schemes/elliptic_curves/gp_cremona.py
Hunk #1 FAILED at 0
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/gp_cremona.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 9343_jd_review.patch
drkirkby@hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg status
```


Dave


---

Comment by jdemeyer created at 2010-08-15 06:51:20

Replying to [comment:216 drkirkby]:
> {{{
> drkirkby`@`hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg status
> drkirkby`@`hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9343/sagelib_9343_combined6.patch
> adding sagelib_9343_combined6.patch to series file
> drkirkby`@`hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9343/sagelib_9343-heegner_ell_ratioanal.patch
> adding sagelib_9343-heegner_ell_ratioanal.patch to series file
> drkirkby`@`hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9343/9343_jd_review.patch
> adding 9343_jd_review.patch to series file
> drkirkby`@`hawk:~/32/sage-4.5.3.alpha0/devel/sage$ hg qpush -a
> applying 9343_jd_review.patch
> }}}

You're applying the patches in the wrong order.  I usually do

```
$ hg qimport <patch>
$ hg qpush
$ hg qimport <patch>
$ hg qpush
...
```


which should work fine.  Maybe there is a better way, I don't know much about Mercurial.


---

Comment by cremona created at 2010-08-15 11:37:17

I agree with David that Mercurial is counter-intuitive -- you have to push one at a time since push means "push the last patch imported".

My complete new spkg and patch install and test on a 32-bit Ubuntu (Intel, gcc 4.2.4) went smoothly, with only the 32/64 issues with the new analytic rank as Jeroen found.  So I popped the last patch and pushed the replacement, and now that works fine.

Now testing the rebuilding od documentation...


---

Comment by jdemeyer created at 2010-08-15 11:39:44

I have made a new sage distribution with this ticket, based on 4.5.3.alpha0. It also includes the Singular update (#8059). Download it from http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha0.tar


---

Comment by cremona created at 2010-08-15 11:42:03

Replying to [comment:218 cremona]:

> Now testing the rebuilding od documentation...

html docs rebuilt with no errors/warnings.


---

Comment by cremona created at 2010-08-15 11:46:53

Replying to [comment:219 jdemeyer]:
> I have made a new sage distribution with this ticket, based on 4.5.3.alpha0. It also includes the Singular update (#8059). Download it from http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha0.tar

OK, got that -- will do 32- and 64-bit builds and report back.


---

Comment by leif created at 2010-08-15 14:56:38

Replying to [comment:219 jdemeyer]:
> I have made a new sage distribution with this ticket, based on 4.5.3.alpha0. It also includes the Singular update (#8059). Download it from http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha0.tar

Announce on sage-release? ;-)

Btw, Mitesh is currently compiling [Sage 4.5.3.alpha1](http://trac.sagemath.org/sage_trac/query?group=component&order=priority&col=id&col=summary&col=status&col=owner&col=type&col=priority&col=milestone&merged=~4.5.3.alpha1) (which includes the new Singular, a new libm4ri and an updated PolyBoRi package, and some bug fixes).


---

Comment by cremona created at 2010-08-15 16:12:49

Replying to [comment:222 cremona]:
> Replying to [comment:219 jdemeyer]:
> > I have made a new sage distribution with this ticket, based on 4.5.3.alpha0. It also includes the Singular update (#8059). Download it from http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha0.tar
> 
> OK, got that -- will do 32- and 64-bit builds and report back.

Built fine and all tests pass on 32-bit ubuntu (Intel, gcc 4.2.4) and 64-bit ubuntu (AMD, 4.3.3).


---

Comment by cremona created at 2010-08-15 16:18:53

Replying to [comment:224 cremona]:
> Replying to [comment:222 cremona]:
> > Replying to [comment:219 jdemeyer]:
> > > I have made a new sage distribution with this ticket, based on 4.5.3.alpha0. It also includes the Singular update (#8059). Download it from http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha0.tar
> > 
> > OK, got that -- will do 32- and 64-bit builds and report back.
> 
> Built fine and all tests pass on 32-bit ubuntu (Intel, gcc 4.2.4) and 64-bit ubuntu (AMD, 4.3.3).
> 

However, this needs cleaning up:

```
jec@selmer%pwd
/storage/jec/sage-4.6.prealpha0/devel/sage
jec@selmer%hg status
! sage/schemes/elliptic_curves/gp_cremona.py
```

-- I think "hg remove" & then commit will do it.


---

Comment by leif created at 2010-08-15 16:36:44

Replying to [comment:225 cremona]:
> However, this needs cleaning up:

```
jec@selmer%pwd
/storage/jec/sage-4.6.prealpha0/devel/sage
jec@selmer%hg status
! sage/schemes/elliptic_curves/gp_cremona.py
```

> -- I think "hg remove" & then commit will do it.

Yes, and there are some more. Try

```sh
find $SAGE_ROOT -name .hg -exec sh -c "cd {}; hg status" \;
```

and you'll see them all.


---

Comment by drkirkby created at 2010-08-15 19:03:01

Replying to [comment:218 cremona]:
> I agree with David that Mercurial is counter-intuitive -- you have to push one at a time since push means "push the last patch imported".

But I did not type 

`hg qpush`

but instead 


```
hg qpush -a}}

Looking for help on that:

{{{
drkirkby@hawk:~$ hg qpush -h
hg qpush [-f] [-l] [-a] [-m] [-n NAME] [PATCH | INDEX]

push the next patch onto the stack

    When -f/--force is applied, all local changes in patched files
    will be lost.

options:

 -f --force  apply if the patch has rejects
 -l --list   list patch name in commit text
 -a --all    apply all patches
 -m --merge  merge from another queue
 -n --name   merge queue name

use "hg -v help qpush" to show global options
}}}

I interpret that is meaning all of them would be applied. 

Dave


---

Comment by cremona created at 2010-08-15 19:21:50

Replying to [comment:227 drkirkby]:
> Replying to [comment:218 cremona]:
> > I agree with David that Mercurial is counter-intuitive -- you have to push one at a time since push means "push the last patch imported".
> 
> But I did not type 
> 
> `hg qpush`
> 
> but instead 
> 
> {{{hg qpush -a}}
> 
> Looking for help on that:
> 
> {{{
> drkirkby`@`hawk:~$ hg qpush -h
> hg qpush [-f] [-l] [-a] [-m] [-n NAME] [PATCH | INDEX]
> 
> push the next patch onto the stack
> 
>     When -f/--force is applied, all local changes in patched files
>     will be lost.
> 
> options:
> 
>  -f --force  apply if the patch has rejects
>  -l --list   list patch name in commit text
>  -a --all    apply all patches
>  -m --merge  merge from another queue
>  -n --name   merge queue name
> 
> use "hg -v help qpush" to show global options
> }}}
> 
> I interpret that is meaning all of them would be applied. 
> 
> Dave 

Sure -- what is (possibly) counter intuitive is the *order* in which they are applied, which is the reverse of the order they were imported.  For this reason I find "hg qpush -a" rarely useful.


---

Comment by jdemeyer created at 2010-08-15 19:48:15

Replying to [comment:225 cremona]:
> -- I think "hg remove" & then commit will do it.

I see.  Simply removing the file is not good enough...


---

Attachment

Fixes Sphinx warning from PariInstance.read() docstring. Apply to Sage library.


---

Comment by leif created at 2010-08-15 22:40:49

I've attached a [single-character patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9343/trac_9343-sagelib-fix_sphinx_warning-reviewer.patch) to fix the Sphinx warning.


---

Comment by leif created at 2010-08-15 22:50:55

Replying to [comment:224 cremona]:
> Replying to [comment:222 cremona]:
> > Replying to [comment:219 jdemeyer]:
> > > I have made a new sage distribution with this ticket, based on 4.5.3.alpha0. It also includes the Singular update (#8059). Download it from http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha0.tar
> > 
> > OK, got that -- will do 32- and 64-bit builds and report back.
> 
> Built fine and all tests pass on 32-bit ubuntu (Intel, gcc 4.2.4) and 64-bit ubuntu (AMD, 4.3.3).
> 

Also passed `ptestlong` on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4, native code, with `O2`).


---

Comment by drkirkby created at 2010-08-16 00:01:30

I decided to test the http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha0.tar on my OpenSolaris machine. Sage has never passed all the doc tests on OpenSolaris, so I did not expect it to. I'll list the failures and what I think they are due to. There's one unexecpted failure. 

A better test would be on 't2', but that takes forever to build Sage. This is an order of magnitude quicker. 


```
The following tests failed:

	sage -t  -long devel/sage/sage/lfunctions/sympow.py # 13 doctests failed
	sage -t  -long devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py # 1 doctests failed
	sage -t  -long devel/sage/sage/modular/abvar/abvar.py # 1 doctests failed
	sage -t  -long devel/sage/sage/modular/hecke/submodule.py # 1 doctests failed
	sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 17 doctests failed
	sage -t  -long devel/sage/sage/stats/hmm/chmm.pyx # 3 doctests failed
	sage -t  -long devel/sage/sage/symbolic/expression.pyx # 2 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1913.9 seconds
```


1) `devel/sage/sage/lfunctions/sympow.py` SYMPOW is the worst code I've ever seen in Sage and is broken on Solaris x86 (#9703), Cygwin (#9166) and reportedly ArchLinux too. The examples at http://www.sagemath.org/doc/reference/sage/lfunctions/sympow.html do not work if you try them on sage.math, so I we can ignore this failure. The code in SYMPOW is so bad, I can't really be bothered to try to fix it. 

2) `devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py` *An unexpected failure.* 

3) `devel/sage/sage/modular/abvar/abvar.py` Caused by SYMPOW. So we can ignore that. 

4) `devel/sage/sage/modular/hecke/submodule.py` Again, caused by SYMPOW, so we can ignore that. 
 
5) `devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py` Again, caused by SYMPOW, so we can ignore that. 

6) `devel/sage/sage/stats/hmm/chmm.pyx` This is numerical noise, #9735, which will hopefully be merged soon. 

7) ` devel/sage/sage/symbolic/expression.pyx` Again numerical noise (#9689  & #9693). 

So the unexpected failure I see was this one:


```
sage -t  -long devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py
**********************************************************************
File "/export/home/drkirkby/sage-4.6.prealpha0/devel/sage-main/sage/rings/polynomial/polynomial_quotient_ring.py", line 1280:
    sage: [phi(k.0^2) for phi in v]
Expected:
    [2.9757207403766761469671194565 - 1.2983430720865060515202099613e-47*I, -2.4088994371613850098316292196 + 1.9025410530350528612407363802*I, -2.4088994371613850098316292196 - 1.9025410530350528612407363802*I, 0.92103906697304693634806949137 - 3.0755331188457794473265418086*I, 0.92103906697304693634806949137 + 3.0755331188457794473265418086*I]
Got:
    [2.9757207403766761469671194565, -2.4088994371613850098316292196 + 1.9025410530350528612407363802*I, -2.4088994371613850098316292196 - 1.9025410530350528612407363802*I, 0.92103906697304693634806949137 - 3.0755331188457794473265418086*I, 0.92103906697304693634806949137 + 3.0755331188457794473265418086*I]
**********************************************************************
```


Could that be due to Pari? If not, and you know where I should look for the cause, let me know. 

Dave


---

Comment by leif created at 2010-08-16 01:26:27

Replying to [comment:231 leif]:
> Replying to [comment:224 cremona]:
> > Replying to [comment:222 cremona]:
> > > Replying to [comment:219 jdemeyer]:
> > > > I have made a new sage distribution with this ticket, based on 4.5.3.alpha0. It also includes the Singular update (#8059). Download it from http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha0.tar
> > > 
> > > OK, got that -- will do 32- and 64-bit builds and report back.
> > 
> > Built fine and all tests pass on 32-bit ubuntu (Intel, gcc 4.2.4) and 64-bit ubuntu (AMD, 4.3.3).
> > 
> 
> Also passed `ptestlong` on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4, native code, with `O2`).

Passed `testlong` on Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3, native code, with `O2`), too.


---

Comment by jdemeyer created at 2010-08-16 05:28:00

Replying to [comment:232 drkirkby]:
> So the unexpected failure I see was this one:


```
sage -t  -long devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py
**********************************************************************
File "/export/home/drkirkby/sage-4.6.prealpha0/devel/sage-main/sage/rings/polynomial/polynomial_quotient_ring.py", line 1280:
    sage: [phi(k.0^2) for phi in v]
Expected:
    [2.9757207403766761469671194565 - 1.2983430720865060515202099613e-47*I, -2.4088994371613850098316292196 + 1.9025410530350528612407363802*I, -2.4088994371613850098316292196 - 1.9025410530350528612407363802*I, 0.92103906697304693634806949137 - 3.0755331188457794473265418086*I, 0.92103906697304693634806949137 + 3.0755331188457794473265418086*I]
Got:
    [2.9757207403766761469671194565, -2.4088994371613850098316292196 + 1.9025410530350528612407363802*I, -2.4088994371613850098316292196 - 1.9025410530350528612407363802*I, 0.92103906697304693634806949137 - 3.0755331188457794473265418086*I, 0.92103906697304693634806949137 + 3.0755331188457794473265418086*I]
**********************************************************************
```


This particular doctest was changed by this patch.  Interestingly, it is a test which is documented to give a different result on 32-bit and 64-bit systems and your result is precisely the correct result for a 64-bit machine.  This can probably be solved with "..."


---

Comment by drkirkby created at 2010-08-16 09:02:24

Replying to [comment:234 jdemeyer]:

> This particular doctest was changed by this patch.  Interestingly, it is a test which is documented to give a different result on 32-bit and 64-bit systems and your result is precisely the correct result for a 64-bit machine.  This can probably be solved with "..."

Note the machine I used is 64-bit (it has a quad core 3.33 GHz Intel Xeon W3580 CPU), but the build was performed 32-bit. Both Solaris and OpenSolaris build 32-bit applications by default - for 64-bit, you need to add the `-m64` compiler switch when building. The 64-bit builds of Sage are not very successful yet. 

Does anyone know what the result should be? For the first result, I get the *real number* `2.9757207403766761469671194565` but the expected value is the *complex number* `2.9757207403766761469671194565 - 1.2983430720865060515202099613e-47*I` So for the real part I get *exactly* the same number, but I get no imaginary part whatsoever. 

I assume someone here must know the maths behind this, and know whether the result is supposed to be real or complex. If it should really be real (so the number I got is actually the more accurate of the two), then putting dots would be *very* dangerous. Then a result of `2.9757207403766761469671194565 + 1e300*I` would still pass! That's almost entirely imaginary, with a very small real part in comparison to the massive imaginary component. 

Dave


---

Comment by davidloeffler created at 2010-08-16 09:17:27

Replying to [comment:235 drkirkby]:

> Does anyone know what the result should be? For the first result, I get the *real number* `2.9757207403766761469671194565` but the expected value is the *complex number* `2.9757207403766761469671194565 - 1.2983430720865060515202099613e-47*I` So for the real part I get *exactly* the same number, but I get no imaginary part whatsoever. 
> 
> I assume someone here must know the maths behind this, and know whether the result is supposed to be real or complex. If it should really be real (so the number I got is actually the more accurate of the two), then putting dots would be *very* dangerous. Then a result of `2.9757207403766761469671194565 + 1e300*I` would still pass! That's almost entirely imaginary, with a very small real part in comparison to the massive imaginary component. 

Maybe rather than directly testing the answer, one could do something like this:

```
sage: x = [calculation]; abs(x - 2.975975720740376676146967119) < 10^(-27)
True
```

That would be less dangerous, while still allowing the necessary flexibility.


---

Comment by drkirkby created at 2010-08-16 09:43:45

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-08-16 09:43:45

Replying to [comment:236 davidloeffler]:

> Maybe rather than directly testing the answer, one could do something like this:
> {{{
> sage: x = [calculation]; abs(x - 2.975975720740376676146967119) < 10^(-27)
> True
> }}}
> That would be less dangerous, while still allowing the necessary flexibility. 

The first question I personally need answering is should the number be real or complex? 

I might guess the small imaginary component should not be there at all, but would my guess be right? I'm not a mathematician. 

Only when I know the answer to that question do I feel able to comment on a test. 

Given the number of digits that are printed (> 16), this would suggest to me that arbitrary precision maths is being used, and not just a floating point processor. If so, the answer should be the same irrespective of whether the machine is 32-bit or 64-bit. Rounding errors occur in floating point processors - they do not on integer arithmetic if done properly. 

If this is being done with just an FPU, then printing these number of digits is a bit pointless. 

Dave


---

Comment by cremona created at 2010-08-16 10:33:46

Replying to [comment:237 drkirkby]:
> Replying to [comment:236 davidloeffler]:
> 
> > Maybe rather than directly testing the answer, one could do something like this:
> > {{{
> > sage: x = [calculation]; abs(x - 2.975975720740376676146967119) < 10^(-27)
> > True
> > }}}
> > That would be less dangerous, while still allowing the necessary flexibility. 
> 
> The first question I personally need answering is should the number be real or complex? 

It is real.  The list is the list of values of `z^2` as z runs over the roots of `f = x^5 + x + 17`, which has exactly one real root, listed first.  Apart from precision the output should be the same as 

```
sage: [z[0]^2 for z in f.roots(CC)]
[2.97572074037668, -2.40889943716139 + 1.90254105303505*I, -2.40889943716139 - 1.90254105303505*I, 0.921039066973047 - 3.07553311884578*I, 0.921039066973047 + 3.07553311884578*I]
```

The function being tested is rather general, so one could not expect the function's code to test for this special case (I think).  Still, it is disappointing that the imaginary part is not a better approximation to zero than it is.


> 
> I might guess the small imaginary component should not be there at all, but would my guess be right? I'm not a mathematician. 
> 
> Only when I know the answer to that question do I feel able to comment on a test. 
> 
> Given the number of digits that are printed (> 16), this would suggest to me that arbitrary precision maths is being used, and not just a floating point processor. If so, the answer should be the same irrespective of whether the machine is 32-bit or 64-bit. Rounding errors occur in floating point processors - they do not on integer arithmetic if done properly. 
> 
> If this is being done with just an FPU, then printing these number of digits is a bit pointless. 
> 
> Dave


---

Comment by rishi created at 2010-08-16 10:55:20

Replying to [comment:238 cremona]:
> Replying to [comment:237 drkirkby]:
> > Replying to [comment:236 davidloeffler]:
> > 
> > > Maybe rather than directly testing the answer, one could do something like this:
> > > {{{
> > > sage: x = [calculation]; abs(x - 2.975975720740376676146967119) < 10^(-27)
> > > True
> > > }}}

> It is real.  The list is the list of values of `z^2` as z runs over the roots of `f = x^5 + x + 17`, which has exactly one real root, listed first.  Apart from precision the output should be the same as 
> {{{
> sage: [z[0]^2 for z in f.roots(CC)]
> [2.97572074037668, -2.40889943716139 + 1.90254105303505*I, -2.40889943716139 - 1.90254105303505*I, 0.921039066973047 - 3.07553311884578*I, 0.921039066973047 + 3.07553311884578*I]
> }}}
> The function being tested is rather general, so one could not expect the function's code to test for this special case (I think).  Still, it is disappointing that the imaginary part is not a better approximation to zero than it is.
> 

It is a complex embedding, so the output is a [ComplexNumber](ComplexNumber), ideally with real part zero. The precision is 100 bit. This indeed makes 10^{-27} a bit disappoint.

> 
> > 
> > I might guess the small imaginary component should not be there at all, but would my guess be right? I'm not a mathematician. 
> > 
> > Only when I know the answer to that question do I feel able to comment on a test. 
> > 
> > Given the number of digits that are printed (> 16), this would suggest to me that arbitrary precision maths is being used, and not just a floating point processor. If so, the answer should be the same irrespective of whether the machine is 32-bit or 64-bit. Rounding errors occur in floating point processors - they do not on integer arithmetic if done properly. 
> > 
> > If this is being done with just an FPU, then printing these number of digits is a bit pointless. 
> > 
> > Dave


---

Comment by rishi created at 2010-08-16 11:03:39

> It is a complex embedding, so the output is a [ComplexNumber](ComplexNumber), ideally with real part zero. The precision is 100 bit. This indeed makes 10^-27 a bit disappointing.

I meant to say imaginary part zero.


---

Attachment

Hopefully fixes problem with polynomial_quotient_ring.py


---

Comment by jdemeyer created at 2010-08-16 13:10:09

Replying to [comment:232 drkirkby]:
> 2) `devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py` *An unexpected failure.* 

Can you try the patch I just uploaded to see if it fixes the problem? I have tested this patch on a 32bit and 64bit Intel Linux system and `polynomial_quotient_ring.py` passed the tests. I haven't tested it yet against the whole sage library.


---

Comment by jdemeyer created at 2010-08-16 13:46:36

Flattening of the above sagelib patches against sage-4.5.3.alpha1


---

Attachment


---

Comment by drkirkby created at 2010-08-16 15:49:30

Whilst the doctest can be changed to make this pass, is a real bug being covered up? 

Can anyone explain why a calculation performed with integers should differ depending on whether the program is compiled 32-bit or 64-bit? Since to me, of the arbitrary precision maths is implemented correctly, they should give the same result. I never get any issues like this with the MPFR tests. 

Dave


---

Comment by jdemeyer created at 2010-08-16 15:59:54

Replying to [comment:243 drkirkby]:
> Whilst the doctest can be changed to make this pass, is a real bug being covered up? 
I would rather say on the contrary.  The problem was that we were computing the roots of a polynomial with complex non-exact roots.  I.e.: instead of computing the roots of x^5+x-17, we were computing the roots of (1.0 + 0.0*I)*x^5 + ...  I changed that in my patch.

> Can anyone explain why a calculation performed with integers should differ depending on whether the program is compiled 32-bit or 64-bit? Since to me, of the arbitrary precision maths is implemented correctly, they should give the same result.

This is not always true because the precisions might be different.  In PARI, the precision is always a multiple of the machine word size.  If you try to compute with 90 bits of precision, you will get 96 bits of precision on a 32-bit machine but you will get 128 bits of precision on a 64-bit machine.

If might be possible to change this such that PARI always uses a multiple of 64 bits of precision (I have been thinking about this), but it's not so easy.


---

Comment by jdemeyer created at 2010-08-16 15:59:54

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-08-16 16:22:18

Jeroen is right.  Almost all (and maybe all) the doctests in Sage which are tagged 32/64 bit are a result of this feature of pari's way of handling multi-precision floating point arithmetic.


---

Comment by drkirkby created at 2010-08-16 17:05:15

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-08-16 17:05:15

Replying to [comment:245 cremona]:
> Jeroen is right.  Almost all (and maybe all) the doctests in Sage which are tagged 32/64 bit are a result of this feature of pari's way of handling multi-precision floating point arithmetic.

OK, fair point. Now I understand. I was under the impression 100 bits were being used. 

After applying Jeroen's patch


```
drkirkby@hawk:~/sage-4.6.prealpha0$ ./sage -t  -long devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py
sage -t -long "devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py"
	 [30.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 30.2 seconds
```


I've set this to positive review. 

I copied all the authors to reviewers, as I think everyone that has wrote part of it has reviewed part of it. I also added Leif and François as reviewers, as they have contributed too. But I've not done an extensive search to see who should be on the reviewer and the author list. I suspect there are some missing. 

Dave


---

Comment by jdemeyer created at 2010-08-16 17:12:25

New distribution with all patches: [http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha1.tar](http://cage.ugent.be/~jdemeyer/sage/sage-4.6.prealpha1.tar)


---

Comment by leif created at 2010-08-16 17:22:54

Replying to [comment:245 cremona]:
> Jeroen is right.  Almost all (and maybe all) the doctests in Sage which are tagged 32/64 bit are a result of this feature of pari's way of handling multi-precision floating point arithmetic.

Others are due to the different width of Python's `int` type (and perhaps some due to pointer width).


---

Comment by leif created at 2010-08-16 17:47:44

Just for the record: I noticed some empty `EXAMPLES` sections (in `sage/libs/pari/gen.pyx`), some functions do not have docstrings at all.

But perhaps something for a follow-up ticket, cleaning up other docstrings as well.


---

Attachment

Doctest coverage of sage/libs/pari/gen.pyx (Sage 4.6.prealpha0)


---

Comment by leif created at 2010-08-16 19:57:10

Replying to [comment:249 leif]:
> Just for the record: I noticed some empty `EXAMPLES` sections (in `sage/libs/pari/gen.pyx`), some functions do not have docstrings at all.
> 
> But perhaps something for a follow-up ticket, cleaning up other docstrings as well.

I've attached the current [coverage report for gen.pyx](http://trac.sagemath.org/sage_trac/attachment/ticket/9343/pari-gen.pyx-coverage.txt) (Sage 4.6.prealpha0):


```
SCORE devel/sage/sage/libs/pari/gen.pyx: 55% (215 of 387)
```



---

Comment by jdemeyer created at 2010-08-17 10:20:34

I have tried to compile sage-4.6.alpha1 on an old PPC Mac OS X 10.4 and it *failed* compiling PARI.  Since this is supposed to be an officially supported platform, this should be addressed.  I also tried to compile PARI/GP stand-alone and it also failed, so the problem is upstream.  The error is the following:


```
/usr/bin/gcc  -o "/Users/jdemeyer/pari-2.4.3.svn-12577/src/Odarwin-ppc"/libpari-2.4.dylib -dynamiclib  -O3 -Wall -fno-strict-aliasing -fom
it-frame-pointer    -fPIC -Wl,-flat_namespace,-undefined,suppress  mp.o mpinl.o F2x.o FF.o Flx.o FpE.o FpV.o FpX.o Qfb.o RgV.o RgX.o ZV.o
ZX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bb_group.o bibli1.o bibli2.o bit.o buch1.o buch2.o buch
3.o buch4.o concat.o ellanal.o elliptic.o galconj.o gen1.o gen2.o gen3.o hnf_snf.o ifactor1.o lll.o perm.o polarit1.o polarit2.o polarit3.
o prime.o random.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o compile.o default.o errmsg.o es.o eval.o has
h.o init.o intnum.o members.o pariinl.o parse.o sumiter.o DedekZeta.o Hensel.o QX_factor.o aprcl.o elldata.o ellsea.o galois.o galpol.o gr
oupid.o krasner.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o darwin.o
ld: common symbols not allowed with MH_DYLIB output format with the -multi_module option
init.o definition of common _DEBUGMEM (size 4)
init.o definition of common _avma (size 4)
init.o definition of common _bot (size 4)
[...]
es.o definition of common _pariErr (size 4)
es.o definition of common _pariOut (size 4)
init.o definition of common _pari_errfile (size 4)
init.o definition of common _pari_infile (size 4)
init.o definition of common _pari_outfile (size 4)
init.o definition of common _cb_pari_err_recover (size 4)
init.o definition of common _foreignFuncFree (size 4)
init.o definition of common _cb_pari_handle_exception (size 4)
init.o definition of common _cb_pari_sigint (size 4)
init.o definition of common _cb_pari_whatnow (size 4)
init.o definition of common _foreignExprHandler (size 4)
init.o definition of common _foreignHandler (size 4)
init.o definition of common _memused (size 4)
/usr/bin/libtool: internal link edit command failed
make[1]: *** [libpari-2.4.dylib] Error 1
make: *** [gp] Error 2
```


Version of gcc (I believe this is the most recent version from Apple which exists for that machine):

```
powerpc-apple-darwin8-gcc-4.0.1 (GCC) 4.0.1 (Apple Computer, Inc. build 5367)
Copyright (C) 2005 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```


Is somebody else able to test this architecture?  Just in case the problem is with the machine and not with PARI (I know essentially nothing about Darwin, I just asked a collegue to test it on his machine).


---

Comment by leif created at 2010-08-17 11:31:37

Replying to [comment:251 jdemeyer]:
> I have tried to compile sage-4.6.alpha1 on an old PPC Mac OS X 10.4 and it *failed* compiling PARI.  Since this is supposed to be an officially supported platform, this should be addressed.  I also tried to compile PARI/GP stand-alone and it also failed, so the problem is upstream.  [...]
> Is somebody else able to test this architecture?  Just in case the problem is with the machine and not with PARI (I know essentially nothing about Darwin, I just asked a collegue to test it on his machine).

Karl-Dieter (kcrisman) has access to such a box.


---

Comment by leif created at 2010-08-17 14:24:43

Replying to [comment:251 jdemeyer]:
> I have tried to compile sage-4.6.alpha1 on an old PPC Mac OS X 10.4 and it *failed* compiling PARI.  Since this is supposed to be an officially supported platform, this should be addressed.  I also tried to compile PARI/GP stand-alone and it also failed, so the problem is upstream.  The error is the following:
> 

```
/usr/bin/gcc  -o "/Users/jdemeyer/pari-2.4.3.svn-12577/src/Odarwin-ppc"/libpari-2.4.dylib -dynamiclib  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -fPIC -Wl,-flat_namespace,-undefined,suppress  mp.o mpinl.o F2x.o FF.o Flx.o FpE.o FpV.o FpX.o Qfb.o RgV.o RgX.o ZV.o ZX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bb_group.o bibli1.o bibli2.o bit.o buch1.o buch2.o buch3.o buch4.o concat.o ellanal.o elliptic.o galconj.o gen1.o gen2.o gen3.o hnf_snf.o ifactor1.o lll.o perm.o polarit1.o polarit2.o polarit3.o prime.o random.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o compile.o default.o errmsg.o es.o eval.o hash.o init.o intnum.o members.o pariinl.o parse.o sumiter.o DedekZeta.o Hensel.o QX_factor.o aprcl.o elldata.o ellsea.o galois.o galpol.o groupid.o krasner.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o darwin.o
ld: common symbols not allowed with MH_DYLIB output format with the -multi_module option
init.o definition of common _DEBUGMEM (size 4)
init.o definition of common _avma (size 4)
init.o definition of common _bot (size 4)
[...]
es.o definition of common _pariErr (size 4)
es.o definition of common _pariOut (size 4)
init.o definition of common _pari_errfile (size 4)
init.o definition of common _pari_infile (size 4)
init.o definition of common _pari_outfile (size 4)
init.o definition of common _cb_pari_err_recover (size 4)
init.o definition of common _foreignFuncFree (size 4)
init.o definition of common _cb_pari_handle_exception (size 4)
init.o definition of common _cb_pari_sigint (size 4)
init.o definition of common _cb_pari_whatnow (size 4)
init.o definition of common _foreignExprHandler (size 4)
init.o definition of common _foreignHandler (size 4)
init.o definition of common _memused (size 4)
/usr/bin/libtool: internal link edit command failed
make[1]: *** [libpari-2.4.dylib] Error 1
make: *** [gp] Error 2
```


Perhaps add `-fno-common` to `DLCFLAGS` in `config/get_dlcflags` if `$osname` is `darwin`.

Just a guess, I don't play with apples.


---

Comment by leif created at 2010-08-17 14:46:26

Replying to [comment:253 leif]:
> Perhaps add `-fno-common` to `DLCFLAGS` in `config/get_dlcflags` if `$osname` is `darwin`.
> 
> Just a guess, I don't play with apples.

I'm pretty sure this will fix it. In PARI 2.3.x, we patched `get_dlcflags`:

```sh
_dl_list="DLCFLAGS"
if test -n "$__gnuc__"; then
  # Some architectures need -fPIC for building dynamic lib
  # *-i?86|*-sparc*|*-powerpc|*-s390|*-mips) DLCFLAGS=
  case "$osname-$arch" in
    *-hppa|*-ia64|*-alpha|*-arm|*-m68k|*linux-ppc) DLCFLAGS=-fPIC ;;
    *-x86_64|*-sparc*|*-amd64) case "$sizeof_long" in
              8) DLCFLAGS=-fPIC;;
              esac;;
    darwin-*) DLCFLAGS=-fno-common;;
  esac
else
  case "$osname-$arch" in
    hpux-*) DLCFLAGS=+z;;
    solaris-sparc*) case "$sizeof_long" in
              8) DLCFLAGS=-KPIC;; # assume sun cc
              esac;;
  esac
fi

echo "C compiler is          $CC $CFLAGS $DLCFLAGS"
```


(Note the `darwin-*`. A number of other changes has been dropped...)


---

Comment by leif created at 2010-08-17 14:59:09

Dave, could you check if we still need (some of) the dropped changes for Solaris and HP-UX?

(I suspect except for the `-fPIC`, we'll need these, too.)


---

Comment by leif created at 2010-08-17 15:35:28

I think `spkg-install` needs some work anyway:

 * Shouldn't `SAGE_TUNE_pari` be `SAGE_TUNE_PARI`?
 * I don't understand why we _unconditionally_ add `--graphic=none` to `./Configure`. (This is already added if `$PARI_EXTRA_OPTS` are empty.)
 * The test of `$?` at the bottom is redundant/superfluous, or even wrong; we should simply `exit 1` there, or change the whole `if-then` logic, e.g. using `elif`. (Shouldn't it be a build error if `$SAGE_LOCAL/lib/libpari.so` is not present on any system except Darwin? A test for Cygwin's DLL is completely missing there, so we'd have to add that, too.)


---

Comment by drkirkby created at 2010-08-17 15:52:25

Replying to [comment:256 leif]:
> I think `spkg-install` needs some work anyway:
> 
>  * Shouldn't `SAGE_TUNE_pari` be `SAGE_TUNE_PARI`?
I forget who it was, but someone proposed something like this SAGE_THREADS_$packagename where the '$packagename' would be lower case. I think that's quite a reasonable idea. It potentially allows the name to be automatically generated. 

If you want to clean it up, it would be better to open another ticket for that.


---

Comment by jdemeyer created at 2010-08-17 16:13:13

Replying to [comment:253 leif]:
> Perhaps add `-fno-common` to `DLCFLAGS` in `config/get_dlcflags` if `$osname` is `darwin`.

Great!  This fixes the problem indeed (at least on this particular machine).  I have reported this upstream.


---

Comment by jdemeyer created at 2010-08-17 16:37:58

Anybody with access to a Darwin machine: please test


```
sage -i http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg
```


starting from either a vanilla Sage or an already-9343-patched Sage. The main thing is to see whether this *compiles* properly.


---

Comment by leif created at 2010-08-17 16:40:25

Replying to [comment:255 leif]:
> Dave, could you check if we still need (some of) the dropped changes for Solaris and HP-UX?
> 
> (I suspect except for the `-fPIC`, we'll need these, too.)

Ok, `+z` is used on HP-UX and `-KPIC` on Solaris if the compiler is not gcc, you in addition tested for SPARC and 64-bit on Solaris though...


---

Comment by jhpalmieri created at 2010-08-17 17:17:42

I notice this message when pari is being installed:

```
To sage build time, Pari will not be tuned for your systems
If you want higher performance, at the expense of a slower build
set the environment variable SAGE_TUNE_pari=yes by typing the following
before building Sage (or at least before building Pari)
```

Aside from the lack of punctuation (a very minor point), I think there is a word missing in the first line: should it say "To _minimize_ sage build time" or something like that?

Also, if you're introducing the environment variable `SAGE_TUNE_pari`, you should also document it in the Sage installation guide -- see the section on environment variables in SAGE_ROOT/devel/sage/doc/en/installation/source.rst.


---

Comment by drkirkby created at 2010-08-17 17:30:14

Replying to [comment:260 leif]:
> Replying to [comment:255 leif]:
> > Dave, could you check if we still need (some of) the dropped changes for Solaris and HP-UX?
> > 
> > (I suspect except for the `-fPIC`, we'll need these, too.)
> 
> Ok, `+z` is used on HP-UX and `-KPIC` on Solaris if the compiler is not gcc, you in addition tested for SPARC and 64-bit on Solaris though...

When were these dropped - since I tested this on OpenSolaris, or are these other changes? I can't keep up with the changes on this ticket! 

Without trying to build in HP-UX I don't know for sure what will be needed, and I don't have time to try that now. 

Dave


---

Comment by jdemeyer created at 2010-08-17 17:38:12

Replying to [comment:262 drkirkby]:
> When were these dropped - since I tested this on OpenSolaris, or are these other changes? I can't keep up with the changes on this ticket! 
By looking at `hg log`: 22 July 2010 (or possibly before)


---

Comment by drkirkby created at 2010-08-17 17:41:28

Replying to [comment:261 jhpalmieri]:
> I notice this message when pari is being installed:
> {{{
> To sage build time, Pari will not be tuned for your systems
> If you want higher performance, at the expense of a slower build
> set the environment variable SAGE_TUNE_pari=yes by typing the following
> before building Sage (or at least before building Pari)
> }}}
> Aside from the lack of punctuation (a very minor point), I think there is a word missing in the first line: should it say "To _minimize_ sage build time" or something like that?

Yes agreed. I'll create a patch and attach it to the ticket. 

> Also, if you're introducing the environment variable `SAGE_TUNE_pari`, you should also document it in the Sage installation guide -- see the section on environment variables in SAGE_ROOT/devel/sage/doc/en/installation/source.rst.

That is now #9756


---

Comment by drkirkby created at 2010-08-17 17:44:02

Replying to [comment:263 jdemeyer]:
> Replying to [comment:262 drkirkby]:
> > When were these dropped - since I tested this on OpenSolaris, or are these other changes? I can't keep up with the changes on this ticket! 
> By looking at `hg log`: 22 July 2010 (or possibly before)

In that case, it's pointless worrying about them now. Sage will not build with SunStudio and does not build on HP-UX. These are two things I'd like to fix (especially the former), but they are not critical to this ticket. Any issues like that can go on another ticket. 

Dave


---

Comment by jdemeyer created at 2010-08-17 17:45:34

Replying to [comment:264 drkirkby]:
> Yes agreed. I'll create a patch and attach it to the ticket.
Thanks, but I already did it.  New spkg (same name): [http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg)


---

Comment by jhpalmieri created at 2010-08-17 17:49:27

Two more comments:

 - I can't get this to build on t2.  I get an error message

```
Extracting examples/Makefile.solaris-sparcv9
Extracting Osolaris-sparcv9/Makefile
./Configure: test: argument expected
ERROR - configure PARI with readline and gmp failed.
```

I've put the full log here: [http://sage.math.washington.edu/home/palmieri/misc/pari-2.4.3.svn-12577.log](http://sage.math.washington.edu/home/palmieri/misc/pari-2.4.3.svn-12577.log).

 - on a Mac OS X 10.6 machine (intel), the spkg included in sage-4.6.prealpha1.tar seems to build fine, although I haven't finished building the rest of Sage or doing doctests.  But if I do `export SAGE_TUNE_pari=yes`, then it doesn't build.  Here's an excerpt from the log:

```
In file included from ../src/test/tune.c:21:
../src/headers/pari.h:59:21: error: mpinl.h: No such file or directory
../src/test/tune.c: In function 'speed_redc':
../src/test/tune.c:213: warning: implicit declaration of function 'int_LSW'
../src/test/tune.c:213: error: invalid type argument of 'unary *'
../src/test/tune.c: In function 'speed_modii':
../src/test/tune.c:216: error: invalid type argument of 'unary *'
../src/test/tune.c: In function 'speed_remiimul':
../src/test/tune.c:220: error: invalid type argument of 'unary *'
make[2]: *** [tune.o] Error 1
./Configure: line 168: tune: command not found
```

If I use the new spkg [http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg), then it gets past this error.  It's not done building yet, though...


---

Comment by jhpalmieri created at 2010-08-17 17:58:08

By the way, "hg status" reports

```
? patches/files/base2.c
? patches/files/get_dlcflags
? patches/files/get_ld
? patches/files/get_tests
? patches/files/gphelp.in
? patches/files/init.c
? patches/files/mp.c
? patches/files/paripriv.h
? patches/files/polarit3.c
```



---

Comment by jdemeyer created at 2010-08-17 18:07:57

Replying to [comment:268 jhpalmieri]:
> By the way, "hg status" reports
> {{{
> ? patches/files/base2.c
> ? patches/files/get_dlcflags
> ? patches/files/get_ld
> ? patches/files/get_tests
> ? patches/files/gphelp.in
> ? patches/files/init.c
> ? patches/files/mp.c
> ? patches/files/paripriv.h
> ? patches/files/polarit3.c
> }}}

I'm not sure what the question mark means, but these files are not supposed to be under revision control.  They are generated by my `spkg-make` script from the corresponding patches/*.patch files.


---

Comment by drkirkby created at 2010-08-17 18:11:54

This needs work now. 

 * It's not building on 't2'
 * SPKG.txt needs updating
 * If the files in {{{patches/files}} directory are not supposed to be under revision control, then the directory should be added to .hgignore. But it's hard to understand why the files should be present, but not under revision control.


---

Comment by drkirkby created at 2010-08-17 18:11:54

Changing status from positive_review to needs_work.


---

Comment by leif created at 2010-08-17 18:14:38

Replying to [comment:269 jdemeyer]:
> Replying to [comment:268 jhpalmieri]:
> > By the way, "hg status" reports

```
? patches/files/base2.c
? patches/files/get_dlcflags
? patches/files/get_ld
? patches/files/get_tests
? patches/files/gphelp.in
? patches/files/init.c
? patches/files/mp.c
? patches/files/paripriv.h
? patches/files/polarit3.c
```

> 
> I'm not sure what the question mark means, but these files are not supposed to be under revision control.  They are generated by my `spkg-make` script from the corresponding patches/*.patch files.

In that case, you'd have to add them to `.hgignore`.


---

Comment by jhpalmieri created at 2010-08-17 18:16:04

I'm having problems with tuning.  If I do `export SAGE_TUNE_pari=yes`, then on both sage.math and on my Intel Mac OS X 10.6, the build fails.  Logs are here:

 - http://sage.math.washington.edu/home/palmieri/misc/tuning.sage-math.pari-2.4.3.svn-12577.log
 - http://sage.math.washington.edu/home/palmieri/misc/tuning.mac.pari-2.4.3.svn-12577.p2.log

On sage.math at least, if I don't tell it to tune, then everything builds and all tests pass.  On the mac, everything builds, but it hasn't finished testing.


---

Comment by leif created at 2010-08-17 18:21:41

Replying to [comment:272 jhpalmieri]:
> I'm having problems with tuning.  If I do `export SAGE_TUNE_pari=yes`, then on both sage.math and on my Intel Mac OS X 10.6, the build fails.  Logs are here:
> 
>  - http://sage.math.washington.edu/home/palmieri/misc/tuning.sage-math.pari-2.4.3.svn-12577.log
>  - http://sage.math.washington.edu/home/palmieri/misc/tuning.mac.pari-2.4.3.svn-12577.p2.log
> 
> On sage.math at least, if I don't tell it to tune, then everything builds and all tests pass.  On the mac, everything builds, but it hasn't finished testing.

Reinstalling the package with `SAGE_TUNE_pari=yes` hangs for me on Fedora 13 x86 (Pentium 4 Prescott); I doubt it will take more than an hour to tune a single function:

```
...
Setting INVNEWTON_LIMIT... (default 803)
              algorithm-A  algorithm-B   ratio  possible
               (seconds)    (seconds)    diff    thresh
size =  66     0.00001332   0.00001739   0.2340    66
size =  67     0.00001441   0.00001736   0.1700    67
size =  69     0.00001627   0.00001851   0.1208    69
size =  71     0.00001636   0.00001891   0.1345    71
size =  73     0.00001632   0.00002036   0.1983    73
size =  75     0.00001836   0.00002218   0.1721    75
size =  77     0.00001818   0.00002236   0.1869    77
size =  79     0.00002042   0.00002363   0.1358    79
size =  81     0.00002082   0.00002545   0.1821    81
size =  83     0.00002345   0.00002527   0.0718    83
size =  85     0.00002345   0.00002586   0.0931    85
size =  87     0.00002234   0.00002745   0.1863    87
size =  89     0.00002545   0.00002897   0.1217    89
size =  91     0.00002672   0.00002891   0.0756    91
size =  93     0.00002709   0.00003054   0.1132    93
size =  95     0.00002799   0.00002972   0.0582    95
size =  97     0.00002927   0.00003105   0.0575    97

```



---

Comment by leif created at 2010-08-17 18:25:59

(Oh, the last blank line was unintentionally added by me.)


---

Comment by drkirkby created at 2010-08-17 19:39:56

I suggest if the tuning is not reliable, we do not prevent it being used, but issue a warning not to use it. Then we can get people to test the tuning, and report where it works and where it does not. It certainly built OK on OpenSolaris. 

Dave


---

Comment by leif created at 2010-08-17 20:16:31

Replying to [comment:275 drkirkby]:
> I suggest if the tuning is not reliable, we do not prevent it being used, but issue a warning not to use it. Then we can get people to test the tuning, and report where it works and where it does not. It certainly built OK on OpenSolaris. 

Hmmm, I reproducably get (PARI-catched) segfaults (everytime at the same point) on Ubuntu 9.04 x86_64 (Core2, gcc 4.5.0)...

One the Fedora machine, `tune -t` is meanwhile at 3h 12m CPU time (without further output), so I'll assume it will run forever and terminate it.


---

Comment by jdemeyer created at 2010-08-17 20:39:00

Replying to [comment:267 jhpalmieri]:
> Two more comments:
> 
>  - I can't get this to build on t2.  I get an error message
> {{{
> Extracting examples/Makefile.solaris-sparcv9
> Extracting Osolaris-sparcv9/Makefile
> ./Configure: test: argument expected
> ERROR - configure PARI with readline and gmp failed.
> }}}

Please try compiling PARI by itself to check whether this is an upstream problem:

```
$ tar xjf pari-2.4.3.svn-12577.p2.spkg
$ cd pari-2.4.3.svn-12577.p2/src
$ ./Configure
$ make gp
```



---

Comment by jhpalmieri created at 2010-08-17 20:48:04

Replying to [comment:277 jdemeyer]:

> Please try compiling PARI by itself to check whether this is an upstream problem:

I get the same error after typing `./Configure`:

```
==========================================================================
Extracting examples/Makefile.solaris-sparcv9
Extracting Osolaris-sparcv9/Makefile
./Configure: test: argument expected
```

Unfortunately skynet is down, so I don't have access to any other Solaris machines right now to test on.


---

Comment by drkirkby created at 2010-08-17 20:56:04

Replying to [comment:278 jhpalmieri]:
> Replying to [comment:277 jdemeyer]:
> 
> > Please try compiling PARI by itself to check whether this is an upstream problem:
> 
> I get the same error after typing `./Configure`:
> {{{
> ==========================================================================
> Extracting examples/Makefile.solaris-sparcv9
> Extracting Osolaris-sparcv9/Makefile
> ./Configure: test: argument expected
> }}}
> Unfortunately skynet is down, so I don't have access to any other Solaris machines right now to test on.


I've powered up my Sun Blade 1000. I will report back later once I've copied the necessary files to it and started a build. 

Dave


---

Comment by drkirkby created at 2010-08-17 20:59:27

I'm attaching a patch which reports:


```
Pari will be tuned for your system since you set SAGE_TUNE_pari="yes". This can take a long time.
WARNING: Tuning Pari is VERY unreliable. You may find your build
of Pari fails, or Pari does not work properly once built.
```


or 


```
To minimize Sage build time and to ensure the best relieability,
Pari will not be tuned for your system. Experience shows tuning
is unreliable - see
http://trac.sagemath.org/sage_trac/ticket/9343
If you wish to test the tuning code, set the environment
variable SAGE_TUNE_pari=yes by typing the following
before building Sage (or at least before building Pari):
SAGE_TUNE_pari=yes
export SAGE_TUNE_pari
```


depending on whether `SAGE_TUNE_pari` i set to "yes" or not. 

Dave


---

Attachment

Print information about how to use SAGE_TUNE_pari and the risks it has.


---

Comment by drkirkby created at 2010-08-17 21:26:01

I can confirm what John found on 't2.math' - this package is now broken on Solaris 10 SPARC in at least 32-it mode. 

This is on my own personal machine, a Sun Blade 1000 with a pair of 900 MHz UltraSPARC III+ CPUs. It runs the very first release of Solaris 10 (March 2005), whereas t2.math runs a quite recent version. 

I think we are seeing the problems of working with unstable snapshots. An updated Pari was working on 't2' a few weeks ago - I posted the list of test failures above. Since then, the snapshot has been updated, which no doubt fixes one problem, but creates another. Last I noticed, the upstream snapshot was being updated three times per day on average. Clearly the snapshots are not well tested, yet we are using them, and doing the tests ourselves.

I suggest that we report this, and try to get a fix. But rather than download the latest snapshot, we just apply the fix we actually need. Otherwise we have to go thought a lengthly test cycle again. I'm sure it will be tempting to update to the latest snapshot to get even more bugs fixed, but how many will be added? 

Worth reading is a book by Fred Brooks called The Mythical Man-Month. 

Of particular note here is is point that [that in a suitably complex system there is a certain irreducible number of errors. Any attempt to fix observed errors tends to result in the introduction of other errors.](http://en.wikipedia.org/wiki/The_Mythical_Man-Month#The_tendency_towards_irreducible_number_of_errors) 


```
32 drkirkby@redstart:[~/src] $ uname -a
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
32 drkirkby@redstart:[~/src] $ cat /etc/release
                         Solaris 10 3/05 s10_74L2a SPARC
           Copyright 2005 Sun Microsystems, Inc.  All Rights Reserved.
                        Use is subject to license terms.
                            Assembled 22 January 2005
32 drkirkby@redstart:[~/src] $ ./Configure
Configuring pari-2.4.3 (DEVELOPMENT VERSION) [ development svn-12577 ]
Checking echo to see how to suppress newlines...
...using \c
Looking for some tools first ...
...ld is /usr/ccs/bin/ld
...zcat is /usr/bin/zcat
...gzip is /usr/bin/gzip
...ranlib is /usr/ccs/bin/ranlib
...perl is /usr/bin/perl
Looking for the compilers ...
...cc is /usr/ucb/cc
...gcc is /usr/local/gcc-4.5.0/bin/gcc
GNU compiler version 4.5.0 (GCC gmp-5.0.1 mpfr-3.0.0 mpc-0.8.2)
Given the previous choices, sizeof(long) is 4 chars.
The internal word representation of a double is l[0], l[1].
==========================================================================
Building for: UltraSparc running solaris (MicroSparc/GMP kernel) 32-bit version
==========================================================================
C compiler is          /usr/local/gcc-4.5.0/bin/gcc -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -fPIC
Executable linker is   /usr/local/gcc-4.5.0/bin/gcc  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    
Dynamic Lib linker is  /usr/local/gcc-4.5.0/bin/gcc  -shared -mimpure-text $(CFLAGS) $(DLCFLAGS) -Wl,-G,-h,$(LIBPARI_SONAME) 
Looking in C lib for some symbols...
...Found exp2.
...Found log2.
...Found strftime.
...Found getrusage.
...Found sigaction.
...Found TIOCGWINSZ.
...Found getrlimit.
...Found stat.
...Found vsnprintf.
...Found waitpid.
...Found setsid.
...Found getenv.
...Found isatty.
...Found alarm.
...Found dlopen.
Checking for optional libraries and headers...
### Building without GNU MP support
...Found libX11 in /usr/openwin/lib
...Found X11 header files in /usr/openwin/include/X11
...Extra Libraries are -lsocket -lnsl
Hi-Res Graphics: X11
### Building without GNU readline support
Installation prefix ? [/usr/local]
...for architecture-independent files (share-prefix) ? [/usr/local/share]
Installation directories for:
...executables (gp, gphelp) ? [/usr/local/bin]
...libraries (libpari) ? [/usr/local/lib]
...include files ? [/usr/local/include]
...manual pages ? [/usr/local/share/man/man1]
...other system-dependent data ? [/usr/local/lib/pari]
...other system-independent data ? [/usr/local/share/pari]
Default is dynamic executable and shared library
==========================================================================
Extracting examples/Makefile.solaris-sparcv9
Extracting Osolaris-sparcv9/Makefile
./Configure: test: argument expected
32 drkirkby@redstart:[~/src] $ 
```



---

Comment by jdemeyer created at 2010-08-17 21:29:26

Replying to [comment:276 leif]:
> Hmmm, I reproducably get (PARI-catched) segfaults (everytime at the same point) on Ubuntu 9.04 x86_64 (Core2, gcc 4.5.0)...

Same here, Gentoo Linux, x86_64 Intel Core2, 64bit, gcc 4.6.0.

So tuning is *completely broken*.


---

Comment by drkirkby created at 2010-08-17 21:34:05

Replying to [comment:282 jdemeyer]:
> Replying to [comment:276 leif]:
> > Hmmm, I reproducably get (PARI-catched) segfaults (everytime at the same point) on Ubuntu 9.04 x86_64 (Core2, gcc 4.5.0)...
> 
> Same here, Gentoo Linux, x86_64 Intel Core2, 64bit, gcc 4.6.0.
> 
> So tuning is *completely broken*.

It works on OpenSolaris - or at least it did do when I tested it before. 

Dave


---

Comment by jdemeyer created at 2010-08-17 21:41:16

Replying to [comment:278 jhpalmieri]:
> I get the same error after typing `./Configure`:
> {{{
> ==========================================================================
> Extracting examples/Makefile.solaris-sparcv9
> Extracting Osolaris-sparcv9/Makefile
> ./Configure: test: argument expected
> }}}

Please try

```
/bin/sh -c "test -d"
```

in a shell and see what happens.


---

Comment by jhpalmieri created at 2010-08-17 21:48:21

Replying to [comment:284 jdemeyer]:
> Please try

```
/bin/sh -c "test -d"
```

> in a shell and see what happens.


```
$ /bin/sh -c "test -d"
/bin/sh: test: argument expected
```



---

Comment by jdemeyer created at 2010-08-17 21:56:40

Maybe the solaris problem is due to `config/Makefile.SH`, but it's hard to debug without access to a Solaris box.  There are several unquoted `test` statements in that file, probably one of them is the culprit.  Also, that file has changed recently.


---

Comment by mpatel created at 2010-08-17 22:18:44

Replying to [comment:286 jdemeyer]:
> Maybe the solaris problem is due to `config/Makefile.SH`, but it's hard to debug without access to a Solaris box.  There are several unquoted `test` statements in that file, probably one of them is the culprit.  Also, that file has changed recently.

William (Stein) should be able to make an account for you on the Sage cluster, which includes the Solaris 10 SPARC machine t2.math.washington.edu.  Just send him an email.


---

Comment by drkirkby created at 2010-08-17 22:35:59

Replying to [comment:283 drkirkby]:
> Replying to [comment:282 jdemeyer]:
> > Replying to [comment:276 leif]:
> > > Hmmm, I reproducably get (PARI-catched) segfaults (everytime at the same point) on Ubuntu 9.04 x86_64 (Core2, gcc 4.5.0)...
> > 
> > Same here, Gentoo Linux, x86_64 Intel Core2, 64bit, gcc 4.6.0.
> > 
> > So tuning is *completely broken*.
> 
> It works on OpenSolaris - or at least it did do when I tested it before. 
> 
> Dave 

It's now busted on OpenSolaris too!


---

Comment by leif created at 2010-08-17 23:05:06

To report something _positive_, I've successfully - *without* PARI tuning - built and tested (`ptestlong`) the prealpha1 on:
 * Fedora 13 x86 (P4 Prescott, gcc 4.4.4, native code with `O2`, parallel build with 6 jobs)
 * Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3, native code with `O3`, parallel build with 32 jobs)
 * Ubuntu 9.04 x86_64 (Core2, gcc 4.5.0, native code with `O3`, parallel build with 16 jobs)

Btw, FLTK-devel was installed (and almost all X11 developer packages); PARI correctly did *not* attempt to build with this (since we configure with `--graphic=none`).


---

Comment by jdemeyer created at 2010-08-18 19:06:17

Tuning errors reported to PARI/GP development: [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1089](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1089)


---

Comment by mpatel created at 2010-08-19 11:13:38

Changing priority from major to blocker.


---

Comment by leif created at 2010-08-19 11:26:59

Replying to [comment:289 leif]:
> To report something _positive_, I've successfully - *without* PARI tuning - built and tested (`ptestlong`) the prealpha1 on:
 * Fedora 13 x86 (P4 Prescott, gcc 4.4.4, native code with `O2`, parallel build with 6 jobs)
 * Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3, native code with `O3`, parallel build with 32 jobs)
 * Ubuntu 9.04 x86_64 (Core2, gcc 4.5.0, native code with `O3`, parallel build with 16 jobs)

Also:
 * Ubuntu 9.04 x86 (P4 Prescott, gcc 4.3.3, native code without opt., parallel build with 6 jobs)

> Btw, FLTK-devel was installed (and almost all X11 developer packages); PARI correctly did *not* attempt to build with this (since we configure with `--graphic=none`).

I think I've found the culprit of #9722 (PARI attempting to use FLTK for no reason):
*Lots* of "local" variables used in the PARI scripts aren't reset/initialized.

Try, e.g.:

```sh
$ export with_fltk=yes
$ ./Configure --graphic=none
```

in the PARI source directory, or

```sh
$ export with_fltk=yes
$ unset PARI_EXTRA_OPTS
$ ./sage -f pari-2.3.5.p2 # or the appropriate PARI version, e.g. 2.4.3.svn-12577.p2
```

in `$SAGE_ROOT`.


---

Comment by leif created at 2010-08-19 12:02:59

(The above doesn't _fail_ in all cases, but PARI _attempts_ to use X11 or FLTK despite `--graphic=none` given. On Ubuntu, I had to create a symbolic link from `/usr/lib/libfltk.so` to `/usr/lib/libfltk.so.1.1` to produce the _compilation_ error reported at #9722, _with_ X11 developer packages, and with just FLTK, not FLTK-devel installed.)


---

Comment by jdemeyer created at 2010-08-21 11:01:45

To the people who cannot compile PARI/GP because of #9722:

Please check whether the following works:
 * Download [http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg)
In a shell, type:

```
tar xjf pari-2.4.3.svn-12577.p2.spkg
cd pari-2.4.3.svn-12577.p2/src
./Configure --graphic=none
make gp
```


On my system (Gentoo Linux), this correctly disables graphics.


---

Comment by leif created at 2010-08-21 13:58:43

Jeroen, the last changes to p3 (`SPKG.txt`, `patches/README.txt`) aren't yet committed.

Thanks for setting up the Wiki page.

I'm working on #9722 btw, still hoping that it will make it into 4.5.3, since I don't believe 4.6 will be ready in time, and/or don't expect people to install a brand new major release (despite the ".0" missing) right before a new semester starts.

I'll take a closer look at p3 later; I don't think `PARI_EXTRA_OPTS` is yet documented though.


---

Comment by leif created at 2010-08-21 14:53:30

Jeroen, IIRC 4.6.prealpha1 is based on 4.5.3.alpha*0*, and doesn't contain all of the latest (#9343) changes, so perhaps update/correct the Wiki page s.t. people will test the lastest PARI(-related) spkgs and patches, not the old one(s) contained in the complete Sage distribution.

Please excuse if I'm wrong here...

(In case you prepare a new one, I think it should be prealpha2 to avoid confusion with the previous one.)


---

Comment by jdemeyer created at 2010-08-21 15:12:17

Replying to [comment:296 leif]:
> Jeroen, the last changes to p3 (`SPKG.txt`, `patches/README.txt`) aren't yet committed.
Done, spkg changed with same name.


---

Comment by jdemeyer created at 2010-08-21 15:46:55

Replying to [comment:297 leif]:
> (In case you prepare a new one, I think it should be prealpha2 to avoid confusion with the previous one.)

I will post a prealpha2 later today which will also include #9400.


---

Comment by jdemeyer created at 2010-08-21 22:22:47

New distribution: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha2.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha2.tar)
For more info, see [http://wiki.sagemath.org/NewPARI](http://wiki.sagemath.org/NewPARI)


---

Comment by drkirkby created at 2010-08-22 09:18:41

Replying to [comment:300 jdemeyer]:
> New distribution: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha2.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha2.tar)
> For more info, see [http://wiki.sagemath.org/NewPARI](http://wiki.sagemath.org/NewPARI)

This distro is still broken on *any* form of Solaris - both SPARC and x86. 


```
Extracting examples/Makefile.solaris-sparcv9
Extracting Osolaris-sparcv9/Makefile
./Configure: test: argument expected
ERROR - configure PARI with readline and gmp failed.

real	0m12.936s
user	0m3.857s
sys	0m5.748s
sage: An error occurred while installing pari-2.4.3.svn-12577.p3
```


One of your earlier releases, based on a snapshot prior to 12577 was OK, so this is a very recently introduced bug. 

Dave


---

Comment by jdemeyer created at 2010-08-22 14:41:56

I found out what prevents PARI/GP from compiling on Solaris.  The problem is that `/bin/sh` from Solaris doesn't know about `test -e <filename>`.
So there are two solutions:

*Solution 1*: In `Configure`, replace
{{{#! /bin/sh
```

by

```/usr/bin/env bash
```


*Solution 2*: In `config/Makefile.SH`, replace all occurances of

```
test -e
```

by

```
test -f
```


Using either of these solutions makes PARI/GP compile.

Since Sage assumes the existence of `bash`, we might as well apply the first solution anyway.  I will report this upstream.


---

Attachment

Complete spkg patch (for reference)


---

Comment by jdemeyer created at 2010-08-22 20:03:39

* PARI/GP bug report about Solaris: [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1091](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1091)
 * New PARI spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p4.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p4.spkg)
 * New distribution: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar)


---

Comment by leif created at 2010-08-22 20:28:56

Replying to [comment:303 jdemeyer]:
>  * PARI/GP bug report about Solaris: [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1091](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1091)
>  * New PARI spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p4.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p4.spkg)
>  * New distribution: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar)

Any changes in p4 / prealpha3 other than the Solaris fix?


---

Comment by jdemeyer created at 2010-08-23 10:34:50

Replying to [comment:304 leif]:
> Any changes in p4 / prealpha3 other than the Solaris fix?

In sage-4.6.prealpha3, I merged #9703 and #9735 which hopefully makes Sage pass all tests on Solaris.


---

Comment by drkirkby created at 2010-08-23 11:17:37

Replying to [comment:305 jdemeyer]:
> Replying to [comment:304 leif]:
> > Any changes in p4 / prealpha3 other than the Solaris fix?
> 
> In sage-4.6.prealpha3, I merged #9703 and #9735 which hopefully makes Sage pass all tests on Solaris.

It was not necessary to include #9703 and #9735 for Sage to pass all doc tests on Solaris 10 (SPARC), which is the only currently supported version of Solaris on Sage. Both of those tickets only affect x86 versions. They will not do any harm, but they were unnecessary. 

However, since #9703 has been merged, I would request that anyone that builds sage-4.6.prealpha3.tar, that they report on ticket #9703 of the success or failure of these three tests:


```
	sage -t  -long devel/sage/sage/modular/abvar/abvar.py # 
	sage -t  -long devel/sage/sage/lfunctions/sympow.py # 
	sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py 
```


#9703 still awaits positive review, so clearly evidence it is working on many systems will add to the confidence that the ticket is valid. Just adding a quick comment like "The three tests passed on <your system>" would be useful. 

Neither are those two tickets sufficient to cause all doc tests on Solaris 10 on x86 or OpenSolaris on x86, though they will reduce the number of failures. A couple more tickets need to be merged to get all doc tests to pass on Solaris 10 x86 - these are #9689 and #9693. However, that's outside the scope of the Pari upgrade, so I'm not expecting you to merge them, though if you did create a later alpha, I would not object if you did merge them!

Dave


---

Comment by ggrafendorfer created at 2010-08-23 13:41:10

Replying to [comment:294 jdemeyer]:
> To the people who cannot compile PARI/GP because of #9722:
> 
> Please check whether the following works:
>  * Download [http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg)
> In a shell, type:
> {{{
> tar xjf pari-2.4.3.svn-12577.p2.spkg
> cd pari-2.4.3.svn-12577.p2/src
> ./Configure --graphic=none
> make gp

worked fine on Fedora 13, 

Georg
> }}}
> 
> On my system (Gentoo Linux), this correctly disables graphics.


---

Comment by leif created at 2010-08-23 14:38:48

Replying to [comment:303 jdemeyer]:
>  * New distribution: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar)

Passed `ptestlong` on Fedora 13 x86_64 (Core2, gcc 4.4.4, native code, `O3`), parallel build with 32 jobs, test with 4 threads.

Ubuntu 9.04 x86 in progress.

Dave, a bit more happy now?


---

Comment by jdemeyer created at 2010-08-23 15:14:07

Sage 4.6.prealpha3, which includes this ticket, passed all tests (ptestlong) on a Sun UltraSPARC with Solaris 10.


---

Comment by cremona created at 2010-08-23 15:28:16

Replying to [comment:309 jdemeyer]:
> Sage 4.6.prealpha3, which includes this ticket, passed all tests (ptestlong) on a Sun UltraSPARC with Solaris 10.

4.6.prealpha3 built fine and passed all tests (ptestlong) on 64-bit ubuntu.  Also built on 32-bit Suse, tests still running.


---

Comment by jdemeyer created at 2010-08-24 10:17:03

Now that sgae-4.5.3.alpha2 is released, I plan to make a new 4.6.prealpha4 based on that. I will do my best to port #9722. Any other tickets which should be included (which are not in sage-4.5.3.alpha2)?


---

Comment by drkirkby created at 2010-08-24 10:41:12

Replying to [comment:311 jdemeyer]:
> Now that sgae-4.5.3.alpha2 is released, I plan to make a new 4.6.prealpha4 based on that. I will do my best to port #9722. Any other tickets which should be included (which are not in sage-4.5.3.alpha2)?
I would just keep my eye on the list of blockers for 4.5.3. There is a way of getting that list, but I don't know the link.


---

Comment by leif created at 2010-08-24 10:56:40

Replying to [comment:311 jdemeyer]:
> Now that sgae-4.5.3.alpha2 is released, I plan to make a new 4.6.prealpha4 based on that. I will do my best to port #9722.

If you have little patience, I'll backport the changes from #9722 to #9343, perhaps a little bit cleaner regarding the messages/graphics detection when no graphics support was requested (I'd like to keep that, i.e. not completely disabling it). In addition, we should catch illegal parameters to `--graphic=`.

I don't know if you plan to make further changes to the PARI spkg.


---

Comment by leif created at 2010-08-24 11:56:28

From a first glance, the graphics detection in svn-12577 is cleaner, so the changes regarding that will be, too.

It's still not robust, and needs the same fixes as PARI 2.3.5, e.g.
 * add `libstdc++` for `plotfltk`,
 * handle libraries in `.../lib64` directories,
 * make sure FLTK include directory really exists,
 * less annoying/clarified messages.

I haven't yet dealt with graphics support using Qt, which can break the build, too. I.e., the detection should be improved to either give an error earlier or disable Qt in case not all required components are available.

Most of the other changes (`spkg-install`) still apply. In addition, there are superfluous tests of `$?` at the end which I had not removed in 2.3.5.p4 (but added comments to remove them).


---

Comment by leif created at 2010-08-24 12:11:38

Replying to [comment:308 leif]:
> Replying to [comment:303 jdemeyer]:
> >  * New distribution: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar)
> 
> Passed `ptestlong` on Fedora 13 x86_64 (Core2, gcc 4.4.4, native code, `O3`), parallel build with 32 jobs, test with 4 threads.
> 
> Ubuntu 9.04 x86 in progress.

Passed `ptestlong`, too (Pentium 4 Prescott, gcc 4.3.3, native code, `O3`), parallel build with 6 jobs, test with 2 threads.


---

Comment by jdemeyer created at 2010-08-24 19:26:11

Replying to [comment:313 leif]:
> If you have little patience, I'll backport the changes from #9722 to #9343, perhaps a little bit cleaner regarding the messages/graphics detection when no graphics support was requested (I'd like to keep that, i.e. not completely disabling it). In addition, we should catch illegal parameters to `--graphic=`.
> 
> I don't know if you plan to make further changes to the PARI spkg.
No, I don't.  As far as I can tell, #9722 is the only remaining issue.

If you would like to port #9722 to #9343, go ahead and do it.  Otherwise, I can also do it (for me it's the same).


---

Comment by leif created at 2010-08-24 19:56:46

Replying to [comment:316 jdemeyer]:
> Replying to [comment:313 leif]:
> > If you have little patience, I'll backport the changes from #9722 to #9343, perhaps a little bit cleaner regarding the messages/graphics detection when no graphics support was requested (I'd like to keep that, i.e. not completely disabling it). In addition, we should catch illegal parameters to `--graphic=`.
> > 
> > I don't know if you plan to make further changes to the PARI spkg.
> No, I don't.  As far as I can tell, #9722 is the only remaining issue.
> 
> If you would like to port #9722 to #9343, go ahead and do it.

Ok, I'll create a 2.4.3.svn-12577.p5, but not today, perhaps tomorrow.

Did anybody test the latest on Cygwin?


---

Comment by mpatel created at 2010-08-24 21:38:28

Replying to [comment:314 leif]:
> From a first glance, the graphics detection in svn-12577 is cleaner, so the changes regarding that will be, too. 

> It's still not robust, and needs the same fixes as PARI 2.3.5, e.g.

> [...]

Would upstream be receptive to Leif's changes?


---

Comment by leif created at 2010-08-24 21:46:26

Replying to [comment:318 mpatel]:
> Replying to [comment:314 leif]:
> > From a first glance, the graphics detection in svn-12577 is cleaner, so the changes regarding that will be, too. 
> 
> > It's still not robust, and needs the same fixes as PARI 2.3.5, e.g.
> 
> > [...]
> 
> Would upstream be receptive to Leif's changes?

I'd say we should report the changes when we've included them in our svn snapshot.


---

Comment by leif created at 2010-08-26 09:46:32

4.6.prealpha3 (with `PARI_EXTRA_OPTS` _not_ set) also passed `ptestlong` on 32-bit Fedora 13.

On 64-bit Ubuntu 10.04 LTS the build failed in the first place (MPIR and Tachyon); simply rerunning `make` the build succeeded, and all long tests passed.

Perhaps another missing dependency that only rarely comes into play in parallel builds. (This never happened before, and 4.5.3.alpha2 built fine with the same settings). I'll have to inspect that further.

I though get three new Sphinx warnings:

```
docstring of sage.libs.pari.gen:136: (WARNING/2) Literal block expected; none found.
docstring of sage.libs.pari.gen.gen.nfbasis:8: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
docstring of sage.libs.pari.gen.gen.nfinit:19: (WARNING/2) Literal block expected; none found.
build succeeded, 3 warnings.
```



---

Comment by jdemeyer created at 2010-08-26 09:56:47

Replying to [comment:320 leif]:
> I though get three new Sphinx warnings:
> {{{
> docstring of sage.libs.pari.gen:136: (WARNING/2) Literal block expected; none found.
> docstring of sage.libs.pari.gen.gen.nfbasis:8: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
> docstring of sage.libs.pari.gen.gen.nfinit:19: (WARNING/2) Literal block expected; none found.
> build succeeded, 3 warnings.
> }}}
Those are probably my fault.  Can you tell me *how* you get those warnings, i.e. what is the command that I should type to see those warnings?


---

Comment by cremona created at 2010-08-26 11:24:33

Replying to [comment:321 jdemeyer]:
> Replying to [comment:320 leif]:
> > I though get three new Sphinx warnings:
> > {{{
> > docstring of sage.libs.pari.gen:136: (WARNING/2) Literal block expected; none found.
> > docstring of sage.libs.pari.gen.gen.nfbasis:8: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
> > docstring of sage.libs.pari.gen.gen.nfinit:19: (WARNING/2) Literal block expected; none found.
> > build succeeded, 3 warnings.
> > }}}
> Those are probably my fault.  Can you tell me *how* you get those warnings, i.e. what is the command that I should type to see those warnings?

Try sage -docbuild reference html.  Or look in the build log?  I think that "make" does not build the docs (I may be wrong on that) but "make testlong" does, so it might be in the test log.  Anyway, if you touch the offending files and do docbuild reference html it will presumable process them again.


---

Comment by leif created at 2010-08-26 12:33:22

Replying to [comment:322 cremona]:
> Replying to [comment:321 jdemeyer]:
> > Can you tell me *how* you get those warnings, i.e. what is the command that I should type to see those warnings?
> 
> Try sage -docbuild reference html.  Or look in the build log?  I think that "make" does not build the docs (I may be wrong on that) but "make testlong" does, so it might be in the test log.  Anyway, if you touch the offending files and do docbuild reference html it will presumable process them again.

Yes, they usually drown in the flood of Sphinx messages. (And even worse, Sphinx *errors*, too.)

I normally do e.g. `grep -i warn dochtml.log`; grepping for "error" gives also lines with _filenames_ containing it... ;-)

In case you've deleted the log, you have to touch the sources before doing `make doc`, e.g. by `./sage -ba-force`, but that would cause a rebuild of _all_ Cython files, and Sphinx would rebuild the whole reference manual from scratch. So better just touch the files mentioned in the warning messages, and do `./sage -b`, then `make doc`, and carefully watch what rushes down the screen... ;-)


---

Comment by leif created at 2010-08-26 13:57:22

Replying to [comment:320 leif]:
> On 64-bit Ubuntu 10.04 LTS the build failed in the first place (MPIR and Tachyon); simply rerunning `make` the build succeeded, and all long tests passed.
> 
> Perhaps another missing dependency that only rarely comes into play in parallel builds. (This never happened before, and 4.5.3.alpha2 built fine with the same settings). I'll have to inspect that further.

Well, installing Tachyon actually did _not_ fail; I hadn't looked at the whole log.

It first tries a 32-bit build (prepending `-m32` to `CFLAGS`), which indeed fails with a `make` error. But this is catched by some Tachyon script I think, followed by an attempt to do a 64-bit build, which then succeeds. Quite odd, though the whole process of installing the Tachyon spkg takes less than four seconds for me (on that machine)...

The MPIR failure seems to be due to a race condition:

```
...
make[4]: Entering directory `/home/leif/Sage/sage-4.6.prealpha3/spkg/build/mpir-1.2.2.p1/src'
make[4]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Entering directory `/home/leif/Sage/sage-4.6.prealpha3/spkg/build/mpir-1.2.2.p1/src'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
test -z "/home/leif/Sage/sage-4.6.prealpha3/local/lib" || mkdir -p -- "/home/leif/Sage/sage-4.6.prealpha3/local/lib"
test -z "/home/leif/Sage/sage-4.6.prealpha3/local/include" || mkdir -p -- "/home/leif/Sage/sage-4.6.prealpha3/local/include"
test -z "/home/leif/Sage/sage-4.6.prealpha3/local/include" || mkdir -p -- "/home/leif/Sage/sage-4.6.prealpha3/local/include"
 /bin/bash ./libtool --mode=install /usr/bin/install -c  'libmpir.la' '/home/leif/Sage/sage-4.6.prealpha3/local/lib/libmpir.la'
 /usr/bin/install -c -m 644 'mpirxx.h' '/home/leif/Sage/sage-4.6.prealpha3/local/include/mpirxx.h'
 /usr/bin/install -c -m 644 'mpir.h' '/home/leif/Sage/sage-4.6.prealpha3/local/include/mpir.h'
make -j32  install-data-hook
make[6]: Entering directory `/home/leif/Sage/sage-4.6.prealpha3/spkg/build/mpir-1.2.2.p1/src'
make[6]: warning: -jN forced in submake: disabling jobserver mode.
(cd /home/leif/Sage/sage-4.6.prealpha3/local/include  && rm -f gmp.h   && cp mpir.h   gmp.h)
cp: cannot stat `mpir.h': No such file or directory
make[6]: *** [install-data-hook] Error 1
make[6]: Leaving directory `/home/leif/Sage/sage-4.6.prealpha3/spkg/build/mpir-1.2.2.p1/src'
make[5]: *** [install-data-am] Error 2
make[5]: *** Waiting for unfinished jobs....
...
```

I haven't looked at MPIR's Makefile(s); perhaps some dependency is missing there.


---

Comment by leif created at 2010-08-26 18:51:20

Replying to [comment:324 leif]:
> Well, installing Tachyon actually did _not_ fail; I hadn't looked at the whole log.
> 
> It first tries a 32-bit build (prepending `-m32` to `CFLAGS`), which indeed fails with a `make` error. But this is catched by some Tachyon script I think, followed by an attempt to do a 64-bit build, which then succeeds. Quite odd, though the whole process of installing the Tachyon spkg takes less than four seconds for me (on that machine)...

Just for the record: This is actually a completely weird *Sage "feature"* (on Linux), i.e. `spkg-install` does this. I think I'll open a ticket for that, since Sage's beta(!) version of Tachyon is also out of date since at least 19 month and the spkg really needs work...

Sorry for this rather off-topic comment.


---

Comment by drkirkby created at 2010-08-26 20:16:22

Replying to [comment:325 leif]:
> Replying to [comment:324 leif]:
> > Well, installing Tachyon actually did _not_ fail; I hadn't looked at the whole log.
> > 
> > It first tries a 32-bit build (prepending `-m32` to `CFLAGS`), which indeed fails with a `make` error. But this is catched by some Tachyon script I think, followed by an attempt to do a 64-bit build, which then succeeds. Quite odd, though the whole process of installing the Tachyon spkg takes less than four seconds for me (on that machine)...
> 
> Just for the record: This is actually a completely weird *Sage "feature"* (on Linux), i.e. `spkg-install` does this. I think I'll open a ticket for that, since Sage's beta(!) version of Tachyon is also out of date since at least 19 month and the spkg really needs work...
> 
> Sorry for this rather off-topic comment.

Leif, 

you should open a ticket for this Tachyon problem. Put what info you have and _cc_ me. I'd like to know of anything that adds `-m32` as that sort of thing could screw up on any system, but particularly might screw up on systems were we add `-m64` as we do on 64-bit Solaris builds. As you say, it's well off topic for this ticket, which is already very very long. 

Dave


---

Comment by leif created at 2010-08-27 14:06:16

Should we open a new ticket for issues with MPIR 2.1.1 (#8664) and ECM 6.3 (#5847)?

(Both currently need review, work for me with 4.5.3.alpha2, but not fully with 4.6.prealpha3 [segfault in `sage/schemes/elliptic_curves/ell_point.py`].)


---

Comment by jdemeyer created at 2010-08-27 15:37:31

Replying to [comment:327 leif]:
> Should we open a new ticket for issues with MPIR 2.1.1 (#8664) and ECM 6.3 (#5847)?
> 
> (Both currently need review, work for me with 4.5.3.alpha2, but not fully with 4.6.prealpha3 [segfault in `sage/schemes/elliptic_curves/ell_point.py`].)

Any idea which patch from 4.6.prealpha3 could cause this?  I don't think MPIR or ECM depends on PARI/GP.


---

Comment by leif created at 2010-08-27 16:17:21

Replying to [comment:328 jdemeyer]:
> Replying to [comment:327 leif]:
> > Should we open a new ticket for issues with MPIR 2.1.1 (#8664) and ECM 6.3 (#5847)?
> > 
> > (Both currently need review, work for me with 4.5.3.alpha2, but not fully with 4.6.prealpha3 [segfault in `sage/schemes/elliptic_curves/ell_point.py`].)
> 
> Any idea which patch from 4.6.prealpha3 could cause this? 

Nope. I'm not competent to track this down. But since the file containing the failing example also has a 9343-patched doctest (different _result_ only), the code obviously (indirectly) uses PARI.

> I don't think MPIR or ECM depends on PARI/GP.

No, but the code depends on them.

I guess John C. will know. I just wonder _where_ we should address such issues; #8664 (with #5847 mandatory) is likely to go into the 4.6 series. (Though perhaps not 4.6.0, I'm not the release manager.)


---

Comment by leif created at 2010-08-27 16:28:18

P.S.: Perhaps "just" some rare incompatibility of PARI to the new GMP/MPIR.


---

Comment by cremona created at 2010-08-27 16:34:36

Replying to [comment:329 leif]:
> Replying to [comment:328 jdemeyer]:
> > Replying to [comment:327 leif]:
> > > Should we open a new ticket for issues with MPIR 2.1.1 (#8664) and ECM 6.3 (#5847)?
> > > 
> > > (Both currently need review, work for me with 4.5.3.alpha2, but not fully with 4.6.prealpha3 [segfault in `sage/schemes/elliptic_curves/ell_point.py`].)
> > 
> > Any idea which patch from 4.6.prealpha3 could cause this? 
> 
> Nope. I'm not competent to track this down. But since the file containing the failing example also has a 9343-patched doctest (different _result_ only), the code obviously (indirectly) uses PARI.
> 
> > I don't think MPIR or ECM depends on PARI/GP.
> 
> No, but the code depends on them.
> 
> I guess John C. will know. I just wonder _where_ we should address such issues; #8664 (with #5847 mandatory) is likely to go into the 4.6 series. (Though perhaps not 4.6.0, I'm not the release manager.)

What exactly might I know?


---

Comment by leif created at 2010-08-27 16:46:07

Replying to [comment:330 leif]:
> P.S.: Perhaps "just" some rare incompatibility of PARI to the new GMP/MPIR.

At least PARI 2.4.3.svn-12577.p4 passes its test suite with MPIR 2.1.1.


---

Comment by leif created at 2010-08-27 16:56:46

Replying to [comment:331 cremona]:
> What exactly might I know?

Sorry, John, I have not even posted the failing doctest, because I'm not sure if we should discuss it on _this_ already large ticket... (and also hesitated to open a ticket "not-yet-positively-reviewed fails on/with not-yet-released 4.6.prealpha3")

But you're one of the authors of `sage/schemes/elliptic_curves/ell_point.py`.


---

Comment by leif created at 2010-08-27 19:39:37

Replying to [comment:333 leif]:
> Replying to [comment:331 cremona]:
> > What exactly might I know?
> 
> Sorry, John, I have not even posted the failing doctest, because I'm not sure if we should discuss it on _this_ already large ticket...

I think my guess (that you would know the code) was right. :-)

It's exactly the two *long* doctests you added at #8319 (as part of a regression doctest) that individually both segfault with MPIR 2.1.1 and ECM 6.3, in `EllipticCurvePoint_number_field.height()`. Tagging these two doctests `# not tested`, `ptestlong` passes all tests on 64-bit Ubuntu 10.04; still waiting for the results on another, 32-bit Fedora 13 machine.


---

Comment by leif created at 2010-08-27 19:50:55

Replying to [comment:334 leif]:
> It's exactly the two *long* doctests you added at #8319 (as part of a regression doctest) that individually both segfault with MPIR 2.1.1 and ECM 6.3 [...]

... and of course *only* in combination with the *new* PARI, i.e. all tests pass with 4.5.3.alpha2 and MPIR 2.1.1 and ECM 6.3.


---

Comment by cremona created at 2010-08-27 20:30:31

Replying to [comment:335 leif]:
> Replying to [comment:334 leif]:
> > It's exactly the two *long* doctests you added at #8319 (as part of a regression doctest) that individually both segfault with MPIR 2.1.1 and ECM 6.3 [...]
> 
> ... and of course *only* in combination with the *new* PARI, i.e. all tests pass with 4.5.3.alpha2 and MPIR 2.1.1 and ECM 6.3.
>  

OK, here's one way of testing this (perhaps).  I made an input file for gp which computes that same example:  http://www.warwick.ac.uk/staff/J.E.Cremona/pari-test.gp

To test this save the file and run it using `sage -gp pari-test.gp`.  If nothing goes wrong it should output some stuff ending with 

```
%11 = 2.386623822 E-29
```



---

Comment by leif created at 2010-08-27 22:52:27

Replying to [comment:336 cremona]:
> To test this save the file and run it using `sage -gp pari-test.gp`.  If nothing goes wrong it should output some stuff ending with 

```
%11 = 2.386623822 E-29
```



```
leif@quadriga:~/Sage/sage-4.6.prealpha3-with-mpir-2.1.1$ ./sage -gp
                      GP/PARI CALCULATOR Version 2.4.3 (development svn-12577)
                    amd64 running linux (x86-64/GMP-5.0.1 kernel) 64-bit version
                     compiled: Aug 27 2010, gcc-4.4.3 (Ubuntu 4.4.3-4ubuntu5) 
                           (readline v6.0 enabled, extended help enabled)

                               Copyright (C) 2000-2008 The PARI Group

PARI/GP is free software, covered by the GNU General Public License, and comes WITHOUT ANY WARRANTY 
WHATSOEVER.

Type ? for help, \q to quit.
Type ?12 for how to get moral (and possibly technical) support.

parisize = 8000000, primelimit = 500509
? read("pari-test-cremona.gp")
%1 = -8.968227546699448805 E-38
? quit
Goodbye!
```

I'm not that sure I made it right, but except for the number following "%", the output looks ok to me.

The segfaults when doctesting happen in `libgmp.so`, `mpn_submul_1()`, which is (indirectly) called by `__gmpn_divexact()` (gdb stack), but the origin/cause seems to be `sage/libs/pari/gen.pyx`, `gen.__setitem__()`, or its caller `EllipticCurvePoint_field.__getitem__()`... I don't recall when I last used debuggers... ;-)

The last output from running the doctest example (copied to a `.sage` file, activating `pdb` right before `Q.height()`) in gdb is:

```
> /home/leif/Sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py(657)pari_curve()->[0, 0, 0...854 E-19]
-> return self._pari_curve[L[-1]]
(Pdb) 
--Call--
> /home/leif/Sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_point.py(334)__getitem__()
-> def __getitem__(self, n):
(Pdb) 
> /home/leif/Sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_point.py(345)__getitem__()
-> return self._coords[n]
(Pdb) 
--Return--
> /home/leif/Sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_point.py(345)__getitem__()->21043516...115795849
-> return self._coords[n]
(Pdb) 
--Call--
> /home/leif/Sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_point.py(334)__getitem__()
-> def __getitem__(self, n):
(Pdb) 
> /home/leif/Sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_point.py(345)__getitem__()
-> return self._coords[n]
(Pdb) 
--Return--
> /home/leif/Sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_point.py(345)__getitem__()->30508178...767198757
-> return self._coords[n]
(Pdb) 

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff29c08fd in mpn_submul_1 ()
   from /home/leif/Sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/libgmp.so.8
(gdb) c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
0x00007fffeca17fee in __pyx_pf_4sage_4libs_4pari_3gen_3gen___setitem__ (
    __pyx_v_self=<value optimized out>, __pyx_v_n=<value optimized out>, 
    __pyx_v_y=<value optimized out>) at sage/libs/pari/gen.c:7018
7018	}
(gdb) 
```



---

Comment by mpatel created at 2010-08-27 23:12:37

Replying to [comment:329 leif]:
> I guess John C. will know. I just wonder _where_ we should address such issues; #8664 (with #5847 mandatory) is likely to go into the 4.6 series. (Though perhaps not 4.6.0, I'm not the release manager.)

Although #8664 and #5847 are not prerequisites for the PARI upgrade --- please correct me if I'm wrong --- I think is OK to add comments about "NewPARI."  Just be sure to prefix the comments with, e.g.,

 *This is about #9343's PARI upgrade.  See [NewPARI](http://wiki.sagemath.org/NewPARI) for more information and links.*


---

Comment by leif created at 2010-08-27 23:20:22

Replying to [comment:337 leif]:
>

```
...
%1 = -8.968227546699448805 E-38
```


I get the same result with "vanilla" 4.6.prealpha3 (MPIR 1.2.2.p1/GMP-4.2.1 kernel).

----

The 32-bit Fedora machine segfaults at `Q.height()`, too; in addition, a segfault occurs in `ell_rational_field.py`. (Again 4.6.prealpha3 *with* MPIR 2.1.1 and ECM 6.3.)


---

Comment by leif created at 2010-08-27 23:50:46


```
? read("../pari-test-cremona.gp")
%1 = 2.386623822 E-29
```

Exactly John's result on the _32-bit_ machine with 4.6.prealpha3 and MPIR 2.1.1/GMP-5.0.1 kernel.


---

Comment by cremona created at 2010-08-28 08:54:48

Replying to [comment:340 leif]:
> {{{
> ? read("../pari-test-cremona.gp")
> %1 = 2.386623822 E-29
> }}}
> Exactly John's result on the _32-bit_ machine with 4.6.prealpha3 and MPIR 2.1.1/GMP-5.0.1 kernel.
Those are the expected results on 32 and 64 bit machines.

Sorry, I'm not able to look at this at all today (Saturday).


---

Comment by leif created at 2010-08-28 18:56:55

Replying to [comment:341 cremona]:
> Sorry, I'm not able to look at this at all today (Saturday).

It's an upstream problem (PARI/GP 2.4.3.svn-12577 with MPIR 2.1.1). :)

More to come...


---

Comment by cremona created at 2010-08-28 20:07:58

Replying to [comment:342 leif]:
> Replying to [comment:341 cremona]:
> > Sorry, I'm not able to look at this at all today (Saturday).
> 
> It's an upstream problem (PARI/GP 2.4.3.svn-12577 with MPIR 2.1.1). :)

I thought it might be, which is why I provided a test gp script which Pari developers would like more than some Sage code.

> 
> More to come...


---

Comment by leif created at 2010-08-28 20:35:33

Replying to [comment:343 cremona]:
> Replying to [comment:342 leif]:
> > It's an upstream problem (PARI/GP 2.4.3.svn-12577 with MPIR 2.1.1). :)
> 
> I thought it might be, which is why I provided a test gp script which Pari developers would like more than some Sage code.

I was actually thinking (fearing) it was a Sage/Cython bug, but can meanwhile reproduce the segfault with a GP script; going to sort out if it's PARI's or MPIR's fault.


---

Comment by jdemeyer created at 2010-08-29 09:51:33

Replying to [comment:342 leif]:
> Replying to [comment:341 cremona]:
> > Sorry, I'm not able to look at this at all today (Saturday).
> 
> It's an upstream problem (PARI/GP 2.4.3.svn-12577 with MPIR 2.1.1). :)

I'm *not* able to reproduce this problem.  I'm using vanilla MPIR 2.1.1, vanilla PARI svn-12577 and using PARI's --with-gmp feature and setting LD_LIBRARY_PATH to use my newly compiled MPIR.  This is using gcc (GCC) 4.6.0 20100705 (experimental) on a Gentoo Linux x86_64 system.  I run the gp script provided by John and it just works.


---

Comment by leif created at 2010-08-29 13:04:15

Replying to [comment:345 jdemeyer]:
> Replying to [comment:342 leif]:
> > It's an upstream problem (PARI/GP 2.4.3.svn-12577 with MPIR 2.1.1). :)
> 
> I'm *not* able to reproduce this problem.  I'm using vanilla MPIR 2.1.1, vanilla PARI svn-12577 [...]

> I run the gp script provided by John and it just works.

Well, I wrote _"*a* GP script"_; John's doesn't resemble what Sage actually does.

Try `ellorder(E,Q)`...

With true [GMP](http://gmplib.org/) 5.0.1 (and ECM 6.3), Sage 4.6.prealpha3 passes all tests for me; I'll try later on further machines. 

I've put a remark on the [NewPARI Wiki page](http://wiki.sagemath.org/NewPARI), and will revert #8664 to "needs work".


---

Comment by cremona created at 2010-08-29 13:19:31

Replying to [comment:346 leif]:
> Replying to [comment:345 jdemeyer]:
> > Replying to [comment:342 leif]:
> > > It's an upstream problem (PARI/GP 2.4.3.svn-12577 with MPIR 2.1.1). :)
> > 
> > I'm *not* able to reproduce this problem.  I'm using vanilla MPIR 2.1.1, vanilla PARI svn-12577 [...]
> 
> > I run the gp script provided by John and it just works.
> 
> Well, I wrote _"*a* GP script"_; John's doesn't resemble what Sage actually does.

My script was intended to make the pari library do exactly what is does in that Sage example, i.e. it calls ellheight with the same point and curve.

> 
> Try `ellorder(E,Q)`...

Meaning?  That returns 0, which is correct (it means infinite order).

> 
> With true [GMP](http://gmplib.org/) 5.0.1 (and ECM 6.3), Sage 4.6.prealpha3 passes all tests for me; I'll try later on further machines. 
> 
> I've put a remark on the [NewPARI Wiki page](http://wiki.sagemath.org/NewPARI), and will revert #8664 to "needs work".


---

Comment by jdemeyer created at 2010-08-29 13:40:17

Replying to [comment:346 leif]:
> Try `ellorder(E,Q)`...
Allright, bug confirmed!


---

Comment by jdemeyer created at 2010-08-29 13:53:36

Replying to [comment:348 jdemeyer]:
> Replying to [comment:346 leif]:
> > Try `ellorder(E,Q)`...
> Allright, bug confirmed!

Interestingly, the _statically compiled_ `gp-sta` version of gp works.


---

Comment by drkirkby created at 2010-08-29 13:56:21

If I understand correctly, this is a probably a Pari bug, which the Pari developers will hopefully fix. (It might not be of course - I'm not saying it is a Pari bug). 

I would suggest that it would suggest it might be wiser to just add the bug fix to the Sage package, and not use the very latest svn checkout. That should reduce the chance of you getting any new bugs that might have been created. Since these are only svn snapshots, they can't be expected to be as stable as a well tested release. 

Of course, it would be wise to ask the Pari developers too, but my general feeling is that it would be wise to make major changes now. 

Dave


---

Comment by leif created at 2010-08-29 14:00:17

Replying to [comment:347 cremona]:
> Replying to [comment:346 leif]:
> > Well, I wrote _"*a* GP script"_; John's doesn't resemble what Sage actually does.
> 
> My script was intended to make the pari library do exactly what is does in that Sage example, i.e. it calls ellheight with the same point and curve.

This wasn't meant as an offense; perhaps I should have written _"... does not *fully* resemble what Sage does"_.

> > Try `ellorder(E,Q)`...
> 
> Meaning?  That returns 0, which is correct (it means infinite order).

Yes, and *that*'s what crashes with MPIR 2.1.1.

Sage's `EllipticCurvePoint_number_field.height()` first calls `self.has_finite_order()`, which in turn calls `self.order()`, which uses PARI's `orderell()` (deprecated, `ellorder()` in the GP interpreter).


---

Comment by jdemeyer created at 2010-08-29 14:02:45

In order not to flood this ticket any further, I opened a ticket for this new PARI + new MPIR issue: #9837


---

Comment by mpatel created at 2010-08-30 01:33:33

How close are the essential PARI upgrade tickets #9343, #9591, and #9592 (any others?) to being positively reviewed?


---

Comment by drkirkby created at 2010-08-30 08:57:58

Replying to [comment:353 mpatel]:
> How close are the essential PARI upgrade tickets #9343, #9591, and #9592 (any others?) to being positively reviewed?
If the Pari upgrade is stalled over some issues, it might be worth considering putting the upgrade off for the a release. That would not slow the Pari upgrade, if the tickets merged had an almost zero probability of conflicting with the upgrade. 

* #9766 is for example a ticket I reviewed, which is an update to an SPKG.txt file only. 
That's an extreme example, but there must be other tickets which have a very small probability of affecting the Pari upgrade. 

That said, I'm glad the 4.5.3.alpha2 has become available, and people are having time to test that without 4.5.3 being rushed out.


---

Comment by cremona created at 2010-08-30 11:49:52

Replying to [comment:353 mpatel]:
> How close are the essential PARI upgrade tickets #9343, #9591, and #9592 (any others?) to being positively reviewed?

I lost track of who is doing what, so I don't know what (or who) we are waiting for.  Or who will be the one to actually give it a positive review.  Presumably what we want is that as soon as 4.5.3 is released the current prealpha of 4.6 is released as an alpha?  What is to stop that happening now?


---

Comment by jdemeyer created at 2010-08-30 14:50:48

As far as I know, the only remaining issue is to port #9722 to #9343.  I believe leif is working on that (If leif is unable to do it, I'm also willing to take care of that).

The large number of doctests without errors for sage-4.6.prealpha3 seem to indicate that the patches are fine.

I also would very much like somebody to have a look at #9400, because it also touches a lot of PARI code (the patch for #9400 has been included in 4.6.prealpha2 and 4.6.prealpha3).


---

Comment by leif created at 2010-08-30 18:30:54

Replying to [comment:355 cremona]:
> I lost track of who is doing what, so I don't know what (or who) we are waiting for.  Or who will be the one to actually give it a positive review.

Me, too. Also, it looks as if there was a lack of (other, "independent") reviewers, or at least people testing this. I still don't know if this has been tested on Cygwin, and, if there were any issues, if we should address them _here_. (Mike has provided a "follow-up" Lcalc to make it work on Cygwin; I'm not sure if that's the only required change w.r.t. prealpha3.) 
 
> Presumably what we want is that as soon as 4.5.3 is released the current prealpha of 4.6 is released as an alpha?

I actually expected a 4.5.3 release candidate rather than an alpha2, and 4.5.3 released earlier. 4.6.prealpha3 is still based on 4.5.3.alpha1, but as far as I know the only changes in 4.5.3.alpha2 are fixing numerical noise in doctests, and #9722, which I am porting to the new PARI; Mitesh will know better.

> What is to stop that happening now?

Regarding this ticket, the only things I'm aware of are:
 * preparing a PARI 2.4.3.svn-12577.p5 spkg, with the fixes from #9722, and in addition disabling the use of GMP internals by PARI by default (with an _option_ to make PARI use them)
 * fixing Sphinx warnings
 * adding more documentation (strings) and doctests to (at least) `sage/libs/pari/gen.pyx` (cf. [this comment](http://trac.sagemath.org/sage_trac/ticket/9343#comment:250) and the [corresponding attachment](http://trac.sagemath.org/sage_trac/attachment/ticket/9343/pari-gen.pyx-coverage.txt)).

I don't know if further (new?) PARI functions should be wrapped; I only came across the deprecated `orderell()`.

IMHO other things (e.g. Lcalc spkg improvements; I've commented on Mike's follow-up #9775) should be addressed during the normal 4.6 release cycle.

I guess an official 4.6.alpha would be tested by far more people, on a broader variety of systems. Same for 4.5.3 (final). If any problems arise with the latter, they should be fixed during the preparation of 4.6 alphas, not in our inofficial prealphas.

Replying to [comment:356 jdemeyer]:
> [...] port #9722 to #9343. I believe leif is working on that.

Yes. Unfortunately the MPIR 2.1.1 issue took too much of my time and resources; I now consider it (more or less) "resolved", and continue the work on the PARI 2.4.3.svn-12577.p5 spkg.
    
> The large number of doctests without errors for sage-4.6.prealpha3 seem to indicate that the patches are fine.

Hopefully. It might also indicate a lack of (appropriate) doctests... ;-)

(E.g., despite the obvious bug in MPIR 2.1.1, Sage 4.5.3.alpha2 and 4.6.prealpha3 - with PARI _not_ using GMP internals - both passed all long tests on two systems with it. There have been similar cases in the past.)


---

Comment by leif created at 2010-08-30 18:36:56

P.S.: In prealpha3, the "coverage" slightly rised (by 1 percent):

```
SCORE devel/sage/sage/libs/pari/gen.pyx: 56% (220 of 389)
```



---

Comment by jdemeyer created at 2010-08-30 21:28:43

Replying to [comment:357 leif]:
>  * preparing a PARI 2.4.3.svn-12577.p5 spkg, with the fixes from #9722, and in addition disabling the use of GMP internals by PARI by default (with an _option_ to make PARI use them)

I'm assuming you refer to the "GMP internals" mentioned in #9837?  Note that these are actually *documented* GMP internals, so it's not as bad as it sounds.  So I would prefer not to touch that code and leave PARI using documented GMP/MPIR internals as it is.

Also, on the who-is-doing-what part: I am not doing anything with this for the moment (I do plan to release a prealpha4 when leif's done with p5).


---

Comment by mpatel created at 2010-08-30 22:35:11

I'll release a 4.5.3.rc0 later today (or possibly, tomorrow) which, if there are no new blockers, will become Sage 4.5.3 a week later.  Soon after that, I'll start merging positively-reviewed (PR) tickets (listed at reports {11} and {32}) into 4.6.alpha0.

If the essential PARI upgrade tickets are 

 * PR at that time, I'll merge them (and perhaps other PR PARI-related tickets) into 4.6.alpha0 and leave the other PR tickets for 4.6.alpha1 (or later).

 * Not PR at that time, I'll merge other PR tickets into 4.6.alpha0 and leave the PARI tickets for 4.6.alpha1 (or later).

Either way, I don't plan to release Sage 4.6 (== 4.6.0) until it's sufficiently stable.


---

Comment by jdemeyer created at 2010-09-05 13:22:07

The PARI have been starting to fix some bugs that we reported (as I said, they usually do it, albeit slowly).  Two patches which are in pari-2.4.3.svn-12577.p4.spkg are now fixed upstream in svn 12588:
 * http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1089
 * http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1091

Personally, I think we should upgrade our spkg from svn 12577 to 12588. This might be a controversial proposal, so what do you think of it?

Leif, how is the progress on p5?


---

Comment by leif created at 2010-09-05 16:35:22

Replying to [comment:361 jdemeyer]:
> Personally, I think we should upgrade our spkg from svn 12577 to 12588. This might be a controversial proposal, so what do you think of it?

No idea what else they changed. Without further knowledge, I'd prefer staying with "our already well-tested" 12577, but don't insist on that. I'll leave the decision to the others.

Btw, as Mitesh mentioned, we need a (formal) positive review to get this into Sage 4.6.


> Leif, how is the progress on p5?

Ongoing... ;-)

I currently have some hardware issues I cannot solve until tomorrow, but will post a p5 either later today or latest by tomorrow evening.


---

Comment by drkirkby created at 2010-09-05 19:27:33

Replying to [comment:361 jdemeyer]:
> The PARI have been starting to fix some bugs that we reported (as I said, they usually do it, albeit slowly).  Two patches which are in pari-2.4.3.svn-12577.p4.spkg are now fixed upstream in svn 12588:
>  * http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1089
>  * http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1091
> 
> Personally, I think we should upgrade our spkg from svn 12577 to 12588. This might be a controversial proposal, so what do you think of it?

I think that would be a bad idea. It's difficult to say for sure without knowing what was changed in all 11 different svn snapshots, but given these are only snapshots with little testing, I think you have a reasonable probability of hitting another bug. 

Not only that, but people have spent a lot of time testing this. Their appetite for testing might diminish. 

Where do you stop? 

Dave


---

Comment by jdemeyer created at 2010-09-06 10:09:19

Replying to [comment:363 drkirkby]:
> I think that would be a bad idea. It's difficult to say for sure without knowing what was changed in all 11 different svn snapshots, but given these are only snapshots with little testing, I think you have a reasonable probability of hitting another bug. 

So the PARI/GP people are fixing bugs that we reported, but we're not going to apply those bugfixes? That also sounds stupid.


---

Comment by leif created at 2010-09-06 10:17:40

Replying to [comment:364 jdemeyer]:
> So the PARI/GP people are fixing bugs that we reported, but we're not going to apply those bugfixes? [...]

_"In a later, stable release..."_ ;-)

I think we should really get into 4.6 what we have by now, or this ticket will never end.


---

Comment by fbissey created at 2010-09-06 10:23:17

Replying to [comment:364 jdemeyer]:
> Replying to [comment:363 drkirkby]:
> > I think that would be a bad idea. It's difficult to say for sure without knowing what was changed in all 11 different svn snapshots, but given these are only snapshots with little testing, I think you have a reasonable probability of hitting another bug. 
> 
> So the PARI/GP people are fixing bugs that we reported, but we're not going to apply those bugfixes? That also sounds stupid.

I think you didn't get Dave's point. He wants the fixes and only the fixes. If we 
take another snapshot we get the fixes and who knows what else.

I second leif this needs merging soon or it will never happen. 
We just have to be ready to pick up the pieces in 4.6.1.


---

Comment by drkirkby created at 2010-09-06 11:53:33

Replying to [comment:366 fbissey]:
> Replying to [comment:364 jdemeyer]:
> > Replying to [comment:363 drkirkby]:
> > > I think that would be a bad idea. It's difficult to say for sure without knowing what was changed in all 11 different svn snapshots, but given these are only snapshots with little testing, I think you have a reasonable probability of hitting another bug. 
> > 
> > So the PARI/GP people are fixing bugs that we reported, but we're not going to apply those bugfixes? That also sounds stupid.
> 
> I think you didn't get Dave's point. He wants the fixes and only the fixes. If we 
> take another snapshot we get the fixes and who knows what else.

That is *exactly* what I meant. 

> I second leif this needs merging soon or it will never happen. 
> We just have to be ready to pick up the pieces in 4.6.1.

Me too.


---

Comment by leif created at 2010-09-06 12:50:00

I've put the diffs of and a link to the [new PARI 2.4.3.svn-12577.p5 spkg](http://spkg-upload.googlecode.com/files/pari-2.4.3.svn-12577.p5.spkg) onto #9860. *Needs review...*


---

Comment by leif created at 2010-09-06 13:41:30

Dave, you changed the status from "positive review" to "needs work" about three weeks ago.

Are there still known issues not yet fixed?

Otherwise we should at least put it back to "needs review".


---

Comment by jdemeyer created at 2010-09-06 13:45:03

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-09-06 14:00:39

I will add some small changes to your spkg:
 * config/Makefile.SH: now fixed upstream.
 * src/tune/tune.c: tuning fixed upstream.

I will update just these two files from upstream and remove our patch for config/Makefile.SH (no other changes, I promise!)


---

Comment by jdemeyer created at 2010-09-06 16:10:28

I have made a few small changes to the pari spkg and put the result at [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p5.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p5.spkg) (I kept the p5 version number).


---

Comment by jdemeyer created at 2010-09-06 16:30:58

I will now make a new 4.6-prealpha4 based on 4.5.3-rc0 with the new spkgs (I will also update genus2reduction, see #9591 and lcalc, see #9845).


---

Comment by jdemeyer created at 2010-09-07 10:00:41

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-09-07 10:00:41

New prealpha4: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha4.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha4.tar)

Tested successfully on `sage.math.washington.edu`, more testing underway.  Also tuning and spkg-check worked:

```
env SAGE_CHECK=yes SAGE_TUNE_pari=yes ./sage -f pari-2.4.3.svn-12577.p5.spkg
```


As far as I know, there are no remaining issues, so I will be bold and set this back to positive review.


---

Comment by leif created at 2010-09-07 10:13:06

The prealpha4 passed `ptestlong` on Ubuntu 10.04 x86_64 (Core2) and Fedora 13 x86 (Pentium 4 Prescott), too. Installing the package with `SAGE_CHECK=yes` also works.

Tuning now doesn't give an error on the former, but still hangs on the latter (see previous posts).

The patch to `tune.c` from svn 12588 is a one-liner btw.


---

Comment by drkirkby created at 2010-09-07 11:04:43

Replying to [comment:374 jdemeyer]:
> New prealpha4: [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha4.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha4.tar)
> 
> Tested successfully on `sage.math.washington.edu`, more testing underway.  Also tuning and spkg-check worked:
> {{{
> env SAGE_CHECK=yes SAGE_TUNE_pari=yes ./sage -f pari-2.4.3.svn-12577.p5.spkg
> }}}
> 
> As far as I know, there are no remaining issues, so I will be bold and set this back to positive review.

Having produced a tar file for people to test, it would have been wise to get some more feedback before setting it to positive review. 

I'm going to build it now on OpenSolaris. Nice thing about that is that's it's very quick. Downloading the tarball is less so!

Dave


---

Comment by leif created at 2010-09-07 11:33:01

Replying to [comment:376 drkirkby]:
> I'm going to build it now on OpenSolaris. Nice thing about that is that's it's very quick.

If so, you could try reinstalling the PARI package with `PARI_EXTRA_OPTS="--graphic=auto"` or e.g. `X11`; best once with X11 development files present, and once in addition without (a functional) `xmkmf`. (I don't know what X11 [development] packages OpenSolaris provides.) :-)

> Downloading the tarball is less so!

Took more than three times longer than usual for me yesterday...


---

Comment by drkirkby created at 2010-09-07 12:18:36

Replying to [comment:377 leif]:
> Replying to [comment:376 drkirkby]:
> > I'm going to build it now on OpenSolaris. Nice thing about that is that's it's very quick.
> 
> If so, you could try reinstalling the PARI package with `PARI_EXTRA_OPTS="--graphic=auto"` or e.g. `X11`; best once with X11 development files present, and once in addition without (a functional) `xmkmf`. (I don't know what X11 [development] packages OpenSolaris provides.) :-)
> 
> > Downloading the tarball is less so!
> 
> Took more than three times longer than usual for me yesterday...


Is the 

`PARI_EXTRA_OPTS="--graphic=auto"` 

just an environment variable I should set? If so, that will be trivial. I'm actually building two copies of Sage at the minute on this machine, so its under a heavy load, but I'll try this later

I see your point elsewhere about Qt. I have some Qt libraries on here, which come as part of Mathematica. Not sure if I should set LD_LIBRARY_PATH to include them. Let me know. 

Dave


---

Comment by leif created at 2010-09-07 12:47:42

Replying to [comment:378 drkirkby]:
> Replying to [comment:377 leif]:
> > Replying to [comment:376 drkirkby]:
> > > I'm going to build it now on OpenSolaris. Nice thing about that is that's it's very quick.
> > 
> > If so, you could try reinstalling the PARI package with `PARI_EXTRA_OPTS="--graphic=auto"` or e.g. `X11`; best once with X11 development files present, and once in addition without (a functional) `xmkmf`. (I don't know what X11 [development] packages OpenSolaris provides.) :-)
> Is the 
> 
> `PARI_EXTRA_OPTS="--graphic=auto"` 
> 
> just an environment variable I should set?

Yes, that's passed (verbatim) to PARI's `Configure` by Sage, so do

```sh
export PARI_EXTRA_OPTS="--graphic=X11"
```

(`--graphic=auto` will pick X11 if it's found, otherwise try FLTK and Qt.)
 
> I'm actually building two copies of Sage at the minute on this machine, so its under a heavy load, but I'll try this later

That would be nice.

> I see your point elsewhere about Qt. I have some Qt libraries on here, which come as part of Mathematica. Not sure if I should set LD_LIBRARY_PATH to include them. Let me know.

I don't think Mathematica ships with Qt _development_ files... (But there should be such OpenSolaris packages. If you choose X11, PARI will just use "plain" X11.)

W.r.t. #9603, my main machine is still headless... :/


---

Comment by leif created at 2010-09-07 13:19:11

Replying to [comment:375 leif]:
> The prealpha4 passed `ptestlong` on Ubuntu 10.04 x86_64 (Core2) and Fedora 13 x86 (Pentium 4 Prescott), too. Installing the package with `SAGE_CHECK=yes` also works.
> 
> Tuning now doesn't give an error on the former, but still hangs on the latter (see previous posts).

It also hangs with `CFLAGS=-O0`, and also if I do

```
.../pari-2.4.3.svn-12577.p5/src$ ./Configure --graphic=none --kernel=gmp --tune
```

(which uses the system's GMP, which is version 4.3.1), regardless of `CFLAGS` settings. (gcc is version 4.4.4.)

It doesn't always hang at _exactly_ the same point (of output), but this might simply be due to unflushed buffers; the point where it "stops" only differs by some lines (different size / threshold for the same function, when attempting to tune `REMIIMUL_LIMIT` if I understand correctly). When I interrupt the tuning from within a Sage build with Control-C, I get cores dumped. Plain PARI seems to catch the signal (properly) and exits with

```
^C  ***   user interrupt.
  ***   Error in the PARI system. End of program.
```

but continues compilation (which of course fails).


---

Comment by leif created at 2010-09-07 15:48:20

On a Pentium 4 (Northwood), PARI self-tuning works, and `make test-all` apparently passes all tests except those few that require extra data files, though the self-test also ends with

```
+++ [BUG] Total bench for gp-sta is 585030
+++ [BUG] Total bench for gp-dyn is 592375

...
```

I'm not sure what that's intended to mean.

This is with gcc 4.2.1 and GMP 4.3.2 though.


---

Comment by jdemeyer created at 2010-09-07 16:39:20

Replying to [comment:381 leif]:
> On a Pentium 4 (Northwood), PARI self-tuning works, and `make test-all` apparently passes all tests except those few that require extra data files, though the self-test also ends with
> {{{
> +++ [BUG] Total bench for gp-sta is 585030
> +++ [BUG] Total bench for gp-dyn is 592375
> 
> ...
> }}}

This means that some self-tests failed.  Normally you can see which tests failed by looking at the last lines of the output of `make test-all`.


---

Comment by leif created at 2010-09-07 16:55:54

Replying to [comment:382 jdemeyer]:
> Replying to [comment:381 leif]:

```
+++ [BUG] Total bench for gp-sta is 585030
+++ [BUG] Total bench for gp-dyn is 592375

...
```

> 
> This means that some self-tests failed.  Normally you can see which tests failed by looking at the last lines of the output of `make test-all`.

Yes, and these are exactly the six (IIRC) tests that need extra data; I verified that by looking at the diffs. I don't know what _"total bench"_ and the numbers express. (It's near to, but *not* the seconds the tests took... ;-) )


---

Comment by leif created at 2010-09-07 17:23:18

Oh, it _might_ be the (CPU) time in ms the test(s) took (sum about 20 minutes), but the _"[BUG]"_ next to it is quite irritating.

Btw, tuning also works on the Pentium 4 *Prescott* with GMP *4.2.4* and gcc *4.3.3*, so perhaps there's a bug in GMP; a bug in gcc (4.4.4) is IMHO rather unlikely.


---

Comment by leif created at 2010-09-07 17:37:09

Replying to [comment:384 leif]:
> Btw, tuning also works on the Pentium 4 *Prescott* with GMP *4.2.4* and gcc *4.3.3*, so perhaps there's a bug in GMP; a bug in gcc (4.4.4) is IMHO rather unlikely.

But there another test fails (in `linear-{sta,dyn`}) which is not due to missing data files; perhaps numerical noise... (Both diffs are identical.)


---

Comment by jdemeyer created at 2010-09-07 20:50:09

Replying to [comment:385 leif]:
> But there another test fails (in `linear-{sta,dyn`}) which is not due to missing data files; perhaps numerical noise... (Both diffs are identical.) 

This shouldn't happen, can you make a new ticket and post the the `linear-sta.dif`?


---

Comment by leif created at 2010-09-07 22:50:17

Final post _here_ (I'll open a new ticket shortly):

Replying to [comment:380 leif]:
> Replying to [comment:375 leif]:
> > The prealpha4 passed `ptestlong` on Ubuntu 10.04 x86_64 (Core2) and Fedora 13 x86 (Pentium 4 Prescott), too. Installing the package with `SAGE_CHECK=yes` also works.
> > 
> > Tuning now doesn't give an error on the former, but still hangs on the latter (see previous posts).
> 
> It also hangs with `CFLAGS=-O0`, and also if I do

```
.../pari-2.4.3.svn-12577.p5/src$ ./Configure --graphic=none --kernel=gmp --tune
```

> (which uses the system's GMP, which is version 4.3.1), regardless of `CFLAGS` settings. (gcc is version 4.4.4.)

It also hangs with GMP 5.0.1 ("plain" PARI, gcc 4.4.4 as before, in tuning `REMIIMUL_LIMIT`).
 
> It doesn't always hang at _exactly_ the same point (of output), but this might simply be due to unflushed buffers; the point where it "stops" only differs by some lines (different size / threshold for the same function, when attempting to tune `REMIIMUL_LIMIT` if I understand correctly).


---

Comment by cremona created at 2010-09-08 21:11:08

prealpha4 worked fine for me on 32-bit and 64-bit linux.

Now that 4.5.3 has been released it would be great of we could get this as the beginning of an actual 4.6.0 series.


---

Comment by leif created at 2010-09-08 21:27:10

Replying to [comment:388 cremona]:
> Now that 4.5.3 has been released it would be great of we could get this as the beginning of an actual 4.6.0 series.

Mitesh Patel wrote on sage-release ("4.6 sketch" thread):
> On 09/07/2010 05:38 PM, Jason Grout wrote:
> > What do you see as the window for merging changes into 4.6?  I'd like to
> > finish some significant changes to fast_callable, but don't think they
> > should be introduced in a point-point release.  4.6 sounds like a good
> > release for the changes.
> Up to three weeks.  I think there will be three alphas for the 4.6
> cycle, since I'll focus on the PARI upgrade (#9343 and related tickets)
> for 4.6.alpha0.  For alpha1 and alpha2, I plan to merge most of the
> other positively reviewed tickets waiting at reports 11 and 32:
> 
> http://trac.sagemath.org/sage_trac/report/11
> http://trac.sagemath.org/sage_trac/report/32
> 
> Of course, how it really goes will depend significantly on build and
> test reports.
> [...]

:)

(For unknown reason I do not see this thread on Google's page.)


---

Attachment

Update commit string for combined extcode patch.


---

Comment by mpatel created at 2010-09-10 06:34:23

I've updated the commit string for the extcode patch and updated [NewPARI](http://wiki.sagemath.org/NewPARI).


---

Comment by mpatel created at 2010-09-10 10:38:49

Resolution: fixed


---

Comment by leif created at 2010-09-24 19:23:35

Replying to [comment:302 jdemeyer]:
> I found out what prevents PARI/GP from compiling on Solaris.  The problem is that `/bin/sh` from Solaris doesn't know about `test -e <filename>`.

It should, since `test -e ...` is POSIX (2004).

Dave, what shell is `/bin/sh` there?


---

Comment by drkirkby created at 2010-09-25 01:39:06

Replying to [comment:392 leif]:
> Replying to [comment:302 jdemeyer]:
> > I found out what prevents PARI/GP from compiling on Solaris.  The problem is that `/bin/sh` from Solaris doesn't know about `test -e <filename>`.
> 
> It should, since `test -e ...` is POSIX (2004).
> 
> Dave, what shell is `/bin/sh` there?

`/bin/sh` is a borne shell, but it is *not* POSIX compatible, since to make it POSIX compatible would break backwards compatibility in Solaris. 

There are however other shells, such as `/usr/xpg4/bin/sh` which are POSIX compatible. Hence there is a need to work around the Solaris shell `/bin/sh`, and do not assume that it is POSIX compatible, since it is not. 

Dave
