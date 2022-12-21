# Issue 4671: [with patch; needs review] sage-3.2.1 startup time: it sucks again

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-02 05:24:14

Assignee: boothby

On OS X the Sage startup time is horrible.  Doing sage -startuptime yields:

```
## Slowest (including children)
1.604 sage.all (None)
0.453 sage.server.all (sage.all)
0.449 notebook.all (sage.server.all)
0.445 notebook_object (notebook.all)
0.441 notebook (notebook_object)
0.352 worksheet (notebook)
0.345 twist (worksheet)
0.329 sage.misc.all (sage.all)
0.246 twisted.web2 (twist)
0.125 sage_timeit_class (sage.misc.all)
0.125 sage_timeit (sage_timeit_class)
```


I'm pretty suspicious, because the twisted stuff does *not* have to be imported at all for Sage to startup and in fact I put a lot of effort into making sure they don't (it's really annoying that they are suddenly being imported again!)

The tiny attached patch just moves a few imports and for me on OS X reduces the startup time of Sage from about 1.64 to 1.273.  It also includes a doctest that makes sure twisted will *never* get imported on startup by default.




---

Attachment


---

Comment by mhansen created at 2008-12-02 07:42:04

Looks good to me.


---

Comment by mabshoff created at 2008-12-03 08:53:07

Bad mhansen: This patch breaks pickling all over the combinat tree:

```
	sage -t -long devel/sage/sage/combinat/root_system/weight_space.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_reducible.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_dual.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_G.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_F.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_E.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/type_A.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/root_space.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/root_system.py # 3 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/dynkin_diagram.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/cartan_type.py # 2 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/ambient_space.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/tensor_product.py # 4 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/letters.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/sloane_functions.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/weyl_group.py # 2 doctests failed
	sage -t -long devel/sage/sage/combinat/root_system/weyl_characters.py # 4 doctests failed
```

Probably a trivial problem, but "needs work" nonetheless :p

Cheers,

Michael


---

Comment by was created at 2008-12-04 21:14:35

This is really really weird.  The *only* thing I change is to remove two instances of "import twist" in the notebook code.  The *only* doctests in the whole Sage tree that break are those combinat pickles.  Absolutely nothing else breaks (I just tested this).  If one tries them by hand on the command line they break, but if one does

```
  sage: import sage.server.notebook.twist
```

then they suddenly work. 

And those tests are not just pickle tests that fail.

Mike -- can you think of anything that combinat code uses that might somehow have something to do with twisted or twist.py being imported?


---

Attachment


---

Comment by mhansen created at 2008-12-16 17:17:37

I've put up a new patch which imports twisted.persisted.styles, but still make startup time way faster.


```
<mhansen> No
<mhansen> I still have no idea why it's happening.
<mhansen> And I found it.  [08:40]
<mhansen> Twisted has some code in twisted.persistant.styles that allows you
          to pickle things that aren't picklable normally.  [08:42]
<mhansen> Importing just that takes .110s on my machine while doing import
          twist takes 0.675s.  [08:48]
<mhansen> Doing so causes wstein|afk's doctest to fail.  [08:49]
<wstein|afk> mhansen -- importing twisted.persistant.styles and changing my
             doctest is a good solution.  [09:02]
```



---

Comment by mabshoff created at 2008-12-21 11:02:23

We should attempt to get this into 3.2.3.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 21:30:30

The patch trac_4671-2.patch fixes the picklig issue and reduces the startup time significantly. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 21:30:58

Resolution: fixed


---

Comment by mabshoff created at 2008-12-21 21:30:58

Merged in Sage 3.2.3.alpha0
