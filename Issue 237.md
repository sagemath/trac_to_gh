# Issue 237: create an interface to the "Inverse Symbolic Calculator"

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-01 20:26:05

Assignee: was

CC:  kini slelievre

Write a function that queries this web pge and gives the result:

    http://oldweb.cecm.sfu.ca/projects/ISC/ISCmain.html


---

Comment by nbruin created at 2007-02-07 07:33:28

This interface is running on a heavily ageing SGI server. The software providing the interface is completely unmaintained. When this server dies, the Inverse Symbolic Calculator will be gone.


---

Comment by kcrisman created at 2009-12-30 05:25:31

There is a new version of this, apparently supported by both Maplesoft and NSERC, at [this link](http://glooscap.cs.dal.ca:8087/standard).  So maybe this is doable after all - we already have an interface for Wolfram integrator, for instance.


---

Comment by nbruin created at 2010-01-20 01:04:30

Replying to [comment:4 kcrisman]:
> There is a new version of this, apparently supported by both Maplesoft and NSERC, at [this link](http://glooscap.cs.dal.ca:8087/standard).

I am sure that their names are only there because the work was done on grants funded by them. Jon Borwein is no longer at Dalhousie and I don't think there is much of his group left there either. You'll be interfacing with unmaintained code.


---

Comment by jason created at 2012-04-26 17:07:05

Indeed, the "new version" seems to not be up now.


---

Comment by jason created at 2012-04-26 17:07:40

See also RIES: http://groups.google.com/group/sage-devel/browse_thread/thread/339a2a5fce57814d for another option for this functionality.


---

Comment by kcrisman created at 2013-01-29 20:53:39

Indeed, kini made an spkg for that.  Let's change this summary.


---

Comment by kcrisman created at 2013-01-29 20:54:26

http://boxen.math.washington.edu/home/keshav/files/ries-20120420.spkg is still there as of today.


---

Comment by kini created at 2013-01-29 21:17:00

Latest version appears to be 20130125 so it's still under active development. I'll update the SPKG in a bit.


---

Comment by kini created at 2013-01-30 00:04:56

New SPKG: http://wstein.org/home/keshav/files/ries-20130125.spkg

We should probably have Python bindings for this SPKG, otherwise it's kind of useless for casual users (who would seem to be a major audience for this functionality, since it's not only of interest to researchers in some abstruse area).


---

Comment by kcrisman created at 2013-01-30 01:47:56

> We should probably have Python bindings for this SPKG, otherwise it's kind of useless for casual users (who would seem to be a major audience for this functionality, since it's not only of interest to researchers in some abstruse area).
Agreed.  Is there a model spkg/pyx file that you could point interested people to for how to do this?  I wouldn't want to ask you to do it, unless you were really motivated, but I think this could be a neat project for a new developer interested in such things (inspired by the Borweins, for instance).


---

Comment by kini created at 2013-01-30 02:54:34

I don't think it would be such a big deal. By "bindings" I don't mean actual bindings - this kind of program isn't going to be called en masse or require a whole lot of speed in the communication pipeline like, say GAP does, so writing a `libries` (to actually link against the RIES code) is surely unnecessary.

We can just write an interface in `$SAGE_ROOT/devel/sage/sage/interfaces/` which takes a Sage number of some kind, converts it into a string, and then calls `ries` on the command line with it. The only nontrivial part would be to convert the result back into a form that is meaningful in Sage, (as opposed to just printing it as it appears when calling `ries` on the command line). For example you might want to convert the output of `ries` into a list of Sage symbolic expressions, or something like that. That would involve string parsing to decipher the output notation `ries` uses.

I could probably give it a try if I get some time. Of course, other developers are free to do so as well :)


---

Comment by ncohen created at 2013-04-27 08:01:07

Soooooo is anybody still working on interfacing Sage wth ISC (http://isc.carma.newcastle.edu.au/standard) at the moment ? And does it make sense to you ? If so I'm willing to give it a try `:-)`

Nathann


---

Comment by jason created at 2013-04-27 08:17:33

I was trying to find this website the other day in class to show my students (and check one of their conjectures).  I wasn't able to locate it via google---I should have known to try searching here!

Yes, it would be great if Sage interfaced with it!  I would have used it last week in class!


---

Comment by ncohen created at 2013-04-27 11:17:58

Ok, then let's work hard so that you could have used it last week `:-P`

Well, I wrote a few lines of code and it "works", but there are some problems for which I would like everybody's advice.


```
sage: ask_ISC(3.14)                         
Asking ISC what it knows about 3.14000000000000
No result found in ISC
```


That's the first problem : 3.14, for Sage, is equal to 3.1400000000. Which, for ISC, is totally different.

There's a way out if we only feed the function with a string instead, but it's not a good way out for it should ultimately be a method of Sage constants...

Second problem, which is just technical : where should this method appear ? Where in the code ? Or should it appear nowhere, and just be available as a function in a module ?

Then, the output.


```
sage: ask_ISC("3.14")
Asking ISC what it knows about 3.14
3140000117869847 sin(Pi*4/35)*sin(Pi*19/54)
3140000181376111 Lehmer^sr(Pi)/2^(1/3)
3140000375403483 sum(1/(5^n+(31/2*n^2-27/2*n+51)),n=1..inf)
3140000446459760 (K(1/sr(2))+GAM(5/24))^Golomb
3140000895104510 GAM(2/3)-Li4(1/2)^ln(Pi)
3140001879986726 (exp(1/Pi)+5)/(-arctan(1/2)+2/3)
...
```


I don't think that it would make sense to return a Python object for I have no idea what one could want to do with it automatically. Most of the symbolic formulas have no meaning in Sage, so it's really just for the user to see. Right now the method returns nothing and just prints the result. The only think that may be cool to add would be a nice way to display such results in the notebook, but I would like to hear your advice on the possible outputs too `:-)`

And you can try this small patch if you want in the meantime.

Have fuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunnn !!!

Nathann


---

Attachment


---

Comment by kcrisman created at 2013-04-28 00:46:45

Though see comment:2 and a few early on on this ticket.


---

Comment by slelievre created at 2021-08-15 17:41:16

The function `algdep` can help identify algebraic numbers.

It would be nice to be able to identify transcendental
expressions as well.

Some more links:

- SageMath's `algdep` aka `algebraic_dependency` function: [code](https://github.com/sagemath/sage/blob/9.4.rc2/src/sage/arith/misc.py#L44) - [docs](https://doc.sagemath.org/html/en/reference/rings_standard/sage/arith/misc.html#sage.arith.misc.algdep)
  - based on PARI's algdep
  - also available as a method of various classes of floating-point numbers
- Ordner: [Ordner home](https://fungrim.org/ordner/) - [blog post introducing Ordner](http://fredrikj.net/blog/2019/09/what-is-the-most-common-real-number/)
- [xkcd comic: Approximations](https://xkcd.com/1047/)
- [RIES](http://mrob.com/pub/ries/)
- [Maple's "identify"](https://www.maplesoft.com/support/help/Maple/view.aspx?path=identify)
- SageMath's interface to the OEIS: [code](https://github.com/sagemath/sage/blob/9.4.rc2/src/sage/databases/oeis.py) - [docs](https://doc.sagemath.org/html/en/reference/databases/sage/databases/oeis.html)
- [sage-devel 2012-04 discussion](https://groups.google.com/g/sage-devel/c/M5oqX85XgU0)
- [Former ISC at CECM](http://web.archive.org/web/20150727021614/http://oldweb.cecm.sfu.ca/projects/ISC/ISCmain.html)
- [Former ISC at CARMA](https://web.archive.org/web/20180828122202/http://isc.carma.newcastle.edu.au/)


---

Comment by @sheerluck created at 2021-08-16 07:18:27

https://github.com/clsn/ries -- RIES with `constants.ries` profile, GSL Support and other extensions


---

Comment by slelievre created at 2021-10-18 11:00:02

Adding some more links found in:

- David R. Stoutemyer. How to hunt wild constants. https://arxiv.org/abs/2103.16720


---

Comment by slelievre created at 2022-02-02 21:09:39

Similar discussion on the maxima-discuss list

- [maxima-discuss, 2022-01: Inverse Symbolic Calculator interface](https://sourceforge.net/p/maxima/mailman/maxima-discuss/thread/CADB8Zm5D%3DcwNeA_XrgTEwnzb1S0wRKGz6A1Mb8EdSAYC2mujNA%40mail.gmail.com/#msg37598821)
