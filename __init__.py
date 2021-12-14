class EventDoesNotExist(Exception):
    pass

class Events:
    def __init__(self, allow_nonexistent_events=True, allow_emitting_nonexistent_events=True):
        self.allow_ne_ev: bool = allow_nonexistent_events
        self.allow_em_ne_ev: bool = allow_emitting_nonexistent_events
        self.eventMap: dict[str, list[function]] = {}

    def add_events(self, eventList):
        for event in eventList:
            self.eventMap[event] = []
            
    def on(self, event: str):
        def decorator(func):
            if event in self.eventMap:
                self.eventMap[event].append(func)
            elif event not in self.eventMap and self.allow_ne_ev:
                self.eventMap[event] = [func]
            else:
                raise EventDoesNotExist(f"Event '{event}' does not exist and cannot have event handlers attached.")
            
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)

            return wrapper

        return decorator
    
    def emit(self, event: str, *args, **kwargs):
        if event in self.eventMap:
            for func in self.eventMap[event]:
                func(*args, **kwargs)
        elif event not in self.eventMap and not self.allow_em_ne_ev:
            raise EventDoesNotExist(f"Event {event} does not existent and cannot be emitted. Please add events with add_events().")
    
