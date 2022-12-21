# Issue 8254: sage takes way too long to startup

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-02-13 00:27:52

Assignee: tbd

Sage still takes too long.  20 seconds, 30 seconds, 5 seconds, on various places... and it is all so painful.


---

Comment by mpatel created at 2010-02-14 02:06:00

Could you provide some additional data?  Which platforms?  I assume that `sage -startuptime` does not help, or does it?


---

Comment by mpatel created at 2010-02-14 03:52:23

By "help," I mean "help to identify the problem(s)."


---

Comment by robertwb created at 2010-02-15 19:39:17

OS X for one.


---

Comment by drkirkby created at 2010-02-28 17:59:23

FWIW, Sage 4.3.3 (with some mods to get it to build on Solaris) takes 8 seconds to start on a Sun Blade 1000, with 2 x 900 MHz CPUs and 2 GB RAM. That machine has 15,000 rpm 2 Gbit/s fibre channel FC-AL disks. 

Considering the age of that machine, I'm not overly concerned over that one. Although this machine is quite old, the disks are quite high spec. I don't know if that gives any clues. File systems are local. 

The doc test 


```
sage -t  "devel/sage/sage/rings/polynomial/symmetric_ideal.py" 
```


takes 459.4 seconds to run on that machine, so this is no quick machine - I had to increase SAGE_TIMEOUT just to get some doctests to pass. 

Dave


---

Comment by drkirkby created at 2010-02-28 18:04:24

Given the startup time for me, on that SPARC, and the fact I have a quicker SPARC, I'm not overly concerned by this myself. 

But those interested in fixing it might like to look at using 'iostat', 'vmstat' and 'sar' to see what the system is doing. 

Dave


---

Comment by drkirkby created at 2010-02-28 18:15:23

PS, that Blade 1000 of mine is using UFS disks, not ZFS. Using ZFS would take more memory from a machine that already has very little. 

I suspect the startup time has more to do with disk & file-system performance than it does with CPU speed. 

Dave


---

Comment by drkirkby created at 2010-02-28 18:15:23

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2010-02-28 18:15:41

Remove assignee drkirkby.


---

Comment by robertwb created at 2010-03-06 09:46:47

Shaves off about 0.3 seconds for me. Depends on #8456


---

Comment by was created at 2010-11-03 04:38:43

Changing status from new to needs_review.


---

Attachment

I talked to Robert today and he told me thought he had marked this "needs review", but he hadn't.  So I am.


---

Comment by robertwb created at 2010-11-03 08:00:56

Yep, this is ready for review (assuming it hasn't bitrotted). Regarding Davve Kirkby's comment, I agree that disk access is probably the main bottleneck, and this addresses that by loading fewer modules.


---

Comment by lftabera created at 2010-11-04 13:25:25

The patch applies to 4.6 after rebasing #8456

In my computer, from a first running (disc access is necessary), Sage passes from 12.059 seconds to 11.290 So, a save less than 10%

If I further lazy import doing a 
lazy import for every * imports and running sage.misc.lazy_import.save_cache_file() the time drops to 10.259

If I run Sage with the initialitation files in RAM (disc acces is not necessary) the time with lazy_importing all * drops from 1.123 to 0.907

So, still, with lazy imports, disc access is too high.


with Robert patch I get the following doctest failures:
sage-devel -t  -long -force_lib devel/sage/doc/en/bordeaux_2008/generators_for_rings.rst
sage-devel -t  -long -force_lib devel/sage/sage/structure/coerce_actions.pyx
sage-devel -t  -long -force_lib devel/sage/sage/modular/cusps.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/hecke/module.py 
sage-devel -t  -long -force_lib devel/sage/sage/modular/hecke/hecke_operator.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/modsym/heilbronn.pyx
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/arithgroup_element.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_gammaH.py 
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_sl2z.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_gamma0.py 
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_gamma1.py 
sage-devel -t  -long -force_lib devel/sage/sage/modular/arithgroup/congroup_generic.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/modform/space.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/modform/find_generators.py
sage-devel -t  -long -force_lib devel/sage/sage/modular/modform/cuspidal_submodule.py


---

Comment by robertwb created at 2010-11-04 18:04:26

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-11-04 18:04:26

The first import * (after every sage -b) needs to import the modules to get the names. However, if there's only a 10% gain, I should take another look and make sure something isn't accidentally still pulling it in. (A lot has changed since I wrote this patch...)


---

Comment by jason created at 2010-11-05 03:37:45

I've attached a patch that seems to get some of the worst offenders for wasteful imports in 4.6.  I haven't run doctests yet, though...


---

Comment by jason created at 2010-11-05 03:39:35

From a warm file cache, my patch seems to shave off about 1.4% of the startup time (times averaged over 5 runs).  From a cold file cache, my guess is that it would be more than that because the unnecessary imports I take care of touch a lot of files.


---

Comment by lftabera created at 2010-11-05 08:07:40

Another issue I have found with this patch. With the lazy_imports in all.py, the namespace used in the instances is not the global namespace.

(after several runnings of sage, so it uses the cached database of functions)


```
sage: sloane_sequence
<sage.misc.lazy_import.LazyImport object at 0x3e4d950>
sage: sloane_sequence._get_object()
<function sloane_sequence at 0x51a7230>
sage: sloane_sequence
<sage.misc.lazy_import.LazyImport object at 0x3e4d950>
```


It does not introduce sloane_sequence function in the global namespace but in sloane_sequence._namespace that seems to not be the global one.


---

Comment by jason created at 2010-11-05 12:36:24

Okay, I guess because of the ticket title, I attached my patch.  But the ticket title is way too general.  I've made the title more descriptive, and moved my much simpler patch to #10220


---

Comment by lftabera created at 2011-03-03 10:02:47

Concerning the input on the global namespace in sage.all.py one can write


```
import __builtin__
G = __builtin__.__dict__
del __builtin__
```


and insert everything in the dictionary G.

But his looks like a very ugly hack.


---

Comment by lftabera created at 2011-03-03 22:59:18

What I wrote above is nonsense. I am adding names to the __builtin__ namespace. Instead it should be _ip.user_ns, the namespace of the IPython session.

If we only do lazy_imports from sage.all we will not get an usable enviroment that load fasts.

If we add lazy_imports in other all.py files we will get problems messing with namespaces.

Suppose the following:

in sage.all:[br]
from sage.rings.all import *

in sage.rings.all:[br]
from sage.rings.polynomial.all import *

If we lazy_import sage.rings.polynomial.all names in sage.rings.all then we have to choose a namespace.

If the namespace chosen is the top one. When inserting the real object, it will be inserted in the main namespace, so, in the module sage.rings.all we will always have the lazy_import object.

If the namespace chosen is sage.rings.all then we will always have the lazy_object in the main namespace...

This is too technical for me to offer a solution at module level. One idea is to add other files called lazy_all.py. these will be modules that import/lazy_import names in the IPython top namespace. They are not intended for the library code, only to have a more fine grain control on what are lazy_importing or not at the start.

Comments? It is worth to give it a try?


---

Comment by robertwb created at 2011-03-04 05:49:20

If we do a lazy_import of x in sage.foo, and then someone does "from sage.foo import x" in m, I don't see any way to resolve the original x in m. It may be worth registering a "top-level" namespace that substitutions would be made into. 

Note, however, that lazy imports are for library code as well.


---

Comment by robertwb created at 2011-03-26 09:18:18

I'm making this ticket into a meta-ticket, link from here to various speedups.


---

Comment by was created at 2011-08-24 23:29:58

Changing keywords from "" to "sd32".


---

Comment by nbruin created at 2019-09-16 18:16:17

See [https://bugs.python.org/issue34690](https://bugs.python.org/issue34690) for a quite different approach to (significantly) speed up start-up time. It avoids file stats to speed up as well, so I suspect it would be a particularly suitable speed-up for sage (where we're stat-ing loads of files). If we can use this somehow, we'd probably need some tuning parameters to choose which parts of the library are cached and which are loaded fresh.
