import json
import random
from typing import Dict, List, Union
import os

class NFTTraitGenerator:
    def __init__(self):
        # Collection info
        self.collection_name = "Crayon Cats"
        self.base_url = "https://crayoncats.io"
        self.image_base_url = "https://storage.crayoncats.io/images"
        self.description_templates = [
            "A whimsical {base} drawn in crayon style. This adorable feline has {fur_color} fur, {eyes} eyes, and a {expression} expression. {special_trait}",
            "Meet this charming {base} with {fur_color} fur! Known for their {eyes} eyes and {expression} personality. {special_trait}",
            "An enchanting {base} featuring {fur_color} fur and {eyes} eyes. Always wearing a {expression} look. {special_trait}"
        ]
        
        # Special traits for each base character
        self.special_traits = {
            "Astronaut": "Dreams of exploring the cosmic catnip fields.",
            "Princess": "Rules over the kingdom of Purrington with grace and wisdom.",
            "Pirate": "Sails the seven seas in search of legendary fish treasures.",
            "Chef": "Creates the most delectable gourmet cat treats in town.",
            "Superhero": "Protects the city from notorious dog villains.",
            "Artist": "Paints masterpieces using whiskers as brushes.",
            "Wizard": "Masters the ancient arts of feline magic.",
            "Rock Star": "Performs sold-out concerts at the Meow Arena.",
            "Ninja": "Stealthily prowls through the shadows.",
            "Scientist": "Conducts groundbreaking research in catnip physics.",
            "Explorer": "Discovers new territories in the backyard jungle.",
            "Detective": "Solves mysterious cases of missing yarn balls."
        }

        # Define possible traits for each category
        self.traits = {
            "Base": [
                "Astronaut Cat", "Princess Cat", "Pirate Cat", "Chef Cat",
                "Superhero Cat", "Artist Cat", "Wizard Cat", "Rock Star Cat",
                "Ninja Cat", "Scientist Cat", "Explorer Cat", "Detective Cat"
            ],
            "Fur Color": [
                "White", "Black", "Orange", "Gray", "Brown", "Calico",
                "Siamese", "Blue", "Purple", "Rainbow", "Golden", "Silver"
            ],
            "Eyes": [
                "Round", "Curious", "Sleepy", "Determined", "Sparkly",
                "Mysterious", "Playful", "Wise", "Brave", "Sweet",
                "Focused", "Dreamy"
            ],
            "Expression": [
                "Happy", "Excited", "Confident", "Thoughtful", "Mischievous",
                "Proud", "Calm", "Energetic", "Friendly", "Bold",
                "Peaceful", "Adventurous"
            ],
            "Outfit": {
                "Astronaut": ["Space Suit", "Helmet", "Oxygen Pack", "Moon Boots"],
                "Princess": ["Crown", "Royal Dress", "Magic Wand", "Crystal Shoes"],
                "Pirate": ["Eye Patch", "Striped Shirt", "Captain Hat", "Treasure Map"],
                "Chef": ["Chef Hat", "Apron", "Wooden Spoon", "Recipe Book"],
                "Superhero": ["Cape", "Mask", "Power Gloves", "Hero Belt"],
                "Artist": ["Beret", "Paint Brush", "Palette", "Smock"],
                "Wizard": ["Pointy Hat", "Magic Staff", "Spell Book", "Enchanted Robe"],
                "Rock Star": ["Mohawk", "Guitar", "Star Glasses", "Leather Jacket"],
                "Ninja": ["Headband", "Stealth Suit", "Katana", "Smoke Bombs"],
                "Scientist": ["Lab Coat", "Safety Goggles", "Test Tubes", "Data Pad"],
                "Explorer": ["Safari Hat", "Adventure Vest", "Compass", "Binoculars"],
                "Detective": ["Deerstalker Hat", "Magnifying Glass", "Notebook", "Pipe"]
            },
            "Background": [
                "Space", "Castle", "Ocean", "Kitchen", "City", "Art Studio",
                "Magic Library", "Concert Stage", "Dojo", "Laboratory",
                "Jungle", "Mystery Office"
            ],
            "Special Effect": [
                "Stardust", "Hearts", "Lightning", "Bubbles", "Paint Splatter",
                "Magic Sparkles", "Music Notes", "Smoke", "Data Stream",
                "Nature Aura", "Time Ripple", "Mystery Fog"
            ]
        }
        
        # Define stat ranges
        self.stat_ranges = {
            "Level": (1, 100),
            "Energy": (1.0, 10.0),
            "Creativity": (1, 100),
            "Magic Power": (1, 100),
            "Agility": (1, 100),
            "Generation": (1, 5)
        }

    def generate_name(self, base: str, traits: Dict) -> str:
        """Generate a creative name based on traits"""
        adjectives = {
            "Astronaut": ["Cosmic", "Stellar", "Nova", "Galaxy"],
            "Princess": ["Royal", "Majestic", "Noble", "Regal"],
            "Pirate": ["Captain", "Salty", "Stormy", "Brave"],
            "Chef": ["Tasty", "Spicy", "Sweet", "Savory"],
            "Superhero": ["Mighty", "Super", "Amazing", "Ultra"],
            "Artist": ["Creative", "Colorful", "Artistic", "Dreamy"],
            "Wizard": ["Mystic", "Magical", "Enchanted", "Arcane"],
            "Rock Star": ["Electric", "Wild", "Rockin'", "Star"],
            "Ninja": ["Silent", "Shadow", "Swift", "Stealth"],
            "Scientist": ["Doctor", "Professor", "Genius", "Smart"],
            "Explorer": ["Adventure", "Wild", "Brave", "Bold"],
            "Detective": ["Clever", "Sharp", "Wise", "Sleuth"]
        }
        
        base_type = base.split()[0]  # Get type (e.g., "Astronaut" from "Astronaut Cat")
        adj = random.choice(adjectives.get(base_type, ["Cool"]))
        color = traits["Fur Color"].lower()
        
        return f"{adj} {color.title()} {base_type}"

    def generate_description(self, traits: Dict) -> str:
        """Generate a description based on traits"""
        base_type = traits["Base"].split()[0]  # Get type (e.g., "Astronaut" from "Astronaut Cat")
        template = random.choice(self.description_templates)
        
        return template.format(
            base=traits["Base"],
            fur_color=traits["Fur Color"].lower(),
            eyes=traits["Eyes"].lower(),
            expression=traits["Expression"].lower(),
            special_trait=self.special_traits.get(base_type, "A truly unique cat!")
        )

    def generate_random_traits(self, token_id: int) -> Dict:
        # Select base character
        base = random.choice(self.traits["Base"])
        base_type = base.split()[0]
        
        # Get trait values
        fur_color = random.choice(self.traits["Fur Color"])
        eyes = random.choice(self.traits["Eyes"])
        expression = random.choice(self.traits["Expression"])
        background = random.choice(self.traits["Background"])
        special_effect = random.choice(self.traits["Special Effect"])
        
        # Create traits dict for name/description generation
        trait_dict = {
            "Base": base,
            "Fur Color": fur_color,
            "Eyes": eyes,
            "Expression": expression
        }
        
        # Generate metadata
        metadata = {
            "name": f"CAT#{token_id}",
            "description": self.generate_description(trait_dict),
            "external_url": f"{self.base_url}/{token_id}",
            "image": f"{self.image_base_url}/{token_id}.png",
            "attributes": [
                {"trait_type": "Base", "value": base},
                {"trait_type": "Fur Color", "value": fur_color},
                {"trait_type": "Eyes", "value": eyes},
                {"trait_type": "Expression", "value": expression},
                {"trait_type": "Background", "value": background},
                {"trait_type": "Special Effect", "value": special_effect}
            ]
        }
        
        # Add outfit pieces
        outfit_pieces = self.traits["Outfit"].get(base_type, [])
        for piece in outfit_pieces:
            metadata["attributes"].append({
                "trait_type": "Outfit",
                "value": piece
            })
        
        # Add stats
        metadata["attributes"].extend([
            {
                "display_type": "number",
                "trait_type": "Level",
                "value": random.randint(*self.stat_ranges["Level"])
            },
            {
                "display_type": "boost_number",
                "trait_type": "Energy",
                "value": round(random.uniform(*self.stat_ranges["Energy"]), 1)
            },
            {
                "display_type": "boost_percentage",
                "trait_type": "Creativity",
                "value": random.randint(*self.stat_ranges["Creativity"])
            },
            {
                "display_type": "boost_number",
                "trait_type": "Magic Power",
                "value": random.randint(*self.stat_ranges["Magic Power"])
            },
            {
                "display_type": "boost_percentage",
                "trait_type": "Agility",
                "value": random.randint(*self.stat_ranges["Agility"])
            },
            {
                "display_type": "number",
                "trait_type": "Generation",
                "value": random.randint(*self.stat_ranges["Generation"])
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
