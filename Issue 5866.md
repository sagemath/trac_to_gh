# Issue 5866: Fix freetype build on systems where make is not GNU make.

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2009-04-23 06:51:35

Assignee: mabshoff

Change 'make' to ${MAKE} - is the recommended way to recursively invoke make to ensure that the subordinate make is the same as the parent make (and also ensures that the two make instances will communicate on things like '-jX').

Explicitly export the parent make into the configure script.

These changes avoid problems on systems like FreeBSD where make is not GNU make.


---

Attachment


---

Comment by mabshoff created at 2009-04-23 07:30:31

I will work on integrating this tomorrow.

Cheers,

Michael


---

Comment by mhansen created at 2009-06-20 02:17:45

Looks good to me.

The spkg with this change incorporated can be found at http://sage.math.washington.edu/home/mhansen/freetype-2.3.5.p1.spkg


---

Comment by mhansen created at 2009-06-20 02:17:45

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-20 02:17:45

Changing assignee from mabshoff to mhansen.


---

Comment by rlm created at 2009-07-02 22:08:33

Resolution: fixed


---

Comment by drkirkby created at 2010-06-10 07:31:46

I'll create a new ticket for this issue, but I thought it useful to add to this ticket. 

I tried to update freetype to the latest version (2.3.12), but the build fails with:


```
libtool: link: (cd "/export/home/drkirkby/32/sage-4.4.3/spkg/build/freetype-2.3.12/src/objs/.libs" && rm "libfreetype.so.6" && ln -s "libfreetype.so.6.4.0" "libfreetype.so.6")
libfreetype.so.6: No such file or directory
make: *** [/export/home/drkirkby/32/sage-4.4.3/spkg/build/freetype-2.3.12/src/objs/libfreetype.la] Error 2

real    3m16.562s
user    2m54.021s
sys     0m22.112s
sage: An error occurred while installing freetype-2.3.12
```


Changing spkg-install to 


```
if [ "x`uname`" != xSunOS ] ; then 
   GNUMAKE=${MAKE} ./configure --prefix="$SAGE_LOCAL"
else
  ./configure --prefix="$SAGE_LOCAL"
fi
```


allows the latest freetype to build on Solaris 10 on SPARC.


---

Comment by drkirkby created at 2010-06-10 07:34:18

I should have added that 'make' is a version of GNU make on Solaris, as Sun's make will never build Sage. The MAKE environment variable was not set. 

Dave
