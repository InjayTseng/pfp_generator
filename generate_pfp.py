import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
from PIL import Image
import io
import json
import base64

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
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        # Create directories if they don't exist
        self.input_dir = Path('input')
        self.output_dir = Path('output')
        self.input_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)

    def generate_image(self, image_path, prompt, negative_prompt="", control_strength=0.8, seed=None):
        """
        Generate an image using the Stability API with ControlNet.
        
        Args:
            image_path (str): Path to the input skeleton image
            prompt (str): Text prompt describing the desired output
            negative_prompt (str): Things to avoid in the generation
            control_strength (float): How strongly the skeleton guides the image
            seed (int): Random seed for reproducibility
        """
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Input image not found: {image_path}")

        # Resize image to 1024x1024
        with Image.open(image_path) as img:
            img = img.convert('RGB')  # Convert to RGB mode
            img = img.resize((1024, 1024), Image.Resampling.LANCZOS)
            
            # Save to bytes
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')

        # Prepare the payload
        payload = {
            "text_prompts": [
                {
                    "text": prompt,
                    "weight": 1.0
                },
                {
                    "text": negative_prompt,
                    "weight": -1.5  # 進一步增加負面提示詞的權重
                }
            ],
            "cfg_scale": 12.0,  # 大幅增加 CFG Scale
            "steps": 50,
            "samples": 1,
            "style_preset": "anime",
            "control_inputs": [
                {
                    "control_type": "pose",
                    "image_base64": img_base64,
                    "weight": control_strength,
                    "guidance_start": 0.0,
                    "guidance_end": 1.0,
                    "control_mode": "balanced"  # 添加控制模式
                }
            ]
        }
        
        if seed is not None:
            payload["seed"] = seed

        # Send request to API
        response = requests.post(
            self.base_url,
            headers=self.headers,
            json=payload
        )

        # Handle the response
        if response.status_code == 200:
            try:
                # Parse the JSON response
                response_json = response.json()
                
                # Get the base64 image data from the response
                if 'artifacts' in response_json and len(response_json['artifacts']) > 0:
                    image_data = response_json['artifacts'][0]['base64']
                    
                    # Decode base64 to binary
                    image_bytes = base64.b64decode(image_data)
                    
                    # Generate output filename with timestamp
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    output_path = self.output_dir / f"generated_pfp_{timestamp}.png"
                    
                    # Save the generated image
                    with open(output_path, "wb") as f:
                        f.write(image_bytes)
                    print(f"Image successfully generated and saved as {output_path}")
                    return output_path
                else:
                    print("No image data found in the response")
                    print(f"Response content: {json.dumps(response_json, indent=2)}")
            except Exception as e:
                print(f"Error processing response: {e}")
                print(f"Raw response: {response.text}")
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None

def main():
    generator = PFPGenerator()
    
    # Example prompts - you can modify these
    prompts = [
        "exact pose only, full body shot, 1girl, follow pose strictly, upper body straight, arms at sides, legs spread apart in A-frame stance, no pose alteration, precise pose matching, anime art style",
        "exact pose only, full body shot, 1boy, follow pose strictly, upper body straight, arms at sides, legs spread apart in A-frame stance, no pose alteration, precise pose matching, urban style",
        "exact pose only, full body shot, 1girl, follow pose strictly, upper body straight, arms at sides, legs spread apart in A-frame stance, no pose alteration, precise pose matching, magical style"
    ]
    
    negative_prompt = "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, wrong pose, distorted pose, deformed pose, different pose, standing straight, alternate pose, inaccurate pose, shifted pose, raised arms, bent body"
    
    # Find all png files in the input directory
    input_files = list(Path('input').glob('*.png'))
    
    if not input_files:
        print("No PNG files found in the input directory!")
        return
    
    # Generate images for each input file with different prompts
    for input_file in input_files:
        for i, prompt in enumerate(prompts):
            print(f"\nGenerating image {i+1} for {input_file.name}...")
            generator.generate_image(
                str(input_file),
                prompt=prompt,
                negative_prompt=negative_prompt,
                control_strength=2.0,  # 進一步提高控制強度
                seed=None  # Random seed for variation
            )

if __name__ == "__main__":
    main()
