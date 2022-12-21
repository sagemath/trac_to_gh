# Issue 9982: boehm_gc fails to build properly on AIX 5.3

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-23 20:26:50

Assignee: drkirkby

CC:  chapoton

Using the following system: 

 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * DDS-4 tape drive 

boehm_gc-7.1.p6 fails to build properly on AIX. See attached log of the build. I'm not sure yet if this is an upstream problem on a Sage problem. 


---

Comment by drkirkby created at 2010-09-23 20:27:51

Log of a failed build on an RS/6000 running AIX 5.3


---

Attachment

EOL for AIX 5.3 was four years ago, and nobody seems to care about this ticket. So I suggest we close this as wontfix.


---

Comment by jmantysalo created at 2016-08-30 04:43:09

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-08-30 07:14:59

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2016-08-30 09:58:42

Should we mass-close all tickets about AIX?


---

Comment by jmantysalo created at 2016-08-30 10:06:31

Replying to [comment:3 jdemeyer]:
> Should we mass-close all tickets about AIX?

Is anyone using [SageMath](SageMath) on AIX?

At least #9993 ("Singular fails to build on AIX 5.3") has no value, as it just tells an error. But  #9990 ("Pari fails to build on AIX") contains some discussion. But OTOH also closed tickets can be searched.


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix
