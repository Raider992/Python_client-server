import yaml

def write_to_yaml():
    data = {
        'list': ['l', 'i', 's', 't'],
        'num': 2,
        'dict': {'first': '1€', 'second': '2€'}
    }
    with open('file.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

write_to_yaml()
