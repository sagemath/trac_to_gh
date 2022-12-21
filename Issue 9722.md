# Issue 9722: PARI/GP build error on Fedora 13

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-08-11 01:34:21

Assignee: tbd

CC:  ggrafendorfer leif jdemeyer jsp

Reported by Georg Grafendorfer on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/7abfbeedb07abb53/42338e44dc36ae3f#42338e44dc36ae3f):

```
sage does not built on my machine, AMD Phenom(tm) II X4 925, Fedora
13,

here are the relevant lines of the log file:

Shall we try to build pari 2.3.5 (released) now (y/n)? [n]
Ok. Type "make install" when you are ready
Bye !
Building and install PARI
make[2]: Entering directory `/scratch/sage-4.5.3.alpha0/spkg/build/
pari-2.3.5.p2/src'
Making gp in Olinux-x86_64
make[3]: Entering directory `/scratch/sage-4.5.3.alpha0/spkg/build/
pari-2.3.5.p2/src/Olinux-x86_64'
File ../src/funclist not changed.
../config/genkernel ../src/kernel/x86_64/asm0.h > parilvl0.h
cat ../src/kernel/gmp/tune.h ../src/kernel/gmp/int.h ../src/kernel/
none/level1.h > parilvl1.h
cat parilvl0.h parilvl1.h > pariinl.h
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -
I../src/headers -I../src/language -I/scratch/sage-4.5.3.alpha0/local/
include -o gp.o ../src/gp/gp.c
cd ../src/desc && /usr/bin/perl merge_822 ../functions/*/* > def-linux-
x86_64-6659.tmp
mv ../src/desc/def-linux-x86_64-6659.tmp ../src/desc/pari.desc
cd ../src/desc && /usr/bin/perl gen_proto gp pari.desc > gp_init-linux-
x86_64-6659.tmp
mv ../src/desc/gp_init-linux-x86_64-6659.tmp ../src/gp/gp_init.h
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -
I../src/headers -I../src/graph -o gp_init.o ../src/gp/gp_init.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -
I../src/headers -I../src/language -I/scratch/sage-4.5.3.alpha0/local/
include -o gp_rl.o ../src/gp/gp_rl.c
cd ../src/desc && /usr/bin/perl gen_proto highlevel pari.desc >
highlvl-linux-x86_64-6659.tmp
mv ../src/desc/highlvl-linux-x86_64-6659.tmp ../src/gp/highlvl.h
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -
I../src/headers -DDL_DFLT_NAME=NULL -o highlvl.o ../src/gp/highlvl.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -
I../src/headers -o whatnow.o ../src/gp/whatnow.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -
I../src/headers -I../src/graph -o plotport.o ../src/graph/plotport.c
g++ -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../
src/headers -I"/usr/local"/include  -o plotfltk.o ../src/graph/
plotfltk.c
../src/graph/plotfltk.c:27:19: error: FL/Fl.H: No such file or
directory
../src/graph/plotfltk.c:28:26: error: FL/Fl_Window.H: No such file or
directory
../src/graph/plotfltk.c:29:24: error: FL/fl_draw.H: No such file or
directory
../src/graph/plotfltk.c:31: error: expected class-name before '{'
token
../src/graph/plotfltk.c:45: error: 'Fl_Color' does not name a type
../src/graph/plotfltk.c:48: error: 'Fl_Color' does not name a type
../src/graph/plotfltk.c: In constructor 'Plotter::Plotter(long int*,
long int*, long int*, long int, const char*)':
../src/graph/plotfltk.c:56: error: class 'Plotter' does not have any
field named 'Fl_Window'
../src/graph/plotfltk.c:60: error: 'color' was not declared in this
scope
../src/graph/plotfltk.c:60: error: 'FL_WHITE' was not declared in this
scope
../src/graph/plotfltk.c:61: error: 'FL_BLACK' was not declared in this
scope
../src/graph/plotfltk.c:62: error: 'FL_BLUE' was not declared in this
scope
../src/graph/plotfltk.c:63: error: 'rgb_color' was not declared in
this scope
../src/graph/plotfltk.c:64: error: 'FL_RED' was not declared in this
scope
../src/graph/plotfltk.c:65: error: 'FL_GREEN' was not declared in this
scope
../src/graph/plotfltk.c: In function 'void DrawPoint(void*, long int,
long int)':
../src/graph/plotfltk.c:73: error: 'fl_point' was not declared in this
scope
../src/graph/plotfltk.c: In function 'void DrawLine(void*, long int,
long int, long int, long int)':
../src/graph/plotfltk.c:79: error: 'fl_line' was not declared in this
scope
../src/graph/plotfltk.c: In function 'void DrawRectangle(void*, long
int, long int, long int, long int)':
../src/graph/plotfltk.c:85: error: 'fl_rect' was not declared in this
scope
../src/graph/plotfltk.c: In function 'void DrawPoints(void*, long int,
plot_points*)':
../src/graph/plotfltk.c:92: error: 'fl_point' was not declared in this
scope
../src/graph/plotfltk.c: In function 'void SetForeground(void*, long
int)':
../src/graph/plotfltk.c:97: error: 'Fl_Color' was not declared in this
scope
../src/graph/plotfltk.c:97: error: 'color' was not declared in this
scope
../src/graph/plotfltk.c:97: error: expected primary-expression before
')' token
../src/graph/plotfltk.c:97: error: expected ';' before 'data'
../src/graph/plotfltk.c:98: error: 'fl_color' was not declared in this
scope
../src/graph/plotfltk.c: In function 'void DrawLines(void*, long int,
plot_points*)':
../src/graph/plotfltk.c:105: error: 'fl_line' was not declared in this
scope
../src/graph/plotfltk.c: In function 'void DrawString(void*, long int,
long int, char*, long int)':
../src/graph/plotfltk.c:111: error: 'fl_draw' was not declared in this
scope
../src/graph/plotfltk.c: In member function 'void Plotter::draw()':
../src/graph/plotfltk.c:118: error: 'class Plotter' has no member
named 'w'
../src/graph/plotfltk.c:119: error: 'class Plotter' has no member
named 'h'
../src/graph/plotfltk.c:121: error: 'FL_COURIER' was not declared in
this scope
../src/graph/plotfltk.c:121: error: 'fl_font' was not declared in this
scope
../src/graph/plotfltk.c:122: error: 'FL_WHITE' was not declared in
this scope
../src/graph/plotfltk.c:122: error: 'fl_color' was not declared in
this scope
../src/graph/plotfltk.c:123: error: 'class Plotter' has no member
named 'w'
../src/graph/plotfltk.c:123: error: 'class Plotter' has no member
named 'h'
../src/graph/plotfltk.c:123: error: 'fl_rectf' was not declared in
this scope
../src/graph/plotfltk.c:133: error: 'color' was not declared in this
scope
../src/graph/plotfltk.c: In member function 'int
Plotter::handle(int)':
../src/graph/plotfltk.c:140: error: 'FL_PUSH' was not declared in this
scope
../src/graph/plotfltk.c:141: error: 'Fl' has not been declared
../src/graph/plotfltk.c:155: error: 'class Plotter' has no member
named 'x'
../src/graph/plotfltk.c:156: error: 'class Plotter' has no member
named 'y'
../src/graph/plotfltk.c:157: error: 'class Plotter' has no member
named 'w'
../src/graph/plotfltk.c:158: error: 'class Plotter' has no member
named 'h'
../src/graph/plotfltk.c:159: error: 'class Plotter' has no member
named 'fullscreen'
../src/graph/plotfltk.c:163: error: 'class Plotter' has no member
named 'fullscreen_off'
../src/graph/plotfltk.c:164: error: 'class Plotter' has no member
named 'size_range'
../src/graph/plotfltk.c: In function 'void rectdraw0(long int*, long
int*, long int*, long int)':
../src/graph/plotfltk.c:188: error: 'Fl' has not been declared
../src/graph/plotfltk.c:188: error: 'FL_DOUBLE' was not declared in
this scope
../src/graph/plotfltk.c:188: error: 'FL_INDEX' was not declared in
this scope
../src/graph/plotfltk.c:190: error: 'class Plotter' has no member
named 'size_range'
../src/graph/plotfltk.c:191: error: 'class Plotter' has no member
named 'box'
../src/graph/plotfltk.c:191: error: 'FL_FLAT_BOX' was not declared in
this scope
../src/graph/plotfltk.c:192: error: 'class Plotter' has no member
named 'end'
../src/graph/plotfltk.c:193: error: 'class Plotter' has no member
named 'show'
../src/graph/plotfltk.c:194: error: 'Fl' has not been declared
make[3]: *** [plotfltk.o] Error 1
make[3]: Leaving directory `/scratch/sage-4.5.3.alpha0/spkg/build/
pari-2.3.5.p2/src/Olinux-x86_64'
make[2]: *** [gp] Error 2
make[2]: Leaving directory `/scratch/sage-4.5.3.alpha0/spkg/build/
pari-2.3.5.p2/src'
Error building GP 
```

There's now a [dedicated thread](http://groups.google.com/group/sage-release/browse_thread/thread/e1fe601e7e184479/e9a241101d3fb776#e9a241101d3fb776).


---

Comment by mpatel created at 2010-08-11 01:36:04

Georg, if I've correctly guessed your trac name, could you please update the [Sage trac account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?


---

Comment by ggrafendorfer created at 2010-08-11 11:33:47

Replying to [comment:1 mpatel]:
> Georg, if I've correctly guessed your trac name, could you please update the [Sage trac account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?

done, Georg


---

Comment by ggrafendorfer created at 2010-08-11 13:02:59

As suggested by leif i have made the admins here (eth zürich) install fltk-devel (fltk is installed anyway),
still does not work, the log message looks different now:

Shall we try to build pari 2.3.5 (released) now (y/n)? [n]
Ok. Type "make install" when you are ready
Bye !
Building and install PARI
make[2]: Entering directory `/scratch/sage-4.5.3.alpha0/spkg/build/pari-2.3.5.p2/src'
Making gp in Olinux-x86_64
make[3]: Entering directory `/scratch/sage-4.5.3.alpha0/spkg/build/pari-2.3.5.p2/src/Olinux-x86_64'
File ../src/funclist not changed.
../config/genkernel ../src/kernel/x86_64/asm0.h > parilvl0.h
cat ../src/kernel/gmp/tune.h ../src/kernel/gmp/int.h ../src/kernel/none/level1.h > parilvl1.h
cat parilvl0.h parilvl1.h > pariinl.h
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I../src/language -I/scratch/sage-4.5.3.alpha0/local/include -o gp.o ../src/gp/gp.c
cd ../src/desc && /usr/bin/perl merge_822 ../functions/*/* > def-linux-x86_64-379.tmp
mv ../src/desc/def-linux-x86_64-379.tmp ../src/desc/pari.desc
cd ../src/desc && /usr/bin/perl gen_proto gp pari.desc > gp_init-linux-x86_64-379.tmp
mv ../src/desc/gp_init-linux-x86_64-379.tmp ../src/gp/gp_init.h
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I../src/graph -o gp_init.o ../src/gp/gp_init.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I../src/language -I/scratch/sage-4.5.3.alpha0/local/include -o gp_rl.o ../src/gp/gp_rl.c
cd ../src/desc && /usr/bin/perl gen_proto highlevel pari.desc > highlvl-linux-x86_64-379.tmp
mv ../src/desc/highlvl-linux-x86_64-379.tmp ../src/gp/highlvl.h
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -DDL_DFLT_NAME=NULL -o highlvl.o ../src/gp/highlvl.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -o whatnow.o ../src/gp/whatnow.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I../src/graph -o plotport.o ../src/graph/plotport.c
g++ -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I"/usr/local"/include  -o plotfltk.o ../src/graph/plotfltk.c
cat ../src/kernel/gmp/mp.c ../src/kernel/none/cmp.c ../src/kernel/none/gcdll.c ../src/kernel/none/ratlift.c  ../src/kernel/none/invmod.c ../src/kernel/gmp/gcd.c ../src/kernel/none/mp_indep.c ../src/kernel/none/add.c > mp.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -fPIC -I. -I../src/headers -I/scratch/sage-4.5.3.alpha0/local/include -o mp.o mp.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o mpinl.o ../src/kernel/none/mpinl.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o Flx.o ../src/basemath/Flx.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o Qfb.o ../src/basemath/Qfb.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o RgX.o ../src/basemath/RgX.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o alglin1.o ../src/basemath/alglin1.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o alglin2.o ../src/basemath/alglin2.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o arith1.o ../src/basemath/arith1.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o arith2.o ../src/basemath/arith2.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o base1.o ../src/basemath/base1.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o base2.o ../src/basemath/base2.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o base3.o ../src/basemath/base3.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o base4.o ../src/basemath/base4.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o base5.o ../src/basemath/base5.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o bibli1.o ../src/basemath/bibli1.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o bibli2.o ../src/basemath/bibli2.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o buch1.o ../src/basemath/buch1.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o buch2.o ../src/basemath/buch2.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o buch3.o ../src/basemath/buch3.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o buch4.o ../src/basemath/buch4.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o galconj.o ../src/basemath/galconj.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o gen1.o ../src/basemath/gen1.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o gen2.o ../src/basemath/gen2.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o gen3.o ../src/basemath/gen3.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o ifactor1.o ../src/basemath/ifactor1.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o perm.o ../src/basemath/perm.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o polarit1.o ../src/basemath/polarit1.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o polarit2.o ../src/basemath/polarit2.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o polarit3.o ../src/basemath/polarit3.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o rootpol.o ../src/basemath/rootpol.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o subcyclo.o ../src/basemath/subcyclo.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o subgroup.o ../src/basemath/subgroup.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o trans1.o ../src/basemath/trans1.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o trans2.o ../src/basemath/trans2.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o trans3.o ../src/basemath/trans3.c
cd ../src/desc && /usr/bin/perl gen_member pari.desc > members-linux-x86_64-379.tmp
mv ../src/desc/members-linux-x86_64-379.tmp ../src/language/members.h
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o anal.o ../src/language/anal.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o compat.o ../src/language/compat.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o default.o ../src/language/default.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o errmsg.o ../src/language/errmsg.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o es.o ../src/language/es.c
cd ../src/desc && /usr/bin/perl gen_proto basic pari.desc > init-linux-x86_64-379.tmp
mv ../src/desc/init-linux-x86_64-379.tmp ../src/language/init.h
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o init.o ../src/language/init.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o intnum.o ../src/language/intnum.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o members.o ../src/language/members.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o sumiter.o ../src/language/sumiter.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o aprcl.o ../src/modules/aprcl.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o elldata.o ../src/modules/elldata.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o elliptic.o ../src/modules/elliptic.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o galois.o ../src/modules/galois.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o groupid.o ../src/modules/groupid.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o kummer.o ../src/modules/kummer.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o mpqs.o ../src/modules/mpqs.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o nffactor.o ../src/modules/nffactor.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o part.o ../src/modules/part.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o stark.o ../src/modules/stark.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o subfield.o ../src/modules/subfield.c
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -fPIC -o thue.o ../src/modules/thue.c
rm -f libpari-gmp.so.2.3.5
gcc  -o libpari-gmp.so.2.3.5 -shared  -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -fPIC -Wl,-shared,-soname=libpari-gmp.so.2 mp.o mpinl.o Flx.o Qfb.o RgX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bibli1.o bibli2.o buch1.o buch2.o buch3.o buch4.o galconj.o gen1.o gen2.o gen3.o ifactor1.o perm.o polarit1.o polarit2.o polarit3.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o default.o errmsg.o es.o init.o intnum.o members.o sumiter.o aprcl.o elldata.o elliptic.o galois.o groupid.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o -lc -ldl -lm -L/scratch/sage-4.5.3.alpha0/local/lib -lgmp 
if test "libpari-gmp.so.2.3.5" != "libpari.so"; then 	  rm -f libpari.so;	  ln -s libpari-gmp.so.2.3.5 libpari.so; fi
if test "libpari-gmp.so.2.3.5" != "libpari-gmp.so.2"; then 	  rm -f libpari-gmp.so.2;	  ln -s libpari-gmp.so.2.3.5 libpari-gmp.so.2; fi
rm -f gp-dyn
gcc  -o gp-dyn -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -Wl,--export-dynamic  gp.o gp_init.o gp_rl.o highlvl.o whatnow.o plotport.o plotfltk.o  -L"/scratch/sage-4.5.3.alpha0/spkg/build/pari-2.3.5.p2/src/Olinux-x86_64" -L/scratch/sage-4.5.3.alpha0/local/lib -lreadline -L/scratch/sage-4.5.3.alpha0/local/lib/ -ltermcap -L/scratch/sage-4.5.3.alpha0/local/lib -lpari -L"/usr/local"/lib -lfltk  -ldl -lm -L/scratch/sage-4.5.3.alpha0/local/lib -lgmp
/usr/bin/ld: plotfltk.o: undefined reference to symbol '__gxx_personality_v0`@``@`CXXABI_1.3'
/usr/bin/ld: note: '__gxx_personality_v0`@``@`CXXABI_1.3' is defined in DSO /usr/lib64//libstdc++.so.6 so try adding it to the linker command line
/usr/lib64//libstdc++.so.6: could not read symbols: Invalid operation
collect2: ld returned 1 exit status
make[3]: *** [gp-dyn] Error 1
make[3]: Leaving directory `/scratch/sage-4.5.3.alpha0/spkg/build/pari-2.3.5.p2/src/Olinux-x86_64'
make[2]: *** [gp] Error 2
make[2]: Leaving directory `/scratch/sage-4.5.3.alpha0/spkg/build/pari-2.3.5.p2/src'
Error building GP

real	0m45.782s
user	0m41.047s
sys	0m3.976s
sage: An error occurred while installing pari-2.3.5.p2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /scratch/sage-4.5.3.alpha0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/scratch/sage-4.5.3.alpha0/spkg/build/pari-2.3.5.p2 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/scratch/sage-4.5.3.alpha0/spkg/build/pari-2.3.5.p2' && '/scratch/sage-4.5.3.alpha0/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
make[1]: *** [installed/pari-2.3.5.p2] Error 1
make[1]: Leaving directory `/scratch/sage-4.5.3.alpha0/spkg'

real	35m5.899s
user	24m57.842s
sys	8m21.169s
Error building Sage.

Georg


---

Comment by leif created at 2010-08-11 16:15:08

Replying to [comment:3 ggrafendorfer]:
> As suggested by leif i have made the admins here (eth zürich) install fltk-devel (fltk is installed anyway),
> still does not work, the log message looks different now:

```
...
gcc  -o gp-dyn -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -Wl,--export-dynamic  gp.o gp_init.o gp_rl.o highlvl.o whatnow.o plotport.o plotfltk.o  -L"/scratch/sage-4.5.3.alpha0/spkg/build/pari-2.3.5.p2/src/Olinux-x86_64" -L/scratch/sage-4.5.3.alpha0/local/lib -lreadline -L/scratch/sage-4.5.3.alpha0/local/lib/ -ltermcap -L/scratch/sage-4.5.3.alpha0/local/lib -lpari -L"/usr/local"/lib -lfltk  -ldl -lm -L/scratch/sage-4.5.3.alpha0/local/lib -lgmp
/usr/bin/ld: plotfltk.o: undefined reference to symbol '__gxx_personality_v0`@``@`CXXABI_1.3'
/usr/bin/ld: note: '__gxx_personality_v0`@``@`CXXABI_1.3' is defined in DSO /usr/lib64//libstdc++.so.6 so try adding it to the linker command line
/usr/lib64//libstdc++.so.6: could not read symbols: Invalid operation
collect2: ld returned 1 exit status
...
```


That's just the usual [Fedora 13 error](http://fedoraproject.org/wiki/DSOLinkBugs). ;-)

The simplest solution would be to uninstall FLTK completely, but since you seem to not have admin rights, we should perhaps fix this in the PARI package.

There's already a [new PARI Sage package underway](http://trac.sagemath.org/sage_trac/ticket/9343#comment:171), which is afaik intended to get merged into Sage 4.6, but I don't believe you want to wait for that.

So we have to decide if we want to provide a new intermediate PARI 2.3.5.p3 package here, to get merged into Sage 4.5.3. (I think we can solve this by a 9-character patch.)

Mitesh, your opinion?

Jeroen, perhaps you know if this is already fixed upstream/in svn 12577. (There are various ways to fix this.)


---

Comment by ggrafendorfer created at 2010-08-11 17:23:20

> There's already a [new PARI Sage package underway](http://trac.sagemath.org/sage_trac/ticket/9343#comment:171), which is afaik intended to get merged into Sage 4.6, but I don't believe you want to wait for that.

I'm not doing numerical calculations right now, but I'm trying to spread sage here (eth zürich), which is a bit difficult if it does not built ;-), some of us are using it for teaching, the semester starts in middle of September, would be great to fix it until then,

btw, this bug exists since version after 4.3.4, which was the last which built correctly,
I reported it two times before, but was ignored (once a workaround was given)),

Georg


---

Comment by leif created at 2010-08-11 17:39:56

Replying to [comment:5 ggrafendorfer]:
> btw, this bug exists since version after 4.3.4, which was the last which built correctly,

Hmmm, I don't think this error showed up before Fedora 13 was released... ;-)


> I reported it two times before, but was ignored (once a workaround was given)),

Where?

Anyway, I think I have a trivial patch/new spkg ready.

Are you familiar with patching spkgs? (Then you could apply it yourself immediately - or make sure it works on Fedora 13; I've only tested it on Ubuntu, where this is not an issue. It does _not_ fix the first error, i.e. PARI attempting to use FLTK despite no headers being present, since I currently cannot reproduce that. I could perhaps fix that later though.)


---

Comment by ggrafendorfer created at 2010-08-11 18:11:54

Replying to [comment:6 leif]:
> Replying to [comment:5 ggrafendorfer]:
> > btw, this bug exists since version after 4.3.4, which was the last which built correctly,
> 
> Hmmm, I don't think this error showed up before Fedora 13 was released... ;-)

We had Fedora 11 before, where the same error occured, my second report is here:

http://groups.google.com/group/sage-devel/browse_thread/thread/51630a0ef2f8989/c6f07d55a7b091c4?lnk=gst&q=built+error+fedora+11#c6f07d55a7b091c4

> 
> Anyway, I think I have a trivial patch/new spkg ready.
> 
> Are you familiar with patching spkgs?

no, is it difficult, where is the new spkgs?

> It does _not_ fix the first error, i.e. PARI attempting to use FLTK despite no headers being present, since I currently cannot reproduce that. I could perhaps fix that later though.)

Since all the machines are the same, it should also fix the first error, since this is obviously the default state of the machines,

Georg


---

Comment by leif created at 2010-08-11 18:18:27

Changing status from new to needs_review.


---

Comment by leif created at 2010-08-11 18:18:27

I've uploaded a patch to fix the second (i.e. the linker) error. Yet only tested on Ubuntu; _should_ work for Fedora 13...


```
### pari-2.3.5.p3 (Leif Leonhardy, August 11th 2010)
 * #9722: Explicitly link against libstdc++ if FLTK is used, to support
   Fedora 13.
 * TODO/FIXME: On Fedora 13, PARI tries to use FLTK even if just the
   library (as opposed to the required developer) package of FLTK is
   installed.
```



---

Comment by leif created at 2010-08-11 19:10:50

Replying to [comment:7 ggrafendorfer]:
> Replying to [comment:6 leif]:
> > Replying to [comment:5 ggrafendorfer]:
> > > btw, this bug exists since version after 4.3.4, which was the last which built correctly,
> > 
> > Hmmm, I don't think this error showed up before Fedora 13 was released... ;-)

I of course meant the linker error.

> We had Fedora 11 before, where the same error occured, my second report is here:
> 
> http://groups.google.com/group/sage-devel/browse_thread/thread/51630a0ef2f8989/c6f07d55a7b091c4?lnk=gst&q=built+error+fedora+11#c6f07d55a7b091c4

Nice. A trivial work-around, if you simply want to compile Sage/PARI *without* FLTK is:

```
export PARI_EXTRA_OPTS="--with-fltk=no"
```

(This will complain that the directory `.../no` does not exist, but proceed building without FLTK.)

> > Anyway, I think I have a trivial patch/new spkg ready.
> > 
> > Are you familiar with patching spkgs?
> 
> no, is it difficult, where is the new spkgs?

I don't have an account on sage.math, so I could only put it into the volatile ftp directory. (But someone else could move it.)

Applying patches to spkgs is relatively simple. If you have Mercurial (`hg`) installed:

```sh
$ tar xjf /path/to/pari-2.3.5.p2.spkg
$ mv pari-2.3.5.p2 pari-2.3.5.p3
$ cd pari-2.3.5.p3
$ hg import /path/to/spkg-patch.patch # replace with appropriate filename
$ cd ..
$ tar cjf pari-2.3.5.p3.spkg pari-2.3.5.p3
```

Then you can install the new spkg the usual way (`./sage -i ...`, but perhaps first copy it over to `$SAGE_ROOT/spkg/standard` to get around limitations of `sage-spkg`, and then type `./sage -i pari-2.3.5.p3`).
 
> > It does _not_ fix the first error, i.e. PARI attempting to use FLTK despite no headers being present, since I currently cannot reproduce that. I could perhaps fix that later though.)
> Since all the machines are the same, it should also fix the first error, since this is obviously the default state of the machines,

Ok, I've read this too late...

Wouldn't be bad then to install `libfltk-dev` on _all_ machines... (I would assume the machines get configured/installed from a central server anyway.)


---

Comment by jdemeyer created at 2010-08-11 21:23:54

ggrafendorfer: could you please try to see if the problem is there when you compile PARI/GP by itself?  That is, download [http://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.3.5.tar.gz](http://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.3.5.tar.gz), do `./Configure && make` and see what happens.  If you can, please try it both with fltk-devel uninstalled and installed.  If it doesn't compile like that, it should be reported upstream.


---

Comment by mpatel created at 2010-08-11 22:44:31

If it helps, I don't mind merging an intermediate / incremental PARI package in the 4.5.3 series.

Leif, I can make your package available on sage.math.  Since it's ~2 MB, just send it to me by email.

Although I haven't tried it myself, it might be easier to set up and use [spkg-upload](http://code.google.com/p/spkg-upload/).


---

Comment by leif created at 2010-08-11 22:51:57

Replying to [comment:12 mpatel]:
> If it helps, I don't mind merging an intermediate / incremental PARI package in the 4.5.3 series.

Ok.

 
> Leif, I can make your package available on sage.math.  Since it's ~2 MB, just send it to me by email.

I'm going to set up a Fedora box and will try to address the configuration error as well.

> Although I haven't tried it myself, it might be easier to set up and use [spkg-upload](http://code.google.com/p/spkg-upload/).

I'd need credentials from Minh, but the sun is just rising down under... :)


---

Comment by ggrafendorfer created at 2010-08-12 15:36:29

Replying to [comment:11 jdemeyer]:
> ggrafendorfer: could you please try to see if the problem is there when you compile PARI/GP by itself?  That is, download [http://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.3.5.tar.gz](http://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.3.5.tar.gz), do `./Configure && make` and see what happens.  If you can, please try it both with fltk-devel uninstalled and installed.  If it doesn't compile like that, it should be reported upstream.

Done, on two different machines, one with ftlk + fltk-devel, one with fltk but without fltk-devel installed, both on Fedora 13 64bit, both failed after successful configuration, I reported this to the pari project,

Georg


---

Comment by ggrafendorfer created at 2010-08-16 12:08:44

Here is my report to the pari project and the answer:

> Hi,
>
> there are some problems with the pari package when building sage (http://www.sagemath.org) reported here:
>
> http://trac.sagemath.org/sage_trac/ticket/9722
>
>
> I tried to build pari separately (stand alone) but also does not work:
>
> After successful configuration pari does not build in 2 different cases:
>
> AMD Phenom II X4 925, Fedora 13, with fltk and fltk-devel installed: for log-message see file "log_with_fltk-devel" attached
>
> Esprimo 64bit, Fedora 13, with fltk, but not fltk-devel installed: for log-message see file "log_without_fltk-devel" attached

Hello Georg,

On both system, there is libfltk library installed in /usr/local/lib64/, but no
matching header files in /usr/local/include is provided, so compiling fltk does not work.
Configure output a warning:

###
### libX11.so not found. Please install X11 development files.
### They usually come in XFree86-devel (RPM) or xlibs-dev (Debian) packages
###
### X11 not found
###

So either install XFree86-devel (or whathever is the correct name of fedora) or use
--graphic=none to disable graphics.

Installing fltk and fltk-devel does not work because the version of fltk it provides is
not compatible with the one in /usr/local/lib64/ (this is only a guess).

Cheers,
Bill.


---

Comment by leif created at 2010-08-16 18:41:38

Changing keywords from "" to "FLTK, DSO, libstdc++, plotfltk, FL/Fl.H".


---

Comment by leif created at 2010-08-16 18:41:38

Replying to [comment:15 ggrafendorfer]:
> Here is my report to the pari project and the answer:
> 
> > Hi,
> >
> > there are some problems with the pari package when building sage (http://www.sagemath.org) reported here:
> >
> > http://trac.sagemath.org/sage_trac/ticket/9722
> >
> >
> > I tried to build pari separately (stand alone) but also does not work:
> >
> > After successful configuration pari does not build in 2 different cases:
> >
> > AMD Phenom II X4 925, Fedora 13, with fltk and fltk-devel installed: for log-message see file "log_with_fltk-devel" attached
> >
> > Esprimo 64bit, Fedora 13, with fltk, but not fltk-devel installed: for log-message see file "log_without_fltk-devel" attached
> 
> Hello Georg,
> 
> On both system, there is libfltk library installed in /usr/local/lib64/, but no
> matching header files in /usr/local/include is provided, so compiling fltk does not work.
> Configure output a warning:
> 
> ###
> ### libX11.so not found. Please install X11 development files.
> ### They usually come in XFree86-devel (RPM) or xlibs-dev (Debian) packages
> ###
> ### X11 not found
> ###
> 
> So either install XFree86-devel (or whathever is the correct name of fedora) or use
> --graphic=none to disable graphics.
> 
> Installing fltk and fltk-devel does not work because the version of fltk it provides is
> not compatible with the one in /usr/local/lib64/ (this is only a guess).
> 
> Cheers,
> Bill.

In any case, PARI shouldn't attempt to build with FLTK support if no (or not matching) header files are present; the second (linker) error is also definitely a bug, which currently only shows up on Fedora 13 (and derivatives) due to [stricter linkage rules](http://fedoraproject.org/wiki/UnderstandingDSOLinkChange).

I couldn't (yet) reproduce the errors on 32-bit Fedora 13 though, most probably because _other_ headers and libraries weren't installed. (I tested installing Sage's PARI spkg with only `fltk-1.1.10-1.fc13`, and then in addition `fltk-devel-1.1.10-1.fc13` installed; both with PARI 2.3.5 and the new PARI 2.4.3 svn snapshot from #9343.)

I'll examine that later in more detail.


---

Comment by leif created at 2010-08-16 19:01:05

P.S.: Btw, we *do* (unconditionally) configure PARI with `--graphic=none`...

(Although the user can set `PARI_EXTRA_OPTS` to pass additional configuration options; cf. my trivial work-around above.)


---

Comment by mpatel created at 2010-08-19 09:11:43

Should we reply to the PARI developers with Leif's points?

For now, can we bypass PARI's FLTK checks altogether because/when we use `--graphic=none`?


---

Comment by leif created at 2010-08-19 09:25:51

Replying to [comment:18 mpatel]:
> Should we reply to the PARI developers with Leif's points?
> 
> For now, can we bypass PARI's FLTK checks altogether because/when we use `--graphic=none`?

Cf. also #9343. I couldn't reproduce PARI attempting to build FLTK on any system, including Fedora 13 (32-bit though).

And we already pass `--graphic=none` to PARI's `Configure`...

(I wonder if Georg _wanted_ PARI to use X11/FLTK.)

The missing libstdc++ in `plotfltk`'s libraries is of course a bug (which my patch solves).


---

Comment by leif created at 2010-08-19 09:31:43

s/build FLTK/build using FLTK/


---

Comment by leif created at 2010-08-19 09:44:12

We could in addition bypass (`if false && test ...`) this part of `Configure` for use with Sage:

```sh
...
if test "$optimization" != profiling; then
  . ./get_X11  # X11, X11_INC, X11_LIBS
  . ./get_graphic_lib # which_graphic_lib
  . ./get_fltk # FLTKDIR, FLTK_LIBS
  . ./get_Qt   # QTDIR, QTLIB
  echo "Hi-Res Graphics: $which_graphic_lib"
  . ./get_readline # $_readline_list (includes 'readline')
else
  which_graphic_lib=none
fi
...
```


But that's not very nice, and unless I can reproduce the problem...

And this would of course break graphics support for other users completely.


---

Comment by leif created at 2010-08-19 09:48:48

Georg, could you perhaps attach (upload) the two logfiles you sent to the PARI developers here, too?


---

Comment by leif created at 2010-08-19 10:50:08

Georg, could you please check your environment settings?

```sh
user`@`host$ printenv | grep fltk
```


I found PARI not resetting/initializing variables presumably intended to be locally used only...


---

Comment by leif created at 2010-08-19 10:52:57

Changing status from needs_review to needs_info.


---

Attachment


---

Attachment


---

Comment by ggrafendorfer created at 2010-08-19 14:26:19

Replying to [comment:22 leif]:
> Georg, could you perhaps attach (upload) the two logfiles you sent to the PARI developers here, too?

done, and here is my environment setting:

ggeorg`@`maschke% printenv | grep fltk
ggeorg`@`maschke% rpm -qa | grep fltk
fltk-devel-1.1.10-1.fc13.x86_64
fltk-1.1.10-1.fc13.x86_64
ggeorg`@`maschke%


---

Comment by leif created at 2010-08-19 14:53:26

Replying to [comment:25 ggrafendorfer]:
> Replying to [comment:22 leif]:
> > Georg, could you perhaps attach (upload) the two logfiles you sent to the PARI developers here, too?
> 
> done, and here is my environment setting:
> 

```sh
ggeorg`@`maschke% printenv | grep fltk
ggeorg`@`maschke% rpm -qa | grep fltk
fltk-devel-1.1.10-1.fc13.x86_64
fltk-1.1.10-1.fc13.x86_64
ggeorg`@`maschke% 
```


Hmmm, I could [reproduce your compilation error](http://trac.sagemath.org/sage_trac/ticket/9343#comment:292) on Ubuntu, but only by e.g. `export with_fltk=yes` (with FLTK, but not its header files/devel package installed)...


---

Comment by leif created at 2010-08-19 15:03:17

Replying to [comment:25 ggrafendorfer]:
> Replying to [comment:22 leif]:
> > Georg, could you perhaps attach (upload) the two logfiles you sent to the PARI developers here, too?
> 
> done

Thanks, does the same happen if you run `./Configure --graphic=none`?


---

Comment by ggrafendorfer created at 2010-08-19 15:10:23

Replying to [comment:27 leif]:
> Replying to [comment:25 ggrafendorfer]:
> > Replying to [comment:22 leif]:
> > > Georg, could you perhaps attach (upload) the two logfiles you sent to the PARI developers here, too?
> > 
> > done
> 
> Thanks, does the same happen if you run `./Configure --graphic=none`?

yes, I'll attach the log file,

Georg


---

Attachment

Replying to [comment:28 ggrafendorfer]:
> Replying to [comment:27 leif]:
> > Thanks, does the same happen if you run `./Configure --graphic=none`?
> 
> yes, I'll attach the log file,

LOL, that's because you _don't_ have _X11_ development packages installed! :)

`config/get_fltk`:

```sh
if test -z "$with_fltk"; then
  case "$which_graphic_lib" in
    fltk) with_fltk=yes;;
  esac
  if test -z "$X11"; then with_fltk=yes; fi
fi
...
```


PARI is really funny. I'll fix _all three_ issues and upload a second patch here later...


---

Comment by leif created at 2010-08-19 16:54:03

Changing status from needs_info to needs_work.


---

Comment by jdemeyer created at 2010-08-19 17:38:39

Whatever you do, it would be good to report these issues upstream.  The PARI developers usually accept patches which fix bugs (although they are sometimes slow).  

I haven't followed up on this ticket so much, but does the new version (see #9343) also need patching?


---

Comment by leif created at 2010-08-19 18:26:37

Replying to [comment:30 jdemeyer]:
> Whatever you do, it would be good to report these issues upstream.

I thought _you_ were our PARI spokesman... ;-)

(I guess you'll speak French [too], btw.)

> The PARI developers usually accept patches which fix bugs (although they are sometimes slow).

:) I'm not that sure what the _intended_ logic behind the graphics detection scripts is, so at least one of the fixes is rather targeted at PARI/GP _in Sage_.

So I'll first provide a patch for PARI 2.3.5[.p2] / Sage 4.5.3, then we can see what we report upstream and what we fix in (our) 2.4.3 svn / for #9343 / Sage 4.6.

(The answer Georg got from upstream did not really address his problem btw.)
 
> I haven't followed up on this ticket so much, but does the new version (see #9343) also need patching?

Yes, definitely, despite the scripts having changed between these versions.
I've also commented on that at #9343 a few hours ago...


---

Comment by mpatel created at 2010-08-20 08:37:48

Replying to [comment:29 leif]:
> PARI is really funny. I'll fix _all three_ issues and upload a second patch here later...

I would have guessed that adding `--graphic=none` makes `Configure` skip all graphics detection tests.

I can make an updated spkg with your new patch and host it on sage.math.


---

Comment by mpatel created at 2010-08-21 08:50:35

I'd like to release 4.5.3.rc0 by Monday, 23 August, and if all goes well, 4.5.3 by the end of next week.  Since the necessary changes here aren't trivial --- we'd need to test them on "all" platforms --- I suggest that we fix this ticket in the new PARI spkg at #9343, which I'll merge into 4.6.alpha0.  This presumes that #9343, #9591, and #9592 will be ready.  I'll send a message to sage-devel about their status.


---

Comment by mpatel created at 2010-08-21 21:25:28

Georg, could you look at [comment:ticket:9343:294 Jeroen's comment] at #9343 and let us know any results?


---

Comment by mpatel created at 2010-08-21 21:36:30

Cross-replying to [comment:ticket:9343:296 leif]:
> I'm working on #9722 btw, still hoping that it will make it into 4.5.3, since I don't believe 4.6 will be ready in time, and/or don't expect people to install a brand new major release (despite the ".0" missing) right before a new semester starts.

That's great!  Do you think, for any reason, it'll take more than two days, say, to fix all three problems?


---

Comment by leif created at 2010-08-22 19:13:15

SPKG patch, apply to PARI 2.3.5.p2. Fixes Fedora 13 link error when FLTK is used. (Updated version, only doc changes.)


---

Attachment

*New PARI spkg (p3)*, with the attached patch applied:

http://spkg-upload.googlecode.com/files/pari-2.3.5.p3.spkg

This *only fixes the linker error* on Fedora 13 (that occurred when `fltk-devel` was installed).

If you run into the _compiler_ error, convince your system administrator to
 * _either_ install `fltk-devel`
 * _or_ remove an (invalid) _unversioned_ link to the FLTK library installed. (I.e., if only `fltk` is installed, there should be no `libfltk.so`, but just versioned filenames like e.g. `libfltk.so.1.1`, perhaps including _versioned_ symbolic links to the actual libraries.)

I'll perhaps later upload an improved (p4) spkg that also makes the FLTK-devel detection more robust, s.t. the compiler error shouldn't occur either, even with such unexpected links present.


---

Comment by leif created at 2010-08-22 21:04:31

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-08-22 22:20:45

For me, this has a positive_review, because:
 * I viewed the patch, it makes sense (fltk is c++ after all) and looks good.
 * It doesn't break anything on various systems which I tried (none of these is Fedora though).
 * It fixes the problem for leif (I have *not* tested this).

Leif: keep me up to date with your potential .p4.  I assume this patch has to be ported also to #9343?


---

Comment by jdemeyer created at 2010-08-22 22:20:45

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-08-23 04:43:29

I've compiled a `pari-2.3.5.p4-preview.spkg` (changes not yet checked in, still testing on some systems with various combinations of parameters and installed packages):

```
### pari-2.3.5.p4 (Leif Leonhardy, August 23th 2010)
 * #9722: "--graphic=none" is now respected by PARI. We still look
   for graphics libraries, but don't use them in that case (see below,
   too).
 * #9722: Improved patch to config/get_fltk (makes sure the header
   files are present, too, if the FLTK library was found - fixes
   compiler error on IMHO misconfigured installations).
   We still look for FLTK components even if "--graphic=none" was
   specified, and print appropriate messages, but then simply do not
   use them.
 * #9722: New patch to config/get_X11:
   - Added/corrected/clarified messages regarding what was (not) found,
     and if this is really relevant.
   - An X11 library in */lib64/* will be found now, too (if we do a
     64-bit build); on Fedora, libX11.so is located in /usr/lib64.
   - Added comments.
 * spkg-install:
   - Clear (unset) lots of variables that might (unintentionally) be
     used by PARI; perhaps upstream should initialize them.
   - Clear GP_INSTALL_PREFIX, which is interpreted by PARI.
   - Added help & informational message regarding PARI_EXTRA_OPTS; in
     addition, allow the user to override Sage's "--graphic=none"
     since this now works (see above; we don't want to annoy users
     that perhaps previously made use of GP's plotting support).
 * Clean-up in spkg-install:
   - Quote more environment variables (including SAGE_LOCAL).
   - Consistently use $UNAME instead of `uname` (set in sage-env).
   - Added some comments.
 * NOTE: At least some of these changes should be incorporated into
   our PARI 2.4.3 (svn 12577, see #9343), and/or reported upstream.
   I haven't changed config/get_Qt. It seems Qt support is broken on
   newer systems (because Qt <=3 is expected), but this doesn't break
   the build, only Qt will not be used.
```

Contact me if you are interested in testing this, too. (Appreciated.)

-Leif


---

Comment by leif created at 2010-08-23 04:57:56

I've attached a [diff between the p3 and the p4-preview spkg](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9722/trac_9722-pari-2.3.5.p3-p4.patch), in case anybody is interested... ;-)

Note that this currently is just a diff, not a proper Mercurial patch ("changeset").


---

Comment by jdemeyer created at 2010-08-23 07:44:18

Replying to [comment:39 leif]:
> I've attached a [diff between the p3 and the p4-preview spkg](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9722/trac_9722-pari-2.3.5.p3-p4.patch), in case anybody is interested... ;-)

That's a lot of stuff to look at :-)

I am personally a fan of GNU `autoconf` for these situations because a lot of these checks can be simplified. However, I tried in vain to convince the PARI/GP developers to use `autoconf`. Maybe I should do it for Sage just to prove a point...


---

Comment by leif created at 2010-08-23 08:09:27

Some people call it GNU autocrap...

Also a matter of taste (I personally find the `configure` scripts readable), but autotools often unnecessarily slow down the installation process, and it's easy to build bad scripts with them, too.

Btw, I've meanwhile prepared a new, slightly corrected (wrt. `--graphic=none`) p4 spkg, with also some more comments and improved messages.

I'll update the attached diff here, and after a bit more testing also a link to the (hopefully final) spkg.

(More interesting are the diffs of `get_X11` and `get_fltk`, i.e. `patches/get_{X11,fltk`}.)


---

Comment by jdemeyer created at 2010-08-23 08:16:24

Replying to [comment:41 leif]:
> Some people call it GNU autocrap...
I know some people are against it (for reasons which I never fully understand), but given the choice between editing a configure.ac script and PARI's mess, I will choose the former.


---

Comment by leif created at 2010-08-23 08:31:02

Just to ease seeing some of the changes I made... (Do not apply, it's in the patch, too.)


---

Attachment

Just to ease seeing some of the changes I made... (Do not apply, it's in the patch, too.)


---

Comment by drkirkby created at 2010-08-23 08:51:08

Replying to [comment:42 jdemeyer]:
> Replying to [comment:41 leif]:
> > Some people call it GNU autocrap...
> I know some people are against it (for reasons which I never fully understand), but given the choice between editing a configure.ac script and PARI's mess, I will choose the former.

I'm with Jeroen on that. Properly used, `autoconf` can simplify the build process considerably. 

Of course, any tool badly used can result in a mess. There's one part of Sage where `Makefile.am` is a file that one is expected to edit for "site customisation". Clearly the person using it did not have a clue what he/she was doing. 

I would strongly suggest the Pari developers move to `autoconf/automake`. I've personally not used `libtool` for development, so can't really comment on that. 

Pari's system, where there are specific targets, is always going to be a problem when versions of operating systems change and people have different search order for their PATH. In contrast, the `autoconf` system tests what actually works, using the settings the person building the code has. 

Also, the autoconf/automake mailing lists are very active and helpful. In contrast, I've found with `SCons`, which is another build tool used in Sage, that getting help is very difficult. That takes too much control away from the programmer. I know there's one part of Sage (I forget which) where a developer removed SCons code and replaced it by a Makefile. 

Dave


---

Comment by leif created at 2010-08-23 10:14:30

SPKG patch, now a proper Mercurial changeset. Apply to pari-2.3.5.p3.spkg. (Further improvements w.r.t. graphics support; some clean-up.)


---

Attachment

After testing various combinations of installed (graphics) packages and PARI configure options (`$PARI_EXTRA_OPTS`) on 64-bit Fedora 13, 32-bit and 64-bit Ubuntu 9.04, I'm now quite confident with it and will "release" PARI 2.3.5.p4.

I've replaced the p4-preview diff by a Mercurial patch, and will shortly provide a link to the "final" spkg, with all changes committed.

_"Please build, test, and report!  We'd love to hear about your experiences with this new package."_<sup>TM</sup>

(I've so far only tested the spkg on top of Sage 4.5.3.alpha0 and 4.5.3.alpha1.)


---

Comment by leif created at 2010-08-23 11:12:08

Replying to [comment:44 leif]:
> [...] will shortly provide a link to the "final" spkg, with all changes committed.

New spkg now available: http://spkg-upload.googlecode.com/files/pari-2.3.5.p4.spkg

> _"Please build, test, and report!  We'd love to hear about your experiences with this new package."_<sup>TM</sup>

I think the easiest way to test this is to copy it into `$SAGE_ROOT/spkg/standard`, set and export `PARI_EXTRA_OPTS` as you like, and then do:

```sh
$ ./sage -f pari-2.3.5.p4 2>&1 | tee my_log-parameters.log
```

The "cumulative" spkg install log automatically created by Sage is `$SAGE_ROOT/spkg/logs/pari-2.3.5.p4.log`.

Potential settings for `PARI_EXTRA_OPTS` are:
 * empty / unset (no graphics support; default)
 * `--graphic=auto` (should use X11 if available)
 * `--with-fltk`
 * `--with-qt` (likely to not build on newer systems, requires some Qt development packages too, i.e. _can_ lead to build errors; should disable graphics support if no Qt libraries are found)

Thanks for testing this; we really would like to release Sage 4.5.3[.rc0]...

P.S.: Should work on all reported machines at ETH Zürich, too (with or without `fltk-devel`, even if `--with-fltk` was specified). ;-)

Of course Sage can also be built from scratch with this spkg; just copy the spkg as mentioned above to `spkg/standard` (Sage will automatically pick the newest), and then type `make` or `make build`.


> (I've so far only tested the spkg on top of Sage 4.5.3.alpha0 and 4.5.3.alpha1.)

Also installed without problems on Sage 4.5.2, now running `ptest`.

P.P.S.: The positive review of this ticket currently only applies to the p3 spkg.


---

Comment by mpatel created at 2010-08-23 11:47:47

Changing status from positive_review to needs_info.


---

Comment by mpatel created at 2010-08-23 11:47:54

Changing status from needs_info to needs_review.


---

Comment by mpatel created at 2010-08-23 13:44:07

I get a build failure with `PARI_EXTRA_OPTS=--graphic=x11` on sage.math.  I've put the log [here](http://sage.math.washington.edu/home/mpatel/trac/9722/sage.math--graphic=x11.log).


---

Comment by ggrafendorfer created at 2010-08-23 13:47:27

Replying to [comment:34 mpatel]:
> Georg, could you look at [comment:ticket:9343:294 Jeroen's comment] at #9343 and let us know any results?

worked fine on fedora 13, http://trac.sagemath.org/sage_trac/ticket/9343#comment:307
sorry for the delay, it's my office machine,

Georg


---

Comment by mpatel created at 2010-08-23 14:00:44

I've updated the description with a link to the new package.

*But does PARI 2.4.3.svn-12577 fix the problem anyway?*  Georg, could you try installing Jeroen's spkg with

 `./sage -f http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg`

?  Sage will not work properly without other the changes at #9343 (and related tickets; see [NewPARI](http://wiki.sagemath.org/NewPARI)), but it would help to know.  Thanks for your patience.


---

Comment by leif created at 2010-08-23 14:03:32

Replying to [comment:48 mpatel]:
> I get a build failure with `PARI_EXTRA_OPTS=--graphic=x11` on sage.math.  I've put the log [here](http://sage.math.washington.edu/home/mpatel/trac/9722/sage.math--graphic=x11.log).

I get the same error when I pass `--graphic=this_funny_thing`. (Honestly.) ;-)


---

Comment by mpatel created at 2010-08-23 14:20:29

Replying to [comment:51 leif]:
> Replying to [comment:48 mpatel]:
> > I get a build failure with `PARI_EXTRA_OPTS=--graphic=x11` on sage.math.  I've put the log [here](http://sage.math.washington.edu/home/mpatel/trac/9722/sage.math--graphic=x11.log).
> 
> I get the same error when I pass `--graphic=this_funny_thing`. (Honestly.) ;-)

Oops.  I should have set `PARI_EXTRA_OPTS=--graphic=X11`.  With this, I don't get an error.


---

Comment by leif created at 2010-08-23 14:29:03


```sh
[leif`@`quadriga tmp]$ cd pari-2.3.5.p4/src/
[leif`@`quadriga src]$ ./Configure --help
Configuring pari-2.3.5 (STABLE) 
Usage: Configure [-ask|-help|-g|-pg] [ --load <filename> ] [ --prefix=<dir> ]

Options: some names can be abbreviated to one character (e.g -h = -help)
-a, --ask        interactive configuration
-h, --help       this message
-l, --load       skip Configure and specify a default config file
-s, --static     build static GP binary only
-v, --verbhelp   a longer help message
Build Options:
  --host=<arch-osname>  target achitecture
  --kernel=<kern>       kernel used
  --graphic=<gr>        graphic library used (default X11) (none X11 Qt fltk)
  --time=<fun>          timing function to use (getrusage times ftime)
  --builddir=<dir>      directory where the object files will be created
Additional developer options:
  -g              creates debugging version (in Oxxx.dbg)
  -pg             creates profiling version (in Oxxx.prf)

Installation directories:
  --prefix=<dir>        install files in <dir> (default /usr/local)
  --share-prefix=<dir>  as 'prefix', for architecture independent files
  --bindir=<dir>        for binaries
  --emacsdir=<dir>      for emacs macros
  --includedir=<dir>    for C header files
  --libdir=<dir>        for libraries
  --mandir=<dir>        for manual pages
  --sysdatadir=<dir>    for architecture-dependent data
  --datadir=<dir>       for architecture-independent data 

Optional libraries:
  --without-readline          do not link with GNU readline
  --with-readline[=DIR]       use GNU readline [prefix for readline files]
  --with-readline-include=DIR specify location of readline headers
  --with-readline-lib=DIR     specify location of readline libs
  --with-ncurses-lib=DIR      specify location of ncurses lib (for readline)

  --without-gmp               use the native kernel instead of GNU MP
  --with-gmp[=DIR]            use the GMP kernel [prefix for gmp files]
  --with-gmp-include=DIR      specify location of gmp headers
  --with-gmp-lib=DIR          specify location of gmp libs

  --with-qt[=DIR]        use the Qt graphical library [prefix for Qt dir.]
  --with-fltk[=DIR]      use the FLTK graphical library [prefix for FLTK dir.]
```


Of course we (or actually upstream) should catch such.


---

Comment by mpatel created at 2010-08-23 14:45:41

Replying to [comment:50 mpatel]:
> *But does PARI 2.4.3.svn-12577 fix the problem anyway?*  Georg, could you try installing Jeroen's spkg with
> 
>  `./sage -f http://cage.ugent.be/~jdemeyer/sage/pari-2.4.3.svn-12577.p2.spkg`
> 
> ?  Sage will not work properly without other the changes at #9343 (and related tickets; see [NewPARI](http://wiki.sagemath.org/NewPARI)), but it would help to know.  Thanks for your patience.

And more importantly for this ticket, does Leif's [new spkg](http://spkg-upload.googlecode.com/files/pari-2.3.5.p4.spkg) help on the ETH Zürich Fedora 13 machines?


---

Comment by mpatel created at 2010-08-23 14:54:13

The p4 package installs cleanly with various legal settings for `PARI_EXTRA_OPTS` on bsd, redhawk, sage, and t2.math.  The long doctests then pass on redhawk and sage.math.  I'm now running the tests on bsd and t2.


---

Comment by mpatel created at 2010-08-23 14:56:42

Combined p2-p4 SPKG patch


---

Attachment

Replying to [comment:45 leif]:
> Replying to [comment:44 leif]:
> > (I've so far only tested the spkg on top of Sage 4.5.3.alpha0 and 4.5.3.alpha1.)
> 
> Also installed without problems on Sage 4.5.2, now running `ptest`.

 * Passed `make ptest` with Sage 4.5.2, Ubuntu 9.04 x86 (P4 Prescott, gcc 4.3.3).
 * Passed `make test` with Sage 4.5.3.alpha1, Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3).
 * Passed `make ptestlong` with Sage 4.5.3.alpha1, Fedora 13 x86_64 (Core2, gcc 4.4.4).


---

Comment by ggrafendorfer created at 2010-08-23 17:14:04

Replying to [comment:45 leif]:

building sage 4.5.3.alpha1 from scratch works fine now on fedora 13,

thanks, Georg


---

Comment by jdemeyer created at 2010-08-23 19:03:48

Built .p4 successfully with all possible options for --graphic on a x86_64 Gentoo Linux system.

The patch looks messy though, it might be non-trivial to port to #9343.


---

Comment by mpatel created at 2010-08-23 19:50:06

Replying to [comment:56 mpatel]:
> The p4 package installs cleanly with various legal settings for `PARI_EXTRA_OPTS` on bsd, redhawk, sage, and t2.math.  The long doctests then pass on redhawk and sage.math.  I'm now running the tests on bsd and t2.

The long doctests also pass on bsd and t2.


---

Comment by mpatel created at 2010-08-23 22:13:21

Replying to [comment:58 ggrafendorfer]:
> building sage 4.5.3.alpha1 from scratch works fine now on fedora 13,

Great!

Replying to [comment:59 jdemeyer]:
> The patch looks messy though, it might be non-trivial to port to #9343. 

Yes.  I think we can ask for Leif's help.

Although I can't test every branch in the patched `Configure` script, the changes look correct to me.  The package also installs and tests well on a variety of systems.


---

Comment by mpatel created at 2010-08-23 22:13:21

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-24 02:50:04

Resolution: fixed
