# Issue 9521: Cliquer: Move test commands from spkg-install to spkg-check

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-17 01:00:09

Assignee: tbd

CC:  ncohen leif

From Cliquer's `spkg-install`:

```sh
if [ "$SAGE_CHECK" = "yes" ]; then
    echo "Compiling and running the test cases of cliquer..."

    make testcases
    if [ $? -ne 0 ]; then
        echo "Failed to compile test cases of cliquer... exiting"
        exit 1
    fi

    ./testcases
    if [ $? -ne 0 ]; then
        echo "Failed to run test cases of cliquer... exiting"
        exit 1
    fi
fi
```

We can move this code (or most of it) to a new `spkg-check`.

Since `SAGE_LOCAL/bin/sage-spkg` contains

```sh
    cd $BASEDIR
    if [ "$SAGE_CHECK" != "" -a -f spkg-check ]; then
        echo "Running the test suite."
        chmod +x spkg-check
        ./spkg-check
        if [ $? -ne 0 ]; then
```

we don't need to check `SAGE_CHECK` in `spkg-install`.


---

Comment by drkirkby created at 2010-09-04 07:41:52

See 

http://groups.google.com/group/sage-devel/browse_thread/thread/88102b4c4eadbba7/0100c924f44cf18c?hl=en

I think in this case, it is better to run the test code in `spkg-install` on every build, as it takes takes very little time - about 5 seconds to do so on my machine. As such, I suggest we 

 * Remove the code that actually checks for SAGE_CHECK in spkg-install. 
 * Run the tests all the time. 
 * Make spkg-check just return 0 - there's not much point running it twice. 

One issue here is that `make` exits with 0, even if the test suite fails. I found this after purposely inducing some failures. It makes me wonder how many other test suites do this too! 

See also #9767 and some comments from myself and Leif. 

Dave


---

Comment by drkirkby created at 2010-09-04 08:27:10

I've closed #9767 as a duplicate of this one. I've cc'ed Leif, who commented on #9767 and Nathann as the package maintainer. 

I need to respond to Leif's comment on #9767 though: 

*Dave, be warned: You'll hate me if I should review this (`spkg-install`, `patches/Makefile`).*

I think Leif has unreasonable expectations some times - in particular #9603, (an iconv change), has resulted in a large number of changes, which all took time, which could have been better spent addressing other more serious issues in Sage. The number of changes Leif requested on #9603 was excessive I feel. Six weeks after the ticket was created to just add 

`&& [ "x$UNAME" != xHP-UX ]` 

it is still awaiting a positive review. 

I'm not denying the changes Leif requested on #9603 has improved the iconv package - though I think it was one of the better packages to start with. I do however think the time spent on it could have been put to more productive use. 

If tickets to add a very small change are going to result in weeks of iterations, then the changes are not going to be made - at least not by me. 

I am happy to attempt to clean up Cliquer, but on the understanding it does not become like #9603. I've no desire to spend so much time on endless small changes. 

The only changes I would make to `patches/Makefile` are Solaris-specific, as the compiler flags are wrong. (Oh, and I might add the necessary change to package so it builds on HP-UX, where shared libraries are .sl and not .so.) But I have no intension of re-writing the whole of the Makefile. 

There's a lot of unnecessary things in `spkg-install` and I'm happy to remove them, but I'm not willing to spend weeks on it. 

Dave


---

Comment by drkirkby created at 2010-09-07 22:48:04

See: 
 * #9871 which updates Cliquer and runs the tests in a better way. 
 * #9870 which will clean up Cliquer. 

Dave


---

Comment by jdemeyer created at 2014-01-16 13:32:32

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-01-16 13:32:32

Duplicate of #9870.


---

Comment by jdemeyer created at 2014-01-16 13:32:37

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-21 14:28:44

Resolution: duplicate
