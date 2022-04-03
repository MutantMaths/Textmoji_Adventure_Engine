import color

list = [ # start npc list
  
  {
    "x": 0,
    "y": -1,
    "emoji": "🧓‍",
    "name": "Agelu",
    "type": "elderly lady",
    "state": "original",
    "original_state": "says \"Ahh! Young one! Please, I dropped my old key. Could you reach down and get it for me by typing GET OLD KEY, and then pass it to me by typing GIVE OLD KEY? Thank you so much...\"",
    "say_trigger": "key",
    "say_response_say": "Yes, please type GET OLD KEY then press ENTER, then type GIVE OLD KEY and press ENTER again. Thank you...",
    "say_response_give": "",
    "say_response_final": False,
    "give_trigger": "old key",
    "give_response_say": "Oh, you are such a kind-hearted child! My last visitor used the key to steal some of the gold that's locked in my bedroom! Fortunately I changed the locks. Please take this gold coin as a reward for your kindness...",
    "give_response_give": "gold coin",
    "give_response_final": True,
    "final_state": "smiles at you and says \"Thank you for your assistance ealier...\"",
    
  },
  
  {
    "x": 2,
    "y": 1,
    "emoji": "🧚",
    "name": "Lolani",
    "type": "Flower Fairy",
    "state": "original",
    "original_state": "squeeks \"Eeeyaa! Got any shamrocks for me?!\"",
    "say_trigger": "shamrock",
    "say_response_say": "Yaaa-eeeh!! That's right, some peeps call them a four-leafed clover! Would you like this seedling?",
    "say_response_give": "seedling",
    "say_response_final": False,
    "give_trigger": "shamrock",
    "give_response_say": "Yee-yee-yeeee-aahhh!! Here ya go!",
    "give_response_give": "chestnut",
    "give_response_final": True,
    "final_state": "flitters happily between the flowers admiring her shamrock.",
    
  },
  
  {
    "x": 2,
    "y": -3,
    "emoji": "🥷",
    "name": "Lubba",
    "type": "Eastern Guard",
    "state": "original",
    "original_state": "sternly says \"Nobody passes here. And nobody should ASK about the secret!\"",
    "say_trigger": "secret",
    "say_response_say": "Yes, whatever you do, do not ask my sister about the secret path!",
    "say_response_give": "",
    "say_response_final": False,
    "give_trigger": "wubba",
    "give_response_say": "The first part of the password is 'Mr Haywood'...",
    "give_response_give": "",
    "give_response_final": False,
    "final_state": "",
    
  },
  
  {
    "x": -2,
    "y": -3,
    "emoji": "🥷",
    "name": "Wubba",
    "type": "Western Guard",
    "state": "original",
    "original_state": "sternly says \"Nobody passes here. And nobody asks about the secret!\"",
    "say_trigger": "path",
    "say_response_say": "Yes, whatever you do, do not ask the gardener about the secret path!",
    "say_response_give": "",
    "say_response_final": False,
    "give_trigger": "lubba",
    "give_response_say": "The second part of the passord is 'is the best'...",
    "give_response_give": "",
    "give_response_final": False,
    "final_state": "",
    
  },
  
  {
    "x": 0,
    "y": 1,
    "emoji": "🧝",
    "name": "Dub Dub",
    "type": "Flower Gardener",
    "state": "original",
    "original_state": "is tending to the flowers mumbling something about... needing a bath ...?",
    "say_trigger": "path",
    "say_response_say": "Oh! No, no. Absolutely no secret paths around here... Oh, and no CRAWLING either!",
    "say_response_give": "",
    "say_response_final": False,
    "give_trigger": "",
    "give_response_say": "",
    "give_response_give": "",
    "give_response_final": False,
    "final_state": "",
    
  },
  
  {
    "x": -2,
    "y": 3,
    "emoji": "🧞",
    "name": "Olioli",
    "type": "Cave Djinn",
    "state": "original",
    "original_state": "floats ominously over a rusty gem-encrusted lamp. She is made of magical smoke the color of gemstone",
    "say_trigger": "ghost",
    "say_response_say": "See the impassable cave walls around us? Haha, well, take this gem. Craft it into a ghost ring and then type \"ghost east\" and you'll be in for quite a shock! But remember they, such rings are single-use only!",
    "say_response_give": "gem",
    "say_response_final": False,
    "give_trigger": "gem",
    "give_response_say": "Greetings little one. Did you know that a "+color.item+"gem"+color.npc+" like this can be CRAFTED into a "+color.item+"ghost ring"+color.npc+"? Here you go...",
    "give_response_give": "ghost ring",
    "give_response_final": False,
    "final_state": "",
    
  },
  
  {
    "x": -1,
    "y": -3,
    "emoji": "🦹",
    "name": "Viliamu",
    "type": "Street Lurker",
    "state": "original",
    "original_state": "is loitering suspiciously in the shadows.",
    "say_trigger": "",
    "say_response_say": "Got any swag?",
    "say_response_give": "",
    "say_response_final": False,
    "give_trigger": "bag o' swag",
    "give_response_say": "Mwhahaha! Here ya go...",
    "give_response_give": "bomb",
    "give_response_final": False,
    "final_state": "",
    
  },
  
  {
    "x": 2,
    "y": 3,
    "emoji": "👷",
    "name": "Taito",
    "type": "Craft-Master",
    "state": "original",
    "original_state": "is inspecting a strange half-finished gizmo that lies on a table. \"Hey kid. Anybody told you about crafting?\" she says.",
    "say_trigger": "craft",
    "say_response_say": "Yep. Assuming you have the source material, you can use the CRAFT command to craft items that you need. Try crafting an "+color.item+"bowl"+color.npc+" from this "+color.item+"piece of metal"+color.npc+".",
    "say_response_give": "piece of metal",
    "say_response_final": False,
    "give_trigger": "bowl",
    "give_response_say": "Good job!",
    "give_response_give": "bowl",
    "give_response_final": False,
    "final_state": "",
    
  },
  
  {
    "x": -3,
    "y": 3,
    "emoji": "🐉",
    "name": "Laki",
    "type": "Gemstone Dragon",
    "state": "original",
    "original_state": "is sleeping here.",
    "say_trigger": "",
    "say_response_say": "*Yawn*",
    "say_response_give": "gem",
    "say_response_final": False,
    "give_trigger": "gem",
    "give_response_say": "Zzz...",
    "give_response_give": "gem",
    "give_response_final": False,
    "final_state": "",
    
  },
  
  {
    "x": -2,
    "y": 4,
    "emoji": "🧙",
    "name": "Kenese",
    "type": "Inventress",
    "state": "original",
    "original_state": "looks up from her work. \"Can you craft a magnet for me please?\"",
    "say_trigger": "exist",
    "say_response_say": "Doesn't exist?? Just INVENT one!! You could use this as the source material.",
    "say_response_give": "piece of metal",
    "say_response_final": False,
    "give_trigger": "magnet",
    "give_response_say": "Oh yeah!!! Now you can invent anything you want!!!",
    "give_response_give": "",
    "give_response_final": True,
    "final_state": "is using your magnet to engineer something ominous.",
    
  },
  
  {
    "x": 2,
    "y": 4,
    "emoji": "👺",
    "name": "Semis",
    "type": "Beast-Summoner",
    "state": "original",
    "original_state": "growls at you: \"Tell me something about dragons and I'll tell you something useful in return!\"",
    "say_trigger": "dragon",
    "say_response_say": "Have you tried to SUMMON a new NPC yet?? It's experimental magic though so don't say you haven't been warned! Also, I'm looking for a boomerang if you happen to come across one...",
    "say_response_give": "",
    "say_response_final": False,
    "give_trigger": "boomerang",
    "give_response_say": "Fantastic! Here's a tip. Try heading North until you reach the ocean. Then crawl North down the cliff.",
    "give_response_give": "",
    "give_response_final": False,
    "final_state": "",
    
  },
  
  {
    "x": 2,
    "y": 7,
    "emoji": "🐙",
    "name": "Samitioata",
    "type": "End Boss",
    "state": "original",
    "original_state": "yells \"Tell me the PASSWORD and you'll complete this game!!! Give Wubba and item called 'lubba', and Lubba and item called 'wubba' to reveal the secret phrase!\"",
    "say_trigger": "mr haywood is the best",
    "say_response_say": "⭐⭐⭐ YEAH!!! YOU DID IT! HERE YOU GO!!! ⭐⭐⭐",
    "say_response_give": "trophy",
    "say_response_final": False,
    "give_trigger": "trophy",
    "give_response_say": "Wait? Does this mean that I completed the game?!? YEAH!",
    "give_response_give": "",
    "give_response_final": True,
    "final_state": "is dancing around the bay.",
    
  },
  
  {
    "x": 2,
    "y": 5,
    "emoji": "👻",
    "name": "Teuila",
    "type": "Eastern Spirit",
    "state": "original",
    "original_state": "is floating here...",
    "say_trigger": "ghost",
    "say_response_say": "...",
    "say_response_give": "gem",
    "say_response_final": False,
    "give_trigger": "gem",
    "give_response_say": "... If you don't know what to craft with this gemstone, find my Master Olioli in the Forest Cave ...",
    "give_response_give": "gem",
    "give_response_final": False,
    "final_state": "",
    
  },
  
  {
    "x": -2,
    "y": 5,
    "emoji": "👻",
    "name": "Tuala",
    "type": "Western Spirit",
    "state": "original",
    "original_state": "is floating here...",
    "say_trigger": "ghost",
    "say_response_say": "...",
    "say_response_give": "gem",
    "say_response_final": False,
    "give_trigger": "gem",
    "give_response_say": "... If you don't know what to craft with this gemstone, find my Master Olioli in the Forest Cave ...",
    "give_response_give": "gem",
    "give_response_final": False,
    "final_state": "",
    
  },

] # end npc list