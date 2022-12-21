# Issue 4461: fricas-1.0.4 update

Issue created by migration from Trac.

Original creator: bpage

Original creation time: 2008-11-07 16:45:58

Assignee: mabshoff

Keywords: axiom interface

The fricas project [http://groups.google.com/group/fricas-devel/t/813c8e04c3052043?hl=en](http://groups.google.com/group/fricas-devel/t/813c8e04c3052043?hl=en) has a new release (1.0.4) which includes enhancements specifically related to the Sage interface. A new version of the optional fricas package (current verson fricas-1.0.3.p0) needs to be created.

The procedure involves first building fricas on some convenient platform to generate cached lisp code. This might take about 1 - 2 hours on a fast machine.  This generated code can than be included in a new source distribution created by running

  ../fricas/src/scripts/mkdist.sh --copy_lisp

The contents of the ./dist directory can be moved to the ./src directory of the spkg. The use of cached lisp allows fricas to be built in about 12 minutes or less on a the target machine.

Note: There may be a problem with clisp support of FFI in Sage. A patch to allow fricas to build without FFI is attached (not yet tested with fricas-1.0.4).


---

Attachment

disable FFI in fricas


---

Comment by mabshoff created at 2008-11-07 17:08:02

I am not sure what to do about the Aldor interface, i.e. we discourage spkgs downloading content dynamically during build. For now I would prefer that the default for now does not attempt to build the Aldor interface and only does so if some env variable (like SAGE_FRICAS_ALDOR is equal to 'yes').

Cheers,

Michael


---

Comment by bpage created at 2009-01-27 03:56:30

No package for fricas release 1.0.4 was ever completed. Meanwhile there is a new version of FriCAS available.

An experimental package for fricas release 1.0.5 is available here:

[http://sage.math.washington.edu/home/page/packages/fricas-1.0.5.spkg](http://sage.math.washington.edu/home/page/packages/fricas-1.0.5.spkg)

So far I have only tested this package with sage-3.1.2 on sage.math using the following commands:


```
  $ wget http://sage.math.washington.edu/home/page/packages/fricas-1.0.5.spkg
  $ .../sage -f fricas-1.0.5.spkg
```


For example with this version you can compute the following integral:


```
sage: ex1=axiom(2^x/sqrt(1+4^x));ex1

       x
      2
  ---------
   +------+
   | x
  \|4  + 1
sage: ex1.integrate(x)

         +-----------------+
         |   x log(2) 2          x log(2)
    log(\|(%e        )  + 1  - %e        )
  - --------------------------------------
                    log(2)

```



Help testing on other platforms and versions of Sage would be appreciated.


---

Comment by bpage created at 2009-01-27 13:18:42

On Mon, 26 Jan 2009 21:56:44 -0800 William Stein wrote:

It fails the following tests (have you posted a patch to trac to update this)?

By the way, when using this, I repeatedly felt like I wished the
command in Sage were "fricas" instead of "axiom" and the file to test
were "fricas.py" instead of "axiom.py".


```
wstein`@`sage:~/sage/devel/sage/sage/interfaces$ sage -t -optional axiom.py
sage -t -optional "devel/sage-main/sage/interfaces/axiom.py"
**********************************************************************
File "/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py", line 61:
    sage: F.type()                              # optional
Expected:
    Factored Polynomial Integer
Got:
    Factored(Polynomial(Integer))
**********************************************************************
File "/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py", line 80:
    sage: print axiom.eval('factor(x^5 - y^5)')   # optional
Expected:
               4      3    2 2    3     4
    - (y - x)(y  + x y  + x y  + x y + x )
    <BLANKLINE>
    Type: Factored Polynomial Integer
Got:
                 4      3    2 2    3     4
      - (y - x)(y  + x y  + x y  + x y + x )


                                                                 Type:
Factored(Polynomial(Integer))
    <BLANKLINE>
**********************************************************************
File "/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py", line 561:
    sage: axiom(x+2).type()  #optional -- requires Axiom
Expected:
    Polynomial Integer
Got:
    Polynomial(Integer)
**********************************************************************
File "/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py", line 623:
    sage: _.type()        #optional
Expected:
    Tuple PositiveInteger
Got:
    Tuple(PositiveInteger)
**********************************************************************
3 items had failures:
   2 of  21 in __main__.example_0
   1 of   3 in __main__.example_19
   1 of   6 in __main__.example_22

```



---

Comment by mhansen created at 2009-02-19 20:38:12

Hi Bill, 

I made a patch at #5111 which separates the FriCAS and the Axiom interfaces.  Most of the functionality is still in axiom.py since it is common to both.  Also, the improvements at #4036 are in that patch.

Could you make it so that the spkg does not install an executable named 'axiom'?  Then, we can put that spkg up when that patch goes in.

Thanks,
--Mike


---

Comment by mhansen created at 2009-02-19 20:38:12

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-19 20:38:12

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-02-19 22:39:53

It looks like this is being taken care of at http://groups.google.com/group/fricas-devel/browse_thread/thread/3f6186988dc9683e?hl=en


---

Comment by mvngu created at 2009-08-12 16:48:45

Changing component from packages to optional packages.


---

Comment by mvngu created at 2009-08-12 16:48:45

Resolution: wontfix


---

Comment by mvngu created at 2009-08-12 16:48:45

Closing this as #6517 deals with a more recent version of FriCAS than the current ticket.
