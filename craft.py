import color, determiner, item, npc

def function(target):

  item_exists = False
  craftable = False
  
  for i in range(len(item.list)):
    if item.list[i]["name"] in target:
      item_exists = True

      for j in range(len(item.list)):
        if item.list[i]["source"] == item.list[j]["name"]:
          craftable = True
          determiner2 = determiner.function(item.list[i]["name"])
          if item.list[j]["x"] == "i" and item.list[j]["y"] == "i":
  
            item.list[j]["x"] = "-"
            item.list[j]["y"] = "-"

            item.list[i]["x"] = "i"
            item.list[i]["y"] = "i"
            
            print("You use your "+color.item+item.list[j]["name"]+color.none+" to craft "+determiner2+" "+color.item+item.list[i]["name"]+color.none+"!")
          else:
            determiner1 = determiner.function(item.list[i]["source"])
        
            print("You need "+determiner1+" "+color.item+item.list[i]["source"]+color.none+" to craft "+determiner2+" "+color.item+item.list[i]["name"]+color.none+", but you don't have that!")

      if not craftable:
        print("That item cannot be crafted...")        

  if not item_exists:
    print("No such item exists in this universe!")