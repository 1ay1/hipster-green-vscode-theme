#!/usr/bin/env python3
"""Generate soothing theme variants with muted colors"""

import json
import re

def remove_json_comments(text):
    """Remove // comments and /* */ from JSON"""
    # Remove /* */ comments
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    # Remove // comments
    text = re.sub(r'//.*?$', '', text, flags=re.MULTILINE)
    return text

def load_json_with_comments(filepath):
    """Load JSON file that may contain comments"""
    with open(filepath, 'r') as f:
        content = f.read()
    content = remove_json_comments(content)
    return json.loads(content)

def create_soothing_green():
    theme = load_json_with_comments('themes/hipster-green-color-theme.json')
    
    theme['name'] = 'Hipster Green Soothing'
    
    # Adjust key colors to be more muted
    color_map = {
        '#84c138': '#6b9f48',  # Primary green - more muted
        '#23ff18': '#4db84d',  # Bright green - much softer
        '#00a600': '#4d994d',  # Vivid green - softer
        '#00a6b2': '#5a9ba5',  # Cyan - muted
        '#e5e500': '#b8b85a',  # Yellow - much softer
        '#b200b2': '#9a5a9a',  # Magenta - softer
        '#e50000': '#cc5555',  # Red - less harsh
        '#86a93e': '#7a9658',  # Olive - slightly muted
        '#5a6a50': '#6b7a65',  # Comment green - lighter
    }
    
    # Apply color mappings
    theme_str = json.dumps(theme)
    for old, new in color_map.items():
        theme_str = theme_str.replace(old, new)
    
    theme = json.loads(theme_str)
    
    with open('themes/hipster-green-soothing-theme.json', 'w') as f:
        json.dump(theme, f, indent=2)
    
    print("✓ Created Hipster Green Soothing")

def create_soothing_blue():
    theme = load_json_with_comments('themes/hipster-blue-dark-theme.json')
    
    theme['name'] = 'Hipster Blue Soothing'
    
    color_map = {
        '#42a5f5': '#6b9fc4',  # Primary blue - muted
        '#2196f3': '#5a99cc',  # Bright blue - softer
        '#26c6da': '#5da5b5',  # Cyan - muted
        '#1976d2': '#5a7fa5',  # Blue - softer
        '#0d47a1': '#3a5a7a',  # Dark blue - warmer
    }
    
    theme_str = json.dumps(theme)
    for old, new in color_map.items():
        theme_str = theme_str.replace(old, new)
    
    theme = json.loads(theme_str)
    
    with open('themes/hipster-blue-soothing-theme.json', 'w') as f:
        json.dump(theme, f, indent=2)
    
    print("✓ Created Hipster Blue Soothing")

def create_soothing_ocean():
    """Create a new ocean/teal soothing theme"""
    theme = load_json_with_comments('themes/hipster-green-color-theme.json')
    
    theme['name'] = 'Hipster Ocean Soothing'
    
    # Ocean/teal color palette - very soothing
    color_map = {
        '#84c138': '#5a9a96',  # Teal
        '#23ff18': '#6db8b4',  # Bright teal
        '#00a600': '#569f9b',  # Green-teal
        '#00a6b2': '#5a9fa5',  # Cyan
        '#e5e500': '#b8b08a',  # Sandy yellow
        '#b200b2': '#8a7a9a',  # Muted purple
        '#e50000': '#b86a6a',  # Soft red
        '#86a93e': '#7a9a8a',  # Sage
        '#5a6a50': '#6b7a7a',  # Gray-green
        '#100a05': '#0f1416',  # Dark teal bg
        '#1a1510': '#151a1c',  # Slightly lighter bg
        '#0d0905': '#0d1214',  # Panel bg
        '#083905': '#1a3a3a',  # Borders/accents
    }
    
    theme_str = json.dumps(theme)
    for old, new in color_map.items():
        theme_str = theme_str.replace(old, new)
    
    theme = json.loads(theme_str)
    
    with open('themes/hipster-ocean-soothing-theme.json', 'w') as f:
        json.dump(theme, f, indent=2)
    
    print("✓ Created Hipster Ocean Soothing")

def create_forest_theme():
    """Create forest/nature soothing theme"""
    theme = load_json_with_comments('themes/hipster-green-color-theme.json')
    
    theme['name'] = 'Hipster Forest Soothing'
    
    # Forest colors - deep greens and earth tones
    color_map = {
        '#84c138': '#7a9a6b',  # Forest green
        '#23ff18': '#8fb87a',  # Lighter forest
        '#00a600': '#6b9f6b',  # Medium green
        '#00a6b2': '#6b9a9a',  # Blue-green
        '#e5e500': '#b8a86b',  # Earth yellow
        '#b200b2': '#9a7a8a',  # Muted purple
        '#e50000': '#b86b6b',  # Terra cotta
        '#86a93e': '#8a9a7a',  # Sage
        '#5a6a50': '#6b7a6b',  # Moss
        '#100a05': '#0f120e',  # Deep forest bg
        '#1a1510': '#151a16',  # Dark earth bg
        '#0d0905': '#0d110e',  # Panel bg
        '#083905': '#2a3a2a',  # Forest accent
    }
    
    theme_str = json.dumps(theme)
    for old, new in color_map.items():
        theme_str = theme_str.replace(old, new)
    
    theme = json.loads(theme_str)
    
    with open('themes/hipster-forest-soothing-theme.json', 'w') as f:
        json.dump(theme, f, indent=2)
    
    print("✓ Created Hipster Forest Soothing")

if __name__ == '__main__':
    create_soothing_green()
    create_soothing_blue()
    create_soothing_ocean()
    create_forest_theme()
    print("\n✨ All soothing variants created!")
