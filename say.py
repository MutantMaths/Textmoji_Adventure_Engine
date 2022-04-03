import color, item, npc, player

def function(target):
  print("You say \""+target+"\".")
  for i in range(len(npc.list)):
      if npc.list[i]["x"] == player.x and npc.list[i]["y"] == player.y:
        if npc.list[i]["say_trigger"] in target and npc.list[i]["state"] != "final":
          if npc.list[i]["say_response_say"] != "":
            print()
            print(color.npc+npc.list[i]["emoji"]+" "+npc.list[i]["name"]+" says \""+npc.list[i]["say_response_say"]+"\"."+color.none)
          if npc.list[i]["say_response_give"] != "":
            for j in range(len(item.list)):
              if item.list[j]["name"] == npc.list[i]["say_response_give"]:
                item.list[j]["x"] = "i"
                item.list[j]["y"] = "i"
                print()
                print(color.item+npc.list[i]["emoji"]+" "+npc.list[i]["name"]+" gives you a "+item.list[j]["emoji"]+" "+item.list[j]["name"]+"."+color.none)
                
          if npc.list[i]["say_response_final"]:
            npc.list[i]["state"] = "final"