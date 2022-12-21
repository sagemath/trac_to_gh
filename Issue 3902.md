# Issue 3902: %cython -- add an option #clibinclude that is like cinclude; otherwise linking in your own libraries is impossible

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-19 21:27:53

Assignee: cwitty

Right now we have

```
      \item[clang] may be either c or c++ indicating whether a C or
                   C++ compiler should be used

      \item[clib] additional libraries to be linked in, the space
                  separated list is split and passed to distutils.

      \item[cinclude] additional directories to search for header
                      files. The space separated list is split and
                      passed to distutils.
```

and we need

```
      \item[clibinclude] additional directories to search for library
                      files. The space separated list is split and
                      passed to distutils.
```



---

Comment by AlexGhitza created at 2009-01-23 02:47:15

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2019-01-11 13:08:05

Obsoleted by Cython features.


---

Comment by jdemeyer created at 2019-01-11 13:08:05

Resolution: wontfix
