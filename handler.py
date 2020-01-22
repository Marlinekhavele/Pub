class HandlerService(object):
    name = "handler_service"

    @events_handler("emitter_service", "some_event")
    def handler(self, payload):
        print("%s : %s" % (self.name, payload))
