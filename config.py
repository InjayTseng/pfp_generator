# Configuration file for NFT generation settings

# Base prompt configurations
BASE_PROMPTS = {
    "pixel_rpg": {
        "prompt": """16-bit RPG pixel art character, top-down RPG style,
simple pixel design, clear silhouette, small body with large head,
standing pose, centered composition, minimal details,
soft pastel color palette, simple shading, expressive face,
classic SNES RPG style, charming and nostalgic,
light beige canvas backdrop, small descriptive caption below""",
        "negative_prompt": """realistic, 3D, modern, high detail, complex background,
photorealistic, high resolution, ultra detailed, cinematic, dark, gloomy,
blurry, deformed, disfigured, mutated, ugly, noise, grainy"""
    },
    "tiny_sprite": {
        "prompt": """16x16 pixel art, tiny sprite of a character, NES-style, 
limited color palette, blocky pixels, minimal detail, retro video game sprite, 
centered composition, low resolution, clear silhouette, cute and simple""",
        "negative_prompt": """realistic, 3D, modern, high detail, complex background,
photorealistic, high resolution, ultra detailed, cinematic, dark, gloomy"""
    },
    "chibi": {
        "prompt": """Chibi character, big head small body, cute pixel art style,
RPG character, vibrant colors, simple design, game asset,
adorable expression, clear silhouette, minimal details""",
        "negative_prompt": """realistic, detailed, complex, photorealistic,
high resolution, ultra detailed, dark, gloomy, adult, mature"""
    }
}

# Character types and their traits
CHARACTER_TYPES = {
    "Warrior": {
        "description": "stout warrior with small weapon",
        "special_trait": "Known for bravery in battle and unwavering loyalty.",
        "outfit": ["Small Sword", "Simple Armor", "Leather Boots", "Shield"]
    },
    "Knight": {
        "description": "mighty knight with miniature armor",
        "special_trait": "Protects the realm with honor and courage.",
        "outfit": ["Helmet", "Chainmail", "Small Shield", "Sword"]
    },
    "Lady": {
        "description": "gentle lady with elegant attire",
        "special_trait": "Known for wisdom and kindness.",
        "outfit": ["Simple Dress", "Small Necklace", "Elegant Shoes"]
    },
    "Wizard": {
        "description": "wise wizard with tiny staff",
        "special_trait": "Masters ancient magical arts and spells.",
        "outfit": ["Wizard Hat", "Magic Staff", "Robe", "Spell Book"]
    },
    "Scholar": {
        "description": "avid scholar with tiny book",
        "special_trait": "Studies ancient tomes and shares knowledge.",
        "outfit": ["Glasses", "Book", "Quill", "Simple Robe"]
    },
    "Princess": {
        "description": "fair princess with small crown",
        "special_trait": "Rules with wisdom and kindness.",
        "outfit": ["Crown", "Royal Dress", "Scepter"]
    },
    "Pirate": {
        "description": "fearsome pirate with tiny sword",
        "special_trait": "Sails the digital seas in search of pixel treasures.",
        "outfit": ["Pirate Hat", "Eye Patch", "Small Sword", "Striped Shirt"]
    },
    "Cook": {
        "description": "chef with small cooking pot",
        "special_trait": "Creates delicious meals that restore health points.",
        "outfit": ["Chef Hat", "Apron", "Wooden Spoon", "Pot"]
    },
    "Hero": {
        "description": "brave hero with miniature sword",
        "special_trait": "Always ready to save the day when danger appears.",
        "outfit": ["Cape", "Simple Armor", "Sword", "Boots"]
    },
    "Witch": {
        "description": "cunning witch with tiny hat",
        "special_trait": "Brews powerful potions and casts mysterious spells.",
        "outfit": ["Witch Hat", "Magic Wand", "Potion", "Robe"]
    },
    "Alchemist": {
        "description": "alchemist with small vials",
        "special_trait": "Transforms ordinary items into magical artifacts.",
        "outfit": ["Small Vial", "Apron", "Gloves", "Goggles"]
    },
    "Woodcutter": {
        "description": "woodcutter with miniature axe",
        "special_trait": "Provides the finest wood for crafting weapons.",
        "outfit": ["Axe", "Plaid Shirt", "Work Boots", "Gloves"]
    },
    "Tech": {
        "description": "tech enthusiast with tiny gadgets",
        "special_trait": "Tinkers with gadgets and futuristic devices.",
        "outfit": ["Glasses", "Tool Belt", "Gadget", "Headset"]
    },
    "Frog": {
        "description": "small green frog",
        "special_trait": "A simple amphibian with unexpected wisdom.",
        "outfit": ["None"]
    },
    "Cat": {
        "description": "one lazy cat",
        "special_trait": "Lazes around but occasionally helps on quests.",
        "outfit": ["None"]
    },
    "Monster": {
        "description": "small monster on the prowl",
        "special_trait": "Not all monsters are evil, some just look scary.",
        "outfit": ["Horns", "Claws", "Armor Plates", "Spikes"]
    }
}

# Common traits that can be applied to any character
COMMON_TRAITS = {
    "Name": [
        "Cal", "Roderick", "Barbara", "Ansel", "Joelle", "Arabella", 
        "Bjorn", "Harald", "Finn", "Morgana", "Oswald", "Chad", 
        "Arnold", "Edith", "Nancy", "Timothy", "Hugh", "Virgil", 
        "Otis", "Quincy"
    ],
    "Hair Color": [
        "Brown", "Blonde", "Red", "Black", "Gray", "White", 
        "Blue", "Green", "Purple", "Orange"
    ],
    "Eyes": [
        "Round", "Small", "Focused", "Bright", "Wise", "Kind",
        "Determined", "Curious", "Gentle", "Stern"
    ],
    "Expression": [
        "Happy", "Serious", "Brave", "Calm", "Thoughtful", "Confident",
        "Gentle", "Stern", "Curious", "Friendly"
    ],
    "Background": [
        "Forest", "Castle", "Village", "Mountain", "Field", "Beach",
        "Tavern", "Library", "Dungeon", "Market", "Farm", "River",
        "Cave", "Simple"
    ],
    "Special Effect": [
        "None", "Magic Glow", "Sparkle", "Shadow", "Fire", "Water",
        "Lightning", "Wind", "Earth", "Light Beam", "Stars"
    ]
}

# RPG Stats for characters
RPG_STATS = {
    "Level": (1, 99),
    "HP": (10, 999),
    "MP": (0, 500),
    "Strength": (1, 99),
    "Intelligence": (1, 99),
    "Dexterity": (1, 99),
    "Luck": (1, 99)
}

# Description templates for character metadata
DESCRIPTION_TEMPLATES = [
    "A charming 16-bit {base} with {hair_color} hair. Known for being {expression} and having {eyes} eyes. {special_trait}",
    "Meet {name}, a {base} from the pixel realm. Has {hair_color} hair and {eyes} eyes with a {expression} personality. {special_trait}",
    "A classic RPG {base} with {hair_color} hair and {eyes} eyes. Always looks {expression}. {special_trait}"
]
