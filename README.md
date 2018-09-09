# LogPy Logger - the versatile Python Logger

This module offers universal logging solution for software development, taking into considerations things such as logfile title, managing existing logfiles, changing working directories, 4 log types, adjustable timestamp and log with pre- and postfixes.

It is also supplied with multithreading opportunity, using Events and Exception handling.

## Usage
To use the LogPy, clone the repository into your directory using Git:

```console
$ git clone https://github.com/PiotrJZielinski/LogPy
```

You can then (assuming you put LogPy module in your working directory) import it into your project using:

```python
from LogPy.LogPy import Logger
```

The class is initialized with parameters:

```python
Logger(filename='main', directory='', logtype='info', timestamp='%Y-%m-%d | %H:%M:%S.%f', logformat='[{timestamp}] {logtype}:   {message}', prefix='', postfix='', title='Main Logger', logexists='append', console=False):
```

where 
* *filename* is the name of the file in which you intend to put the log in;
* *directory* is the directory in which you want to put the file; leaving it default puts the file in your working directory;
* *logtype* is the default log message to use (one of: *info*, *warning*, *error*, *fatal*);
* *timestamp* is the string used for defining (see datetime.strftime() for timestamp formatting details);
* *logformat* is the log configuration (string containing variables: *timestamp*, *logtype*, *message*, *prefix*, *postfix*)
* *prefix*
* *postfix*
* *title* is the string to be put on the top of the logfile
* *logexists* is the default action to be performed in case logfile already exists (*append*, *overwrite* or *rename*)
* *console* is a boolean specifying whether the logger should print messages in the console