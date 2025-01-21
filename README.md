# PFP Generator using Stability.ai API

This project generates profile pictures (PFPs) using the Stability.ai API with ControlNet, based on OpenPose skeleton images.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your Stability API key:
```
STABILITY_API_KEY=your_api_key_here
```

3. Place your OpenPose skeleton image in the `input` directory.

## Usage

Run the generator script:
```bash
python generate_pfp.py
```

Generated images will be saved in the `output` directory.
