# Issue 9977: Add a test for the maths library in the 'prereq' script.

Issue created by migration from https://trac.sagemath.org/ticket/9978

Original creator: drkirkby

Original creation time: 2010-09-23 13:46:47

Assignee: drkirkby

CC:  jhpalmieri nthiery

The 'prereq' script in `$SAGE_ROOT/spkg/base` is currently version 0.7. This does not check that the maths library `libm` exists. I thought that was pretty much a formality, but it is not on AIX, where the shared maths library `/usr/lib/libm.a` does not get installed by default. 


```
-bash-4.1$ ls /usr/lib/libm*
/usr/lib/libmbx.a
```


The maths library is part of the `bos.adt` fileset. Hence a test for the maths library should be added. After installing `bos.adt`, so the maths library exists:


```
-bash-4.1$ ls /usr/lib/libm*
/usr/lib/libm.a       /usr/lib/libmbx.a     /usr/lib/libm_r.a     /usr/lib/libmsaa.a    /usr/lib/libmsaa_r.a
```


Dave


---

Comment by drkirkby created at 2011-03-28 18:01:36

Changing type from defect to enhancement.


---

Comment by drkirkby created at 2011-03-28 18:01:36

Changing status from new to needs_review.


---

Comment by drkirkby created at 2011-03-28 18:01:36

Changing component from AIX or HP-UX ports to build.


---

Comment by malb created at 2011-03-29 08:14:51

I read the patch and it looks good. I haven't tested it, though.


---

Comment by drkirkby created at 2011-03-29 08:26:49

Replying to [comment:2 malb]:
> I read the patch and it looks good. I haven't tested it, though.
Thank you.


---

Comment by drkirkby created at 2011-03-29 09:24:33

Here is some results when installed on my IBM RS/6000, which runs AIX 5.3. 


```
-bash-4.1$ uname
AIX
```


Here's the output after running "make" on the AIX system, which has the maths library installed, since the bos.adt fileset was installed. 


```
-bash-4.1$ uname 
AIX
-bash-4.1$ make

<snip irrelevant output>

Starting prerequisite check.
Machine: AIX aixbox 3 5 000245984C00
prereq-0.8/
prereq-0.8/install-sh
prereq-0.8/aclocal.m4

<snip out irrelevant output>

checking for sqrt in -lm... yes
checking for sqrtl in -lm... yes
configure: creating ./config.status
config.status: creating Makefile
config.status: creating config.h
config.status: executing depfiles commands
```


Then I removed the maths library, /usr/lib/libm.a.


```
-bash-4.1$ su
root's Password:
# mv /usr/lib/libm.a /usr/lib/foo
# exit
```


Then after running make, we see that the 'prereq' script exits with an error. 


```
checking for sqrt in -lm... no
configure: This system has no maths library installed.
configure: On AIX, this is in the bos.adt.libm fileset.
configure: Actually, we recommend to install the complete bos.adt fileset.
configure: This needs to be performed by a system administrator.
configure: error: Exiting, since a maths library was not found.
 ERROR: You do not have all of the prerequisites needed
 to build Sage from source.  See the errors above.
make[1]: *** [installed/prereq-0.8] Error 1
make[1]: Leaving directory `/home/users/drkirkby/sage-4.7.alpha1/spkg'

real    0m54.880s
user    0m29.577s
sys     0m10.611s
Error building Sage.
make: *** [build] Error 1
```


Finally, I did manage to remember to restore my maths library!


```
-bash-4.1$ su
root's Password:
# mv /usr/lib/foo /usr/lib/libm.a
# exit
-bash-4.1$ 
```



---

Comment by drkirkby created at 2011-03-29 23:18:48

Nicolas M. Thiéry wrote on sage-devel


```
I did not actually run the code, especially on AIX, but trust you did
(both with and without libm installed). Reading it sounds very
reasonable; I am thus ready to give it a positive review.

Quick variant:

    # On AIX libm is not installed by default - strange as that might seem -
    # While we are it, bos.adt is likely to contain other useful things for Sage
    if test "x`uname`" = 'xAIX'
    then
       AC_MSG_NOTICE([On AIX, libm is contained in the bos.adt.libm fileset.]) 
       AC_MSG_NOTICE([Actually, we recommend to install the complete bos.adt fileset.]) 

Cheers,
				Nicolas
```


The patch has been changed to include Nicolas's revised wording on the error message that is generated.


---

Comment by drkirkby created at 2011-03-29 23:19:46

Somehow I managed to remove John. I've put him back!


---

Attachment

Changes to the configure.ac file which check that sqrt exists in the maths library.


---

Comment by drkirkby created at 2011-03-30 16:24:40

New tar file. This does not need reviewing. Changes from prereq-0.7.tar are due to changes in the configure.ac file, which is in the tar file


---

Attachment

I realised that I had not used Nicolas's exact wording for one of the messages, which was better than my own. Hence I have rebuilt the tar file. I checked again on AIX, and this is what it produced when I temporarily removed the maths library `/usr/lib/libm.a`



```
checking for sqrt in -lm... no
configure: This system has no maths library installed.
configure: On AIX, libm is contained in the bos.adt.libm fileset.
configure: Actually, we recommend to install the complete bos.adt fileset.
configure: This needs to be performed by a system administrator.
configure: error: Exiting, since a maths library was not found.
 ERROR: You do not have all of the prerequisites needed
 to build Sage from source.  See the errors above.
make[1]: *** [installed/prereq-0.8] Error 1
make[1]: Leaving directory `/home/users/drkirkby/sage-4.7.alpha1/spkg'

real    0m55.207s
user    0m29.541s
sys     0m10.628s
Error building Sage.
make: *** [build] Error 1
```



---

Comment by nthiery created at 2011-03-30 17:17:04

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-05 11:59:57

Resolution: fixed
