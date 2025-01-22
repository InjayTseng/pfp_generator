import json
import os
from generate_pfp import PFPGenerator
import glob

class NFTImageGenerator:
    def __init__(self):
        self.generator = PFPGenerator()
        self.base_prompt = """ draw like a 5-year-old, kindergarten art, simple crayon art,
        basic shapes, thick lines and strokes, solid colors, minimal background,
        cute and playful, childlike style, simple cat face,
        clear focal point, centered composition, happy cat,
        construction paper texture, primary colors"""

    def traits_to_prompt(self, traits):
        """Convert NFT traits to an image generation prompt"""
        # Extract core traits
        base = next(t["value"] for t in traits if t["trait_type"] == "Base")
        fur_color = next(t["value"] for t in traits if t["trait_type"] == "Fur Color")
        eyes = next(t["value"] for t in traits if t["trait_type"] == "Eyes")
        expression = next(t["value"] for t in traits if t["trait_type"] == "Expression")
        background = next(t["value"] for t in traits if t["trait_type"] == "Background")
        special_effect = next(t["value"] for t in traits if t["trait_type"] == "Special Effect")
        
        # Get outfit pieces
        outfit_pieces = [t["value"] for t in traits if t["trait_type"] == "Outfit"]
        outfit_desc = ", ".join(outfit_pieces) if outfit_pieces else ""
        
        # Construct the prompt
        prompt = f"{self.base_prompt}, {base}, {fur_color} fur, {eyes} eyes, {expression} expression"
        
        if outfit_desc:
            prompt += f", {outfit_desc}"
            
        prompt += f", {background} background, {special_effect} effect"
        
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
