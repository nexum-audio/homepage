from pathlib import Path
import json,html,re
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parent.parent
strings=json.loads((ROOT/'tools/web-strings.json').read_text(encoding='utf-8'))
translations={}
def fill(s):
 for line in s.splitlines():
  if '|' in line:
   n,t=line.split('|',1);translations[strings[int(n)]]=t
fill('''7| to 
9| folder to 
11|. Third-party libraries retain their respective licenses. The full license texts included in the archive apply.
12|. Then run your DAW's plugin scan. Nexum is an instrument; FX, Tune and Gate are audio effects.
15|01 / ONE FAMILY
16|01 / Hybrid synthesizer
18|02 / YOUR TOOLS
19|02 / Modular effect rack
21|03 / OPEN BY DESIGN
24|04 / READY FOR YOUR SESSION
31|5.9 MB
32|6.7 MB
34|7.9 MB
35|8.0 MB
40|AGPLv3 license 
41|Read AGPLv3 
42|ALSO IN THE FAMILY
43|Eight pattern slots with up to 64 steps, individual levels and ties. Attack, Decay, Sustain, Release and Gate Length shape each pulse.
44|Current development builds · Windows 64-bit
45|Development build · ZIP · 5.9 MB
46|Development build · ZIP · 6.7 MB
47|Development build · ZIP · 7.9 MB
48|Development build · ZIP · 8.0 MB
49|Load as an insert
50|Close image
51|Enlarge view ↗
52|Audio input
53|EXAMPLE / NEXUM + FX
54|Edit notes, intonation and vibrato, then audition the passage in a loop.
55|Fine-tune the movement
56|Shape the movement
57|See your sound move
58|Libraries & licenses
59|Build instructions
61|CODE YOU CAN BUILD ON.
63|Code for your ideas.
64|YOUR WORKFLOW
65|MAKE IT YOUR OWN
66|GET STARTED
67|The right tool for each edit
68|Your expression.
69|Your rack.
70|Your signal path
71|Your sound.
72|Your source.
73|Your tool.
74|Your next track
75|Your voice.
76|Bring your own tools.
77|The starting point for your sound.
78|The signal flows through Shaper → Gate → Pan. Each stage can pass audio through unchanged. Low Band Only uses an internal crossover, not an external sidechain input.
79|The source is included.
80|The shared effect rack, as an insert.
81|Your recording becomes editable notes with pitch curves. Colors show the distance to the target pitch; uncertain passages appear in gray.
82|Downloads do not include external sound, sample or preset packs. Import your own content into the libraries.
83|The effects from Nexum, in a standalone audio plugin. Place your rack on vocals, drums or a bus and load effect chains from the same library.
84|The Nexum Suite is an open-source project for sound creation and audio editing. Use the plugins, look under the hood and take your own ideas further.
85|The Open-Source Audio Suite · Nexum Audio
86|The Pan stage adds stereo movement to your rhythms. Shaper, Gate and Pan each have independent switches and depth controls.
87|The suite
88|Explore the suite 
89|The available binaries are for Windows x64. Ready-made macOS and Linux downloads are not currently provided. The source code is openly available.
90|The original implementations of all four Nexum plugins are released under 
91|Full PowerShell build commands for all four products are included in the source archive's README.
93|Three main oscillators with Wavetable, Sample, Multisample, Granular and Spectral modes. Sub and Noise complete the foundation.
94|Ducking, rhythm and stereo movement.
95|Ducking curves, rhythmic gate patterns and stereo movement in three clear modules. Combine them or switch each stage into the signal path independently.
96|A SHARED FOUNDATION
97|One rack, your signal
98|A free, open-source plugin.
99|One creative flow.
100|One view. Your next move.
101|One idea.
102|A library for your ideas
103|One shared FX library
104|Use them individually.
105|Explore ↗
106|Extract
107|Add filters, the arpeggiator, clips and effects. Save the entire sound as a preset.
108|Add Pan and adjust depth, timing and mix in the context of your track.
109|Make music first.
111|Export the edited recording or drag its WAV file into your timeline.
112|External sample, wavetable and preset packs are not included. Load your own content into the libraries.
115|Find your next sound.
117|Add Nexum FX to an audio track or mixer bus.
118|For every track.
119|Gate: build your rhythm
120|Shared UI
121|Make precise corrections
122|Give your
123|Are macOS or Linux versions available?
124|Same effects. Same sound.
126|Main navigation
127|Main oscillators
128|Hybrid synthesizer
129|Listen, compare, export
130|A CLOSER LOOK
131|Shape it in context
132|Stay in time
133|Install in three steps.
134|Yes, under the terms of AGPLv3. The source package includes the full license and notices for all bundled libraries.
135|Every possible sound.
136|Each ZIP includes VST3, standalone and license notices.
137|Can I modify the code?
138|Shared FX engine
139|No account or subscription required.
140|No account. No subscription. Direct downloads.
141|Without four copies of the code.
142|Choose a sound
143|Combine effects such as Distortion, Chorus, Delay, Convolve and Trancegate. Change their order and control bypass directly on each module.
144|Copy the entire folder ending in 
145|Copy the entire 
146|Copy
147|Download for free 
148|Choose a curve
149|LICENSES
150|Load WAV, AIFF or FLAC, or record audio directly in the plugin.
151|Download the Windows ZIP and extract it into its own folder.
152|Load individual modules or a saved effect chain.
153|MODULAR EFFECT RACK
155|Macros for your workflow
156|More possibilities.
157|Menu 
158|Mixer insert
159|Modular effect rack
161|Music is never
162|NEXUM / THE INTERFACE
163|NEXUM FX / THE INTERFACE
164|NEXUM GATE / THE INTERFACE
166|NEXUM TUNE / THE INTERFACE
168|Back to top ↑
171|Nexum Audio home
174|Nexum FX product mockup
175|Download Nexum FX for Windows
176|Download Nexum FX 
177|Nexum FX processes incoming audio and has no synthesis oscillators. The standalone requires a selected audio input.
179|Enlarge Nexum FX interface
182|Nexum FX: modular effect rack with the macro sidebar
185|Nexum Gate product mockup
186|Download Nexum Gate for Windows
187|Download Nexum Gate 
189|Enlarge Nexum Gate interface
192|Nexum Gate: Shaper, Gate and Pan with the macro sidebar
194|Nexum product mockup
195|Nexum synthesizer with oscillators, filters and modulation
198|Nexum Tune product mockup
199|Download Nexum Tune for Windows
200|Download Nexum Tune 
202|Enlarge Nexum Tune interface
205|Nexum Tune: vocal pitch and timing editor with the macro sidebar
206|Explore Nexum
207|Download Nexum for Windows
208|Download Nexum 
209|Nexum and Nexum FX build their effect modules from one implementation. A shared UI library keeps the family visually connected. Tune and Gate complement them as independent audio effects.
210|Nexum and Nexum FX share their effect implementations. New effects are built into both products from the same codebase.
212|Enlarge Nexum interface
215|Nexum: hybrid synthesizer with the macro sidebar
216|Notes, not guesswork
217|Note editing
218|Use it, understand it, change it. All four plugins include their original source code under AGPLv3. The full source download also includes the required libraries and build instructions.
219|OSC modes
220|Or go straight to the code.
221|Open possibilities.
222|Open code.
224|Explore open source 
226|Organize presets, wavetables and multisamples with folders, categories, tags and ratings. Your own content stays editable.
227|Original comparison
229|Pan: move through stereo
230|Adjust parameters, order and macros to suit your input signal.
231|Add a pattern
234|Scan for plugins
235|Plugin view
236|Choose a plugin preview
238|Download plugins 
239|Product source, assets, shared UI components, tests, build files and full license notices. Configure each project in its own build directory.
240|Checksum
242|Build your rack
243|Reduce pitch modulation within selected notes. Edits remain non-destructive and can be undone.
244|Route generators to filters, buses, Main or Direct. Draw connections in the mixer and follow the structure of your sound.
245|BUILD IT YOURSELF
246|SHA-256 checksums 
247|SHA-256 checksums ↗
251|Close ×
252|Get started in your DAW.
253|Set gate steps, levels and ties, then shape the envelope.
254|Set the playhead, draw a preview loop and compare with the original. Export the result as WAV or drag the prepared file into your DAW.
256|Shaper curves
257|Shaper: make some space
258|See, hear and edit your vocal pitch. Correct individual notes, reduce vibrato and bring the edited recording back into your session as WAV.
259|Signal modules
260|Are sound packs included?
261|sound a pulse.
262|Finish your sound
264|Save individual effects and complete chains. The library is shared with Nexum, including names, categories, tags and ratings.
265|Run a fresh plugin scan in your DAW and load Nexum FX as an audio effect. The EXE in the ZIP opens the standalone.
266|Run a fresh plugin scan in your DAW and load Nexum Gate as an audio effect. The EXE in the ZIP opens the standalone.
267|Run a fresh plugin scan in your DAW and load Nexum Tune as an audio effect. The EXE in the ZIP opens the standalone.
268|Run a fresh plugin scan in your DAW and load Nexum as an instrument. The EXE in the ZIP opens the standalone.
269|Start with a wavetable or load your own samples and SFZ instruments.
270|Steps per pattern
271|Suite source code 
272|Download suite source 
273|Sync to the host or use free tempo. MIDI and audio triggers restart the movement; the signal-flow display shows each stage's level.
276|Pitch and timing for your vocals.
277|Tools for your sound.
278|Transparent down
279|Tune is primarily designed for monophonic vocals. Individual notes within recorded chords cannot currently be separated and edited independently. Recording is limited to 60 seconds.
280|Neither is our code.
284|Copy the VST3
285|Link several controls to one macro and save assignments with your project. The first eight macros are also available for DAW automation.
286|Enlarged plugin view
287|Connect LFOs, envelopes and macros to sound parameters.
288|Dial in the vibrato
289|Four envelopes, eight LFOs and velocity and note curves bring movement to your sound. Assign modulation sources to controls.
290|Four perspectives.
291|Four plugins. One shared idea: make music, explore sound and keep your tools in your own hands.
292|Four products.
293|Four free open-source audio plugins: Nexum, Nexum FX, Nexum Tune and Nexum Gate. Windows VST3, standalone and full source code.
295|Record or import vocals
296|Full Nexum Suite source code under AGPLv3. Libraries, build instructions and direct downloads.
297|Full suite source code 
298|From the first oscillator to the final vocal edit: Nexum Suite brings together sound creation, effects, pitch editing and rhythm. With a shared design language, visible signal paths and macros that follow your workflow.
299|From wavetable to multisample
300|From your idea
304|What you need
305|What's in the archive
306|Wavetables, samples and multisamples in one instrument. Build your sound, shape its movement and connect it to your own effect rack.
307|Fewer detours.
308|How do I install the plugins?
312|Windows x64, Visual Studio 2022 with Desktop development with C++, and CMake 3.22 or newer. Source archives include JUCE and the other required libraries.
313|Windows download 
314|Select notes and change their pitch, timing, length or volume. Split and merge sections or copy notes to create additional harmonies.
315|Choose a shaper curve or draw the movement yourself.
316|Choose one of 16 quick-access curves or draw your own. Depth, Offset and Low Band Only control how the volume shaping is applied.
317|Extract the ZIP, copy the VST3 and rescan your plugins. Or open the included standalone.
318|Skip to content
319|Explore the open project 
320|Back into the track
321|Together as a suite.
323|into your session.
324|can start here.
325|a finished product.
333|to the dependencies.
335|← The Nexum Suite''')
class EnglishHTML(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.out=[]
 def handle_decl(self,d):self.out.append('<!'+d+'>')
 def handle_starttag(self,t,attrs):
  new=[]
  for k,v in attrs:
   if t=='html' and k=='lang':v='en'
   elif v is not None:v=translations.get(v,v)
   new.append(k if v is None else k+'="'+html.escape(v,quote=True)+'"')
  self.out.append('<'+t+(' '+' '.join(new) if new else '')+'>')
 def handle_endtag(self,t):self.out.append('</'+t+'>')
 def handle_startendtag(self,t,a):self.handle_starttag(t,a)
 def handle_data(self,d):self.out.append(html.escape(translations.get(d,d),quote=False))
 def handle_comment(self,d):self.out.append('<!--'+d+'-->')
for p in ROOT.glob('*.html'):
 t=EnglishHTML();t.feed(p.read_text(encoding='utf-8-sig'));p.write_text(''.join(t.out),encoding='utf-8')
js=ROOT/'assets/site.js';s=js.read_text(encoding='utf-8-sig')
for a,b in {'Menü':'Menu','HYBRID-SYNTHESIZER':'HYBRID SYNTHESIZER','MODULARES EFFEKTRACK':'MODULAR EFFECT RACK','entdecken':'explore','Kopiert ✓':'Copied ✓','Kopieren':'Copy','Bitte Text markieren':'Please select the text'}.items():s=s.replace(a,b)
js.write_text(s,encoding='utf-8')
(ROOT/'tools/web-english.json').write_text(json.dumps(translations,ensure_ascii=False,indent=2),encoding='utf-8')
print('Translated',len(translations),'website strings.')
