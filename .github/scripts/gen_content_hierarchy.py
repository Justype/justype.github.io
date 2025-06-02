import os
import json

def get_type(filename):
    ext = filename.lower().split('.')[-1]
    if ext in ['md', 'markdown']: return 'markdown'
    if ext == 'pdf': return 'pdf'
    if ext in ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'webp']: return 'image'
    if ext in ['mp4', 'webm', 'mov', 'avi', 'mkv']: return 'video'
    if ext == 'html': return 'html'
    if ext in ['txt', 'text', 'log']: return 'text'
    return 'file'

def build_hierarchy(path, rel_path=''):
    items = []
    for name in sorted(os.listdir(path)):
        if name.startswith('.'):
            continue
        full_path = os.path.join(path, name)
        rel = os.path.join(rel_path, name) if rel_path else name
        if os.path.isdir(full_path):
            children = build_hierarchy(full_path, rel)
            items.append({
                'name': name,
                'type': 'folder',
                'path': rel.replace('\\', '/'),
                'children': children
            })
        else:
            items.append({
                'name': name,
                'type': get_type(name),
                'path': rel.replace('\\', '/')
            })
    # Folders first, then files
    items.sort(key=lambda x: (x['type'] != 'folder', x['name'].lower()))
    return items

if __name__ == '__main__':
    root = 'content'
    hierarchy = build_hierarchy(root)
    with open('content-hierarchy.json', 'w', encoding='utf-8') as f:
        json.dump(hierarchy, f, indent=2, ensure_ascii=False)
