import json
import csv
import os
import glob

def get_attribute_value(attributes, trait_type):
    """Get value for a specific trait type from attributes list"""
    for attr in attributes:
        if attr["trait_type"] == trait_type:
            return attr["value"]
    return ""

def get_outfit_pieces(attributes):
    """Get list of outfit pieces from attributes"""
    outfit_pieces = []
    for attr in attributes:
        if attr["trait_type"] == "Outfit":
            outfit_pieces.append(attr["value"])
    # Pad with empty strings if less than 3 pieces
    while len(outfit_pieces) < 3:
        outfit_pieces.append("")
    return outfit_pieces

def get_stat_value(attributes, trait_type):
    """Get value for a stat attribute"""
    for attr in attributes:
        if attr["trait_type"] == trait_type:
            return str(attr["value"])
    return ""

def compile_metadata_to_csv(metadata_dir, output_file):
    """Compile all metadata JSON files into a single CSV file"""
    # Get all JSON files and sort them numerically
    json_files = glob.glob(os.path.join(metadata_dir, "*.json"))
    json_files.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))
    
    # Prepare CSV headers
    headers = [
        "file_name", "name", "description",
        "attributes[Base]", "attributes[Fur Color]", "attributes[Eyes]",
        "attributes[Expression]", "attributes[Background]", "attributes[Special Effect]",
        "attributes[Outfit]", "attributes[Outfit].1", "attributes[Outfit].2",
        "attributes[Level]", "attributes[Energy]", "attributes[Creativity]",
        "attributes[Magic Power]", "attributes[Agility]", "attributes[Generation]"
    ]
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Write to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        
        # Process each JSON file
        for json_file in json_files:
            token_id = os.path.basename(json_file).split('.')[0]
            
            # Read JSON metadata
            with open(json_file, 'r') as f:
                metadata = json.load(f)
            
            # Get outfit pieces
            outfit_pieces = get_outfit_pieces(metadata.get("attributes", []))
            
            # Create row data
            row = {
                "file_name": f"{token_id}.png",
                "name": metadata.get("name", ""),
                "description": metadata.get("description", ""),
                "attributes[Base]": get_attribute_value(metadata.get("attributes", []), "Base"),
                "attributes[Fur Color]": get_attribute_value(metadata.get("attributes", []), "Fur Color"),
                "attributes[Eyes]": get_attribute_value(metadata.get("attributes", []), "Eyes"),
                "attributes[Expression]": get_attribute_value(metadata.get("attributes", []), "Expression"),
                "attributes[Background]": get_attribute_value(metadata.get("attributes", []), "Background"),
                "attributes[Special Effect]": get_attribute_value(metadata.get("attributes", []), "Special Effect"),
                "attributes[Outfit]": outfit_pieces[0],
                "attributes[Outfit].1": outfit_pieces[1],
                "attributes[Outfit].2": outfit_pieces[2],
                "attributes[Level]": get_stat_value(metadata.get("attributes", []), "Level"),
                "attributes[Energy]": get_stat_value(metadata.get("attributes", []), "Energy"),
                "attributes[Creativity]": get_stat_value(metadata.get("attributes", []), "Creativity"),
                "attributes[Magic Power]": get_stat_value(metadata.get("attributes", []), "Magic Power"),
                "attributes[Agility]": get_stat_value(metadata.get("attributes", []), "Agility"),
                "attributes[Generation]": get_stat_value(metadata.get("attributes", []), "Generation")
            }
            
            # Write row to CSV
            writer.writerow(row)
            print(f"Processed metadata for token #{token_id}")

def main():
    metadata_dir = "metadata"
    output_file = "metadata_csv/compiled_metadata.csv"
    
    print("Starting metadata compilation...")
    compile_metadata_to_csv(metadata_dir, output_file)
    print(f"\nMetadata compilation complete! Output saved to: {output_file}")

if __name__ == "__main__":
    main()
