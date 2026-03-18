#!/usr/bin/env python3
"""
Organize cybersecurity skills into categories based on subdomain.

This script:
1. Traverses /skills/ folder recursively to find all SKILL.md files
2. Parses YAML frontmatter from each file to extract metadata:
   - name, description, domain, subdomain, tags
3. Groups all skills by their 'subdomain' to create categories
4. Generates Markdown files in /categories/ for each category
5. Updates README.md with a categories table with download links
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple
import urllib.parse


def parse_skill_metadata(skill_path: Path) -> Dict | None:
    """
    Parse YAML frontmatter from SKILL.md file.
    
    Returns: Dict with skill metadata or None if parsing fails
    """
    try:
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter between --- markers
        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return None
        
        frontmatter = match.group(1)
        metadata = {}
        
        # Parse YAML-like format (simple key-value extraction)
        # Handle multi-line strings like: description: >- ... 
        lines = frontmatter.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # Handle multi-line YAML values (>-, |-, >|)
                if value in ('>', '>-', '|', '|-', '>|'):
                    # Collect the multi-line value
                    i += 1
                    value_lines = []
                    while i < len(lines):
                        next_line = lines[i]
                        # Stop if we hit another key or empty line followed by a key
                        if next_line.strip() and ':' in next_line and not next_line.startswith(' '):
                            break
                        if next_line.strip():
                            # Remove leading spaces (YAML indentation)
                            value_lines.append(next_line.strip())
                        i += 1
                    value = ' '.join(value_lines)
                    i -= 1
                
                # Handle tags specially - extract from list format
                if key == 'tags':
                    # Extract tags from list format: [tag1, tag2, tag3]
                    tags = re.findall(r'\w+', value)
                    metadata[key] = tags
                else:
                    # Remove quotes
                    value = value.strip('\'"')
                    metadata[key] = value
            
            i += 1
        
        return metadata if 'subdomain' in metadata else None
    
    except Exception as e:
        print(f"  ⚠️  Error parsing {skill_path}: {e}")
        return None


def collect_skills() -> Dict[str, List[Tuple[str, Dict]]]:
    """
    Traverse skills directory and collect all skill metadata.
    
    Returns: Dict mapping subdomain -> list of (skill_name, metadata) tuples
    """
    skills_dir = Path(__file__).parent / 'skills'
    skills_by_subdomain = {}
    
    print(f"📂 Scanning skills directory: {skills_dir}")
    
    for skill_folder in sorted(skills_dir.iterdir()):
        if not skill_folder.is_dir():
            continue
        
        skill_path = skill_folder / 'SKILL.md'
        if not skill_path.exists():
            print(f"  ⚠️  No SKILL.md found in {skill_folder.name}")
            continue
        
        metadata = parse_skill_metadata(skill_path)
        if not metadata:
            print(f"  ⚠️  Could not parse {skill_folder.name}")
            continue
        
        skill_name = metadata.get('name', skill_folder.name)
        subdomain = metadata.get('subdomain', 'uncategorized').lower()
        
        if subdomain not in skills_by_subdomain:
            skills_by_subdomain[subdomain] = []
        
        skills_by_subdomain[subdomain].append((skill_name, metadata))
        print(f"  ✓ {skill_name} → {subdomain}")
    
    return skills_by_subdomain


def format_subdomain_name(subdomain: str) -> str:
    """Convert subdomain like 'api-security' to 'API Security'."""
    # Split on hyphens and capitalize each word
    words = subdomain.split('-')
    # Special cases for acronyms and common terms
    acronyms = {'api', 'siem', 'ot', 'ict', 'iam', 'mfa', 'vpn', 'dns'}
    
    formatted = []
    for word in words:
        if word.lower() in acronyms:
            formatted.append(word.upper())
        else:
            formatted.append(word.capitalize())
    
    return ' '.join(formatted)


def generate_category_file(category_name: str, skills: List[Tuple[str, Dict]], 
                          output_dir: Path) -> str:
    """
    Generate a Markdown file for a category with all its skills.
    
    Returns: Path to the generated file
    """
    # Sort skills by name
    sorted_skills = sorted(skills, key=lambda x: x[0])
    
    # Build markdown content
    lines = [
        f"# {category_name} Skills\n",
        f"*Generated category with {len(sorted_skills)} skills*\n",
    ]
    
    for skill_name, metadata in sorted_skills:
        description = metadata.get('description', 'No description available.').strip()
        # Clean up description from YAML multi-line format
        description = ' '.join(description.split())
        
        lines.append(f"\n- **{skill_name}**")
        lines.append(f"  {description}\n")
    
    # Create output file
    filename = f"{category_name}.md"
    filepath = output_dir / filename
    
    content = '\n'.join(lines)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Generated {filename} with {len(sorted_skills)} skills")
    return filepath


def generate_category_files(skills_by_subdomain: Dict[str, List]) -> Dict[str, Path]:
    """Generate all category Markdown files."""
    categories_dir = Path(__file__).parent / 'categories'
    categories_dir.mkdir(exist_ok=True)
    
    print(f"\n📝 Generating category files in {categories_dir}")
    
    category_files = {}
    for subdomain in sorted(skills_by_subdomain.keys()):
        category_name = format_subdomain_name(subdomain)
        skills = skills_by_subdomain[subdomain]
        filepath = generate_category_file(category_name, skills, categories_dir)
        category_files[category_name] = filepath
    
    return category_files


def update_readme(skills_by_subdomain: Dict[str, List], category_files: Dict[str, Path]):
    """Update README.md with categories table and download links."""
    readme_path = Path(__file__).parent / 'README.md'
    
    # Read existing README
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Generate categories table
    repo_owner = "mukul975"
    repo_name = "Anthropic-Cybersecurity-Skills"
    github_raw_url = f"https://github.com/{repo_owner}/{repo_name}/raw/main/categories"
    
    table_lines = [
        "## Skill Categories\n",
        "| Category | Skills | Example Skills | Download |",
        "|----------|-------:|---|---|",
    ]
    
    for subdomain in sorted(skills_by_subdomain.keys()):
        category_name = format_subdomain_name(subdomain)
        skills = skills_by_subdomain[subdomain]
        skill_count = len(skills)
        
        # Get up to 3 example skills
        example_skills = ', '.join([name for name, _ in sorted(skills, key=lambda x: x[0])[:3]])
        
        # Create downloadable link with URL encoding
        encoded_filename = urllib.parse.quote(f"{category_name}.md")
        download_link = f"[📥 Download]({github_raw_url}/{encoded_filename})"
        
        table_lines.append(
            f"| {category_name} | {skill_count} | {example_skills} | {download_link} |"
        )
    
    table_text = '\n'.join(table_lines) + '\n'
    
    # Replace or insert the categories table
    # Look for existing "## Skill Categories" section with more flexible pattern
    pattern = r'## Skill Categories\n(?:\|.*?\n)*'
    
    match = re.search(pattern, readme_content)
    if match:
        # Replace existing table
        readme_content = re.sub(pattern, table_text, readme_content)
        print("  ✓ Updated existing categories table in README.md (with download links)")
    else:
        # Insert after README header or at a suitable location
        # Find a good insertion point (after the Quick Start section)
        insertion_point = readme_content.find('## Quick Start')
        if insertion_point != -1:
            # Find the end of Quick Start section
            next_section = readme_content.find('\n## ', insertion_point + 1)
            if next_section != -1:
                insertion_point = next_section
            else:
                insertion_point = len(readme_content)
        
        # Only insert if not already present
        if '## Skill Categories' not in readme_content:
            readme_content = readme_content.rstrip() + '\n\n' + table_text
            print("  ✓ Added categories table to README.md")
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)


def main():
    """Main execution function."""
    print("🚀 Organizing Anthropic Cybersecurity Skills by Subdomain\n")
    
    # Collect all skills
    skills_by_subdomain = collect_skills()
    
    if not skills_by_subdomain:
        print("\n❌ No skills found!")
        return
    
    print(f"\n✅ Found {len(skills_by_subdomain)} categories with "
          f"{sum(len(v) for v in skills_by_subdomain.values())} total skills\n")
    
    # Generate category files
    category_files = generate_category_files(skills_by_subdomain)
    
    # Update README
    print("\n📄 Updating README.md")
    update_readme(skills_by_subdomain, category_files)
    
    print("\n✨ Done! Skill categories organized successfully!")
    print(f"📂 Categories directory: {Path(__file__).parent / 'categories'}/")
    print(f"📋 Total categories: {len(skills_by_subdomain)}")
    print(f"🎯 Total skills organized: {sum(len(v) for v in skills_by_subdomain.values())}")


if __name__ == '__main__':
    main()