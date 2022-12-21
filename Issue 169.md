# Issue 169: slice assignment not implemented for PARI C library interface

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-11-15 15:44:35

Assignee: was

{{{From "Luislang" 

Following session says it all.
 
--------------------------------------------------------
--------------------------------------------------------
 
sage: s=pari.vector(2,[0,0])
sage: s[:1]
 _2 = [0]
sage: s[:1]=[1]
------------------------------------------------------------
Traceback (most recent call last):
  File "<console>", line 1, in ?
  File "gen.pyx", line 417, in gen.gen.__setitem__
IndexError: index (slice(0, 1, None)) must be between 0 and 1
}}}


---

Comment by was created at 2006-11-15 15:49:05


```
 
I'm not understanding your question. Lists are mutable:
sage: L = [0,0]
sage: L[:1] = [1]
sage: L
 [1, 0]
pari vectors apparently are not. Are you saying they should be?
Or is it that you don't like the error message?
 
The problem is simply that I only implemented __setitem__ in
the case of an integer input.  He wants a more general __setitem__
to be implemented also for PARI vectors, which are mutable:
sage: s=pari.vector(2,[0,0])
sage: s[0] = 5
sage: s
[5, 0]
 
I think the problem is that I didn't realize "s[slice] = blah"
was a standard Python idiom, so I didn't implement support for
it for the PARI C-library interface.
 
 }}}


---

Comment by mabshoff created at 2007-08-23 12:34:48

So William, would still consider this worth fixing? Sage 2.8.2-rc3 still has this issue roughly 18months later :(

```
sage: s=pari.vector(2,[0,0])
sage: sage: s[:1]
[0]
sage: s[:1]=[1]
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/<ipython console> in <module>()

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/gen.pyx in gen.gen.__setitem__()

<type 'exceptions.IndexError'>: index (slice(None, 1, None)) must be between 0 and 1
```


Cheers,

Michael


---

Comment by craigcitro created at 2008-11-14 05:27:24

Resolution: fixed


---

Comment by craigcitro created at 2008-11-14 05:27:24

Actually, this is already fixed:


```
sage: s=pari.vector(2,[0,0])
sage: s[:1]
[0]
sage: s[:1]=[1]
True
```


The `__getslice__` function is also already doctested, so no need to add more. I'm closing this as fixed.


---

Comment by craigcitro created at 2008-11-14 05:33:00

Resolution changed from fixed to 


---

Comment by craigcitro created at 2008-11-14 05:33:00

Changing status from closed to reopened.


---

Comment by craigcitro created at 2008-11-14 05:33:00

Sorry, I can't read. I didn't notice that it was `__setslice__` that we were talking about.


---

Comment by mabshoff created at 2008-11-14 05:33:50

Changing status from reopened to new.


---

Comment by mabshoff created at 2008-11-14 05:33:50

Changing assignee from was to craigcitro.


---

Comment by mabshoff created at 2008-11-14 05:33:50

Indeed:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |
| Type notebook() for the GUI, and license() for information.        |
sage: s=pari.vector(2,[0,0])
sage: s[:1]
[0]
sage: s[:1]=[1]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.2.rc1/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.gen.__setitem__ (sage/libs/pari/gen.c:6394)()

TypeError: int() argument must be a string or a number, not 'slice'
sage: 
```



---

Comment by craigcitro created at 2008-11-14 06:42:16

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-11-14 06:42:16

Okay, in exchange for being an idiot at reading, I went ahead and fixed this. Attached patch should do the trick.


---

Comment by jason created at 2008-11-14 15:24:10

First, __setslice__ is deprecated: http://www.python.org/doc/2.5.2/ref/sequence-methods.html

Instead, check for a slice object in the __setitem__ function.

Also, the slice could have a step as well:


```
sage: a=[1,2,3,4,5,6,7,8,9]
sage: a[2:8:2]
[3, 5, 7]
```



---

Comment by jason created at 2008-11-14 15:26:09

I should add: Thanks so much for doing this long-standing feature request!  You rock!


---

Comment by craigcitro created at 2008-11-14 17:26:07

Ah, cool. I had no idea that `__setslice__` was deprecated. I'll clean this up today or tomorrow.


---

Comment by craigcitro created at 2008-11-19 11:22:47

new and improved patch


---

Attachment

New patch, with lots of added functionality. (I read what all you can do with the `step` parameter to slice.


---

Comment by robertwb created at 2008-11-21 00:03:20

Wow, that was a lot of work. Looks good to me.


---

Comment by jason created at 2008-11-21 02:48:38

Wow, robertwb is right; that was a lot of work.

Thanks for the generic normalize slice function.  Eventually, it would be great to move that to a more general utility function, maybe somewhere in sage/misc or something.  I can see it being very, very useful for other objects that need to implement slice notation (for example, matrices and vectors of other types).


---

Comment by mabshoff created at 2008-11-21 05:19:15

Oops:

```
        sage -t -long devel/sage/sage/tests/book_stein_modform.py # 7 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 47 doctests failed
        sage -t -long devel/sage/sage/rings/number_field/number_field.py # 3 doctests failed
        sage -t -long devel/sage/sage/rings/integer.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/modular/modform/tests.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/modform/submodule.py # 1 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 4 doctests failed
        sage -t -long devel/sage/sage/modular/modform/hecke_operator_on_qexp.py # 11 doctests failed
        sage -t -long devel/sage/sage/modular/modform/half_integral.py # 5 doctests failed
        sage -t -long devel/sage/sage/modular/modform/space.py # 61 doctests failed
        sage -t -long devel/sage/sage/modular/modform/ambient_g1.py # 1 doctests failed
        sage -t -long devel/sage/sage/modular/modform/cuspidal_submodule.py # 6 doctests failed
        sage -t -long devel/sage/sage/modular/modform/eisenstein_submodule.py # 12 doctests failed
        sage -t -long devel/sage/sage/modular/modform/constructor.py # 6 doctests failed
        sage -t -long devel/sage/sage/modular/modform/ambient_R.py # 1 doctests failed
        sage -t -long devel/sage/sage/modular/modform/ambient.py # 12 doctests failed
        sage -t -long devel/sage/sage/modular/modform/element.py # 49 doctests failed
        sage -t -long devel/sage/sage/modular/hecke/module.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/constructor.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_newform.py # 11 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/morphism.py # 4 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/homspace.py # 32 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar.py # 10 doctests failed
        sage -t -long devel/sage/sage/libs/pari/gen.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 8 doctests failed
```

Is there a dependency I missed?

Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2008-11-21 05:32:47

Yep, I forgot to handle the case of lists of length 0. Oops.

Attached patch should fix everything.


---

Comment by mabshoff created at 2008-11-21 05:34:55

+1 on trac-169-pt2.patch.

Cheers,

Michael


---

Comment by robertwb created at 2008-11-21 05:40:12

I ran doctests on a couple of files as well as trying this out and looking at the code, but I guess there's nothing like a full sage -testall


---

Comment by mabshoff created at 2008-11-21 06:40:36

Mhh, odd things happen on 64 bit I assume:

```
sage -t -long devel/sage/sage/libs/pari/gen.pyx             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/libs/pari/gen.pyx", line 2714:
    sage: pari(2**50).length()
Expected:
    4             
Got:
    1
**********************************************************************
```

I would guess this is a 32 vs. 64 bit issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-21 06:53:57


```
[10:22pm] mabshoff: craigcitro: One more think for #169 - looks like 32 vs. 64 bit maybe?
[10:50pm] craigcitro: mabshoff: oops, i can't count.
[10:50pm] craigcitro: i multiplied by 2 when i should have divided ...
[10:50pm] craigcitro: the 4 should really be a 1
[10:50pm] mabshoff: Don't tell me this fails on your box, too 
[10:51pm] mabshoff:
[10:51pm] craigcitro: (it's already got cases for 32 vs 64 bit)
[10:51pm] craigcitro: grin
[10:51pm] mabshoff:
[10:51pm] craigcitro: yeah, i was just being dumb.
[10:51pm] mabshoff: Don't divide - craigcitro inside?
[10:51pm] craigcitro: hahahahaha
[10:51pm] mabshoff: Couldn't resist 
[10:51pm] craigcitro: should i make a new patch? or do you want to edit the patch?
[10:51pm] mabshoff: I will edit the patch
[10:51pm] craigcitro: k
```



---

Comment by mabshoff created at 2008-11-21 07:27:26

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 07:27:26

Merged both patches in Sage 3.2.1.alpha0
