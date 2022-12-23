# Issue 9189: libgcrypt fails to build on Fedora 13

Issue created by migration from https://trac.sagemath.org/ticket/9189

Original creator: jsp

Original creation time: 2010-06-08 14:07:19

Assignee: GeorgSWeber


```
Hi Maurice,

> I'm trying to install sage-4.3.3 on fedora 13.
> Compiling the source i got the message :
> ------------------------------------------------------------------------
>
> /usr/bin/ld: register.o: undefined reference to symbol 'gpg_strerror'
> /usr/bin/ld: note: 'gpg_strerror' is defined in DSO
> /home/maurice/Public/sage-4.3.3/local/lib/libgpg-error.so.0 so try
> adding it to the linker command line
> /home/maurice/Public/sage-4.3.3/local/lib/libgpg-error.so.0: could not
> read symbols: Invalid operation
> collect2: ld returned 1 exit status
> make[4]: *** [register] Erreur 1
> make[4]: quittant le répertoire «
> /home/maurice/Public/sage-4.3.3/spkg/build/libgcrypt-1.4.4.p2/src/tests »
> make[3]: *** [all-recursive] Erreur 1
> make[3]: quittant le répertoire «
> /home/maurice/Public/sage-4.3.3/spkg/build/libgcrypt-1.4.4.p2/src »
> make[2]: *** [all] Erreur 2
> make[2]: quittant le répertoire «
> /home/maurice/Public/sage-4.3.3/spkg/build/libgcrypt-1.4.4.p2/src »
> failed to build libgcrypt
>
> real 1m51.070s
> user 1m4.656s
> sys 0m33.780s
>
> ------------------------------------------------------------------------
>
> If somebody knows what is missing ...
> Thanks
> Maurice
>
>

Same here on Fedora 13, 32 bit. I'll open a ticket.

Jaap

```




---

Comment by mhansen created at 2010-06-08 18:31:35

See http://groups.google.com/group/sage-support/browse_thread/thread/98ca4f3f25e223e9/a87f3e4c536871e0?lnk=raot for info on a fix.


---

Comment by mhansen created at 2010-06-08 19:19:33

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-06-08 19:19:33

I've put an spkg at http://sage.math.washington.edu/home/mhansen/libgcrypt-1.4.4.p3.spkg which should hopefully fix this issue.  I don't have access to a Fedora 13 box so someone needs to test it.


---

Comment by jsp created at 2010-06-08 20:28:16

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-06-08 20:28:16

This works on Fedora 13, 32 bit


```
Successfully installed libgcrypt-1.4.4.p3
You can safely delete the temporary build directory
/home/jaap/downloads/sage-4.4.3/spkg/build/libgcrypt-1.4.4.p3
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing libgcrypt-1.4.4.p3.spkg
[jaap@paix sage-4.4.3]$ 

```



Positive review.

Jaap


---

Comment by mhansen created at 2010-06-09 02:14:34

Resolution: fixed
