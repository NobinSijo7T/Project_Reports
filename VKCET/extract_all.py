import fitz
import json

doc = fitz.open('reference.pdf')

pages_data = []

for i, page in enumerate(doc):
    page_info = {
        'page_num': i + 1,
        'rect': [page.rect.x0, page.rect.y0, page.rect.x1, page.rect.y1],
        'text': page.get_text(),
        'blocks': []
    }
    
    text_dict = page.get_text('dict')
    for b in text_dict['blocks']:
        if b.get('type') == 0: # text
            block_lines = []
            for l in b['lines']:
                line_spans = []
                for s in l['spans']:
                    line_spans.append({
                        'text': s['text'],
                        'font': s['font'],
                        'size': s['size'],
                        'flags': s['flags'],
                        'color': s['color'],
                        'bbox': [round(x, 2) for x in s['bbox']]
                    })
                block_lines.append({
                    'bbox': [round(x, 2) for x in l['bbox']],
                    'spans': line_spans
                })
            page_info['blocks'].append({
                'type': 'text',
                'bbox': [round(x, 2) for x in b['bbox']],
                'lines': block_lines
            })
        elif b.get('type') == 1: # image
            page_info['blocks'].append({
                'type': 'image',
                'bbox': [round(x, 2) for x in b['bbox']],
                'width': b.get('width'),
                'height': b.get('height')
            })
            
    pages_data.append(page_info)

with open('extracted_pages.json', 'w', encoding='utf-8') as f:
    json.dump(pages_data, f, indent=2, ensure_ascii=False)

print('Extracted data for all', len(doc), 'pages into extracted_pages.json')

