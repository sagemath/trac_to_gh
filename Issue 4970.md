# Issue 4970: modify tkinter detection in our python spkg so that it works on macs

Issue created by migration from https://trac.sagemath.org/ticket/4970

Original creator: was

Original creation time: 2009-01-13 14:12:13

Assignee: mabshoff

CC:  dunfield

This is from a sage-support thread:

```
Hi Michael

thanks a lot! Tkinter is now working fine for me and I can use
matplotlib with the TkAgg backend
For the record, here are the steps I followed to get it working on Mac
OS (10.4 and 10.5)
1) Download the Tcl/Tk sources
2) Compile the unix version (of Tcl and Tk) as follows
./configure --enable-framework --disable-xft, make, make install
3) Modify the setup.py file in the src directory of python-2.5.2.p8 by
putting
/System/Library  underneath /Library/Frameworks at the top the
function detect_tkinter_darwin
4) run ./spkg-install in python-2.5.2.p8
5) reinstall matplotlib: sage -f matplotlib-0.98.3.p4

As this is the way Apple recommends to do it in the developer
documentation. I suggest that
the fix in the function detect_tkinter_darwin of the python-2.5.2.p8
setup.py gets included in the official Sage release. People needing
Tkinter on mac would then just need to have Tcl/Tk without
xft installed before compiling Sage.

Best wishes and thanks for the great job you are doing with the Sage
developers and maintainers,
Eric
```



---

Comment by mabshoff created at 2009-02-13 17:33:10

I will do this during the upgrade to Python 2.5.4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 06:17:28

Replying to [comment:1 mabshoff]:
> I will do this during the upgrade to Python 2.5.4.

I did not do this in the python-2.5.4.spkg update since we have for now disabled support of TkAgg in MPL since it caused exceptions in the plotting code on systems where no X was installed and/or not running. We can resolve this problem in two ways:

 * conditionally reenable TkAgg support in MPL
 * fix the issue in MPL or at least catch the exception and just ignore it
 
> Cheers,
> 
> Michael

Anyway, I am attaching a patch on top of the python-2.5.4.spkg that can be used as the basis to make this happen on OSX once we sorted out the TkAgg issue.

Bumping to 3.4.1.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-02-16 06:27:39

trac_4970-potential-fix.patch is an untested prototype patch. Given that we fixed the libpng problem which triggered all this in the first place we might not even need any of the above modifications. 

Cheers,

Michael


---

Comment by dunfield created at 2015-01-06 13:45:48

As of January 2015, Tkinter works out-of-the box on OS X with any recent source or binary release of Sage, so the patch here isn't needed anymore.


---

Comment by dunfield created at 2015-01-07 15:22:39

Changing status from needs_work to positive_review.


---

Comment by dunfield created at 2015-01-07 15:27:54

Changing assignee from mabshoff to dunfield.


---

Comment by vbraun created at 2015-01-13 01:15:46

Resolution: fixed
