# 1. on macOS + in VS Code integrated terminal

1. Scenario 1.1

   take the following steps:

   - 2 instances of the integrated terminal

   - in instance 1, `$ python 08-example/print_numbers.py &> 08-example/log.txt < /dev/null & echo $! > 08-example/pid.txt`

   - in instance 2, `$ top -pid $(cat 08-example/pid.txt)`

   - in instance 1, issue `$ exit`

   the last step "stops/closes" instance 1

   the remaining instance indicates that the process with the PID stored in `08-example/pid.txt` continues executing; that process completes successfully without any errors, producing a `08-example/log.txt` file with the numbers from 0 to 59

2. Scenario 1.2

   take the following steps:

   - ...

   - ...

   - ...

   - in instance 1, click the "Kill Terminal" button in VS Code's GUI

   the last step "stops/closes" instance 1

   the remaining instance indicates that the process with the PID stored in `08-example/pid.txt` has halted executing; that process has produced a `08-example/log.txt` file without any content (an empty file)

3. Scenario 1.3

   take the following steps:

   - ...

   - ...

   - ...

   - in instance 1, issue `$ kill $(echo $$)`

   the last step does not "stop/close" instance 1

   the result is analogous to that in Scenario 1.1 - namely: instance 2 indicates that the process with the PID stored in `08-example/pid.txt` continues executing; that process completes successfully without any errors, producing a `08-example/log.txt` file with the numbers from 0 to 59

4. Scenario 1.4

   take the following steps:

   - ...

   - ...

   - ...

   - in instance 1, issue `$ kill -KILL $(echo $$)`

   the last step "stops/closes" instance 1

   the result is analogous to that in Scenario 1.1 - namely: ...

# 2. on macOS + the macOS Terminal application

1. Scenario 2.1

   take the following steps:

   - 2 instances of the terminal

   - in instance 1, `$ python 08-example/print_numbers.py &> 08-example/log.txt < /dev/null & echo $! > 08-example/pid.txt`

   - in instance 2, `$ top -pid $(cat 08-example/pid.txt)`

   - in instance 1, issue `$ exit`

   the last step outputs

   ```
   logout
   Saving session...
   ...copying shared history...
   ...saving history...truncating history files...
   ...completed.

   [Process completed]
   ```

   indicating that the command, at least in some sense, "stops/closes" instance 1

   the remaining instance indicates that the process with the PID stored in `08-example/pid.txt` continues executing; that process completes successfully without any errors, producing a `08-example/log.txt` file with the numbers from 0 to 59

2. Scenario 2.2

   take the following steps:

   - ...

   - ...

   - ...

   - in instance 1, click the "Close" button in Terminal application window's GUI

   the last step "stops/closes" instance 1

   the remaining instance indicates that the process with the PID stored in `08-example/pid.txt` has halted executing; that process has produced a `08-example/log.txt` file without any content (an empty file)

3. Scenario 2.3

   take the following steps:

   - ...

   - ...

   - ...

   - in instance 1, issue `$ kill $(echo $$)`

   the last step does not "stop/close" instance 1

   the result is analogous to that in Scenario 2.1 - namely: instance 2 indicates that the process with the PID stored in `08-example/pid.txt` continues executing; that process completes successfully without any errors, producing a `08-example/log.txt` file with the numbers from 0 to 59

4. Scenario 2.4

   take the following steps:

   - ...

   - ...

   - ...

   - in instance 1, issue `$ kill -KILL $(echo $$)`

   the last step outputs

   ```

   [Process completed]
   ```

   indicating that the command, at least in some sense, "stops/closes" instance 1

   the result is analogous to that in Scenario 2.1 - namely: ...

# 3. "`nohup` incarnations" of (1. on macOS + in VS Code integrated terminal)

1. Scenario 3.1

   take the following steps:

   - [the corresponding step from Scenario 1.1]

   - in instance 1, `$ nohup python 08-example/print_numbers.py &> 08-example/log.txt < /dev/null & echo $! > 08-example/pid.txt`

   - [the corresponding step from Scenario 1.1]

   - [the corresponding step from Scenario 1.1]

   [the same as the corresponding observation in Scenario 1.1]

2. Scenario 3.2

   take the following steps:

   - [the corresponding step from Scenario 1.2]

   - ...

   - [the corresponding step from Scenario 1.2]

   - [the corresponding step from Scenario 1.2]

   [different from the corresponding observation in Scenario 1.2, the same as the corresponding observation in Scenario 1.1]

3. Scenario 3.3

   Choose not to try this out as "`nohup` incarnation" of Scenario 1.3, because that scenario does not "stop/close" instance 1.

4. Scenario 3.4

   take the following steps:

   - [the corresponding step from Scenario 1.4]

   - ...

   - [the corresponding step from Scenario 1.4]

   - [the corresponding step from Scenario 1.4] in instance 1, issue `$ kill -KILL $(echo $$)`, which "stops/closes" instance 1

   [the same as the corresponding observation in Scenario 1.4]

# 4. "`nohup` incarnations" of (2. on macOS + the macOS Terminal application)

1. Scenario 4.1

   take the following steps:

   - [the corresponding step from Scenario 2.1]

   - in instance 1, `$ nohup python 08-example/print_numbers.py &> 08-example/log.txt < /dev/null & echo $! > 08-example/pid.txt`

   - [the corresponding step from Scenario 2.1]

   - [the corresponding step from Scenario 2.1]

   [the same as the corresponding observation in Scenario 2.1]

2. Scenario 4.2

   take the following steps:

   - [the corresponding step from Scenario 2.2]

   - ...

   - [the corresponding step from Scenario 2.2]

   - [the corresponding step from Scenario 2.2]

   [different from the corresponding observation in Scenario 2.2, the same as the corresponding observation in Scenario 2.1]

3. Scenario 4.3

   Choose not to try this out as "`nohup` incarnation" of Scenario 2.3, because that scenario does not "stop/close" instance 1.

4. Scenario 4.4

   take the following steps:

   - [the corresponding step from Scenario 2.4]

   - ...

   - [the corresponding step from Scenario 2.4]

   - [the corresponding step from Scenario 2.4]

   [the same as the corresponding observation in Scenario 2.4]

# 5. (`CTRL + Z`) + `bg`

```
shell 1                                   shell 2
-------                                   -------
$ python 14-example/run_a_long_time.py

CTRL + Z

[1]+  Stopped                 python 14-example/run_a_long_time.py

$ jobs -l
[1]+  9786 Stopped                 python 14-example/run_a_long_time.py

                                          $ pstree -asp 9786
                                          systemd,1 splash
                                          └─systemd,5954 --user
                                                └─gnome-terminal-,6610
                                                   └─bash,12392
                                                      └─python,9786 14-example/run_a_long_time.py

                                          $ sudo strace -e trace=signal -p 9786
                                          [sudo] password for kaloyanmarinov:
                                          strace: Process 9786 attached
                                          --- stopped by SIGTSTP ---
                                          _

$ bg
[1]+ python 14-example/run_a_long_time.py &

                                          --- SIGCONT {si_signo=SIGCONT, si_code=SI_USER, si_pid=12392, si_uid=1000} ---

$ jobs -l
[1]+  9786 Running                 python 14-example/run_a_long_time.py &

$ exit

                                          rt_sigaction(SIGINT, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fc8a6fdc040}, {sa_handler=0x564d37d2d490, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fc8a6fdc040}, 8) = 0
                                          +++ exited with 0 +++

SUCCESS: AFTER 1 MINUTE HAS PASSED,
         A 14-example/output.txt FILE WITH THE EXPECTED CONTENTS IS CREATED.
```

```
shell 1                                   shell 2
-------                                   -------
$ python 14-example/run_a_long_time.py

CTRL + Z

[1]+  Stopped                 python 14-example/run_a_long_time.py

jobs -l

[1]+ 10717 Stopped                 python 14-example/run_a_long_time.py

                                          $ pstree -asp 10717
                                          systemd,1 splash
                                          └─systemd,5954 --user
                                                └─gnome-terminal-,6610
                                                   └─bash,10528
                                                      └─python,10717 14-example/run_a_long_time.py

                                          $ sudo strace -e trace=signal -p 10717
                                          [sudo] password for kaloyanmarinov:
                                          strace: Process 10717 attached
                                          --- stopped by SIGTSTP ---
                                          _

$ bg
[1]+ python 14-example/run_a_long_time.py &

                                          --- SIGCONT {si_signo=SIGCONT, si_code=SI_USER, si_pid=10528, si_uid=1000} ---

$ jobs -l
[1]+  10717 Running                 python 14-example/run_a_long_time.py &

CTRL + D

                                          rt_sigaction(SIGINT, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7f382dd53040}, {sa_handler=0x5627cde93490, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7f382dd53040}, 8) = 0
                                          +++ exited with 0 +++

SUCCESS: AFTER 1 MINUTE HAS PASSED,
         A 14-example/output.txt FILE WITH THE EXPECTED CONTENTS IS CREATED.
```

```
shell 1                                   shell 2
-------                                   -------
$ python 14-example/run_a_long_time.py

CTRL + Z

[1]+  Stopped                 python 14-example/run_a_long_time.py

jobs -l

[1]+ 11159 Stopped                 python 14-example/run_a_long_time.py

                                          $ pstree -asp 11159
                                          systemd,1 splash
                                          └─systemd,5954 --user
                                                └─gnome-terminal-,6610
                                                   └─bash,11078
                                                      └─python,11159 14-example/run_a_long_time.py

                                          $ sudo strace -e trace=signal -p 11159
                                          strace: Process 11159 attached
                                          --- stopped by SIGTSTP ---
                                          _

$ bg
[1]+ python 14-example/run_a_long_time.py &

                                          --- SIGCONT {si_signo=SIGCONT, si_code=SI_USER, si_pid=11078, si_uid=1000} ---

$ jobs -l
[1]+  11159 Running                 python 14-example/run_a_long_time.py &

$ kill -HUP $$
                                          --- SIGHUP {si_signo=SIGHUP, si_code=SI_USER, si_pid=11078, si_uid=1000} ---
                                          +++ killed by SIGHUP +++

FAILURE: AS SOON AS THE LAST COMMAND IS ISSUED,
         THE PROCESS IS DESTROYED
         (AND IS NO LONGER VISIBLE VIA `top -p <pid>` OR `htop -p <pid>` in a "shell 3")

         THIS IS A FAILURE BECAUSE, EVEN THOUGH A 14-example/output.txt FILE IS CREATED,
         IT IS AN EMTPY FILE AND THUS LACKS THE EXPECTED CONTENTS.
```

```
shell 1                                   shell 2
-------                                   -------
$ python 14-example/run_a_long_time.py

CTRL + Z

[1]+  Stopped                 python 14-example/run_a_long_time.py

jobs -l

[1]+ 11557 Stopped                 python 14-example/run_a_long_time.py

                                          $ pstree -asp 11557
                                          systemd,1 splash
                                          └─systemd,5954 --user
                                                └─gnome-terminal-,6610
                                                   └─bash,11547
                                                      └─python,11557 14-example/run_a_long_time.py

                                          $ sudo strace -e trace=signal -p 11557
                                          strace: Process 11557 attached
                                          --- stopped by SIGTSTP ---
                                          _

$ bg
[1]+ python 14-example/run_a_long_time.py &

                                          --- SIGCONT {si_signo=SIGCONT, si_code=SI_USER, si_pid=11547, si_uid=1000} ---

$ jobs -l
[1]+ 11557 Running                 python 14-example/run_a_long_time.py &

close the window
                                          --- SIGHUP {si_signo=SIGHUP, si_code=SI_USER, si_pid=11547, si_uid=1000} ---
                                          +++ killed by SIGHUP +++

FAILURE: AS SOON AS THE LAST COMMAND IS ISSUED,
         THE PROCESS IS DESTROYED
         (AND IS NO LONGER VISIBLE VIA `top -p <pid>` OR `htop -p <pid>` in a "shell 3")

         THIS IS A FAILURE BECAUSE, EVEN THOUGH A 14-example/output.txt FILE IS CREATED,
         IT IS AN EMTPY FILE AND THUS LACKS THE EXPECTED CONTENTS.
```

6. `&`

```
shell 1                                   shell 2
-------                                   -------
$ python 14-example/run_a_long_time.py &
[1] 14537

                                          $ pstree -asp 14537
                                          systemd,1 splash
                                          └─systemd,5954 --user
                                                └─gnome-terminal-,6610
                                                   └─bash,14475
                                                      └─python,14537 14-example/run_a_long_time.py

                                          $ sudo strace -e trace=signal -p 14537
                                          strace: Process 14537 attached

$ exit

                                          rt_sigaction(SIGINT, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fd3ccca5040}, {sa_handler=0x5590eebe9490, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fd3ccca5040}, 8) = 0
                                          +++ exited with 0 +++

SUCCESS: AFTER 1 MINUTE HAS PASSED,
         A 14-example/output.txt FILE WITH THE EXPECTED CONTENTS IS CREATED.
```

```
shell 1                                   shell 2
-------                                   -------
$ python 14-example/run_a_long_time.py &
[1] 14830

                                          $ pstree -asp 14830
                                          systemd,1 splash
                                          └─systemd,5954 --user
                                                └─gnome-terminal-,6610
                                                   └─bash,14819
                                                      └─python,14830 14-example/run_a_long_time.py

                                          $ sudo strace -e trace=signal -p 14830
                                          strace: Process 14830 attached

CTRL + D

                                          rt_sigaction(SIGINT, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fb505c30040}, {sa_handler=0x55dd83eb9490, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fb505c30040}, 8) = 0
                                          +++ exited with 0 +++

SUCCESS: AFTER 1 MINUTE HAS PASSED,
         A 14-example/output.txt FILE WITH THE EXPECTED CONTENTS IS CREATED.
```

```
shell 1                                   shell 2
-------                                   -------
$ python 14-example/run_a_long_time.py &
[1] 15342

                                          $ pstree -asp 15342
                                          systemd,1 splash
                                          └─systemd,5954 --user
                                                └─gnome-terminal-,6610
                                                   └─bash,15329
                                                      └─python,15342 14-example/run_a_long_time.py

                                          $ sudo strace -e trace=signal -p 15342
                                          strace: Process 15342 attached

kill -HUP $$

                                          --- SIGHUP {si_signo=SIGHUP, si_code=SI_USER, si_pid=15329, si_uid=1000} ---
                                          +++ killed by SIGHUP +++

FAILURE: AS SOON AS THE LAST COMMAND IS ISSUED,
         THE PROCESS IS DESTROYED
         (AND IS NO LONGER VISIBLE VIA `top -p <pid>` OR `htop -p <pid>` in a "shell 3")

         THIS IS A FAILURE BECAUSE, EVEN THOUGH A 14-example/output.txt FILE IS CREATED,
         IT IS AN EMTPY FILE AND THUS LACKS THE EXPECTED CONTENTS.
```
