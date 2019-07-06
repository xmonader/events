listeners = {
        '*': [],
}

def handlemany(eventclasses):
    def decorator(fun):
        for eventclass in eventclasses:
            eventcallbacks = listeners.setdefault(eventclass, [])
            eventcallbacks.append(fun)
            listeners[eventclass] = eventcallbacks
        def wrapper(*args, **kwargs):   
            fun(*args, **kwargs)
        return wrapper
    return decorator

# def registercb(eventclass, cb):
#     cbs = listeners.setdefault(eventclass, [])
#     cbs.append(cb)
#     listeners[eventclass] = cbs

def handleany(fun):
    listeners['*'].append(fun)
    def wrapper(*args, **kwargs):   
        fun(*args, **kwargs)
    return wrapper    

def handle(eventclass):
    def decorator(fun):
        eventcallbacks = listeners.setdefault(eventclass, [])
        eventcallbacks.append(fun)
        listeners[eventclass] = eventcallbacks
        def wrapper(*args, **kwargs):   
            print(args, kwargs)
            fun(*args, **kwargs)
        return wrapper
    return decorator


def notify(with_event):
    eventclass = with_event.__class__
    interested = listeners.get(eventclass, []) + listeners['*']
    for l in interested:
        l(with_event)



