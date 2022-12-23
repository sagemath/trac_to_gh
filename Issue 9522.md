# Issue 9522: MPIR: Don't check SAGE_CHECK in spkg-install

Issue created by migration from https://trac.sagemath.org/ticket/9522

Original creator: mpatel

Original creation time: 2010-07-17 01:02:45

Assignee: tbd

From the end of MPIR's `spkg-install`:

```sh
if [ "$SAGE_CHECK" = "yes" ]; then
    cd ..; ./spkg-check
fi
```

We should remove this, since `SAGE_LOCAL/bin/sage-spkg` already does this check:

```sh
    cd $BASEDIR
    if [ "$SAGE_CHECK" != "" -a -f spkg-check ]; then
        echo "Running the test suite."
        chmod +x spkg-check
        ./spkg-check
        if [ $? -ne 0 ]; then
```



---

Comment by leif created at 2010-08-26 21:02:56

There's already [a ticket for updating MPIR to version 2.1.1](http://trac.sagemath.org/sage_trac/ticket/8664) (currently needing review), which apparently is aware of _this_ ticket.

I though haven't checked if Mike deleted the superfluous test suite invocation in `spkg-install`.


---

Comment by leif created at 2010-08-26 21:24:52

Replying to [comment:1 leif]:
> I though haven't checked if Mike deleted the superfluous test suite invocation in `spkg-install`.

Done, he _did_ remove it. So *this ticket can be closed as duplicate as soon as #8664 gets merged*.


---

Comment by drkirkby created at 2010-09-21 19:45:08

I think there's a good argument for running the mpir test suite every time (i.e. from spkg-install), as it has historically caught several compiler bugs. 

It's obviously pointless running it twice. 

Dave


---

Comment by leif created at 2011-09-29 23:46:49

Resolution: fixed
