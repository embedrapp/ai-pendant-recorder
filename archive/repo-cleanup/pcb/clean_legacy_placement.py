"""Retire old board directives and superseded legacy schematic coordinates.
Does not edit physical board or agent positions (the final sch block is retained).
"""
from pathlib import Path
p = Path(__file__).with_name('ai_pendant_recorder.zen')
s = p.read_text()
last = s.rfind('# pcb:sch C1.C')
assert last >= 0
before, current = s[:last], s[last:]
before = '\n'.join(line for line in before.splitlines()
                   if not line.startswith(('# pcb:sch ', '# pcb:brd ')))
p.write_text(before.rstrip() + '\n\n# Base revision: physical placement intentionally unset.\n' + current)