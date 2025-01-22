# PFP Generator - NFT Collection Generator

A Python-based NFT (Non-Fungible Token) collection generator that creates whimsical cat characters with various traits and attributes. The project includes tools for generating NFT metadata, creating images using AI, and compiling metadata into CSV format.

## Features

- Generate unique NFT traits and metadata
- Create AI-generated images based on metadata
- Compile metadata into CSV format for easy analysis
- Support for various character attributes:
  - Base character type
  - Fur color
  - Eyes
  - Expression
  - Background
  - Special effects
  - Outfits
  - Stats (Level, Energy, Creativity, Magic Power, Agility)

## Project Structure

```
pfp_generator/
├── main.py                 # Main script to run the entire pipeline
├── nft_traits.py          # NFT trait generation logic
├── generate_pfp.py        # AI image generation using Stable Diffusion
├── generate_nft_images.py # NFT image generation from metadata
├── compile_metadata_csv.py # Metadata CSV compiler
├── metadata/              # Generated NFT metadata JSON files
├── nft_images/           # Generated NFT images
└── metadata_csv/         # Compiled metadata CSV files
```

## Requirements

- Python 3.x
- Required Python packages:
  - requests
  - Pillow
  - pandas

## Usage

1. Run the entire pipeline:
```bash
python3 main.py
```

This will:
- Generate NFT traits and metadata
- Create NFT images
- Compile metadata into CSV format

2. Configure the number of NFTs:
- Open `main.py`
- Modify the `nft_count` variable (default: 10)

## Output

The generator creates three main directories:

1. `metadata/`: Contains individual JSON files for each NFT with their traits and attributes
2. `nft_images/`: Contains the generated NFT images
3. `metadata_csv/`: Contains the compiled metadata in CSV format

## Metadata Format

Each NFT includes:
- Name
- Description
- Image URL
- Attributes:
  - Base traits (character type)
  - Visual traits (fur color, eyes, expression)
  - Special traits (background, effects)
  - Multiple outfit pieces
  - Character stats

## CSV Format

The compiled CSV includes columns for:
- File name
- NFT name
- Description
- All attributes in separate columns
- Character stats

## Contributing

Feel free to submit issues and enhancement requests!

## License

[MIT License](LICENSE)
