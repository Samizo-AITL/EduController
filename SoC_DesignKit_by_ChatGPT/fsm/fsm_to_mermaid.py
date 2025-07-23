# 🐍 fsm_to_mermaid.py
# YAMLで定義されたFSMをMermaid.jsのステート図に変換するスクリプト

import yaml
import sys

def load_fsm_yaml(filename):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
    return data['fsm']

def generate_mermaid(fsm):
    lines = []
    lines.append("stateDiagram-v2")
    for transition in fsm['transitions']:
        frm = transition['from']
        to = transition['to']
        trigger = transition.get('trigger', '')
        lines.append(f"    {frm} --> {to} : {trigger}")
    return '\n'.join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python fsm_to_mermaid.py <fsm_yaml_file>")
        return

    fsm_yaml = sys.argv[1]
    fsm = load_fsm_yaml(fsm_yaml)
    mermaid_output = generate_mermaid(fsm)
    print(mermaid_output)

if __name__ == "__main__":
    main()
