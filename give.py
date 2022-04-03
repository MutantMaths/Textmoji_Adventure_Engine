import color, determiner, item, npc, player

def function(target):
  item_is_here = False
  npc_is_here = False
  if target == "":
    print("What is it that you want to give?")
  else:
    this_npc = ""
    for i in range(len(npc.list)):
      if npc.list[i]["x"] == player.x and npc.list[i]["y"] == player.y:
        this_npc = i
    if this_npc == "":
      print("There's nobody here to something to...")
    else:
      for i in range(len(item.list)):
        if item.list[i]["x"] == "i" and item.list[i]["y"] == "i" and item.list[i]["name"] in target:
          item_is_here = True

          if npc.list[this_npc]["give_trigger"] == item.list[i]["name"] and npc.list[this_npc]["state"] != "final":
            item.list[i]["x"] = "-"
            item.list[i]["y"] = "-"
            print(color.item+"You give the "+item.list[i]["emoji"]+" "+item.list[i]["name"]+" to "+color.npc+npc.list[this_npc]["emoji"]+" "+npc.list[this_npc]["name"]+color.item+"."+color.none)
            if npc.list[this_npc]["give_response_say"] != "":
              print()
              print(color.npc+npc.list[this_npc]["emoji"]+" "+npc.list[this_npc]["name"]+" says \""+npc.list[this_npc]["give_response_say"]+"\"."+color.none)
            if npc.list[this_npc]["give_response_give"] != "":
              for j in range(len(item.list)):
                if item.list[j]["name"] == npc.list[this_npc]["give_response_give"]:
                  item.list[j]["x"] = "i"
                  item.list[j]["y"] = "i"
                  print()

                  this_determiner = determiner.function(item.list[j]["name"])
                  
                  print(color.item+npc.list[this_npc]["emoji"]+" "+npc.list[this_npc]["name"]+" gives you "+this_determiner+" "+item.list[j]["emoji"]+" "+item.list[j]["name"]+"."+color.none)

            if npc.list[this_npc]["give_response_final"]:
              npc.list[this_npc]["state"] = "final"

          else:
            print("They don't look interested in that...")

      if not item_is_here:
        print("You're not carrying anything like that...")