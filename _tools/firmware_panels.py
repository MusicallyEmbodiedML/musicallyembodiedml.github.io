#!/usr/bin/env python3
"""Make one annotated MEMLNaut panel SVG per NISPS firmware.

Starts from assets/images/nisps/memlnaut-panel-nisps.svg (the default NISPS
controls) and swaps in each firmware's own functions. Controls that differ from
the NISPS defaults get a dashed gold ring and a gold label.

    python3 _tools/firmware_panels.py

Writes assets/images/nisps/panel-<slug>.svg. Jekyll skips folders starting
with "_", so this script is not published.
"""
from html import escape
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
BASE = SITE / "assets/images/nisps/memlnaut-panel-nisps.svg"
OUT = SITE / "assets/images/nisps"

GOLD = "#d6b92a"
SANS = "Helvetica, Arial, sans-serif"
MONO = "Menlo, Consolas, monospace"

# Standard screens around the mode screens (InterfaceRL order).
AFTER_MODE = ["NN Inputs", "Messages", "Save Model", "Load Model", "Input Source"]

FIRMWARES = [
    {
        "slug": "memlcelium", "name": "MEMLCelium", "build": "MODE_MEMLCELIUM",
        "tagline": "three-voice PAF synth with sequencer",
        "knob_y": ("Y · tempo", "30–200 BPM"),
        "tog_b_down": ("Sequencer", "stop / start"),
        "inputs_used": False, "messages": False, "midi_in": None, "joystick": None,
        "mode_screens": ["Focus", "Enable"], "end_screens": [],
        "notes": ["The sequencer starts playing at power-on. 83 network outputs."],
    },
    {
        "slug": "mixmastermeml", "name": "MixMasterMEML", "build": "MODE_MIXMASTERMEML",
        "tagline": "three voices, arp and bass, with effects and mixer",
        "knob_y": ("Y · tempo", "30–200 BPM"),
        "tog_b_down": ("Sequencer", "stop / start"),
        "inputs_used": False, "messages": False, "midi_in": None, "joystick": None,
        "mode_screens": ["Focus", "Enable", "Mixer"], "end_screens": [],
        "notes": ["Trains on demand: settles once it has learned your likes; any new gesture restarts training. 122 outputs."],
    },
    {
        "slug": "verbfx", "name": "VerbFX", "build": "MODE_VERBFX",
        "tagline": "reverb, filterbank and delays for line input",
        "knob_y": ("Y · wet / dry", "0 = dry"),
        "tog_b_down": None,
        "inputs_used": True, "messages": False, "midi_in": "MIDI in · feedback CCs",
        "joystick": None,
        "mode_screens": ["Focus", "FX Enable", "Voice Spaces"], "end_screens": [],
        "notes": ["MIDI CC 1 like · 2 dislike · 3 scramble · 4 forget · 5 exploration · 6 training speed."],
    },
    {
        "slug": "livefx", "name": "LiveFX", "build": "MODE_DJFX",
        "tagline": "ten tempo-synced effects for live sets and DJing",
        "knob_y": ("Y · DJ filter", "low-pass ◂ centre ▸ high-pass"),
        "knob_y_extra": "DJ Mode off: wet / dry",
        "tog_b_down": None,
        "inputs_used": True, "messages": True, "midi_in": "MIDI in · feedback CCs",
        "joystick": ("Joystick · explore + wet/dry", "DJ Mode: dry at centre, wet at edge"),
        "mode_screens": ["Focus", "FX Enable", "VU"], "end_screens": ["Options"],
        "notes": ["Tap tempo on the RL screen. DJ Mode is on the Options screen.",
                  "MIDI CC 1 like · 2 dislike · 3 scramble · 4 forget · 5 exploration · 6 training speed."],
    },
]


def sub(svg, old, new):
    """Replace one exact fragment of the base SVG; fail loudly if it moved."""
    n = svg.count(old)
    if n != 1:
        raise SystemExit(f"expected one match, found {n}: {old[:70]!r}")
    return svg.replace(old, new)


def ring(cx, cy, r):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GOLD}" '
            f'stroke-width="3" stroke-dasharray="7 6"/>')


def screen_list(fw):
    """Replace the RL sketch with this firmware's screen order."""
    after = [s for s in AFTER_MODE if fw["messages"] or s != "Messages"]
    screens = (["RL"] + [(s, True) for s in fw["mode_screens"]] + after
               + [(s, True) for s in fw["end_screens"]])
    screens = [s if isinstance(s, tuple) else (s, False) for s in screens]
    rows = (len(screens) + 1) // 2
    out = [f'<g font-family="{MONO}" font-size="16">']
    for i, (name, own) in enumerate(screens):
        col, row = divmod(i, rows)
        x, y = 231 + col * 210, 545 + row * 34
        fill = GOLD if own else "#c6d0c8"
        out.append(f'<text x="{x}" y="{y}" fill="#5f7369">{i + 1:>2}</text>'
                   f'<text x="{x + 30}" y="{y}" fill="{fill}">{escape(name)}</text>')
    out.append("</g>")
    return "\n    ".join(out)


def build(fw):
    svg = BASE.read_text()
    name = fw["name"]
    changed = []

    # title on the board
    svg = sub(svg, '<text x="372" y="233" font-family="Helvetica, Arial, sans-serif" font-size="44" fill="#eef2ee">MEMLNaut</text>',
              f'<text x="372" y="233" font-family="{SANS}" font-size="44" fill="#eef2ee">MEMLNaut '
              f'<tspan fill="{GOLD}">{escape(name)}</tspan></text>\n'
              f'  <text x="374" y="262" font-family="{SANS}" font-size="16" fill="#c6d0c8">{escape(fw["tagline"])}</text>')
    svg = sub(svg, "NISPS bindings (InterfaceRL.tpp).",
              f"{name} ({fw['build']}), generated by _tools/firmware_panels.py.")

    # G knob: plain volume in every firmware here
    svg = sub(svg, '\n    <text x="338" y="397" font-size="13" fill="#c6d0c8">TR-8S: CC home value</text>', "")

    # line inputs
    if not fw["inputs_used"]:
        svg = sub(svg, '<circle cx="177" cy="214" r="20"/><circle cx="256" cy="214" r="20"/>',
                  '<circle cx="177" cy="214" r="20" opacity=".35"/><circle cx="256" cy="214" r="20" opacity=".35"/>')
        svg = sub(svg, '<text x="177" y="182">in L</text><text x="256" y="182">in R</text>',
                  '<text x="216" y="182" fill="#c6d0c8" opacity=".7">in: not used</text>')

    # MIDI in
    if fw["midi_in"]:
        svg = sub(svg, '<text x="522" y="100">MIDI in</text>',
                  f'<text x="522" y="100" fill="{GOLD}">{escape(fw["midi_in"])}</text>')

    # knob Y
    title, note = fw["knob_y"]
    svg = sub(svg, '<text x="912" y="558" font-size="17" font-weight="bold">Y · reward scale</text>',
              f'<text x="912" y="558" font-size="17" font-weight="bold" fill="{GOLD}">{escape(title)}</text>')
    extra = fw.get("knob_y_extra")
    svg = sub(svg, '<text x="912" y="577" font-size="13" fill="#c6d0c8">some modes: tempo / wet-dry / fade</text>',
              f'<text x="912" y="577" font-size="13" fill="#c6d0c8">{escape(note)}</text>'
              + (f'<text x="866" y="621" font-size="13" fill="#c6d0c8" text-anchor="end">{escape(extra)}</text>'
                 if extra else ""))
    changed.append(ring(912, 616, 34))

    # toggle B down
    if fw["tog_b_down"]:
        svg = sub(svg, '<text x="1032" y="502" font-size="14" font-weight="normal" fill="#c6d0c8">▼ mode-specific</text>',
                  f'<text x="1032" y="504" fill="{GOLD}"><tspan fill="#eef2ee">▼ </tspan>{escape(fw["tog_b_down"][0])}</text>'
                  f'<text x="1053" y="524" font-size="14" font-weight="normal" fill="{GOLD}">{escape(fw["tog_b_down"][1])}</text>')
        changed.append(ring(994, 480, 32))
    else:
        svg = sub(svg, "▼ mode-specific", "▼ not used")

    # joystick
    if fw["joystick"]:
        jt, jn = fw["joystick"]
        svg = sub(svg, '<text x="1312" y="664" font-size="19" font-weight="bold">Joystick · explore</text>',
                  f'<text x="1312" y="664" font-size="19" font-weight="bold" fill="{GOLD}">{escape(jt)}</text>')
        svg = sub(svg, '<text x="1312" y="686" font-size="14" fill="#c6d0c8">X · Y · Z, plus W on 4-axis sticks</text>',
                  f'<text x="1312" y="686" font-size="14" fill="#c6d0c8">{escape(jn)}</text>')
        changed.append(ring(1312, 502, 140))

    # screen
    start = svg.index('  <text x="223" y="490"')
    end = svg.index("  </g>\n", svg.index('RL screen (sketch)')) + len("  </g>\n")
    svg = (svg[:start]
           + f'  <text x="223" y="490" font-family="{MONO}" font-size="14" fill="#8fa49a">screens · turn the encoder</text>\n'
           + '  <rect x="223" y="508" width="414" height="1" fill="#2a3a33"/>\n  '
           + screen_list(fw) + "\n"
           + f'  <text x="223" y="768" font-family="{MONO}" font-size="13" fill="#5f7369">gold = {escape(name)} screens</text>\n'
           + svg[end:])

    # rings, legend and notes
    svg = sub(svg, "  <!-- joystick", "  <!-- controls that differ from NISPS -->\n  " + "\n  ".join(changed) + "\n\n  <!-- joystick")
    svg = sub(svg, '<text x="660" y="882">place a sound (hold, move, release)</text>',
              '<text x="660" y="882">place a sound (hold, move, release)</text>\n'
              f'    <circle cx="1007" cy="877" r="8" fill="none" stroke="{GOLD}" stroke-width="2.5" stroke-dasharray="4 3"/>'
              f'<text x="1024" y="882" fill="{GOLD}">different in {escape(name)}</text>')
    svg = sub(svg, '<text x="58" y="920" fill="#9fb8b8" font-size="14">▲ / ▼ = switch pushed up / down. Momentary switches spring back; toggles stay where you put them.</text>',
              '<text x="58" y="906" fill="#9fb8b8" font-size="14">▲ / ▼ = switch pushed up / down. Momentary switches spring back; toggles stay where you put them.</text>'
              + "".join(f'<text x="58" y="{928 + 20 * i}" fill="#eef5e0" font-size="14">{escape(n)}</text>'
                        for i, n in enumerate(fw["notes"])))

    # accessible description
    desc = [f"MEMLNaut front panel with the {name} controls.",
            "Momentary switch A (left): up scrambles the network, down jolts it.",
            "Momentary B (right): up likes the current sound, down dislikes it.",
            "Toggle A (left) down forgets the memory; toggle B (right) up drags a sound to a new place"
            + (", down stops or restarts the sequencer." if fw["tog_b_down"] else "."),
            f"Knob X sets the learning rate, knob {title.replace(' · ', ' sets the ')}"
            + (f" ({note}; {extra})" if extra else f" ({note})") + ", Z the exploration.",
            (fw["joystick"][0] + ". " if fw["joystick"] else "The joystick explores; pressing it also drags. "),
            "Screens: " + ", ".join(fw["mode_screens"] + fw["end_screens"]) + " are added for this firmware."]
    start = svg.index('aria-label="') + len('aria-label="')
    svg = svg[:start] + escape(" ".join(desc)) + svg[svg.index('"', start):]
    return svg


def main():
    for fw in FIRMWARES:
        path = OUT / f"panel-{fw['slug']}.svg"
        path.write_text(build(fw))
        print("wrote", path.relative_to(SITE))


if __name__ == "__main__":
    main()
