import os

base_dir = r"C:\Users\hp\.gemini\antigravity\scratch\Projects\content\July 2026"
projects = ["A1 Auto Panel", "Kowhai Kids Club"]
files = {
    "web2.0.md": "Web 2.0",
    "guest_post.md": "Guest Post",
    "article.md": "Article"
}

for project in projects:
    for filename, prefix in files.items():
        filepath = os.path.join(base_dir, project, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        parts = content.split("---")
        new_parts = []
        count = 1
        for part in parts:
            part = part.strip()
            if not part:
                continue
            
            # Remove existing prefix if it somehow already exists to avoid duplication
            if part.startswith(f"# {prefix}"):
                # Find the next # to start the actual article
                lines = part.split("\n")
                new_lines = []
                for line in lines:
                    if line.startswith(f"# {prefix}"):
                        continue
                    new_lines.append(line)
                part = "\n".join(new_lines).strip()
            
            # Add the new header
            new_part = f"# {prefix} {count}\n\n{part}"
            new_parts.append(new_part)
            count += 1
            
        new_content = "\n\n---\n\n".join(new_parts)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
            
print("Headers added successfully.")
