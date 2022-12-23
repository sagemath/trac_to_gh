# Issue 6355: [with SPKG, needs review] Cliquer to compute maximum cliques

Issue created by migration from https://trac.sagemath.org/ticket/6355

Original creator: ncohen

Original creation time: 2009-06-18 12:57:35

Assignee: rlm

Keywords: Clique max, Cliquer

Hello everybody ! I hope this is the last step for this patch to compute the maximum cliques in a graph.
Here is the SPKG file with the source code of Cliquer.
As for planarity or other modules, the original source code of cliquer is copied, but in this case it is copied in local/lib/cliquer-1.2, I was told planarity was to be an exception to the rule.

You can download the SPKG file at this address :
http://www-sop.inria.fr/members/Nathann.Cohen/cliquer-1.2.spkg


---

Comment by rlm created at 2009-06-19 22:34:36

This ticket, plus #5793 and #5669, are all a total mess, IMHO. There are two separate spkg's linked, here and on #5669, and there are two different sets of patches (`11803.patch` is separately 229.4KB and 6.0KB) at #5793 and #5669.

1. Patch names need to be of the form `trac_####-description.patch`.
2. I don't even know which spkg to review.
3. #5793 and #5669 are total duplicates.

My recommendation is to close the other two tickets as duplicates, indicate which spkg to review here, properly format the correct patches to be applied, and post everything here. There's just too much confusion right now.

Nathann -- I would really like to see cliquer included in Sage, so if you need any help getting this in, please don't hesitate to contact me directly.


---

Comment by rlm created at 2009-07-01 14:56:20

As far as I could tell at Sage Days 16, the next step required for cliquer is: Someone needs to implement a build system for Cliquer, either using autotools or SCons. Given how simple cliquer is, SCons is probably the way to go, since this would be something like the one liner `Library('cliquer', ['foo.c', 'bar.c'])`.


---

Comment by ncohen created at 2009-07-07 13:16:19

I updated the SPKG file for cliquer.. This new one builds a shared library and I do not call any .c file in the cython code anymore !!

The address is still the same, though ;-)

Nathann


---

Comment by rlm created at 2009-07-13 18:56:12

Replying to [comment:3 ncohen]:
> I updated the SPKG file for cliquer.. This new one builds a shared library and I do not call any .c file in the cython code anymore !!

True, this builds a shared library, but it doesn't seem very portable. The problem is that the code you've written probably works only on systems very similar to yours. For example, when I try building on OS X (32- or 64-bit), I get:

```
ld: unknown option: -soname
collect2: ld returned 1 exit status
cp: cannot stat `libcliquer.so': No such file or directory

real	0m2.000s
user	0m0.465s
sys	0m0.190s
sage: An error occurred while installing cliquer-1.2
```


You need to use SCons or some form of autotools as I suggested above, for this to ever be a viable SPKG.


---

Comment by ncohen created at 2009-07-16 09:56:55

I just updated the SPKG, which now uses Scons !

Nathann


---

Comment by rlm created at 2009-07-16 18:45:51

Nathann,

This is great work! However, you are still hard-coding some Linux-isms in spkg-install:


```
scons && cp Build/libcliquer.so "$SAGE_LOCAL/lib/"
```


Unfortunately, on OS X, it is `libcliquer.dylib` that is built by SCons. Why don't you copy `Build/*` over, to include all cases? You should also delete the commented part from spkg-install. While I'm reviewing, you need a Mercurial repository in the base directory of the spkg, and the License section of SPKG.txt needs to be clarified (i.e. GPLv2+).

Keep up the good work!


---

Comment by ncohen created at 2009-07-17 18:18:57

All has been done according to your wishes ;-)

The spkg has been updated !


---

Comment by rlm created at 2009-07-17 18:28:41

1. You need to check in your changes to the repo!

2. You should add a line to `spkg-install` which copies header files to the right place, something like `cp src/*.h "$SAGE_LOCAL/include/cliquer/"`

3. This is all I can think of, so after this it's a lot of testing on different platforms.


---

Comment by ncohen created at 2009-07-17 18:34:30

done again ! ;-)


---

Comment by rlm created at 2009-07-17 18:42:39

Change `cliquer-1.2` to `cliquer` (twice) in `spkg-install`, so that we don't need to keep upgrading code in the Sage library when Cliquer upgrades.

After that, I think that this is ready to go! It builds successfully on 32-bit and 64-bit OS X and on sage.math.


---

Comment by ncohen created at 2009-07-17 18:46:21

Done. I have to change the patch though, as the directory changed.


---

Comment by rlm created at 2009-07-17 18:49:13

The spkg looks great! Nice work.

NOTE: This will be little useful without also merging #5793, when it is ready.

Nathann, shall we continue at #5793?


---

Comment by ncohen created at 2009-07-17 18:59:16

A small problem with the creation of a directory, and changes commited to the hg repository.


---

Comment by rlm created at 2009-07-17 19:01:52

Ah, you beat me to posting the same fix! :-)


---

Comment by rlm created at 2009-07-17 19:06:40

However, there is now a `cliquer-1.2.spkg` inside the spkg!!!


---

Comment by ncohen created at 2009-07-17 19:11:00

It comes from a tar command run in the wrong directory.... fixed ;-)


---

Comment by mvngu created at 2009-07-23 04:41:46

Resolution: fixed


---

Comment by mvngu created at 2009-07-23 04:41:46

The SPKG at

http://www-sop.inria.fr/members/Nathann.Cohen/cliquer-1.2.spkg

doesn't conform to the naming convention for SPKG's. I've renamed it as `cliquer-1.2.p0.spkg` and uploaded the renamed SPKG up at

http://sage.math.washington.edu/home/mvngu/patch/cliquer-1.2.p0.spkg

As far as I understand, this new SPKG doesn't depend on #5793. So I'm merging the SPKG into the standard SPKG repository.


---

Comment by mvngu created at 2009-07-26 08:27:34

See #6626 for a follow-up to this ticket.


---

Comment by mvngu created at 2009-07-26 08:30:25

Resolution changed from fixed to 


---

Comment by mvngu created at 2009-07-26 08:30:25

Changing status from closed to reopened.


---

Comment by mvngu created at 2009-07-26 08:30:25

I'm reopening this ticket until #6626 is fixed.


---

Comment by mvngu created at 2009-07-31 10:22:13

Are there any code or doctests to test the functionalities provided by this package? Any package that is merged in the standard package repository must be doctested by code in the Sage library.


---

Comment by ncohen created at 2009-07-31 10:25:37

The code/doctest related to cliquer is to be found in #5793 : almost all the functions of the Graph class related to cliques use it, and if I make no mistake I documented all of them ;-)


---

Comment by mvngu created at 2009-07-31 23:30:48

Resolution: fixed


---

Comment by mvngu created at 2009-07-31 23:30:48

Merged in standard package repository.
