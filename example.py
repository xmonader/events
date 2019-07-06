import events


class Event:
    def __init__(self):
        pass

class UserHungryEvent:
    def __init__(self, name):
        self.name = name

    def msg(self):
        return f"{self.name} is hungry."


class UserThirstyEvent:
    def __init__(self, name):
        self.name = name

    def msg(self):
        return f"{self.name} is thirsty."


@events.handle(UserHungryEvent)
def handle_hungry(ev):
    m = ev.msg()
    print(f"handling event with msg: {m}")


@events.handle(UserThirstyEvent)
def handle_thirsty(ev):
    m = ev.msg()
    print(f"handling thirst with water :d ev with msg: {m}")



@events.handleany
def events_hunger_thirst_logger(ev):
    m = ev.msg()
    print(f"logging from any{m}")


ev1 = UserHungryEvent('ahmed')
ev2 = UserThirstyEvent('dmdm')

events.notify(ev1)
events.notify(ev2)
