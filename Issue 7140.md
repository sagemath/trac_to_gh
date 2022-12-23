# Issue 7140: HP-UX port of Sage - issues arrising from such an attempt.

Issue created by migration from https://trac.sagemath.org/ticket/7140

Original creator: drkirkby

Original creation time: 2009-10-06 13:05:45

Assignee: tbd

CC:  david.kirkby@onetel.net dimpase

I think it would be useful if we could get an HP-UX port of Sage. Mathematica used to support HP-UX until quite recently, but no longer does. However, as of today (6th October 2009) an HP-UX port is clearly of low-priority compared to issues with OS X 10.6, Solaris, Windows and Cygwin. 

Having just done a fresh install of HP-UX on my [HP Visulize C3600](http://h20000.www2.hp.com/bizsupport/TechSupport/Home.jsp?locale=en_US&prodTypeId=12454&prodSeriesId=44449) which is fitted with a pair of 36 GB SCSI disks and 1 GB RAM (soon to be upgraded to 8 GB). 


```
# uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
```


I thought I'd document the issues one would get from a totally fresh install. It should be noted that the C3600 uses the [PA-RISC](http://en.wikipedia.org/wiki/PA-RISC) processor, not the [Intel Itanium](http://www.intel.com/design/itanium/documentation.htm) which has been used on all HP's machines running HP-UX since the end of 2008. 

As and when bugs are found which would prevent Sage building on HP-UX, the trac numbers will be added here. 
 
 * The C compiler supplied with HP-UX is not fully functional, and is only intended to rebuild the kernel. As such, it would be useless for building Sage. Compilers are available from HP, but cost money. 
 * gcc is not supplied, but can be downloaded free from various sites. When I checked, the HP website had the latest gcc (4.4.1), which would imply HP keep an up to date copy of gcc. In order to download gcc from the HP site, you need to join HP's _Developer & Solution Partner Program (DSPP)_, but that is free for individual users at least. 
 * On PA 11.11 systems, the linker patch PHSS_33033 is required to compile C++ programs with gcc. 
 * By default, /home, where user's home directories resides is limited to about 20 MB or so. This needed to be expanded using _/usr/sbin/sam_

Dave


---

Comment by drkirkby created at 2011-02-05 10:40:42

Changing component from porting to AIX or HP-UX ports.


---

Comment by mkoeppe created at 2020-04-25 02:59:17

outdated, should be closed


---

Comment by mkoeppe created at 2020-04-25 02:59:17

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-04-26 08:31:02

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-04-27 09:07:40

Resolution: invalid
