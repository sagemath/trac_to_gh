# Issue 1264: upgrade to newest version of ipython

Issue created by migration from https://trac.sagemath.org/ticket/1264

Original creator: was

Original creation time: 2007-11-25 07:26:28

Assignee: was

I made a new ipython spkg, which is here:

http://sage.math.washington.edu/home/was/tmp/ipython-0.8.1.r2871.spkg

However, it DOES NOT WORK.


```
I tried updating Sage to this version of Ipython, and
when I start sage it just immediately exits:

rank4:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
rank4:~ was$
| SAGE Version 2.8.13, Release Date: 2007-11-21                      |
| Type notebook() for the GUI, and license() for information.        |

I.e., I get immediately dumped to the prompt.   Do you
have any idea why?  (I haven't tried at all to figure out why.)

If anybody wants to try this, just do

   wget http://sage.math.washington.edu/home/was/tmp/ipython-0.8.1.r2871.spkg
   sage -f ipython-0.8.1.r2871.spkg

then run sage.

To restore the previous version of Ipython, just do

   sage -f ipython-0.8.1.p1.spkg
----


[sage-support] install problem with pickleshare
Reply to all
Forward
Reply by chat
Filter messages like this
Print
Add to Contacts list
Delete this message
Report phishing
Report not phishing
Show original
Message text garbled?
Why is this spam/nonspam?
maxj	
I am attempting the default installation of sage-2.8.6-PowerMacintosh- Darwin...
	
Oct 15
William Stein to sage-support
	
show details Oct 15
	
	
	
Reply
	
	
On 10/15/07, maxj <max_corvallis@yahoo.com> wrote:
>
> I am attempting the default installation of sage-2.8.6-PowerMacintosh-
> Darwin, but Sage exits immediately with error:
>
> ImportError: No module named pickleshare
>
> I tried an earlier version of Sage with similar results, although I
> don't think the missing python module was named pickleshare -- I think
> I'd remember the name!
>
> Any suggestions?

Please post very precise details about your computer, version of OS X,
output of "gcc -v" (from the command line), and the exact error message
when you start Sage.  Also, do you have fink installed?

William
- Show quoted text -

>
>
> --~--~---------~--~----~------------~-------~--~----~
> To post to this group, send email to sage-support@googlegroups.com
> To unsubscribe from this group, send email to sage-support-unsubscribe@googlegroups.com
> For more options, visit this group at http://groups.google.com/group/sage-support
> URLs: http://sage.math.washington.edu/sage/ and http://sage.scipy.org/sage/
> -~----------~----~----~----~------~----~------~--~---
>
>


--
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org
Reply
		
Forward
		
	
maxj	
______________________________________ Machine Name: Mac mini Machine Model: ...
	
Oct 16
William Stein to Fernando
	
show details Oct 16
	
	
	
Reply
	
	
Does this ring any bells to you?
- Show quoted text -

---------- Forwarded message ----------
From: maxj <max_corvallis@yahoo.com>
Date: Oct 16, 2007 8:32 AM
Subject: [sage-support] Re: install problem with pickleshare
To: sage-support <sage-support@googlegroups.com>



On Oct 16, 12:06 am, "William Stein" <wst...@gmail.com> wrote:

> Please post very precise details about your computer, version of OS X,
> output of "gcc -v" (from the command line), and the exact error message
> when you start Sage.  Also, do you have fink installed?
______________________________________

 Machine Name: Mac mini
 Machine Model:        PowerMac10,1
 CPU Type:     PowerPC G4  (1.2)
 Number Of CPUs:       1
 CPU Speed:    1.25 GHz
 L2 Cache (per CPU):   512 KB
 Memory:       512 MB
 System Version:       Mac OS X 10.4.10 (8R218)
 Kernel Version:       Darwin 8.10.0
________________________________

max$ gcc -v
Using built-in specs.
Target: powerpc-apple-darwin8
Configured with: /private/var/tmp/gcc/gcc-5250.obj~12/src/configure --
disable-checking -enable-werror --prefix=/usr --mandir=/share/man --
enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg]
[^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --
build=powerpc-apple-darwin8 --host=powerpc-apple-darwin8 --
target=powerpc-apple-darwin8
Thread model: posix
gcc version 4.0.1 (Apple Computer, Inc. build 5250)
________________________________

----------------------------------------------------------------------
----------------------------------------------------------------------
Traceback (most recent call last):
 File "/Users/max/Desktop/sage-2.8.6-PowerMacintosh-Darwin/local/bin/
sage-ipython", line 10, in <module>
   import IPython
 File "/Users/max/Desktop/sage-2.8.6-PowerMacintosh-Darwin/local/lib/
python2.5/site-packages/IPython/__init__.py", line 60, in <module>
   __import__(name,glob,loc,[])
 File "/Users/max/Desktop/sage-2.8.6-PowerMacintosh-Darwin/local/lib/
python2.5/site-packages/IPython/Shell.py", line 44, in <module>
   from IPython.iplib import InteractiveShell
 File "/Users/max/Desktop/sage-2.8.6-PowerMacintosh-Darwin/local/lib/
python2.5/site-packages/IPython/iplib.py", line 58, in <module>
   import pickleshare
ImportError: No module named pickleshare
______________________________
| SAGE Version 2.8.6, Release Date: 2007-10-06                       |
| Type notebook() for the GUI, and license() for information.        |
Yes, I have Fink 0.24.14 installed.

Thanks, Max



--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-support@googlegroups.com
To unsubscribe from this group, send email to
sage-support-unsubscribe@googlegroups.com
For more options, visit this group at
http://groups.google.com/group/sage-support
URLs: http://sage.math.washington.edu/sage/ and http://sage.scipy.org/sage/
-~----------~----~----~----~------~----~------~--~---



- Show quoted text -
--
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org
Reply
		
Forward
		
	
Fernando Perez	
Hey folks, if anyone can help William with this, I'd be very grateful. This d...
	
Oct 17
Brian Granger	
This is really odd. pickleshare.py is in the Extensions subfolder of IPython,...
	
Oct 17
William Stein to max_corvallis
	
show details Oct 17
	
	
	
Reply
	
	
---------- Forwarded message ----------
From: Brian Granger <ellisonbg.net@gmail.com>
Date: Oct 17, 2007 8:18 PM
Subject: Re: [IPython-dev] Fwd: [sage-support] Re: install problem
with pickleshare
To: Fernando Perez <Fernando.Perez@colorado.edu>
- Show quoted text -
Cc: William Stein <wstein@gmail.com>, ipython-dev@scipy.org


This is really odd.  pickleshare.py is in the Extensions subfolder of
IPython, and thus iplib.py shouldn't be able to import it.  This is
exactly what William is seeing.....but, this code has been in ipython
for a while (my own running version has it), but it is not causing a
problem.  Ville knows most about this module, any thoughts?

Brian

On 10/17/07, Fernando Perez <Fernando.Perez@colorado.edu> wrote:
> Hey folks,
>
> if anyone can help William with this, I'd be very grateful.  This
> doesn't ring any bells in my jet lagged brain and need to run out in a
> second, so I won't be able to deal with this, likely for a few days.
>
> Cheers,
>
> f
>
> ---------- Forwarded message ----------
> From: William Stein <wstein@gmail.com>
> Date: Oct 16, 2007 5:12 PM
> Subject: Fwd: [sage-support] Re: install problem with pickleshare
> To: Fernando Perez <Fernando.Perez@colorado.edu>
>
>
> Does this ring any bells to you?
>
> ---------- Forwarded message ----------
> From: maxj <max_corvallis@yahoo.com>
> Date: Oct 16, 2007 8:32 AM
> Subject: [sage-support] Re: install problem with pickleshare
> To: sage-support <sage-support@googlegroups.com>
>
>
>
> On Oct 16, 12:06 am, "William Stein" <wst...@gmail.com> wrote:
>
> > Please post very precise details about your computer, version of OS X,
> > output of "gcc -v" (from the command line), and the exact error message
> > when you start Sage.  Also, do you have fink installed?
> ______________________________________
>
>   Machine Name: Mac mini
>   Machine Model:        PowerMac10,1
>   CPU Type:     PowerPC G4  (1.2)
>   Number Of CPUs:       1
>   CPU Speed:    1.25 GHz
>   L2 Cache (per CPU):   512 KB
>   Memory:       512 MB
>   System Version:       Mac OS X 10.4.10 (8R218)
>   Kernel Version:       Darwin 8.10.0
> ________________________________
>
> max$ gcc -v
> Using built-in specs.
> Target: powerpc-apple-darwin8
> Configured with: /private/var/tmp/gcc/gcc-5250.obj~12/src/configure --
> disable-checking -enable-werror --prefix=/usr --mandir=/share/man --
> enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg]
> [^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --
> build=powerpc-apple-darwin8 --host=powerpc-apple-darwin8 --
> target=powerpc-apple-darwin8
> Thread model: posix
> gcc version 4.0.1 (Apple Computer, Inc. build 5250)
> ________________________________
>
> ----------------------------------------------------------------------
> | SAGE Version 2.8.6, Release Date: 2007-10-06                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> Traceback (most recent call last):
>   File "/Users/max/Desktop/sage-2.8.6-PowerMacintosh-Darwin/local/bin/
> sage-ipython", line 10, in <module>
>     import IPython
>   File "/Users/max/Desktop/sage-2.8.6-PowerMacintosh-Darwin/local/lib/
> python2.5/site-packages/IPython/__init__.py", line 60, in <module>
>     __import__(name,glob,loc,[])
>   File "/Users/max/Desktop/sage-2.8.6-PowerMacintosh-Darwin/local/lib/
> python2.5/site-packages/IPython/Shell.py", line 44, in <module>
>     from IPython.iplib import InteractiveShell
>   File "/Users/max/Desktop/sage-2.8.6-PowerMacintosh-Darwin/local/lib/
> python2.5/site-packages/IPython/iplib.py", line 58, in <module>
>     import pickleshare
> ImportError: No module named pickleshare
> ______________________________
>
> Yes, I have Fink 0.24.14 installed.
>
> Thanks, Max
>
>
>
> --~--~---------~--~----~------------~-------~--~----~
> To post to this group, send email to sage-support@googlegroups.com
> To unsubscribe from this group, send email to
> sage-support-unsubscribe@googlegroups.com
> For more options, visit this group at
> http://groups.google.com/group/sage-support
> URLs: http://sage.math.washington.edu/sage/ and http://sage.scipy.org/sage/
> -~----------~----~----~----~------~----~------~--~---
>
>
>
> --
> William Stein
> Associate Professor of Mathematics
> University of Washington
> http://wstein.org
> _______________________________________________
> IPython-dev mailing list
> IPython-dev@scipy.org
> http://lists.ipython.scipy.org/mailman/listinfo/ipython-dev
>


--
- Show quoted text -
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org
Reply
		
Forward
		
	
Ville M. Vainio	
Perhaps this is due to sys.path not containing Extensions yet for some reason...
	
Oct 17
Fernando Perez	
Mmh, I hadn't realized this bug hadn't been fixed in trunk. I've just committ...
	
8:29 PM (2 hours ago)
William Stein to sage-devel, Fernando, Ville, Fernando, ipython-dev
	
show details 11:22 PM (2 minutes ago)
	
	
	
Reply
	
	
- Show quoted text -
On Nov 24, 2007 8:29 PM, Fernando Perez <fperez.net@gmail.com> wrote:
> On Oct 17, 2007 11:47 PM, Ville M. Vainio <vivainio@gmail.com> wrote:
> > Perhaps this is due to sys.path not containing Extensions yet for some
> > reason (I'm not aware why this is not a problem on my box).
> >
> > To get over it quickly, change line:
> >
> > > python2.5/site-packages/IPython/iplib.py", line 58, in <module>
> > >     import pickleshare
> >
> >
> > to:
> >
> > from IPython.Extensions import pickleshare.
>
> Mmh, I hadn't realized this bug hadn't been fixed in trunk.  I've just
> committed the fix as r2871.

I tried updating Sage to this version of Ipython, and
when I start sage it just immediately exits:

rank4:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
rank4:~ was$
| SAGE Version 2.8.13, Release Date: 2007-11-21                      |
| Type notebook() for the GUI, and license() for information.        |

I.e., I get immediately dumped to the prompt.   Do you
have any idea why?  (I haven't tried at all to figure out why.)

If anybody wants to try this, just do

   wget http://sage.math.washington.edu/home/was/tmp/ipython-0.8.1.r2871.spkg
   sage -f ipython-0.8.1.r2871.spkg

then run sage.

To restore the previous version of Ipython, just do

   sage -f ipython-0.8.1.p1.spkg

 -- William
Reply
	
Reply to all
	
Forward
		
	
William Stein to Fernando, sage-devel, Ville, Fernando, ipython-dev
	
show details 11:24 PM (0 minutes ago)
	
	
	
Reply
	
	
On Nov 24, 2007 11:22 PM, William Stein <wstein@gmail.com> wrote:
>
> On Nov 24, 2007 8:29 PM, Fernando Perez <fperez.net@gmail.com> wrote:
> > On Oct 17, 2007 11:47 PM, Ville M. Vainio <vivainio@gmail.com> wrote:
> > > Perhaps this is due to sys.path not containing Extensions yet for some
> > > reason (I'm not aware why this is not a problem on my box).
> > >
> > > To get over it quickly, change line:
> > >
> > > > python2.5/site-packages/IPython/iplib.py", line 58, in <module>
> > > >     import pickleshare
> > >
> > >
> > > to:
> > >
> > > from IPython.Extensions import pickleshare.
> >
> > Mmh, I hadn't realized this bug hadn't been fixed in trunk.  I've just
> > committed the fix as r2871.
>
> I tried updating Sage to this version of Ipython, and
> when I start sage it just immediately exits:

I should add that

 sage -ipython

which runs Ipython directly (without sage preparsing, etc.),
works fine, as does import sage.all:

rank4:standard was$ sage -ipython
Python 2.5.1 (r251:54863, Nov  2 2007, 12:50:27)
Type "copyright", "credits" or "license" for more information.

IPython 0.8.2.svn.r2848 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object'. ?object also works, ?? prints more.

In [1]: from sage.all import *

In [2]: 2/3
Out[2]: 0

In [3]: ZZ(2) / ZZ(3)
Out[3]: 2/3


>
> rank4:~ was$ sage
> ----------------------------------------------------------------------
> | SAGE Version 2.8.13, Release Date: 2007-11-21                      |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> rank4:~ was$
>
>
> I.e., I get immediately dumped to the prompt.   Do you
> have any idea why?  (I haven't tried at all to figure out why.)
>
> If anybody wants to try this, just do
>
>     wget http://sage.math.washington.edu/home/was/tmp/ipython-0.8.1.r2871.spkg
>     sage -f ipython-0.8.1.r2871.spkg
>
> then run sage.
>
> To restore the previous version of Ipython, just do
>
>     sage -f ipython-0.8.1.p1.spkg
>
>  -- William
>

	
	
```



---

Comment by mabshoff created at 2007-11-25 18:09:12

Fernando says:

```
Sorry about that!  Could you redo the process with the current SVN
(r2873, if it matters)?  Because of how Sage starts ipython, it was
getting confused and going into 'batch mode' right away, thus never
entering the interactive loop.  Fixed now.

Cheers,

f
```


Cheers,

Michael


---

Comment by burcin created at 2008-05-11 16:30:13

There is a package for version 0.8.2 available at #905. The problem described here doesn't appear with that version, maybe we should close this bug.


---

Comment by mabshoff created at 2008-05-11 19:41:57

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 19:41:57

Yep. Fixed by merging the spkg from #905 in Sage 3.0.2.alpha0
