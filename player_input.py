import drop, craft, give, item, location, look, magic, player, say, take

def function():
  location_index = 0
  for i in range(len(location.list)):
    if player.x == location.list[i]["x"] and player.y == location.list[i]["y"]:
      location_index = i
  north = location.list[location_index]["n"]
  east = location.list[location_index]["e"]
  south = location.list[location_index]["s"]
  west = location.list[location_index]["w"]
  input_string = "("+str(player.x)+","+str(player.y)+") ["
  if north == "yes":
    input_string += "N"
  if east == "yes":
    input_string += "E"
  if south == "yes":
    input_string += "S"
  if west == "yes":
    input_string += "W"
  input_string += "] > "
  player_input = input(input_string).lower()
  print()
  player_input = player_input.split(" ",1)
  action = ""
  target = ""
  if len(player_input) > 0:
    action = player_input[0]
  if len(player_input) > 1:
    target = player_input[1]
    
  ghost_ring_index = 0
  for i in range(len(item.list)):
    if item.list[i]["name"] == "ghost ring":
      ghost_ring_index = i

  if "look" in action or "see" in action or action == "l":
    look.function(target)
  
  elif action == "crawl" and target == "north":
    if north == "hidden" or north == "yes":
      player.y += 1
      look.function("")
    else:
      print("You can't crawl that way.")
  elif action == "crawl" and target == "east":
    if east == "hidden" or east == "yes":
      player.x += 1
      look.function("")
    else:
      print("You can't crawl that way.")
  elif action == "crawl" and target == "south":
    if south == "hidden" or south == "yes":
      player.y -= 1
      look.function("")
    else:
      print("You can't crawl that way.")
  elif action == "crawl" and target == "west":
    if west == "hidden" or west == "yes":
      player.x -= 1
      look.function("")
    else:
      print("You can't crawl that way.")
  elif action == "crawl":
    print("Which way do you want to crawl?")

  elif action == "ghost" and target == "north" and item.list[ghost_ring_index]["x"] == "i" and item.list[ghost_ring_index]["y"] == "i":
    item.list[ghost_ring_index]["x"] = "-"
    item.list[ghost_ring_index]["y"] = "-"
    player.y += 1
    look.function("")
  elif action == "ghost" and target == "east" and item.list[ghost_ring_index]["x"] == "i" and item.list[ghost_ring_index]["y"] == "i":
    item.list[ghost_ring_index]["x"] = "-"
    item.list[ghost_ring_index]["y"] = "-"
    player.x += 1
    look.function("")
  elif action == "ghost" and target == "south" and item.list[ghost_ring_index]["x"] == "i" and item.list[ghost_ring_index]["y"] == "i":
    item.list[ghost_ring_index]["x"] = "-"
    item.list[ghost_ring_index]["y"] = "-"
    player.y -= 1
    look.function("")
  elif action == "ghost" and target == "west" and item.list[ghost_ring_index]["x"] == "i" and item.list[ghost_ring_index]["y"] == "i":
    item.list[ghost_ring_index]["x"] = "-"
    item.list[ghost_ring_index]["y"] = "-"
    player.x -= 1
    look.function("")
  elif action == "ghost":
    print("Ghosting requires the ghost ring and a valid direction...")
    
  elif action == "n" or "north" in target:
    if north == "yes":
      player.y += 1
      look.function("")
    else:
      print("You can't move that way.")
  elif action == "e" or "east" in target:
    if east == "yes":
      player.x += 1
      look.function("")
    else:
      print("You can't move that way.")
  elif action == "s" or "south" in target:
    if south == "yes":
      player.y -= 1
      look.function("")
    else:
      print("You can't move that way.")
  elif action == "w" or "west" in target:
    if west == "yes":
      player.x -= 1
      look.function("")
    else:
      print("You can't move that way.")
      
  elif "take" in action or "get" in action or "pick" in action:
    take.function(target)
  elif "drop" in action or "throw" in action or "dump" in action:
    drop.function(target)
  elif "give" in action or "show" in action:
    give.function(target)
  elif "say" in action or "speak" in action or "ask" in action or "shout" in action:
    say.function(target)
  elif "craft" in action or "make" in action or "build" in action:
    craft.function(target)
  elif "invent" in action:
    if target == "":
      print("What do you want to invent?")
    else:
      magic.invent(target)
  elif "summon" in action:
    if target == "":
      print("Whom do you want to summon?")
    else:
      magic.summon(target)
      
  else:
    print("Try typing something else...")
  print()
  function()