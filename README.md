# Game Dev Courses

Interactive, click-by-click courses for Blender and Unreal Engine, each lesson built around a real production result.

**Live site:** https://1337viper.github.io/gamedev-courses/

| Course | Status |
| --- | --- |
| [Geometry Nodes Fast Track](https://1337viper.github.io/gamedev-courses/geometry-nodes/) (Blender 5.3) | Modules 1–2 (Module 2 ends in a sellable pack) |
| [Niagara VFX Fast Track](https://1337viper.github.io/gamedev-courses/niagara-vfx/) (Unreal Engine 5.8) | Modules 1–2 (Module 2 ends in a sellable pack) |
| [Compositing Fast Track](https://1337viper.github.io/gamedev-courses/blender-compositing/) (Blender 5.3) | Modules 1–2 (Module 2 ends in a sellable pack) |

Progress (ticks, notes, best times) saves in your browser. To keep it in a file instead, run a course locally:

```
python geometry-nodes/serve.py
```

then open http://127.0.0.1:5177 (Niagara: `niagara-vfx/serve.py`, port 5178; Compositing: `blender-compositing/serve.py`, port 5179) and progress is written to `progress.json` next to the page.
