# 1. on macOS + in VS Code integrated terminal

1. Scenario 1.1

   take the following steps:

      - 2 instances of the integrated terminal

      - in instance 1, `$ python 7-example/print_numbers.py &> 7-example/log.txt < /dev/null & echo $! > 7-example/pid.txt`

      - in instance 2, `$ top -pid $(cat 7-example/pid.txt)`

      - in instance 1, issue `$ exit`, which "stops/closes" instance 1

   the remaining instance indicates that the process with the PID stored in `7-example/pid.txt` continues executing; that process completes successfully without any errors, producing a `7-example/log.txt` file with the numbers from 0 to 59

2. Scenario 1.2

   take the following steps:

      - ...

      - ...

      - ...

      - in instance 1, click the "Kill Terminal" button in VS Code's GUI, which "stops/closes" instance 1

    the remaining instance indicates that the process with the PID stored in `7-example/pid.txt` has halted executing; that process has produced a `7-example/log.txt` file without any content (an empty file)

3. Scenario 1.3

    take the following steps:

      - ...

      - ...

      - ...

      - in instance 1, issue `$ kill $(echo $$)`, which does not "stop/close" instance 1
    
    the result is analogous to that in Scenario 1.1 - namely: instance 2 indicates that the process with the PID stored in `7-example/pid.txt` continues executing; that process completes successfully without any errors, producing a `7-example/log.txt` file with the numbers from 0 to 59

4. Scenario 1.4

    take the following steps:

      - ...

      - ...

      - ...

      - in instance 1, issue `$ kill -KILL $(echo $$)`, which "stops/closes" instance 1

      the result is analogous to that in Scenario 1.1 - namely: ...

# 2. on macOS + the macOS Terminal application

1. Scenario 2.1

   take the following steps:

      - 2 instances of the terminal

      - in instance 1, `$ python 7-example/print_numbers.py &> 7-example/log.txt < /dev/null & echo $! > 7-example/pid.txt`

      - in instance 2, `$ top -pid $(cat 7-example/pid.txt)`

      - in instance 1, issue `$ exit`, which outputs
         ```
         logout
         Saving session...
         ...copying shared history...
         ...saving history...truncating history files...
         ...completed.

         [Process completed]
         ```
         indicating that the command, at least in some sense, "stops/closes" instance 1

   the remaining instance indicates that the process with the PID stored in `7-example/pid.txt` continues executing; that process completes successfully without any errors, producing a `7-example/log.txt` file with the numbers from 0 to 59

2. Scenario 2.2

   take the following steps:

      - ...

      - ...

      - ...

      - in instance 1, click the "Close" button in Terminal application window's GUI, which "stops/closes" instance 1

    the remaining instance indicates that the process with the PID stored in `7-example/pid.txt` has halted executing; that process has produced a `7-example/log.txt` file without any content (an empty file)

3. Scenario 2.3

    take the following steps:

      - ...

      - ...

      - ...

      - in instance 1, issue `$ kill $(echo $$)`, which does not "stop/close" instance 1
    
    the result is analogous to that in Scenario 2.1 - namely: instance 2 indicates that the process with the PID stored in `7-example/pid.txt` continues executing; that process completes successfully without any errors, producing a `7-example/log.txt` file with the numbers from 0 to 59

4. Scenario 2.4

    take the following steps:

      - ...

      - ...

      - ...

      - in instance 1, issue `$ kill -KILL $(echo $$)`, which outputs
      ```

      [Process completed]
      ```
      indicating that the command, at least in some sense, "stops/closes" instance 1

      the result is analogous to that in Scenario 2.1 - namely: ...

# 3. "`nohup` incarnations" of (on macOS + in VS Code integrated terminal)

1. Scenario 3.1

   take the following steps:

      - [the corresponding step from Scenario 1.1]

      - in instance 1, `$ nohup python 7-example/print_numbers.py &> 7-example/log.txt < /dev/null & echo $! > 7-example/pid.txt`

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

      [different from the corresponding observation in Scenario 1.4, the same as the corresponding observation in Scenario 1.1]