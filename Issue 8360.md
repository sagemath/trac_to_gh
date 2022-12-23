# Issue 8360: Add an interface to Jean-Eric Pin's Semigroupe package

Issue created by migration from https://trac.sagemath.org/ticket/8360

Original creator: nthiery

Original creation time: 2010-02-25 09:00:20

Assignee: nthiery

CC:  sage-combinat jean-eric.pin@liafa.jussieu.fr abmasse tscrim

Keywords: Semigroupes

Add an interface to Jean-Eric Pin's Semigroupe package

http://www.liafa.jussieu.fr/~jep/semigroupes.html

Patch and spkg under development on the Sage-Combinat server.


---

Attachment


---

Comment by nthiery created at 2010-03-16 13:04:44

Changing status from new to needs_work.


---

Comment by nthiery created at 2010-03-17 20:23:24

Superceedes the previous spkg


---

Attachment


---

Comment by saliola created at 2010-05-11 20:43:35

There seems to be a problem on a 64bit machine. After installing the spkg, the following commands will cause Sage to segfault:

```
sage: W = CoxeterGroup(["H",4])
sage: S = semigroupe.AutomaticSemigroup(W.semigroup_generators(), W.one(), category = FiniteCoxeterGroups())
sage: S.cardinality()
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in Sage.
...
```


The problem seems to be with compiling Semigroupe on a 64bit machine. After installing the package, the following segfaults:

```
karkwa: cd $SAGE_ROOT/local/bin
karkwa: Semigroupe
karkwa: ./Semigroupe
Segmentation fault
karkwa: ./SelfContainedTest 
Toto
a | 2  3  1 
b | 2  1  3 
c | 1  2  1 

Segmentation fault
karkwa: ./SemigroupeModuleTest 

a | 2  1 
b | 1  1 

Segmentation fault 
```

I think that the two test suites (I think they are test suites...) should be run by the `spkg-check` script.


---

Comment by aschilling created at 2010-05-12 02:43:34

On a 32-bit machine, I obtain the following error:

sage: S = semigroupe.AutomaticSemigroup(W.semigroup_generators(), W.one(), category = FiniteCoxeterGroups())
sage: S.cardinality()
python(24860) malloc: *** vm_allocate(size=262144) failed (error code=3)
python(24860) malloc: *** error: can't allocate region
python(24860) malloc: *** set a breakpoint in szone_error to debug
memory allocation failed
memory usage :

size : 2^       used/allocated 
  0              310/312       
  1               21/22        
  2              109/109       
  3               73/73        
  4               49/50        
  5                5/6         
  6                9/9         
  7                3/3         
  8                1/1         
  9                1/1         
 10                1/2         
 11                0/1         
 12                0/0         
 13                0/1         
 14                1/1         
 15            25959/25959     
 16                0/0         
 17                0/0         
 18                0/0         
 19                0/0         
 20                0/0         
 21                0/0         
 22                0/0         
 23                0/0         
 24                0/0         
 25                0/0         
 26                0/0         
 27                0/0         
 28                0/0         
 29                0/0         
 30                0/0         
 31                0/0         

total :  850645964/850657280  4-byte units used/allocated
.../Applications/sage-4.4/devel/sage-combinat/sage/combinat/crystals$ 

Anne


---

Comment by saliola created at 2010-05-13 16:46:40

In case this helps track down the issue: things seem to be working correctly in a 32bit virtual machine. I created a 32bit VirtualBox virtual machine, installed Ubuntu 10.04, then I installed the sage-4.4.1 binary, the gap3 spkg from #8906, and the semigroupe spkg here.


---

Comment by nthiery created at 2010-05-26 19:20:24

> I think that the two test suites (I think they are test suites...) should be run by the `spkg-check` script.

Those are little self contained test programs we had written with Florent to understand how semigroupe was working. Yes, they eventually should be turned into test suites, and run from `spkg-check`.


---

Attachment

Same as previous one, working on both 32bits and 64bits, but managing the patches on the semigroupe sources in a mercurial queue


---

Comment by slabbe created at 2014-02-06 12:51:04

Note that semigroupe is now part of the experimental packages:

http://www.sagemath.org/packages/experimental/

One can install it with the usual `sage -i semigroupe-2.0-2.spkg`.

next step is to make the code in sage-combinat go into sage...


---

Comment by nthiery created at 2014-02-06 13:00:38

Great, thanks Sébastien for taking care of this!

The next step is actually just to make a branch out of the patch. I am not sure about actually getting this branch into Sage until Semigroupe will be fixed one way or the other to support several semigroups simultaneously.

Cheers,
                                Nicolas


---

Comment by slabbe created at 2014-02-06 13:42:10

Replying to [comment:12 nthiery]:
> Great, thanks Sébastien for taking care of this!
> 
> The next step is actually just to make a branch out of the patch.

you mean a git branch?

which patch? is it finite_semigroup-nt.patch ?

I don't see how this patch uses semigroupe.

> I am not sure about actually getting this branch into Sage until 
> Semigroupe will be fixed one way or the other to support several 
> semigroups simultaneously.

I think I don't agree. I think the goal of the actual ticket #8360 is to make the actual semigroup into sage as it is. semigroupe was written for something no? Let's first make this available!

Then I suggest to open a ticket showing with sage command line code illustrating how the bug for creating two semigroup simultaneously is obtained. The new ticket would ask for an upstream fix.

Sébastien


---

Comment by nthiery created at 2014-02-06 14:04:14

Replying to [comment:13 slabbe]:
> Replying to [comment:12 nthiery]:
> > The next step is actually just to make a branch out of the patch.
> you mean a git branch?

Yup.

> which patch? is it finite_semigroup-nt.patch ?
> I don't see how this patch uses semigroupe.

trac_8360_semigroupe-interface-nt.patch

> > I am not sure about actually getting this branch into Sage until 
> > Semigroupe will be fixed one way or the other to support several 
> > semigroups simultaneously.
> I think I don't agree. I think the goal of the actual ticket #8360
> is to make the actual semigroup into sage as it is. semigroupe was
> written for something no? Let's first make this available!

Indeed, the interface was written for something. But in practice, even
if I spent quite some time on it, I am actually seldom using it
because that misfeature is making it relatively unusable (at least in
my use-cases).

> Then I suggest to open a ticket showing with sage command line code
> illustrating how the bug for creating two semigroup simultaneously
> is obtained. The new ticket would ask for an upstream fix.

That's an option. If you are convinced that:

- At some point not to far in the future the bug will be fixed upstream (upstream meaning possibly us taking the time to do the fix).

- The current code won't need serious interface change then.

Then let's go ahead. I'd love to have this code always under my fingertips. Otherwise I am a bit reluctant to put in Sage some code that we might need to remove (because unused) or change a
lot later on.

At the end of the day, this would actually be best handled by putting
the interface code in the spkg and not in the Sage library. I haven't
checked how hard/easy it would be to handle.

Cheers,
                            Nicolas


---

Attachment
