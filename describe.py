import biome, color, item
import os

def function(location):
  os.system("clear")
  inventory_string = "🎒 Inventory:"
  for i in range(len(item.list)):
    if item.list[i]["x"] == "i" and item.list[i]["y"] == "i":
      inventory_string += "  "+item.list[i]["emoji"]
  print(inventory_string)
  
  this_biome = biome.dictionary[location["biome"]]
  biome_triple = this_biome["emoji"]+" "+this_biome["emoji"]+" "+this_biome["emoji"]
  print()
  print(this_biome["color"]+biome_triple+" "+location["title"]+" "+biome_triple)
  print()
  print(location["description"]+color.none)