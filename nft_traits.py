import json
import random
from typing import Dict, List, Union
import os

class NFTTraitGenerator:
    def __init__(self):
        # Collection info
        self.collection_name = "Pixel Heroes"
        self.base_url = "https://pixelheroes.io"
        self.image_base_url = "https://storage.pixelheroes.io/images"
        self.description_templates = [
            "A charming 16-bit {base} with {hair_color} hair. Known for being {expression} and having {eyes} eyes. {special_trait}",
            "Meet {name}, a {base} from the pixel realm. Has {hair_color} hair and {eyes} eyes with a {expression} personality. {special_trait}",
            "A classic RPG {base} with {hair_color} hair and {eyes} eyes. Always looks {expression}. {special_trait}"
        ]
        
        # Special traits for each base character
        self.special_traits = {
            "Warrior": "Known for bravery in battle and unwavering loyalty.",
            "Knight": "Protects the realm with honor and courage.",
            "Princess": "Rules with wisdom and kindness.",
            "Wizard": "Masters ancient magical arts and spells.",
            "Scholar": "Studies ancient tomes and shares knowledge.",
            "Witch": "Brews powerful potions and casts mysterious spells.",
            "Cook": "Creates delicious meals that restore health points.",
            "Pirate": "Sails the digital seas in search of pixel treasures.",
            "Hero": "Always ready to save the day when danger appears.",
            "Alchemist": "Transforms ordinary items into magical artifacts.",
            "Woodcutter": "Provides the finest wood for crafting weapons.",
            "Tech": "Tinkers with gadgets and futuristic devices.",
            "Frog": "A simple amphibian with unexpected wisdom.",
            "Cat": "Lazes around but occasionally helps on quests."
        }

        # Define possible traits for each category
        self.traits = {
            "Base": [
                "Warrior", "Knight", "Lady", "Wizard", "Scholar", "Princess", 
                "Pirate", "Cook", "Hero", "Witch", "Alchemist", "Woodcutter", 
                "Tech", "Shepherd", "Frog", "Cat", "Monster"
            ],
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
            "Outfit": {
                "Warrior": ["Small Sword", "Simple Armor", "Leather Boots", "Shield"],
                "Knight": ["Helmet", "Chainmail", "Small Shield", "Sword"],
                "Lady": ["Simple Dress", "Small Necklace", "Elegant Shoes"],
                "Wizard": ["Wizard Hat", "Magic Staff", "Robe", "Spell Book"],
                "Scholar": ["Glasses", "Book", "Quill", "Simple Robe"],
                "Princess": ["Crown", "Royal Dress", "Scepter"],
                "Pirate": ["Pirate Hat", "Eye Patch", "Small Sword", "Striped Shirt"],
                "Cook": ["Chef Hat", "Apron", "Wooden Spoon", "Pot"],
                "Hero": ["Cape", "Simple Armor", "Sword", "Boots"],
                "Witch": ["Witch Hat", "Magic Wand", "Potion", "Robe"],
                "Alchemist": ["Small Vial", "Apron", "Gloves", "Goggles"],
                "Woodcutter": ["Axe", "Plaid Shirt", "Work Boots", "Gloves"],
                "Tech": ["Glasses", "Tool Belt", "Gadget", "Headset"],
                "Shepherd": ["Staff", "Simple Clothes", "Hat", "Boots"],
                "Frog": ["None"],
                "Cat": ["None"],
                "Monster": ["Horns", "Claws", "Armor Plates", "Spikes"]
            },
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
        
        # Define stat ranges for RPG characters
        self.stat_ranges = {
            "Level": (1, 99),
            "HP": (10, 999),
            "MP": (0, 500),
            "Strength": (1, 99),
            "Intelligence": (1, 99),
            "Dexterity": (1, 99),
            "Luck": (1, 99)
        }

    def generate_name(self, base: str, traits: Dict) -> str:
        """Generate a name from the predefined list"""
        # Simply use a name from the predefined list
        return random.choice(self.traits["Name"])

    def generate_description(self, traits: Dict) -> str:
        """Generate a description based on traits"""
        base_type = traits["Base"]  # Get character type (e.g., "Warrior")
        name = traits["Name"]  # Get character name
        template = random.choice(self.description_templates)
        
        return template.format(
            base=base_type.lower(),
            name=name,
            hair_color=traits["Hair Color"].lower(),
            eyes=traits["Eyes"].lower(),
            expression=traits["Expression"].lower(),
            special_trait=self.special_traits.get(base_type, "A truly unique character!")
        )

    def generate_random_traits(self, token_id: int) -> Dict:
        # Select base character type
        base = random.choice(self.traits["Base"])
        
        # Get character name
        name = self.generate_name(base, {})
        
        # Get trait values
        hair_color = random.choice(self.traits["Hair Color"])
        eyes = random.choice(self.traits["Eyes"])
        expression = random.choice(self.traits["Expression"])
        background = random.choice(self.traits["Background"])
        special_effect = random.choice(self.traits["Special Effect"])
        
        # Create traits dict for description generation
        trait_dict = {
            "Base": base,
            "Name": name,
            "Hair Color": hair_color,
            "Eyes": eyes,
            "Expression": expression
        }
        
        # Generate character caption
        caption = ""
        if base == "Warrior":
            caption = "stout warrior"
        elif base == "Knight":
            caption = "mighty knight"
        elif base == "Lady":
            caption = "gentle lady"
        elif base == "Wizard":
            caption = "wise wizard"
        elif base == "Scholar":
            caption = "avid scholar"
        elif base == "Princess":
            caption = "fair princess"
        elif base == "Pirate":
            caption = "fearsome pirate"
        elif base == "Cook":
            caption = "cooks"
        elif base == "Hero":
            caption = "saves the day"
        elif base == "Witch":
            caption = "cunning witch"
        elif base == "Alchemist":
            caption = "alchemist"
        elif base == "Woodcutter":
            caption = "woodcutter"
        elif base == "Tech":
            caption = "tech enthusiast"
        elif base == "Shepherd":
            caption = "herds sheep"
        elif base == "Frog":
            caption = "a frog"
        elif base == "Cat":
            caption = "one lazy cat"
        elif base == "Monster":
            caption = "on the prowl"
        
        # Generate metadata
        metadata = {
            "name": f"{name}",
            "description": self.generate_description(trait_dict),
            "external_url": f"{self.base_url}/{token_id}",
            "image": f"{self.image_base_url}/{token_id}.png",
            "attributes": [
                {"trait_type": "Base", "value": base},
                {"trait_type": "Name", "value": name},
                {"trait_type": "Caption", "value": caption},
                {"trait_type": "Hair Color", "value": hair_color},
                {"trait_type": "Eyes", "value": eyes},
                {"trait_type": "Expression", "value": expression},
                {"trait_type": "Background", "value": background},
                {"trait_type": "Special Effect", "value": special_effect}
            ]
        }
        
        # Add outfit pieces
        outfit_pieces = self.traits["Outfit"].get(base, [])
        for piece in outfit_pieces:
            if piece != "None":
                metadata["attributes"].append({
                    "trait_type": "Outfit",
                    "value": piece
                })
        
        # Add RPG stats
        metadata["attributes"].extend([
            {
                "display_type": "number",
                "trait_type": "Level",
                "value": random.randint(*self.stat_ranges["Level"])
            },
            {
                "display_type": "number",
                "trait_type": "HP",
                "value": random.randint(*self.stat_ranges["HP"])
            },
            {
                "display_type": "number",
                "trait_type": "MP",
                "value": random.randint(*self.stat_ranges["MP"])
            },
            {
                "display_type": "number",
                "trait_type": "Strength",
                "value": random.randint(*self.stat_ranges["Strength"])
            },
            {
                "display_type": "number",
                "trait_type": "Intelligence",
                "value": random.randint(*self.stat_ranges["Intelligence"])
            },
            {
                "display_type": "number",
                "trait_type": "Dexterity",
                "value": random.randint(*self.stat_ranges["Dexterity"])
            },
            {
                "display_type": "number",
                "trait_type": "Luck",
                "value": random.randint(*self.stat_ranges["Luck"])
            }
        ])
        
        return metadata

    def generate_batch(self, start_id: int, count: int) -> List[Dict]:
        """Generate multiple NFT metadata sets"""
        return [self.generate_random_traits(i) for i in range(start_id, start_id + count)]

    def save_metadata(self, metadata: Union[Dict, List[Dict]], output_dir: str):
        """Save metadata to JSON file(s)"""
        os.makedirs(output_dir, exist_ok=True)
        
        if isinstance(metadata, list):
            # Save batch as individual files
            for nft in metadata:
                token_id = int(nft["image"].split("/")[-1].split(".")[0])
                filename = os.path.join(output_dir, f"{token_id}.json")
                with open(filename, 'w') as f:
                    json.dump(nft, f, indent=2)
        else:
            # Save single metadata
            token_id = int(metadata["image"].split("/")[-1].split(".")[0])
            filename = os.path.join(output_dir, f"{token_id}.json")
            with open(filename, 'w') as f:
                json.dump(metadata, f, indent=2)

def main():
    # Create generator
    generator = NFTTraitGenerator()
    
    # Create output directory
    output_dir = "metadata"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate a single NFT metadata
    single_nft = generator.generate_random_traits(1)
    generator.save_metadata(single_nft, output_dir)
    
    # Generate a batch of NFT metadata
    batch_size = 333
    batch_nfts = generator.generate_batch(2, batch_size)
    generator.save_metadata(batch_nfts, output_dir)
    
    print(f"Generated metadata for 1 single NFT and {batch_size} batch NFTs")
    print(f"Saved to '{output_dir}' directory")

if __name__ == "__main__":
    main()
