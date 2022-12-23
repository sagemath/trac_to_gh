# Issue 6028: get_memory_usage() sucks performance wise on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/6028

Original creator: mabshoff

Original creation time: 2009-05-12 07:32:08

Assignee: mabshoff

Use /proc/$PID/psinfo instead of top - see

 * http://getthegood.com/TechNotes/Papers/ProcStatistics.html
 * http://manpages.unixforum.co.uk/man-pages/unix/solaris-10-11_06/4/proc-man-page.html

get_memory_usage() costs about *1 second* of CPU time per invocation. This makes sage/rings/tests.py time out since that code calls it a couple thousand times.

Cheers,

Michael


---

Comment by was created at 2009-05-28 06:52:27

This isn't critical for 4.0.


---

Comment by was created at 2009-06-15 23:29:28

If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker. Note that the lisp interface is in fact 100% completely broken right now.


---

Comment by was created at 2009-06-15 23:29:28

Changing priority from blocker to critical.


---

Comment by drkirkby created at 2009-08-24 21:56:56

'top' is not a standard part of Solaris. Sure it can be downloaded, but I can't believe using 'top' is the best way to do things.


---

Comment by drkirkby created at 2010-02-27 19:28:06

Using a system call would be the correct way to do this, but as a temporary fix, replacing 'top' with 'prstat' is sensible. That is not fast, but even on a single-processor 500 MHz machine with a load average of 2, prstat is taking less than 100 ms to execute (see below). 

I've created a ticket #8391 to call 'prstat' instead of 'top', despite the fact either solution is a hack. 


```
drkirkby@kestrel:~$ /usr/sbin/psrinfo -v
Status of virtual processor 0 as of: 02/27/2010 19:22:41
  on-line since 02/27/2010 15:10:42.
  The sparcv9 processor operates at 500 MHz,
	and has a sparcv9 floating point processor.
drkirkby@kestrel:~$ time prstat -n 65000 1 1 > b

real	0m0.085s
user	0m0.027s
sys	0m0.050s
drkirkby@kestrel:~$ cat b
   PID USERNAME  SIZE   RSS STATE  PRI NICE      TIME  CPU PROCESS/NLWP       
  2023 root     4800K 3424K run     20    0   0:18:51  37% qq10/1
  2044 root     6032K 5496K run      0   19   0:13:55  31% pgn-extract/1
  2043 root     1872K 1336K run      0   19   0:12:17  28% pgn-extract/1
  2025 root     2768K 1976K sleep   59    0   0:00:21 0.5% telnet/1
   656 drkirkby 9352K 4128K sleep   59    0   0:00:03 0.2% sshd/1
   666 drkirkby 3456K 2464K sleep   49    0   0:00:01 0.2% bash/1
  2115 drkirkby 4280K 3568K cpu0    49    0   0:00:00 0.2% prstat/1
   255 root     3112K 1592K sleep  100    -   0:00:03 0.0% xntpd/1
   564 root       15M 5016K sleep   59    0   0:00:02 0.0% httpd/1
   642 root     8616K 2328K sleep   59    0   0:00:00 0.0% sendmail/1
  2051 nobody     15M 4568K sleep   59    0   0:00:00 0.0% httpd/1
  2050 nobody     15M 4568K sleep   59    0   0:00:00 0.0% httpd/1
  2052 nobody     15M 4568K sleep   59    0   0:00:00 0.0% httpd/1
  2053 nobody     15M 4568K sleep   59    0   0:00:00 0.0% httpd/1
   493 root       17M   10M sleep   59    0   0:00:00 0.0% Xsun/1
   485 root     1720K 1152K sleep    2   19   0:00:00 0.0% icc-opponents/1
   481 root     1664K 1096K sleep   59    0   0:00:00 0.0% runqq10/1
  2055 nobody     15M 4568K sleep   59    0   0:00:00 0.0% httpd/1
   461 root     6536K 1368K sleep   59    0   0:00:00 0.0% dtlogin/1
   655 root     5552K 2560K sleep   59    0   0:00:00 0.0% sshd/1
   644 smmsp    8616K 1928K sleep   59    0   0:00:00 0.0% sendmail/1
   398 root     4288K 1712K sleep   59    0   0:00:00 0.0% syslogd/13
   387 root     4552K 1440K sleep   59    0   0:00:00 0.0% sshd/1
   394 root       15M 4568K sleep   59    0   0:00:05 0.0% fmd/19
   376 root     3208K 1712K sleep   59    0   0:00:00 0.0% automountd/3
  2054 nobody     15M 4568K sleep   59    0   0:00:00 0.0% httpd/1
   424 root     9768K 2320K sleep   59    0   0:00:00 0.0% snmpd/1
   291 daemon   3160K 1256K sleep   59    0   0:00:00 0.0% rpcbind/1
   155 root     5784K 3472K sleep   59    0   0:00:01 0.0% nscd/30
   302 root     5352K 2184K sleep   59    0   0:00:01 0.0% inetd/4
   306 root     2928K 1424K sleep   59    0   0:00:00 0.0% ttymon/1
   294 daemon   3104K 1544K sleep   59    0   0:00:00 0.0% statd/1
   311 root     2872K 1392K sleep   59    0   0:00:00 0.0% ttymon/1
   119 daemon   4920K 1280K sleep   59    0   0:00:00 0.0% kcfd/3
   141 root     3600K 1872K sleep   59    0   0:00:00 0.0% picld/4
   114 root     6344K 2272K sleep   59    0   0:00:00 0.0% syseventd/15
   305 daemon   2744K 1216K sleep   60  -20   0:00:00 0.0% lockd/2
   239 root     2592K  856K sleep   59    0   0:00:00 0.0% iscsid/2
   375 root     2920K 1080K sleep   59    0   0:00:00 0.0% automountd/2
   277 root     3272K 1248K sleep   59    0   0:00:00 0.0% cron/1
   310 root     1672K 1032K sleep   59    0   0:00:00 0.0% utmpd/1
     9 root       11M 9184K sleep   59    0   0:00:34 0.0% svc.configd/17
     7 root       10M 3720K sleep   59    0   0:00:07 0.0% svc.startd/12
   304 root     2520K 1128K sleep   59    0   0:00:00 0.0% sac/1
     1 root     2928K 1480K sleep   59    0   0:00:00 0.0% init/1
Total: 45 processes, 158 lwps, load averages: 2.32, 2.29, 2.20
```



---

Comment by drkirkby created at 2010-02-28 10:22:19

I do not know what hardware Micheal used when he found the CPU time used was about a second, but on a dual processor 900 MHz Sun Blade 2000, with a load average of 1.0, the times are *much* faster using 'prstat'. This is a slightly modified version of Sage 4.3.3, so it builds on Solaris. Since the load average was 1.0, and its dual processor, I doubt it would be any faster on an idle system.

The CPU time can't be measured (displayed as 0.00 s), but the wall time is 0.08s. 


```
Exiting SAGE (CPU time 0m0.20s, Wall time 5m59.86s).
drkirkby@redstart:~/fresh/sage-4.3.3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: time get_memory_usage()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.08 s
91.0
```

| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
This means using 'prstat' to get the times is *much faster* than using 'top'.


---

Comment by was created at 2012-02-26 17:54:51

This was resolved by drkirkby via #8391.


---

Comment by jdemeyer created at 2013-02-08 14:24:22

Resolution: duplicate
