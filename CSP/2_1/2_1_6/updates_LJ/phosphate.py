def monitor():

  ph_level = .3

  current = get_posphate()
  mesg = "Posphates OK"
  
  if (current > ph_level):
      mesg = "Posphates too high!"

  return mesg

# Function to simulate actual fish tank monitoring
def get_posphate():
  return .05 