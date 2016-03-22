# Windows Event Command Line Logger

Simple command line tool to log message to Windows Event Log

## Requirements

To run the single executable _wevlog.exe_ no python or additional modules are needed. To run the Python-Script, you need

* Python 2.7
* pypiwin32 (tested with 291)

To build the executable:

* py2exe-py2 (tested with 0.6.9)
* setuptools (testet with 19.5)

## Build

Execute _build.bat_. The portable executable _wevlog.exe_ located in _win32_.

## Run

```
wevlog.exe [INFO|ERROR|WARNING] (MESSAGE)

  INFO    Mark event as information (default)
  ERROR   Mark event as error
  WARNING Mark event as warning
  
  MESSAGE The message written to Event Log
```
