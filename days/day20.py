import sys

class Module:
    def __init__(self, name, module_type, dest):
        self.module_type = module_type

        self.signal = "low"
        self.input_signals = []
        self.outputs = []
        self.enabled = False
        self.name = name
        self.destinations = dest

    def module_trigger(self, signal):
        # input_ = self.signal
        if self.module_type in ["broadcaster", "button"]:
            self.signal = signal
        if self.module_type == "flipflop":
            if signal == "low":
                if not(self.enabled):
                    self.enabled = True
                    self.signal = "high"
                else:
                    self.enabled = False
                    self.signal = "low"
            else:
                self.signal = None
        elif self.module_type == "conjunction":
            if self.input_signals.count("high") == len(self.input_signals):
                self.signal = "low"
            else:
                self.signal = "high"
        return self.signal


    def __str__(self):
        return f"module {self.name} destinations: {self.destinations} signal: {self.signal}"

data = """-broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""
button_module = Module(name="button", module_type="button", dest=["broadcaster"])
modules = {"button": button_module}
# modules = {}
sources = ["button"]

module_types = {}
module_type = "None"

for line in data.splitlines():
    # print(line)
    marker = line[0]
    if marker == "-":
        module_type = "broadcaster"
    elif marker == "%":
        module_type = "flipflop"
    elif marker == "&":
        module_type = "conjunction"
    else:
        print("Marker not recognized")
        sys.exit()

    source = line.split(" -> ")[0][1:].strip()
    dest = line.split(" -> ")[1].strip().replace(" ", "").split(",")
    module = Module(name=source, module_type=module_type, dest=dest)
    module_types[source] = module_type
    modules[source] = module
    sources.append(source)

# print(modules)

# module = button_module
# while True:
#     if len(sources) == 0:
#         break
#     module_name = sources.pop(0)
#     module = modules[module_name]
#     for dest in module.destinations:
#         signal = module.signal
#         modules[dest].input_signals.append(signal)
#         modules[dest].module_trigger()
#         print(f"{module_name} -{signal}-> {dest}")
#         if not(modules[dest].signal):
#             break


def handle_signal(module, signal):
    # print(f"module {module.name} input signal {signal}")
    signal = module.module_trigger(signal)

    if not(signal):
        # print("vvv")
        return
    for dest in module.destinations:
        # print("AAA")
        # modules[dest].module_trigger(signal)
        print(f"{module.name} -{signal}-> {dest}")

    for dest in module.destinations:
        modules[dest].input_signals.append(signal)
        handle_signal(modules[dest], signal)


for source in sources[1:]:
    # print(f"SOURCE={source}")
    handle_signal(modules[source], modules[source].signal)

# print(sources)