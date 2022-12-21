# Issue 8172: Support for CPLEX

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-02-03 13:04:21

Assignee: jkantor

CC:  malb schilly

This patch enables support for Cplex, when the new package #8171 for CBC is installed. It also includes several lines of documentation to explain how CPLEX can be used, and fixes a bad docstring which I noticed while testing this package :-)

Nathann


---

Comment by ncohen created at 2010-02-03 13:06:05

Changing status from new to needs_review.


---

Comment by malb created at 2010-02-03 14:22:24

You are doctesting `solve_coin` in `solve_cplex`


---

Comment by ncohen created at 2010-02-03 14:34:26

OOps :-)

The code from mip_cplex is a pure copy of mip_coin ( I only needed to change the types from OsiCbcSolverInterface to OsiCplexSolverInterface, etc .... )

This code has already been reviewed, by the way.....

Fixed ! Thank you :-)

Nathann


---

Comment by malb created at 2010-02-03 14:38:53

I wonder if we can factor out the differences and this way would make it very very easy to hook up new solvers (with say, some function pointers and such) The redundancy of copying a function does not seem very elegant to me.


---

Comment by ncohen created at 2010-02-03 14:50:34

I do not like it either, but this way it answers two other difficulties :

*  Coin me be compiled independently from the presence of CPLEX. So I can not be assume in mip_coin that CPLEX libraries are available and that this file *can* actually be compiled.

*  Testing for the presence of a CPLEX solver amounts to try to import solve_cplex, which is nice and can only be done if the file has been compiled successfully

Nathann


---

Comment by malb created at 2010-02-03 15:07:12

We could still reduce the amount of code duplication. Say we replace the functions `solve_*` by instances of a class `OSISolver` which would get function pointers pointing to the correct function to call for each solver and have a call method which implements the current `solve_*` function. So for each new solver we'd only need to add a new instance. All the points you raise above would be addressed.


---

Comment by ncohen created at 2010-02-03 17:07:47

Hmm.. It is almost done, but I have a few problems with cimporting in mip_cplex the c_solve function defined in mip_coin.... :-)


---

Comment by ncohen created at 2010-02-05 17:14:13

Ok, I have spent 3 or 4 hours dealing with this bug, if you want to give it a try it is almost finished : we but have to find a way to import this *********** function...

I'm sorry for my rudeness, but I can not stand these stupid error messages anymore !

Nathann


---

Comment by ncohen created at 2010-02-05 17:18:33

If you can fix it, I will obviously finish to clean the patch....

Nathann


---

Comment by drkirkby created at 2010-02-22 00:41:50

What platforms has this been tested on? It needs to work on OS X, Linux and Solaris. It's not clear from reading this that anyone has actually checked it works on Solaris. 

There's general information about building on Solaris at

  http://wiki.sagemath.org/solaris

 Information specifically for 't2' at

  http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

 Both the source (4.3.0.1 is the latest to build on Solaris) and a binary
 which will run on any SPARC can be found at http://www.sagemath.org
 /download-source.html

 Dave


---

Comment by drkirkby created at 2010-02-22 00:41:50

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2010-02-22 17:05:36

Here is a new *WORKING* version of the patch :-)

I received plenty of help, and it can finally be used !!

I can not test this piece of code on all these platforms. Anyway, CPLEX will be used by very few users of Sage as it already requires one to have a licence, which is pretty expensive ! ;-)

Nathann


---

Comment by ncohen created at 2010-02-22 17:05:36

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2010-02-25 17:12:53

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-02-26 11:08:08

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-02-26 11:08:08

New version of this patch... 

 * It now handles exceptions
 * I added options to have Cbc work multithread when the user wants it
 * I refactored some code which is now much more readable
 * I rounded some values in the docstrings, as Cplex behaves a bit differently from it friends concerning numerical noise

This patch can now be reviewed, and will be a nice addition whether one uses Cplex or not because of the multithread ! :-)

Nathann


---

Comment by ncohen created at 2010-03-08 15:42:00

Cplex seems to be freely available for academics and students :

http://www.ibm.com/developerworks/forums/thread.jspa?threadID=319342&tstart=0

Nathann


---

Comment by drkirkby created at 2010-03-08 16:33:34

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-03-08 16:33:34

I understand you feel this would be useful, especially given CPLEX is available free for academics and students. (I'm neither a student or academic, so can't get a copy free myself). Given CPLEX is available for OSX, Solaris on both SPARC and x86, I believe it would be wise that you test it on those platforms.

You do have access to 't2' (Solaris) and 'bsd' (OS X) I assume. 

Testing on Solaris or OS X is not necessary for an experimental package (I'm not sure about optional), but certainly it would never be accepted as standard if it did not build on Solaris or OS X. I'm not quite sure where this package aims to fit (standard/experiemental/optional). That would dictate whether it needs to build on Solaris and OS X. 

I've put to 'need info' so you can clarify this for us. 

Dave


---

Comment by malb created at 2010-03-09 16:56:02

* it seems you define `ctypedef struct c_OsiSolverInterface "OsiSolverInterface"` a few times in a few different files. Why?
 * CPLEX has a few `# optional - requires Cbc`
 * Why did you change `log=False` to `log=0`? Also the docstring does not match anymore.
 * `# a hand-made memset` why don't you just call memset?


---

Comment by malb created at 2010-03-09 16:57:01

Btw. applies cleanly and builds fine on sage.math


---

Comment by ncohen created at 2010-03-09 20:17:52

Hello !!!

 * ctypedef repeated : fixed
 * optional cbc : fixed
 * because Cbc has several levels of output. Cplex too, perhaps, nce I will know how to tune it :-)
 * because I did not know where to find the memset function : fixed

Thank you very much for your help ! I just updated the patch :-)

Nathann


---

Comment by ncohen created at 2010-03-09 20:24:54

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2010-03-09 20:24:54

About tests on other platforms : Cbc, GLPK and obviously CPLEX will never be made standard packages because of license incompatibilities. I am still looking for a totally free solver but haven't found one yet, nor do I hope to ever find (an efficient) one.

I am really sorry but I can not say I will find the time to test them on these platforms. I do not know them, and even if it worked I have no idea of how to make platform-dependent fixes... :-/

Nathann


---

Comment by malb created at 2010-03-10 11:42:07

I just ran doctests on OSX (32-bit I think, its bsd.math). I think we should only worry about the patch on all platforms. If the optional package fails on say Solaris we can deal with this later.


---

Comment by malb created at 2010-03-10 11:42:26

Can we allow the same number of threads parameter for CPLEX?


---

Comment by ncohen created at 2010-03-10 11:55:44

I have to admit I do not know... The function I use to set Coin to n threads is Coin-specific. Cplex is used through the Osi interface, which is a good way to quickly add new solvers, but also means that I can not access a solver-specific function when the interface does not let me do it.

On the other side, Cplex is not free, and the multithreaded version is even more expensive. I have no access to a multithreaded version, but I sent a request for a free licence and I am still waiting for the answer ... With a bit of luck, the licence will let me use this mode and I will be able to take a more serious look at it :-)

Nathann


---

Comment by malb created at 2010-03-10 12:00:11

Dave, do you object if we give this ticket a positive review?


---

Comment by drkirkby created at 2010-03-10 23:55:54

Replying to [comment:23 malb]:
> Dave, do you object if we give this ticket a positive review?

Since it is optional, I think this can go without it building on Solaris. But I would draw Nathann's attention to the developers guide, in particular:

http://www.sagemath.org/doc/developer/inclusion.html?highlight=solaris

*Some Sage developers are willing to help you port to OS X, Solaris and Windows. But this is no guarantee and you or your project are expected to do the heavy lifting and also support those ports upstream if there is no Sage developer who is willing to share the burden.*

However, since this is not a standard package, then I think it can go. 

It was not clear to me on the #8171 whether that was intended to be experimental or optional. I believe the requirements for optional are more stringent than experimental, but I don't know exactly that they are. I believe Building on Solaris and OS X might be a requirement for optional, but are certainly not for experimental. I think that point needs clarification at some point in the future. 

I'm feel unable to review this, as it is outside my area, so if Micheal feels it deserves a positive review, then go ahead, but do not put my name on it. 

Note also the "Author" field is not completed.

Dave


---

Comment by drkirkby created at 2010-03-11 11:48:46

A couple of points which I believe are important before this gets a positive review. 

 * The patch is based on #8171, which at the very least needs clarification as to whether it is optional or experimental. Despite being a new package, it starts with .p2. I've asked for clarification on whether #8171 is expected to be 'experimental' or 'optional'. 

 * I've asked on sage-devel for clarification of whether building on Solaris is a requirement for optional packages. If so, (as I expect it is), then I believe that package (and this patch) should be checked on Solaris before getting a positive review.


---

Comment by ncohen created at 2010-03-11 12:42:02

Hello !!

As Martin mentionned it on #8171, the Cbc package is to be optional, exactly as it currently is. After all, #8171 is just an update. The .p2 is present precisely because it is an update. I hesitated before writing it, though, as the version of Cbc also changed. Do we increase the p# when the version of the source is fixed, and change it otherwise ? As the source changed (I updated it), do I need to "go back" to p0 ?

To be frank, I have in the end no idea of what exactly Solaris is. I know I can check it on the internet very quickly, and this is exactly what I intend to do, but in the end this is where my knowledge of it will stop. I have absolutely no idea how to deal with it...

Nathann


---

Comment by drkirkby created at 2010-03-11 14:31:42

Replying to [comment:26 ncohen]:
> Hello !!
> 
> As Martin mentionned it on #8171, the Cbc package is to be optional, exactly as it currently is. After all, #8171 is just an update. The .p2 is present precisely because it is an update. I hesitated before writing it, though, as the version of Cbc also changed. Do we increase the p# when the version of the source is fixed, and change it otherwise ? As the source changed (I updated it), do I need to "go back" to p0 ?

Neither. See:

http://www.sagemath.org/doc/developer/patching_spkgs.html

If the version is changed from the upstream source code, then the new package should be called by that version number, and nothing else - not even p0. Once the first patch to that is made, it becomes p0. 

> 
> To be frank, I have in the end no idea of what exactly Solaris is. I know I can check it on the internet very quickly, and this is exactly what I intend to do, but in the end this is where my knowledge of it will stop. I have absolutely no idea how to deal with it...
> 
> Nathann

Solaris is a Unix operating system. Unlike Linux, which is a Unix-like operating system, Solaris is officially classified as a POSIX compliant Unix operating system. It was created by Sun, who were recently bought by Oracle for $7 billion. Sage builds on Solaris 10 and soon will be an officially supported operating system, just as some linux distributions are. 

't2', which people refer to is a Sun T5240 machine with two SPARC processors. (The SPARC processor is similar to the Intel/AMD processors, though not identical). Each processor has 64-threads (128 in total). 

For any package to become a standard part of Sage, then it will need to build on Solaris 10 on SPARC. I'm unsure of the situation with optional packages. I don't mind helping if you have specific problems, but I am not going to do all the testing for you. 

When I checked the IBM web site, the library was available for Solaris. 

dave


---

Comment by malb created at 2010-03-11 18:37:29

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-03-12 08:59:51

Hello !

I just tried to log on t2 but my password was refused. This is a bit weird as I should not even be asked for a password as I set my ssh key in authorized_keys, but it looks like this server does not know me. Is there something special to do to log on it which is different from the procedure applied for sage.math ?

Nathann


---

Comment by dimpase created at 2010-03-20 04:46:58

Hi,
do you understand how to request an "academic" license for CPLEX?

I went to the IBM website and registered as an academic user and downloaded
the stuff, and can even compile and link CPLEX examples, but I cannot figure out where and how to get a licence (it does not come with the download...)
Thanks,
Dima


---

Comment by dimpase created at 2010-03-20 05:11:57

Replying to [comment:30 dimpase]:
> Hi,
> do you understand how to request an "academic" license for CPLEX?

OK, I figured it out:
here are the details:

[http://download.boulder.ibm.com/ibmdl/pub/software/dw/university/support/ILOGQuickStart.pdf](http://download.boulder.ibm.com/ibmdl/pub/software/dw/university/support/ILOGQuickStart.pdf)

First, one has to register here:
[https://www.ibm.com/developerworks/university/software/get_software.html](https://www.ibm.com/developerworks/university/software/get_software.html)

and after somewhat tedious registration get to download a zip archive, that
contains tarballs of several Linux, MacOS, and Solaris binary installations.
Install the right tarball somewhere.

Licence can be requested here:
[https://www.ibm.com/developerworks/university/support/ilog.html](https://www.ibm.com/developerworks/university/support/ilog.html)

you will get a file named access.ilm that you e.g. can place into /usr/ilog/ilm/
(or you can go for a custom location and an environment variable to hold it (see the quickstart pdf linked above)

Dima


---

Comment by ncohen created at 2010-03-20 11:32:19

From the tests done in my lab since we are using this new license ( we were using CPLEX 10 before ), this one is *much* faster, especially for integer multiflows.

Nathann


---

Comment by dimpase created at 2010-04-09 05:38:49

Replying to [comment:32 ncohen]:
> From the tests done in my lab since we are using this new license ( we were using CPLEX 10 before ), this one is *much* faster, especially for integer multiflows.
> 
> Nathann

works for me with the free academic CPLEX license on Linux x86_64 Debian!


---

Comment by dimpase created at 2010-04-09 06:34:46

fixed few places where "Mixed Integer" was omitted


---

Attachment

Replying to [comment:33 dimpase]:
> Replying to [comment:32 ncohen]:
> > From the tests done in my lab since we are using this new license ( we were using CPLEX 10 before ), this one is *much* faster, especially for integer multiflows.
> > 
> > Nathann
> 
> works for me with the free academic CPLEX license on Linux x86_64 Debian!

Good work!
I am giving it a positive review, subject to the patch being updated to the one I just uploaded (that adds Mixed Integer here and there, to avoid a confusion stemming from the fact that Sage does have an LP solver, from cvxopt)

Dima


---

Comment by ncohen created at 2010-04-09 07:09:28

Excellent ! I looked at the result of "diff" on the two patches, and I agree with your changes ! :-)

Nathann


---

Comment by ncohen created at 2010-04-09 07:11:01

Now the two patches are the same, just to avoid confusion... ;-)

Nathann


---

Comment by was created at 2010-04-29 05:16:38

Resolution: fixed


---

Attachment
