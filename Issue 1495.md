# Issue 1495: ATLAS fails to compile on FC7 32 bit with multiple cores

Issue created by migration from https://trac.sagemath.org/ticket/1495

Original creator: jsp

Original creation time: 2007-12-13 23:16:08

Assignee: mabshoff

According to INSTALL.txt: CPU-Throttling, you have to do

```
/usr/bin/cpufreq-selector -g performance
```

But with two cores you have to force the cpu1 to run at its peak frequency:


```
As root:
cp /sys/devices/system/cpu/cp0/cpufreq/scaling_governor \
    /sys/devices/system/cpu/cp1/cpufreq/scaling_governor
```




---

Comment by mabshoff created at 2007-12-18 23:04:56

We need to detect if power management is enabled and set some non-performance mode. Otherwise print a warning and ask for confirmation to continue.

Cheers,

Michael


---

Comment by was created at 2008-01-19 20:34:02


```
jkantor: 1495 we can't fix and 1547  I don't know how to do
[12:31pm] william_stein: #1495 -- should go in the docs somewhere
[12:31pm] william_stein: Also, maybe we can check if the cpu throttling is on and immediately terminate the build with a help message.
```



---

Comment by mabshoff created at 2008-04-11 22:38:35

After thinking about this for a long time and some feedback I got from IRC during the ATLAS 3.8.1 upgrade when I did terminate the build I considered that it will cause more trouble than it is worth it. Fixing the power management setting requires root priviledges and since power management is enabled on pretty much any current kernel this would prevent quite a number of users from building Sage. Consequently: won't fix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-11 22:38:35

Resolution: wontfix
