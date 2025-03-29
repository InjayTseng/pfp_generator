import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import base64
import json
import random

# Load environment variables
load_dotenv()

class PFPGenerator:
    def __init__(self):
        self.api_key = os.getenv('STABILITY_API_KEY')
        if not self.api_key:
            raise ValueError("Please set STABILITY_API_KEY in your .env file")
        
        self.base_url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        # Create directories if they don't exist
        self.output_dir = Path('output')
        self.output_dir.mkdir(exist_ok=True)

    def generate_image(self, prompt="", negative_prompt="", seed=None):
        """
        Generate an image using the Stability API with text-to-image.
        
        Args:
            prompt (str): Text prompt describing the desired output
            negative_prompt (str): Things to avoid in the generation
            seed (int): Random seed for reproducibility
            
        Returns:
            str: Path to the generated image file, or None if generation failed
        """
        payload = {
            "steps": 50,
            "width": 1024,
            "height": 1024,
            "seed": seed if seed is not None else random.randint(0, 4294967295),
            "cfg_scale": 7.5,
            "samples": 1,
            "text_prompts": [
                {
                    "text": prompt,
                    "weight": 1
                },
                {
                    "text": negative_prompt,
                    "weight": -1
                }
            ],
            "style_preset": "pixel-art"  # Corrected to pixel-art (with hyphen) for better results
        }

        try:
            # Make the API request
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload
            )

            # Handle the response
            if response.status_code == 200:
                response_json = response.json()
                if 'artifacts' in response_json and len(response_json['artifacts']) > 0:
                    # Get the base64 image data
                    image_data = response_json['artifacts'][0]['base64']
                    image_bytes = base64.b64decode(image_data)
                    
                    # Generate output filename with timestamp
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    output_file = self.output_dir / f"generated_pfp_{timestamp}.png"
                    
                    # Save the generated image
                    with open(output_file, "wb") as f:
                        f.write(image_bytes)
                    print(f"Image successfully generated and saved as {output_file}")
                    
                    # Return the path to the generated image
                    return str(output_file)
                else:
                    print("No image data found in response")
                    print(f"Response content: {json.dumps(response_json, indent=2)}")
                    return None
            else:
                print(f"Error: {response.status_code}")
                print(f"Response: {response.text}")
                return None

        except Exception as e:
            print(f"Error processing request: {e}")
            return None


def main():
    generator = PFPGenerator()
    
    base_prompt = """child's drawing, crayon art style, kindergarten art, simple shapes,
    wobbly lines, bright primary colors, uneven coloring, scribbled background,
    basic shapes, imperfect proportions, cute and playful, childlike imagination,
    construction paper texture, messy coloring outside lines, simple cat face,
    colorful and cheerful, hand-drawn by 5 year old, cat character, kitty"""
    
    # Random whimsical cat characters in child's drawing style
    character_styles = [
        f"{base_prompt}, space explorer cat, astronaut helmet, star pattern spacesuit, floating in space, planet earth behind, shooting stars, moon and planets, happy whiskers, round eyes full of wonder",
        
        f"{base_prompt}, princess cat, sparkly pink crown, fluffy tutu dress, magic wand with ribbon, castle in background, hearts floating around, rainbow trail, long eyelashes, royal pose",
        
        f"{base_prompt}, pirate kitty, eye patch, striped sailor shirt, captain's hat with skull, treasure map in paws, parrot friend, ship wheel, ocean waves, island with X marks the spot",
        
        f"{base_prompt}, chef cat, big white hat, red and white apron, holding wooden spoon, kitchen background, floating cookies, cake and cupcakes, sprinkles everywhere, happy cooking face",
        
        f"{base_prompt}, superhero cat, rainbow cape flowing, star mask, lightning bolt on chest, saving the day, city skyline, speech bubble with meow, clouds shaped like fish",
        
        f"{base_prompt}, artist cat, paint-splattered fur, beret hat, holding paintbrush, colorful palette, easel with painting, rainbow paint splatters, inspired expression",
        
        f"{base_prompt}, wizard cat, pointy hat with moons, magic spell book, glowing wand, sparkly potion bottles, floating fish, magical swirls, starry background",
        
        f"{base_prompt}, rock star cat, spiky collar, electric guitar, rainbow mohawk, music notes floating, stage lights, microphone stand, star-shaped sunglasses"
    ]
    
    negative_prompt = """realistic, detailed, professional, clean lines, proper anatomy,
    correct proportions, sophisticated, mature style, complex shading, perfect symmetry,
    photorealistic, refined artwork, advanced technique, adult art style, dog, human"""
    
    # Generate all character variations with random seeds for more uniqueness
    import random
    for i, prompt in enumerate(character_styles):
        print(f"\nGenerating character {i+1}...")
        generator.generate_image(
            prompt=prompt,
            negative_prompt=negative_prompt,
            seed=random.randint(1, 999999)  # Random seed for each generation
        )

if __name__ == "__main__":
    main()
