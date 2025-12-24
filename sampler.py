class Event:
  def __init__(self, kind: str, timestamp: float, function: str):
    self.kind = kind
    self.timestamp = timestamp
    self.function = function 

class Sample:
  def __init__(self, timestamp: float, functions: list[str]):
    self.timestamp = timestamp
    self.functions = functions

def convertToTrace(samples: list[Sample]):  
  '''
    the stack is one of:
      - has fewer functions than the sample (new ones started)
      - has more functions than the sample (running ones ended)
      - is representative of the sample (nothing changed)
  '''

  stack: list[str] = []
  trace: list[Event] = []

  for sample in samples:
    
    # function(s) ended
    while len(stack) > len(sample.functions):
      function = stack.pop()
      event = Event('end', sample.timestamp, function)
      trace.append(event)

    # function(s) started
    while len(stack) < len(sample.functions):
      new = sample.functions[len(stack):]
      for function in new:
        event = Event('start', sample.timestamp, function)
        stack.append(function)
        trace.append(event)

  return trace


if __name__ == "__main__":
  print('test')
  samples = [
    Sample("7.5", ["main"]),
    Sample("9.2", ["main","my_fn"]),
    Sample("10.7", ["main"]),
    Sample("12.2", ["main","my_fn","my_fn2","my_fn3"]),
    Sample("14.6", ["main","my_fn","my_fn2","my_fn3"]),
    Sample("18.3", ["main","my_fn"]),
    Sample("21.3", ["main"]),
    Sample("23.1", []),
  ]

  x = convertToTrace(samples)
  for event in x:
    print(f"{event.function} {event.kind} at {event.timestamp}")