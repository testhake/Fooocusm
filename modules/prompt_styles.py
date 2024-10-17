import os
import re
import json
import math

from modules.extra_utils import get_files_from_folder

prompt_styles_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../prompt_styles/'))

def normalize_key(k):
    k = k.replace('-', ' ')
    words = k.split(' ')
    words = [w[:1].upper() + w[1:].lower() for w in words]
    k = ' '.join(words)
    k = k.replace('3d', '3D')
    k = k.replace('Sai', 'SAI')
    k = k.replace('Mre', 'MRE')
    k = k.replace('(s', '(S')
    return k

prompt_styles = {}
prompt_styles_files = get_files_from_folder(prompt_styles_path, ['.json'])

for styles_file in prompt_styles_files:
    try:
        with open(os.path.join(prompt_styles_path, styles_file), encoding='utf-8') as f:
            for entry in json.load(f):
                name = normalize_key(entry['name'])
                prompt = entry['prompt'] if 'prompt' in entry else ''
                negative_prompt = entry['negative_prompt'] if 'negative_prompt' in entry else ''
                prompt_styles[name] = (prompt, negative_prompt)
    except Exception as e:
        print(str(e))
        print(f'Failed to load prompt style file {styles_file}')

prompt_style_keys = list(prompt_styles.keys())
legal_prompt_style_names = prompt_style_keys

def apply_prompt_style(style, positive):
    p, n = prompt_styles[style]
    return p.replace('{prompt}', positive).splitlines(), n.splitlines(), '{prompt}' in p

def get_words(arrays, total_mult, index):
    if len(arrays) == 1:
        return [arrays[0].split(',')[index]]
    else:
        words = arrays[0].split(',')
        word = words[index % len(words)]
        index -= index % len(words)
        index /= len(words)
        index = math.floor(index)
        return [word] + get_words(arrays[1:], math.floor(total_mult / len(words)), index)
    
def apply_arrays(text, index):
    arrays = re.findall(r'\[\[(.*?)\]\]', text)
    if len(arrays) == 0:
        return text

    print(f'[Arrays] processing: {text}')
    mult = 1
    for arr in arrays:
        words = arr.split(',')
        mult *= len(words)
    
    index %= mult
    chosen_words = get_words(arrays, mult, index)
    
    i = 0
    for arr in arrays:
        text = text.replace(f'[[{arr}]]', chosen_words[i], 1)   
        i = i+1
    
    return text
