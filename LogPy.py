import datetime
import os


class LogPy:
    """Main class for versatile Python Logger

    read documentation for usage instructions"""

    def __init__(self, filename='main.log', directory='', def_logtype='info', timestamp='%Y-%m-%d | %H:%M:%S.%f',
                 logformat='[{timestamp}] {logtype}: {message}', prefix='', postfix=''):
        """Initialization method

        This will create logger object, prepare logfile and initialize log format
        :param filename: file to save log in
        :param directory: directory where logfile is located
        :param def_logtype: default log type; available: 'info', 'warning', 'error', 'fatal'
        :param timestamp: string used for defining (see datetime.strftime() for timestamp formatting details)
        :param logformat: log configuration; available elements: 'timestamp', 'logtype', 'message', 'prefix', 'postfix'
        """

        # create logfile and its directory
        self.filename = filename
        self.directory = directory
        self.resume()
        # available log methods:
        self._logmethods = {'info': self.info, 'warning': self.warning, 'error': self.error, 'fatal': self.fatal}
        assert def_logtype in self._logmethods.keys()
        self._logdef = self._logmethods[def_logtype]
        # timestamp format
        assert isinstance(timestamp, str)
        self._timestamp = timestamp
        # message format
        assert isinstance(logformat, str)
        self._logformat = logformat
        # prefix & postfix
        assert isinstance(prefix, str)
        assert isinstance(postfix, str)
        self._prefix = prefix
        self._postfix = postfix
        # boolean for running logger
        self._enabled = True

    def pause(self):
        if self._enabled:
            self._enabled = False

    def resume(self):
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





    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

    def fatal(self, msg):
        pass

