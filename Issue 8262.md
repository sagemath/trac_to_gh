# Issue 8262: developer's guide: document the variable SAGE_CHECK

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-02-14 12:19:48

Assignee: mvngu

As the subject says.


---

Comment by drkirkby created at 2010-02-14 14:01:57

Changing assignee from mvngu to drkirkby.


---

Comment by drkirkby created at 2010-02-14 14:01:57

See also #8263, which aims to document all environment variables. SAGE_CHECK is not the only one which is either undocumented, or poorly documented.


---

Comment by mpatel created at 2010-03-02 23:48:14

Some somewhat related data: `SAGE_LOCAL/bin/sage-spkg` contains

```sh
    cd $BASEDIR
    if [ "$SAGE_CHECK" != "" -a -f spkg-check ]; then
        echo "Running the test suite."
        chmod +x spkg-check
        ./spkg-check
        if [ $? -ne 0 ]; then
```

but


```sh
$ \ls -1 /home/release/latest/sage-4.3.3/spkg/standard/*.spkg | awk '{print "tar jxvf "$0}' > zz
$ . zz
$ gr -A3 -B2 spkg-check */spkg-install
flint-1.5.0.p3/spkg-install-
flint-1.5.0.p3/spkg-install-if [ "$SAGE_CHECK" = "yes" ]; then
flint-1.5.0.p3/spkg-install:    cd ..; ./spkg-check
flint-1.5.0.p3/spkg-install-fi
--
mpfr-2.4.1.p1/spkg-install-# Do not bypass the checks, as some MPFR failures
mpfr-2.4.1.p1/spkg-install-# have been observed, so MPFR should be carefully tested.
mpfr-2.4.1.p1/spkg-install:cd ..; ./spkg-check
--
mpir-1.2.2.p0/spkg-install-
mpir-1.2.2.p0/spkg-install-if [ "$SAGE_CHECK" = "yes" ]; then
mpir-1.2.2.p0/spkg-install:    cd ..; ./spkg-check
mpir-1.2.2.p0/spkg-install-fi
```

In particular, with `SAGE_CHECK="yes"`, the flint's long-running tests are run twice.


---

Comment by rlm created at 2010-07-16 07:54:32

Can this ticket be closed now?


---

Comment by mvngu created at 2010-07-16 07:59:56

Replying to [comment:3 rlm]:
> Can this ticket be closed now?

Yes, this ticket can be closed. The issue of this ticket has been fixed in #8263. I leave it to the release manager to close the current ticket.


---

Comment by rlm created at 2010-07-16 08:03:27

Resolution: duplicate


---

Comment by rlm created at 2010-07-16 08:03:27

Right. Just wanted a second opinion. Thanks!


---

Comment by mpatel created at 2010-07-16 21:02:42

Revisiting [comment:2 the comment above] for Sage 4.5, I get

```sh
$ \ls -1 /path/to/sage-4.5/spkg/standard/*.spkg | awk '{print "tar jxvf "$0}' > unpackem
$ . unpackem
$ egrep -A3 -B2 -i SAGE_CHECK\|spkg-check */spkg-install
cliquer-1.2.p5/spkg-install-fi
cliquer-1.2.p5/spkg-install-
cliquer-1.2.p5/spkg-install:if [ "$SAGE_CHECK" = "yes" ]; then
cliquer-1.2.p5/spkg-install-    echo "Compiling and running the test cases of cliquer..."
cliquer-1.2.p5/spkg-install-
cliquer-1.2.p5/spkg-install-    make testcases
--
mpfr-2.4.2/spkg-install-# Do not bypass the checks, as some MPFR failures
mpfr-2.4.2/spkg-install-# have been observed, so MPFR should be carefully tested.
mpfr-2.4.2/spkg-install:cd ..; ./spkg-check
--
mpir-1.2.2.p1/spkg-install-fi
mpir-1.2.2.p1/spkg-install-
mpir-1.2.2.p1/spkg-install:if [ "$SAGE_CHECK" = "yes" ]; then
mpir-1.2.2.p1/spkg-install:    cd ..; ./spkg-check
mpir-1.2.2.p1/spkg-install-fi
```

If no one objects, I can open tickets for MPIR and Cliquer.


---

Comment by mpatel created at 2010-07-17 01:03:37

Replying to [comment:6 mpatel]:
> If no one objects, I can open tickets for MPIR and Cliquer.

These are now #9522 (MPIR) and #9521 (Cliquer).
