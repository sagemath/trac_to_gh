# Issue 8178: zn_poly fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-02-03 18:58:37

Assignee: drkirkby

Setting SAGE64=yes has only effect in this package in OSX Darwin.

To let this work on Open Solaris and evt. other platforms we changed
spkg-install and patches/makemakefile.py a little bit.

A patch is coming up.

Jaap




---

Attachment


---

Comment by jsp created at 2010-02-03 19:44:10

The spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p2.spkg)



```
jaap`@`opensolaris:~/Downloads/sage-4.3.2.alpha0$ file local/lib/libzn_poly*
local/lib/libzn_poly-0.9.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libzn_poly.a:	current ar archive, not a dynamic executable or shared object
local/lib/libzn_poly.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped

```



Jaap


---

Comment by jsp created at 2010-02-03 19:44:10

Changing assignee from drkirkby to jsp.


---

Comment by jsp created at 2010-02-03 19:44:48

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-02-04 17:10:53

To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit.


---

Comment by drkirkby created at 2010-02-04 17:10:53

Changing status from needs_review to needs_work.


---

Attachment

Replying to [comment:3 drkirkby]:
> To avoid the risk of messing something up for everyone, I would make the chances in patches/makemakefile.py to specific to Solaris on 64-bit. 


I think it is pritty harmless to add $LDFLAGS here. If you don't agree I leave this one to you. I've enough of -m64 :)

Jaap


---

Comment by jsp created at 2010-02-04 18:56:36

And oops, I was on the wrong page. How can I remove an attachement?

Jaap


---

Comment by jsp created at 2010-02-04 19:00:19

Changing assignee from jsp to drkirkby.


---

Comment by jsp created at 2010-02-04 19:00:19

Accidently changed owner to jsp. This happens while scrolling down the page with
the mouse wheel.

Jaap


---

Comment by drkirkby created at 2010-02-04 19:09:38

Unless this has been checked on several systems, I would prefer not to commit it now.


---

Comment by jsp created at 2010-02-04 20:02:45

One more comment. Look at this from the spkg-install file:



```
if [ "x$SAGE64" = xyes ]; then
   echo "64 bit build"
   CFLAGS="-O3 -g -m64 -fPIC -L."; export CFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
   cp patches/makemakefile.py src/makemakefile.py
elif [ `uname` = "SunOS" -a "`ld  --version  2>&1  | grep GNU`" = ""  ]; then
   # Change -soname to -h if the Sun linker is used. 
   sed 's/-soname/-h/g' src/makemakefile.py > /tmp/makemakefile.py.$$
   mv /tmp/makemakefile.py.$$ src/makemakefile.py
   CFLAGS="-fPIC -O3 -L."; export CFLAGS
   LDFLAGS=""; export LDFLAGS
else
   CFLAGS="-fPIC -O3 -L."; export CFLAGS
   LDFLAGS=""; export LDFLAGS
fi

```


You see LDFAGS is empty except when SAGE64=yes. For now Darwin and SunOS x64 64 bit.

Only in this case the patches/makemakefile.py is copied. The darwin case is resolved first (even without using the LDFLAGS :) ), see the makefile.

Remains the building of the .so file in our case and that definitely needs the
LDFLAGS set to -m64.

If you don't accept this reasoning, I rest my case.


Cheers,

Jaap


---

Comment by jsp created at 2010-02-04 20:02:45

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-02-21 00:12:20

OK, I accept your reasoning. However #8280 got .p2 first, so you will need to create a version against that. 

Once you have done that, I'll convert this to a positive review. 

Dave


---

Comment by drkirkby created at 2010-02-21 00:12:31

Changing status from needs_review to needs_work.


---

Attachment

The new spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg)

See also the new attachment.

Jaap


---

Comment by jsp created at 2010-02-21 17:52:25

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-02-21 23:31:23

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 23:16:32

Merged [zn_poly-0.9.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zn_poly-0.9.p3.spkg) in the standard spkg repository.


---

Comment by mvngu created at 2010-03-02 23:16:32

Resolution: fixed
