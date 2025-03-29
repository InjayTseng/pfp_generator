import json
import os
from generate_pfp import PFPGenerator
import glob

class NFTImageGenerator:
    def __init__(self):
        self.generator = PFPGenerator()
        self.base_prompt = """16x16 pixel art, tiny sprite of a chibi girl chef, wearing a white apron and a big chef hat, standing in a small kitchen with stove and utensils, NES-style, limited color palette, blocky pixels, minimal detail, retro video game sprite, centered composition, low resolution, clear silhouette, cute and simple
no background, transparent background, character only"""


    def traits_to_prompt(self, traits):
        """Convert NFT traits to an image generation prompt optimized for 8-bit pixel art style"""
        # Extract core traits with safe fallbacks
        def get_trait_value(trait_type, default=""):
            try:
                return next(t["value"] for t in traits if t["trait_type"] == trait_type)
            except StopIteration:
                return default
        
        # Get all core traits
        base = get_trait_value("Base", "character")
        fur_color = get_trait_value("Fur Color", "")
        eyes = get_trait_value("Eyes", "")
        expression = get_trait_value("Expression", "neutral")
        background = get_trait_value("Background", "simple")
        special_effect = get_trait_value("Special Effect", "")
        
        # Get outfit pieces
        outfit_pieces = [t["value"] for t in traits if t["trait_type"] == "Outfit"]
        
        # Style-specific descriptors for RPG pixel art characters like in the reference image
        style_descriptors = {
            "fur": {
                "Red": "warm auburn",
                "Blue": "soft blue",
                "Green": "forest green",
                "Yellow": "golden blonde",
                "Purple": "royal purple",
                "Orange": "ginger orange",
                "Pink": "rose pink",
                "White": "light cream",
                "Black": "dark ebony",
                "Brown": "chestnut brown",
                "Gray": "silver gray"
            },
            "eyes": {
                "Big": "large round",
                "Small": "small dot",
                "Round": "simple circle",
                "Narrow": "thin line",
                "Glowing": "bright",
                "Sleepy": "half-closed",
                "Surprised": "wide"
            },
            "expression": {
                "Happy": "cheerful smile",
                "Sad": "slight frown",
                "Angry": "stern look",
                "Surprised": "open mouth",
                "Neutral": "calm expression",
                "Excited": "wide smile",
                "Confused": "puzzled look"
            },
            "background": {
                "Forest": "simple green trees",
                "Space": "starry night",
                "City": "small houses",
                "Beach": "sandy shore",
                "Mountains": "distant peaks",
                "Desert": "sandy dunes",
                "Underwater": "blue waters",
                "Castle": "stone walls",
                "Simple": "plain backdrop"
            },
            "effect": {
                "Glitch": "slight static",
                "Sparkle": "tiny stars",
                "Fire": "small flame",
                "Water": "water droplets",
                "Lightning": "small lightning",
                "Rainbow": "colorful arc",
                "Shadow": "soft shadow",
                "Glow": "gentle glow",
                "None": ""
            },
            "character_type": {
                "Warrior": "stout warrior with small weapon",
                "Mage": "wise wizard with tiny staff",
                "Rogue": "nimble character with small dagger",
                "Knight": "mighty knight with miniature armor",
                "Princess": "fair princess with small crown",
                "Witch": "cunning witch with tiny hat",
                "Cook": "chef with small cooking pot",
                "Scholar": "avid scholar with tiny book",
                "Farmer": "simple farmer with small tool",
                "Pirate": "fearsome pirate with tiny sword",
                "Cat": "one lazy cat with orange fur",
                "Frog": "small green frog"
            },
            "occupation": {
                "Sports": "likes sports",
                "Knight": "mighty knight",
                "Lady": "gentle lady",
                "Wizard": "wise wizard",
                "Scholar": "avid scholar",
                "Princess": "fair princess",
                "Warrior": "stout warrior",
                "Shepherd": "herds sheep",
                "Hero": "saves the day",
                "Witch": "cunning witch",
                "Cook": "cooks",
                "Tech": "tech enthusiast",
                "Alchemist": "alchemist",
                "Woodcutter": "woodcutter",
                "Pirate": "fearsome pirate",
                "Frog": "a frog",
                "Cat": "one lazy cat",
                "Monster": "on the prowl"
            }
        }
        
        # Enhance outfit descriptions to match the simple RPG style
        enhanced_outfit = []
        for outfit in outfit_pieces:
            if "Hat" in outfit:
                enhanced_outfit.append(f"small {outfit}")
            elif "Glasses" in outfit:
                enhanced_outfit.append(f"tiny {outfit}")
            elif "Shirt" in outfit or "Jacket" in outfit:
                enhanced_outfit.append(f"simple {outfit}")
            elif "Pants" in outfit:
                enhanced_outfit.append(f"basic {outfit}")
            elif "Shoes" in outfit or "Boots" in outfit:
                enhanced_outfit.append(f"small {outfit}")
            elif "Accessory" in outfit or "Necklace" in outfit:
                enhanced_outfit.append(f"tiny {outfit}")
            elif "Staff" in outfit or "Wand" in outfit:
                enhanced_outfit.append(f"magical {outfit}")
            elif "Sword" in outfit or "Axe" in outfit or "Weapon" in outfit:
                enhanced_outfit.append(f"miniature {outfit}")
            else:
                enhanced_outfit.append(f"simple {outfit}")
        
        outfit_desc = ", ".join(enhanced_outfit) if enhanced_outfit else ""
        
        # Get enhanced descriptions from style dictionaries
        fur_desc = style_descriptors["fur"].get(fur_color, f"{fur_color} pixelated") if fur_color else ""
        eyes_desc = style_descriptors["eyes"].get(eyes, f"{eyes} pixel") if eyes else ""
        expression_desc = style_descriptors["expression"].get(expression, f"{expression} pixel") if expression else ""
        background_desc = style_descriptors["background"].get(background, f"{background} pixel") if background else ""
        effect_desc = style_descriptors["effect"].get(special_effect, f"{special_effect} pixel") if special_effect else ""
        
        # Get character type and occupation descriptions
        character_type_desc = style_descriptors["character_type"].get(base, f"{base}") if base else ""
        occupation_desc = style_descriptors["occupation"].get(base, "") if base else ""
        
        # Build the prompt with enhanced descriptions
        prompt_parts = [self.base_prompt]
        
        # Add character base with type
        prompt_parts.append(f"{character_type_desc}")
        
        # Add name and caption
        name = get_trait_value("Name", base)
        caption = occupation_desc if occupation_desc else f"a {base}"
        prompt_parts.append(f"named {name}")
        prompt_parts.append(f"caption: '{name}, {caption}'")
        
        # Add fur color if present
        if fur_desc:
            prompt_parts.append(f"{fur_desc} hair")
        
        # Add eyes if present
        if eyes_desc:
            prompt_parts.append(f"{eyes_desc} eyes")
        
        # Add expression if present
        if expression_desc:
            prompt_parts.append(f"{expression_desc}")
        
        # Add outfit if present
        if outfit_desc:
            prompt_parts.append(outfit_desc)
        
        # Add background if present
        if background_desc:
            prompt_parts.append(f"{background_desc} background")
        
        # Add special effect if present
        if effect_desc:
            prompt_parts.append(f"{effect_desc}")
        
        # Join all parts with commas
        prompt = ", ".join(prompt_parts)
        
        return prompt

    def generate_from_metadata_files(self, metadata_dir: str, output_dir: str):
        """Generate images from individual metadata JSON files"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Get all metadata files and sort them by number
        metadata_files = glob.glob(os.path.join(metadata_dir, "*.json"))
        metadata_files.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))
        
        # Process each metadata file
        for metadata_file in metadata_files:
            # Get token ID from filename (e.g., "1.json" -> "1")
            token_id = os.path.basename(metadata_file).split('.')[0]
            output_path = os.path.join(output_dir, f"{token_id}.png")
            
            print(f"\nProcessing NFT #{token_id}...")
            
            # Load metadata from file
            with open(metadata_file, 'r') as f:
                nft = json.load(f)
            
            print(f"Character: {next(t['value'] for t in nft['attributes'] if t['trait_type'] == 'Base')}")
            
            # Convert traits to prompt
            prompt = self.traits_to_prompt(nft["attributes"])
            
            # Generate image
            self.generator.generate_image(
                prompt=prompt,
                negative_prompt="""realistic, detailed, professional, clean lines, proper anatomy,
                correct proportions, sophisticated, mature style, complex shading, perfect symmetry,
                photorealistic, refined artwork, advanced technique, adult art style, dog, human""",
                seed=int(token_id)  # Use token_id as seed for reproducibility
            )
            
            # Rename the generated file to match token_id
            latest_file = max(glob.glob(os.path.join("output", "*.png")), key=os.path.getctime)
            os.rename(latest_file, output_path)
            
            print(f"Generated image saved as {output_path}")

def main():
    generator = NFTImageGenerator()
    
    # Input and output paths
    metadata_dir = "metadata"
    output_dir = "nft_images"
    
    # Generate images from metadata files
    generator.generate_from_metadata_files(metadata_dir, output_dir)
    
    print("\nFinished generating all NFT images!")

if __name__ == "__main__":
    main()
