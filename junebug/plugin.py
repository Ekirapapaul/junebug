class JunebugPlugin(object):
    '''Base class for all Junebug plugins'''

    def start_plugin(self, config):
        '''
        Can be overridden with any required startup code for the plugin.
        Can return a deferred.

        :param config: The config that Junebug was started with.
        :type config: :class:`JunebugConfig`
        '''
        pass

    def channel_started(self, channel):
        '''
        Called whenever a channel is started. Should be implemented by the
        plugin. Can return a deferred.

        :param channel: The channel that has been started.
        :type channel: :class:`Channel`
        '''
        pass

    def channel_stopped(self, channel):
        '''
        Called whenever a channel is stopped. Should be implemented by the
        plugin. Can return a deferred.

        :param channel: The channel that has been stopped.
        :type channel: :class:`Channel`
        '''
        pass
