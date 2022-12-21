# Issue 2287: error installing rubiks

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-02-24 01:10:30

Assignee: mabshoff

Log:
sizekoc1.c: In function ‘main’:
sizekoc1.c:134: warning: incompatible implicit declaration of built-in function ‘exit’
sizekoc1.c:153: warning: incompatible implicit declaration of built-in function ‘exit’
sizekoc1.c:230: warning: incompatible implicit declaration of built-in function ‘exit’
gcc -O -DLARGE_MEM -DVERBOSE -o sizekoc1 sizekoc1.o
size sizekoc1
   text    data     bss     dec     hex filename
  14622     296 82244256        82259174        4e72ce6 sizekoc1
gcc -O -DLARGE_MEM -DVERBOSE -DCCPERM -DIPERM -c sizekoc2.c
sizekoc2.c: In function ‘main’:
sizekoc2.c:171: warning: incompatible implicit declaration of built-in function ‘exit’sizekoc2.c:190: warning: incompatible implicit declaration of built-in function ‘exit’sizekoc2.c:267: warning: incompatible implicit declaration of built-in function ‘exit’
gcc -O -DLARGE_MEM -DVERBOSE -o sizekoc2 sizekoc2.o
size sizekoc2
   text    data     bss     dec     hex filename
  15212     296 409577600       409593108       1869e514        sizekoc2
make[3]: Leaving directory `/home/yqiang/Software/sage-2.10.2/spkg/build/rubiks-20070912.p2/src/dik'
make[3]: Entering directory `/home/yqiang/Software/sage-2.10.2/spkg/build/rubiks-20070912.p2/src/reid'
make[3]: Nothing to be done for `all'. 
make[3]: Leaving directory `/home/yqiang/Software/sage-2.10.2/spkg/build/rubiks-20070912.p2/src/reid'
mkdir -p /home/yqiang/Software/sage-2.10.2/local/bin
/usr/bin/install reid/optimal /home/yqiang/Software/sage-2.10.2/local/bin
make[2]: /usr/bin/install: Command not found
make[2]: *** [install] Error 127
make[2]: Leaving directory `/home/yqiang/Software/sage-2.10.2/spkg/build/rubiks-20070912.p2/src'

real    0m29.404s
user    0m28.275s
sys     0m1.107s
sage: An error occurred while installing rubiks-20070912.p2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of


-------------------------

On my distribution 'install' is in /bin/install instead of /usr/bin/install. Maybe the script needs to check where 'install' actually is.


---

Comment by mabshoff created at 2008-02-24 02:52:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-21 13:00:56

An updated spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha1/rubiks-20070912.p3.spkg

Changes:
 * SAGE_LOCAL check (#633)
 * remove binary crap
 * rename cube to dikcube to avoid name clash with polymake (#2595)
 * detect the location of install instead of hardcoding it (#2287)


---

Comment by gfurnish created at 2008-03-21 13:05:22

Looks good to me.


---

Comment by mabshoff created at 2008-03-21 13:17:48

Resolution: fixed


---

Comment by mabshoff created at 2008-03-21 13:17:48

Merged in Sage 2.11.alpha1
