# Issue 143: Gnuplot build fails on sage-1.4.1.2

archive/issues_000143.json:
```json
{
    "body": "Assignee: @williamstein\n\nMissing header file:\n\ngnuplot-4.0.0: blew chunks here:\n    if gcc -DHAVE_CONFIG_H -I. -I. -I..  -I../term -I../term \\\n         -DBINDIR=\\\"/SandBox/Justin/sb/sage-1.4/local/bin\\\" \\\n         -DX11_DRIVER_DIR=\\\"/SandBox/Justin/sb/sage-1.4/local/libexec/gnuplot/4.0\\\" \\\n         -DCONTACT=\\\"gnuplot-bugs`@`lists.sourceforge.net\\\" \\\n         -DHELPFILE=\\\"/SandBox/Justin/sb/sage-1.4/local/share/gnuplot/4.0/gnuplot.gih\\\" \\\n         -I/SandBox/Justin/sb/sage-1.4/local/include  -g -O2 -ObjC -MT gplt_x11.o -MD -MP \\\n         -MF \".deps/gplt_x11.Tpo\" \\\n      -c -o gplt_x11.o `test -f 'gplt_x11.c' || echo './'`gplt_x11.c; \\\n    then mv \".deps/gplt_x11.Tpo\" \".deps/gplt_x11.Po\"; \\\n    else rm -f \".deps/gplt_x11.Tpo\"; exit 1; \\\n    fi\n    gplt_x11.c:519: error: 'Class' redeclared as different kind of symbol\n    <built-in>:0: error: previous declaration of 'Class' was here\n    make[3]: *** [gplt_x11.o] Error 1\n    make[2]: *** [all-recursive] Error 1\n    make[1]: *** [all-recursive] Error 1\n    make: *** [all] Error 2\n    Error building gnuplot\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/143\n\n",
    "created_at": "2006-10-21T20:41:55Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "title": "Gnuplot build fails on sage-1.4.1.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/143",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

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


Issue created by migration from https://trac.sagemath.org/ticket/143





---

archive/issue_comments_000655.json:
```json
{
    "body": "Attachment [Gnuplot.errlog](tarball://root/attachments/some-uuid/ticket143/Gnuplot.errlog) by justin created at 2006-10-21 20:42:52\n\nBuild log for gnuplot",
    "created_at": "2006-10-21T20:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/143#issuecomment-655",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Attachment [Gnuplot.errlog](tarball://root/attachments/some-uuid/ticket143/Gnuplot.errlog) by justin created at 2006-10-21 20:42:52

Build log for gnuplot



---

archive/issue_comments_000656.json:
```json
{
    "body": "The problem is that, on Mac OS X, gnuplot builds with the flag \"-ObjC\" (enable Objective C support).  This has to do with support for something called AquaTerm, which it (gnuplot) can use as a display vehicle.\n\nThe flag should only be used for the code that actually uses Objective C, but instead it is used for all code; 'Class' is a reserved word for Objective C, and a variable name in the gnuplot code.  Hence...\n\nWe need an 'autoconfig' guy!",
    "created_at": "2006-10-22T21:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/143#issuecomment-656",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

The problem is that, on Mac OS X, gnuplot builds with the flag "-ObjC" (enable Objective C support).  This has to do with support for something called AquaTerm, which it (gnuplot) can use as a display vehicle.

The flag should only be used for the code that actually uses Objective C, but instead it is used for all code; 'Class' is a reserved word for Objective C, and a variable name in the gnuplot code.  Hence...

We need an 'autoconfig' guy!



---

archive/issue_comments_000657.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2007-01-12T23:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/143#issuecomment-657",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_comments_000658.json:
```json
{
    "body": "Since gnuplot is not integrated in any way with SAGE, and won't be a longterm part of SAGE, people should get it some other way (e.g., fink or Darwinports, etc.).  Therefore I've removed SAGE's optional gnuplot package.",
    "created_at": "2007-01-12T23:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/143#issuecomment-658",
    "user": "https://github.com/williamstein"
}
```

Since gnuplot is not integrated in any way with SAGE, and won't be a longterm part of SAGE, people should get it some other way (e.g., fink or Darwinports, etc.).  Therefore I've removed SAGE's optional gnuplot package.
