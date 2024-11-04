# raspberry-pi-physical-computing
Repository of lab projects demonstrating the basics of physical computing on the Raspberry Pi 5 Platform. Topics covered include basic GPIO, LEDs, distance sensors, motor controllers, camera module, etc.

### Package Installation
1. Make sure you have Python installed with the *pip* and *venv* packages installed.
2. Navigate to the [root](./) folder of this repository.
3. Inside this repository, create a local python virtual environment. `python -m venv ./venv`
4. Activate the virtual environment. `source ./activate`
5. Install the required packages listed in [requirements.txt](./requirements.txt). `pip install -r ./requirements.txt`

### Troubleshooting
* If running a program produces the "GPIO busy" error, it is likely that you tried running a new program without terminating the currently running program. One way to terminate the program is the find the python3 process using `pgrep -a python3`, then kill it using `kill <Process ID>`
