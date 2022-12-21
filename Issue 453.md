# Issue 453: singuname.sh support for Nexenta OS

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-19 08:27:02

Assignee: malb

Hello Martin, 

can you merge the following?

From Didier Deshommes:

And for singular to find ix86-nexentaos, singuname.sh has to have the following:

```
elif (echo $uname_a | $egrep "SunOS" >$devnull)
    then
        # NexentaOS ###############
        if (echo $uname_a | $egrep "NexentaOS" > $devnull)
            then
               #echo "----------------------------------------------------"
               echo ${prefix}-nexentaos
               #echo "----------------------------------------------------"
               #exit 0
        else
            echo ix86-SunOS
            #exit 0
        fi
        exit 0
```


This might also be interesting for the official Singular upstream.

Cheers,

Michael


---

Comment by malb created at 2007-08-19 15:35:00

fixed in /home/malb/pkgs/singular-3-0-3-20070819.spkg.


---

Comment by malb created at 2007-08-19 15:35:00

Resolution: fixed
