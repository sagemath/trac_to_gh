# Issue 1021: real_roots sometimes returns incorrect roots

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-28 17:31:26

Assignee: was

For example:

```
sage: x = polygen(ZZ)
sage: (x^5 * (x^2 - 9999)^2 - 1).real_root_intervals()

[((-120886537286091774329444377/1208925819614629174706176,
   -60443268541873225202027201/604462909807314587353088),
  1),
 ((-29274496381311/9007199254740992, 419601125186091/2251799813685248), 1),
 ((2126658450145849453951061654415153249597/21267647932558653966460912964485513216,
   4253316902721330018853696359533061621799/42535295865117307932921825928971026432),
  1),
 ((1063329226287740282451317352558954186101/10633823966279326983230456482242756608,
   531664614358685696701445201630854654353/5316911983139663491615228241121378304),
  1)]
sage: len((x^5 * (x^2 - 9999)^2 - 1).real_root_intervals())
4
```


This example returns 4 roots, even though the polynomial in question actually has only 3.

This is because the root finder finds a list of intervals known to have either 0 or 1 root, but is not correctly weeding out some of the intervals that are known to have 0 roots.


---

Attachment


---

Comment by cwitty created at 2007-10-28 17:43:59

Resolution: fixed
