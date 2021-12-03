import random

def main():
  die = createDie(6) # default max number for the die. This can be changed for a die with a different number of sides
  bRun = True
  while bRun:
    bRun = promptRoll()
    rollDie(die,bRun)

def createDie(sides):
  outList = []
  for i in range(sides):
    addNumb = sides-i
    for n in range(addNumb):
      outList.append(i+1)
  return outList

def promptRoll():
  shouldRoll = True
  prompt = input('Press enter to roll. Type "quit" to quit the program: ')
  if prompt == 'quit':
    shouldRoll = False
  return shouldRoll

def rollDie(die,bRun):
  if not bRun:
    return
  rng = random.randint(0,len(die)-1)
  print("You rolled a " + str(die[rng]))

main()
