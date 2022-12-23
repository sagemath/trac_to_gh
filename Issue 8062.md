# Issue 8062: New givaro-3.2.13rc2.p0.spkg works with Open Solaris 64 bit, SAGE64="yes"

Issue created by migration from https://trac.sagemath.org/ticket/8062

Original creator: jsp

Original creation time: 2010-01-25 21:23:19

Assignee: drkirkby

Let spkg-install work with SAGE64="yes" on Open Solaris.

[http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg)

Jaap




---

Comment by jsp created at 2010-01-25 21:23:35

Changing status from new to needs_review.


---

Attachment


---

Comment by drkirkby created at 2010-01-28 08:44:40

Changing status from needs_review to needs_work.


---

Attachment

The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris. 


A more accurate comment would be. 

Ensures the compiler flag -m64 is added when the environment variable SAGE64 was set to yes - previously this was only happening on OS X. This should aid building 64-bit on any platform, though it has only been tested on Open Solaris. 

Also, add the trac ticket number #8062 to the comment. 

It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. 

You might want to remove Martin Albrecht as a maintainer, as his name is duplicated.


---

Comment by jsp created at 2010-01-28 11:42:26

Replying to [comment:2 drkirkby]:
> The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris. 
> 
> 
> A more accurate comment would be. 
> 
> Ensures the compiler flag -m64 is added when the environment variable SAGE64 was set to yes - previously this was only happening on OS X. This should aid building 64-bit on any platform, though it has only been tested on Open Solaris. 
>

That maybe better, but rather long for a short comment.
 
> Also, add the trac ticket number #8062 to the comment. 
> 
> It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. 
>

Sure that is a possibility. I've seen a lot of SPKG.txt files without trac numbers.

> You might want to remove Martin Albrecht as a maintainer, as his name is duplicated. 

That is what I did. As you can see in the patch.

Jaap


---

Comment by jsp created at 2010-01-28 13:11:48

Changing status from needs_work to needs_review.


---

Attachment

Updated SPKG.txt

Left patch level p0.

Link is still
[http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg)


Jaap


---

Comment by drkirkby created at 2010-01-28 13:39:19

Positive review. All dynamic libraries are 64-bit. I don't know how one can determine this with static libraries, as 'ldd' does not indicate anything about them. But I assume they are probably ok


```
drkirkby@hawk:~/sage-4.3.1$ file local/lib/libgivaro*
local/lib/libgivaro.a:	current ar archive, not a dynamic executable or shared object
local/lib/libgivaro.la:	commands text
local/lib/libgivaro.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libgivaro.so.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libgivaro.so.0.0.2:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```


It would be worth trying to find out a way of confirming the exact type of static libraries, but I think the fact the shared libraries are ok, this patch is fine. 

Dave


---

Comment by drkirkby created at 2010-01-28 13:39:19

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:16:55

Resolution: fixed
