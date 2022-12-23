# Issue 5333: pynac.spkg: Delete old pynac libray during spkg-install

Issue created by migration from https://trac.sagemath.org/ticket/5333

Original creator: mabshoff

Original creation time: 2009-02-21 22:54:28

Assignee: mabshoff

Left over pynac libraries in $SAGE_LOCAL/lib cause upgrade trouble from some releases. William reported some as well as John Cremona in 

http://groups.google.com/group/sage-devel/t/d1105e1b1cd3d057

The fix is trivial, but very important to get into 3.4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-21 22:54:38

Changing status from new to assigned.


---

Comment by burcin created at 2009-02-26 11:10:03

Resolution: fixed


---

Comment by burcin created at 2009-02-26 11:10:03

The pynac package already deletes the existing libraries before installing new ones. The errors mentioned on the linked threads were seen because the sage library was not updated properly.

Here are the relevant lines from spkg-install in pynac-0.1.2.spkg, which is included in Sage-3.3:

```
install_pynac()
{
    rm ${SAGE_LOCAL}/lib/*ginac*
    rm ${SAGE_LOCAL}/lib/*pynac*
    rm -rf ${SAGE_LOCAL}/include/ginac
    rm -rf ${SAGE_LOCAL}/include/pynac
    cd ${PYNACDIR}
    $MAKE install
    if [ $? -ne 0 ]; then
        echo "Error installing pynac."
        exit 1
    fi
    cd ${WORKDIR} 
}
```


I suggest resolving this as invalid.


---

Comment by burcin created at 2009-02-26 11:10:38

Resolution changed from fixed to 


---

Comment by burcin created at 2009-02-26 11:10:38

Changing status from closed to reopened.


---

Comment by burcin created at 2009-02-26 11:10:38

I need to learn how to use trac.


---

Comment by mabshoff created at 2009-02-26 11:50:46

Replying to [comment:3 burcin]:
> I need to learn how to use trac. 

:)

But you are right -> invalid.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-26 11:50:46

Resolution: invalid
