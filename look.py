import color, describe, item, location, npc, player

def function(target):
  location_exists = False
  #if target == "" or "here" in target or "around" in target:
  for i in range(len(location.list)):
    if player.x == location.list[i]["x"] and player.y == location.list[i]["y"]:
      location_exists = True
      describe.function(location.list[i])
  if not location_exists:
      describe.function(location.list[0])

  for i in range(len(npc.list)):
    if player.x == npc.list[i]["x"] and player.y == npc.list[i]["y"]:
      print()
      npc_state = npc.list[i]["original_state"]
      if npc.list[i]["state"] == "final":
        npc_state = npc.list[i]["final_state"]
      print(color.npc+npc.list[i]["emoji"]+" "+npc.list[i]["name"]+" the "+npc.list[i]["type"]+" "+npc_state+color.none)
    
  for i in range(len(item.list)):
    if player.x == item.list[i]["x"] and player.y == item.list[i]["y"]:
      print()
      
      # Fix grammar for a or an
      determiner = "a"
      if item.list[i]["name"][0] == "a" or item.list[i]["name"][0] == "e" or item.list[i]["name"][0] == "i" or item.list[i]["name"][0] == "o" or item.list[i]["name"][0] == "u":
        determiner = "an"
      
      print(color.item+item.list[i]["emoji"]+" There is "+determiner+" "+item.list[i]["name"]+" here."+color.none)