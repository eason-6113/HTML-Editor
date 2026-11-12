"""Check the standalone release pages and their inline JavaScript."""

from html.parser import HTMLParser
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory


class ReleasePage(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.ids = set()
        self.scripts = []
        self.script = None
        self.language = None

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "html":
            self.language = attrs.get("lang")
        element_id = attrs.get("id")
        if element_id:
            if element_id in self.ids:
                raise ValueError(f"Duplicate ID: {element_id}")
            self.ids.add(element_id)
        if tag == "script":
            if "src" in attrs:
                raise ValueError("Standalone pages must embed their scripts")
            self.script = []

    def handle_data(self, data):
        if self.script is not None:
            self.script.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.script is not None:
            self.scripts.append("".join(self.script))
            self.script = None


root = Path(__file__).resolve().parents[1]
with TemporaryDirectory() as directory:
    for name in ("index.html", "guide.html"):
        parser = ReleasePage()
        parser.feed((root / name).read_text(encoding="utf-8-sig"))
        parser.close()
        if parser.language != "zh-Hant" or not parser.scripts or parser.script is not None:
            raise ValueError(f"Invalid release page: {name}")
        for number, script in enumerate(parser.scripts):
            script_path = Path(directory, f"{name}-{number}.js")
            script_path.write_text(script, encoding="utf-8")
            subprocess.run(["node", "--check", script_path], check=True)
        print(f"OK: {name}")
