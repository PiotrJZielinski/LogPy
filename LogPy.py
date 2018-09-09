import datetime
import os


class LogPy:
    """Main class for versatile Python Logger

    read documentation for usage instructions"""

    def __init__(self, filename='main.log', directory='', logtype='info', timestamp='%Y-%m-%d | %H:%M:%S.%f',
                 logformat='[{timestamp}] {logtype}: {message}', prefix='', postfix=''):
        """Initialization method

        his will create logger object, prepare logfile and initialize log format
        :param filename: file to save log in
        :param directory: directory where logfile is located; defaults to current directory
        :param logtype: default log type; available: 'info', 'warning', 'error', 'fatal'
        :param timestamp: string used for defining (see datetime.strftime() for timestamp formatting details)
        :param logformat: log configuration; available elements: 'timestamp', 'logtype', 'message', 'prefix', 'postfix'
        :param prefix: string to prepend in the log
        :param postfix: string to append to the log
        """

        # boolean for running logger
        self._enabled = False
        # create logfile and its directory
        self.filename = filename
        self.directory = directory
        # available log methods:
        self._logtypes = {'info': self.info, 'warning': self.warning, 'error': self.error, 'fatal': self.fatal}
        self.logtype = logtype
        # timestamp format
        self.timestamp = timestamp
        # message format
        self.logformat = logformat
        # prefix & postfix
        self.prefix = prefix
        self.postfix = postfix
        # resume logger
        self.resume()

    def pause(self):
        """Pause the logger

        this will set boolean attribute to False, which will stop saving log to the logfile"""
        if self._enabled:
            self._enabled = False

    def resume(self):
        """Resume logging

        this will set boolean attribute to True, which will resume logging to the logfile"""
        if not self._enabled:
            if not os.path.exists(self._directory):
                print('WARNING: directory does not exist. Creating directory {dir}'.format(dir=self.directory))
                os.makedirs(self._directory)
            self._path = '{dir}/{filename}'.format(dir=self._directory, filename=self.filename)
            open(self._path, 'a').close()
            self._enabled = True

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, value):
        self.pause()
        assert isinstance(value, str)
        self._directory = value

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self.pause()
        assert isinstance(value, str)
        self._filename = value

    @property
    def logtype(self):
        return list([key for key, ltype in self._logtypes.items() if ltype is self._logtype])

    @logtype.setter
    def logtype(self, value):
        assert value in self._logtypes.keys()
        self._logtype = self._logtypes[value]

    @property
    def timestamp(self):
        return datetime.datetime.now().strftime(self._timestamp)

    @timestamp.setter
    def timestamp(self, value):
        assert isinstance(value, str)
        self._timestamp = value

    @property
    def logformat(self):
        return self._logformat.format(timestamp=self.timestamp, logtype=self.logtype, message='logformat test',
                                      prefix=self.prefix, postfix=self.postfix)

    @logformat.setter
    def logformat(self, value):
        assert isinstance(value, str)
        self._logformat = value

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        assert isinstance(value, str)
        self._prefix = value

    @property
    def postfix(self):
        return self._postfix

    @postfix.setter
    def postfix(self, value):
        assert isinstance(value, str)
        self._postfix = value

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

    def fatal(self, msg):
        pass
