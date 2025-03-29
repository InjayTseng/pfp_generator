import json
import os
from generate_pfp import PFPGenerator
from config import BASE_PROMPTS, CHARACTER_TYPES, COMMON_TRAITS

class SimplifiedImageGenerator:
    def __init__(self, style="pixel_rpg"):
        self.generator = PFPGenerator()
        self.style = style
        self.base_prompt = BASE_PROMPTS[style]["prompt"]
        self.negative_prompt = BASE_PROMPTS[style]["negative_prompt"]
    
    def set_style(self, style):
        """Change the base prompt style"""
        if style in BASE_PROMPTS:
            self.style = style
            self.base_prompt = BASE_PROMPTS[style]["prompt"]
            self.negative_prompt = BASE_PROMPTS[style]["negative_prompt"]
            return True
        return False
    
    def traits_to_prompt(self, traits):
        """Convert NFT traits to an image generation prompt"""
        # Extract core traits with safe fallbacks
        def get_trait_value(trait_type, default=""):
            try:
                return next(t["value"] for t in traits if t["trait_type"] == trait_type)
            except StopIteration:
                return default
        
        # Get all core traits
        base = get_trait_value("Base", "character")
        name = get_trait_value("Name", "")
        hair_color = get_trait_value("Hair Color", "")
        eyes = get_trait_value("Eyes", "")
        expression = get_trait_value("Expression", "neutral")
        background = get_trait_value("Background", "simple")
        special_effect = get_trait_value("Special Effect", "")
        
        # Get outfit pieces
        outfit_pieces = [t["value"] for t in traits if t["trait_type"] == "Outfit"]
        
        # Get character description from config
        character_desc = CHARACTER_TYPES.get(base, {}).get("description", f"{base}")
        
        # Build the prompt
        prompt_parts = [self.base_prompt]
        
        # Add character base description
        prompt_parts.append(f"{character_desc}")
        
        # Add name if present
        if name:
            prompt_parts.append(f"named {name}")
        
        # Add hair color if present
        if hair_color:
            prompt_parts.append(f"{hair_color.lower()} hair")
        
        # Add eyes if present
        if eyes:
            prompt_parts.append(f"{eyes.lower()} eyes")
        
        # Add expression if present
        if expression:
            prompt_parts.append(f"{expression.lower()} expression")
        
        # Add outfit pieces if present
        if outfit_pieces:
            outfit_desc = ", ".join([f"small {piece.lower()}" for piece in outfit_pieces if piece != "None"])
            if outfit_desc:
                prompt_parts.append(outfit_desc)
        
        # Add background if present and not 'Simple'
        if background and background != "Simple":
            prompt_parts.append(f"{background.lower()} background")
        
        # Add special effect if present and not 'None'
        if special_effect and special_effect != "None":
            prompt_parts.append(f"{special_effect.lower()} effect")
        
        # Join all parts with commas
        prompt = ", ".join(prompt_parts)
        
        return prompt
    
    def generate_from_metadata_files(self, metadata_dir, output_dir):
        """Generate images from individual metadata JSON files"""
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Get all JSON files in the metadata directory
        metadata_files = [f for f in os.listdir(metadata_dir) if f.endswith('.json')]
        
        for file_name in sorted(metadata_files, key=lambda x: int(x.split('.')[0])):
            token_id = int(file_name.split('.')[0])
            file_path = os.path.join(metadata_dir, file_name)
            
            # Load metadata
            with open(file_path, 'r') as f:
                metadata = json.load(f)
            
            print(f"\nProcessing NFT #{token_id}...")
            
            # Get character type for logging
            character_type = next((attr["value"] for attr in metadata["attributes"] 
                                if attr["trait_type"] == "Base"), "Unknown")
            print(f"Character: {character_type}")
            
            # Generate prompt from traits
            prompt = self.traits_to_prompt(metadata["attributes"])
            
            # Generate image
            output_path = self.generator.generate_image(
                prompt=prompt,
                negative_prompt=self.negative_prompt,
                seed=None  # Random seed
            )
            
            if output_path:
                # Copy to the NFT images directory with the token ID as filename
                output_file = os.path.join(output_dir, f"{token_id}.png")
                
                # Use the returned path from generate_image
                import shutil
                shutil.copy(output_path, output_file)
                print(f"Generated image saved as {output_file}")
