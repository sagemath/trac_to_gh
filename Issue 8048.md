# Issue 8048: command to gather build report on a platform/hardware combination

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-01-24 02:16:43

Assignee: tbd

CC:  saliola jasonbhill

From [sage-release](http://groups.google.com/group/sage-release/msg/cf028395e198f4cf):

```
>> I'm not saying that this wiki page is not a useful resource, but I don't
>> have the time or patience to go through this at each release.

> I'm too am frustrated by the wiki at times. Sometimes it won't allow
> me to save edits containing some strings, because it deemed those
> strings to be a sign of spam content or something. I would then spend
> minutes figuring out how to get the wiki to accept the edits or
> rewrite my edits.

> Anyway, if you want, you could send information according to the
> template below to sage-release and I'd update the wiki with the
> information you supply.

> OS version:
> Machine name:
> Architecture:
> 32/64 bit:
> RAM:
> Compiler:
> Build:
> Doctest:

Maybe you should add a command to sage, e.g.,

  sage: _build_report()

or

  sage -buildreport

that runs a script, gathers relevant information, then submits it
somewhere.  The resulting submission could then be summarized on a web
page.   This is a perfect example of where it would be far, far better
to spend time writing some code than doing something manually.

William
```



---

Attachment

half-baked solution; based on Sage 4.3.2.rc0; don't use


---

Comment by mvngu created at 2010-03-02 02:28:07

I have attached a half-baked patch, which is not ready for review. I leave it here so I, or anyone, can work on it later on.


---

Comment by drkirkby created at 2010-06-25 15:44:27

Mathematica actually provides one called 

```
  SystemInformation[]
```

http://reference.wolfram.com/mathematica/ref/SystemInformation.html

http://reference.wolfram.com/mathematica/guide/SystemInformation.html

It also provides information on the machine precision. A look at what they provide might be useful.

I would suggest we also include the value of exp(1.0), as that is system dependent, though care needs to be used in computing that so compilers don't inline the result. 

Some possible sources of information would be:

 == Solaris ==

 * $ /usr/sbin/prtconf | grep Memory (gives you memory information)
 * $ /usr/platform/`uname -i`/sbin/prtdiag (More hardware information)
 * $ showrev (more information)
 * $ /usr/sbin/psrinfo -v (gives you processor information)
 * $ prstat (like top, but more accurate on Solaris)
 * $ cat /etc/release (gives operating system information)
 * $ uname -a (gives you the usual things)
 * $ uptime (how long the system has been up, and load average)
 * $ dmesg (system messages)
 * $ df -h (gives you some information about disk usage)
 
The best way to find out if a Solaris system is running out of memory is to use the scan rate ('sr' column) of 'vmstat'. (Don't even think about believing top)

 == Linux ==

 * $ uname -a
 * $ cat /etc/issue
 * $ cat /proc/cpuinfo
 * $ cat /proc/meminfo

 == OS X ==
 * $ uname -a
 * $ /usr/sbin/system_profiler


---

Comment by jasonbhill created at 2010-06-30 18:16:30

I will take this and try to write it for linux and sunos. It should
1) Be capable of being called from within Sage after installation.
2) Be capable of being called from command line outside Sage assuming an installation failure. (Assuming python exists.)
3) Be capable of returning precision,etc information from within Sage.
4) Be scalable to a new OS.
 

Stay tuned.


---

Attachment

shell script to determine *somewhat verbose* environment and hardware info, Linux only currently


---

Comment by jasonbhill created at 2010-07-16 04:42:08

Notes on hrdwr-info.sh as of July 15:

 * only writes to the screen, not to a file yet
 * is bash instead of python
 * only checks Linux right now. (The other OSs are easier, IMO, but I mainly have access to Linux and some Solaris machines. I'll do Solaris next.)

There are several things to consider: * Pruning info from /etc is not safe. It is not standardized, subject to user modifications, subject to lack of updates between distros (Ubuntu -> Mint etc). But, when the info exists it can be useful. It can also be badly formatted... with \r and \n explicit in the file. I used some 'sed' commands to get around this a bit.

 * Pruning from /proc is fine, since the data is standardized and updated by the OS. The only problem I have had in testing here is with virtual machines where the CPU is a virtual processor. But, the output in that case makes the situation obvious.
 * Getting your hands on the 32/64-bit declaration is tricky, since you'd like to use uname to do it. We can do that, but this ONLY returns information about the OS and not the hardware capabilities. I suppose that is fine, since we're testing installs and we only really care what bitlength the OS is capable of. But, many of the servers I've tested on are running 32-bit Linux distros on 64-bit capable hardware... and so I listed the OS and hardware bitlengths separately. I'm just curious if this will ever cause issues.

Questions I have: * Can you test it, break it?

 * What looks useful? What doesn't? What looks left out? Why?
 * How would something like this be used? I'm under the impression that this can get written to a log and the user can paste that log... where?

I'll post a link with sample output since it isn't formatting nicely in this forum wysiwyg editor.


---

Comment by jasonbhill created at 2010-07-16 04:50:51

example outputs


---

Attachment

I had a look at this and have a few comments. 
 * Overall, I was very impressed. It has nice output. 
 * I believe it should be released under "GPL 2, or at your option, any later version". 
 * It would be useful to know if CPU throttling is enabled or not. This can cause problems building ATLAS for example. 
 * I would see if `pwd`/local/bin/sage-banner exists, and if so grab the sage version from there.
 * I would show the full output of gcc -v, rather than just part of it. 
 * It would be useful to know if there is a server listening on port 8000 (default for Sage). I don't know how to do that though - I could find out on Solaris no doubt. 
 * I would show the output of the following three commands:

```
drkirkby`@`hawk:~$ command -v gcc
/usr/local/gcc-4.4.4-multilib/bin/gcc
drkirkby`@`hawk:~$ command -v g++
/usr/local/gcc-4.4.4-multilib/bin/g++
drkirkby`@`hawk:~$ command -v gfortran
/usr/local/gcc-4.4.4-multilib/bin/gfortran
```


 ('command -v' is portable - the use of 'which' is not). This will allow us to see if the compilers are a mix of compilers from places like `/usr/bin` and `/usr/local/bin`. 
 * I don't know if you are aware of the [Useless Use of Cat Award](http://partmaps.org/era/unix/award.html) - well worth reading, as it is both educational and funny. Several of your commands use `cat` when it is not necessary. Both `sed` and `awk` can read from a file, so there is no need to `cat` the file and pipe it to these programs - it just creates another process, which slows things down. It's obviously not significant on small files, but it is on larger ones. It does make the code longer too. 
 {{{
HW_RELEASE=$(cat /etc/lsb-release | sed -e "s/DISTRIB_/ /g" | tr -d '\r\n' | sed -e "s/^ //g" 2> /dev/null)
 }}}
 could be changed to:
 {{{
HW_RELEASE=$(sed "s/DISTRIB_/ /g" /etc/lsb-release | tr -d '\r\n' | sed "s/^ //g" 2> /dev/null)
 }}}
 (There is no need for the -e option to `sed` if there is only one command like here).  One could even combine the `sed` into one, but that gets more complex to write. Likewise
 {{{
HW_CPU_NUM=$(cat /proc/cpuinfo | grep "physical id" | uniq | grep -c "physical id")
 }}}
 Could be changed to:
 {{{
 HW_CPU_NUM=$(grep "physical id" /proc/cpuinfo | uniq | grep -c "physical id")
 }}}
 by simply removing the unnecessary `cat`. Unless you are guaranteed the output of the first grep command is in sorted order, you should pipe to `sort` before `uniq`, as `uniq` only looks at adjacent lines. See below, where the word _hello_ is in the file twice, but uniq does not indicate this:
 {{{
drkirkby`@`hawk:~$ cat test
hello
fred
hello
jim
drkirkby`@`hawk:~$ uniq test
hello
fred
hello
jim
drkirkby`@`hawk:~$ sort test | uniq
fred
hello
jim
 }}}
 * Given the number of different linux systems, I wonder if it might not be better to simply print the contents of `/etc/lsb-release`, `/etc/release` or whatever else exists, rather than try to parse them to get a distribution from them. It might be safer. 
 * The comment on line 148 (`# function to return memory info for linux`) is wrong. 
 * Although it would take 1 second to run, I think the output of:
 {{{
  vmstat 1 2
 }}}
 could be useful, as it allows one to see more what is happening on a system at the point of failure. 

Overall, this looks very useful. I was quite impressed with it.


---

Comment by jhpalmieri created at 2010-07-23 21:28:59

I used this on a bunch of machines earlier today to help produce the page [http://wiki.sagemath.org/skynet](http://wiki.sagemath.org/skynet).  Very nice.  I don't know how useful the username, pwd, and shell lines are, but they don't hurt.  On two machines, both with processors described by `arch` as "ia64" (is that itanium?), there is no line "model name" in /proc/cpuinfo, so the corresponding line in the summary printed by the script ends up blank.  Otherwise, it seems to work well on all of the linux machines I tried.

On Mac OS X, I think a lot of the relevant information can be extracted by running the command `sysctl -a`.  See [http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man8/sysctl.8.html](http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man8/sysctl.8.html) and [http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man3/sysctl.3.html](http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man3/sysctl.3.html).


---

Comment by jasonbhill created at 2010-07-23 23:41:11

jhpalmieri: Can you please send me (jason.b.hill`@`colorado.edu) the /proc/cpuinfo files for Cicero and Cleo? I have made some changes to the script via what David said above, but there are some things that I can improve if I know what those proc files look like, since there are a couple of cases when the script is catching errors and shouldn't be.

I'll respond more after making those changes and re-uploading the script.


---

Comment by jhpalmieri created at 2010-07-24 00:00:14

I've copied /proc/cpuinfo for cicero, cleo, and iras to the files

 - [http://sage.math.washington.edu/home/palmieri/misc/cicero-cpu.txt](http://sage.math.washington.edu/home/palmieri/misc/cicero-cpu.txt)

 - [http://sage.math.washington.edu/home/palmieri/misc/cleo-cpu.txt](http://sage.math.washington.edu/home/palmieri/misc/cleo-cpu.txt)

 - [http://sage.math.washington.edu/home/palmieri/misc/iras-cpu.txt](http://sage.math.washington.edu/home/palmieri/misc/iras-cpu.txt)


---

Comment by jasonbhill created at 2010-07-24 02:36:38

How many physical processors do Iras and Cleo have? (My guess is 2.) Have you noticed that their "physical id" tags are very strange? The physical cpu labels are 0 and 3 instead of 0 and 1. I'm wondering if this is consistent with other Itaniums.


---

Comment by jhpalmieri created at 2010-07-24 02:55:04

How do I find out how many physical processors they have?  A comment on some random web page suggests that if two "processors" in /proc/cpuinfo have the same physical address, then they're the same processor.  How else do I tell?


---

Comment by drkirkby created at 2010-07-24 03:02:50

Replying to [comment:11 jhpalmieri]:
> How do I find out how many physical processors they have?  A comment on some random web page suggests that if two "processors" in /proc/cpuinfo have the same physical address, then they're the same processor.  How else do I tell?

On Solaris or OpenSolaris:


```
kirkby`@`t2:[~] $  /usr/sbin/psrinfo -p
2
```


but I don't know about any other operating system.


---

Comment by jasonbhill created at 2010-07-24 03:22:56

_Usually_ the following happens: If the system has 1 cpu, then no "physical id" will be present in /proc/cpuinfo. Otherwise, physical_id gives the slot number of the cpu/core/thread in question. The problem with Itaniums is that the original "topology" listed the first slot as -1 on the board, instead of 0. So, it may be that there is still a bug in translating the topology.

Try looking in
/sys/devices/system/cpu/cpu0/topology
/sys/devices/system/cpu/cpu1/topology
/sys/devices/system/cpu/cpu2/topology
...

and seeing how many different entries you can find. Those, if they exist, should correspond to board slots for cpus.


---

Comment by jhpalmieri created at 2010-07-24 04:51:50

Cleo has four different directories `/sys/devices/system/cpu/cpuN/topology/`, for N from 0 to 3.  The file `cpu0/topology/core_id` is the same as that for cpu2 (and the ones for cpu1 and cpu3 are equal to each other), while the file `cpu0/topology/physical_package_id` is the same as that for cpu1, different from that for cpu2 and cpu3.  Same situation for iras.


---

Comment by drkirkby created at 2010-07-24 20:53:27

It looks like on Solaris, 


```
kirkby`@`t2:[~] $ netstat -an | grep LISTEN | awk '{print $1}' | grep ^*.8000
kirkby`@`t2:[~] $ 
```


can be used to determine if there is something listening on port 8000, which would be useful to know for Sage. 

Sorry that don't help with the physical processors. To be honest, its not one of the most useful parameters though. I can't think of many Sage issues where the physical number of CPUs is going to be that important. 

[memconf](http://www.4schmidts.com/memconf.html) seems pretty clever on 't2,math'


```
# ./memconf
Gathering data for memconf. This may take over a minute. Please wait...
hostname: t2
Sun Microsystems, Inc. T5240 (2 X 8-Core 8-Thread UltraSPARC-T2+ 1167MHz)
Memory Interleave Factor: 8-way
socket MB/CMP0/BR0/CH0/D0 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP0/BR0/CH0/D1 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP0/BR0/CH1/D0 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP0/BR0/CH1/D1 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP0/BR1/CH0/D0 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP0/BR1/CH0/D1 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP0/BR1/CH1/D0 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP0/BR1/CH1/D1 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP1/BR0/CH0/D0 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP1/BR0/CH0/D1 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP1/BR0/CH1/D0 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP1/BR0/CH1/D1 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP1/BR1/CH0/D0 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP1/BR1/CH0/D1 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP1/BR1/CH1/D0 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
socket MB/CMP1/BR1/CH1/D1 has a Samsung 501-7953-01 Rev 05 2GB FB-DIMM
empty sockets: MB/CMP0/MR0/BR0/CH0/D2 MB/CMP0/MR0/BR0/CH0/D3 MB/CMP0/MR0/BR0/CH1/D2 MB/CMP0/MR0/BR0/CH1/D3 MB/CMP0/MR0/BR1/CH0/D2 MB/CMP0/MR0/BR1/CH0/D3 MB/CMP0/MR0/BR1/CH1/D2 MB/CMP0/MR0/BR1/CH1/D3 MB/CMP1/MR1/BR0/CH0/D2 MB/CMP1/MR1/BR0/CH0/D3 MB/CMP1/MR1/BR0/CH1/D2 MB/CMP1/MR1/BR0/CH1/D3 MB/CMP1/MR1/BR1/CH0/D2 MB/CMP1/MR1/BR1/CH0/D3 MB/CMP1/MR1/BR1/CH1/D2 MB/CMP1/MR1/BR1/CH1/D3
total memory = 32768MB (32GB)
```


knowing how many CPUs there are, how many cores they have and how many threads there are. 


Dave


---

Comment by drkirkby created at 2010-07-24 20:55:34

One thing that would be useful is the free disk space on whatever file system someone is building Sage on. Not sure the best way to find that out. Any ideas?

Dave


---

Attachment

I attached a new file. I made the 'useless cat' and other changes. (Thanks Dave!)

Some more notes:

 * cpu throttling: It is easy to determine if a cpu supports throttling, but can be a pain to determine (across various linux distributions) if it is enabled. Even from Ubuntu 9.10 to 10.04, this changed, and both are inconsistent with the Debian installations I've tried. So, I'm not incredibly optimistic here.
 * Getting the sage banner isn't a problem, so long as I know my pwd and how that relates to the banner's location. I haven't yet assumed that this script is executed anywhere specific.
 * I changed the gcc version command to output the entire output. The extra lines now included are only copyright info though, and so I'd question if we'd want them.
 * I'll add the netstat command (and/or equivalent).
 * diskspace is relatively easy. I'll add that as well.

It looks like the OS-X commands are somewhat straightforward, and the hardware is much more standardized there. Dave: We have a couple of lists of relevant Sunos commands... can we develop a single list of what is useful and what isn't? I have Open Solaris on a machine and so testing won't be an issue.

John:

 * You want to update some of the skynet information you posted before. The cpu information for at least one of the machines changed (since I thought 'uniq' would apply 'sort' and it doesn't... meaning that the cores/cpu-count is off).
 * I also added the correct greps to attempt to get information from those Itaniums. My best guess as to why those topology numbers are so strange is that those machines may actually accept 4 processors, but only have 2 plugged in. If that's not the case, then it's buggy and there just aren't enough people using those cpus to make it worth fixing.


---

Comment by drkirkby created at 2010-07-28 03:42:35

Replying to [comment:17 jasonbhill]:
> I attached a new file. I made the 'useless cat' and other changes. (Thanks Dave!)

You are welcome. 
 
> Some more notes:
> 
>  * cpu throttling: It is easy to determine if a cpu supports throttling, but can be a pain to determine (across various linux distributions) if it is enabled. Even from Ubuntu 9.10 to 10.04, this changed, and both are inconsistent with the Debian installations I've tried. So, I'm not incredibly optimistic here.

You do not surprise me. I came to the same conclusion on Solaris too. 

>  * Getting the sage banner isn't a problem, so long as I know my pwd and how that relates to the banner's location. I haven't yet assumed that this script is executed anywhere specific.
>  * I changed the gcc version command to output the entire output. The extra lines now included are only copyright info though, and so I'd question if we'd want them.

We should be able to get all the parameters that gcc was configured with


```
drkirkby`@`hawk:~$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: /export/home/drkirkby/gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4-multilib --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.4.4-multilib --with-mpfr=/usr/local/gcc-4.4.4-multilib --disable-nls --enable-checking=release --enable-werror=no --enable-multilib --with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld
Thread model: posix
gcc version 4.4.4 (GCC) 
```


that lot can be very useful to know. 

>  * I'll add the netstat command (and/or equivalent).

OK. 

>  * diskspace is relatively easy. I'll add that as well.

How do you propose to get the disk space? I came to the conclusion that was quite difficult, and have not found a way. 
 
> It looks like the OS-X commands are somewhat straightforward, and the hardware is much more standardized there. Dave: We have a couple of lists of relevant Sunos commands... can we develop a single list of what is useful and what isn't? I have Open Solaris on a machine and so testing won't be an issue.


Yes. It's late here. I will get onto that after some sleep. 

Dave 

> John:
> 
>  * You want to update some of the skynet information you posted before. The cpu information for at least one of the machines changed (since I thought 'uniq' would apply 'sort' and it doesn't... meaning that the cores/cpu-count is off).
>  * I also added the correct greps to attempt to get information from those Itaniums. My best guess as to why those topology numbers are so strange is that those machines may actually accept 4 processors, but only have 2 plugged in. 

It might be worth giving memconf a try, to see what it finds. I'm not suggesting including that, but it might confirm your guesses. 

If that's not the case, then it's buggy and there just aren't enough people using those cpus to make it worth fixing.


---

Comment by jhpalmieri created at 2010-07-28 18:43:02

Replying to [comment:18 drkirkby]:
> Replying to [comment:17 jasonbhill]:

> >  * You want to update some of the skynet information you posted before. 

Thanks, I've done that.

> It might be worth giving memconf a try, to see what it finds.

memconf doesn't seem to be installed on the skynet machines, or at least I haven't found it.


---

Comment by drkirkby created at 2010-07-28 20:40:00

Replying to [comment:19 jhpalmieri]:
> Replying to [comment:18 drkirkby]:
> > Replying to [comment:17 jasonbhill]:
> 
> > >  * You want to update some of the skynet information you posted before. 
> 
> Thanks, I've done that.
> 
> > It might be worth giving memconf a try, to see what it finds.
> 
> memconf doesn't seem to be installed on the skynet machines, or at least I haven't found it.

On some systems it runs as a normal user process. It can be downloaded in a few seconds, change the permission to make it executable and you are ready to go. It does not need compiling- its just a perl script. 

On 't2' it needs root access. I have no idea on other systems. I think it would work on mark without root access.
