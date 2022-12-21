# Issue 870: singular.spkg requires bison to build

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-13 02:11:40

Assignee: malb

See http://groups.google.com/group/sage-forum/browse_thread/thread/6f56a3cc9f4a1598

To quote malb:

```
Hi,

SAGE 2.8.5 shipped a version of Singular where we got rid of the dependency of
bison/flex ourselves. SAGE 2.8.6 removes this workaround because Singular
3-0-3-1 handles this itself.

However, it seems the Singular team forgot to take care of the factory
library. There are three ways to solve this issue for you:

(a) Install bison for now

(b) replace

$(srcdir)/readcf.cc: readcf.y
        $(BISON) $< -o $`@`; \

with

$(srcdir)/readcf.cc: readcf.y
                `@`if test -r $`@`; then \
                        touch $`@` ;\
                else \
                if test "${BISON}" = where-is-your-bison; then \
                        echo Error: no bison given, could not rebuilt
grammar.cc; \
                        exit 1; \
                fi; \
                $(BISON) $< -o $`@`; \
                fi

in the singular spkg / factory/GNUmakefile.in or drop in the attached file.
This requires that you know a little about SAGE SPKGs.

(c) wait until I got confirmation from the Singular team and provide an
updated SPKG. (I am BCC'ing Hans Schönemann from the Singular team with this
e-mail)

Cheers,
Martin 
```



---

Comment by mabshoff created at 2007-10-13 02:12:18

malb's temporary solution


---

Attachment


---

Comment by malb created at 2007-10-20 18:32:10

This is fixed in Singular 3-0-3-2 and an updated spkg can be found at
 http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071020.spkg


---

Comment by malb created at 2007-10-20 18:32:34

This is fixed in Singular 3-0-3-2 and an updated spkg can be found at 

http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071020.spkg


---

Comment by was created at 2007-10-20 18:43:24

Resolution: fixed
