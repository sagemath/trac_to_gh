# Issue 2068: zlib -- not picking up the right zlib when building libpng

Issue created by migration from https://trac.sagemath.org/ticket/2068

Original creator: was

Original creation time: 2008-02-05 23:13:09

Assignee: mabshoff


```

Hi,

libpng-1.2.22.p5 added this in spkg-install:
LDFLAGS="-L\"$SAGE_LOCAL/lib\" $LDFLAGS"

I tried the following modification:
LDFLAGS="-L$SAGE_LOCAL/lib $LDFLAGS"
and it worked.

The problem is that quoting the arg of -L seems still wise as the path
could contain a space but it seems it interferes with the (eval
"$ac_link") 2>conftest.er1  in src/configure.
E.g. the original LD_FLAGS definition works if we use instead: (eval
bash -c \"$ac_link\") 2>conftest.er1

```



---

Comment by mabshoff created at 2008-02-15 02:13:17

An updated spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha0/libpng-1.2.22.p5.spkg

Compile tested on Linux & OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 02:14:13

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 02:14:13

Merged in Sage 2.10.2.alpha0
