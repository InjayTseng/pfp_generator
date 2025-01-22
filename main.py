import os
import time
from nft_traits import NFTTraitGenerator
from generate_nft_images import NFTImageGenerator
from compile_metadata_csv import compile_metadata_to_csv

class NFTGenerationPipeline:
    def __init__(self):
        self.trait_generator = NFTTraitGenerator()
        self.image_generator = NFTImageGenerator()
        
        # Create necessary directories
        self.directories = {
            "metadata": "metadata",
            "images": "nft_images",
            "csv": "metadata_csv"
        }
        
        for dir_path in self.directories.values():
            os.makedirs(dir_path, exist_ok=True)
    
    def generate_traits_and_metadata(self, start_id=1, count=10):
        """Step 1: Generate NFT traits and metadata"""
        print("\n=== Step 1: Generating NFT Traits and Metadata ===")
        
        # Generate batch of NFTs
        batch_nfts = self.trait_generator.generate_batch(start_id, count)
        
        # Save individual metadata files
        self.trait_generator.save_metadata(batch_nfts, self.directories["metadata"])
        
        print(f"✓ Generated {count} NFT metadata files")
        return batch_nfts
    
    def generate_nft_images(self):
        """Step 2: Generate NFT images from metadata"""
        print("\n=== Step 2: Generating NFT Images ===")
        
        # Generate images from metadata
        self.image_generator.generate_from_metadata_files(
            self.directories["metadata"],
            self.directories["images"]
        )
        
        print("✓ Generated NFT images")
    
    def compile_metadata_csv(self):
        """Step 3 (Optional): Compile metadata into CSV"""
        print("\n=== Step 3: Compiling Metadata CSV ===")
        
        output_file = os.path.join(self.directories["csv"], "compiled_metadata.csv")
        compile_metadata_to_csv(self.directories["metadata"], output_file)
        
        print("✓ Compiled metadata CSV")

def main():
    # Initialize the pipeline
    pipeline = NFTGenerationPipeline()
    
    # Configuration
    start_id = 1  # Starting token ID
    nft_count = 10  # Number of NFTs to generate
    
    # Record start time
    start_time = time.time()
    
    try:
        # Step 1: Generate traits and metadata
        pipeline.generate_traits_and_metadata(start_id, nft_count)
        
        # Step 2: Generate NFT images
        pipeline.generate_nft_images()
        
        # Step 3 (Optional): Compile metadata CSV
        pipeline.compile_metadata_csv()
        
        # Calculate total time
        total_time = time.time() - start_time
        
        print("\n=== NFT Generation Complete! ===")
        print(f"Total time: {total_time:.2f} seconds")
        print(f"Generated {nft_count} NFTs")
        print("\nOutput directories:")
        print(f"- Metadata: {pipeline.directories['metadata']}/")
        print(f"- Images: {pipeline.directories['images']}/")
        print(f"- CSV: {pipeline.directories['csv']}/")
        
    except Exception as e:
        print(f"\n❌ Error during NFT generation: {str(e)}")
        raise

if __name__ == "__main__":
    main()
