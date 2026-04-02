import re

with open('src/app/page.tsx', 'r') as f:
    text = f.read()

# Replace cyan variants with silver/white/gray gradients
text = re.sub(r'#00d2ff', '#cccccc', text)
text = re.sub(r'rgba\(0,210,255', 'rgba(204,204,204', text)
text = re.sub(r'#009acc', '#888888', text)
text = re.sub(r'#00a3cc', '#999999', text)
text = re.sub(r'#006c8c', '#555555', text)
text = re.sub(r'text-cyan-400', 'text-gray-300', text)
text = re.sub(r'hover:bg-cyan-400', 'hover:bg-gray-300', text)

# Just to be safe, replace SUI blue #00d2ff is already replaced
text = re.sub(r'fill="#00d2ff"', 'fill="#cccccc"', text)

with open('src/app/page.tsx', 'w') as f:
    f.write(text)

print("Done replacing.")
