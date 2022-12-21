# Issue 1476: R -- enable installation of optional packages

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-12 16:04:27

Assignee: was


```
tried to test it... but funny things, at first I wasn't able to
install any package... take a look at this:

gcc -std=gnu99 -I/opt/sage/local/lib/r//include -I/opt/sage/local/lib/
r//include  -I/usr/local/include WARNING: ignoring environment value
of R_HOME  -fvisibility=hidden -fpic  -I/opt/sage/local/include -L/opt/
sage/local/lib/  -c corStruct.c -o corStruct.o
gcc: WARNING:: No such file or directory
gcc: ignoring: No such file or directory
gcc: environment: No such file or directory
gcc: value: No such file or directory
gcc: of: No such file or directory
gcc: R_HOME: No such file or directory
make: *** [corStruct.o] Error 1

this actually stops any addon R library installation... I got that
running R from Sage, using !R and typing install.packages("MASS",
dependencies=T) - there are more of those of course, for almost
every .c file in libraries... after commenting out first few lines in
local/bin/R and local/lib/r/bin/R - warning was no longer generated
and thus I was able to install packages... (I think those can be
commented because variables set and checked there are overwritten in
"sagehack" just below... this almost allowed me to build packages,
because one failed (it works on my plain R install, sage-fortran
wasn't able to compile one file - it was library "Hmisc" that failed:

sage_fortran   -fpic  -g -O2 -c largrec.f -o largrec.o
In file largrec.f:27

     DO xl=xlim(1),xlim(2)-width,xinc
        1
Error: Loop variable at (1) must be a scalar INTEGER
In file largrec.f:28

        DO yl=ylim(1),ylim(2)-height,yinc
           1
Error: Loop variable at (1) must be a scalar INTEGER
In file largrec.f:29

           DO xr=xl+width,xlim(2),xinc
              1
Error: Loop variable at (1) must be a scalar INTEGER
In file largrec.f:30

              DO yu=yl+height,ylim(2),yinc
                 1
Error: Loop variable at (1) must be a scalar INTEGER
make: *** [largrec.o] Error 1

is this sage_fortran problem or package problem but it works on system
compiler...

anyway I installed other package (tseries) and was able to use
functions from (from R console, Sage console and notebook), just auto-
compl. worked for those functions after they were called for the first
time not before...

On Dec 12, 2007 2:35 AM, Marshall Hampton <hamptonio`@`gmail.com> wrote:
>
> Hi,
>
> I'm not very familiar with R and rpy, but in reading the rpy
> documentation they implied that if you install optional R components
> you do _not_ have to rebuild rpy...but I suppose someone should verify/
> test that.
>
> Marshall Hampton
>

cheers,
```



---

Comment by rlm created at 2007-12-19 19:52:04

Resolution: worksforme
