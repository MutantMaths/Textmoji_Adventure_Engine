import color, item, player

def function(target):
  item_is_here = False
  if target == "":
    print("What is it that you want to drop?")
  else:
    for i in range(len(item.list)):
      if item.list[i]["x"] == "i" and item.list[i]["y"] == "i" and item.list[i]["name"] in target:
        item_is_here = True
        item.list[i]["x"] = player.x
        item.list[i]["y"] = player.y
        print(color.item+"You drop the "+item.list[i]["emoji"]+" "+item.list[i]["name"]+"."+color.none)
    if not item_is_here:
      print("You're not carrying anything like that...")