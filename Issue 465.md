# Issue 465: LinBox: reenable Strassen-Winograd optimization test on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/465

Original creator: mabshoff

Original creation time: 2007-08-19 22:57:53

Assignee: mabshoff

Hello, 

the lround fix we applied to the LinBox spkg also fixes the Strassen-Winograd optimization test:

checking best threshold for Strassen-Winograd matrix multiplication...
fgemm 300x300: 0.45 s, 120 Mffops
1Wino 300x300: 0.31 s, 174.194 Mffops

fgemm 300x300: 0.45 s, 120 Mffops
1Wino 300x300: 0.31 s, 174.194 Mffops

fgemm 44x44: 0 s, Inf Mffops
1Wino 44x44: 0 s, Inf Mffops

fgemm 172x172: 0.09 s, 113.077 Mffops
1Wino 172x172: 0.05 s, 203.538 Mffops

fgemm 172x172: 0.09 s, 113.077 Mffops
1Wino 172x172: 0.06 s, 169.615 Mffops
done

This was from the compile test I ran on Neron.

For the updated spkg have a look at 

http://sage.math.washington.edu/home/mabshoff/spkg-install-LinBox-enable-SWO

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-21 16:10:07

At http://sage.math.washington.edu/home/mabshoff/linbox-20070814.p1.spkg is an updated LinBox spkg. Changes:

```
mabshoff@neron standard$ less linbox-20070814.p1/SPKG.txt
*20070821:

- reenable tuning test
- added spkg-check
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-08-22 19:39:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-25 01:20:50

Resolution: fixed


---

Comment by mabshoff created at 2008-08-25 01:20:50

This was fixed a while ago. On

```
-bash-3.00$ uname -a
SunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc
```

we now have:

```
checking best threshold for Strassen-Winograd matrix multiplication... 
fgemm 300x300: 0.01129 s, 4782.99 Mffops
1Wino 300x300: 0.012612 s, 4281.64 Mffops

fgemm 812x812: 0.175283 s, 6108.83 Mffops
1Wino 812x812: 0.180449 s, 5933.95 Mffops

fgemm 1324x1324: 0.707952 s, 6556.77 Mffops
1Wino 1324x1324: 0.700415 s, 6627.33 Mffops

fgemm 1324x1324: 0.703776 s, 6595.68 Mffops
1Wino 1324x1324: 0.700589 s, 6625.68 Mffops

fgemm 1068x1068: 0.37835 s, 6439.47 Mffops
1Wino 1068x1068: 0.381192 s, 6391.46 Mffops

fgemm 1196x1196: 0.525748 s, 6507.98 Mffops
1Wino 1196x1196: 0.52432 s, 6525.7 Mffops

fgemm 1196x1196: 0.525852 s, 6506.69 Mffops
1Wino 1196x1196: 0.524372 s, 6525.05 Mffops
done
checking whether to build documentation... no
```


Cheers,

Michael
