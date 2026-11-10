"""把本机已确认的无限画布资料归档；不读取账号配置、密钥或浏览器凭据。"""
import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = Path('E:/AI code/infinite-canvas')
DESKTOP = Path('C:/Users/bojia/Desktop')
DEST = ROOT / 'library/infinite-canvas'
manifest = []


def redact(text):
    text = re.sub(r'\bsk-[A-Za-z0-9_-]{12,}', '[REDACTED_API_KEY]', text)
    text = re.sub(r'(?i)(Bearer\s+)[A-Za-z0-9_.-]{20,}', r'\1[REDACTED_TOKEN]', text)
    return text


def archive(source, relative):
    target = DEST / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() in {'.md', '.mdx', '.js', '.txt'}:
        target.write_text(redact(source.read_text(encoding='utf-8-sig')), encoding='utf-8')
    else:
        shutil.copyfile(source, target)
    data = target.read_bytes()
    manifest.append({'path': target.relative_to(ROOT).as_posix(), 'source': source.name,
                     'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})


for source in sorted((SOURCE / 'docs/content/docs').rglob('*.mdx')):
    archive(source, Path('docs') / source.relative_to(SOURCE / 'docs/content/docs'))
for name in ('README.md', 'LICENSE', 'CHANGELOG.md', 'VERSION'):
    archive(SOURCE / name, Path('project') / name)
archive(SOURCE / 'docs/index.md', Path('project/DOCUMENTATION-INDEX.md'))
for name in ('Docker安装和启动指南.md', 'GPT-Image-2.5-配置指南.md',
             'infinite-canvas-启动说明.md', 'infinite-canvas-setup-guide.md',
             'MiniMax-H3-调用脚本.js', 'MiniMax-H3-Max-调用脚本.js'):
    source = SOURCE.parent / name
    if source.exists():
        archive(source, Path('guides') / name)
for name in ('ff904c26-3e8c-4e6c-a5c6-c18dba35fb3e.png',
             '162679a9-ddfa-4b98-a1aa-81711665efec.png',
             '110614f5-7cf0-458b-aaca-2122204d7d82.png',
             'f28d2803-450d-454d-9b76-55671db553cd.png',
             '60d50370-a126-4806-9a54-81075039c336.png'):
    archive(DESKTOP / name, Path('references/characters') / name)
archive(SOURCE.parent / 'seedance-tiger-4s-480p-test/tiger-4s-480p.mp4', Path('examples/seedance/tiger-4s-480p.mp4'))
archive(SOURCE.parent / 'minimax-tiger-1s-test/tiger-first-frame.png', Path('examples/seedance/tiger-first-frame.png'))
(DEST / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
lines = ['# 无限画布资料索引', '', '| 文件 | 字节数 |', '| --- | --- |']
for item in manifest:
    path = Path(item['path']).relative_to('library/infinite-canvas').as_posix()
    lines.append(f"| [{path}]({path.replace(' ', '%20')}) | {item['bytes']} |")
(DEST / 'INDEX.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(json.dumps({'files': len(manifest), 'bytes': sum(x['bytes'] for x in manifest)}, ensure_ascii=False))
