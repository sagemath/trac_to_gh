# Issue 143: Gnuplot build fails on sage-1.4.1.2

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2006-10-21 20:41:55

Assignee: was

Missing header file:

gnuplot-4.0.0: blew chunks here:
    if gcc -DHAVE_CONFIG_H -I. -I. -I..  -I../term -I../term \
         -DBINDIR=\"/SandBox/Justin/sb/sage-1.4/local/bin\" \
         -DX11_DRIVER_DIR=\"/SandBox/Justin/sb/sage-1.4/local/libexec/gnuplot/4.0\" \
         -DCONTACT=\"gnuplot-bugs`@`lists.sourceforge.net\" \
         -DHELPFILE=\"/SandBox/Justin/sb/sage-1.4/local/share/gnuplot/4.0/gnuplot.gih\" \
         -I/SandBox/Justin/sb/sage-1.4/local/include  -g -O2 -ObjC -MT gplt_x11.o -MD -MP \
         -MF ".deps/gplt_x11.Tpo" \
      -c -o gplt_x11.o `test -f 'gplt_x11.c' || echo './'`gplt_x11.c; \
    then mv ".deps/gplt_x11.Tpo" ".deps/gplt_x11.Po"; \
    else rm -f ".deps/gplt_x11.Tpo"; exit 1; \
    fi
    gplt_x11.c:519: error: 'Class' redeclared as different kind of symbol
    <built-in>:0: error: previous declaration of 'Class' was here
    make[3]: *** [gplt_x11.o] Error 1
    make[2]: *** [all-recursive] Error 1
    make[1]: *** [all-recursive] Error 1
    make: *** [all] Error 2
    Error building gnuplot



---

Attachment

Build log for gnuplot


---

Comment by justin created at 2006-10-22 21:13:09

The problem is that, on Mac OS X, gnuplot builds with the flag "-ObjC" (enable Objective C support).  This has to do with support for something called AquaTerm, which it (gnuplot) can use as a display vehicle.

The flag should only be used for the code that actually uses Objective C, but instead it is used for all code; 'Class' is a reserved word for Objective C, and a variable name in the gnuplot code.  Hence...

We need an 'autoconfig' guy!


---

Comment by was created at 2007-01-12 23:33:56

Resolution: wontfix


---

Comment by was created at 2007-01-12 23:33:56

Since gnuplot is not integrated in any way with SAGE, and won't be a longterm part of SAGE, people should get it some other way (e.g., fink or Darwinports, etc.).  Therefore I've removed SAGE's optional gnuplot package.
