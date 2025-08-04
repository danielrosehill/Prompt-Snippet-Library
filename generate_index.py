#!/usr/bin/env python3
"""
Generate an alphabetical index of prompt snippets with LLM-generated descriptions.
"""

import os
import json
import subprocess
from pathlib import Path

def get_snippet_files():
    """Find all markdown files containing snippets."""
    snippets = []
    base_path = Path(".")
    
    # Skip README.md and any files in .git
    for md_file in base_path.rglob("*.md"):
        if md_file.name != "README.md" and ".git" not in str(md_file):
            snippets.append(md_file)
    
    return sorted(snippets)

def read_snippet_content(file_path):
    """Read the content of a snippet file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_description(snippet_name, content):
    """Generate a one-sentence description using Ollama."""
    prompt = f"""You are tasked with creating a one-sentence description for a prompt snippet called "{snippet_name}".

Here is the content of the snippet:

{content}

Create a concise, one-sentence description that explains what this prompt snippet does and when to use it. Focus on the practical purpose and benefit. Do not include the snippet name in the description.

Response format: Just the one sentence, no additional text."""

    try:
        # Use Ollama with llama3.2
        result = subprocess.run([
            'ollama', 'run', 'llama3.2', prompt
        ], capture_output=True, text=True, timeout=20)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Error generating description for {snippet_name}: {result.stderr}")
            return "Prompt snippet for AI workflow enhancement."
    
    except subprocess.TimeoutExpired:
        print(f"Timeout generating description for {snippet_name}")
        return "Prompt snippet for AI workflow enhancement."
    except Exception as e:
        print(f"Error with {snippet_name}: {e}")
        return "Prompt snippet for AI workflow enhancement."

def format_snippet_name(file_path):
    """Convert file path to readable snippet name."""
    name = file_path.stem.replace('-', ' ').replace('_', ' ')
    return name.title()

def main():
    print("Generating prompt snippet index...")
    
    snippets = get_snippet_files()
    index_entries = []
    
    for snippet_file in snippets:
        print(f"Processing: {snippet_file}")
        
        snippet_name = format_snippet_name(snippet_file)
        content = read_snippet_content(snippet_file)
        description = generate_description(snippet_name, content)
        
        index_entries.append({
            'name': snippet_name,
            'file': str(snippet_file),
            'description': description
        })
    
    # Sort alphabetically by name
    index_entries.sort(key=lambda x: x['name'])
    
    # Generate markdown index
    print("\n## Alphabetical Index\n")
    for entry in index_entries:
        print(f"- **{entry['name']}** - {entry['description']}")
    
    print(f"\nGenerated index for {len(index_entries)} snippets.")

if __name__ == "__main__":
    main()
