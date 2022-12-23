# Issue 6391: libGAP!  -- create a Cython library interface to gap

Issue created by migration from https://trac.sagemath.org/ticket/6391

Original creator: was

Original creation time: 2009-06-23 21:59:35

Assignee: was

CC:  burcin nborie robertwb jeremywest iandrus davidm kini kcrisman nthiery jpflori simonking

There's libSingular, there's libPari, and next we need to create libGAP.


---

Comment by was created at 2009-06-23 22:04:57

To try out the first demo libgap.a use of GAP as a library:

1. Install this spkg: http://sage.math.washington.edu/home/wstein/patches/gap-4.4.10.p13.spkg

2. Apply the patch trac_6391.patch attached to this ticket and do "sage -br".

Then

```
sage: sage.libs.gap.gap.command()
...
> NormalSubgroups(SymmetricGroup(4));
[ Group(()), Group([ (1,4)(2,3), (1,3)(2,4) ]), Group([ (2,4,3), (1,4)(2,3), (1,3)(2,4) ]), Sym( [ 1 .. 4 ] ) ]
sage: sage.libs.gap.gap.command()
> a := 8383;
8383
sage: sage.libs.gap.gap.command()
> a^20;
2937577432790013740156622649268134038711666398939150844563902439935080138297601
```



---

Comment by was created at 2009-06-23 22:17:09

Before the above, be sure to do 

```
import sage.libs.gap.gap
```



---

Attachment

Make sure to use the latest spkg, which I'll keep in the ticket description.


---

Attachment


---

Comment by was created at 2009-06-25 21:25:14

Changing type from defect to enhancement.


---

Attachment


---

Attachment


---

Comment by was created at 2009-09-28 21:09:17

This log pretty much explains what/why/what next:

```
sage: import sage.libs.gap.gap as g
sage: a = g.libgap('10')
sage: a
10
sage: type(a)
<type 'sage.libs.gap.gap.GapElement'>
sage: a*a
100
sage: timeit('a*a')
625 loops, best of 3: 209 ns per loop
sage: b = gap('10')
sage: b
10
sage: b*b
100
sage: type(b)
<class 'sage.interfaces.gap.GapElement'>
sage: !ps ax |grep gap
 5497 pts/110  Ss+    0:00 /home/bober/sage-4.1/local/lib/gap-4.4.10/bin/x86_64-unknown-linux-gnu-gcc/gap -m 24m -l /home/bober/sage-4.
19751 pts/84   SNs+   0:00 /home/SimonKing/SAGE/sage-4.1.alpha1/local/lib/gap-4.4.10/bin/x86_64-unknown-linux-gnu-gcc/gap -m 24m -l /ho
27563 pts/109  Ss+    0:00 /scratch/steinz/sage/local/lib/gap-4.4.10/bin/x86_64-unknown-linux-gnu-gcc/gap -m 24m -l /scratch/steinz/sag
27572 pts/98   S+     0:00 sh -c ps ax |grep gap
27574 pts/98   S+     0:00 grep gap
sage: b.name()
'$sage1'
sage: timeit('b*b')
625 loops, best of 3: 292 µs per loop
sage: a = g.libgap('0')
sage: a
0
sage: b = g.libgap('10')
sage: b/a
hit stderr
```



---

Comment by was created at 2009-09-28 21:24:31

Overview:

* Modified version of GAP, which is built by doing

```
sage -f -m  http://sage.math.washington.edu/home/wstein/patches/gap/gap-4.4.10.p17.spkg
wait...
cd sage/spkg/build/gap-4.4.10.p17
```

To rebuild:

```
steinz@sage:~/scratch/sage/spkg/build/gap-4.4.10.p17/src$ make
steinz@sage:~/scratch/sage/spkg/build/gap-4.4.10.p17/src/bin/x86_64-unknown-linux-gnu-gcc$ gcc -shared *.o -o libgap.so
```


* Cython code to use the Gap library:

```
In here:
   sage/devel/sage/sage/libs/gap/gap.pyx
```


If you change gap.pyx, do `sage -br` to build the changed version and start Sage.


---

Comment by davidm created at 2010-04-10 23:32:02

I get an error when importing libgap on sage 4.3.5 on OSX 10.6.3: 



```
sage: import sage.libs.gap.gap
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/ayeq/sage-devel/<ipython console> in <module>()

/Users/ayeq/sage-devel/gap.pyx in init sage.libs.gap.gap (sage/libs/gap/gap.c:6286)()

/Users/ayeq/sage-devel/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __init__(self, f, classmethod)
     54 
     55         """
---> 56         self._common_init(f, ArgumentFixer(f,classmethod=classmethod))
     57         self.cache = {}
     58 

/Users/ayeq/sage-devel/local/lib/python2.6/site-packages/sage/misc/function_mangling.pyc in __init__(self, f, classmethod)
    107         """        
    108 
--> 109         defaults = f.func_defaults
    110         if defaults is None:
    111             defaults = []

AttributeError: 'builtin_function_or_method' object has no attribute 'func_defaults'
```


The cached_function decorator works at the interpreter level so I really do not see what is happening. When the line is removed  the import works fine and from what I understand about cache_function this should be okay. 


```
--- a/sage/libs/gap/gap.pyx	Sat Jun 27 05:49:14 2009 +0200
+++ b/sage/libs/gap/gap.pyx	Sat Apr 10 16:30:27 2010 -0700
@@ -71,8 +71,8 @@
 
 from sage.structure.element cimport ModuleElement, RingElement
   
-from sage.misc.cachefunc import cached_function
-@cached_function
+#from sage.misc.cachefunc import cached_function
+#@cached_function
 def gap_root():
     """
     Find the location of the GAP root install which is stored in the gap
```



---

Comment by dimpase created at 2011-01-14 18:34:03

Replying to [comment:14 davidm]:
> I get an error when importing libgap on sage 4.3.5 on OSX 10.6.3: 
> 
 
 {{{
 sage: import sage.libs.gap.gap
 ---------------------------------------------------------------------------
 AttributeError                            Traceback (most recent call last)
 
 /Users/ayeq/sage-devel/<ipython console> in <module>()
 
 /Users/ayeq/sage-devel/gap.pyx in init sage.libs.gap.gap (sage/libs/gap/gap.c:6286)()
 
/Users/ayeq/sage-devel/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __init__(self, f, classmethod)
      54 
      55         """
 ---> 56         self._common_init(f, ArgumentFixer(f,classmethod=classmethod))
      57         self.cache = {}
      58 
 
 /Users/ayeq/sage-devel/local/lib/python2.6/site-packages/sage/misc/function_mangling.pyc in __init__(self, f, classmethod)
     107         """        
     108 
 --> 109         defaults = f.func_defaults
     110         if defaults is None:
     111             defaults = []
 
 AttributeError: 'builtin_function_or_method' object has no attribute 'func_defaults'
 }}}


I see exactly the same with the new spkg on OSX 10.6. 
And the patch to gap.pyx you suggest works for me too.


---

Comment by dimpase created at 2011-01-14 21:37:06

Replying to [comment:19 dimpase]:
> Replying to [comment:14 davidm]:
> > I get an error when importing libgap on sage 4.3.5 on OSX 10.6.3: 
> > 
> 
> I see exactly the same with the new spkg on OSX 10.6. 
> And the patch to gap.pyx you suggest works for me too.
> 

moreover, I get the same problem (and solition(?)) on Linux (on boxen). So this is certainly not OSX-specific.


---

Attachment

cumulative patch for sage 4.6.1


---

Comment by dimpase created at 2011-01-17 14:15:46

Replying to [comment:20 dimpase]:
> Replying to [comment:19 dimpase]:
> > Replying to [comment:14 davidm]:
> > > I get an error when importing libgap on sage 4.3.5 on OSX 10.6.3: 
> > > 
> > 
> > I see exactly the same with the new spkg on OSX 10.6. 
> > And the patch to gap.pyx you suggest works for me too.
> > 
> 
> moreover, I get the same problem (and solition(?)) on Linux (on boxen). So this is certainly not OSX-specific.

it turns out that cached_function won't work in Cython at all, so indeed this needs to be changed.
The cumulative patch 6391.6.patch fixed this, as well, as it supersedes the previous 4 patches.

To install for Sage 4.6.1, install the updated spkg, and this patch.


Dima


---

Comment by dimpase created at 2011-01-18 13:34:33

Perhaps someone who understands libs/gap/gap.pyx better than me can comment on few sticking points I encounter:

class Gap(ParentWithBase) is instantiated only once, for base=ZZ. Is it meant that it should be instantiated for other bases, too? And if so, which ones? (I must say it's very puzzling to me piece of code...)

in the class GapElement, _div_ and other member functions can potentially fail (as demonstrated in the comment "This log pretty much explains what/why/what next:..." above), e.g. due to division by 0. It is meant that the corresponding checks are to be implemented in these member functions? I guess not, it's rather a matter of properly catching the corresponding GAP interrupts, right?

What _dealloc_ in this class meant to do?


---

Comment by was created at 2011-01-18 16:32:51

Replying to [comment:22 dimpase]:
> class Gap(ParentWithBase) is instantiated only once, for base=ZZ. Is it meant that it should be instantiated for other bases, too? And if so, which ones? (I must say it's very puzzling to me piece of code...)
> 

No, only once for base=ZZ.  

> in the class GapElement, _div_ and other member functions can potentially fail (as demonstrated in the comment "This log pretty much explains what/why/what next:..." above), e.g. due to division by 0. It is meant that the corresponding checks are to be implemented in these member functions? I guess not, it's rather a matter of properly catching the corresponding GAP interrupts, right?
> 

Yes.  I don't know if GAP uses "interrupts" though.  You are basically above asking: "Here is a problem nobody has solved yet, which is why libgap hasn't moved forward.  What is the solution?"

> What _dealloc_ in this class meant to do? 

See {{__dealloc__}} at http://docs.cython.org/src/reference/extension_types.html for the definition of __dealloc__.  It is like __del__ in python.


---

Comment by dimpase created at 2011-01-18 22:19:04

Replying to [comment:23 was]:
> Replying to [comment:22 dimpase]:

> > in the class GapElement, _div_ and other member functions can potentially fail (as demonstrated in the comment "This log pretty much explains what/why/what next:..." above), e.g. due to division by 0. It is meant that the corresponding checks are to be implemented in these member functions? I guess not, it's rather a matter of properly catching the corresponding GAP interrupts, right?
> > 
> 
> Yes.  I don't know if GAP uses "interrupts" though.  You are basically above asking: "Here is a problem nobody has solved yet, which is why libgap hasn't moved forward.  What is the solution?"
> 

From printing contents of the GAP interpreter output_buffer (introduced in the patch of GAP's scanner.c), I see that during the fatal a._div_(g.libgap('0'))_ it starts getting the contents of the usual GAP error message, like Entering break read-eval-print loop (i.e. it does a "GAP interrupt"). And then the crash happens in the Python interpreter. So I suppose more reverse engineering/understanding of the GAP interpreter is needed here, in order to avoid replicating it in Python...


---

Comment by vbraun created at 2011-03-22 01:27:38

Changing status from new to needs_work.


---

Comment by vbraun created at 2011-03-22 01:27:38

I updated the patch to work with Sage-4.7.alpha1. I also added a bunch of doctests while trying to understand what is going on and replaced the deprecated `ParentWithBase` with `Parent`.

I'll be doing some more work on libgap during Sage Days 29, so let me know if you have any suggestions.


---

Comment by dimpase created at 2011-03-22 01:39:31

Replying to [comment:25 vbraun]:
> I updated the patch to work with Sage-4.7.alpha1. I also added a bunch of doctests while trying to understand what is going on and replaced the deprecated `ParentWithBase` with `Parent`.
> 
> I'll be doing some more work on libgap during Sage Days 29, so let me know if you have any suggestions.
> 

I am not so sure that we should invest a lot of time in libGAP based on the current GAP 4.4.12, as GAP 4.5 is almost ready,
(as a GAP package developer, I'm expecting to get it pretty soon) and has a lot of internals reworked. I understand that the GC is replaced by the Bohm's GC, and the arbitrary precision arithmetic is done by GMP, not by the internal GAP code (I suggested that they should try MPIR instead of GMP).


---

Comment by was created at 2011-03-22 01:42:24

From my memory of libGAP the GC and the large integer arithmetic are totally orthogonal/irrelevant.    I think working on libGAP whenever somebody has the interest (!) is a good idea, since it really will be a major, major plus for Sage when it starts working.


---

Comment by vbraun created at 2011-03-22 02:24:14

I think the big issues right now are
  * being able to get out of the break/debug loop after a gap error
  * use libtool to build the library
If upstream manages to rid themselves of their memory manager and arbitrary precision arithmetic then thats awesome!


---

Comment by dimpase created at 2011-03-22 02:30:40

Replying to [comment:28 vbraun]:
> I think the big issues right now are
>   * being able to get out of the break/debug loop after a gap error
>   * use libtool to build the library
> If upstream manages to rid themselves of their memory manager and arbitrary precision arithmetic then thats awesome!
> 

Hi Volker,
please see my current (Sage-4.6.1) snapshot, catching zero division etc.

  http://sage.math.washington.edu/home/dima/packages/gap-4.4.12.p6.spkg

It gets rid of the zero division problem. I.e. I can divide by 0 in GAP and still retain Sage/GAP session.
Here is an example (sorry for extra print statements producing noise below)


```
sage: import sage.libs.gap.gap as g
    
            #########           ######         ###########           ###  
         #############          ######         ############         ####  
        ##############         ########        #############       #####  
       ###############         ########        #####   ######      #####  
      ######         #         #########       #####    #####     ######  
     ######                   ##########       #####    #####    #######  
     #####                    ##### ####       #####   ######   ########  
     ####                    #####  #####      #############   ###  ####  
     #####     #######       ####    ####      ###########    ####  ####  
     #####     #######      #####    #####     ######        ####   ####  
     #####     #######      #####    #####     #####         #############
      #####      #####     ################    #####         #############
      ######     #####     ################    #####         #############
      ################    ##################   #####                ####  
       ###############    #####        #####   #####                ####  
         #############    #####        #####   #####                ####  
          #########      #####          #####  #####                ####  
                                                                          
     Information at:  http://www.gap-system.org
     Try '?help' for help. See also  '?copyright' and  '?authors'
    
   Loading the library. Please be patient, this may take a while.
GAP4, Version: 4.4.12 of 17-Dec-2008, i686-apple-darwin10.6.0-gcc
sage: a = g.libgap('0')
> status in GapElement()= 0
sage: b = g.libgap('10')
> status in GapElement()= 0
sage: a
calling READ_ERR at ViewObjVar0
output_buffer=0

0
sage: b
calling READ_ERR at ViewObjVar10
output_buffer=10

10
sage: a*b
calling READ_ERR at ViewObjVar0
output_buffer=0

0
sage: b/a
Rational operations: <divisor> must not be zero
not in any function
Entering break read-eval-print loop ...
you can 'quit;' to quit to outer loop, or
you can replace <divisor> via 'return <divisor>;' to continue
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/usr/local/src/sage/sage-4.6.1.rc0/spkg/standard/<ipython console> in <module>()

/usr/local/src/sage/current/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:11931)()

RuntimeError: ReadEvalDebug called!
sage: a*b
calling READ_ERR at ViewObjVar0
output_buffer=0

0
sage: b+b
calling READ_ERR at ViewObjVar20
output_buffer=20

20
sage: 
```

Dima


---

Comment by dimpase created at 2011-03-22 12:24:58

Replying to [comment:27 was]:
> From my memory of libGAP the GC and the large integer arithmetic are totally orthogonal/irrelevant.    I think working on libGAP whenever somebody has the interest (!) is a good idea, since it really will be a major, major plus for Sage when it starts working. 

I'll try to get access to GAP 4.5 for Sage as soon as possible.
As I understood from GAP people, their current GC is a major headache making it hard to write a "usual" library interface, 
which might be much nicer to have...
AFAIK, Bohm's GC is more manageable in this respect.  

Well, perhaps indeed the changes in 4.5 aren't that big to warrant putting this on old.


---

Comment by vbraun created at 2011-03-22 19:09:55

Updated patch


---

Attachment

Changes to the newest spkg:
 * removed dist directory
 * removed unsetting CC/CXX since "sage -sh" sets these to sane values
 * converted all copied files from patches/ into patches
 * using libtool to build libGAP
 * Code cleanups

Basic functionality now works including trapping errors:

```
sage: import sage.libs.gap.gap as g
sage: g.libgap('1/0')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1312, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/vbraun/opt/sage-4.7.alpha1/devel/sage-main/sage/libs/gap/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6816)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3254)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3157)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.Gap._element_constructor_ (sage/libs/gap/gap.c:4963)()
    684         """
    685         initialize_libgap()
--> 686         return self.element_class(self, x)
    687 
    688 

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.GapElement.__init__ (sage/libs/gap/gap.c:3047)()
    366         except RuntimeError, msg:
    367             ClearError()
--> 368             raise ValueError, 'Gap: '+str(msg)
    369 
    370         assert Symbol == S_SEMICOLON, 'Did not end with semicolon?'

ValueError: Gap: Rational operations: <divisor> must not be zero
```



---

Comment by vbraun created at 2011-03-23 01:38:38

See also: http://wiki.sagemath.org/days29/projects#libGAP


---

Comment by dimpase created at 2011-03-23 05:06:59

Replying to [comment:33 vbraun]:
> Changes to the newest spkg:
 Volker,
the spkg does not buid on MacOSX.
When building the library, I get

```
...
checking host system type... (cached) i686-apple-darwin10.6.0
configure: creating ./config.status
config.status: creating gac
config.status: creating Makefile
config.status: creating config.h
( cd bin/i686-apple-darwin10.6.0-gcc ; make CC='gcc' )
libtool --mode=compile gcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o ariths.o -c ../../src/ariths.c
libtool: unknown option character `-' in: --mode=compile
Usage: libtool -static [-] file [...] [-filelist listfile[,dirname]] [-arch_only arch] [-sacLT]
Usage: libtool -dynamic [-] file [...] [-filelist listfile[,dirname]] [-arch_only arch] [-o output] [-install_name name] [-compatibility_version #] [-current_version #] [-seg1addr 0x#] [-segs_read_only_addr 0x#] [-segs_read_write_addr 0x#] [-seg_addr_table <filename>] [-seg_addr_table_filename <file_system_path>] [-all_load] [-noall_load]
make[1]: *** [ariths.o] Error 1
make: *** [compile] Error 2
Error building GAP.
```



---

Comment by vbraun created at 2011-03-23 05:40:54

Hi Dima, Ivan Andrus already told me about the OSX issue and I'm pretty sure he'll fix it tomorrow. The problem is that OSX calls libtool `glibtool`.


---

Comment by vbraun created at 2011-03-23 05:49:57

Replying to [comment:9 was]:
> This log pretty much explains what/why/what next:


```
sage: import sage.libs.gap.gap as g
sage: a = g.libgap('10')
sage: a
10
sage: type(a)
<type 'sage.libs.gap.gap.GapElement'>
sage: a*a
100
sage: timeit('a*a')
625 loops, best of 3: 898 ns per loop
sage: b = gap('10')
sage: timeit('b*b')
125 loops, best of 3: 2.05 ms per loop
sage: a = g.libgap('0')
sage: a
0
sage: b = g.libgap('10')
sage: b/a
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/vbraun/opt/sage-4.7.alpha1/devel/sage-main/sage/libs/gap/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:12696)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.GapElement._div_ (sage/libs/gap/gap.c:4443)()
    613         except RuntimeError, msg:
    614             ClearError()
--> 615             raise ValueError, 'Gap: '+str(msg)
    616 
    617 

ValueError: Gap: Rational operations: <divisor> must not be zero
```


I'm currently adding code to access Gap containers, e.g.

```
sage: S4 = g.libgap('SymmetricGroup(4)')
sage: S4.List()
[ (), (1,4), (1,2,4), (1,3,4), (2,4), (1,4,2), (1,2), (1,3,4,2), (2,3,4), (1,4,2,3), (1,2,3), (1,3)(2,4), (3,4), (1,4,3), (1,2,4,3), (1,3), (2,4,3), (1,4,3,2), (1,2)(3,4), (1,3,2), (2,3), (1,4)(2,3), (1,2,3,4), (1,3,2,4) ]
sage: S4_elements = _
sage: type(S4_elements)
<type 'sage.libs.gap.gap.GapElement_List'>
sage: S4_elements[3]
(1,3,4)
sage: prod( g for g in S4_elements )
(1,3)(2,4)
```



---

Comment by iandrus created at 2011-03-23 19:21:13

I got it into a bad state:

```
sage: import sage.libs.gap.gap as g
sage: g.libgap('0')
0
sage: g.libgap('if 4>3 then\nPrint("hi");\nfi')
NULL
sage: g.libgap('if 4>3 thenPrint("hi");\nfi')
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

/Users/gvol/<ipython console> in <module>()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6816)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3254)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3157)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.Gap._element_constructor_ (sage/libs/gap/gap.c:6866)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.libgap_eval (sage/libs/gap/gap.c:2976)()

AssertionError: The return status of ReadEvalCommand must be zero.
sage: g.libgap('0')
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

/Users/gvol/<ipython console> in <module>()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6816)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3254)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3157)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.Gap._element_constructor_ (sage/libs/gap/gap.c:6866)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.libgap_eval (sage/libs/gap/gap.c:2976)()

AssertionError: The return status of ReadEvalCommand must be zero.
sage: 
```



---

Comment by dimpase created at 2011-03-24 01:38:16

Replying to [comment:38 iandrus]:

well, it works as it should in p6, so that's something that got in p7.
Indeed, with p6 I get

```
sage: gap('if 4>3 thenPrint("hi");\nfi')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/private/tmp/<ipython console> in <module>()

/usr/local/src/sage/current/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1093             
   1094         if isinstance(x, basestring):
-> 1095             return cls(self, x, name=name)
   1096         try:
   1097             return self._coerce_from_special_method(x)

/usr/local/src/sage/current/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1520             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1521                 self._session_number = -1
-> 1522                 raise TypeError, x
   1523         self._session_number = parent._session_number
   1524 

TypeError: Gap produced error output
Syntax error: expression expected
$sage3:=if 4>3 thenPrint("hi");fi;;
         ^

   executing $sage3:=if 4>3 thenPrint("hi");fi;;
```


which is basically how it should be: cf. sage: gap('if 4>3 then\nPrint("hi");\nfi')


---

Comment by dimpase created at 2011-03-24 01:41:09

Replying to [comment:39 dimpase]:

oops, no, sorry, please disregard my last comment; with p6 I also get something strange...


---

Comment by vbraun created at 2011-03-24 01:59:18

Updated version (both spkg and library patch) fixes this issue:

```
sage: import sage.libs.gap.gap as g
sage: g.libgap('0')
0
sage: g.libgap('if 4>3 then\nPrint("hi");\nfi')
NULL
sage: g.libgap('if 4>3 thenPrint("hi");\nfi')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1312, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/vbraun/opt/sage-4.7.alpha1/devel/sage-main/sage/libs/gap/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6816)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3254)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3157)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.Gap._element_constructor_ (sage/libs/gap/gap.c:6995)()
   1125         if not isinstance(x, str):
   1126             x = x._gap_init_()
-> 1127         return make_GapElement(self, libgap_eval(x))
   1128 
   1129 

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.libgap_eval (sage/libs/gap/gap.c:3034)()
    424     if status != STATUS_END:
    425         ClearError()
--> 426         raise ValueError, 'Not a normal statement.'
    427         return NULL
    428         

ValueError: Not a normal statement.
sage: g.libgap('0')
0
```

Also, I changed the libGAP memory allocation to not use `sbrk()`, now it runs under valgrind ;-)


---

Comment by vbraun created at 2011-03-24 19:52:25

The latest version of the libGAP patch now properly holds references to the GAP memory objects and releases them during `GapElement.__deref__`. No more random crashes because the GAP memory manager (GASMAN) recycles the Gap objects that Sage still references!

I feel this is now stable enough for wider testing. I can't crash it any more :-) Please give it a whirl and let me know if you manage to segfault it!


---

Comment by vbraun created at 2011-03-25 04:56:33

Newest version can convert various GAP datatypes back to Sage, for example cyclotomic numbers

```
sage: libgap('5/3 + 7*E(3)').sage()
7*zeta3 + 5/3
```

and permutations:

```
sage: generators = libgap.AlternatingGroup(4).GeneratorsOfGroup().sage()
sage: generators   # a Sage list of Sage permutations!
[(1,2,3), (2,3,4)]
sage: PermutationGroup(generators).cardinality()   # computed in Sage
12
sage: libgap.AlternatingGroup(4).Size()            # computed in GAP
12
```



---

Comment by dimpase created at 2011-03-25 05:04:57

Replying to [comment:44 vbraun]:
> Newest version can convert various GAP datatypes back to Sage, for example cyclotomic numbers
> {{{
> sage: libgap('5/3 + 7*E(3)').sage()
> 7*zeta3 + 5/3
> }}}
> and permutations:
> {{{
> sage: generators = libgap.AlternatingGroup(4).GeneratorsOfGroup().sage()
> sage: generators   # a Sage list of Sage permutations!
> [(1,2,3), (2,3,4)]
> sage: PermutationGroup(generators).cardinality()   # computed in Sage
> 12
> sage: libgap.AlternatingGroup(4).Size()            # computed in GAP
> 12
> }}}

This sounds  great! What about matrices? 
(it would be even better if there was a well-explained in docs implementation example of such a conversion).
E.g. for my work I need to convert GAP matrices (or non-standard sparse GAP matrices) into CVXOPT matrices.


---

Comment by was created at 2011-03-25 05:22:05

Hi  -- vbraun, this is amazing!  You are a genius.  W00t.


---

Comment by vbraun created at 2011-03-25 05:24:37

Replying to [comment:45 dimpase]:
> This sounds  great! What about matrices? 

If a dense matrix is good enough for you then you can just convert it to a List of Lists in Gap and then use the `.sage()` method which recurses through the lists and can convert numbers:

```
sage: from sage.libs.gap.libgap import libgap
sage: M = libgap('BlockMatrix([[1,1,[[1, 2],[ 3, 4]]], [1,2,[[9,10],[11,12]]], [2,2,[[5, 6],[ 7, 8]]]],2,2)')
sage: M
<block matrix of dimensions (2*2)x(2*2)>
sage: M.List().sage()
[[1, 2, 9, 10], [3, 4, 11, 12], [0, 0, 5, 6], [0, 0, 7, 8]]
sage: matrix(ZZ,_)
[ 1  2  9 10]
[ 3  4 11 12]
[ 0  0  5  6]
[ 0  0  7  8]
```



---

Comment by kcrisman created at 2011-03-25 15:57:10

When testing the sage/libs/gap/ directory, I get a number of errors in libgap.pyx only.   Most stuff passes, but it seems to handle errors differently.  See below for an example; every error is something analogous to this, though of course they look different depending on what error is raised instead of what is expected.

This is on Mac OS X 10.4 PPC.


```
File "/Users/student/Desktop/sage-4.6.2/devel/sage/sage/libs/gap/libgap.pyx", line 670:
    sage: libgap(1) / libgap('0')
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Gap: Rational operations: <divisor> must not be zero
Got:
    Traceback (most recent call last):
      File "/Users/student/Desktop/sage-4.6.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[7]>", line 1, in <module>
        libgap(Integer(1)) / libgap('0')###line 670:
    sage: libgap(1) / libgap('0')
      File "element.pyx", line 1549, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:11981)
    RuntimeError: Rational operations: <divisor> must not be zero
```


By the way, this needs some authors and reviewers in the list :)


---

Comment by dimpase created at 2011-03-25 16:34:30

Replying to [comment:48 kcrisman]:
> When testing the sage/libs/gap/ directory, I get a number of errors in libgap.pyx only.   Most stuff passes, but it seems to handle errors differently.  See below for an example; every error is something analogous to this, though of course they look different depending on what error is raised instead of what is expected.
> 
> This is on Mac OS X 10.4 PPC.
> 


```
 File "/Users/student/Desktop/sage-4.6.2/devel/sage/sage/libs/gap/libgap.pyx", line 670:
     sage: libgap(1) / libgap('0')
```


I expect that this is caught by Sage itself rather than by GAP (Sage recognizes that an illegal division is going to happen).

[...]

> By the way, this needs some authors and reviewers in the list :)

I added some authors, in alphabetical order--–don't know if this is a complete list.


---

Comment by vbraun created at 2011-03-25 16:40:10

No, `libgap(1) / libgap('0')` is evaluated in GAP and raises an error in GAP. We injected an `abort()` in the GAP code, so the `sig_on()`/`sig_off()` block catches it as `RuntimeError`. The `GapElement._div_` method should catch the `RuntimeError` and re-raise it as `ValueError`. This works for me (all doctests pass on Fedora 14 x86_64). Are you using the newest version of `trac_6391_libGAP.patch`?


---

Comment by iandrus created at 2011-03-25 17:08:28

Assuming you do not have the GAP small group database installed, then running

```
sage: import sage.libs.gap.gap as g
sage: g.libgap('SmallGroup(12,3)')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/gvol/SageStuff/gap-4.4.12.p7/src/<ipython console> in <module>()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6816)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3254)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3157)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.Gap._element_constructor_ (sage/libs/gap/gap.c:7237)()

/Users/gvol/vcs/cur-sage/local/lib/python2.6/site-packages/sage/libs/gap/gap.so in sage.libs.gap.gap.libgap_eval (sage/libs/gap/gap.c:3005)()

ValueError: Gap: Aborted
```


The error message could be a bit more helpful, but  when runnning under `sage --valgrind` it leads to a segfault.


---

Comment by kcrisman created at 2011-03-25 18:52:26

Replying to [comment:50 vbraun]:
> No, `libgap(1) / libgap('0')` is evaluated in GAP and raises an error in GAP. We injected an `abort()` in the GAP code, so the `sig_on()`/`sig_off()` block catches it as `RuntimeError`. The `GapElement._div_` method should catch the `RuntimeError` and re-raise it as `ValueError`. This works for me (all doctests pass on Fedora 14 x86_64). Are you using the newest version of `trac_6391_libGAP.patch`?
I think so.

```
sage: hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6391/trac_6391_libGAP.patch')
```

is how I imported it, then `./sage -br`.  Like I said, it passes everything else in that directory.  (I haven't done other tests because it takes a loooong time.)

That part seems to have first shown in in the .2.patch.  It didn't get cancelled in the going back to just .patch, did it?


---

Comment by vbraun created at 2011-03-25 19:24:47

Replying to [comment:52 kcrisman]:
> That part seems to have first shown in in the .2.patch.  It didn't get cancelled in the going back to just .patch, did it?  

The patches are not cummulative. You need to back out old versions before applying the newest one.


---

Comment by kcrisman created at 2011-03-25 19:34:20

Replying to [comment:53 vbraun]:
> Replying to [comment:52 kcrisman]:
> > That part seems to have first shown in in the .2.patch.  It didn't get cancelled in the going back to just .patch, did it?  
> 
> The patches are not cummulative. You need to back out old versions before applying the newest one.

I only applied this most recent one.  I was just wondering whether somehow I should have applied the .2.patch.  But I don't think this is the issue.

Interestingly, I get long hangs, so I think you may be right that I'm somehow missing the !sig_on stuff.  But

```
        try:            sig_on()            result = make_GapElement(self.parent(),                                     DIFF(self.value, (<GapElement>right).value))            sig_off()            return result        except RuntimeError, msg:            ClearError()            raise ValueError, 'Gap: '+str(msg)
```

is what I get for the code of `g1._sub_??`.

But I did get this scary thing:

```
sage: libgap(1)
/Users/student/Desktop/sage-4.6.2/local/bin/sage-sage: line 308: 14591 Abort trap              sage-ipython "$@" -i
```

Could this is another example of using the wrong !MAC_OSX_DEPLOYMENT_TARGET or something, like it was for the initial problems with 10.6 not working... ?  Maybe that's impossible.


---

Comment by kcrisman created at 2011-03-25 20:10:58

This also seems to be a strangely formed spkg. All that is in it is a folder called gap-4.4.12.p7, which is not the usual practice.  Where is src/, spkg-install, etc?


---

Comment by vbraun created at 2011-03-25 21:29:58

The libGAP requires Sage-4.7.alpha1 or later because it uses the new signal handling stuff that Jeroen just merged. I saw you use 4.6.2, so that explains why the exceptions are not caught correctly. The spkg has the normal layout, not sure what you are doing wrong. It is not bzip2-compressed since that is faster to test, seems like you are not unpacking it correctly.


---

Comment by kcrisman created at 2011-03-26 01:55:32

Replying to [comment:56 vbraun]:
> The libGAP requires Sage-4.7.alpha1 or later because it uses the new signal handling stuff that Jeroen just merged. I saw you use 4.6.2, so that explains why the exceptions are not caught correctly. 
Great, that clarifies that.
>The spkg has the normal layout, not sure what you are doing wrong. It is not bzip2-compressed since that is faster to test, seems like you are not unpacking it correctly.
This is hilarious - my Macs interpret the file ending `.p7` as a cryptographic file.  Removing that makes all well.

Sounds like you are all well on the way to solving this - another nice addition!


---

Attachment

Updated patch


---

Comment by vbraun created at 2011-03-26 18:58:19

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2011-03-26 18:58:19

The updated gap-4.4.12.p8 now contains a separate `libgap/` directory with a copy of the gap kernel sources and new autoconf scripts that can actually build a shared library on Solaris. 

While this layout is probably not the final word in how to build libgap, I think its good enough to test it on a wider audience. Once we are confident that it works well we should contact upstream and find out in how far they are willing to add shared library support. Ready for review!


---

Comment by vbraun created at 2011-03-26 19:11:20

libgap interface header (for review purposes only)


---

Attachment

Replying to [comment:59 vbraun]:
> The updated gap-4.4.12.p8 now contains a separate `libgap/` directory with a copy of the gap kernel sources and new autoconf scripts that can actually build a shared library on Solaris. 
> 
> While this layout is probably not the final word in how to build libgap, I think its good enough to test it on a wider audience. Once we are confident that it works well we should contact upstream and find out in how far they are willing to add shared library support. Ready for review!

Hi Volker, you mentioned adding doctests etc.
Do you mean for the low-level stuff in gap.pyx ? 

Did you try completely replacing gap interface with libgap interface?
IMHO it's about time to start doing this --- this would uncover more  things to do, I imagine.

It would be great is libgap/ contained at least one C example on building a C application that links against libGAP and does something, like computing the order of a permutation group. Would be good for stress-testing, and just understanding the
interface better.
Anyone out there who has time for this now? (not me :-( ) I imagine it's more work on a makefile than on the C side.

Regarding Sage-libGAP  interface, I would like to understand what happens in a scenario when a Python object P holds
a reference to a GAP object G, and then P gets GC'ed. This should result in G getting freed (eventually) by GAP's GC.
It would be good to see an evidence that this actually does happen.

Did you check that things work with GAP workspaces (Saving/Loading workspaces, that is)?


---

Comment by vbraun created at 2011-03-27 13:48:15

Hi Dima,

Yes everything in `libgap.pyx` is doctested. I have't tried to replace gap by libgap in the Sage library, first I want to see if the new spkg compiles on all supported platforms. But p8 uses the standard autotools to build the shared library, so I'm pretty confident.

There is a subdirectory `sage/libs/gap/test` that contains a small C program for testing purposes just like what you want.

Getting garbage collection in Gap work to work correctly was one of the major issues that I worked on over the week. For starters, Gasman has no explicit reference counts. It is also compacting, so we must never hold direct pointers into the memory. The way it works is that 
  1. `libgap.pyx` first creates a new Gap global variable `libgap_owned_objects` and assigns an empty `rec()` to it.
  1. Every Python `GapElement` adds is wrapped Gap object to `libgap_owned_objects`.
  1. The `GapElement.__dealloc__` removes the Gap object from `libgap_owned_objects`. It is then no longer referenced inside Gap and Gasman eventually recycles the object.
This is doctested in the `__dealloc__` documentation.

I haven't tried saving/loading Gap workspaces. But it doesn't make much sense in libGAP since it would break the Python<->Gap object relations. If you need to load a huge pre-evaluated Gap script then you probably don't need libGAP, which is all about fast interaction with Gap.


---

Comment by dimpase created at 2011-03-27 15:11:28

Replying to [comment:61 vbraun]:


> 
> I haven't tried saving/loading Gap workspaces. But it doesn't make much sense in libGAP since it would break the Python<->Gap object relations. If you need to load a huge pre-evaluated Gap script then you probably don't need libGAP, which is all about fast interaction with Gap.

At least the initialization of libGAP should probably use a prebuilt workspace, as is done by the current interface.
The reason is to speed it up. 

Even with Python<-> GAP relations lost, saving workspace might still make sense (if you know the GAP names of objects
created, you can get them, right?).
And I don't see why it is really lost, as is it recorded in Gap global variable libgap_owned_objects. 
Which would make it possible to re-create the corresponding Python's `GapElement` data.


---

Comment by vbraun created at 2011-03-27 15:53:59

During the libgGAP initialization you can pass any command line arguments to GAP, so we can easily load a workspace. Note that Gap initialization happens the first time you use libGAP, so it does not add to the Sage startup time.  

Its true that one could recreate the `GapElement`s from a saved/loaded workspace (though you lose the Python variable names), but it still doesn't seem to be the most pressing issue right now.


---

Comment by dimpase created at 2011-03-27 16:31:02

Replying to [comment:63 vbraun]:
> During the libgGAP initialization you can pass any command line arguments to GAP, so we can easily load a workspace. Note that Gap initialization happens the first time you use libGAP, so it does not add to the Sage startup time.  

OK, but it does add to libGAP startup time.

> 
> Its true that one could recreate the `GapElement`s from a saved/loaded workspace (though you lose the Python variable names), but it still doesn't seem to be the most pressing issue right now.

I certainly agree with this.


---

Comment by was created at 2011-05-20 18:15:17

A relevant status update and overview from Volker:

Hi Stephen,

I wanted to contact you for a while about whether and how to integrate
the C GAP library interface that we wrote. I think it would be great
to have a well-defined shared library interface, and it sounds like
you are interested in that as well. We have a working prototype at
http://trac.sagemath.org/sage_trac/ticket/6391 that just needs review
as far as I am concerned. It doesn't have a nicely abstracted
interface, but it works for Sage purposes. Let me comment on the
points in your pdf:

1) IO: we want to inject input and catch output, so we can evaluate
input strings and parse output strings. For this, we just patched
SyFgets() / PutChrTo().

2) For errors, just send a signal from the shared library. We patched
ReadEvalError() to call abort(). The user of the shared library can
then install their own signal handler if they want to catch that. I
don't think entering the break/eval loop is particularly useful in a
shared library, we just set BreakOnError = 0.

3) similarly, if the user of the library wants to interrupt a GAP
computation she can just signal SIGINT etc.

4) To keep objects alive, the Sage library interface just creates a
global GAP record (which aren't garbage collected)

   libgap_owned_objects = GVarName( "libgap_owned_objects" );
   AssGVar(libgap_owned_objects, NEW_PREC(0))

and then references any objects that are wrapped by libGAP:

   libgap_owned_objects_counter += 1
   self.libgap_owned_objects_rnam = RNamIntg(libgap_owned_objects_counter)
   AssPRec(VAL_GVAR(libgap_owned_objects),
       self.libgap_owned_objects_rnam, self.value)

For simplicity we implemented this in Cython, but that should probably
be moved in the C library interface.

5) Memory management: I replaced the sbrk with a malloc'ed workspace.
Added advantage: you can then use valgrind. I think valgrind disallows
large sbrk() calls to force the libc malloc implementation to avoid
it. For now, the libGAP workspace size has to be fixed at
initialization. This isn't ideal but Dima thought that you have some
long-term plans for switching to a different garbage collector. Maybe
you can tell us more about that.

6) We didn't hit any name collisions in Sage, so its not an urgent
issue. I agree that eventually only the relevant symbols should be
exported by the shared library but GAP generally uses less common
names. Most C code doesn't use [CamelCase](CamelCase), for starters.

7) I haven't tried loading modules from within libGAP.

8) I didn't encounter any problems with GMP. Sage uses MPIR.

In any case, I'm very interested in getting a library implementation
upstream and can help with that. I'm currently travelling around for
conferences and will be back in DIAS in Dublin for more than a couple
of days starting in August.

Best wishes,
Volker


---

Comment by was created at 2011-06-17 01:45:17

Needs work?


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: import sage.libs.gap.all
sage: a = sage.libs.gap.all.libgap(2)
sage: a + a
4
sage: timeit('a+a', number=10^6)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (27, 0))
| Sage Version 4.7, Release Date: 2011-05-17                         |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/tmp/wstein/sage-4.7/devel/sage-main/<ipython console> in <module>()

/tmp/wstein/sage-4.7/local/lib/python2.6/site-packages/sage/misc/sage_timeit_class.so in sage.misc.sage_timeit_class.SageTimeit.__call__ (sage/misc/sage_timeit_class.c:744)()

/tmp/wstein/sage-4.7/local/lib/python2.6/site-packages/sage/misc/sage_timeit_class.so in sage.misc.sage_timeit_class.SageTimeit.eval (sage/misc/sage_timeit_class.c:605)()

/tmp/wstein/sage-4.7/local/lib/python2.6/site-packages/sage/misc/sage_timeit.pyc in sage_timeit(stmt, globals, preparse, number, repeat, precision)
    182                     break
    183 
--> 184         best = min(timer.repeat(repeat, number)) / number
    185 
    186     finally:

/tmp/wstein/sage-4.7/local/lib/python/timeit.pyc in repeat(self, repeat, number)
    218         r = []
    219         for i in range(repeat):
--> 220             t = self.timeit(number)
    221             r.append(t)
    222         return r

/tmp/wstein/sage-4.7/local/lib/python/timeit.pyc in timeit(self, number)
    191         gcold = gc.isenabled()
    192         gc.disable()
--> 193         timing = self.inner(it, self.timer)
    194         if gcold:
    195             gc.enable()

/tmp/wstein/sage-4.7/devel/sage-main/<magic-timeit> in inner(_it, _timer)

/tmp/wstein/sage-4.7/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11367)()

/tmp/wstein/sage-4.7/local/lib/python2.6/site-packages/sage/libs/gap/libgap.so in sage.libs.gap.libgap.GapElement._add_ (sage/libs/gap/libgap.c:4381)()

ValueError: Gap: Exhausted the GAP memory pool.
```



---

Comment by was created at 2011-06-17 01:45:17

Changing status from needs_review to needs_work.


---

Comment by was created at 2011-07-19 23:22:51

PING:   Should we try to get a very experimental version of libGAP in that has memory leaks?  Seems worrisome...?


---

Comment by mmarco created at 2012-05-13 22:04:36

I have been trying to make my free groups/finitely presented groups (see #12339) wraper with libgap, and in general it works fine (and an impressive speed, i must say). There are some random segfauls though. And i have run into a problem that can be traced down to:





```
sage: from sage.libs.gap.all import libgap
sage: F=libgap('FreeGroup(2)')
sage: lis=libgap('[]')
sage: (a,b)=F.GeneratorsOfGroup()
sage: lis.Add(a^2)
sage: lis.Add(b^2)
sage: lis.Add(a*b*a*b)
sage: lis
[ f1^2, f2^2, f1*f2*f1*f2 ]
sage: H=F/lis
sage: H
<fp group on the generators [ f1, f2 ]>
sage: H.IsomorphismSimplifiedFpGroup()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/mmarco/sage-4.7.2/<ipython console> in <module>()

/home/mmarco/sage-4.7.2/local/lib/python2.6/site-packages/sage/libs/gap/libgap.so in sage.libs.gap.libgap.GapElement_MethodProxy.__call__ (sage/libs/gap/libgap.c:7643)()

/home/mmarco/sage-4.7.2/local/lib/python2.6/site-packages/sage/libs/gap/libgap.so in sage.libs.gap.libgap.GapElement_Function.__call__ (sage/libs/gap/libgap.c:7259)()

ValueError: Gap: Aborted
```



---

Attachment

Updated patch


---

Comment by vbraun created at 2012-08-30 11:28:39

The libgap doctests pass now. Also, mmarco's example works:

```
sage: F = libgap.FreeGroup(2)
sage: a,b = F.GeneratorsOfGroup()
sage: lis = libgap('[]')
sage: lis.Add(a^2)
sage: lis.Add(b^2)
sage: lis.Add(a*b*a*b)
sage: lis
[ f1^2, f2^2, f1*f2*f1*f2 ]
sage: H=F/lis
sage: H
<fp group on the generators [ f1, f2 ]>
sage: H.IsomorphismSimplifiedFpGroup()
[ f1, f2 ] -> [ f1, f2 ]
```

William's `timeit('a+a', number=10^6)` also works. If you have any interest in libGAP please try it out **this week** and let me know if you find any bugs, then I can investigate them during the rest of this week...


---

Comment by mmarco created at 2012-08-30 16:51:35

I am running some tests with it. It seems to work fine, except for a few random segfaults (much less than before) I cannot reproduce them.

I will run some more tests, but so far, it looks great.

Is it possible to fix the memory limit for the gap session?


---

Comment by vbraun created at 2012-08-30 17:56:48

What do you mean by "fix memory limit"? The absolute limit is fixed. But we can increase the memory limit to be very large on 64-bit, it will only be virtual and not actually used. On 32-bit it will hurt that it counts against the 4GB process limit.


---

Comment by mmarco created at 2012-08-30 18:20:09

What i mean is the amount of memory that the gap session can use (which is determined by the -o option). I have noticed that libgap handles this question in a different way than the classical pexpect interface.

Before, if i run a computaqtion that took too much memory in gap, the gap session would eventually be killed (because it is run with the option -o 9999G) by the system, leaving orphaned all the sage objects that interfaced objects in that session.

I have noticed that with this interface it just returns an error, but the objects are not orphaned. This error is returned before all the system memory is exhausted. So i wonder how much memory is used before the error is issued, and how is all this handled.


---

Comment by vbraun created at 2012-08-30 18:45:30

The gap command line options that are used for setting up libgap can easily be changed. Right now its pretty small, I know. 

If you have any random segfaults can you post your code? I can still debug it even if it is not reproducable.


---

Comment by mmarco created at 2012-08-30 23:26:00

I think it would be best if the memory limit would be set automatically deppending on the available RAM in the system.

I just got a segfault playing with a modified version of my patch for finitely presented groups:


```
F=FreeGroup(3)
F.inject_variables()
Defining x0, x1, x2
G=F.quotient([x0^2,x1^2,x2^2,(x0*x1)^3,(x1*x2)^3,(x0*x2)^2])
G.inject_variables()
Defining x0, x1, x2
sage: g=G.gap()
sage: g
<fp group of size 24 on the generators [ x0, x1, x2 ]>
sage: x=x0.gap()
sage: x.Order()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/mmarco/sage-5.2/<ipython console> in <module>()

/home/mmarco/sage-5.2/local/lib/python2.7/site-packages/sage/libs/gap/libgap.so in sage.libs.gap.libgap.GapElement_MethodProxy.__call__ (sage/libs/gap/libgap.c:8449)()

/home/mmarco/sage-5.2/local/lib/python2.7/site-packages/sage/libs/gap/libgap.so in sage.libs.gap.libgap.GapElement_Function.__call__ (sage/libs/gap/libgap.c:8037)()

ValueError: libGAP: Segmentation fault
```


I can send you the whole file with the definition of the classes for G and x0, but i don't think it would give any useful information here: g is just a finitely presented group object of the ligbap interface, and x is one of its generators.

I couldn't reproduce the error.


---

Comment by mmarco created at 2012-08-30 23:41:22

Another comment (i am not sure if itshould be fixed or if it is my fault): the testuite of my classes fails because comparison bewteen objects of this interface is not implemented. It works for the old interface though.


---

Comment by vbraun created at 2012-08-31 00:13:54

Comparison isn't implemented yet. 

If the error is not reproducible try to run it ~100 times to see if it crashes occasionally. And/or run it on another architecture.


---

Comment by mmarco created at 2012-08-31 00:31:13

Ok, i have tried to isolate the issue and run it in a loop to reproduce it. It is not easy to catch, but every few thousand iterations it fails:


```
sage: g=libgap('FreeGroup(2)')
sage: (a,b)=g.GeneratorsOfGroup()
sage: lis=libgap('[]')
sage: lis.Add(a^2)    
sage: lis.Add(b^2)    
sage: lis.Add(b*a)                          
sage: h=g/lis
sage: c=h.GeneratorsOfGroup()[0]
sage: for i in range(3000):^J    n=c.Order()
....:     
sage: for i in range(3000):^J    n=c.Order()
....:     
sage: for i in range(3000):^J    n=c.Order()
....:     
sage: for i in range(3000):^J    n=c.Order()
....:     
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/mmarco/sage-5.2/<ipython console> in <module>()

/home/mmarco/sage-5.2/local/lib/python2.7/site-packages/sage/libs/gap/libgap.so in sage.libs.gap.libgap.GapElement_MethodProxy.__call__ (sage/libs/gap/libgap.c:8449)()

/home/mmarco/sage-5.2/local/lib/python2.7/site-packages/sage/libs/gap/libgap.so in sage.libs.gap.libgap.GapElement_Function.__call__ (sage/libs/gap/libgap.c:8037)()

ValueError: libGAP: Error, no method found! For debugging hints type ?Recovery from NoMethodFound
Error, no 1st choice method found for `CallFuncList' on 2 arguments
```


I am not sure if it is the same problem though. The error message is different.


---

Comment by mmarco created at 2012-08-31 18:18:28

problem persists with the new patch.


---

Comment by vbraun created at 2012-09-03 16:28:00

I've fixed Miguel's bug and tested that libGAP remains running through hundreds of GAP garbage collections. All in all, I have not had any random crashes with the new version at all even in hundreds of repetitions. So I declare the current state to be totally awesome and ready to be released into the wild and exposed to the general Sage community. Please review!


---

Comment by vbraun created at 2012-09-03 16:28:00

Changing component from interfaces to group theory.


---

Comment by vbraun created at 2012-09-03 16:28:00

Changing status from needs_work to needs_review.


---

Comment by mmarco created at 2012-09-03 20:00:18

Problem persists for me. Not in a 3000 iterations loop, but in longer loops:


```
sage: g=libgap('FreeGroup(2)')                    
sage: (a,b)=g.GeneratorsOfGroup()
sage: lis=libgap('[]')
sage: lis.Add(a^2)    
sage: lis.Add(b^2)    
sage: lis.Add(b*a)    
sage: h=g/lis                                                                                              
sage: c=h.GeneratorsOfGroup()[0]
sage: for i in range(300000):                 
....:     n=c.Order()
....:     
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/mmarco/sage-5.2/<ipython console> in <module>()

/home/mmarco/sage-5.2/local/lib/python2.7/site-packages/sage/libs/gap/element.so in sage.libs.gap.element.GapElement_MethodProxy.__call__ (sage/libs/gap/element.c:7860)()

/home/mmarco/sage-5.2/local/lib/python2.7/site-packages/sage/libs/gap/element.so in sage.libs.gap.element.GapElement_Function.__call__ (sage/libs/gap/element.c:7433)()

ValueError: libGAP: Error, no method found! For debugging hints type ?Recovery from NoMethodFound
Error, no 1st choice method found for `CallFuncList' on 2 arguments

sage: i
6862
```



---

Comment by vbraun created at 2012-09-06 12:26:22

After considerable despair I finally realized that Python called the libgap initialization from a higher stack frame than where `c.Order()` was executing. One peculiarities of the GAP memory manager is that it trawls the stack for pointers into its memory pool and keeps these alive (so you can just work with local stack-allocated GAP objects and not worry). While its easy to figure out the highest stack frame (its you, the currently executing function) we must take care to inform GAP about the lowest stack frame that can hold a pointer to a memory bag!

Now Miguel's example runs perfectly! For the record, you can use the following syntactic sugar to make the code look nicer:

```
    sage: G =libgap.FreeGroup(2)
    sage: a,b = G.GeneratorsOfGroup()
    sage: rel = libgap([a^2, b^2, a*b*a*b])
    sage: H = G / rel
    sage: c = H.GeneratorsOfGroup()[0]
    sage: for i in range(300000):
    ...       n = c.Order()
```



---

Comment by mmarco created at 2012-09-06 13:01:04

x86 means x86_64 also?


---

Comment by vbraun created at 2012-09-06 13:20:18

Yes, anything with an esp/ebp register (I'll add support for the rest later).


---

Comment by mmarco created at 2012-09-06 16:37:18

I guess i am missing something, but that's what i get with the new patch:


```
sage: g=libgap('FreeGroup(2)')
gap: halfing pool size.
sage: (a,b)=g.GeneratorsOfGroup()
sage: h=g/libgap([a^2,b^2,a*b])       
sage: h
<fp group on the generators [ f1, f2 ]>
sage: x=h.GeneratorsOfGroup()[0]
sage: x
f1
sage: x^2
f1^2
sage: x^3
f1^3
sage: x.Order()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/mmarco/sage-5.2/<ipython console> in <module>()

/home/mmarco/sage-5.2/local/lib/python2.7/site-packages/sage/libs/gap/element.so in sage.libs.gap.element.GapElement_MethodProxy.__call__ (sage/libs/gap/element.c:8003)()

/home/mmarco/sage-5.2/local/lib/python2.7/site-packages/sage/libs/gap/element.so in sage.libs.gap.element.GapElement_Function.__call__ (sage/libs/gap/element.c:7576)()

ValueError: libGAP: Segmentation fault

```



---

Comment by nbruin created at 2012-09-06 17:54:30

Great work! I noticed one thing in keeping references in `owned_objects`. The way I read the code, it's a list that any new object gets appended to (and index is stored). Upon deletion of the sage wrapper of the object, the particular location in the `owned_objects` list is unbound. Doesn't that mean that the owned_object list can grow in an unbounded way even when only a bounded number of references to gap_objects is held? i.e., wouldn't something like

```
i = 0
a = GapElement(i)
while True:
    i+=1
    b = a
    a = GapElement(i)
```

let memory balloon?
For ecllib I ended up keeping a doubly linked list, since insertions and deletions are O(1), at the cost of a largish constant in memory overhead.

Alternatives include inserting in the first unbound spot of the list, which has the wrong complexity for object creation unless you keep a free list. You could keep a stack or a deque of free spots. I don't know if a FIFO or LIFO strategy would lead to better opportunities to shorten the reference list.


---

Comment by vbraun created at 2012-09-06 18:06:35

Miguel: the "halfing pool size" means that GAP can't allocate its 4gb pool (or so). I suppose thats the issue here, will try to investigate.

Nils: I know, though it is only a pointer... Originally I was using GAP records (dictionaries/hashes), but back then I didn't understand some of the subtle points of how GAP works with them so I replaced it with the simplest possibility. I'm actually thinking that the best solution would be to add a hook to the garbage collector so we can directly force objects alive.


---

Comment by mmarco created at 2012-09-06 18:13:55

It's strange, since i have plenty of RAM available.


---

Comment by vbraun created at 2012-09-07 21:25:59

I can manually force the "halfing pool size" message by limiting the virtual mem size (in the followng example to 5gb which is a bit more than half of what GAP wants to take on x86 --- note that this is purely virtual and not used unless you actually do a huge computation)

```
[vbraun@volker-desktop ~]$ ulimit -v 5000000
[vbraun@volker-desktop ~]$ sage -c 'print libgap(1)'
gap: halfing pool size.
1
```

Though still all doctests pass and I don't see Miguel's segfault. Can you post a backtrace? (`sage -gdb` and type 'bt' at the gdb prompt after the segfault)


---

Comment by mmarco created at 2012-09-08 01:43:40


```
mmarco@neumann ~/sage-5.2 $ ./sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
/home/mmarco/sage-5.2/local/bin/sage-ipython
GNU gdb (Gentoo 7.3.1 p2) 7.3.1
Copyright (C) 2011 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
For bug reporting instructions, please see:
<http://bugs.gentoo.org/>...
Reading symbols from /home/mmarco/sage-5.2/local/bin/python...done.
[Thread debugging using libthread_db enabled]
Python 2.7.3 (default, Aug 30 2012, 14:13:06) 
[GCC 4.5.4] on linux2
Type "help", "copyright", "credits" or "license" for more information.
| Sage Version 5.2, Release Date: 2012-07-25                         |
| Type "notebook()" for the browser-based notebook interface.        |
| Type "help()" for help.                                            |
Loading Sage library. Current Mercurial branch is: libgap4
sage: 
sage: g=libgap('FreeGroup(2)')
sage: (a,b)=g.GeneratorsOfGroup()
sage: h=g/libgap([a^2,b^2,a*b])
sage: x=h.GeneratorsOfGroup()[0]
sage: x.Order()

Program received signal SIGSEGV, Segmentation fault.
0x00007fffcb4d15c5 in libGAP_GenStackFuncBags () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
(gdb) bt
#0  0x00007fffcb4d15c5 in libGAP_GenStackFuncBags () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#1  0x00007fffcb4d1c2f in libGAP_CollectBags () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#2  0x00007fffcb4d0fda in libGAP_NewBag () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#3  0x00007fffcb4412df in libGAP_SwitchToNewLvars () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#4  0x00007fffcb447ea9 in libGAP_DoExecFunc2args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#5  0x00007fffcb445555 in libGAP_EvalFunccall2args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#6  0x00007fffcb34c9c4 in libGAP_ExecAssLVar () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#7  0x00007fffcb45f8b1 in libGAP_ExecSeqStat4 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#8  0x00007fffcb460a61 in libGAP_ExecFor () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#9  0x00007fffcb46366d in libGAP_ExecRepeat2 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#10 0x00007fffcb45f56a in libGAP_ExecSeqStat () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#11 0x00007fffcb460151 in libGAP_ExecIf () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#12 0x00007fffcb460a61 in libGAP_ExecFor () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#13 0x00007fffcb45f56a in libGAP_ExecSeqStat () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#14 0x00007fffcb4634e8 in libGAP_ExecRepeat () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#15 0x00007fffcb45fd27 in libGAP_ExecSeqStat6 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#16 0x00007fffcb460151 in libGAP_ExecIf () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#17 0x00007fffcb45f56a in libGAP_ExecSeqStat () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#18 0x00007fffcb46006d in libGAP_ExecSeqStat7 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#19 0x00007fffcb447e08 in libGAP_DoExecFunc1args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#20 0x00007fffcb359b16 in libGAP_DoWrap1args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#21 0x00007fffcb445067 in libGAP_EvalFunccall1args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#22 0x00007fffcb34ccf8 in libGAP_ExecAssLVar02 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#23 0x00007fffcb460567 in libGAP_ExecIfElifElse () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#24 0x00007fffcb45fcbb in libGAP_ExecSeqStat6 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#25 0x00007fffcb447e08 in libGAP_DoExecFunc1args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#26 0x00007fffcb41ac00 in libGAP_DoOperation1Args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#27 0x00007fffcb422ad4 in libGAP_DoAttribute () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#28 0x00007fffcb445067 in libGAP_EvalFunccall1args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#29 0x00007fffcb3ec5cb in libGAP_EvalNe () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#30 0x00007fffcb46049d in libGAP_ExecIfElifElse () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#31 0x00007fffcb45f5eb in libGAP_ExecSeqStat2 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#32 0x00007fffcb447e08 in libGAP_DoExecFunc1args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#33 0x00007fffcb41ac00 in libGAP_DoOperation1Args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#34 0x00007fffcb422ad4 in libGAP_DoAttribute () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#35 0x00007fffcb445067 in libGAP_EvalFunccall1args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#36 0x00007fffcb4451e3 in libGAP_EvalFunccall2args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#37 0x00007fffcb464adf in libGAP_ExecReturnObj () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#38 0x00007fffcb45f654 in libGAP_ExecSeqStat2 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#39 0x00007fffcb447f0b in libGAP_DoExecFunc2args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#40 0x00007fffcb41afe0 in libGAP_DoOperation2Args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#41 0x00007fffcb2e792c in libGAP_EqObject () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#42 0x00007fffcb3ec77b in libGAP_EvalNe () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#43 0x00007fffcb463257 in libGAP_ExecWhile2 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#44 0x00007fffcb460004 in libGAP_ExecSeqStat7 () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#45 0x00007fffcb447e08 in libGAP_DoExecFunc1args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#46 0x00007fffcb41ac00 in libGAP_DoOperation1Args () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#47 0x00007fffcb422ad4 in libGAP_DoAttribute () from /home/mmarco/sage-5.2/local/lib/libgap.so.0
#48 0x00007fffcb074e7d in __pyx_pf_4sage_4libs_3gap_7element_19GapElement_Function_2__call__ (__pyx_v_self=0x49651b0, __pyx_v_args=0x7ffff7ed4f50) at sage/libs/gap/element.c:7201
#49 0x00007fffcb0763a8 in __pyx_pw_4sage_4libs_3gap_7element_19GapElement_Function_3__call__ (__pyx_v_self=0x49651b0, __pyx_args=0x7ffff7ed4f50, __pyx_kwds=<optimized out>) at sage/libs/gap/element.c:6998
#50 0x00007ffff7a41913 in PyObject_Call (func=0x494de90, arg=<optimized out>, kw=<optimized out>) at Objects/abstract.c:2529
#51 0x00007ffff7ae7c57 in PyEval_CallObjectWithKeywords (func=0x494de90, arg=0x7ffff7ed4f50, kw=<optimized out>) at Python/ceval.c:3890
#52 0x00007ffff7a5ce2b in wrapperdescr_call (descr=<optimized out>, args=0x7ffff7ed4f50, kwds=0x0) at Objects/descrobject.c:306
#53 0x00007ffff7a41913 in PyObject_Call (func=0x3287b40, arg=<optimized out>, kw=<optimized out>) at Objects/abstract.c:2529
#54 0x00007fffcb06af0d in __pyx_pf_4sage_4libs_3gap_7element_22GapElement_MethodProxy___call__ (__pyx_v_args=0x7ffff7f78050, __pyx_v_self=0x49651b0) at sage/libs/gap/element.c:8003
#55 __pyx_pw_4sage_4libs_3gap_7element_22GapElement_MethodProxy_1__call__ (__pyx_v_self=0x49651b0, __pyx_args=0x7ffff7f78050, __pyx_kwds=<optimized out>) at sage/libs/gap/element.c:7895
#56 0x00007ffff7a41913 in PyObject_Call (func=0x49651b0, arg=<optimized out>, kw=<optimized out>) at Objects/abstract.c:2529
#57 0x00007ffff7aed0ee in do_call (nk=<optimized out>, na=<optimized out>, pp_stack=0x7fffffffbff0, func=0x49651b0) at Python/ceval.c:4239
#58 call_function (oparg=<optimized out>, pp_stack=0x7fffffffbff0) at Python/ceval.c:4044
#59 PyEval_EvalFrameEx (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:2666
#60 0x00007ffff7aef63d in PyEval_EvalCodeEx (co=0x4953830, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:3253
#61 0x00007ffff7aef762 in PyEval_EvalCode (co=<optimized out>, globals=<optimized out>, locals=<optimized out>) at Python/ceval.c:667
#62 0x00007ffff7aeeb83 in exec_statement (locals=0xbc3c80, globals=0xbc3c80, prog=<optimized out>, f=0x4438bd0) at Python/ceval.c:4718
#63 PyEval_EvalFrameEx (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:1880
#64 0x00007ffff7aef63d in PyEval_EvalCodeEx (co=0xaed9b0, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=2, kws=0x4998780, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:3253
#65 0x00007ffff7aed777 in fast_function (nk=<optimized out>, na=2, n=<optimized out>, pp_stack=0x7fffffffc460, func=0xb7d7d0) at Python/ceval.c:4117
#66 call_function (oparg=<optimized out>, pp_stack=0x7fffffffc460) at Python/ceval.c:4042
#67 PyEval_EvalFrameEx (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:2666
#68 0x00007ffff7aef63d in PyEval_EvalCodeEx (co=0xaed930, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=3, kws=0x49a6560, kwcount=0, defs=0xb7b1d0, defcount=2, closure=0x0)
    at Python/ceval.c:3253
#69 0x00007ffff7aed777 in fast_function (nk=<optimized out>, na=3, n=<optimized out>, pp_stack=0x7fffffffc680, func=0xb7d758) at Python/ceval.c:4117
#70 call_function (oparg=<optimized out>, pp_stack=0x7fffffffc680) at Python/ceval.c:4042
#71 PyEval_EvalFrameEx (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:2666
#72 0x00007ffff7aeed6a in fast_function (nk=<optimized out>, na=<optimized out>, n=<optimized out>, pp_stack=0x7fffffffc7f0, func=0xb7d848) at Python/ceval.c:4107
#73 call_function (oparg=<optimized out>, pp_stack=0x7fffffffc7f0) at Python/ceval.c:4042
#74 PyEval_EvalFrameEx (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:2666
#75 0x00007ffff7aef63d in PyEval_EvalCodeEx (co=0xaed4b0, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=2, kws=0xbe59e8, kwcount=0, defs=0xb72c28, defcount=1, closure=0x0)
    at Python/ceval.c:3253
#76 0x00007ffff7aed777 in fast_function (nk=<optimized out>, na=2, n=<optimized out>, pp_stack=0x7fffffffca10, func=0xb7d398) at Python/ceval.c:4117
#77 call_function (oparg=<optimized out>, pp_stack=0x7fffffffca10) at Python/ceval.c:4042
#78 PyEval_EvalFrameEx (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:2666
#79 0x00007ffff7aef63d in PyEval_EvalCodeEx (co=0xaed030, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=2, kws=0xbef170, kwcount=0, defs=0xb72be8, defcount=1, closure=0x0)
    at Python/ceval.c:3253
#80 0x00007ffff7aed777 in fast_function (nk=<optimized out>, na=2, n=<optimized out>, pp_stack=0x7fffffffcc30, func=0xb7d0c8) at Python/ceval.c:4117
#81 call_function (oparg=<optimized out>, pp_stack=0x7fffffffcc30) at Python/ceval.c:4042
#82 PyEval_EvalFrameEx (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:2666
#83 0x00007ffff7aef63d in PyEval_EvalCodeEx (co=0x7ffff7eeac30, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=1, kws=0x6f2200, kwcount=2, defs=0xa30578, defcount=2, 
    closure=0x0) at Python/ceval.c:3253
#84 0x00007ffff7aed777 in fast_function (nk=<optimized out>, na=1, n=<optimized out>, pp_stack=0x7fffffffce50, func=0xb85a28) at Python/ceval.c:4117
#85 call_function (oparg=<optimized out>, pp_stack=0x7fffffffce50) at Python/ceval.c:4042
#86 PyEval_EvalFrameEx (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:2666
#87 0x00007ffff7aef63d in PyEval_EvalCodeEx (co=0x7ffff7f2ab30, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:3253
#88 0x00007ffff7aef762 in PyEval_EvalCode (co=<optimized out>, globals=<optimized out>, locals=<optimized out>) at Python/ceval.c:667
#89 0x00007ffff7b11750 in run_mod (arena=0x623430, flags=0x7fffffffd170, locals=0x641160, globals=0x641160, filename=<optimized out>, mod=0x6f1ba0) at Python/pythonrun.c:1353
#90 PyRun_FileExFlags (fp=0x6d70a0, filename=<optimized out>, start=<optimized out>, globals=0x641160, locals=0x641160, closeit=0, flags=0x7fffffffd170) at Python/pythonrun.c:1339
#91 0x00007ffff7b1225f in PyRun_SimpleFileExFlags (fp=0x6d70a0, filename=0x7fffffffe919 "/home/mmarco/sage-5.2/local/bin/sage-ipython", closeit=0, flags=0x7fffffffd170) at Python/pythonrun.c:943
#92 0x00007ffff7b27976 in RunStartupFile (cf=0x7fffffffd170) at Modules/main.c:153
#93 Py_Main (argc=<optimized out>, argv=0x7fffffffd298) at Modules/main.c:593
#94 0x00007ffff6de222d in __libc_start_main () from /lib64/libc.so.6
#95 0x00000000004006e9 in _start ()

```



---

Comment by vbraun created at 2012-09-09 20:49:03

Can you try the new spkg + patch? I think I tracked down the bug ;-)


---

Comment by mmarco created at 2012-09-10 09:24:49

I am attending a conference this week, so i will have little time. On top of that, i don't have my computer with me. I will try to find time to work remotelly on that, but i cannot ensure when that will happen.


---

Comment by mmarco created at 2012-09-10 21:40:24

I finally could test it. It seems to work fine now. Great work!

I don't have the necessary skills to review the code, but i can go on testing it.


---

Comment by mmarco created at 2012-09-21 18:01:37

Do you plan  to implement comparison of libgap objects? I am trying to port my fpgroups code to libgap, and doctests fail because of this.


---

Comment by vbraun created at 2012-09-22 09:38:13

OK I'll try to update everything to gap-4.5.6 today and add comparison.


---

Comment by vbraun created at 2012-09-22 16:48:25

Ok, done. Comparison works now:

```
sage: libgap('test') == libgap.Concatenation(libgap('te'), libgap('st'))
True
```


I made one incompatible change: since `libgap` is the parent to all gap elements, it should do element construction for strings:

```
sage: libgap('1+1')
"1+1"
sage: type(_)
<type 'sage.libs.gap.element.GapElement_String'>
```

To evaluate a GAP command in a string, you now have to use

```
sage: libgap.eval('1+1')
2
```

Since we aim at wrapping more of GAP one expects that the `libgap.eval` method becomes less useful over time.


---

Comment by vbraun created at 2012-09-22 21:57:35

PS: I also changed the refcounting system, now its hooking directly into GASMAN to keep objects alive.

I think we should get this into Sage for real, now. Dima, are you up to another reviewing challenge? :-)


---

Comment by dimpase created at 2012-09-23 09:27:06

Replying to [comment:98 vbraun]:
> PS: I also changed the refcounting system, now its hooking directly into GASMAN to keep objects alive.
> 
> I think we should get this into Sage for real, now. Dima, are you up to another reviewing challenge? :-)
> 
Well, yes 8-/. 

What about eliminating a hardcoded path in `sage/libs/gap/test/main.c` ?
Is it possible to test this, via a Cython wrapper, say? (It's also easier to test this in sage-check script).


---

Comment by dimpase created at 2012-09-23 09:52:32

I see several messages `halving pool size` if I do `sage: libgap?` immediately after starting Sage.
This looks like some debugging printout getting in the way.


---

Comment by dimpase created at 2012-09-23 10:09:20

Replying to [comment:99 dimpase]:
> Replying to [comment:98 vbraun]:
> > PS: I also changed the refcounting system, now its hooking directly into GASMAN to keep objects alive.
> > 
> > I think we should get this into Sage for real, now. Dima, are you up to another reviewing challenge? :-)
> > 
> Well, yes 8-/. 
> 
> What about eliminating a hardcoded path in `sage/libs/gap/test/main.c` ?

I cannot guess the correct value of this relative to `$SAGE_LOCAL` or `$SAGE_ROOT`. In fact it should be easy to have this build and run from Sage shell prompt (i.e. `sage -sh`), then these hardcoded paths in Makefile and in main.c are not necessary. It would be great to have this fixed.

Then hooking it up on sage-check becomes trivial, too.


---

Comment by dimpase created at 2012-09-23 11:06:46

the new libgap spkg needs to be mentioned in `SAGE_ROOT/spkg/standard/deps`, as it depends on GAP, but this is not done.
Also, libgap needs to be mentioned in `SAGE_ROOT/spkg/install`, AFAIK.


---

Comment by dimpase created at 2012-09-23 11:15:26

on the spkg: it has two (!) upstream-gap subdirectories. Does one need them both? 

I don't understand whether MPIR is used as the replacement of GMP here, or not.
(according to spkg-install it looks as if it uses MPIR, actually).
(Last time I checked (well, long ago) GAP didn't run with MPIR; actually, I was too busy to find out how it is now working with the new GAP spkg; does it build its own GMP?)


---

Comment by vbraun created at 2012-09-23 13:12:04

The `sage/libs/gap/test/main.c` is only for instructional purposes, it demonstrates how to build a standalone binary so you can run libGAP under a debugger/valgrind without Sage. It doesn't exercise anything thats not already in doctests. 

One could add a `spkg-check` to test `src/test` in the spkg, but they again don't exercise anything thats not covered by libGAP doctests.

I've removed the upstream-gap-x.y.z directories from the spkg, the `make-spkg.sh` script copied them there accidentally.

Gap links against MPIR just fine, the only issue is with a version check that I reported here: https://groups.google.com/d/topic/mpir-devel/X48SfwGkSd8/discussion. This is why the `spkg-install` adds `-D__GMP_MP_RELEASE=50002` to the `CFLAGS`:

```
(sage-sh) vbraun@volker-desktop:spkg$ ldd ~/Sage/sage/local/lib/libgap.so
	linux-vdso.so.1 =>  (0x00007fff8ebff000)
	libgmp.so.7 => /home/vbraun/opt/sage-5.4.beta1/local/lib/libgmp.so.7 (0x00007f8a82885000)
	libc.so.6 => /lib64/libc.so.6 (0x00007f8a824a9000)
	/lib64/ld-linux-x86-64.so.2 (0x00000036c4000000)
```



---

Comment by vbraun created at 2012-09-23 13:18:40

I've added a patch for the root repo. I guess we need to vote on sage-devel about adding a new spkg? Though its not really new, its just an alternate version of code that we already ship.


---

Comment by vbraun created at 2012-09-23 13:41:05

Spkg vote: https://groups.google.com/d/topic/sage-devel/24UhIuA5eNc/discussion


---

Comment by mmarco created at 2012-09-23 13:51:40

Can you explain how to set up the amount of memory available for the libgap session?


---

Comment by vbraun created at 2012-09-23 14:55:38

Nowadays GAP uses anonymous mmap to reserve a big chunk of addressing space (not physical RAM, mind you) and uses that as needed. This is the origin of the `halving pool size` message on stdout. The message is purely cosmetic, but I'll ask upstream to suppress it. It also appears on the GAP command line and has nothing to do with libGAP:

```
[vbraun@volker-desktop ~]$ sage -gap -o 16384G
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
 ┌───────┐   GAP, Version 4.5.6 of 16-Sep-2012 (free software, GPL)
 │  GAP  │   http://www.gap-system.org
 └───────┘   Architecture: x86_64-unknown-linux-gnu-gcc-default64
 Libs used:  gmp, readline
 Loading the library and packages ...
 Components: trans 1.0, prim 2.1, small* 1.0, id* 1.0
 Packages:   CTblLib 1.2.1, FactInt 1.5.3, GAPDoc 1.5.1, LAGUNA 3.6.1, TomLib 1.2.2
 Try '?help' for help. See also  '?copyright' and  '?authors'
```

By default we try to acquire 16TB of addressing space, and then halving that until it succeeds:

```
Tasks: 352 total,   3 running, 345 sleeping,   1 stopped,   3 zombie
Cpu(s): 13.5%us,  0.4%sy,  0.0%ni, 85.9%id,  0.0%wa,  0.2%hi,  0.0%si,  0.0%st
Mem:  32835628k total, 32140456k used,   695172k free,  1037012k buffers
Swap: 62499996k total,   485252k used, 62014744k free, 13507248k cached

  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND                                                 
11585 vbraun    20   0 78.2g  48m  992 S  0.0  0.2   0:00.72 gap                                                     
```

The memory you can use in the gap session is limited to the pool size, but at least on 64-bit this should always be a lot.


---

Comment by dimpase created at 2012-09-23 15:16:31

Replying to [comment:104 vbraun]:
> Gap links against MPIR just fine, the only issue is with a version check that I reported here: https://groups.google.com/d/topic/mpir-devel/X48SfwGkSd8/discussion. This is why the `spkg-install` adds `-D__GMP_MP_RELEASE=50002` to the `CFLAGS`:

is there any reason for GAP being linked statically against GMP (i.e. MPIR)?

```
$sage-5.4.beta1/local/gap/latest$ ldd bin/x86_64-unknown-linux-gnu-gcc-default64/gap
        linux-vdso.so.1 =>  (0x00007fff7c4c9000)
        libm.so.6 => /lib/libm.so.6 (0x00007fa3e0d26000)
        libreadline.so.6 => /lib/libreadline.so.6 (0x00007fa3e0ae2000)
        libncurses.so.5 => /usr/lib/libncurses.so.5 (0x00007fa3e089b000)
        libdl.so.2 => /lib/libdl.so.2 (0x00007fa3e0697000)
        libutil.so.1 => /lib/libutil.so.1 (0x00007fa3e0494000)
        libc.so.6 => /lib/libc.so.6 (0x00007fa3e0131000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fa3e0fc3000)
$sage-5.4.beta1/local/gap/latest$ ../../../sage -gap
 *********   GAP, Version 4.5.6 of 16-Sep-2012 (free software, GPL)
 *  GAP  *   http://www.gap-system.org
 *********   Architecture: x86_64-unknown-linux-gnu-gcc-default64
 Libs used:  gmp, readline
 Loading the library and packages ...
 Components: trans 1.0, prim 2.1, small* 1.0, id* 1.0
 Packages:   CTblLib 1.2.1, FactInt 1.5.3, GAPDoc 1.5.1, LAGUNA 3.6.1, TomLib 1.2.2
 Try '?help' for help. See also  '?copyright' and  '?authors'
gap> 
```



---

Comment by dimpase created at 2012-09-23 15:26:40

Replying to [comment:104 vbraun]:
> The `sage/libs/gap/test/main.c` is only for instructional purposes, it demonstrates how to build a standalone binary so you can run libGAP under a debugger/valgrind without Sage. It doesn't exercise anything thats not already in doctests. 

I tried it on the system I am testing libgap now, and it doesn't work (I needed to do changes --- see the patch to be attached --- to the source to make it compile, but it seems to need more, as I get suspicious warnings during compilation, and then a segfault)

```

(sage-sh) dima@spms-banana:test$ make main
gcc -std=gnu99 -I/usr/local/src/sage/sage-5.4.beta1/local/include -I/usr/local/src/sage/sage-5.4.beta1/local/include/python2.6 -c -g -DGAPLOCAL=/usr/local/src/sage/sage-5.4.beta1/local/gap/latest main.c
In file included from main.c:10:
/usr/local/src/sage/sage-5.4.beta1/local/include/gap/vars.h: In function 'libGAP_SwitchToNewLvars':
/usr/local/src/sage/sage-5.4.beta1/local/include/gap/vars.h:163: warning: implicit declaration of function 'libGAP_BODY_FUNC'
/usr/local/src/sage/sage-5.4.beta1/local/include/gap/vars.h:163: warning: cast to pointer from integer of different size
In file included from main.c:10:
/usr/local/src/sage/sage-5.4.beta1/local/include/gap/vars.h: In function 'libGAP_SwitchToOldLVars':
/usr/local/src/sage/sage-5.4.beta1/local/include/gap/vars.h:205: warning: cast to pointer from integer of different size
main.c: In function 'eval':
main.c:24: warning: implicit declaration of function 'libgap_set_error'
main.c:26: warning: implicit declaration of function 'libGAP_ViewObjHandler'
gcc -L/usr/local/src/sage/sage-5.4.beta1/local/lib -o main main.o -lgap -lcsage -lntl -lstdc++ -lpari -lpython2.7 -lm -lgmp
(sage-sh) dima@spms-banana:test$ ./main
Initialized
Input:
1+2+3;
Output:
6
Input:
g:=FreeGroup(2);
Segmentation fault
(sage-sh) dima@spms-banana:test$ 
```



---

Comment by dimpase created at 2012-09-23 15:27:29

reviewer's patch


---

Attachment

I don't think there is any reason for statically linking gmp other than their build system predating much of autotools...

The implicit declaration and pointer cast warnings are normal, GAP just predates ansi C :-)


---

Comment by dimpase created at 2012-09-23 15:49:49

Replying to [comment:111 vbraun]:

> The implicit declaration and pointer cast warnings are normal, GAP just predates ansi C :-)

Well, anyhow... Could you confirm that my change of the code was OK, and this is a genuine issue?
gdb tells me the following:

```

g:=FreeGroup(2);

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff75a8d0f in libGAP_RNamName ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
(gdb) bt
#0  0x00007ffff75a8d0f in libGAP_RNamName ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#1  0x00007ffff76cb0e1 in libGAP_CallErrorInner ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#2  0x00007ffff76cb2f4 in libGAP_ErrorQuit ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#3  0x00007ffff757b8df in libGAP_ErrorMustHaveAssObjHandler ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#4  0x00007ffff75b7b70 in libGAP_DoWrap2args ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#5  0x00007ffff76cb299 in libGAP_CallErrorInner ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#6  0x00007ffff76cb2f4 in libGAP_ErrorQuit ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#7  0x00007ffff757b8df in libGAP_ErrorMustHaveAssObjHandler ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#8  0x00007ffff75b7b70 in libGAP_DoWrap2args ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#9  0x00007ffff76cb299 in libGAP_CallErrorInner ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#10 0x00007ffff76cb2f4 in libGAP_ErrorQuit ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#11 0x00007ffff757b8df in libGAP_ErrorMustHaveAssObjHandler ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#12 0x00007ffff75b7b70 in libGAP_DoWrap2args ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#13 0x00007ffff76cb299 in libGAP_CallErrorInner ()
   from /usr/local/src/sage/sage-5.4.beta1/local/lib/libgap.so.0
#14 0x00007ffff76cb2f4 in libGAP_ErrorQuit ()
.....
```

and it keeps repeating, ad nauseum...
The x86_64 system runs Debian, here are the compiler specs:

```
(sage-sh) dima@spms-banana:test$ gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Debian 4.4.5-8' --with-bugurl=file:///usr/share/doc/gcc-4.4/README.Bugs --enable-languages=c,c++,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-4.4 --enable-shared --enable-multiarch --enable-linker-build-id --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.4 --libdir=/usr/lib --enable-nls --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --with-arch-32=i586 --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.4.5 (Debian 4.4.5-8) 
```



---

Comment by vbraun created at 2012-09-23 16:31:38

Your changes look fine. The `test/main.c` example doesn't do proper error handling, so you shouldn't expect a useful error message. For a relevant stack backtrace you need to post what happens before you get into the error loop.


---

Comment by vbraun created at 2012-09-23 16:44:38

Upon squinting a bit harder, I noticed that

```
argv[2] = "GAPLOCAL" ;
```

in your patch does not use the preprocessor macro, it is just the string `"GAPLOCAL"`. I've updated the patch to not hardcode the path and pass through the gap directory correctly.


---

Comment by dimpase created at 2012-09-23 17:35:34

Replying to [comment:113 vbraun]:
> Your changes look fine. The `test/main.c` example doesn't do proper error handling, so you shouldn't expect a useful error message. For a relevant stack backtrace you need to post what happens before you get into the error loop.

Well, I rebuilt libgap with SAGE_DEBUG on, and I can see it starting the interpreter interaction, parsing the input, calling gasman, then something goes wrong, it tries to print the message `"Variable: 'FreeGroup' must have a value"`

```

(gdb) 
libGAP_SPrTo (buffer=0x7fffffffd0d0 "Variable: 'FreeGroup' must have a value", maxlen=120, 
    format=0x7ffff7750098 "Variable: '%s' must have a value", arg1=140733014557528, arg2=0)
    at scanner.c:3049
```

then I see

```
(gdb) 
libGAP_SyStrncat (dst=0x7fffffffcd20 "justQuit", src=0x7ffff775e32c "justQuit", len=1023)
    at system.c:682

(gdb) 
libGAP_RNamName (name=0x7ffff775e32c "justQuit") at records.c:110
```

and it tries to go further. Eventually I see

```
(gdb) 
libGAP_ErrorQuit (msg=0x7ffff77472a0 "Variable: <<unknown>> must have an assigned value", arg1=0, 
    arg2=0) at gap.c:1451
(gdb) 
libGAP_CallErrorInner (msg=0x7ffff77472a0 "Variable: <<unknown>> must have an assigned value", 
    arg1=0, arg2=0, justQuit=1, mayReturnVoid=0, mayReturnObj=0, lateMessage=0x7ffef510a678, 
    printThisStatement=1) at gap.c:1430

```


this gets repeated many times (buffer corruption), and eventually a segfault.

```
Program received signal SIGSEGV, Segmentation fault.
0x00007ffff75a8eef in libGAP_RNamName (name=Cannot access memory at address 0x7fffff7fefa8
) at records.c:79
```


the trouble starts of course much earlier, before it fails to recognize `FreeGroup` as a valid GAP function...




.


---

Comment by dimpase created at 2012-09-23 17:44:05

Replying to [comment:114 vbraun]:
> Upon squinting a bit harder, I noticed that
> {{{
> argv[2] = "GAPLOCAL" ;
> }}}
> in your patch does not use the preprocessor macro, it is just the string `"GAPLOCAL"`. I've updated the patch to not hardcode the path and pass through the gap directory correctly.

/me facepalm...

OK, now, with the updated patch, it works.


---

Comment by mhansen created at 2012-09-24 00:26:48

What was the reason that sage.interfaces.interface wasn't used?  It seems like we should at least have a GAP Interface that is compatible with the old pexpect one much like was done for the maxima pexpect / ecl interface.


---

Comment by dimpase created at 2012-09-24 04:50:25

Replying to [comment:117 mhansen]:
> What was the reason that sage.interfaces.interface wasn't used?  It seems like we should at least have a GAP Interface that is compatible with the old pexpect one much like was done for the maxima pexpect / ecl interface.

My understanding is that at this point it's still very far to compatibility. On the other hand, it seems that replacing the `pexpect` interface using  libgap's `eval` should already be quite possible.


---

Comment by dimpase created at 2012-09-24 06:31:19

Replying to [comment:111 vbraun]:
> I don't think there is any reason for statically linking gmp other than their build system predating much of autotools...

Would it be much work to libtoolize GAP itself, given that, as far as I understand, the work on this ticket can largely be re-used?


---

Comment by dimpase created at 2012-09-24 06:40:05

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-09-24 06:56:06

As I said on a different ticket, `assert` should not be used for control flow.  An assert checks something which should always be true, a failed assertion is always a bug.  I consider the following to be bad usage of `assert`:

```
        try:
            sig_on()
            proxy = make_GapElement_MethodProxy(self.parent(), 
                                                gap_eval(name),
                                                self)
            sig_off()
            assert proxy.is_function()
        except RuntimeError, AssertionError:
            raise AttributeError, 'Name "'+str(name)+'" does not define a GAP function.'

        return proxy
```



---

Comment by jdemeyer created at 2012-09-24 06:56:06

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-09-24 06:57:55

The `SAGE_ROOT` patch needs to be rebased to #13415.


---

Comment by vbraun created at 2012-09-24 08:37:49

Updated patch


---

Attachment

`sage.interfaces.interface.Interface` doesn't look like the most useful parent, its non-unique and operates on the assumption that one is dealing with a separate process. Here we have a shared library that is full of global variables. I think libGAP should aim at directly translating Sage<->GAP objects, so that the libGAP user does not have to input gap commands as strings at all.

It wouldn't take much to also build a libtoolized standalone interpreter, or even a GAP interpreter that communicates over zeromq. The problem is that 3rd party packages often expect a stand-alone gap tree with upstream's hacked up semi-autotools to install themselves in. From talking with people in St. Andrews I understand that upstream probably would have switched their build system already if it were not for this legacy problem.

I got rid of the assert abuse and added some more tests.


---

Comment by burcin created at 2012-09-24 10:46:34

Replying to [comment:124 vbraun]:

>  a GAP interpreter that communicates over zeromq

This is a great idea. Would we be able to use IPython as the GAP interpreter if we tied your libGAP to zeromq?

Also based on conversations in St. Andrews, some upstream developers are interested in an autotools based build system. AFAICT, the main problem with compiled GAP packages is that they rely on the object files previously compiled for the GAP executable to find symbols they need from the GAP kernel. libGAP solves this problem. This can be fixed by changing GAP's compiler wrapper which adds the path of these object files to find your libGAP instead. Before trying this approach, a GAP interpreter that uses libGAP is needed. Otherwise we will have the GAP binary and libGAP in memory with the same code.


Volker, many thanks for all the hard work on libGAP.


---

Comment by vbraun created at 2012-09-24 11:45:10

Replying to [comment:125 burcin]:
> Would we be able to use IPython as the GAP interpreter if we tied your libGAP to zeromq?

zeromq is just a transport, you'd have to speak the IPython protocol to do this. Much harder than just tying stdin/stdout/stderr to sockets.

> AFAICT, the main problem with compiled GAP packages is that they rely on the object files previously compiled for the GAP executable to find symbols they need from the GAP kernel. libGAP solves this problem. This can be fixed by changing GAP's compiler wrapper which adds the path of these object files to find your libGAP instead.

You also need to prefix the symbol names with `libGAP_` if you want to link against libGAP with legacy code. Doable but at least in the short term its much easier to have libGAP and standalone GAP separately. Much like libSingular and Singular.


---

Comment by dimpase created at 2012-09-24 12:08:31

Replying to [comment:125 burcin]:
> Replying to [comment:124 vbraun]:
> 
> >  a GAP interpreter that communicates over zeromq
> 
> Also based on conversations in St. Andrews, some upstream developers are interested in an autotools based build system. AFAICT, the main problem with compiled GAP packages is that they rely on the object files previously compiled for the GAP executable to find symbols they need from the GAP kernel.

Do you mean GAP extension packages, things which are compiled using `gac` ?
"Normal" GAP packages do not need any of this, AFAIK.
The extension packages are few and far apart. The only one I know is [EDIM](http://www.math.rwth-aachen.de/~Frank.Luebeck/EDIM/index.html).
The main use of `gac` seems to be
to create faster loading GAP executables.


---

Comment by kcrisman created at 2012-09-24 12:56:36

OS X 10.4 PPC:

```
sage -t  "devel/sage-main/sage/algebras/group_algebra_new.py"
**********************************************************************
File "/Users/student/Desktop/sage-5.4.beta1/devel/sage-main/sage/algebras/group_algebra_new.py", line 592:
    sage: GroupAlgebra(DihedralGroup(6), QQ).random_element()
Expected:
    -1/95*(2,6)(3,5) - 1/2*(1,3)(4,6)
Got:
    -1/95*(1,3)(4,6) - 1/2*(1,5,3)(2,6,4)
**********************************************************************
File "/Users/student/Desktop/sage-5.4.beta1/devel/sage-main/sage/algebras/group_algebra_new.py", line 594:
    sage: GroupAlgebra(SU(2, 13), QQ).random_element(1)
Expected:
    1/2*[      1 9*a + 2]
    [9*a + 2      12]
Got:
    1/2*[       4  9*a + 2]
    [6*a + 10        1]
**********************************************************************
1 items had failures:
   2 of   5 in __main__.example_23
***Test Failed*** 2 failures.
```

There were other errors as well, which I'm rerunning.


---

Comment by dimpase created at 2012-09-24 13:15:05

Replying to [comment:128 kcrisman]:
This has nothing to do with this ticket, this is new GAP, i.e. #13211. Just as a sanity check, have you applied the patches from #13211 ?


---

Comment by kcrisman created at 2012-09-24 15:22:34

Thanks, I'll comment there (I only ran tests after doing everything just to save time).

```
Dasher-03:~/Desktop/sage-5.4.beta1/devel/sage student$ ../../sage -hg qseries
trac_13211_fix_gap_doctests.patch
trac_6391_libGAP.patch
```

I think that's right?


---

Comment by dimpase created at 2012-09-24 15:26:52

Replying to [comment:130 kcrisman]:
> Thanks, I'll comment there (I only ran tests after doing everything just to save time).
> {{{
> Dasher-03:~/Desktop/sage-5.4.beta1/devel/sage student$ ../../sage -hg qseries
> trac_13211_fix_gap_doctests.patch
> trac_6391_libGAP.patch
> }}}
> I think that's right?
hopefully you also did `sage -b` before starting the tests? Just checking...


---

Comment by kcrisman created at 2012-09-24 17:05:02

Yes, and I just checked that this was the case.  But I hear you on that kind of thing - it's so easy to forget.


---

Comment by dimpase created at 2012-09-24 17:21:43

Replying to [comment:128 kcrisman]:

> {{{
> sage -t  "devel/sage-main/sage/algebras/group_algebra_new.py"
> **********************************************************************
> File "/Users/student/Desktop/sage-5.4.beta1/devel/sage-main/sage/algebras/group_algebra_new.py", line 592:
>     sage: GroupAlgebra(DihedralGroup(6), QQ).random_element()
> File "/Users/student/Desktop/sage-5.4.beta1/devel/sage-main/sage/algebras/group_algebra_new.py", line 594:
>     sage: GroupAlgebra(SU(2, 13), QQ).random_element(1)
> }}}
these are calls to random stuff, or so it seems! No wonder different hardware gives different (pseudo?)random elements. If it were tests I'd say they'd be marked `# random`, like

```
         GroupAlgebra(DihedralGroup(6), QQ).random_element() # random
```

not sure about examples in this case though. Or else, if these random elements are actually predictable, this could be a bug in the pseudorandom source.


---

Comment by mmarco created at 2012-09-24 18:33:50

I couldn't apply the root patch through normal hg_sage.apply(). Is it supposed to be applied  in some other way?.

Now i get this message when i start the sage session:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
gap: halving pool size.
An error occurred, but libGAP has no handler set.
Error message: 
Loading Sage library. Current Mercurial branch is: libgap6
sage: 
| Sage Version 5.2, Release Date: 2012-07-25                         |
| Type "notebook()" for the browser-based notebook interface.        |
| Type "help()" for help.                                            |
```


But, regardless of the mysterious error, everything seems to work ok (at least my fpgroups code, which is what i am using for testing).


---

Comment by kcrisman created at 2012-09-24 18:41:39

You'd use `hg_root.apply()`.  `hg_sage` applies things to the Sage library code directories, not the root directory of Sage.


---

Comment by vbraun created at 2012-10-08 21:01:10

rebased patch


---

Attachment

I've rebased the root patch just now, and removed the assert that offended Jeroen a while ago.

The startup error handling will be dealt with at #13588, this ticket is already way too long.

This ticket should be easy to review since it contains only minor changes from the previously-reviewed state.


---

Comment by vbraun created at 2012-10-08 21:08:16

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2012-10-10 10:35:08

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2012-10-10 10:35:08

all good.


---

Comment by mmarco created at 2012-10-12 13:42:56

I get a strange behaviour when i use tab completion with libgap objects:


```
sage: F=libgap.eval('FreeGroup(2)')
sage: F.GeneratorsOfGroup()
[ f1, f2 ]
sage: F.GeneratorsOf
F.GeneratorsOfField  F.GeneratorsOfGroup  F.GeneratorsOfIdeal  
sage: F.GeneratorsOfGroup()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/mmarco/sage-5.4/<ipython console> in <module>()

/home/mmarco/sage-5.4/local/lib/python2.7/site-packages/sage/libs/gap/element.so in sage.libs.gap.element.GapElement.__getattr__ (sage/libs/gap/element.c:3555)()

AttributeError: Name "GeneratorsOfGroup" is not defined in GAP.
sage: F
Exception RuntimeError: 'Entered a critical block twice' in 'sage.libs.gap.util.error_handler' ignored
<free group on the generators [ f1, f2 ]>
sage: F.GeneratorsOfGroup()
[ f1, f2 ]
```

(i hitted TAB in the line F.GeneratorsOf, so it showed the possible completions).


---

Comment by mmarco created at 2012-10-12 16:33:19

Another question: i can use much less memory in a gap computation through libgap that i can in a standard sage/gap session:


```
./sage -gap
 *********   GAP, Version 4.5.6 of 16-Sep-2012 (free software, GPL)
 *  GAP  *   http://www.gap-system.org
 *********   Architecture: x86_64-unknown-linux-gnu-gcc-default64
 Libs used:  gmp, readline
 Loading the library and packages ...
 Packages:   GAPDoc 1.5.1
 Try '?help' for help. See also  '?copyright' and  '?authors'
gap> F:=FreeGroup(2);
<free group on the generators [ f1, f2 ]>
gap> H:=F/[F.1^2,F.2^3];
<fp group on the generators [ f1, f2 ]>
gap> a:=GeneratorsOfGroup(H)[1];
f1
gap> a;
f1
gap> Order(a);
2
gap> quit;
```


But:


```
sage: G=libgap.FreeGroup(2)
sage: (a,b)=G.GeneratorsOfGroup()
sage: H=G/libgap([a^2,b^3]) 
sage: (c,d)=H.GeneratorsOfGroup()
sage: c.Order()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/mmarco/sage-5.4/<ipython console> in <module>()

/home/mmarco/sage-5.4/local/lib/python2.7/site-packages/sage/libs/gap/element.so in sage.libs.gap.element.GapElement_MethodProxy.__call__ (sage/libs/gap/element.c:8414)()

/home/mmarco/sage-5.4/local/lib/python2.7/site-packages/sage/libs/gap/element.so in sage.libs.gap.element.GapElement_Function.__call__ (sage/libs/gap/element.c:7947)()

ValueError: libGAP: Error, exceeded the permitted memory (`-o' command line option)
```


It is the same computation, but in the gap session it has enough memory (it doesn't need much: even with -o 256M the computation succeeds), and through libgap it runs out of memory.

I don't know if it is relevant, but i have no swap enabled in my system.


---

Comment by vbraun created at 2012-10-12 17:13:32

Gap and libGap now use the same function sage.interfaces.gap.get_gap_memory_pool_size() to determine how much address space to reserve. Without swap you will reserve actual memory, this is why the current patch then reserves a pretty small amount (free ram / 50). I guess we need to fine-tune the actual values a bit. I'll do this and fix the tab completion issue in #13588.

And whoever comes first gets more memory, so this is probably why gap got more than libgap in your case.


---

Comment by mmarco created at 2012-10-12 17:47:59

Is it possible to use some memory balooning technique? Or are we forced to choose between having too few memory for gap and leaving too few memory for the rest of the system?


---

Comment by vbraun created at 2012-10-12 18:31:43

Replying to [comment:142 mmarco]:
> Is it possible to use some memory balooning technique?

Gap does that already. I've described some of the details here:

```
def set_gap_memory_pool_size(size_in_bytes):
    """
    Set the desired gap memory pool size.

    Subsequently started GAP/libGAP instances will use this as
    default. Currently running instances are unchanged.

    GAP will only reserve ``size_in_bytes`` address space. Unless you
    actually start a big GAP computation, the memory will not be
    used. However, corresponding swap space will be reserved so that
    GAP will always be able to use the reserved address space if
    needed. While nothing is actually written to disc as long as you
    don't run a big GAP computation, the reserved swap space will not
    be available for other processes. 
    ...
```



---

Comment by mmarco created at 2012-10-13 00:52:21

So it sounds like a good idea to reserve a big amount of physical RAM, doesn't it?


---

Comment by mmarco created at 2012-10-29 17:36:06

I am starting to work on some project to allow computing reduced forms in some fp groups, and i found that i can't load gap packages via libgap:


```
./sage -gap
 *********   GAP, Version 4.5.6 of 16-Sep-2012 (free software, GPL)
 *  GAP  *   http://www.gap-system.org
 *********   Architecture: x86_64-unknown-linux-gnu-gcc-default64
 Libs used:  gmp, readline
 Loading the library and packages ...
 Packages:   CTblLib 1.2.1, FactInt 1.5.3, GAPDoc 1.5.1, LAGUNA 3.6.1
 Try '?help' for help. See also  '?copyright' and  '?authors'
gap> LoadPackage("kbmag")
> ;
---------------------------------------------------------------------------------------------------------------------------------------------------------
Loading  kbmag 1.5 (Knuth-Bendix on Monoids and Automatic Groups)
by Derek Holt (http://www.warwick.ac.uk/~mareg).
Homepage: http://www.warwick.ac.uk/~mareg/kbmag
---------------------------------------------------------------------------------------------------------------------------------------------------------
true
gap> LoadPackage("braid");
---------------------------------------------------------------------------------------------------------------------------------------------------------
Loading  braid 1.2 (braid groups package)
by Kay Magaard (http://www.math.wayne.edu/~kaym/),
   Sergey Shpectorov (http://www-math.bgsu.edu/~sergey/), and
   Helmut Voelklein (http://www.exp-math.uni-essen.de/algebra/people/voelklein.html).
Homepage: http://www.math.wayne.edu/~kaym/research/braid/
---------------------------------------------------------------------------------------------------------------------------------------------------------
true
gap> quit;
```


But 


```
./sage     
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: test
sage: libgap.LoadPackage('"kbmag"')
fail
sage: libgap.LoadPackage('"braid"')
fail
sage: libgap.LoadPackage("braid")  
true
sage: libgap.LoadPackage("kbmag")  
fail
```

| Sage Version 5.4.rc1, Release Date: 2012-10-05                     |
| Type "notebook()" for the browser-based notebook interface.        |
| Type "help()" for help.                                            |
Also, i don't know if it is because of libgap overwriting something in the usual gap interface, but gap.LoadPackage() gives an error message.

I installed the kbmag package with this .spkg i just made: 
https://docs.google.com/open?id=0B_B7eBQ-W5NGOFpIMmxiNXZVaGc

Is there something i should take into account?


---

Comment by vbraun created at 2012-10-29 18:02:23

The `kbmag` package has a binary compiled component, this won't work with libgap until kbmag learns about shared libraries. Packages that are pure Gap scripts do work, as you saw:

```
sage: libgap.LoadPackage("braid")  
true
```



---

Comment by mmarco created at 2012-10-29 20:13:04

So the only hope for my project is to rewrite kbmag to be able to communicate with shared libraries? I am afraid that is way beyond my skills now. Anyways, if you can help me a little bit i can try to learn about it.


---

Comment by nbruin created at 2012-10-30 07:01:15

I don't think you need to do anything with shared libraries. As far as I can see, the package communicates with external stand-alone executables via `Exec` calls. I'm a little surprised that libgap doesn't support Gap's `Exec` when it does support the rest of the interpreted language. Perhaps it's just a matter of initializing the environment of the Gap interpreter more fully?

Anyway, if you can't get the `Exec` approach to work, it should be possible to rewrite the `kbmag` routines that interface with the executable so that they produce the output that needs to go into a temporary communication file in a way that does work. Then you can call the executable with whatever means are appropriate and you parse its output back. It may not be pleasant to do, but doesn't require particular skills either. You'd better be very sure it really has a benefit over using a separate GAP process, because it'll be quite a bit of work.

Grep for `Exec` to see where the interfacing takes place.


---

Comment by mmarco created at 2012-10-30 10:24:11

How hard would it be to make Gap's Exec work through libgap?


---

Comment by vbraun created at 2012-10-30 11:33:29

If `kbmag` only uses stdin/out to communicate with its binary component then it should work. The `Exec` GAP function basically works when calling it via libGAP

```
sage: libgap_exec = libgap.eval("Exec")
sage: libgap_exec
<Gap function "Exec">
sage: libgap_exec('echo $HOME')
/home/vbraun
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/vbraun/<ipython console> in <module>()

/home/vbraun/opt/sage-5.4.rc1/local/lib/python2.7/site-packages/sage/libs/gap/element.so in sage.libs.gap.element.GapElement_Function.__call__ (sage/libs/gap/element.c:7929)()

ValueError: libGAP: Segmentation fault
```

There is a segfault when returning the result, I'll fix that in another ticket (maybe #13588).

How did you install `kbmag`, I don't think its one that we ship. Is there a spkg for it?


---

Comment by dimpase created at 2012-10-30 13:44:47

Replying to [comment:151 vbraun]:
 
> How did you install `kbmag`, I don't think its one that we ship. Is there a spkg for it?
> 
the googledocs link above will give you the spkg...
That's certainly not the best way to host files.
There is http://code.google.com/p/spkg-upload/
which would make much more sense.

Or, perhaps, even easier, a bitbucket or github account.


---

Comment by vbraun created at 2012-10-30 14:09:51

And open a ticket to make kbmag an experimental spkg so we have a place to discuss it. This issue is really done so nobody should post to it.


---

Comment by mmarco created at 2012-10-30 17:35:50

I have opened #13673.


---

Comment by tfeulner created at 2012-11-09 12:03:59

Thanks for this great contribution!

I just want to mention a problem with the assertion `strlen(libGAP_stdin_buffer) < length' which 
leads to an unhandled SIGABRT. Could this be avoided? 
 


```
sage: S = SymmetricGroup(10000)
sage: s = S.random_element()
sage: libgap(s)
```



---

Comment by vbraun created at 2012-11-09 15:48:59

Will be done in #13588


---

Comment by mmarco created at 2012-12-26 11:06:17

Now that it seems that gap upgrading has moved to 4.5.7, will this need to change?


---

Comment by mmarco created at 2012-12-26 11:26:33

Indeed, the actual version of libgap is incompatible with the gap-4.5.7 spkg:


```

sage: libgap.FreeGroup(4)
An error occurred, but libGAP has no handler set.
Error message: 
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/mmarco/sage-5.5/<ipython console> in <module>()

/home/mmarco/sage-5.5/local/lib/python2.7/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.LazyImport.__getattr__ (sage/misc/lazy_import.c:1877)()

/home/mmarco/sage-5.5/local/lib/python2.7/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.LazyImport._get_object (sage/misc/lazy_import.c:1291)()

/home/mmarco/sage-5.5/libgap.pyx in init sage.libs.gap.libgap (sage/libs/gap/libgap.c:4157)()

/home/mmarco/sage-5.5/libgap.pyx in sage.libs.gap.libgap.Gap.__init__ (sage/libs/gap/libgap.c:2716)()

/home/mmarco/sage-5.5/local/lib/python2.7/site-packages/sage/libs/gap/util.so in sage.libs.gap.util.initialize (sage/libs/gap/util.c:3489)()

RuntimeError: libGAP initialization failed


You are running a GAP kernel which does not fit with the library.
Probably you forgot to apply the kernel part or the library part
of a bugfix?

If you are using Windows, make sure you installed the file
wbin4r5n7.zoo (or .zip),
Macintosh users make sure the file
bin4r5n7-PPC.sit (or -68k.sit) is installed,
Unix users please recompile.

Error before error-handling is initialized: Update to correct kernel version!
```



---

Comment by dimpase created at 2012-12-26 12:01:11

Replying to [comment:159 mmarco]:
> Indeed, the actual version of libgap is incompatible with the gap-4.5.7 spkg:
SPKG.txt contains brief instructions about upgrading. You'll need to increase the version and rerun autotools to produce new spkg. I never tried this myself though.


---

Comment by vbraun created at 2012-12-26 12:23:07

I'm working on it.


---

Comment by dimpase created at 2012-12-26 12:30:39

Replying to [comment:161 vbraun]:
> I'm working on it.
I've built the new package from your bitbucket repo, and it at least installs OK.


---

Comment by dimpase created at 2012-12-26 12:48:29

Replying to [comment:162 dimpase]:
> Replying to [comment:161 vbraun]:
> > I'm working on it.
> I've built the new package from your bitbucket repo, and it at least installs OK.
http://boxen.math.washington.edu/home/dima/packages/libgap-4.5.7.p1.spkg

It also passes the tests in `sage/libs/gap`

To create the package on MacOSX, I had to install `GNU findtools`, for the native `find` has different options.


---

Comment by vbraun created at 2012-12-26 13:06:53

The libgap source repository is of course at the state of #13588. I've forward-ported all changes there. Since this ticket is now superseded by the new GAP version, it should be closed as duplicate. One of you guys should review #13588 :-)


---

Comment by mmarco created at 2012-12-26 13:14:28

So the patches to the sage library and the root repository should be moved to #13588, right?

I am techically unable to review the code, all i can do is test it and report.


---

Comment by vbraun created at 2012-12-26 13:18:16

Yes, I've moved the patches from here to #13588 to make Jeroen's life easier.


---

Comment by jdemeyer created at 2012-12-27 10:30:42

Resolution: duplicate
