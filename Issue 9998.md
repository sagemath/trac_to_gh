# Issue 9998: Status of AIX port of Sage.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-24 02:40:34

Assignee: drkirkby

CC:  chapoton

This ticket lists those parts of Sage that have built in Sage, along with whether they have passed the tests. Unless otherwise stated, they results are from the following hardware. 

 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)



---

Comment by robertwb created at 2010-09-26 04:39:54

Changing type from defect to enhancement.


---

Comment by fbissey created at 2011-03-17 01:33:14

Since I have the hardware and the software, I'll add myself here.

I should have a aix-7.1 test box soon and some power 7 box on which we may install anything from aix-5.3 to 7.1 by July/August.


---

Comment by drkirkby created at 2011-03-17 02:21:53

Replying to [comment:4 fbissey]:
> Since I have the hardware and the software, I'll add myself here.
> 
> I should have a aix-7.1 test box soon and some power 7 box on which we may install anything from aix-5.3 to 7.1 by July/August.

I'm limited to AIX 5.3 due to the rather old hardware - you can see what I have listed above. 

There was some interest from IBM to semi-fund an AIX port of Sage. They contacted William and were considering giving one or two people access to a quick machine. But due to security issues about where the machine was hosted, it could only be one or two developers and from a couple of IP addresses. As such, both William and I said it was not worth bothering with. 

Then it became apparent IBM wanted us to concentrate on one specific package - it seemed to me IBM were hoping to get a specific tool working on AIX for zero cost to them. I said I'd do that bit if they paid me, but nothing came of that. 

Dave


---

Comment by fbissey created at 2011-03-17 02:30:07

Given the kind of relationship we have with IBM here I should make some enquiries. Can you name the tool in question?


---

Comment by drkirkby created at 2011-03-17 04:01:39

Replying to [comment:6 fbissey]:
> Given the kind of relationship we have with IBM here I should make some enquiries. Can you name the tool in question?

Yes, I just checked my emails. It was Numpy and Scipy that someone at IBM wanted on AIX - I assume for his personal work. I've no idea of the work in doing this, but I'd be willing to at least consider it on a contract basis. 

I don't think there would be much appetite for an AIX port of Sage by sage-developers. In any case, for a port to take place, some decent hardware would be needed. My machine is too old, so even permitting others to use it (and I've done that several times), it would not be suitable for Sage development. Neither is a machine which has access restricted to a couple of people. 

The offers made by IBM before, while I'm sure were made with good intentions, were not acceptable to either William or I. 

Another issue, is that even if IBM gave William a server, he has no AIX administrator. I don't know AIX that well - though perhaps just about to set up a server. I've set my own up OK. 

IBM were supposed to be giving me an account on this 4 GHz AIX box, but I never got it, so I'm stuck using my own RS/6000, which is too old. 

Dave


---

Comment by mkoeppe created at 2020-04-01 14:08:08

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-04-01 14:08:08

should be closed as outdated


---

Comment by chapoton created at 2020-04-01 14:09:16

Resolution: invalid


---

Comment by chapoton created at 2020-04-01 14:09:16

agreed
