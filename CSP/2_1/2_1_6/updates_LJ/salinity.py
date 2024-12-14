def monitor():
  try:
    
    val1 = 28
    val2 = 35

    sal_levels = list(range(val1, val2))

    current = get_salinity()
    mesg = "Salinity OK"

    if (current < sal_levels[0]):
      mesg = "Salinity too low!"
    elif (current > sal_levels[6]):
      mesg = "Salinity too high!"
    
  except:
    print("Salinity: Unexpected error")

  return mesg

# Function to simulate actual fish tank monitoring
def get_salinity():
  return 31