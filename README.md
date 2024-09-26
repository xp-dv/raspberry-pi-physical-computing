# raspberry-pi-physical-computing
Repository of lab projects demonstrating the basics of physical computing on the Raspberry Pi 5 Platform. Topics covered include basic GPIO, LEDs, distance sensors, motor controllers, camera module, etc.

### Troubleshooting
* If running a program produces the "GPIO busy" error, it is likely that you tried running a new program without terminating the currently running program. One way to terminate the program is the find the python3 process using `pgrep -a python3`, then kill it using `kill <Process ID>`
