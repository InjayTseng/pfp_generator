import random
import json
import os
from typing import Dict, List, Any
from config import CHARACTER_TYPES, COMMON_TRAITS, RPG_STATS, DESCRIPTION_TEMPLATES

class SimplifiedTraitGenerator:
    def __init__(self):
        # Collection info
        self.collection_name = "Pixel Heroes"
        self.base_url = "https://pixelheroes.io"
        self.image_base_url = "https://storage.pixelheroes.io/images"
        
        # Load configuration from config.py
        self.character_types = CHARACTER_TYPES
        self.common_traits = COMMON_TRAITS
        self.stat_ranges = RPG_STATS
        self.description_templates = DESCRIPTION_TEMPLATES
    
    def generate_name(self) -> str:
        """Generate a name from the predefined list"""
        return random.choice(self.common_traits["Name"])
    
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
            special_trait=self.character_types[base_type]["special_trait"]
        )
    
    def generate_random_traits(self, token_id: int) -> Dict:
        """Generate random traits for a character"""
        # Select base character type
        base = random.choice(list(self.character_types.keys()))
        
        # Get character name
        name = self.generate_name()
        
        # Get trait values
        hair_color = random.choice(self.common_traits["Hair Color"])
        eyes = random.choice(self.common_traits["Eyes"])
        expression = random.choice(self.common_traits["Expression"])
        background = random.choice(self.common_traits["Background"])
        special_effect = random.choice(self.common_traits["Special Effect"])
        
        # Create traits dict for description generation
        trait_dict = {
            "Base": base,
            "Name": name,
            "Hair Color": hair_color,
            "Eyes": eyes,
            "Expression": expression
        }
        
        # Get character description from config
        character_desc = self.character_types[base]["description"]
        
        # Generate metadata
        metadata = {
            "name": f"{name}",
            "description": self.generate_description(trait_dict),
            "external_url": f"{self.base_url}/{token_id}",
            "image": f"{self.image_base_url}/{token_id}.png",
            "attributes": [
                {"trait_type": "Base", "value": base},
                {"trait_type": "Name", "value": name},
                {"trait_type": "Description", "value": character_desc},
                {"trait_type": "Hair Color", "value": hair_color},
                {"trait_type": "Eyes", "value": eyes},
                {"trait_type": "Expression", "value": expression},
                {"trait_type": "Background", "value": background},
                {"trait_type": "Special Effect", "value": special_effect}
            ]
        }
        
        # Add outfit pieces
        outfit_pieces = self.character_types[base]["outfit"]
        for piece in outfit_pieces:
            if piece != "None":
                metadata["attributes"].append({
                    "trait_type": "Outfit",
                    "value": piece
                })
        
        # Add RPG stats
        for stat_name, stat_range in self.stat_ranges.items():
            metadata["attributes"].append({
                "display_type": "number",
                "trait_type": stat_name,
                "value": random.randint(*stat_range)
            })
        
        return metadata
    
    def generate_batch(self, start_id: int, count: int) -> List[Dict]:
        """Generate a batch of NFT metadata"""
        batch = []
        for i in range(count):
            token_id = start_id + i
            metadata = self.generate_random_traits(token_id)
            metadata["token_id"] = token_id
            batch.append(metadata)
        return batch
    
    def save_metadata(self, batch: List[Dict], output_dir: str) -> None:
        """Save metadata to individual JSON files"""
        os.makedirs(output_dir, exist_ok=True)
        
        for item in batch:
            token_id = item["token_id"]
            file_path = os.path.join(output_dir, f"{token_id}.json")
            
            # Create a copy without the token_id field for the actual metadata file
            metadata = item.copy()
            metadata.pop("token_id", None)
            
            with open(file_path, "w") as f:
                json.dump(metadata, f, indent=2)
