"""同步黑胡子公开灵感作品，输出无限画布兼容的提示词来源。"""
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen

BASE = "https://code.heihuzi.ai"
ROOT = Path(__file__).resolve().parent


def fetch(path):
    request = Request(BASE + path, headers={"User-Agent": "InfiniteCanvas-Knowledge/1.0"})
    with urlopen(request) as response:
        payload = json.load(response)
    if payload.get("code") != 0:
        raise ValueError(payload.get("message", "接口返回失败"))
    return payload["data"]


def main():
    works = {}
    for kind in ("image", "canvas"):
        page = 1
        while True:
            data = fetch(f"/api/v1/inspire/works?kind={kind}&page={page}&page_size=30&sort=recommended")
            for item in data["items"]:
                works[item["id"]] = item
            if page >= data["pages"]:
                break
            page += 1
    with ThreadPoolExecutor(max_workers=3) as pool:
        details = list(pool.map(lambda key: fetch(f"/api/v1/inspire/works/{key}"), works))
    prompts = []
    for item in details:
        if item["kind"] != "image" or not item.get("prompt", "").strip():
            continue
        prompts.append({
            "id": item["id"], "title": item["title"], "prompt": item["prompt"],
            "description": item.get("description", ""),
            "coverUrl": BASE + item["thumbnail_url"],
            "referenceImageUrls": [],
            "tags": list(dict.fromkeys([item["category"], *item.get("tags", [])])),
            "preview": item["prompt"][:160],
            "createdAt": item.get("published_at", ""), "updatedAt": item.get("published_at", ""),
            "author": item.get("author", {}).get("name") or "黑胡子便利店 / 匿名作者",
            "sourceUrl": BASE + "/inspire?work=" + item["id"],
            "imageModel": item.get("model", ""),
        })
    for name, data in (("works.json", details), ("prompts.json", prompts)):
        (ROOT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# 灵感知识库索引", "", "来源：https://code.heihuzi.ai/inspire", "", "| ID | 类型 | 分类 | 标题 |", "| --- | --- | --- | --- |"]
    for item in details:
        title = item["title"].replace("|", "／").replace("\n", " ").replace("\r", " ")
        lines.append(f'| {item["id"]} | {item["kind"]} | {item["category"]} | {title} |')
    (ROOT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"works": len(details), "imagePrompts": len(prompts), "canvas": sum(x["kind"] == "canvas" for x in details)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
