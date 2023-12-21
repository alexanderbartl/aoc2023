import re

from aocd import data, submit

lines = data.split('\n')


class Signal:
    def __init__(self, sender, receivers, isHigh):
        self.sender = sender
        self.receivers = receivers
        self.isHigh = isHigh

    def __repr__(self):
        return f'{self.sender} -> {self.receivers} : {self.isHigh}'


class Module:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    def receive(self, signal):
        pass

    def register_input(self, name):
        pass


class FlipFlop(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.on = False

    def receive(self, signal):
        if not signal.isHigh:
            self.on = not self.on
            signals.append(Signal(self.name, self.outputs, self.on))


class Conjunction(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.inputs = {}

    def register_input(self, name):
        self.inputs[name] = False

    def receive(self, signal):
        self.inputs[signal.sender] = signal.isHigh
        if all(self.inputs.values()):
            signals.append(Signal(self.name, self.outputs, False))
        else:
            signals.append(Signal(self.name, self.outputs, True))


class Broadcaster(Module):
    def __init__(self, outputs):
        super().__init__('broadcaster', outputs)
        self.outputs = outputs

    def receive(self, signal):
        signals.append(Signal('broadcaster', self.outputs, signal.isHigh))


modules = {}
signals = []

for line in lines:
    identifier, outputs = line.split(' -> ')
    outputs = outputs.split(', ')
    if identifier.startswith('%'):
        modules[identifier[1:]] = FlipFlop(identifier[1:], outputs)
    elif identifier.startswith('&'):
        modules[identifier[1:]] = Conjunction(identifier[1:], outputs)
    elif identifier == 'broadcaster':
        modules[identifier] = Broadcaster(outputs)
    else:
        modules[identifier] = Module(identifier, outputs)

for m in modules.values():
    for o in m.outputs:
        if o in modules:
            modules[o].register_input(m.name)

idx = 0
for _ in range(1000):
    signals.append(Signal('button', ['broadcaster'], False))
    while idx < len(signals):
        s = signals[idx]
        for receiver in s.receivers:
            if receiver in modules:
                modules[receiver].receive(s)
        idx += 1

submit(sum(len(s.receivers) for s in signals if s.isHigh) * sum(len(s.receivers) for s in signals if not s.isHigh))
