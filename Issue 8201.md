# Issue 8201: Fortran not found on Linux if gfortran not present

Issue created by migration from Trac.

Original creator: mraum

Original creation time: 2010-02-06 19:09:33

Assignee: Martin Raum

CC:  mvngu

Keywords: fortran

The spkg-install script on Linux first checks "which gfortran" and if no instance is found it aborts. This is a problem if for example the binary is gfortran-4.3. Then sage won't build.

Even then scipy won't build, because as soon as compiler flags are passed in scipy's setup.py, the fortran compiler is not found anymore. This happens because "sage_fortran" is our binary/script but it should be a stardard name. Scipy will have to care for the -fPIC flags.

This is related to #8049 !


---

Comment by mraum created at 2010-02-06 19:10:45

Reorganized spkg-install


---

Comment by mraum created at 2010-02-06 19:11:06

Changing status from new to needs_review.


---

Attachment


---

Comment by mraum created at 2010-02-08 20:04:48

Correcting a build error that occured with 4.3.2


---

Comment by drkirkby created at 2010-02-21 23:54:03

Changing status from needs_review to needs_info.


---

Attachment

What happens if you set SAGE_FORTRAN to /usr/local/bin/gfortran-4.3 ? 

You might find that is all you need, as perhaps 'which' will not be called then. The whole idea of SAGE_FORTRAN is to specify the Fortran compiler. I do wonder if it might not be less hassle to just create a link so there is a program called 'gfortran'. 

Have you checked this on Solaris 10? It is the sort of thing that could screw up on there as there are lots of code changes. 

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by mraum created at 2010-02-22 07:08:16

SAGE_FORTRAN is ignored, if gfortran doesn't exist. Namely, the script will abort. That's why I had to create a patch. Creating links for gfortran is a hack would most probably create new problems anywhere else at another time. Moreover, I don't have admin rights.
I don't have access to Solaris; And I don't have experience with it. But if the GNU suit is installed it should work; if not it won't, but scipy has to blamed for this not fortran itself.
If you can test this on Soloaris I would be happy to integrate any changes you suggest.


---

Comment by mraum created at 2010-02-22 07:08:16

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-02-22 17:46:12

Replying to [comment:3 mraum]:
> SAGE_FORTRAN is ignored, if gfortran doesn't exist. 

> Namely, the script will abort. That's why I had to create a patch. Creating links for gfortran is a hack would most probably create new problems anywhere else at another time. 

What makes you think a symbolic link is a hack? It is very standard practice on Unix systems to create symbolic links for this very purpose. There are loads of them created in Sage. (Some people call them soft links). 

Many shell scripts start 

```/bin/sh
```


But most linux distros do not have a program called /bin/sh. Rather /bin/sh is simply a link to bash, dash or some other shell. On sage.math


```
kirkby`@`sage:~$ ls -l /bin/sh
lrwxrwxrwx 1 root root 4 2010-02-02 13:49 /bin/sh -> dash
kirkby`@`sage:~$ ls -l /bin/dash
-rwxr-xr-x 1 root root 100856 2009-03-09 06:18 /bin/dash
```


When you type 'sh' on sage.math you are really running 'dash'

> Moreover, I don't have admin rights.

You don't need admin rights to create a symbolic link. Something like:


```
$ ln -s /usr/local/bin/gfortran-4.2 $HOME/bin/gfortran
```


will do fine. Then make sure $HOME/bin is in your path before /usr/local/bin. Your will then have 'gfortran'. 

> I don't have access to Solaris; And I don't have experience with it. But if the GNU suit is installed it should work; if not it won't, but scipy has to blamed for this not fortran itself.


Do you have an account on sage.math or similar? If so, you have an account on 't2' - or if not, one is easily created. For all practical purposes you will not find it significantly different from Linux. 

> If you can test this on Soloaris I would be happy to integrate any changes you suggest. 

Unfortunately, I simply do not have time to test everyones changes on Solaris - let alone generate patches if they do not work. 

http://www.sagemath.org/doc/developer/inclusion.html

makes it clear that for a package to be included in Sage, it must support Solaris. 

*Some Sage developers are willing to help you port to OS X, Solaris and Windows. But this is no guarantee and you or your project are expected to do the heavy lifting and also support those ports upstream if there is no Sage developer who is willing to share the burden.*

Your solution seems like a _sledgehammer to crack a walnut_ if you know what I mean by that. A symbolic link has far greater chance of just working, without risking breaking things for everyone else. In stead you propose making changes that could impact anyone, without actually testing them. 

*I'm marking this as wontfix, as I believe the patch is unnecessary. You may find another reviewer see this differently, though I doubt you will find any experienced system administrator see it that way* 

Dave


---

Comment by drkirkby created at 2010-02-22 17:46:12

Resolution: wontfix


---

Comment by AlexGhitza created at 2010-02-22 22:30:22

Dave, please have a look at the trac guidelines:

http://wiki.sagemath.org/devel/TracGuidelines

More specifically, the paragraph about closing tickets: "No Closing Or Invalidating: Unless you have admin powers in trac (which includes all the people who have ever done releases of Sage), do not close tickets unless you are explicitly told to do so. Since we have email notification now this has become less of an issue. If you think that a ticket is invalid or has been fixed, just comment on it and the current release manager will take a look and close it if appropriate."


---

Comment by drkirkby created at 2010-02-22 23:08:49

Thank you Minh. I was not aware of that. 

Dave


---

Comment by drkirkby created at 2010-02-22 23:10:35

Minh, I just realised I left this as closed. Perhaps you can open it and select what you feel is most appropriate - needs work/ need review/ wontfix etc. 

Sorry for the problem, but I do feel this ticket is potentially risky, untested, and is almost certainly better served by creating a symbolic link. 

Dave


---

Comment by drkirkby created at 2010-02-22 23:17:19

Oops, I realised it was Alex this pointed out this policy, not Minh. 

Anyway, Sorry for the problem. I still stand by the fact I do not think the patch should be integrated. 

Dave


---

Comment by mvngu created at 2010-02-23 02:49:09

Replying to [comment:7 drkirkby]:
> Minh, I just realised I left this as closed. Perhaps you can open it and select what you feel is most appropriate - needs work/ need review/ wontfix etc. 

I'm leaving this as "wontfix". If there's a need in the future to address this issue again, open another ticket, but refrain from reopening tickets. A few months ago, only trac administrators had power to close tickets. After some changes to trac, in particular moving to the new process for working on tickets, every suddenly has the power to close tickets. This is the source of the "every can close tickets" problem we're seeing right now.


---

Comment by mvngu created at 2010-02-23 02:50:19

Replying to [comment:9 mvngu]:
> "every can close tickets" problem we're seeing right now.

"everyone", that is.
