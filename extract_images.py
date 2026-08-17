import re

with open(r'C:\Users\user\.gemini\antigravity\brain\d151eb1e-a689-40e9-9904-12e7f1c01851\.system_generated\steps\29\content.md', 'r', encoding='utf-8') as f:
    content = f.read()
section = re.search(r'<section class="partner-section.*?>(.*?)</section>', content, re.DOTALL)
if section:
    images = re.findall(r'<img src="(assets/img/partner-.*?)".*?>', section.group(1))
    for img in images:
        print(f'''<div class="partner-logo-card">
    <img src="https://www.xpertcs.com/{img}" alt="Partner">
</div>''')
