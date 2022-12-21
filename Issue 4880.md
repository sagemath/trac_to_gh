# Issue 4880: [with spkg, needs review] Improved experimental spkg vtk-5.2

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-12-26 15:15:28

Assignee: mabshoff

CC:  schilly

Made vtk-5.2 more fashionable:

* moved VTK and VTKData to src/

* test for the installation of cmake-2.4.8 If it is not installed, we install it.

[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.spkg)

No changes IN VTK and VTKData

Somebody should look into spkg-install and make it work on OSX.

Jaap


---

Comment by cwitty created at 2009-02-04 05:40:32

This worked great for me, and I belive for Jason Grout.  I vote in favor of promoting this version to experimental  (I compiled and used the package, but did not look at the spkg.)


---

Comment by mabshoff created at 2009-02-07 01:44:28

Harald, 

what is the status of adding spkgs to the repo? Should I wait until we switch before uploading this?

Cheers,

Michael


---

Comment by schilly created at 2009-02-07 11:05:30

Replying to [comment:2 mabshoff]:
> what is the status of adding spkgs to the repo? Should I wait until we switch before uploading this?
> 

well, i'm not sure, the new server shouldn't change any more so i would suggest to upload it on the new server, same place and everything like with the old one, and it just takes some days until it is public. (or upload it on both?)


---

Comment by jsp created at 2009-02-26 19:31:04

This is taking way to long!

Remember this is experimental!!!!

The spkg only change is spkg-install and SPKG.txt, no changes in src!

In the mean time I have a vtk-5.2.1.spkg

See:
[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg)

Should we close this ticket and open a new one?

Jaap


---

Comment by mabshoff created at 2009-02-26 22:48:58

Replying to [comment:4 jsp]:

Hi Jaap,

> This is taking way to long!

The problem was that due to the transition from modular to the new image spkg uploads were frozen. Now that the new server has stabilized things should be moving again and this ticket has been looking accusingly at me to get moving every time I skim the tickets with positive review :)

> Remember this is experimental!!!!

See above - it has nothing to do with experimental.

> The spkg only change is spkg-install and SPKG.txt, no changes in src!
> 
> In the mean time I have a vtk-5.2.1.spkg
> 
> See:
> [http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg)
> 
> Should we close this ticket and open a new one?

No, I just changed the summary and will upload this once I get started merging tonight.

> Jaap
> 

Sorry for the delay, it should get better soon and you should have complained more ;)

Cheers,

Michael


---

Comment by jsp created at 2009-03-16 13:55:56

Replying to [comment:5 mabshoff]:
> Replying to [comment:4 jsp]:
[...]
> 
> No, I just changed the summary and will upload this once I get started merging tonight.
> 
> > Jaap
> > 
> 
> Sorry for the delay, it should get better soon and you should have complained more ;)
> 


Let me complain once more!

Jaap


---

Comment by mabshoff created at 2009-04-01 05:29:49

Merged in the Sage 3.4.1 release cycle by uploading the vtk-5.2.1.spkg to the experimental spkg repo.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-01 05:29:49

Resolution: fixed
