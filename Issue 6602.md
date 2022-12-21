# Issue 6602: [with SPKG, need review] GLPK for SAGE

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-07-23 14:08:35

Assignee: jkantor

CC:  wstein mvngu

GLPK ( http://www.gnu.org/software/glpk/ ) is a Linear Program solver from GNU. It can also solve Mixed Integer Programs, and is needed for :
http://trac.sagemath.org/sage_trac/ticket/6502

More informations on :
http://groups.google.com/group/sage-devel/browse_thread/thread/9da47e06bcdfc49f


---

Comment by wdj created at 2009-07-25 23:24:51

I'm not sure what needs to be checked here. It installs fine on an amd64 ubuntu 9.04 machine and passes sage -testall.

Are there any tests I should run? I saw nothing on the url given in the ticket but I am not an OR person.

Positive review from me as far as I can tell, as an optional package.


---

Comment by ncohen created at 2009-07-26 00:09:45

I think that most of the tests of this spkg will be done in http://trac.sagemath.org/sage_trac/ticket/6502

I hope it will be possible to quickly include all of this into SAGE !! ( Oh, and this spkg is meant to be standard, not just optional !! )


---

Comment by mvngu created at 2009-07-26 02:13:50

It's rather difficult to include this SPKG when there are (as yet) no functions in the Sage library to test its functionalities. Once #6502 gets positive review, this SPKG could then be merged in the Sage standard packages repository.


---

Comment by mvngu created at 2009-07-26 02:18:51

We no longer use "SAGE". The days of that capitalization are over. Now use "Sage" instead.


---

Comment by mhampton created at 2009-07-31 23:01:51

I object to including this as standard just because of consistency concerns - I think this needs a vote on sage-devel.


---

Comment by wdj created at 2009-07-31 23:19:36

Note: I said "Positive review from me as far as I can tell, as an optional package. "


---

Comment by mvngu created at 2009-07-31 23:43:40

The proposal here is to merge the SPKG in the *optional* packages repository.


---

Comment by ncohen created at 2009-08-01 07:26:52

I forgot all about the voting process I immediately send a message on Sage-devel about it.

This package has to be included in the --standard-- package repository if we want Sage to have any native LP feature ( see #6502 ). Coin-or and Cplex are both GPL-uncompatible ;-)


---

Comment by ncohen created at 2009-08-01 07:42:40

The vote is going on there :
http://groups.google.com/group/sage-devel/browse_thread/thread/fed15c54478e8d5


---

Comment by wdj created at 2009-08-01 13:28:15

I could be wrong but I think trac is for optional packages. IIRC, once it is optional (ie, posted to http://www.sagemath.org/packages/optional/) then a public vote is carried out on sage-devel.


---

Comment by ncohen created at 2009-08-01 15:44:19

I did not know that !!!

I'm pretty new aboard, and the only thing I wrote for Sage was an interface for Cliquer, which has seemingly found a shortcut through all these steps ;-)

I may be in a hurry, but it is just because :
* I am impatient to see this patch accepted 
* I have already written several graph functions waiting to be included in the Graph class that I will not post until MIP is included into Sage 

Sorry again ! I'll try to be a bit more patient ;-)


---

Comment by mvngu created at 2009-08-02 08:28:39

Changing component from numerical to optional packages.


---

Comment by mvngu created at 2009-08-02 08:28:39

Changing assignee from jkantor to tbd.


---

Comment by mvngu created at 2009-08-04 09:15:35

Resolution: fixed


---

Comment by mvngu created at 2009-08-04 09:15:35

Merged in optional packages repository. The new optional package can be found here:

http://www.sagemath.org/packages/optional/glpk-4.38.spkg
