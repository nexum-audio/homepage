from pathlib import Path
import json,re
root=Path(r'C:/Users/maxim/Desktop/Nexum Audio/Website/tools')
M={}
def pairs(s):
 for line in s.splitlines():
  if '|' in line:
   a,b=line.split('|',1);M[a]=b
pairs('''Alle Eintraege|All entries
Favoriten|Favorites
Alle Kategorien|All categories
Keine Kategorie|No category
Ordner verschoben|Folder moved
Eintrag umbenennen|Rename entry
Gelöscht / im Papierkorb. Der geladene Klang bleibt erhalten.|Moved to the Recycle Bin. The loaded sound is preserved.
Ordner im Papierkorb|Folder moved to the Recycle Bin
Ordner löschen?|Delete folder?
 mit allen enthaltenen Einträgen in den Papierkorb verschieben?| and all its entries to the Recycle Bin?
LÖSCHEN|DELETE
Bewertung / Kategorie gespeichert|Rating / category saved
Neuer Ordner...|New folder...
Ordner umbenennen...|Rename folder...
Ordner löschen...|Delete folder...
Ordner verschieben|Move folder
Neuer Ordner|New folder
Ordner angelegt|Folder created
Ordner umbenennen|Rename folder
Ordner umbenannt|Folder renamed
Umbenennen...|Rename...
Löschen|Delete
Verschieben|Move
Kategorie hinzufuegen...|Add category...
Kategorie umbenennen|Rename category
Kategorie entfernen|Remove category
Neue Kategorie|New category
Kategorie angelegt|Category created
Kategorie und Zuweisungen entfernt|Category and assignments removed
Kategorie umbenannt|Category renamed
Effektkette speichern|Save effect chain
Einzelnen Effekt speichern|Save single effect
Im Ziel-Rack ist kein Effekt zum Speichern.|The destination rack has no effect to save.
Suche nach Name, Ordner, Kategorie...|Search name, folder, category...
Bewertung|Rating
Kategorie|Category
 Sterne; erneut klicken entfernt die Bewertung| stars; click again to clear the rating
Eintraege oder Ordner hierher ziehen, um sie zu verschieben.|Drag entries or folders here to move them.
Doppelklick: laden. Ziehen: verschieben. Rechtsklick: verwalten.|Double-click: load. Drag: move. Right-click: manage.
ORDNER LÖSCHEN|DELETE FOLDER
Das Ziel-Rack ist leer.|The destination rack is empty.
Einzeleffekte und Effektketten speichern, importieren und per Doppelklick laden.|Save and import individual effects or chains. Double-click to load.
WAV-Wavetables als Ordner, ZIP oder Datei hinzufuegen|Add WAV wavetables as a folder, ZIP or file
SFZ-Instrumente mit ihren Sample-Dateien als Ordner, ZIP oder SFZ hinzufuegen|Add SFZ instruments and their samples as a folder, ZIP or SFZ
Speichern als: Neues Preset anlegen / Preset überschreiben|Save as: Create new preset / Overwrite preset
Preset speichern|Save preset
In anderes Pack verschieben|Move to another pack
Preset löschen|Delete preset
Gelöscht: |Deleted: 
 / im Papierkorb. Der geladene Klang bleibt erhalten.| / moved to the Recycle Bin. The loaded sound is preserved.
Preset umbenennen|Rename preset
Bitte zuerst ein neues eigenes Preset speichern.|Please save a new user preset first.
Preset überschrieben: |Preset overwritten: 
Doppelklick laden / VORSCHAU: MIDI-Clip|Double-click to load / PREVIEW: MIDI clip
Eintrag auswaehlen oder per Drag-and-drop in einen anderen Ordner verschieben|Select an entry or drag it into another folder
Keine passenden Eintraege. Ordner oder Filter wechseln.|No matching entries. Choose another folder or filter.
Das aktuelle Preset kann nicht überschrieben werden. Bitte zuerst ein neues Preset anlegen.|This preset cannot be overwritten. Create a new user preset first.
Das Preset konnte nicht gelesen werden.|The preset could not be read.
Die Zieldatei ist kein NoCTRL-Preset.|The destination file is not a compatible Nexum preset.
Ungültiger Preset-Zustand.|Invalid preset state.
Preset gespeichert; Metadaten-Datei konnte nicht aktualisiert werden.|Preset saved; the metadata file could not be updated.
Preset überschreiben|Overwrite preset
Rand Start|Random start
Audio importieren|Import audio
Startet Host-Play, sofern unterstuetzt. Capture wartet auf die laufende Timeline und endet bei Host-Stopp oder Positionssprung.|Requests host playback when supported. Recording waits for the timeline and ends when the host stops or seeks.
Auswahl an gleicher Position kopieren (Ctrl+D), danach Tonhoehe mit Ziehen oder Pfeiltasten aendern.|Duplicate the selection in place (Ctrl+D), then drag or use the arrow keys to change its pitch.
Vibrato-Reduktion: 0% Original, 100% maximale Glaettung. Anwenden auf Auswahl oder alle sicher erkannten Noten.|Vibrato reduction: 0% original, 100% maximum smoothing. Applies to selected or confidently detected notes.
Staerke der Tonhoehenkorrektur; gilt fuer Auswahl oder alle Noten|Pitch correction strength; applies to the selection or all notes
Bearbeitetes Audio in die Playlist ziehen. Vollstaendige Aufnahme, unabhaengig von Loop, Original-A/B und Monitorpegel.|Drag the edited audio into your playlist. Exports the full recording, independent of loop, original A/B and monitor level.
Bearbeitete Aufnahme als WAV speichern|Save edited recording as WAV
LOOP AUS|CLEAR LOOP
VIBRATO ANWENDEN|APPLY VIBRATO
KORRIGIEREN|CORRECT
AUDIO HERAUSZIEHEN|DRAG AUDIO OUT
WAV WIRD VORBEREITET|PREPARING WAV
WARTE AUF AUDIO...|WAITING FOR AUDIO...
ABBRECHEN|CANCEL
AUFNEHMEN|RECORD
NOTE / AUSWAHL|NOTE / SELECTION
TONHOEHENKORREKTUR|PITCH CORRECTION
Ziel |Target 
Konfidenz |Confidence 
Keine Note ausgewaehlt|No note selected
 Noten ausgewaehlt| notes selected
VIBRATO REDUZIEREN|REDUCE VIBRATO
0% Original / 100% ruhiger|0% original / 100% smoother
Auswahl, sonst alle Noten|Selection, otherwise all notes
Auswahl, sonst alle erkannten Noten|Selection, otherwise all detected notes
WAV / bearbeitete Aufnahme|WAV / edited recording
QUELLE|SOURCE
WERKZEUGE|TOOLS
SPEKTROGRAMM|SPECTROGRAM
NOTEN / PITCH EDITOR|NOTES / PITCH EDITOR
Host-Start angefordert. Aufnahme beginnt mit der laufenden Timeline...|Host playback requested. Recording starts with the timeline...
Aufnahme bereit - warte auf den naechsten laufenden Host-Audioblock.|Armed - waiting for the next playing host audio block.
Host hat Autostart abgelehnt. Aufnahme bereit: Play in FL/DAW druecken.|Host declined auto-start. Armed: press Play in your DAW.
Host-Autostart nicht verfuegbar. Aufnahme bereit: Play in FL/DAW druecken.|Host auto-start unavailable. Armed: press Play in your DAW.
Aufnahme laeuft |Recording 
 - synchron zur Host-Timeline| - synced to host timeline
Analyse |Analysis 
Audio wird gerendert |Rendering audio 
% - Vorschau folgt nach Fertigstellung|% - preview available when finished
WAV-Datei wird fuer Export und Drag-and-drop vorbereitet...|Preparing WAV for export and drag-and-drop...
Render vorgemerkt - vorherige Vorschau bleibt bis zur Fertigstellung erhalten|Render queued - previous preview remains available until completion
 s  |  Vorschau | s  |  Preview 
NOTEN|NOTES
SPEKTRUM|SPECTRUM
TEILEN|SPLIT
VERBINDEN|MERGE
LOESCHEN|DELETE
HOST-START SETZEN|SET HOST START
KOPIE|DUPLICATE
LOOP ENTFERNEN|CLEAR LOOP
AUDIO IMPORTIEREN|IMPORT AUDIO
Audio wird importiert...|Importing audio...
Monophone Analyse: |Monophonic analysis: 
 Kanal/Kanaele | | channel(s) | 
 erkannte Noten| detected notes
Import nicht moeglich: Mono/Stereo WAV, AIFF oder FLAC, maximal 5 Minuten.|Cannot import: use mono/stereo WAV, AIFF or FLAC, up to 5 minutes.
Lesefehler beim Audioimport|Audio import read error
WAV gespeichert: |WAV saved: 
WAV konnte nicht gespeichert werden: |Could not save WAV: 
Audioexport: |Audio export: 
Bereit - Audio importieren oder Eingang aufnehmen|Ready - import audio or record the input
Audio hier ablegen oder Eingang aufnehmen|Drop audio here or record the input
Klicken: Playhead   |   Ziehen: Loop|Click: playhead   /   Drag: loop
Tonhoehe geschaetzt|Estimated pitch
Keine Noten. Importiere eine monophone Aufnahme oder nutze Undo.|No notes. Import a monophonic recording or use Undo.
Kopieren (Ctrl+C)|Copy (Ctrl+C)
Einfuegen an Originalposition (Ctrl+V)|Paste at original position (Ctrl+V)
Duplizieren (Ctrl+D)|Duplicate (Ctrl+D)
+12 Halbtone|+12 semitones
-12 Halbtone|-12 semitones
Transponieren um...|Transpose by...
Auf Halbton korrigieren|Snap to semitone
Hier teilen|Split here
Vibrato 50% reduzieren|Reduce vibrato by 50%
Vibrato maximal reduzieren|Reduce vibrato fully
Originalvibrato wiederherstellen|Restore original vibrato
Halbtoene relativ: z.B. 0.25 fuer 25 Cent|Relative semitones: e.g. 0.25 for 25 cents
Abbrechen|Cancel
AUSWAHL|SELECT
TONHOEHE|PITCH
ZEITPOSITION|TIME
NOTENLAENGE|LENGTH
LAUTSTAERKE|GAIN
RADIERER|ERASE
Auswaehlen, Lasso, frei verschieben|Select, lasso, move freely
Nur Tonhoehe; Alt fuer Cent|Pitch only; Alt for cents
Nur Zeitposition verschieben|Move in time only
Laenge ziehen; links oder rechts|Drag length to the left or right
Nach oben lauter, unten leiser|Drag up for louder, down for quieter
Auf die gewuenschte Trennstelle klicken|Click where you want to split
Auswahl oder zwei Nachbarn verbinden|Merge the selection or two adjacent notes
Noten anklicken oder wegstreichen|Click or swipe over notes to erase
Nach unten ziehen: weniger Vibrato; oben: Original zurueck|Drag down to reduce vibrato; up to restore the original
Verknuepfungen entfernen|Remove links
Blau|Blue
Violett|Purple
Gelb|Yellow
Speichern|Save
Shift-Klick: ausgewaehltes Makro zuweisen. Makro-Verknuepfung hierher ziehen. Rechtsklick: Bereich / entfernen.|Shift-click: assign selected macro. Drag a macro link here. Right-click: range / unlink.
Verknuepfung entfernen|Remove link
Ausgangslautstaerke in dB|Output level in dB
Abstand zum Ziel:|Distance to target:
bis 10 ct|up to 10 ct
unsicher|uncertain
geschaetzt|estimated
Chromatisch|Chromatic
Dur|Major
Moll|Minor
Kein Audio vorhanden|No audio available
Exportordner kann nicht angelegt werden|Cannot create export folder
WAV-Datei kann nicht geschrieben werden|Cannot write WAV file
WAV-Encoder nicht verfuegbar|WAV encoder unavailable
Export verworfen: Bearbeitung geaendert|Export discarded: edits changed
Fehler beim Schreiben der WAV-Datei|Error writing WAV file
WAV-Datei kann nicht fertiggestellt werden|Cannot finalize WAV file
Live-Panningkurve und Abspielposition|Live pan curve and playback position
Kurve zeichnen / Rechtsklick: Factory-Kurve wiederherstellen|Draw a curve / Right-click: restore factory curve
Klick: Schritt an/aus / Ziehen: Lautstaerke / Shift: loeschen / Rechtsklick: Tie zum naechsten Schritt|Click: step on/off / Drag: level / Shift: erase / Right-click: tie to next step
Die Datei ist kein gueltiges Nexum-Gate-Preset.|This is not a valid Nexum Gate preset.
Die Datei konnte nicht gespeichert werden.|The file could not be saved.
Bitte einen Dateinamen ohne Sonderzeichen eingeben.|Please enter a filename without special characters.
Preset ueberschreiben?|Overwrite preset?
Preset loeschen?|Delete preset?
 in den Papierkorb verschieben?| to the Recycle Bin?
Die Datei konnte nicht geloescht werden.|The file could not be deleted.
Ungueltiges Nexum-Gate-Preset.|Invalid Nexum Gate preset.
Makro |Macro 
 zuweisen| assign
Makro-Verknuepfung entfernen|Remove macro link
Start und Ende in Parameter-Einheiten|Start and end in parameter units
Makro-Verknuepfung hierher ziehen / Shift-Klick: zuweisen / Rechtsklick: Bereich & Automation|Drag a macro link here / Shift-click: assign / Right-click: range & automation
BEWERTUNG|RATING
DATUM|DATE
DETAILS SPEICHERN|SAVE DETAILS
Details gespeichert|Details saved
Details gespeichert.|Details saved.
Eintrag umbenannt|Entry renamed
Eintrag verschoben|Entry moved
FX SPEICHERN|SAVE FX
FX-Preset gespeichert|FX preset saved
Geladen in |Loaded into 
Geladen in OSC |Loaded into OSC 
Gespeichert: |Saved: 
KATEGORIE|CATEGORY
KATEGORIEN|CATEGORIES
KETTE LADEN|LOAD CHAIN
KETTE SPEICHERN|SAVE CHAIN
Kategorien gespeichert|Categories saved
NEUER ORDNER|NEW FOLDER
NEUES PRESET|NEW PRESET
NEUES PRESET SPEICHERN|SAVE NEW PRESET
Neues Preset anlegen|Create new preset
ORDNER IMPORT|IMPORT FOLDER
ORDNER LOESCHEN|DELETE FOLDER
ORDNER-AKTIONEN|FOLDER ACTIONS
PRESET LOESCHEN|DELETE PRESET
LADEN|LOAD
UMBENENNEN|RENAME
ZIELORDNER / PACK|DESTINATION / PACK
Zyklus in der Hierarchie|Hierarchy contains a cycle
NEXUM darf kein Elternelement haben|NEXUM cannot have a parent
Design konnte nicht geschrieben werden|Could not write design
Design konnte nicht atomar ersetzt werden|Could not replace design atomically''')
# Fragments containing pipe characters need explicit entries.
M[' Kanal/Kanaele | ']=' channel(s) | '
M['Klicken: Playhead   |   Ziehen: Loop']='Click: playhead   |   Drag: loop'
M[' Noten | Ziehen: Ton/Zeit | Alt: Cent/frei | Rand: Laenge | Shift: Mehrfachauswahl']=' notes | Drag: pitch/time | Alt: cents/free | Edge: length | Shift: multi-select'
M[' | Ziel ']=' | Target '
M[' s | Konfidenz ']=' s | Confidence '
M[' s  |  Vorschau ']=' s  |  Preview '
# Only exact string literals are translated; parameter IDs, preset keys and paths are untouched.
roots=[Path(r'C:/Users/maxim/.codex/visualizations/2026/10/23/01a16876-066a-74f0-a735-fb0604030e6e/Serum2/Source'),Path(r'C:/Users/maxim/Desktop/VST3 Plugins/NexumTune/src'),Path(r'C:/Users/maxim/Desktop/VST3 Plugins/NexumTune/tests'),Path(r'C:/Users/maxim/Desktop/VST3 Plugins/NexumGate/src'),Path(r'C:/Users/maxim/Desktop/VST3 Plugins/NexumGate/tests'),Path(r'C:/Users/maxim/Desktop/VST3 Plugins/NexumDesign/include')]
count=0
for r in roots:
 for p in r.rglob('*'):
  if p.suffix not in ['.h','.cpp']:continue
  t=p.read_text(encoding='utf-8-sig')
  def sub(m):
   nonlocal_dummy=None
   s=m.group(1)
   if s in M:return '"'+M[s].replace('"',r'\"')+'"'
   return m.group(0)
  new=re.sub(r'"((?:[^"\\]|\\.)*)"',sub,t)
  if new!=t:p.write_text(new,encoding='utf-8');count+=1
(root/'plugin-english.json').write_text(json.dumps(M,ensure_ascii=False,indent=2),encoding='utf-8')
print('Translated',count,'source files;',len(M),'UI strings.')
