# Issue 7170: HP-UX failure of rubiks as no 'install' program.

Issue created by migration from https://trac.sagemath.org/ticket/7170

Original creator: drkirkby

Original creation time: 2009-10-10 07:43:05

Assignee: tbd

CC:  david.kirkby@onetel.ne dimpase

Keywords: HP-UX install

I think we should either 

 * check for the program 'install' in a modifed 'prereq' script
 * Make use of 'cp' installed. 
 * include an 'install'  



```
       gcc -O2 -g twist.c  -o twist
        mkdir -p /home/drkirkby/sage-4.1.2.rc0/local/bin
        no install in /home/drkirkby/sage-4.1.2.rc0 /home/drkirkby/sage-4.1.2.rc0/local/bin /home/drkirkby/sage-4.1.2.rc0 /home/drkirkby/sage-4.1.2.rc0/local/bin /usr/local/bin /usr/bin /opt/ansic/bin /usr/ccs/bin /usr/contrib/bin /opt/mpi/bin /opt/hparray/bin /opt/nettladm/bin /opt/upgrade/bin /opt/fcms/bin /usr/bin/X11 /usr/contrib/bin/X11 /opt/graphics/common/bin /opt/pd/bin /opt/resmon/bin /opt/mozilla /opt/netscape /usr/local/bin /opt/gnome/bin /opt/graphics/phigs/bin /opt/OpenSource/bin /usr/sbin/diag/contrib /opt/wbem/bin /opt/wbem/sbin /opt/hp-gcc/bin /opt/aCC/bin /opt/cadvise/bin /opt/sentinel/bin /opt/langtools/bin . /opt/kirkby/bin reid/optimal /home/drkirkby/sage-4.1.2.rc0/local/bin
Make: Cannot load no.  Stop.
*** Error exit code 1

Stop.

```




---

Comment by drkirkby created at 2009-10-10 07:44:35

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2009-10-10 07:46:13

It should be noted, Solaris comes with no install program either, except one in /usr/sbin, which would not be in a normal users path (only root).


---

Comment by kcrisman created at 2011-02-16 22:33:31

Changing component from porting to AIX or HP-UX ports.


---

Comment by mkoeppe created at 2020-04-25 02:59:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-04-25 02:59:35

outdated, should be closed


---

Comment by dimpase created at 2020-04-25 04:40:44

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-04-26 07:25:34

Resolution: invalid
