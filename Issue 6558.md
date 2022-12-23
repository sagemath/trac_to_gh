# Issue 6558: Be more selective in patching ATLAS on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/6558

Original creator: drkirkby

Original creation time: 2009-07-19 00:39:23

Assignee: tbd

Keywords: solaris atlas sun4v

Trac ticket #6276 was a patch I added to the ATLAS code, as the tuning process had dumped core on a Sun T5240 machine called ('t2'). This machine is based on the latest T2+ processor from Sun. The patch was suggested by Clint Whaley - the main ATLAS developer.

Despite no known problems with ATLAS dumping core on any of the older systems, or Solaris systems based on the x86 processor, I had applied this patch to all Solaris systems. However, it is really a hack more than a patch, as it allows ATLAS to build by returning a reasonable value for a parameter that the system could not tune properly. 

This patch is an improvement, which simply checks if the system is Solaris and the architecture is 'sun4v' before applying the hack. So only Solaris systems with Sun T1, T2 or T2+ processors will be patched. Those would form only a small fraction of the Solaris machines. On the vast majority of systems in use today, the patch will no longer be applied, so the tuning process will be more accurate. 

A patch for this will be very simple. Although I have not checked it yet, I believe changing:




```
if os.uname()[0] == 'SunOS' :    
   shutil.copy2('patches/mmsearch-with-temp-Solaris-fix.c','src/tune/blas/gemm/mmsearch.c')


```


to 



```
if os.uname()[0] == 'SunOS' and os.uname()[4] == 'sun4v':
   shutil.copy2('patches/mmsearch-with-temp-Solaris-fix.c','src/tune/blas/gemm/mmsearch.c')

```


will fix this. 

I'll attach a patch for review, once its operation has been carefully checked both on a Sun T5240 (a sun4v machine called 't2') and a Sun Blade 2000 (a sun4u machine called 'kestrel'). 



---

Comment by drkirkby created at 2009-07-19 16:57:54

Changing keywords from "solaris atlas sun4v" to "solaris atlas sun4v sun4m".


---

Comment by drkirkby created at 2009-07-19 16:57:54

Here's the patch directory, giving the patch, a rebuild .spkg and an updated SPKG.txt

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/atlas-3.8.3.p6/

here's the actual patch:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/atlas-3.8.3.p6/atlas-3.8.3.p6.spkg

It should be very simple to review, as the only change of code is to one small line. 


```
 import shutil
-if os.uname()[0] == 'SunOS':
+if os.uname()[0] == 'SunOS' and os.uname()[4] == 'sun4v':
    shutil.copy2('patches/mmsearch-with-temp-Solaris-fix.c','src/tune/blas/gemm/mmsearch.c')

```

(There's also a change in a comment, since atlas-3.8.3.p5.spkg had a comment which stopped in mid-sentence. I just completed the sentence.)

The patch is based on the fact that python's os.uname() prints the architecture, and on Solaris that will be sun4v on 't2' and similar machines, but different on machines which do not use the T1, T2 or T2+ processors. These processors, with 

Here's the output of os.uname() on 't2', which is a Sun T5240 the T2+ processors.

```
kirkby@t2:[~] $ python
Python 2.4.4 (#1, Jan 10 2007, 01:25:01) [C] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.uname()
('SunOS', 't2', '5.10', 'Generic_141414-02', 'sun4v')
>>>
```

and here is is on an older machine, a Sun Blade 2000 with UltraSPARC III Cu CPU's, which are the older sun4u architecture. 

```
drkirkby@kestrel:[~] $ python
Python 2.4.4 (#1, Jan 10 2007, 01:25:01) [C] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.uname()
('SunOS', 'kestrel', '5.10', 'Generic_139555-08', 'sun4u')
>>>
```


Dave


---

Comment by drkirkby created at 2009-07-19 16:57:54

Changing assignee from tbd to drkirkby.


---

Comment by mvngu created at 2009-07-21 13:38:02

After uncompressing the SPKG at

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/atlas-3.8.3.p6/atlas-3.8.3.p6.spkg

I see some junk:

```
[mvngu@sage atlas-3.8.3.p6]$ hg st
M SPKG.txt
M spkg-install
? patches/mmsearch-with-temp-Solaris-fix.c
? patches/mmsearch-with-temp-Solaris-fix.c.patch
? spkg-install-script.orig
```

David, can you remove junks from the SPKG. After that, I can deal with checking in changes if you want.


---

Comment by mvngu created at 2009-07-22 18:56:40

Updated SPKG up at

http://sage.math.washington.edu/home/mvngu/patch/atlas-3.8.3.p6.spkg

All changes have been committed in the name of David Kirkby.


---

Comment by mvngu created at 2009-07-23 23:38:08

Builds on Solaris on the machine t2. (It also compiles without problems on Linux.)


---

Comment by mvngu created at 2009-07-23 23:38:08

Resolution: fixed
