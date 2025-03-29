import os
import time
import argparse
from simplified_trait_generator import SimplifiedTraitGenerator
from simplified_image_generator import SimplifiedImageGenerator
from compile_metadata_csv import compile_metadata_to_csv

class SimplifiedNFTGenerator:
    def __init__(self, style="pixel_rpg"):
        self.trait_generator = SimplifiedTraitGenerator()
        self.image_generator = SimplifiedImageGenerator(style=style)
        
        # Create necessary directories
        self.directories = {
            "metadata": "metadata",
            "images": "nft_images",
            "csv": "metadata_csv"
        }
        
        for dir_path in self.directories.values():
            os.makedirs(dir_path, exist_ok=True)
    
    def generate_nfts(self, start_id=1, count=10):
        """Generate NFTs with traits, metadata, and images"""
        print("\n=== Step 1: Generating NFT Traits and Metadata ===")
        batch_nfts = self.trait_generator.generate_batch(start_id, count)
        self.trait_generator.save_metadata(batch_nfts, self.directories["metadata"])
        print(f"✓ Generated {count} NFT metadata files")
        
        print("\n=== Step 2: Generating NFT Images ===")
        self.image_generator.generate_from_metadata_files(
            self.directories["metadata"],
            self.directories["images"]
        )
        print("✓ Generated NFT images")
        
        print("\n=== Step 3: Compiling Metadata CSV ===")
        output_file = os.path.join(self.directories["csv"], "compiled_metadata.csv")
        compile_metadata_to_csv(self.directories["metadata"], output_file)
        print("✓ Compiled metadata CSV")
        
        return batch_nfts

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate pixel art NFTs with simplified configuration")
    parser.add_argument(
        "--style", 
        type=str, 
        default="pixel_rpg",
        choices=["pixel_rpg", "tiny_sprite", "chibi"],
        help="Style of pixel art to generate"
    )
    parser.add_argument(
        "--count", 
        type=int, 
        default=10,
        help="Number of NFTs to generate"
    )
    parser.add_argument(
        "--start-id", 
        type=int, 
        default=1,
        help="Starting token ID"
    )
    
    args = parser.parse_args()
    
    # Initialize the generator with the specified style
    generator = SimplifiedNFTGenerator(style=args.style)
    
    # Record start time
    start_time = time.time()
    
    try:
        # Generate NFTs
        generator.generate_nfts(args.start_id, args.count)
        
        # Calculate total time
        total_time = time.time() - start_time
        
        print("\n=== NFT Generation Complete! ===")
        print(f"Total time: {total_time:.2f} seconds")
        print(f"Generated {args.count} NFTs")
        print(f"Style: {args.style}")
        print("\nOutput directories:")
        print(f"- Metadata: {generator.directories['metadata']}/")
        print(f"- Images: {generator.directories['images']}/")
        print(f"- CSV: {generator.directories['csv']}/")
        
    except Exception as e:
        print(f"\n❌ Error during NFT generation: {str(e)}")
        raise

if __name__ == "__main__":
    main()
