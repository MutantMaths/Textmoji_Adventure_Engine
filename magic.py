import color, determiner, item, npc, player

def invent(target):
  sure = "yes"
  this_determiner = determiner.function(target)
  item_index = "none"
  for i in range(len(item.list)):
    if item.list[i]["name"] == target:
      item_index = i
      print(color.magic+"Are you sure you want to reinvent "+this_determiner+" "+color.item+target+color.magic+"?"+color.none)
      sure = input("??? > ").lower()
      print()
  if sure == "yes":  
    print(color.magic+"What emoji should represent "+this_determiner+" "+color.item+target+color.magic+"?"+color.none)
    emoji = input("[Paste with CTRL+V] > ")
    emoji = emoji[0]
    print()
    print(color.magic+"What source item can you use to craft "+this_determiner+" "+color.item+emoji+" "+target+color.magic+"?"+color.none)
    source = input("??? > ").lower()
    print()
    source_exists = False
    for i in range(len(item.list)):
      if item.list[i]["name"] == source:
        source_exists = True
    verb = "invent"
    if source_exists:
      if item_index != "none":
        item.list[item_index]["emoji"] = emoji
        item.list[item_index]["source"] = source
        verb = "reinvent"
      else:
        item.list.append(
          {
            "x": "-",
            "y": "-",
            "emoji": emoji,
            "name": target,
            "source": source,
          })
      print(color.magic+"You "+verb+" "+this_determiner+" "+color.item+emoji+" "+target+color.magic+", but it's not crafted yet!"+color.none+"")
    else:
      print("Source item does not exist...")


def summon(target):
  npc_already_present = False
  for i in range(len(npc.list)):
    if npc.list[i]["x"] == player.x and npc.list[i]["y"] == player.y:
      npc_already_present = True
  if npc_already_present:
    print("An NPC already exists here...")
  else:

    name = target.capitalize()
    print(color.magic+"What emoji should represent "+color.npc+name+color.magic+"?"+color.none)
    emoji = input("[Paste with CTRL+V] > ")
    emoji = emoji[0]
    print()
    
    print(color.magic+"What type of person/creature are they?"+color.none)
    type = input("??? > ")
    print()

    print(color.magic+"What state should they be in initially?"+color.none)
    original_state = input("[e.g. \"is dancing here\"] > ")
    print()

    print(color.magic+"What key word(s) should they respond to?"+color.none)
    say_trigger = input("??? > ")
    print()
    print(color.magic+"What should they say back?"+color.none)
    say_response_say = input("[Leave blank for no response] > ")
    print()
    print(color.magic+"What item should they give in response?"+color.none)
    say_response_give = input("[Leave blank for no response] > ").lower()
    print()
    if say_response_give != "":
      item_exists = False
      for i in range(len(item.list)):
        if item.list[i]["name"] == say_response_give:
          item_exists = True
      if not item_exists:
        print("That item does not exist...")
    if say_response_give == "" or item_exists:
      print(color.magic+"Should this trigger their final state?"+color.none)
      say_final = input("[yes/no] > ").lower()
      say_response_final = False
      if say_final == "yes":
        say_response_final == True
      print()
  
      print(color.magic+"What key item should they respond to?"+color.none)
      give_trigger = input("??? > ").lower()
      print()
      if give_trigger != "":
        item_exists = False
        for i in range(len(item.list)):
          if item.list[i]["name"] == give_trigger:
            item_exists = True
        if not item_exists:
          print("That item does not exist...")
        else:
          print(color.magic+"What should they say when given this item?"+color.none)
          give_response_say = input("[Leave blank for no response] > ")
          print()
          print(color.magic+"What item should they give in response?"+color.none)
          give_response_give = input("[Leave blank for no response] > ").lower()
          print()
          if give_response_give != "":
            item_exists = False
            for i in range(len(item.list)):
              if item.list[i]["name"] == give_response_give:
                item_exists = True
            if not item_exists:
              print("That item does not exist...")
          if give_response_give == "" or item_exists:
            print(color.magic+"Should this trigger their final state?"+color.none)
            give_final = input("[yes/no] > ").lower()
            give_response_final = False
            if give_final == "yes":
              give_response_final == True
            print()
      
          print(color.magic+"What should they be doing after their final state is triggered?"+color.none)
          final_state = input("[e.g. \"is dancing here\"] > ")
          print()
          
          npc.list.append(
            {
              "x": player.x,
              "y": player.y,
              "emoji": emoji,
              "name": name,
              "type": type,
              "state": "original",
              "original_state": original_state,
              "say_trigger": say_trigger,
              "say_response_say": say_response_say,
              "say_response_give": say_response_give,
              "say_response_final": say_response_final,
              "give_trigger": give_trigger,
              "give_response_say": give_response_say,
              "give_response_give": give_response_give,
              "give_response_final": give_response_final,
              "final_state": final_state,
              
            })
          
          print(color.magic+"You summon "+color.npc+emoji+" "+name+" the "+type+color.magic+" into existence!"+color.none+"")