from pathlib import Path
import zipfile,hashlib,json,datetime
ROOT=Path(r'C:/Users/maxim/Desktop/Nexum Audio/Website')
BASE=Path(r'C:/Users/maxim/Desktop/VST3 Plugins')
SYNTH=Path(r'C:/Users/maxim/.codex/visualizations/2026/10/23/01a16876-066a-74f0-a735-fb0604030e6e/Serum2')
JUCE=SYNTH.parent/'external/JUCE'
license_text=(BASE/'NexumTune/third_party/AGPL-3.0.txt').read_text()
products=[('nexum','Nexum','0.12.0',SYNTH/'build/NexumSynth_artefacts/Release'),('fx','Nexum FX','0.12.0',SYNTH/'build/NexumFx_artefacts/Release'),('tune','Nexum Tune','0.4.1',BASE/'NexumTune/build/NexumTune_artefacts/Release'),('gate','Nexum Gate','1.0.0',BASE/'NexumGate/build/NexumGate_artefacts/Release')]
manifest={}
notes='''NEXUM AUDIO — OPEN-SOURCE DEVELOPMENT RELEASE\n\nOriginal Nexum, Nexum FX, Nexum Tune and Nexum Gate implementation:\nSPDX-License-Identifier: AGPL-3.0-only\nCopyright (c) 2026 Nexum Audio contributors.\n\nReleased under AGPL version 3 by the project owner. Third-party components keep\ntheir own terms. JUCE: AGPLv3 option; Rubber Band: GPLv2 or later; Zstandard:\nBSD/GPL dual licence; Catch2: BSL-1.0 (tests); bundled VST3 SDK: upstream licence.\nAll original component notices and full sources are in the companion source ZIP.\nNo user-imported sound packs, samples, wavetables or third-party preset packs\nare distributed in these packages. The plugin libraries can be populated by users.\n'''
(ROOT/'downloads/THIRD-PARTY-NOTICES.txt').write_text(notes)
def finish(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return {'file':path.name,'bytes':path.stat().st_size,'sha256':h.hexdigest()}
for slug,name,version,release in products:
 path=ROOT/'downloads'/f'nexum-{slug if slug!="nexum" else "synth"}-{version}-windows-x64.zip'
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  z.write(release/f'Standalone/{name}.exe',f'{name}/{name}.exe')
  bundle=release/f'VST3/{name}.vst3'
  for p in bundle.rglob('*'):
   if p.is_file():z.write(p,f'{name}/{name}.vst3/'+p.relative_to(bundle).as_posix())
  z.writestr(f'{name}/LICENSE.txt',license_text)
  z.writestr(f'{name}/THIRD-PARTY-NOTICES.txt',notes)
  z.writestr(f'{name}/README.txt',f'''{name} {version} — Windows x64\n\nVST3: copy the entire {name}.vst3 folder into\nC:/Program Files/Common Files/VST3/NEXUM/\nThen scan for plugins in your DAW.\n{name} {'is an instrument' if slug=='nexum' else 'is an audio effect'}.\nStandalone: launch {name}.exe from this extracted folder.\n\nFull corresponding source: nexum-suite-source-2026-11-03.zip\nWebsite: https://nexum-audio.com\n''')
 manifest[slug]=finish(path)|{'version':version}
 print(name,manifest[slug]['bytes'],flush=True)
source_path=ROOT/'downloads/nexum-suite-source-2026-11-03.zip'
with zipfile.ZipFile(source_path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 prefix='nexum-suite-source/'
 def addtree(folder,arc):
  if not folder.exists():return
  for p in folder.rglob('*'):
   if p.is_file() and not any(x in {'.git','build','dist','__pycache__','.cache'} for x in p.relative_to(folder).parts):z.write(p,prefix+arc+'/'+p.relative_to(folder).as_posix())
 def text(arc,value):z.writestr(prefix+arc,value)
 for folder in ['Source','Assets','External/zstd']:addtree(SYNTH/folder,'Nexum/'+folder)
 for p in SYNTH.glob('README*.md'):z.write(p,prefix+'Nexum/'+p.name)
 cm=(SYNTH/'CMakeLists.txt').read_text().replace('C:/Users/maxim/Desktop/VST3 Plugins/NexumDesign/include','${CMAKE_CURRENT_SOURCE_DIR}/../NexumDesign/include')
 text('Nexum/CMakeLists.txt',cm)
 for folder in ['src','tests','assets','docs','third_party']:addtree(BASE/'NexumTune'/folder,'NexumTune/'+folder)
 for folder in ['src','tests','assets']:addtree(BASE/'NexumGate'/folder,'NexumGate/'+folder)
 for project in ['NexumTune','NexumGate']:
  cm=(BASE/project/'CMakeLists.txt').read_text()
  cm=cm.replace(str(JUCE).replace('\\','/'),'${CMAKE_CURRENT_SOURCE_DIR}/../external/JUCE').replace('C:/Users/maxim/Desktop/VST3 Plugins/NexumDesign/include','${CMAKE_CURRENT_SOURCE_DIR}/../NexumDesign/include')
  text(project+'/CMakeLists.txt',cm)
  text(project+'/README.md',(BASE/project/'README.md').read_text())
 addtree(BASE/'NexumDesign/include','NexumDesign/include')
 addtree(JUCE,'external/JUCE')
 text('LICENSE.txt',license_text);text('THIRD-PARTY-NOTICES.txt',notes)
 for p in ['Nexum','NexumTune','NexumGate']:text(p+'/LICENSE.txt',license_text)
 text('README.md','''# Nexum Suite — source release, 2026-11-03\n\nNexum and Nexum FX share the canonical synthesis/effect implementation in Nexum/.\nTune and Gate are separate projects. Shared family UI: NexumDesign/include/.\nComplete JUCE, Rubber Band, Zstandard and Catch2 sources and notices are included.\nOriginal implementation: AGPL-3.0-only. See LICENSE.txt and THIRD-PARTY-NOTICES.txt.\n\n## Windows x64 build\nRequirements: Visual Studio 2022 with Desktop development with C++, CMake 3.22+.\nConfigure each project into its own build directory (do not add all JUCE projects\nto a single CMake build). From this folder, run:\n\n```powershell\ncmake -S Nexum -B build-synth -G "Visual Studio 17 2022" -A x64\ncmake --build build-synth --config Release --target NexumSynth_VST3 NexumSynth_Standalone NexumFx_VST3 NexumFx_Standalone --parallel 1\ncmake -S NexumTune -B build-tune -G "Visual Studio 17 2022" -A x64\ncmake --build build-tune --config Release --target NexumTune_VST3 NexumTune_Standalone NexumTuneTests --parallel 1\ncmake -S NexumGate -B build-gate -G "Visual Studio 17 2022" -A x64\ncmake --build build-gate --config Release --target NexumGate_VST3 NexumGate_Standalone NexumGateCheck --parallel 1\n```\n\nCMake paths have been made relative for this archive. Run tests with each project\nas the current working directory. The source supports the documented Windows\nx64 development builds; macOS/Linux binaries are not supplied.\n\nNo user content, presets imported from other products, API keys, DAW projects or\nlocal plugin settings are included. Default synthesis remains available without\nexternal content; populate sample/preset libraries with your own files.\n''')
manifest['source']=finish(source_path)
(ROOT/'downloads/releases.json').write_text(json.dumps(manifest,indent=2))
(ROOT/'downloads/SHA256SUMS.txt').write_text(''.join(v['sha256']+'  '+v['file']+'\n' for v in manifest.values()))
print('SOURCE',manifest['source']['bytes'],flush=True)
