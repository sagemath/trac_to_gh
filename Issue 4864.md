# Issue 4864: graphviz optional spkg is broken on our main devel machine (sage.math)

Issue created by migration from https://trac.sagemath.org/ticket/4864

Original creator: was

Original creation time: 2008-12-24 05:16:06

Assignee: mabshoff

On sage.math (ubuntu 8.04), the graphviz optional package does not build.


```
sage: install_package('graphviz-2.16.1.p0')        
...
make[3]: Entering directory `/usr/local/sage/spkg/build/graphviz-2.16.1.p0/src/cmd/dot'
gcc -DHAVE_CONFIG_H -I. -I../..  -I../../lib/common -I../../lib/gvc -I../../lib/pathplan -I../../lib/graph -I../../lib/cdt -I/usr/local/sage/local/include -I/usr/local/sage/local/include  -g -O2 -Wno-unknown-pragmas -Wstrict-prototypes -Wpointer-arith -Wall -ffast-math -MT dot.o -MD -MP -MF .deps/dot.Tpo -c -o dot.o dot.c
mv -f .deps/dot.Tpo .deps/dot.Po
/bin/bash ../../libtool --tag=CC   --mode=link gcc  -g -O2 -Wno-unknown-pragmas -Wstrict-prototypes -Wpointer-arith -Wall -ffast-math  -L/usr/local/sage/local/lib -L/usr/local/sage/local/lib -o dot dot.o ../../lib/gvc/libgvc.la 
mkdir -p .libs
gcc -g -O2 -Wno-unknown-pragmas -Wstrict-prototypes -Wpointer-arith -Wall -ffast-math -o .libs/dot dot.o  -L/usr/local/sage/local/lib ../../lib/gvc/.libs/libgvc.so /usr/local/sage/spkg/build/graphviz-2.16.1.p0/src/lib/graph/.libs/libgraph.so /usr/local/sage/spkg/build/graphviz-2.16.1.p0/src/lib/cdt/.libs/libcdt.so /usr/local/sage/spkg/build/graphviz-2.16.1.p0/src/lib/pathplan/.libs/libpathplan.so -lm /usr/local/sage/spkg/build/graphviz-2.16.1.p0/src/libltdl/.libs/libltdl.so -ldl -lz  -Wl,--rpath -Wl,/usr/local/sage/local/lib
creating dot
gcc -DHAVE_CONFIG_H -I. -I../..  -I../../lib/common -I../../lib/gvc -I../../lib/pathplan -I../../lib/graph -I../../lib/cdt -I/usr/local/sage/local/include -I/usr/local/sage/local/include  -g -O2 -Wno-unknown-pragmas -Wstrict-prototypes -Wpointer-arith -Wall -ffast-math -MT dot_builtins.o -MD -MP -MF .deps/dot_builtins.Tpo -c -o dot_builtins.o `test -f '../../lib/gvc/dot_builtins.c' || echo './'`../../lib/gvc/dot_builtins.c
mv -f .deps/dot_builtins.Tpo .deps/dot_builtins.Po
gcc -DHAVE_CONFIG_H -I. -I../..  -I../../lib/common -I../../lib/gvc -I../../lib/pathplan -I../../lib/graph -I../../lib/cdt -I/usr/local/sage/local/include -I/usr/local/sage/local/include  -g -O2 -Wno-unknown-pragmas -Wstrict-prototypes -Wpointer-arith -Wall -ffast-math -MT no_demand_loading.o -MD -MP -MF .deps/no_demand_loading.Tpo -c -o no_demand_loading.o `test -f '../../lib/gvc/no_demand_loading.c' || echo './'`../../lib/gvc/no_demand_loading.c
mv -f .deps/no_demand_loading.Tpo .deps/no_demand_loading.Po
make[3]: *** No rule to make target `../../plugin/pango/libgvplugin_pango.la', needed by `dot_builtins'.  Stop.
make[3]: Leaving directory `/usr/local/sage/spkg/build/graphviz-2.16.1.p0/src/cmd/dot'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/usr/local/sage/spkg/build/graphviz-2.16.1.p0/src/cmd'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/usr/local/sage/spkg/build/graphviz-2.16.1.p0/src'
make: *** [all] Error 2
Error building Graphviz

real	2m0.002s
user	1m8.040s
sys	0m48.450s
sage: An error occurred while installing graphviz-2.16.1.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /usr/local/sage/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/usr/local/sage/spkg/build/graphviz-2.16.1.p0 and type 'make'.
Instead type "/usr/local/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/usr/local/sage/spkg/build/graphviz-2.16.1.p0
(When you are done debugging, you can type "exit" to leave the
subshell.)
sage:             
```



---

Comment by was created at 2008-12-24 05:34:08


```
21:14 < mabshoff> it is broken because there is no pango installed
21:14 < mabshoff> "plugin/pango/libgvplugin_pango.la
21:14 < wstein> It should give an appropriate error message then.
```


I tried 

```
root@sage:/usr/local/sage# apt-get install libpango1.0-dev
```

then ...

```
6_64-linux-gnu/4.2.4/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/4.2.4/../../../../lib/crtn.o  -Wl,-soname -Wl,libgv_perl.so -o .libs/libgv_perl.so
/usr/bin/ld: cannot find -lperl
collect2: ld returned 1 exit status
make[3]: *** [libgv_perl.la] Error 1
make[3]: Leaving directory `/usr/local/sage/spkg/build/graphviz-2.16.1.p0/src/tclpkg/gv'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/usr/local/sage/spkg/build/graphviz-2.16.1.p0/src/tclpkg'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/usr/local/sage/spkg/build/graphviz-2.16.1.p0/src'
make: *** [all] Error 2
Error building Graphviz

real	2m25.262s
user	1m24.640s
sys	0m57.060s
sage: An error occurred while installing graphviz-2.16.1.p0
```


Next I tried:

```
root@sage:/usr/local/sage# apt-get install libperl-dev
```


And the build of graphviz worked.  So the only problem is dependency detection. 

---

To close this ticket, it would be good to report the detection bugs to graphviz upstream and/or write our own little script that checks for libperl and libpango by trying to link a little C program against them (or runs an autoconf script). 

But I would be OK with this ticket being closed now, since the title of it -- graphviz doesn't build on sage.math, is now completely fixed.


---

Comment by was created at 2008-12-24 05:35:51

Resolution: fixed
