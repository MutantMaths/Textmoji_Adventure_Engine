import color, item
import player

def function(target):
  item_is_here = False
  if target == "":
    print("What is it that you want to take?")
  else:
    for i in range(len(item.list)):
      if player.x == item.list[i]["x"] and player.y == item.list[i]["y"] and item.list[i]["name"] in target:
        item_is_here = True
        item.list[i]["x"] = "i"
        item.list[i]["y"] = "i"
        print(color.item+"You take the "+item.list[i]["emoji"]+" "+item.list[i]["name"]+"."+color.none)
    if not item_is_here:
      print("There is nothing like that here...")