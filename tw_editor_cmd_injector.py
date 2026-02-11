"""
Two Worlds Editor - Command Injector v5.1
Requires: pip install pyautogui pygetwindow
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
import pyautogui
import time
import os
import threading
import json
import subprocess
import re
import shutil
import glob

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.02

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(SCRIPT_DIR, "tw_injector_config.json")

# ============================================================
# LANGUAGE
# ============================================================
LANG = {
  "en": {
    "title": "TW Editor CMD Injector",
    "file": "File", "tools": "Tools",
    "add_txt": "Add TXT file",
    "add_commands_as_button": "Add commands as button",
    "focus_auto": "Auto-detect window",
    "focus_window": "Select focus window",
    "start_editor": "Start Editor",
    "exit": "Exit",
    "settings": "Settings",
    "commands": "Commands",
    "help_menu": "Help", "guide": "Guide", "about_title": "About",
    "focus_label": "Focus:", "no_focus": "No window selected",
    "auto_focus": "Auto", "add_btn": "+ Add TXT",
    "ready": "Ready", "running": "Already running...",
    "no_target": "No target window found!",
    "file_empty": "File is empty",
    "focusing": "Focusing editor...",
    "auto_not_found": "No editor window found!",
    "focus_error": "Focus error:",
    "opening_console": "Opening console...",
    "executed": "commands executed!",
    "aborted": "Aborted (mouse in corner)",
    "error": "Error:",
    "focus_select_title": "Select Focus Window",
    "focus_select_info": "Select the target window:",
    "refresh": "Refresh", "manual_3s": "Manual (3s)", "select": "Select",
    "click_target": "Click on the target window!",
    "cmd_list_title": "TW Editor - Command List",
    "search": "Search:", "commands_in": "commands in",
    "categories": "categories", "matches": "matches",
    "dblclick_copy": "Double-click = copy | Right-click = menu",
    "copy": "Copy", "add_as_button": "Add as button",
    "mark": "Mark", "unmark": "Unmark",
    "marked_as_button": "Marked as button",
    "marked_count": "marked", "clear_marks": "Clear marks",
    "settings_title": "Settings",
    "delay_label": "Delay between commands (ms):",
    "console_key_label": "Console key:",
    "close_console_after": "Close console after execution",
    "always_on_top": "Always on top",
    "language": "Language:", "save_close": "Save && Close",
    "rename": "Rename", "remove": "Remove",
    "expand": "Edit commands", "read_defaults": "Read defaults",
    "enter_name": "Enter name:", "enter_btn_name": "Button name:",
    "auto_found": "Auto-detected:",
    "focus_mode": "Focus mode:",
    "mode_auto": "Auto-detect", "mode_manual": "Manual",
    "editor_path": "Editor .exe path:",
    "last_map": "Last map:",
    "map_converter": "Map to Mod Converter",
    "help_text": """TW Editor Command Injector v5.1

QUICK START:
1. Tool auto-detects the Two Worlds Editor
2. Click '+' to load a TXT file with commands
3. Click button to execute (clipboard paste!)

BUTTONS:
- Right-click > Edit: see all commands,
  change values, run individually
- Read defaults: send commands without values,
  paste console output to capture defaults
- D:value button resets to default

COMMAND LIST (Commands menu):
- Search all commands, right-click to add
- Mark multiple, combine as one button

MAP TO MOD (Tools menu):
- Automated conversion of editor maps to
  playable mods - set paths once in settings

TIPS:
- Commands use clipboard paste (instant!)
- STOP button + auto-stop on focus loss
- Mouse to top-left corner = emergency abort""",
    "about_text": "TW Editor CMD Injector v5.1\n\nFor the TW Modding Community.",
    # Map converter
    "mc_title": "Map to Mod Converter",
    "mc_step": "Step", "mc_start": "Start Conversion",
    "mc_cook": "Cook PhysX in Editor",
    "mc_gen_headers": "Generate Level Headers",
    "mc_copy_files": "Copy map files to Mods",
    "mc_copy_lhc": "Copy LevelHeaders.lhc",
    "mc_repack": "Run WD Repacker",
    "mc_done": "Conversion complete!",
    "mc_running": "Running...",
    "mc_sdk_path": "TwoWorldsSDK path:",
    "mc_game_path": "TW Game path (Steam):",
    "mc_saves_path": "TW Saves/Levels path:",
    "mc_wd_file": "Map Test EX.wd file:",
    "mc_repacker": "Tw1WDRepacker.exe:",
    "mc_info": "Automates the map-to-mod conversion.\nSet all paths, then click Start.",
    "mc_cook_info": "Sending PhysX cook commands to editor...",
    "mc_bat_info": "Running LevelHeadersCacheGen.bat...",
    "mc_copy_info": "Copying map files...",
    "mc_repack_info": "Running repacker...",
    "mc_select_maps": "Select maps to convert:",
    "mc_no_sdk": "SDK path not set!",
    "mc_no_game": "Game path not set!",
    "mc_no_saves": "Saves path not set!",
    "wiz_info_header": "What does this tool do?",
    "wiz_info_text": "This tool sends console commands to the Two Worlds Editor via clipboard paste.\n\n- Create buttons from TXT files or the built-in command database (1272 commands!)\n- Edit values, read current defaults, execute commands individually\n- Convert editor maps to playable mods with the Map-to-Mod converter\n\nThe tool auto-detects the editor window. Just start the editor, then use this tool.",
    "wiz_path_header": "Editor Path (optional)",
    "wiz_path_info": "Set the path to TwoWorldsEditor.exe to launch it from this tool.\nYou can also set this later in Settings.",
    "wiz_browse": "Browse...",
    "wiz_next": "Next >>",
    "wiz_back": "<< Back",
    "wiz_finish": "Start!",
  },
  "de": {
    "title": "TW Editor CMD Injector",
    "file": "Datei", "tools": "Tools",
    "add_txt": "TXT hinzufuegen",
    "add_commands_as_button": "Befehle als Button",
    "focus_auto": "Auto-Erkennung",
    "focus_window": "Fenster waehlen",
    "start_editor": "Editor starten",
    "exit": "Beenden",
    "settings": "Einstellungen",
    "commands": "Commands",
    "help_menu": "Hilfe", "guide": "Anleitung", "about_title": "Ueber",
    "focus_label": "Fokus:", "no_focus": "Kein Fenster",
    "auto_focus": "Auto", "add_btn": "+ TXT hinzufuegen",
    "ready": "Bereit", "running": "Laeuft bereits...",
    "no_target": "Kein Zielfenster gefunden!",
    "file_empty": "Datei ist leer",
    "focusing": "Fokussiere Editor...",
    "auto_not_found": "Kein Editor-Fenster gefunden!",
    "focus_error": "Fokus-Fehler:",
    "opening_console": "Oeffne Konsole...",
    "executed": "Befehle ausgefuehrt!",
    "aborted": "Abgebrochen (Maus in Ecke)",
    "error": "Fehler:",
    "focus_select_title": "Fenster waehlen",
    "focus_select_info": "Zielfenster auswaehlen:",
    "refresh": "Aktualisieren", "manual_3s": "Manuell (3s)", "select": "Waehlen",
    "click_target": "Jetzt auf Zielfenster klicken!",
    "cmd_list_title": "TW Editor - Befehlsliste",
    "search": "Suche:", "commands_in": "Befehle in",
    "categories": "Kategorien", "matches": "Treffer",
    "dblclick_copy": "Doppelklick = kopieren | Rechtsklick = Menue",
    "copy": "Kopieren", "add_as_button": "Als Button",
    "mark": "Markieren", "unmark": "Demarkieren",
    "marked_as_button": "Markierte als Button",
    "marked_count": "markiert", "clear_marks": "Markierungen loeschen",
    "settings_title": "Einstellungen",
    "delay_label": "Delay zwischen Befehlen (ms):",
    "console_key_label": "Konsolen-Taste:",
    "close_console_after": "Konsole nach Ausfuehrung schliessen",
    "always_on_top": "Immer im Vordergrund",
    "language": "Sprache:", "save_close": "Speichern && Schliessen",
    "rename": "Umbenennen", "remove": "Entfernen",
    "expand": "Befehle bearbeiten", "read_defaults": "Defaults lesen",
    "enter_name": "Name eingeben:", "enter_btn_name": "Button-Name:",
    "auto_found": "Erkannt:",
    "focus_mode": "Fokus-Modus:",
    "mode_auto": "Auto-Erkennung", "mode_manual": "Manuell",
    "editor_path": "Editor .exe Pfad:",
    "last_map": "Letzte Map:",
    "map_converter": "Map zu Mod Konverter",
    "help_text": """TW Editor Command Injector v5.1

SCHNELLSTART:
1. Tool erkennt den Editor automatisch
2. '+' fuer TXT-Datei mit Befehlen
3. Button klicken (Clipboard-Paste!)

BUTTONS:
- Rechtsklick > Bearbeiten: Commands sehen,
  Werte aendern, einzeln ausfuehren
- Defaults lesen: Commands ohne Werte senden,
  Konsolenausgabe einfuegen
- D:wert Button setzt auf Default zurueck

MAP ZU MOD (Tools Menue):
- Automatische Konvertierung von Editor-Maps
  zu spielbaren Mods

TIPPS:
- Clipboard-Paste (sofort!)
- STOP Button + Auto-Stop bei Fokusverlust
- Maus in Ecke = Notfall-Abbruch""",
    "about_text": "TW Editor CMD Injector v5.1\n\nFuer die TW Modding Community.",
    "mc_title": "Map zu Mod Konverter",
    "mc_step": "Schritt", "mc_start": "Konvertierung starten",
    "mc_cook": "PhysX im Editor kochen",
    "mc_gen_headers": "Level-Headers generieren",
    "mc_copy_files": "Map-Dateien nach Mods kopieren",
    "mc_copy_lhc": "LevelHeaders.lhc kopieren",
    "mc_repack": "WD Repacker ausfuehren",
    "mc_done": "Konvertierung abgeschlossen!",
    "mc_running": "Laeuft...",
    "mc_sdk_path": "TwoWorldsSDK Pfad:",
    "mc_game_path": "TW Game Pfad (Steam):",
    "mc_saves_path": "TW Saves/Levels Pfad:",
    "mc_wd_file": "Map Test EX.wd Datei:",
    "mc_repacker": "Tw1WDRepacker.exe:",
    "mc_info": "Automatisiert die Map-zu-Mod Konvertierung.\nPfade setzen, dann Start klicken.",
    "mc_cook_info": "Sende PhysX-Befehle an Editor...",
    "mc_bat_info": "Fuehre LevelHeadersCacheGen.bat aus...",
    "mc_copy_info": "Kopiere Map-Dateien...",
    "mc_repack_info": "Fuehre Repacker aus...",
    "mc_select_maps": "Maps zum Konvertieren auswaehlen:",
    "mc_no_sdk": "SDK-Pfad nicht gesetzt!",
    "mc_no_game": "Game-Pfad nicht gesetzt!",
    "mc_no_saves": "Saves-Pfad nicht gesetzt!",
    "wiz_info_header": "Was macht dieses Tool?",
    "wiz_info_text": "Dieses Tool sendet Konsolenbefehle an den Two Worlds Editor per Clipboard-Paste.\n\n- Buttons aus TXT-Dateien oder der eingebauten Datenbank erstellen (1272 Befehle!)\n- Werte bearbeiten, aktuelle Defaults lesen, Befehle einzeln ausfuehren\n- Editor-Maps zu spielbaren Mods konvertieren mit dem Map-zu-Mod Konverter\n\nDas Tool erkennt das Editor-Fenster automatisch. Einfach Editor starten und loslegen.",
    "wiz_path_header": "Editor-Pfad (optional)",
    "wiz_path_info": "Pfad zur TwoWorldsEditor.exe setzen um den Editor von hier zu starten.\nKannst du auch spaeter in den Einstellungen machen.",
    "wiz_browse": "Durchsuchen...",
    "wiz_next": "Weiter >>",
    "wiz_back": "<< Zurueck",
    "wiz_finish": "Los!",
  },
}

# ============================================================
# COMMAND DATABASE
# ============================================================
COMMAND_CATEGORIES = {
    "Editor - Misc": [
        "editor.KbdScroll", "editor.KbdView", "editor.KbdRotate",
        "editor.KbdZoom", "editor.MouseScroll", "editor.MButtonScroll",
        "editor.WheelZoom", "editor.MouseRotate", "editor.MouseView",
        "editor.MouseZoom", "editor.ScrollDistDiv", "editor.ScrollDistDivMin",
        "editor.ScrollDistDivMax", "editor.ZoomDistDiv", "editor.ZoomDistDivMin",
        "editor.ZoomDistDivMax", "editor.TextFontName", "editor.TextFontHeight",
        "editor.TextFontWeight", "editor.TextFontCharset", "Editor.Update",
        "Editor.AddCreateObjectsLockedTexture", "Editor.SetDrawMapObjects", "Editor.UpdateDrawMapObjects",
        "editor.TestConsoleCmd", "editor.stepidleunit",
    ],
    "Editor - Objects & Markers": [
        "editor.MapMarkerSize", "Editor.AddMesh", "Editor.CountObjects",
        "Editor.DeleteAllObjects", "Editor.SaveRS", "Editor.LoadRS",
        "Editor.StartRS", "Editor.ReplaceObject", "Editor.UpdateStandPositions",
        "Editor.SetCreateRect", "Editor.SetCreateMinMaxZ", "Editor.CreateObjectsOnArea",
        "Editor.ResetCreateObjectsOnArea", "Editor.DeleteObjectsOnArea", "Editor.CreateObjectsNearObjectsOnArea",
        "Editor.SetCreateObjectsOnType", "Editor.AddZToAll", "Editor.AddZToAll2",
        "Editor.SetMissingObjectMarkersNumbers", "Editor.DeleteMarker", "Editor.DeleteBadObjectMarkers",
        "Editor.DeleteBadMarkers", "Editor.RecalcObjectsCount", "Editor.UseCalcObjectsCount",
        "Editor.CalcOnlyActiveWorldObjectsCount", "Editor.DeleteObjectsOnEdges", "Editor.DeleteObjectsOnEdgesMargin",
        "Editor.SetDrawMapMarkers", "editor.BuildInsideHouseObjectsDef", "editor.WriteInsideHouseObjectsDef",
        "editor.LoadInsideHouseObjectsDef", "editor.ClearObjectsInsideHouse", "editor.CreateObjectsInsideHouseFromDef",
        "editor.TraceUsedObjects", "editor.TraceIntersectGates",
    ],
    "Editor - Level Management": [
        "Editor.SinglePlayer", "Editor.CheckOverwriteWDLevels", "Editor.ImportOldLevel",
        "Editor.ExportBin", "Editor.ImportBin", "Editor.SetLevelSpecialFlags",
        "Editor.GetLevelSpecialFlags", "Editor.SetLevelInfoText", "Editor.GetLevelInfoText",
        "Editor.WriteCreateLevelsScript", "Editor.LoadLevel", "Editor.SetConnectedLevels",
        "Editor.SaveLevel", "Editor.SaveAllLevels", "Editor.SaveLevelIfEAX",
        "Editor.ForEachLevel", "Editor.ForEachNewLevel", "Editor.ForEachUndergroundLevel",
        "Editor.ForEachSurfaceLevel", "Editor.ForEachLevelWithWater", "Editor.LoadRightConnectedLevel",
        "Editor.LoadLeftConnectedLevel", "Editor.LoadBottomConnectedLevel", "Editor.LoadTopConnectedLevel",
        "Editor.MaxLoadLevelsCnt", "Editor.DumpCS", "Editor.FillCS",
        "Editor.ClearDisabled", "Editor.ClearLockedVertexes", "Editor.LabelNotDisabledPassableFromMarkers",
        "Editor.LoadLevelWithObjects", "Editor.LockVertexesWithConnectedLevel", "Editor.CopyAltitudeFromConnected",
        "Editor.CopyEdgeFromConnected", "Editor.CopyColorFromConnected", "Editor.CopyTexturesFromConnected",
        "Editor.CookAnyLevelName", "Editor.IgnoreLevelsCheckouts", "Editor.SetLevelsSourceDir",
        "Editor.SetLevelsBackupDir", "Editor.SetLevelsSourceUsers", "Editor.OldCheckinMinutes",
        "Editor.JoinLevels", "Editor.SetLevelSize", "Editor.GenerateBlocksFiles",
        "editor.SaveAllLevelsToTexture", "editor.CreateEditorLevelTerrain", "editor.SaveLevelBmp",
    ],
    "Editor - Heightmap & Terrain": [
        "Editor.LoadBmp", "Editor.LoadRaw", "Editor.SaveRaw",
        "Editor.MakeAverageAltitude", "Editor.LoadHMap", "Editor.SaveHMap",
        "Editor.NewBrushSmooth", "Editor.NewBrushSmooth2", "Editor.InitializeSelection",
        "Editor.AltForceMul", "Editor.InitPlaneHeight", "Editor.IncPlaneHeight",
        "Editor.IncAngle", "Editor.PikePower", "Editor.SharpAngle",
        "Editor.MarginLine", "Editor.GenTerrain", "Editor.UseHeightmapMaxSize",
    ],
    "Editor - ColorMap & Textures": [
        "Editor.LoadColorMap", "Editor.SaveColorMap", "Editor.SaveAlphas",
        "Editor.RecreateAllTerrainTexturesBitmaps", "Editor.ColorFill", "Editor.ColorTexture",
        "Editor.ReplaceColor", "Editor.ReplaceColorOnDisabledTerrain", "Editor.FillWorldWithColor",
        "Editor.ColorGoodSel", "Editor.CleanupInvisibleTextures", "Editor.SetTextureOnObjects",
        "Editor.AutoTextureEx", "Editor.TexMixerEx1", "Editor.TexMixerEx2",
        "Editor.ReplaceTexture", "Editor.ReplaceTexSet", "Editor.TextureWherePassable",
        "Editor.TextureFromBitmap", "Editor.TextureFromBitmapEx", "Editor.LockTexture",
        "Editor.FixupTextureEdges",
    ],
    "Editor - Grass & Water": [
        "Editor.DeleteGrass", "Editor.DeleteLava", "Editor.AddGrassOnTexture",
        "Editor.RemoveGrassWhereTexture", "Editor.RemoveGrassWhereWater", "Editor.BlurGrass",
        "Editor.ClampGrassToLimit", "Editor.ReplaceGrass", "Editor.SetGrassTexture",
        "Editor.SetWaterH", "Editor.SetWaterColor", "Editor.RemoveLocalFog",
    ],
    "Editor - Cutscenes & Tracks": [
        "Editor.MoveTrack", "Editor.ScaleTrackTime", "Editor.ConvertCameraTracks",
        "Editor.ImportCutsceneMeshes", "Editor.SaveCutsceneMeshes", "Editor.LoadCutsceneMeshes",
    ],
    "Editor - CookPhysX": [
        "Editor.CookPhysX", "Editor.CookPhysX.XBox", "Editor.CookPhysX.PS3",
        "Editor.CookPhysX.Wii", "Editor.CookPhysX.PC", "editor.cookphysx.pc_xbox",
        "Editor.CookPhysX.Mode", "Editor.CookPhysX.Strength", "Editor.CookPhysX.TrunkRadMul",
        "Editor.CookPhysX.TrunkHeight", "Editor.CookPhysX.Overwrite", "Editor.CookPhysX.ObjectMul",
        "Editor.CookPhysX.WallMul", "Editor.CookPhysX.CorrMul", "Editor.CookPhysX.WallCorrMul",
        "Editor.CookPhysX.MultiInst", "Editor.CookPhysX.LODMinErr", "Editor.CookPhysX.LODMedErr",
    ],
    "Editor - EAX & Audio": [
        "Editor.ClearEAXEnvironment", "Editor.FillEAXEnvironment", "Editor.EAXRangeMax",
        "Editor.SaveEAX", "Editor.LoadEAX",
    ],
    "Settings & System": [
        "checkdiskfreespace", "LoadLevelMargin", "UnloadLevelMargin",
        "LoadDistantLandMargin", "LoadNeighbourDistantLandMargin", "UnloadNeighbourDistantLandMargin",
        "MaxWorldsPreparingLoadDataCnt", "g_use_mxLogger", "g_use_mxError",
        "UseOutputDebugString", "TraceStepping", "AllowStepPause",
        "SetConsoleText", "SetLowConsoleText", "SetConsole2Text",
        "ConsoleTicks", "ConsoleAddToCurrText", "EnableInterface",
        "ShowInterface", "SetUpdateIDAsName", "AllowCreateWithBadSubObj",
        "settings.SetOption", "settings.DumpShortcuts", "settings.DefAntialiasingMode_0",
        "settings.DefAntialiasingMode_1", "settings.DefAntialiasingMode_2", "settings.ShowInfoToolTips",
        "CAsyncTexLoader.MaxTexInLoadItem", "cpu_UseOneProcessor", "cpu_UsePerformanceCounter",
        "cpu_UseRDTSC", "cpu_UseTickCount", "cpu_FixBadRTC",
        "CSStream.DefBufferSize", "CSBuffer.DefStretchSize", "CSWDFile.LogOpenFiles",
        "Console.MaxHistory", "AddFileLineToAssertToTrace", "DBG.AddStamp",
        "DBG.RemStamp", "DBG.SetStamp", "SkyBox.SkydomeRadius",
        "SkyBox.SkydomeDeltaX", "SkyBox.SkydomeDeltaY", "SkyBox.CloudsPower",
        "SkyBox.ReflectionScheme", "SkyBox.HorizonR", "SkyBox.HorizonO",
        "SkyBox.HorizonH", "SkyBox.RainBoxSize", "SkyBox.RainFallSpeed",
        "SkyBox.RainFallMin", "SkyBox.RainCNoise", "SkyBox.SkyVSD",
        "SkyBox.SkyRNGIN", "SkyBox.SkyRNGOUT", "SkyBox.SkyANG1",
        "SkyBox.SkyANG2", "asyncload.MaxQueuedDataSize",
    ],
    "Graph - Misc": [
        "graph.morphtime", "graph.minrate", "graph.mouse",
        "Graph.selection.width", "Graph.selection.MaxObjectSelWidth", "Graph.ShootAimPosX",
        "Graph.ShootAimPosY", "Graph.MagicAimPosX", "Graph.MagicAimPosY",
        "graph.WindSpeedMul", "graph.StepGameAheadWidth", "graph.StepGameAheadHeight",
        "graph.DumpUnreleased", "graph.MeshInterfaceFOVtexture", "graph.MeshInterfaceFOVrender",
        "graph.DisplayXSysUIDrawObjRangeMul", "graph.UnloadNetworkChannelRemoteHeroesAddDistance", "graph.CorrectFeetSlotDz",
    ],
    "Display & Stats": [
        "Stats.PE", "Stats.ObjCnt", "Stats.MemCnt",
        "display.XY", "display.show", "display.FPS",
        "display.console", "display.clear", "display.Printf",
        "display.PrintXY", "Stats", "Stats.ShowMs",
        "Stats.ShowMax", "Stats.mem", "Stats.AutoClear",
        "Stats.AutoClearMax", "Stats.Register", "Stats.Unregister",
        "Stats.Clear",
    ],
    "Engine - Fog & Atmosphere": [
        "graph.fogenable", "graph.enablefog", "graph.fogcolor",
        "Engine.WEffAtmosphere", "Engine.DebugRain", "Engine.DebugSnow",
        "Engine.ATMCLF", "Engine.SetFogParams", "Engine.SetFogColor",
        "SkyBox.FogHazePower", "SkyBox.FogHazeFactor", "SkyBox.FogHazePowFactor",
    ],
    "Graph - Mesh Loading": [
        "graph.ClearCache", "graph.PreLoadMeshesTicks", "graph.UnloadInvisibleMeshesTicks",
        "graph.PreLoadMeshesAddDistance", "graph.UnloadInvisibleMeshesAddDistance", "graph.UnloadInvisibleNotRenderedMeshesAddDistance",
        "graph.SpawnAllowPreLoadDist2Range", "graph.SpawnForceLoadUnitDistance", "graph.UnloadObjectParticlesTicks",
        "graph.TracePreLoadUnload", "graph.DrawNotVisiblePassive",
    ],
    "Graph - Sun/Moon & Day Cycle": [
        "graph.SkyBoxColorFadeFromFogPerTick", "graph.SunAlphaStart", "graph.SunAlphaRange",
        "graph.SunBetaStart", "graph.SunBetaRange", "graph.MoonAlphaStart",
        "graph.MoonAlphaRange", "graph.MoonBetaStart", "graph.MoonBetaRange",
    ],
    "Graph - Display & HUD": [
        "graph.DrawNetworkChannelRemoteHeroesMaxDistance", "graph.DrawNetworkChannelRemoteHeroesMaxCount", "graph.DrawNetworkChannelRemoteHeroesNames",
        "graph.DrawNetworkChannelLocalHeroesNames", "graph.DrawNetworkGameRemoteHeroesNames", "graph.DrawNetworkGameLocalHeroesNames",
        "graph.DrawHeroesNameMaxDistA", "graph.DrawHeroesNameAddHeadZ", "graph.DrawHeroesNameAddHeadDxy",
        "graph.DrawHeroesNameScreenMargin", "graph.DrawHeroesNameFont3DHeight", "graph.DrawHeroesNameMinFontHeight",
        "graph.DrawHeroesNameMaxFontHeight", "graph.DrawHeroesNameBkgColor", "graph.DrawNetworkGameMonstersLabels",
        "graph.DrawMonstersLabelMaxDistA", "graph.DrawMonstersLabelAddHeadZ", "graph.DrawLevelUpIcon",
        "graph.DrawHitInfoInCampaign", "graph.DrawHitInfoInNetwork", "graph.DrawHitInfoOnLocalHero",
        "graph.DrawHitInfoOnNetworkHero", "graph.DrawHitInfoOnUnit", "graph.DrawHitInfoOnUnitBase",
        "graph.DrawHitInfoFromLocalHero", "graph.DrawHitInfoFromNetworkHero", "graph.DrawHitInfoFromUnit",
        "graph.DrawHitInfoMaxDistA", "graph.DrawHitInfoAddHeightZ", "graph.DrawHitInfoScreenMargin",
        "graph.DrawHitInfoFont3DHeight", "graph.DrawHitInfoMinFontHeight", "graph.DrawHitInfoMaxFontHeight",
        "graph.DrawHitInfoBkgColor", "graph.DrawHitInfoDefTextColor", "graph.DrawHitInfoTicks",
        "graph.DrawHitInfoStartFadeTick", "graph.DrawHitInfoMoveUpZ", "graph.DrawLocalHeroCtrl",
        "graph.TextNameScale", "graph.ForceHigherBoxesHeight",
    ],
    "Sound": [
        "sound.MoveListenerToCenterMul", "sound.play", "sound.WindRainVolumeIncrease",
        "sound.WindRainVolumeDecrease", "sound.RainSoundDx", "sound.RainSoundDy",
        "sound.RainSoundDz", "sound.WindSoundDx", "sound.WindSoundDy",
        "sound.WindSoundDz", "sound.RainInsideHouseVolumeMul", "sound.WindInsideHouseVolumeMul",
        "sound.SoundsOutsideHouseVolumeMul", "sound.SoundsInsideHouseVolumeMul", "sound.EAXEnvironmentDefaultInsideHouse",
        "sound.EAXEnvironmentOpenSpace", "sound.EAXEnvironmentUnderground", "cutscene.music",
        "cutscene.allmusic", "sound.TalkDialogWaveMinDist", "sound.TalkDialogWaveMaxDist",
        "sound.ChatDialogWaveMinDist", "sound.ChatDialogWaveMaxDist", "sound.HeroTalkWaveMinDist",
        "sound.HeroTalkWaveMaxDist", "sound.UnitTalkWaveMinDist", "sound.UnitTalkWaveMaxDist",
        "sound.TraceHeroTalk",
    ],
    "Interface - Camera": [
        "interface.Camera.CameraZoffsetMinH", "interface.Camera.Damper", "interface.Camera.CollDeadZoneRange",
        "interface.Camera.CollZOffset", "interface.Camera.CollBackTime", "interface.Camera.HeroTrackingSpeed",
        "interface.Camera.HeroTrackingDeadZone", "interface.Camera.HeroTrackingSuddenDeadZone", "interface.Camera.HeroTrackingRotFuncSpeed",
        "interface.Camera.BetaMoving", "interface.Camera.BetaFighting", "interface.Camera.fCameraBetaSpeed",
        "interface.Camera.CameraZOffsetMin", "interface.Camera.CameraZOffsetMax", "interface.Camera.CameraZOffsetSpeedCol",
        "interface.Camera.CameraZOffsetSpeed", "interface.Camera.CameraZOffsetMinTime", "interface.Camera.CameraZOffsetLen",
        "interface.Camera.CameraZOffsetDamping", "interface.Camera.HideHeroDist", "interface.Camera.HideHeroDistMax",
        "interface.Camera.SmoothMounting", "interface.Camera.SmoothMounting.Speed", "interface.Camera.SmoothMounting.MinSpeed",
        "interface.Camera.SmoothMounting.BETA", "interface.Camera.FPP.FOV", "interface.Camera.XInputThumbCameraMulX",
        "interface.Camera.XInputThumbCameraMulY", "interface.Camera.XInputShootAimCameraMulX", "interface.Camera.XInputShootAimCameraMulY",
        "interface.Camera.MouseRotate", "interface.Camera.MouseView", "interface.Camera.KbdRotate",
        "interface.Camera.KbdView", "interface.Camera.KbdZoom", "interface.Camera.WheelZoomIn",
        "interface.Camera.WheelZoomOut", "interface.Camera.WheelDirection", "interface.Camera.OneWheelZoomInMin",
        "interface.Camera.OneWheelZoomInMax", "interface.Camera.OneWheelZoomOutMin", "interface.Camera.OneWheelZoomOutMax",
        "interface.Camera.AddZ", "interface.Camera.AddFPPZ", "interface.Camera.AddZOnHorse",
        "interface.Camera.AddFPPZOnHorse", "interface.Camera.ZoomMin", "interface.Camera.ZoomMax",
        "interface.Camera.ViewAngleMin", "interface.Camera.ViewAngleMax", "interface.Camera.MinClampDistance",
        "interface.Camera.GetAltRange", "interface.Camera.GetAltRangeRetMax", "interface.Camera.GetAltAddAlt0",
        "interface.Camera.GetAltAddAlt1", "interface.Camera.GetAltAddAlt1Dist", "interface.Camera.AddBoxMargin",
        "interface.Camera.SlowDown.AngleMax", "interface.Camera.SlowDown.AngleTime", "interface.Camera.SlowDown.AngleTestValTime",
        "interface.Camera.SlowDown.AngleTimePow", "interface.Camera.SlowDown.AngleUseAvrgSpeed", "interface.Camera.SlowDown.AngleAvrgPow",
        "interface.Camera.SlowDown.AngleAvrgValForMaxTime", "interface.Camera.SlowDown.ViewAngleMax", "interface.Camera.SlowDown.ViewAngleTime",
        "interface.Camera.SlowDown.ViewAngleTestValTime", "interface.Camera.SlowDown.ViewAngleTimePow", "interface.Camera.SlowDown.ViewAngleUseAvrgSpeed",
        "interface.Camera.SlowDown.ViewAngleAvrgPow", "interface.Camera.SlowDown.ViewAngleAvrgValForMaxTime", "interface.Camera.SlowDown.DistanceMax",
        "interface.Camera.SlowDown.DistanceTime", "interface.Camera.SlowDown.DistanceTestValTime", "interface.Camera.SlowDown.DistanceTimePow",
        "interface.Camera.SlowDown.DistanceUseAvrgSpeed", "interface.Camera.SlowDown.DistanceAvrgPow", "interface.Camera.SlowDown.DistanceAvrgValForMaxTime",
        "interface.Camera.SlowDown.AngleToHorseMax", "interface.Camera.SlowDown.AngleToHorseTime", "interface.Camera.SlowDown.AngleToHorseTestValTime",
        "interface.Camera.SlowDown.AngleToHorseTimePow", "interface.Camera.SlowDown.AngleToHorseUseAvrgSpeed", "interface.Camera.SlowDown.AngleToHorseAvrgPow",
        "interface.Camera.SlowDown.AngleToHorseAvrgValForMaxTime", "interface.Camera.SlowDown.AngleOnMoveMax", "interface.Camera.SlowDown.AngleOnMoveTime",
        "interface.Camera.SlowDown.AngleOnMoveTestValTime", "interface.Camera.SlowDown.AngleOnMoveTimePow", "interface.Camera.SlowDown.AngleOnMoveUseAvrgSpeed",
        "interface.Camera.SlowDown.AngleOnMoveAvrgPow", "interface.Camera.SlowDown.AngleOnMoveAvrgValForMaxTime", "interface.Camera.ZoomInDistanceSpeed",
        "interface.Camera.ZoomOutDistanceSpeed", "interface.Camera.MaxXYMouseMul", "interface.Camera.MaxMouseMoveDxy",
        "interface.Camera.MaxMouseStepTime", "interface.Camera.ClampDistDestAngle", "interface.Camera.SwitchFPPDelay",
        "interface.Camera.MinShootAimFOV", "interface.Camera.ShootAimFOVSpeed", "interface.Camera.MouseSlowDownInMinAimFOV",
        "interface.Camera.OffsetInShootAimMinZoom", "interface.Camera.OffsetInShootAimMaxZoom", "interface.Camera.OffsetInShootAimFPPMode",
        "interface.Camera.OffsetInShootAimMulMinAimFOV", "interface.Camera.OffsetSpeed", "interface.Camera.RotateToHorse",
        "interface.Camera.RotateToHorseAngleDiff", "interface.Camera.RotateToHorseSpeed", "interface.Camera.RotateToHorseSpeedFast",
        "interface.Camera.RotateToHorseSpeedSlowDownTime", "interface.Camera.RotateToHorseSpeedSlowDownDiv", "interface.Camera.RotateOnMoveXInput",
        "interface.Camera.RotateOnMoveSpeed", "interface.Camera.RotateOnMoveMinX", "interface.Camera.RotateOnMovePlusYMul",
        "interface.Camera.RotateOnMoveMinusYMul", "interface.Camera.DistanceMulNearLeafsFade",
    ],
    "Graph - Camera": [
        "Graph.EnableMargin", "Graph.Camera.LookAtZRange1", "Graph.Camera.LookAtZRange2",
        "Graph.Camera.ZoomMin", "Graph.Camera.ZoomMax", "Graph.Camera.AngleMin",
        "Graph.Camera.AngleMax", "Graph.Camera.ViewAngleMinZ", "Graph.Camera.ForceXY",
        "Graph.Camera.FrictionXY", "Graph.Camera.ForceH", "Graph.Camera.FrictionH",
        "Graph.EnableCameraViewLimits", "Graph.AutoZoomCamera", "Graph.Camera.AddZ",
        "LookAt", "DelayedLookAt", "ForcedLookAt",
        "ForcedDelayedLookAt", "ResetForcedLookAt", "Graph.FreeCamera",
        "Graph.CameraGetPos", "Graph.CameraSetPos", "Graph.PlayTrack",
        "Graph.CameraShake.AmplitudeMul", "Graph.CameraShake.FrameRate",
    ],
    "Graph - AVI & Video Capture": [
        "graph.avi.width", "graph.avi.height", "graph.avi.framerate",
        "graph.avi.MaxAviSizeMB", "graph.avi.setup", "graph.avi.start",
        "graph.avi.capture", "graph.avi.stop", "graph.avi.pause",
        "graph.avi.enablekeys", "graph.avi.dir", "graph.avi.StartCaptureInput",
        "graph.avi.StopCaptureInput", "graph.avi.CaptureInput", "graph.avi.ReplayCapturedInput",
        "graph.avi.ReplayCapturedInputAudio", "graph.avi.ReplayCapturedInputVideo", "graph.avi.enableInputKeys",
        "graph.avi.StartAudioCaptureDelayMs", "graph.avi.StopAudioCaptureDelayMs",
    ],
    "Interface - UI & Misc": [
        "interface.OutputLines", "interface.FullScreenConsoleWidth", "interface.MinTextOnlyDialogTicksLength",
        "interface.MaxTextOnlyDialogTicksLength", "interface.TextOnlyDialogTicksPerChar", "interface.GapBetweenWaveDialogsTicks",
        "interface.DelayAfterLastWaveDialogTicks", "interface.OtherCommandAngleToObject", "interface.TooltipObjectAngleToObject",
        "interface.TargetObjectBorderMargin", "interface.WheelNextUsableCommandDir", "interface.TraceDialog",
        "interface.DialogCameraBaseHeroHeadHeight", "interface.DialogCameraBaseHeroOnHorseHeadHeight", "interface.ShowUserChatTooltipsTimeMs",
        "interface.ShowUserChatTooltipsDistA", "interface.DreamlandEntranceChangeSpeed", "interface.ShootTurnToCamera",
        "interface.ForceMoveStepForward", "interface.TestDialogCameraTrack", "interface.StopTestDialogCameraTrack",
        "interface.ShowOverloadInventoryInfoTicks", "interface.ShowOverloadInventoryInfoDelayTicks", "WorldMap.Step",
        "worldmap.CameraColor", "worldmap.CameraBkgColor", "worldmap.UpdateRect",
        "interface.AttackTurnToCamera", "interface.AttackMagicAngleToObject", "interface.AttackShootAngleToObject",
        "interface.ApplyResolutionRevertTimeS", "interface.inventory.WheelScrollDir", "interface.inventory.DragScrollMul",
        "interface.inventory.XPadScrollSpeedTicks", "interface.reputation.WheelScrollSpeed", "interface.reputation.ButtonsScrollSpeed",
        "interface.reputation.DragScrollMul", "interface.reputation.LeftDragScroll", "interface.ReverseMouse",
        "interface.hardwarecursor", "interface.UseWheel", "interface.DrawSafeFrame",
        "interface.EnableSafeFrame", "interface.SafeFramePercentX", "interface.SafeFramePercentY",
        "interface.SetSaveParticleMeshHeaders", "interface.SetFadeOutShowHlpTicks", "interface.EditMoveItems",
    ],
    "World & Walkability": [
        "world.RockAngleDiff", "world.SlopeAngleDiff", "world.WalkableWaterDeep",
        "world.RemoveClosedGoodSurfaceMaxCnt", "world.RemoveClosedGoodSurfaceBorderMaxCnt", "world.RemoveClosedBadSurfaceMaxCnt",
        "world.RemoveClosedBadSurfaceBorderMaxCnt", "world.RemoveClosedBadSurfaceMaxRockAngleDiff", "world.RemoveOutsideBadSurfaceMaxRockAngleDiff",
        "world.BurnGrassNum", "world.DefEndOfTheWorldSmallMarginA", "world.DefEndOfTheWorldWideMarginA",
        "world.DrawGPOverlay", "world.WalkableHeightUseRayJittering", "world.WalkableHeightUseRayJitteringInAllObjects",
    ],
    "Game - Ragdoll & Objects": [
        "game.CreateEditorObjects", "game.ragdoll.StartDelay", "game.ragdoll.MaxTicks",
        "game.ragdoll.MaxSimultaneousCount", "game.ragdoll.SeparateRandForce", "game.ragdoll.ForceRagDollCheckWalkableRange",
        "game.ragdoll.UnitRagDollMaxDistFromLocalHeroA", "game.ragdoll.StrikeHitForce", "game.ragdoll.ShootMissileForce",
        "game.ragdoll.ReloadForceFile", "game.ragdoll.TestDeath",
    ],
    "Network": [
        "network.MinUpdateHeroPosDist", "network.MinUpdateUpdateUserHeroDataTicks", "network.ShowENInvitation",
        "network.ENInvitationTicks", "tracenet1", "tracenet2",
        "tracenet3", "tracenet4", "tracenet5",
        "tracenet6", "tracenet7", "tracenet8",
        "tracenetpacket", "net.executeloadpackets", "tracenetcaptureinput",
        "tracenetRand1", "tracenetRand2", "tracenetRand3",
        "tracenetRand4", "tracenetRand5", "tracenetRand6",
        "tracenetRand7", "tracenetRand8", "tracenetRand9",
        "tracenetRand10", "tracenetRand11", "tracenetEx1",
        "tracenetEx2", "tracenetEx3", "tracenet1start",
        "tracenet2start", "tracenet3start", "tracenet4start",
        "tracenet5start", "tracenet6start", "tracenet7start",
        "tracenet8start", "tracenetrandstart", "net.dp8sim",
        "net.AllowStartOnePlayer", "net.crc", "net.crc1",
        "net.crc2", "net.crc3", "net.crc4",
        "net.tracetransfer", "net.tracenetstate", "net.SetTurnLength",
        "net.SetIOFrequency", "net.SetMaxClientsDiff", "net.SetBalanceTurnLength",
        "net.SetBalanceIOFreqMaxClientDiff", "net.SetDefTurnLength", "net.SetMinTurnLength",
        "net.SetMaxTurnLength", "net.SetMaxSetLowTurnLengthUp", "net.PrintBalance",
        "net.printcnt", "net.SetMinIOFrequency", "net.SetMinMaxClientDifference",
        "net.SetPacketsIOsMode", "net.SetCommandsCountInServerSendPacket", "net.SetCommandsCountInClientSendPacket",
        "net.SetCommandsCountInReplayPacket", "net.SetWaitingServerReplayCommandsCount", "net.SetSendCmdTimeoutServerMs",
        "net.SetSendCmdTimeoutClientMs", "net.SetSendReplyFastTimeoutMs", "net.SetSendReplySlowTimeoutMs",
        "net.SetSendRequestTimeoutMs", "net.SetUrgentThreadSleepMs", "net.SetUrgentThreadSleepAwaitingSendMs",
        "net.ImmediateServerForward", "net.SetMaxRequestInitialDelayMs", "net.SetRequestFirstRoundTripLatencyMul",
        "net.SetRequestSecondRoundTripLatencyMul", "net.SetRequestRestRoundTripLatencyMul", "net.SetMinFirstRequestDelayMs",
        "net.SetMinSecondRequestDelayMs", "net.SetMinRestRequestDelayMs", "net.SetClientSendQueueMsgNumDropLimit",
        "net.SetClientSendQueueMsgBytesDropLimit", "net.SetServerSendQueueMsgNumDropLimit", "net.SetServerSendQueueMsgBytesDropLimit",
        "net.SetCanAdjustServerGameSteps", "net.SetCanAdjustClientGameSteps", "net.SetAdjustServerGameStepsMinQueuedTurnsCnt",
        "net.SetAdjustClientGameStepsMinQueuedTurnsCnt", "net.SetDoubleSendServerCommands", "net.LimitClientCmdPosUpdCommands",
        "net.SendClientKeepAliveOnlyIfNothing", "net.ServerSendUpdatePosWithEoT", "net.ImmediateServerStepPacket",
        "net.LimitClientCmdMoveCommands", "net.LimitClientCmdAttackCommands", "net.ClientSendCommandsDelay",
    ],
    "EC - Scripting": [
        "ec.reloadscripts", "ec.debugcommand", "ec.dbg",
        "ec.trace", "ec.SetPartyEnemy", "ec.SetPartyNeutral",
        "ec.SetPartyNum", "ec.SetIsInParty", "ec.RemoveKilledUnits",
        "ec.AddInventory", "ec.SetGateOpen", "ec.PI.AddMapSign",
        "ec.PlayAnim", "ec.SetCustomIdleAnim", "ec.PlayPositionWave",
        "ec.IsObjectInInventory", "ec.RemoveObjectFromInventory", "ec.AddObjectToShop",
        "ec.RemoveAllObjectsFromShop", "ec.EnableShop", "ec.SetCustomObjectParticleNum",
        "ec.AddMagicCard", "ec.RemoveMagicCards", "ec.CountUnitsInArea",
        "ec.IsUnitInArea", "ec.SetRunMode", "ec.SetAutoRunMode",
        "ec.SetAlarmModeUnit", "ec.CreateObject", "ec.ReplaceObjectsInArea",
        "ec.LoadLevelConfiguration", "ec.SetWind", "ec.SetRain",
        "ec.SetSnow", "ec.LookAt", "ec.DelayedLookAt",
        "ec.ResurrectUnit", "ec.SetForcedSoundEAXEnvironment", "ec.AddQuest",
        "ec.SetQuestPosition", "ec.SetQuestState", "ec.RemoveQuest",
        "ec.AddCampaignLocation", "ec.RemoveCampaignLocation", "ec.SetCampaignLocationPosition",
        "ec.SetQuestsDirTitle", "ec.SetQuestMinVisibleZoomPercent", "ec.SetQuestMaxVisibleZoomPercent",
        "ec.SetCampaignLocationMinVisibleZoomPercent", "ec.SetCampaignLocationMaxVisibleZoomPercent", "ec.AddCampaignLocation2",
        "ec.SetSkyBoxColorFadeFromFog", "ec.GetCreateString", "ec.CommandMakeCustomWork",
        "ec.SetHeadCustomIdleAnim", "ec.SetHeadAngle", "ec.SetNPCNameNum",
        "ec.AddObjectToContainer", "ec.AddObjectsFromParamsToDeadBody", "ec.AddObjectToDeadBody",
        "ec.CreateSoundObject", "ec.AddObjectToUnitContainer", "ec.SetDayLength",
        "ec.PlayVideoCutscene", "ec.SetEndOfTheWorldMargin", "ec.SetEngineFarPlanePercent",
        "ec.SetUnitMapSignNum", "ec.AddMapSign", "ec.RemoveMapSign",
        "ec.RemoveMapSign2", "ec.SetGateLockForUnits", "ec.SetGateUnlockParamsForUnits",
        "ec.SetEndOfTheWorldSouthMargin", "ec.SetEndOfTheWorldNorthMargin", "ec.SetEndOfTheWorldEastMargin",
        "ec.SetEndOfTheWorldWestMargin", "ec.SetLimitedWorldStepRange", "ec.Trace2Screen",
        "ec.Trace2File", "ec.Trace2OutputDebug",
    ],
    "Cheats & Gameplay": [
        "PlayUnitAnim", "StartMagicSchool", "time",
        "SetStrength", "SetGold", "hitHP",
        "hitPoison", "hitMana", "InitMagic",
        "InitSkills", "startRoll", "move",
        "move2", "jump", "jump2",
        "clearSoundObjects", "TestCreate", "moveImm",
        "TestCmd", "jumpU", "jumpU2",
        "hitfall", "AddBasicPoint", "AddBasicSkill",
        "stopM", "SetHeadMesh", "SetNeckMesh",
        "TwoWorldsCheats", "ThisIsGreatGame", "quit",
        "Create", "AddExperiencePoints", "AddParamPoints",
        "AddSkillPoints", "kill", "ResetFog",
        "heal", "healH", "AddGold",
        "gamerate", "CreateEd", "killh",
        "BonusCode", "rescue",
    ],
    "Interface - XInput / Controller": [
        "interface.AttackTurnToCameraXInput", "interface.XInput.MoveSmallSensitivity", "interface.XInput.QuickStopHorseMinY",
        "interface.XCommandsDlg.HideDelay", "interface.XCommandsDlg.ShowDelay", "interface.XCommandsDlg.PressedStartDelay",
        "interface.XCommandsDlg.PressedStraightDelay", "interface.XCommandsDlg.PressedCrossDelay", "interface.XInputDeadZoneThumbLeft",
        "interface.XInputDeadZoneThumbRight", "interface.XInputDeadZoneTrigger", "interface.XInputPadKeyDigitalFirstRepeatTicks",
        "interface.XInputPadKeyDigitalNextRepeatTicks", "interface.XInputPadKeyAnalogFirstRepeatTicks", "interface.XInputPadKeyAnalogNextRepeatTicks",
        "interface.XInputPadKeyMinThumbStrength", "interface.XInputEnable", "interface.vibHurtTime",
        "interface.vibHurtFreq", "interface.vibHurtMotor", "interface.vibHitTime",
        "interface.vibHitFreq", "interface.vibHitMotor",
    ],
    "AnimMesh": [
        "animmesh.console", "animmesh.selected", "animmesh.dx",
        "animmesh.dy", "animmesh.dz", "animmesh.cz",
        "animmesh.alpha", "animmesh.beta", "animmesh.objalpha",
        "animmesh.objbeta", "animmesh.objphi", "animmesh.lightConsole",
        "animmesh.lightDiffuse", "animmesh.lightAmbient", "animmesh.lightAlpha",
        "animmesh.lightBeta", "animmesh.borderColor", "animmesh.blurPhases",
        "animmesh.sepiaColor", "animmesh.dx.D", "animmesh.dy.D",
        "animmesh.dz.D", "animmesh.cz.D", "animmesh.alpha.D",
        "animmesh.beta.D", "animmesh.objalpha.D", "animmesh.UseMeshTextureCache",
        "animmesh.MaxMeshTextureCacheSize", "animmesh.XInputThumbCameraMulX", "animmesh.XInputThumbCameraMulY",
        "animmesh.MeshHead2HipsDz",
    ],
    "Interface - Alchemy": [
        "interface.alchemy.UpdateAlchemyResultOnStep", "interface.alchemy.FormulasAreaMarginLeft", "interface.alchemy.FormulasAreaMarginTop",
        "interface.alchemy.FormulasAreaMarginRight", "interface.alchemy.FormulasAreaMarginBottom", "interface.alchemy.ResultInfoMargin",
        "interface.alchemy.IngredientsLabelMargin", "interface.alchemy.IngredientsMargin", "interface.alchemy.WheelScrollSpeed",
        "interface.alchemy.ButtonsScrollSpeed", "interface.alchemy.DragScrollMul", "interface.alchemy.LeftDragScroll",
        "interface.editalchemy.FormulasAreaMarginLeft", "interface.editalchemy.FormulasAreaMarginTop", "interface.editalchemy.FormulasAreaMarginRight",
        "interface.editalchemy.FormulasAreaMarginBottom", "interface.editalchemy.ResultInfoMargin", "interface.editalchemy.IngredientsLabelMargin",
        "interface.editalchemy.IngredientsMargin", "interface.editalchemy.WheelScrollSpeed", "interface.editalchemy.ButtonsScrollSpeed",
        "interface.editalchemy.DragScrollMul", "interface.editalchemy.LeftDragScroll", "interface.editalchemy.MaxFormulaNameLength",
    ],
    "Interface - Quests & Map": [
        "interface.questsmap.EmptyWorldColor", "interface.questsmap.FogColor", "interface.questsmap.FogColorUnderground",
        "interface.questsmap.MinZoom", "interface.questsmap.DefZoom", "interface.questsmap.XPadMidZoom",
        "interface.questsmap.WheelZoomDir", "interface.questsmap.MouseScrollDir", "interface.questsmap.DragScrollMulX",
        "interface.questsmap.DragScrollMulY", "interface.questsmap.LeftDragScroll", "interface.questsmap.ScrollToQuestMaxZoom",
        "interface.questsmap.XPadThumbScrollMapMul", "interface.questslog.LogAreaMargin.left", "interface.questslog.LogAreaMargin.top",
        "interface.questslog.LogAreaMargin.right", "interface.questslog.LogAreaMargin.bottom", "interface.questslog.QuestsDir2IconMargin",
        "interface.questslog.QuestIconMargin", "interface.questslog.Quest2IconMargin", "interface.questslog.DescriptionMargin",
        "interface.questslog.BarLineMargin", "interface.questslog.WheelScrollSpeed", "interface.questslog.ButtonsScrollSpeed",
        "interface.questslog.DragScrollMul", "interface.questslog.LeftDragScroll", "interface.questslog.XPadThumbScrollMul",
    ],
    "CDXSound - Audio Engine": [
        "CDXSound.ChannelRadius", "CDXSound.CurveDistanceScaler", "CDXSound.Wave3DUPDPeriod",
        "CDXSound.Engine3DUPDPeriod", "CDXSound.FreezeListener", "CDXSound.StartSoundDDist",
        "CDXSound.DEBUGSThread", "CDXSound.DEBUGPeriodic", "CDXSound.DEBUGDWPeriod",
        "CDXSound.ReloadEAX", "CDXSound.ForceEAXEnvironment", "CDXSound.LogToConsoleAMB",
        "CDXSound.LogToConsoleNRM", "CDXSound.QuietMusicInDialogPercent", "CDXSound.LogCoefs",
    ],
    "Sound - Voice Capture": [
        "sound.capture.enable", "sound.capture.TryCreateVCInput", "sound.capture.SampleRate",
        "sound.capture.BitsPerSample", "sound.capture.Channels", "sound.capture.Start",
        "sound.capture.Stop",
    ],
    "PhysX & Physics": [
        "physX.terrain.LoadFrag", "physX.terrain.FreeFrag", "physX.terrain.Clear",
        "physX.terrain.FreeAll", "physX.terrain.FreeRemotest", "physX.terrain.FreeUnderground",
        "physX.terrain.FreeGround", "physX.terrain.SetSlide", "physX.CollQuery.Interpolator",
        "physX.CollQuery.ZOffset", "physX.CollQuery.Sampling", "physX.CollQuery.Radius",
        "physX.Door.Open", "physX.Door.Close", "physX.Door.RemoveAll",
        "physX.BPlane.ZOffset", "Physic.DestroyWorld", "Physic.CreateWorld",
        "Physic.SetWorldStep", "Physic.SetWorldGravity", "Physic.WorldStart",
        "Physic.RagTrigger", "Physic.RagAnimPhase", "Physic.ClearRagForces",
        "Physic.AddRagForce", "Physic.AddRagForceDirect", "Physic.SetScallers",
        "Physic.RAGPX", "Physic.RAGPY", "Physic.RAGPZ",
    ],
    "Engine - Water": [
        "physX.water.slippery", "physX.water.density", "physX.water.depth",
        "physX.water.WindZOffset", "physX.water.WindDirMul", "Engine.WaterReflections",
        "Engine.RenderWBorder", "Engine.UseSplashes", "Engine.WRefFade",
        "Engine.TrueWaterRef", "Engine.WWScale", "Engine.WaterNFBorder",
        "Engine.DLandWaterRefFadeDst", "Engine.HiLoWtrBlend", "Engine.LoDistantWtrBlend",
        "Engine.SeaAmplitude", "Engine.SaveWaterBorder",
    ],
    "Engine - Performance & System": [
        "Engine.DrawSkybox", "Engine.DrawBB", "Engine.FOV",
        "Engine.FOVUPDATE", "Engine.LowqRender", "Engine.LightsPerEntity",
        "Engine.UseVIS", "Engine.TSN", "Engine.TSF",
        "Engine.TSA", "Engine.GenAmbientMap", "Engine.AMapBox",
        "Engine.ABoxScale", "Engine.VISH0", "Engine.VISH1",
        "Engine.UseInstancing", "Engine.ExtStat", "Engine.TCast",
        "Engine.ShowVisMinimap", "Engine.BBClippEpsi", "Engine.BBClippEpsiSm",
        "Engine.BBClippEpsiTR", "Engine.MTVIS", "Engine.ClothOverlay",
        "Engine.ShowGraphicsBBoxes", "Engine.DummyEngine", "Engine.WTLifetime",
        "Engine.WTTolerance", "Engine.UseDynamicLighting", "Engine.PhysicOverlay",
        "Engine.ParticlesDissort", "Engine.DphForDissort", "Engine.ShowTexStats",
        "Engine.TerraSCLLast", "Engine.DepthModeRenderer", "Engine.MTTextures",
        "Engine.TextureFirstLoadMIP", "Engine.TextureFirstLoadMIPBump", "Engine.TextureFirstLoadMIPTerra",
        "Engine.IgnoreDIP", "Engine.DFField", "Engine.FastTerraUpdates",
        "Engine.VISUseHBlock", "Engine.VISByAPC", "Engine.VISThreadDelay",
        "Engine.VISLockDelay", "Engine.SunFlareLens", "Engine.ParticlesSepAlpha",
        "Engine.ParticleSingleLayerNum", "Engine.StampRange", "Engine.StampRngFun",
        "Engine.StampDisplacement", "Engine.IgnoreDIPUP", "Engine.StampsPerGPGrid",
        "Engine.DLOCCNear", "Engine.DLOCCFar", "Engine.DLOCCDebugDraw",
        "Engine.SetTerrainTileScaleX", "Engine.SetTerrainTileScaleY", "Engine.DisableCloth",
        "Engine.ClearConsole", "Engine.LogIoToConsole", "Engine.DreamlandEntrance",
        "Engine.UseEZRenderer", "Engine.UseCDRenderer", "Engine.EZRendererThresh",
        "Engine.MinimapRTSize", "Engine.DumpTextures", "Engine.DumpMeshes",
        "Engine.PentaSegs", "Engine.PentaAngs", "Engine.SunMoonSize",
        "Engine.MaxAnisotrophy", "Engine.HpBlend", "Engine.PresentAtStart",
        "Engine.ReloadTextures", "Engine.EnableSetAntialiasingState", "Engine.SetGP2",
        "Engine.ReloadObjects", "Engine.ReloadAll", "Engine.DumpAMap",
        "Engine.CleanDeviceMemory", "Engine.VCStat", "Engine.ClearDeadMeshes",
        "Engine.LogWorkerThread",
    ],
    "Engine - Render Distance": [
        "Engine.FarPlane", "Engine.RefFar", "Engine.RefOffset",
        "Engine.AlphaFadeNear", "Engine.AlphaFadeFar", "Engine.WBOff",
        "Engine.NearPlane", "Engine.GFadeNear", "Engine.GFadeFar",
        "Engine.DSMargin", "Engine.VisHardMargin", "Engine.DrawDistantLand",
        "Engine.Draw3DObjects", "Engine.DLandFarClipp", "Engine.DLandFarClippOBJ",
        "Engine.DrawReflectedObjects", "Engine.WBDistance", "Engine.DLandAFade",
        "Engine.NearLeafsFade", "Engine.NearLeafsFadeBias", "Engine.DLandFogFarScale",
        "Engine.HOFarFade", "Engine.HONearFade", "Engine.HLFarFade",
        "Engine.WaterRefFarPlaneClipp",
    ],
    "Engine - LOD": [
        "Engine.LOD0", "Engine.LOD1", "Engine.LOD0SCR",
        "Engine.LOD1SCR", "Engine.LodBlend", "Engine.LODToBoxPercentage",
    ],
    "Engine - Grass & Trees": [
        "Engine.GrassDisp", "Engine.GrassX", "Engine.GrassY",
        "Engine.GrassFT", "Engine.GrassQ", "Engine.TreeLAlpha",
        "Engine.TreeLBeta", "Engine.NormalLeafsCount", "Engine.TreeWindFactor",
        "Engine.GrassRandomizer", "Engine.GrassDistFunction", "Engine.GrassNRMAngle",
        "Engine.HorTreeDivider", "Engine.HorTreeOffX", "Engine.HorTreeOffY",
        "Engine.HorizonTreesDiv",
    ],
    "Engine - HDR & Shaders": [
        "Engine.HDR", "Engine.NV_HDRExp", "Engine.NV_HDRGamma",
        "Engine.NV_HDRDefog", "Engine.NV_HDRCutoff", "Engine.NV_HDRGMul",
        "Engine.ATI_HDRExp", "Engine.ATI_HDRGamma", "Engine.ATI_HDRDefog",
        "Engine.ATI_HDRCutoff", "Engine.ATI_HDRGMul", "Engine.ShaderPP",
        "Engine.ShaderNoPreShader", "Engine.PreloadShaders", "Engine.AutoDOF",
        "Engine.AutoDOFTolerance", "Engine.UseNullShaders", "Engine.DistantShaders",
        "Engine.HDRSaturateHDR", "Engine.HDRSaturateLDR", "Engine.HDRBlueshift",
        "Engine.HDRDynamic", "Engine.DBG_HDRExp", "Engine.DBG_HDROff",
        "Engine.DBG_HDRGML", "Engine.ReloadShaders", "Engine.ShadersStat",
        "Engine.ShadersStatReset",
    ],
    "Engine - Shadows": [
        "Engine.Shadows", "Engine.SFarNeg", "Engine.SFarPos",
        "Engine.SFarRng", "Engine.ShX", "Engine.ShY",
        "Engine.ShmapSize", "Engine.ShadowLeafsCount", "Engine.ShadowLeafSize",
        "Engine.TShadows", "Engine.ShowShadowMap", "Engine.UseStencilShadows",
        "Engine.TShadowFocus", "Engine.TShadowDelta", "Engine.ShadowVIS",
        "Engine.ShadowClippVis", "Engine.OShadows", "Engine.StencilShadowsCastAll",
        "Engine.ShowStencilMap", "Engine.DLandTreeShadowSFct", "Engine.DLandTreeShadowCLLo",
        "Engine.DLandTreeShadowCLHi", "Engine.StcFarPln", "Engine.StcObjOff",
        "Engine.StcDbgDraw", "Engine.ShadowDBGNear", "Engine.ShadowDBGFar",
    ],
    "Engine - Physics Systems": [
        "Engine.PhysXAVRAGEIA", "Engine.HSystemActive", "Engine.HSystemStep",
        "Engine.HSystemGravity", "Engine.RagGravity", "Engine.RAGEnvSize",
        "Engine.DSystemActive", "Engine.DSystemStep", "Engine.DSystemGravity",
    ],
    "Engine - Distant Land & Horizon": [
        "Engine.DLandNthMip", "Engine.DLandTexMul", "Engine.DLandZOffT",
        "Engine.DLandZOffO", "Engine.DLandZOffW", "Engine.DLandMode",
        "Engine.DLandTexMultiplier", "Engine.HorizonTexMultiplier", "Engine.HorizonTexDarkener",
        "Engine.DLandNormalizationBias", "Engine.DLandUseOCC", "Engine.LazyOCCMode",
        "Engine.DLCustClipNrm", "Engine.DLandOffFadeAlpha", "Engine.AddHorizonWorld",
        "Engine.AddHorizonWorldEX", "Engine.ClearHorizon", "Engine.LoadHorizon",
        "Engine.SaveHorizon", "Engine.SetHorizonOffset", "Engine.HorizonA",
        "Engine.HorizonB", "Horizon.AddObject", "Horizon.ClearObjects",
        "Horizon.DeleteObject", "Horizon.AddPentagram", "Horizon.SetPentaStr",
        "Engine.SaveDLandTextures",
    ],
    "Engine - InHouse Lighting": [
        "Engine.InHouseAmbR", "Engine.InHouseAmbG", "Engine.InHouseAmbB",
        "Engine.InHouseDifR", "Engine.InHouseDifG", "Engine.InHouseDifB",
        "Engine.InHouseAngX", "Engine.InHouseAngY", "Engine.InHouseAngZ",
    ],
    "Particles": [
        "particles.draw", "particles.drawMesh", "particles.drawFace",
        "particles.drawMappedFace", "particles.drawTrail", "particles.drawLight",
        "particles.drawLaser", "particles.EnableDrawCount", "particles.ForceParticlesDrawSet",
        "particles.SetMaxParticlesOnScene", "particles.SetMaxParticlesOnSceneLow", "particles.SetMaxParticlesOnSceneMedium",
        "particles.SetMaxParticlesOnSceneHigh", "particles.globalAmbientMul", "particles.globalSunColorMul",
        "particles.MaxParticleLayer", "particles.MinFadeCameraShakeDist", "particles.MaxFadeCameraShakeDist",
        "particles.step",
    ],
}


def T(key):
    return LANG.get(App.current_lang, LANG["en"]).get(key, key)


def find_window_by_keyword(keyword):
    try:
        import pygetwindow as gw
        kw = keyword.lower()
        for w in gw.getAllWindows():
            if w.title and w.visible and kw in w.title.lower():
                return w
    except Exception:
        pass
    return None


def clipboard_paste(root, text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    time.sleep(0.01)
    pyautogui.hotkey("ctrl", "v")


# ============================================================
# COLORS (consistent dark theme)
# ============================================================
BG = "#1a1a2e"
BG2 = "#16213e"
BG3 = "#0f3460"
FG = "white"
ACCENT = "#e94560"
GREEN = "#4ecca3"
GRAY = "#aaa"
WARN = "#ffaa00"


# ============================================================
# FOCUS SELECTOR
# ============================================================
class FocusSelector(tk.Toplevel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.title(T("focus_select_title"))
        self.attributes("-topmost", True)
        self.configure(bg=BG)
        self.callback = callback
        self.resizable(False, False)
        self.grab_set()

        tk.Label(self, text=T("focus_select_info"), font=("Segoe UI", 10),
                bg=BG, fg=FG, wraplength=350).pack(padx=15, pady=(15, 5))

        lf = tk.Frame(self, bg=BG)
        lf.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        sb = tk.Scrollbar(lf)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.wl = tk.Listbox(lf, font=("Segoe UI", 9), bg=BG2, fg=FG,
                              selectbackground=ACCENT, height=10, width=50,
                              yscrollcommand=sb.set)
        self.wl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.config(command=self.wl.yview)
        self.wins = []
        self._refresh()

        bf = tk.Frame(self, bg=BG)
        bf.pack(fill=tk.X, padx=15, pady=10)
        tk.Button(bf, text=T("refresh"), font=("Segoe UI", 9), bg=BG3, fg=FG,
                 bd=0, padx=10, pady=5, cursor="hand2",
                 command=self._refresh).pack(side=tk.LEFT)
        tk.Button(bf, text=T("manual_3s"), font=("Segoe UI", 9), bg=BG3, fg=FG,
                 bd=0, padx=10, pady=5, cursor="hand2",
                 command=self._manual).pack(side=tk.LEFT, padx=5)
        tk.Button(bf, text=T("select"), font=("Segoe UI", 9), bg=ACCENT, fg=FG,
                 bd=0, padx=15, pady=5, cursor="hand2",
                 command=self._select).pack(side=tk.RIGHT)
        self.wl.bind("<Double-1>", lambda e: self._select())

    def _refresh(self):
        self.wl.delete(0, tk.END)
        self.wins = []
        try:
            import pygetwindow as gw
            for w in gw.getAllWindows():
                if w.title and w.title.strip() and w.visible:
                    self.wins.append(w.title)
                    self.wl.insert(tk.END, w.title)
        except Exception:
            pass

    def _manual(self):
        self.iconify()
        cw = tk.Toplevel(self.master)
        cw.attributes("-topmost", True)
        cw.overrideredirect(True)
        cw.configure(bg=ACCENT)
        sw, sh = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        cw.geometry(f"300x70+{sw//2-150}+{sh//2-35}")
        lbl = tk.Label(cw, font=("Segoe UI", 14, "bold"), bg=ACCENT, fg=FG)
        lbl.pack(expand=True)
        def cd(n):
            if n > 0:
                lbl.config(text=f"{T('click_target')}\n{n}...")
                cw.after(1000, cd, n - 1)
            else:
                cw.destroy()
                try:
                    import pygetwindow as gw
                    a = gw.getActiveWindow()
                    if a and a.title:
                        self.callback(a.title)
                except Exception:
                    pass
                self.destroy()
        cd(3)

    def _select(self):
        sel = self.wl.curselection()
        if sel:
            self.callback(self.wins[sel[0]])
            self.destroy()


# ============================================================
# EXPAND WINDOW (edit commands in a button)
# ============================================================
class ExpandWindow(tk.Toplevel):
    def __init__(self, parent, app, entry):
        super().__init__(parent)
        self.title(f"Edit: {entry['name']}")
        self.attributes("-topmost", True)
        self.configure(bg=BG)
        self.app = app
        self.entry = entry

        commands = app._get_commands(entry)
        defaults = entry.get("defaults", {})
        h = min(170 + len(commands) * 30, 600)
        self.geometry(f"550x{h}")

        # Header
        hf = tk.Frame(self, bg=BG)
        hf.pack(fill=tk.X, padx=10, pady=(10, 5))
        tk.Label(hf, text=entry["name"], font=("Segoe UI", 11, "bold"),
                bg=BG, fg=FG).pack(side=tk.LEFT)
        tk.Button(hf, text=T("read_defaults"), font=("Segoe UI", 8),
                 bg=BG3, fg=FG, bd=0, padx=8, pady=3, cursor="hand2",
                 command=self._read_defaults).pack(side=tk.RIGHT)
        tk.Button(hf, text="Run all", font=("Segoe UI", 8, "bold"),
                 bg=ACCENT, fg=FG, bd=0, padx=10, pady=3, cursor="hand2",
                 command=lambda: app.execute(entry)).pack(side=tk.RIGHT, padx=5)

        # Scrollable commands
        cf = tk.Frame(self, bg=BG)
        cf.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        canvas = tk.Canvas(cf, bg=BG, highlightthickness=0)
        sb = tk.Scrollbar(cf, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg=BG)
        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        cw_id = canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(cw_id, width=e.width))
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)

        self.cmd_rows = []
        for full_cmd in commands:
            parts = full_cmd.split(None, 1)
            cmd_name, cmd_val = parts[0], (parts[1] if len(parts) > 1 else "")
            dv = defaults.get(cmd_name, "")

            row = tk.Frame(inner, bg=BG2)
            row.pack(fill=tk.X, pady=1, padx=2)

            short = cmd_name.split(".")[-1] if "." in cmd_name else cmd_name
            tk.Label(row, text=short, font=("Consolas", 8), bg=BG2, fg=GRAY,
                    width=22, anchor="w").pack(side=tk.LEFT, padx=(4, 2))

            vv = tk.StringVar(value=cmd_val)
            tk.Entry(row, textvariable=vv, font=("Consolas", 9), bg=BG3, fg=FG,
                    insertbackground=FG, width=12, bd=0).pack(side=tk.LEFT, padx=2)

            if dv:
                tk.Button(row, text=f"D:{dv}", font=("Segoe UI", 7), bg=BG2, fg="#666",
                         bd=0, padx=3, cursor="hand2",
                         command=lambda v=vv, d=dv: v.set(d)).pack(side=tk.LEFT, padx=2)

            tk.Button(row, text="\u25B6", font=("Segoe UI", 7), bg=BG2, fg=GREEN,
                     bd=0, padx=4, cursor="hand2",
                     command=lambda cn=cmd_name, v=vv: self._run1(cn, v)
                     ).pack(side=tk.RIGHT, padx=2)

            self.cmd_rows.append((cmd_name, vv))

        # Bottom
        bf = tk.Frame(self, bg=BG)
        bf.pack(fill=tk.X, padx=10, pady=(5, 10))
        tk.Button(bf, text=T("save_close"), font=("Segoe UI", 9), bg=ACCENT, fg=FG,
                 bd=0, padx=12, pady=5, cursor="hand2",
                 command=self._save_close).pack(side=tk.RIGHT)

    def _run1(self, cn, vv):
        val = vv.get().strip()
        self.app.execute_single_command(f"{cn} {val}" if val else cn)

    def _save_close(self):
        new_cmds = []
        for cn, vv in self.cmd_rows:
            val = vv.get().strip()
            new_cmds.append(f"{cn} {val}" if val else cn)
        if self.entry["source"] == "inline":
            self.entry["commands"] = new_cmds
        elif self.entry["source"] == "file":
            fp = self.entry.get("filepath", "")
            if fp:
                try:
                    with open(fp, "w", encoding="utf-8") as f:
                        f.write("\n".join(new_cmds) + "\n")
                except Exception:
                    pass
        self.app.save_config()
        self.app.refresh_buttons()
        self.destroy()

    def _read_defaults(self):
        ReadDefaultsWindow(self, self.app, self.entry, self.cmd_rows)


# ============================================================
# READ DEFAULTS WINDOW
# ============================================================
class ReadDefaultsWindow(tk.Toplevel):
    def __init__(self, parent, app, entry, cmd_rows):
        super().__init__(parent)
        self.title(T("read_defaults"))
        self.attributes("-topmost", True)
        self.configure(bg=BG)
        self.geometry("500x450")
        self.app = app
        self.entry = entry
        self.cmd_rows = cmd_rows

        tk.Label(self, text="Step 1: Click 'Send' to query all commands without values",
                font=("Segoe UI", 9), bg=BG, fg=FG, wraplength=470,
                justify="left").pack(padx=15, pady=(10, 5), anchor="w")

        cmd_names = [cr[0] for cr in cmd_rows]
        tk.Button(self, text="Send to console", font=("Segoe UI", 9, "bold"),
                 bg=ACCENT, fg=FG, bd=0, padx=12, pady=5, cursor="hand2",
                 command=lambda: self._send(cmd_names)).pack(padx=15, pady=5)

        tk.Label(self, text="Step 2: Copy console output, paste here:",
                font=("Segoe UI", 9), bg=BG, fg=FG, wraplength=470,
                justify="left").pack(padx=15, pady=(10, 3), anchor="w")

        self.text = tk.Text(self, font=("Consolas", 9), bg=BG2, fg=FG,
                           insertbackground=FG, height=12)
        self.text.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        tk.Button(self, text="Parse && Apply", font=("Segoe UI", 10, "bold"),
                 bg=ACCENT, fg=FG, bd=0, padx=15, pady=6, cursor="hand2",
                 command=self._parse).pack(pady=10)

    def _send(self, cmd_names):
        threading.Thread(target=self.__send, args=(cmd_names,), daemon=True).start()

    def __send(self, cmd_names):
        try:
            ew = find_window_by_keyword(self.app.auto_keyword.get())
            if ew:
                ew.activate()
                time.sleep(0.3)
            pyautogui.press(self.app.console_key.get())
            time.sleep(0.5)
            cw = find_window_by_keyword(self.app.console_keyword.get())
            if cw:
                cw.activate()
                time.sleep(0.2)
            for cmd in cmd_names:
                clipboard_paste(self.app.root, cmd)
                time.sleep(0.02)
                pyautogui.press("enter")
                time.sleep(0.03)
        except Exception as e:
            self.app.status_var.set(f"{T('error')} {e}")

    def _parse(self):
        raw = self.text.get("1.0", tk.END)
        defaults = self.entry.get("defaults", {})
        count = 0
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue
            m = re.match(r'^([A-Za-z_][A-Za-z0-9_.]*)\s*[=:]\s*(.+)$', line)
            if not m:
                m = re.match(r'^([A-Za-z_][A-Za-z0-9_.]*)\s+(-?[\d.]+)$', line)
            if m:
                defaults[m.group(1).strip()] = m.group(2).strip()
                count += 1
        self.entry["defaults"] = defaults
        self.app.save_config()
        messagebox.showinfo("", f"Parsed {count} defaults!", parent=self)
        self.destroy()
        self.master.destroy()
        ExpandWindow(self.app.root, self.app, self.entry)


# ============================================================
# MAP TO MOD CONVERTER
# ============================================================
class MapConverterWindow(tk.Toplevel):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.title(T("mc_title"))
        self.attributes("-topmost", True)
        self.configure(bg=BG)
        self.geometry("580x620")
        self.app = app

        tk.Label(self, text=T("mc_title"), font=("Segoe UI", 13, "bold"),
                bg=BG, fg=FG).pack(pady=(10, 2))
        tk.Label(self, text=T("mc_info"), font=("Segoe UI", 9),
                bg=BG, fg=GRAY, justify="center").pack(pady=(0, 10))

        # Paths
        pf = tk.Frame(self, bg=BG)
        pf.pack(fill=tk.X, padx=15)

        self.paths = {}
        path_defs = [
            ("sdk_path",   T("mc_sdk_path"),   app.mc_sdk_path.get()),
            ("game_path",  T("mc_game_path"),  app.mc_game_path.get()),
            ("saves_path", T("mc_saves_path"), app.mc_saves_path.get()),
            ("wd_file",    T("mc_wd_file"),    app.mc_wd_file.get()),
            ("repacker",   T("mc_repacker"),   app.mc_repacker.get()),
        ]

        for key, label, default in path_defs:
            row = tk.Frame(pf, bg=BG)
            row.pack(fill=tk.X, pady=2)
            tk.Label(row, text=label, font=("Segoe UI", 8), bg=BG, fg=FG,
                    width=22, anchor="w").pack(side=tk.LEFT)
            sv = tk.StringVar(value=default)
            tk.Entry(row, textvariable=sv, font=("Segoe UI", 8), bg=BG2, fg=FG,
                    insertbackground=FG).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
            is_file = key in ("wd_file", "repacker")
            tk.Button(row, text="...", font=("Segoe UI", 8), bg=BG3, fg=FG,
                     bd=0, padx=6, cursor="hand2",
                     command=lambda s=sv, f=is_file: self._browse(s, f)
                     ).pack(side=tk.RIGHT)
            self.paths[key] = sv

        tk.Frame(self, height=1, bg="#333").pack(fill=tk.X, padx=15, pady=8)

        # Steps display
        self.steps_frame = tk.Frame(self, bg=BG)
        self.steps_frame.pack(fill=tk.X, padx=15)

        step_texts = [
            f"1. {T('mc_cook')} (editor.cookphysx commands)",
            f"2. {T('mc_gen_headers')} (LevelHeadersCacheGen.bat)",
            f"3. {T('mc_copy_files')} (.bmp + .phx -> Mods/Levels)",
            f"4. {T('mc_copy_lhc')} (Map_LevelHeaders.lhc)",
            f"5. {T('mc_repack')} (Tw1WDRepacker.exe)",
        ]

        self.step_labels = []
        for txt in step_texts:
            lbl = tk.Label(self.steps_frame, text=f"  \u2022 {txt}",
                          font=("Segoe UI", 9), bg=BG, fg=GRAY, anchor="w")
            lbl.pack(fill=tk.X, pady=1)
            self.step_labels.append(lbl)

        tk.Frame(self, height=1, bg="#333").pack(fill=tk.X, padx=15, pady=8)

        # Log
        self.log = tk.Text(self, font=("Consolas", 8), bg=BG2, fg=FG,
                          height=8, state=tk.DISABLED)
        self.log.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        # Buttons
        bf = tk.Frame(self, bg=BG)
        bf.pack(fill=tk.X, padx=15, pady=10)
        self.start_btn = tk.Button(bf, text=T("mc_start"), font=("Segoe UI", 10, "bold"),
                                   bg=ACCENT, fg=FG, bd=0, padx=20, pady=8,
                                   cursor="hand2", command=self._start)
        self.start_btn.pack(side=tk.RIGHT)
        tk.Button(bf, text=T("save_close"), font=("Segoe UI", 9),
                 bg=BG3, fg=FG, bd=0, padx=12, pady=6, cursor="hand2",
                 command=self._save_close).pack(side=tk.LEFT)

    def _browse(self, sv, is_file):
        if is_file:
            p = filedialog.askopenfilename(parent=self)
        else:
            p = filedialog.askdirectory(parent=self)
        if p:
            sv.set(p)

    def _log(self, text):
        self.log.config(state=tk.NORMAL)
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)
        self.log.config(state=tk.DISABLED)
        self.update()

    def _set_step(self, idx, status="running"):
        colors = {"running": WARN, "done": GREEN, "error": ACCENT, "pending": GRAY}
        icons = {"running": "\u25B6", "done": "\u2714", "error": "\u2718", "pending": "\u2022"}
        lbl = self.step_labels[idx]
        txt = lbl.cget("text")
        txt = re.sub(r'^  .', f'  {icons[status]}', txt)
        lbl.config(text=txt, fg=colors[status])

    def _save_close(self):
        self.app.mc_sdk_path.set(self.paths["sdk_path"].get())
        self.app.mc_game_path.set(self.paths["game_path"].get())
        self.app.mc_saves_path.set(self.paths["saves_path"].get())
        self.app.mc_wd_file.set(self.paths["wd_file"].get())
        self.app.mc_repacker.set(self.paths["repacker"].get())
        self.app.save_config()
        self.destroy()

    def _start(self):
        # Save paths first
        self._save_close.__wrapped__ = True  # just save, don't close
        self.app.mc_sdk_path.set(self.paths["sdk_path"].get())
        self.app.mc_game_path.set(self.paths["game_path"].get())
        self.app.mc_saves_path.set(self.paths["saves_path"].get())
        self.app.mc_wd_file.set(self.paths["wd_file"].get())
        self.app.mc_repacker.set(self.paths["repacker"].get())
        self.app.save_config()

        # Validate
        sdk = self.paths["sdk_path"].get()
        game = self.paths["game_path"].get()
        saves = self.paths["saves_path"].get()

        if not sdk or not os.path.isdir(sdk):
            self._log(T("mc_no_sdk"))
            return
        if not game or not os.path.isdir(game):
            self._log(T("mc_no_game"))
            return
        if not saves or not os.path.isdir(saves):
            self._log(T("mc_no_saves"))
            return

        self.start_btn.config(state=tk.DISABLED, text=T("mc_running"))
        threading.Thread(target=self._run_conversion, daemon=True).start()

    def _run_conversion(self):
        try:
            sdk = self.paths["sdk_path"].get()
            game = self.paths["game_path"].get()
            saves = self.paths["saves_path"].get()
            wd_file = self.paths["wd_file"].get()
            repacker = self.paths["repacker"].get()

            mods_dir = os.path.join(game, "Mods")
            mods_levels = os.path.join(mods_dir, "Levels")
            mods_physic = os.path.join(mods_levels, "Physic")
            os.makedirs(mods_levels, exist_ok=True)
            os.makedirs(mods_physic, exist_ok=True)

            # ---- STEP 1: Cook PhysX via editor console ----
            self._set_step(0, "running")
            self._log(T("mc_cook_info"))

            cook_cmds = [
                "editor.cookphysx.mode geomipmap",
                "editor.cookphysx.strength = 1.0",
                "editor.cookphysx.overwrite = 1",
                "editor.cookphysx.pc out",
            ]

            try:
                ew = find_window_by_keyword(self.app.auto_keyword.get())
                if ew:
                    ew.activate()
                    time.sleep(0.3)
                    pyautogui.press(self.app.console_key.get())
                    time.sleep(0.5)
                    cw = find_window_by_keyword(self.app.console_keyword.get())
                    if cw:
                        cw.activate()
                        time.sleep(0.2)
                    for cmd in cook_cmds:
                        clipboard_paste(self.app.root, cmd)
                        time.sleep(0.05)
                        pyautogui.press("enter")
                        time.sleep(0.1)
                        self._log(f"  > {cmd}")
                    # Wait for PhysX cooking to complete
                    self._log("  Waiting for PhysX cooking (10s)...")
                    time.sleep(10)
                    self._set_step(0, "done")
                else:
                    self._log("  Editor not running - skipping PhysX cook")
                    self._log("  (Run these manually if needed)")
                    self._set_step(0, "error")
            except Exception as e:
                self._log(f"  PhysX cook error: {e}")
                self._set_step(0, "error")

            # ---- STEP 2: Run LevelHeadersCacheGen ----
            self._set_step(1, "running")
            self._log(T("mc_bat_info"))

            bat_path = os.path.join(sdk, "Tools", "LevelHeadersCacheGen.bat")
            meshgen = os.path.join(sdk, "Tools", "MeshParamsGen.exe")

            if os.path.exists(bat_path):
                try:
                    result = subprocess.run(
                        [bat_path], cwd=os.path.join(sdk, "Tools"),
                        capture_output=True, text=True, timeout=60,
                        creationflags=subprocess.CREATE_NO_WINDOW
                    )
                    self._log(f"  Bat exit code: {result.returncode}")
                    if result.stdout:
                        for line in result.stdout.strip().splitlines()[:5]:
                            self._log(f"  {line}")
                    self._set_step(1, "done")
                except subprocess.TimeoutExpired:
                    self._log("  Bat timed out (60s) - may still be running")
                    self._set_step(1, "error")
                except Exception as e:
                    self._log(f"  Bat error: {e}")
                    self._set_step(1, "error")
            elif os.path.exists(meshgen):
                # Run meshgen directly
                tw_dir = os.path.dirname(sdk.rstrip("/\\"))
                cmd_line = f'"{meshgen}" "{tw_dir}/>" -levelheaderscache "Levels\\Map_*.lnd" "Levels\\Map_LevelHeaders.lhc"'
                self._log(f"  Running: {cmd_line}")
                try:
                    result = subprocess.run(
                        cmd_line, shell=True, cwd=os.path.join(sdk, "Tools"),
                        capture_output=True, text=True, timeout=60,
                        creationflags=subprocess.CREATE_NO_WINDOW
                    )
                    self._set_step(1, "done")
                except Exception as e:
                    self._log(f"  MeshParamsGen error: {e}")
                    self._set_step(1, "error")
            else:
                self._log(f"  LevelHeadersCacheGen.bat not found in {sdk}/Tools/")
                self._set_step(1, "error")

            # ---- STEP 3: Copy map files ----
            self._set_step(2, "running")
            self._log(T("mc_copy_info"))

            bmp_files = glob.glob(os.path.join(saves, "Map_*.bmp"))
            phx_files = glob.glob(os.path.join(saves, "Map_*.phx"))
            # Also check Physic subfolder
            phx_sub = os.path.join(saves, "Physic")
            if os.path.isdir(phx_sub):
                phx_files += glob.glob(os.path.join(phx_sub, "Map_*.phx"))

            copied = 0
            for f in bmp_files:
                dst = os.path.join(mods_levels, os.path.basename(f))
                shutil.copy2(f, dst)
                self._log(f"  {os.path.basename(f)} -> Mods/Levels/")
                copied += 1

            for f in phx_files:
                dst = os.path.join(mods_physic, os.path.basename(f))
                shutil.copy2(f, dst)
                self._log(f"  {os.path.basename(f)} -> Mods/Levels/Physic/")
                copied += 1

            if copied > 0:
                self._log(f"  Copied {copied} files")
                self._set_step(2, "done")
            else:
                self._log(f"  No map files found in {saves}")
                self._set_step(2, "error")

            # ---- STEP 4: Copy LevelHeaders.lhc ----
            self._set_step(3, "running")
            lhc_src = os.path.join(sdk, "Levels", "Map_LevelHeaders.lhc")
            # Also check TwoWorlds/Levels
            if not os.path.exists(lhc_src):
                tw_levels = os.path.join(os.path.dirname(sdk.rstrip("/\\")), "Levels")
                lhc_src = os.path.join(tw_levels, "Map_LevelHeaders.lhc")

            if os.path.exists(lhc_src):
                shutil.copy2(lhc_src, os.path.join(mods_levels, "Map_LevelHeaders.lhc"))
                self._log(f"  Map_LevelHeaders.lhc -> Mods/Levels/")
                self._set_step(3, "done")
            else:
                self._log(f"  Map_LevelHeaders.lhc not found!")
                self._log(f"  Searched: {lhc_src}")
                self._set_step(3, "error")

            # Copy .wd file if specified
            if wd_file and os.path.exists(wd_file):
                shutil.copy2(wd_file, os.path.join(mods_dir, os.path.basename(wd_file)))
                self._log(f"  {os.path.basename(wd_file)} -> Mods/")

            # ---- STEP 5: Run repacker ----
            self._set_step(4, "running")
            if repacker and os.path.exists(repacker):
                self._log(T("mc_repack_info"))
                try:
                    # Copy repacker to mods dir if not already there
                    repacker_dst = os.path.join(mods_dir, os.path.basename(repacker))
                    if not os.path.exists(repacker_dst):
                        shutil.copy2(repacker, repacker_dst)

                    subprocess.Popen(
                        [repacker_dst],
                        cwd=mods_dir,
                        creationflags=subprocess.CREATE_NEW_CONSOLE
                    )
                    self._log(f"  Repacker opened - set Source & Dest to:\n  {mods_dir}")
                    self._set_step(4, "done")
                except Exception as e:
                    self._log(f"  Repacker error: {e}")
                    self._set_step(4, "error")
            else:
                self._log("  Repacker not set or not found - skipped")
                self._set_step(4, "error")

            self._log("")
            self._log(T("mc_done"))
            self._log(f"Don't forget to enable the mod in TwoWorlds1 Mod Selector!")

        except Exception as e:
            self._log(f"FATAL: {e}")
        finally:
            self.start_btn.config(state=tk.NORMAL, text=T("mc_start"))


# ============================================================
# COMMAND LIST WINDOW
# ============================================================
class CommandListWindow(tk.Toplevel):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.title(T("cmd_list_title"))
        self.attributes("-topmost", True)
        self.configure(bg=BG)
        self.geometry("520x600")
        self.app = app
        self.marked = set()

        sf = tk.Frame(self, bg=BG)
        sf.pack(fill=tk.X, padx=10, pady=(10, 5))
        tk.Label(sf, text=T("search"), font=("Segoe UI", 10),
                bg=BG, fg=FG).pack(side=tk.LEFT)
        self.sv = tk.StringVar()
        self.sv.trace("w", lambda *a: self._filter())
        se = tk.Entry(sf, textvariable=self.sv, font=("Segoe UI", 10),
                     bg=BG2, fg=FG, insertbackground=FG)
        se.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        se.focus_set()

        inf = tk.Frame(self, bg=BG)
        inf.pack(fill=tk.X, padx=15)
        self.cnt = tk.StringVar()
        tk.Label(inf, textvariable=self.cnt, font=("Segoe UI", 8), bg=BG, fg=GRAY).pack(side=tk.LEFT)
        self.mcnt = tk.StringVar()
        tk.Label(inf, textvariable=self.mcnt, font=("Segoe UI", 8, "bold"),
                bg=BG, fg=ACCENT).pack(side=tk.RIGHT)

        tf = tk.Frame(self, bg=BG)
        tf.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=BG2, foreground=FG,
                        fieldbackground=BG2, font=("Consolas", 9))
        style.map("Treeview", background=[("selected", ACCENT)])
        sb = tk.Scrollbar(tf)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree = ttk.Treeview(tf, show="tree", yscrollcommand=sb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.config(command=self.tree.yview)
        self.tree.column("#0", width=500)
        self.tree.bind("<Double-1>", lambda e: self._copy())
        self.tree.bind("<Button-3>", self._ctx)

        bb = tk.Frame(self, bg=BG)
        bb.pack(fill=tk.X, padx=10, pady=(0, 8))
        tk.Label(bb, text=T("dblclick_copy"), font=("Segoe UI", 8), bg=BG, fg="#666").pack(side=tk.LEFT)
        tk.Button(bb, text=T("clear_marks"), font=("Segoe UI", 8), bg=BG3, fg=FG,
                 bd=0, padx=8, pady=2, cursor="hand2", command=self._clear).pack(side=tk.RIGHT)
        self._populate()

    def _get_cmd(self, iid):
        return self.tree.item(iid)["text"].replace(" [*]", "").strip()

    def _populate(self, flt=""):
        self.tree.delete(*self.tree.get_children())
        fl = flt.lower()
        mc = 0
        for cat, cmds in COMMAND_CATEGORIES.items():
            fil = [c for c in cmds if fl in c.lower()] if flt else cmds
            if not fil:
                continue
            cid = self.tree.insert("", tk.END, text=f"[{cat}] ({len(fil)})", open=bool(flt))
            for c in fil:
                m = " [*]" if c in self.marked else ""
                self.tree.insert(cid, tk.END, text=f"  {c}{m}")
                mc += 1
        total = sum(len(v) for v in COMMAND_CATEGORIES.values())
        self.cnt.set(f"{mc} {T('matches')}" if flt else
                    f"{total} {T('commands_in')} {len(COMMAND_CATEGORIES)} {T('categories')}")
        self.mcnt.set(f"{len(self.marked)} {T('marked_count')}" if self.marked else "")

    def _filter(self):
        self._populate(self.sv.get())

    def _copy(self):
        sel = self.tree.selection()
        if not sel:
            return
        cmd = self._get_cmd(sel[0])
        if cmd.startswith("["):
            return
        self.clipboard_clear()
        self.clipboard_append(cmd)
        self.title(T("copy") + "!")
        self.after(1500, lambda: self.title(T("cmd_list_title")))

    def _ctx(self, event):
        row = self.tree.identify_row(event.y)
        if not row:
            return
        self.tree.selection_set(row)
        cmd = self._get_cmd(row)
        if cmd.startswith("["):
            return
        m = tk.Menu(self, tearoff=0, bg=BG2, fg=FG, activebackground=ACCENT, font=("Segoe UI", 9))
        m.add_command(label=T("copy"), command=self._copy)
        m.add_command(label=T("add_as_button"), command=lambda: self._add1(cmd))
        m.add_separator()
        if cmd in self.marked:
            m.add_command(label=T("unmark"), command=lambda: self._toggle(cmd))
        else:
            m.add_command(label=T("mark"), command=lambda: self._toggle(cmd))
        if self.marked:
            m.add_command(label=f"{T('marked_as_button')} ({len(self.marked)})",
                         command=self._add_marked)
        m.post(event.x_root, event.y_root)

    def _toggle(self, cmd):
        self.marked.symmetric_difference_update({cmd})
        self._populate(self.sv.get())

    def _clear(self):
        self.marked.clear()
        self._populate(self.sv.get())

    def _add1(self, cmd):
        d = tk.Toplevel(self)
        d.title(T("add_as_button"))
        d.attributes("-topmost", True)
        d.configure(bg=BG)
        d.grab_set()
        d.resizable(False, False)

        tk.Label(d, text=cmd, font=("Consolas", 10, "bold"), bg=BG, fg=FG).pack(padx=15, pady=(10, 5))
        tk.Label(d, text="Value:", font=("Segoe UI", 9), bg=BG, fg=FG).pack(anchor="w", padx=15)
        vv = tk.StringVar()
        ve = tk.Entry(d, textvariable=vv, font=("Consolas", 11), bg=BG2, fg=FG,
                     insertbackground=FG, width=25)
        ve.pack(padx=15, pady=3)
        ve.focus_set()

        tk.Label(d, text=T("enter_btn_name"), font=("Segoe UI", 9), bg=BG, fg=FG).pack(anchor="w", padx=15, pady=(5, 0))
        short = cmd.split(".")[-1] if "." in cmd else cmd
        nv = tk.StringVar(value=short)
        tk.Entry(d, textvariable=nv, font=("Segoe UI", 10), bg=BG2, fg=FG,
                insertbackground=FG, width=25).pack(padx=15, pady=3)

        def go():
            n = nv.get().strip()
            v = vv.get().strip()
            if n:
                self.app.add_inline_button(n, [f"{cmd} {v}" if v else cmd])
                d.destroy()
        ve.bind("<Return>", lambda e: go())
        tk.Button(d, text=T("add_as_button"), font=("Segoe UI", 10), bg=ACCENT, fg=FG,
                 bd=0, padx=15, pady=6, cursor="hand2", command=go).pack(pady=10)

    def _add_marked(self):
        if not self.marked:
            return
        cmds = sorted(self.marked)
        d = tk.Toplevel(self)
        d.title(T("marked_as_button"))
        d.attributes("-topmost", True)
        d.configure(bg=BG)
        d.grab_set()
        d.geometry("450x{}".format(min(180 + len(cmds) * 32, 600)))

        tk.Label(d, text=T("enter_btn_name"), font=("Segoe UI", 10), bg=BG, fg=FG).pack(anchor="w", padx=15, pady=(10, 2))
        nv = tk.StringVar(value=f"{len(cmds)} commands")
        tk.Entry(d, textvariable=nv, font=("Segoe UI", 10), bg=BG2, fg=FG,
                insertbackground=FG).pack(fill=tk.X, padx=15, pady=(0, 8))

        lf = tk.Frame(d, bg=BG)
        lf.pack(fill=tk.BOTH, expand=True, padx=15)
        canvas = tk.Canvas(lf, bg=BG, highlightthickness=0)
        sb = tk.Scrollbar(lf, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg=BG)
        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        if len(cmds) > 8:
            sb.pack(side=tk.RIGHT, fill=tk.Y)

        vvs = []
        for c in cmds:
            r = tk.Frame(inner, bg=BG)
            r.pack(fill=tk.X, pady=1)
            short = c.split(".")[-1] if "." in c else c
            tk.Label(r, text=short, font=("Consolas", 8), bg=BG, fg=GRAY,
                    width=25, anchor="w").pack(side=tk.LEFT)
            v = tk.StringVar()
            tk.Entry(r, textvariable=v, font=("Consolas", 9), bg=BG2, fg=FG,
                    insertbackground=FG, width=12).pack(side=tk.LEFT, padx=2)
            vvs.append((c, v))

        def go():
            n = nv.get().strip()
            if not n:
                return
            final = [f"{c} {v.get().strip()}" if v.get().strip() else c for c, v in vvs]
            self.app.add_inline_button(n, final)
            self.marked.clear()
            self._populate(self.sv.get())
            d.destroy()

        tk.Button(d, text=T("add_as_button"), font=("Segoe UI", 10), bg=ACCENT, fg=FG,
                 bd=0, padx=15, pady=6, cursor="hand2", command=go).pack(pady=10)


# ============================================================
# SETTINGS WINDOW
# ============================================================
class SettingsWindow(tk.Toplevel):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.title(T("settings_title"))
        self.attributes("-topmost", True)
        self.configure(bg=BG)
        self.resizable(False, False)
        self.app = app
        p = {"padx": 15, "pady": 3}

        tk.Label(self, text=T("focus_mode"), font=("Segoe UI", 10, "bold"),
                bg=BG, fg=FG).pack(anchor="w", **p)
        mf = tk.Frame(self, bg=BG)
        mf.pack(fill=tk.X, padx=15)
        self.mode_var = tk.StringVar(value=app.focus_mode.get())
        for txt, val in [(T("mode_auto"), "auto"), (T("mode_manual"), "manual")]:
            tk.Radiobutton(mf, text=txt, variable=self.mode_var, value=val,
                          font=("Segoe UI", 9), bg=BG, fg=FG, selectcolor=BG3,
                          activebackground=BG).pack(anchor="w")

        for label, var in [("Editor window:", app.auto_keyword),
                           ("Console window:", app.console_keyword)]:
            tk.Label(self, text=label, font=("Segoe UI", 9), bg=BG, fg=FG).pack(anchor="w", **p)
            tk.Entry(self, textvariable=var, font=("Segoe UI", 9), bg=BG2, fg=FG,
                    insertbackground=FG).pack(fill=tk.X, padx=15)

        tk.Frame(self, height=1, bg="#333").pack(fill=tk.X, padx=15, pady=5)

        tk.Label(self, text=T("editor_path"), font=("Segoe UI", 9), bg=BG, fg=FG).pack(anchor="w", **p)
        ef = tk.Frame(self, bg=BG)
        ef.pack(fill=tk.X, padx=15)
        tk.Entry(ef, textvariable=app.editor_path, font=("Segoe UI", 8), bg=BG2, fg=FG,
                insertbackground=FG).pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(ef, text="...", font=("Segoe UI", 8), bg=BG3, fg=FG, bd=0, padx=6,
                 cursor="hand2", command=lambda: self._browse(app.editor_path)).pack(side=tk.RIGHT)

        tk.Frame(self, height=1, bg="#333").pack(fill=tk.X, padx=15, pady=5)

        tk.Label(self, text=T("delay_label"), font=("Segoe UI", 9), bg=BG, fg=FG).pack(anchor="w", **p)
        tk.Scale(self, from_=10, to=300, orient=tk.HORIZONTAL, variable=app.delay_ms,
                bg=BG2, fg=FG, troughcolor=BG3, highlightthickness=0,
                font=("Segoe UI", 8), length=250).pack(padx=15)

        tk.Label(self, text=T("console_key_label"), font=("Segoe UI", 9), bg=BG, fg=FG).pack(anchor="w", **p)
        ckf = tk.Frame(self, bg=BG)
        ckf.pack(fill=tk.X, padx=15)
        tk.Entry(ckf, textvariable=app.console_key, width=5, font=("Segoe UI", 11), bg=BG2, fg=FG,
                insertbackground=FG, justify="center").pack(side=tk.LEFT)

        tk.Checkbutton(self, text=T("close_console_after"), variable=app.close_console,
                       font=("Segoe UI", 9), bg=BG, fg=FG, selectcolor=BG3,
                       activebackground=BG).pack(anchor="w", padx=15, pady=2)
        tk.Checkbutton(self, text=T("always_on_top"), variable=app.always_on_top,
                       font=("Segoe UI", 9), bg=BG, fg=FG, selectcolor=BG3,
                       activebackground=BG,
                       command=lambda: parent.attributes("-topmost", app.always_on_top.get())
                       ).pack(anchor="w", padx=15, pady=2)

        lf = tk.Frame(self, bg=BG)
        lf.pack(fill=tk.X, padx=15, pady=5)
        tk.Label(lf, text=T("language"), font=("Segoe UI", 9), bg=BG, fg=FG).pack(side=tk.LEFT)
        self.lc = ttk.Combobox(lf, values=["English", "Deutsch"], state="readonly",
                                width=12, font=("Segoe UI", 9))
        self.lc.set("English" if app.lang.get() == "en" else "Deutsch")
        self.lc.pack(side=tk.LEFT, padx=10)

        tk.Button(self, text=T("save_close"), font=("Segoe UI", 10), bg=ACCENT, fg=FG,
                 bd=0, padx=15, pady=7, cursor="hand2", command=self._save).pack(pady=10)

    def _browse(self, var):
        p = filedialog.askopenfilename(filetypes=[("Executable", "*.exe"), ("All", "*.*")])
        if p:
            var.set(p)

    def _save(self):
        nl = "en" if self.lc.get() == "English" else "de"
        ol = self.app.lang.get()
        self.app.lang.set(nl)
        App.current_lang = nl
        self.app.focus_mode.set(self.mode_var.get())
        self.app.save_config()
        self.app.update_focus_label()
        if nl != ol:
            messagebox.showinfo("", "Restart to apply language change.", parent=self)
        self.destroy()


# ============================================================
# MAIN APP
# ============================================================
class App:
    current_lang = "en"

    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg=BG)
        self.root.attributes("-topmost", True)

        # Settings vars
        self.delay_ms = tk.IntVar(value=30)
        self.console_key = tk.StringVar(value="c")
        self.close_console = tk.BooleanVar(value=True)
        self.always_on_top = tk.BooleanVar(value=True)
        self.target_window = tk.StringVar(value="")
        self.lang = tk.StringVar(value="en")
        self.focus_mode = tk.StringVar(value="auto")
        self.auto_keyword = tk.StringVar(value="TwoWorlds Editor")
        self.console_keyword = tk.StringVar(value="Console")
        self.editor_path = tk.StringVar(value="")
        self.last_map = tk.StringVar(value="")
        # Map converter paths
        self.mc_sdk_path = tk.StringVar(value="")
        self.mc_game_path = tk.StringVar(value="")
        self.mc_saves_path = tk.StringVar(value="")
        self.mc_wd_file = tk.StringVar(value="")
        self.mc_repacker = tk.StringVar(value="")

        self.running = False
        self.stop_requested = False
        self.button_entries = []
        self.button_widgets = []

        # Check first start BEFORE load_config
        first_start = not os.path.exists(CONFIG_FILE)
        self.load_config()

        # Show wizard on first start
        if first_start:
            self._run_setup_wizard()

        App.current_lang = self.lang.get()
        self.root.title(T("title"))

        self._build_menu()
        self._build_ui()

        for entry in list(self.button_entries):
            if entry["source"] == "file":
                if os.path.exists(entry.get("filepath", "")):
                    self._create_btn(entry)
                else:
                    self.button_entries.remove(entry)
            else:
                self._create_btn(entry)

        self._resize()
        self.root.after(300, self._startup)

    # ---- STARTUP ----

    def _startup(self):
        if self.focus_mode.get() == "auto":
            w = find_window_by_keyword(self.auto_keyword.get())
            if w:
                self.target_window.set(w.title)
                self._parse_map(w.title)
                self.update_focus_label()
            else:
                self.status.set(T("auto_not_found"))
        elif not self.target_window.get():
            FocusSelector(self.root, self._set_target)

    # ---- SETUP WIZARD ----

    def _run_setup_wizard(self):
        wiz = tk.Toplevel(self.root)
        wiz.title("TW Editor CMD Injector - Setup")
        wiz.configure(bg=BG)
        wiz.resizable(False, False)
        wiz.attributes("-topmost", True)
        wiz.transient(self.root)
        W, H = 480, 360
        try:
            sx = wiz.winfo_screenwidth()
            sy = wiz.winfo_screenheight()
            wiz.geometry(f"{W}x{H}+{(sx-W)//2}+{(sy-H)//2}")
        except Exception:
            wiz.geometry(f"{W}x{H}")

        chosen_lang = tk.StringVar(value="en")
        chosen_path = tk.StringVar(value="")
        body = tk.Frame(wiz, bg=BG)
        body.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)

        def _t(key):
            return LANG.get(chosen_lang.get(), LANG["en"]).get(key, key)

        def clear():
            for c in body.winfo_children():
                c.destroy()

        def finish_wizard():
            self.lang.set(chosen_lang.get())
            App.current_lang = chosen_lang.get()
            p = chosen_path.get().strip()
            if p:
                self.editor_path.set(p)
            self.save_config()
            wiz.destroy()

        def page_lang():
            clear()
            tk.Label(body, text="Welcome! / Willkommen!",
                     font=("Segoe UI", 15, "bold"), bg=BG, fg=FG).pack(pady=(10, 20))
            tk.Label(body, text="Choose your language / Sprache waehlen:",
                     font=("Segoe UI", 11), bg=BG, fg=FG).pack(pady=(0, 15))
            bf = tk.Frame(body, bg=BG)
            bf.pack(pady=10)
            kw = dict(font=("Segoe UI", 12), width=16, height=2, cursor="hand2",
                      relief=tk.GROOVE, bd=2)
            def pick(lang):
                chosen_lang.set(lang)
                page_info()
            tk.Button(bf, text="EN  English", bg="#2a4a7f", fg="white",
                      activebackground="#3a5a9f", activeforeground="white",
                      command=lambda: pick("en"), **kw).pack(side=tk.LEFT, padx=8)
            tk.Button(bf, text="DE  Deutsch", bg="#444444", fg="white",
                      activebackground="#555555", activeforeground="white",
                      command=lambda: pick("de"), **kw).pack(side=tk.LEFT, padx=8)
            tk.Label(body, text="v5.1  -  1272 Commands  -  44 Categories",
                     font=("Segoe UI", 9), bg=BG, fg="#888888").pack(side=tk.BOTTOM, pady=(15, 0))

        def page_info():
            clear()
            tk.Label(body, text=_t("wiz_info_header"),
                     font=("Segoe UI", 13, "bold"), bg=BG, fg=FG).pack(pady=(5, 8))
            nav = tk.Frame(body, bg=BG)
            nav.pack(fill=tk.X, side=tk.BOTTOM)
            tk.Button(nav, text=_t("wiz_back"), command=page_lang,
                      bg=BG3, fg=FG, font=("Segoe UI", 10), width=10).pack(side=tk.LEFT)
            tk.Button(nav, text=_t("wiz_next"), command=page_path,
                      bg=ACCENT, fg="white", font=("Segoe UI", 10, "bold"),
                      width=10).pack(side=tk.RIGHT)
            tf = tk.Frame(body, bg="#1e1e1e", bd=1, relief=tk.SUNKEN)
            tf.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
            tx = tk.Text(tf, wrap=tk.WORD, bg="#1e1e1e", fg=FG,
                         font=("Segoe UI", 10), relief=tk.FLAT,
                         padx=10, pady=8, highlightthickness=0)
            tx.insert("1.0", _t("wiz_info_text"))
            tx.configure(state=tk.DISABLED)
            tx.pack(fill=tk.BOTH, expand=True)

        def page_path():
            clear()
            tk.Label(body, text=_t("wiz_path_header"),
                     font=("Segoe UI", 13, "bold"), bg=BG, fg=FG).pack(pady=(5, 8))
            nav = tk.Frame(body, bg=BG)
            nav.pack(fill=tk.X, side=tk.BOTTOM, pady=(20, 0))
            tk.Button(nav, text=_t("wiz_back"), command=page_info,
                      bg=BG3, fg=FG, font=("Segoe UI", 10), width=10).pack(side=tk.LEFT)
            tk.Button(nav, text=_t("wiz_finish"), command=finish_wizard,
                      bg=ACCENT, fg="white", font=("Segoe UI", 11, "bold"),
                      width=10).pack(side=tk.RIGHT)
            tk.Label(body, text=_t("wiz_path_info"), font=("Segoe UI", 10),
                     bg=BG, fg="#cccccc", justify=tk.LEFT, wraplength=420).pack(pady=(0, 15))
            pf = tk.Frame(body, bg=BG)
            pf.pack(fill=tk.X, pady=5)
            pe = tk.Entry(pf, textvariable=chosen_path, font=("Consolas", 10),
                          bg="#1e1e1e", fg=FG, insertbackground=FG)
            pe.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
            def browse():
                fp = filedialog.askopenfilename(
                    parent=wiz, title="TwoWorldsEditor.exe",
                    filetypes=[("Executable", "*.exe"), ("All", "*.*")])
                if fp:
                    chosen_path.set(fp)
            tk.Button(pf, text=_t("wiz_browse"), command=browse,
                      bg=BG3, fg=FG, font=("Segoe UI", 9)).pack(side=tk.RIGHT)

        wiz.protocol("WM_DELETE_WINDOW", finish_wizard)
        page_lang()
        wiz.wait_window(wiz)

    def _parse_map(self, title):
        if " - " in title:
            m = title.split(" - ")[-1].strip()
            if m:
                self.last_map.set(m)
                self.save_config()

    # ---- MENU ----

    def _build_menu(self):
        mb = tk.Menu(self.root, bg=BG3, fg=FG, activebackground=ACCENT, font=("Segoe UI", 9))

        fm = tk.Menu(mb, tearoff=0, bg=BG2, fg=FG, activebackground=ACCENT, font=("Segoe UI", 9))
        fm.add_command(label=T("add_txt"), command=self.add_file)
        fm.add_command(label=T("add_commands_as_button"), command=self.add_manual)
        fm.add_separator()
        fm.add_command(label=T("focus_auto"), command=self._auto_focus)
        fm.add_command(label=T("focus_window"), command=lambda: FocusSelector(self.root, self._set_target))
        fm.add_separator()
        fm.add_command(label=T("start_editor"), command=self._start_editor)
        fm.add_separator()
        fm.add_command(label=T("exit"), command=self.root.quit)
        mb.add_cascade(label=T("file"), menu=fm)

        tm = tk.Menu(mb, tearoff=0, bg=BG2, fg=FG, activebackground=ACCENT, font=("Segoe UI", 9))
        tm.add_command(label=T("map_converter"), command=self._open_converter)
        mb.add_cascade(label=T("tools"), menu=tm)

        mb.add_command(label=T("settings"), command=lambda: SettingsWindow(self.root, self))
        mb.add_command(label=T("commands"), command=lambda: CommandListWindow(self.root, self))

        hm = tk.Menu(mb, tearoff=0, bg=BG2, fg=FG, activebackground=ACCENT, font=("Segoe UI", 9))
        hm.add_command(label=T("guide"), command=self._help)
        hm.add_command(label=T("about_title"),
                      command=lambda: messagebox.showinfo(T("about_title"), T("about_text"), parent=self.root))
        mb.add_cascade(label=T("help_menu"), menu=hm)

        self.root.config(menu=mb)

    # ---- UI ----

    def _build_ui(self):
        # Focus bar
        ff = tk.Frame(self.root, bg=BG3)
        ff.pack(fill=tk.X, padx=5, pady=(5, 2))
        tk.Label(ff, text=T("focus_label"), font=("Segoe UI", 8, "bold"),
                bg=BG3, fg=FG).pack(side=tk.LEFT, padx=(5, 2))
        self.focus_lbl = tk.Label(ff, text="--", font=("Segoe UI", 8), bg=BG3, fg=GRAY, anchor="w")
        self.focus_lbl.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.update_focus_label()
        tk.Button(ff, text="...", font=("Segoe UI", 8), bg=BG3, fg=FG, bd=0, padx=4,
                 cursor="hand2", command=lambda: FocusSelector(self.root, self._set_target)
                 ).pack(side=tk.RIGHT, padx=2)

        # Last map label
        if self.last_map.get():
            mf = tk.Frame(self.root, bg=BG)
            mf.pack(fill=tk.X, padx=5)
            tk.Label(mf, text=f"{T('last_map')} {self.last_map.get()}",
                    font=("Segoe UI", 7), bg=BG, fg="#666").pack(anchor="w", padx=5)

        # Add button
        hf = tk.Frame(self.root, bg=BG)
        hf.pack(fill=tk.X, padx=5, pady=2)
        tk.Button(hf, text=T("add_btn"), font=("Segoe UI", 9, "bold"), bg=ACCENT, fg=FG,
                 bd=0, padx=12, pady=3, activebackground="#c73650", cursor="hand2",
                 command=self.add_file).pack(fill=tk.X)

        tk.Frame(self.root, height=1, bg=ACCENT).pack(fill=tk.X, padx=5, pady=3)

        # Status + stop
        sf = tk.Frame(self.root, bg=BG)
        sf.pack(fill=tk.X, padx=5)
        self.status = tk.StringVar(value=T("ready"))
        tk.Label(sf, textvariable=self.status, font=("Segoe UI", 8), bg=BG, fg=GREEN
                ).pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.stop_btn = tk.Button(sf, text="STOP", font=("Segoe UI", 8, "bold"),
                                  bg="#c73650", fg=FG, bd=0, padx=8, pady=1,
                                  cursor="hand2", command=self._stop)

        # Button scroll area
        bc = tk.Frame(self.root, bg=BG)
        bc.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        self.canvas = tk.Canvas(bc, bg=BG, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(bc, orient="vertical", command=self.canvas.yview)
        self.btn_frame = tk.Frame(self.canvas, bg=BG)
        self.btn_frame.bind("<Configure>", lambda e: (
            self.canvas.configure(scrollregion=self.canvas.bbox("all")), self._resize()))
        self.cw_id = self.canvas.create_window((0, 0), window=self.btn_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.cw_id, width=e.width))
        self.canvas.bind_all("<MouseWheel>",
                             lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

    def _resize(self):
        self.root.update_idletasks()
        max_h = int(self.root.winfo_screenheight() * 0.6)
        need = 140 + self.btn_frame.winfo_reqheight()
        h = max(min(need, max_h), 150)
        if need > max_h:
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        else:
            self.scrollbar.pack_forget()
        self.root.geometry(f"300x{h}")
        self.root.minsize(250, 150)

    def update_focus_label(self):
        if self.focus_mode.get() == "auto":
            w = find_window_by_keyword(self.auto_keyword.get())
            if w:
                d = w.title[:30] + "..." if len(w.title) > 30 else w.title
                self.focus_lbl.config(text=f"[Auto] {d}", fg=GREEN)
                self.target_window.set(w.title)
                self._parse_map(w.title)
            else:
                self.focus_lbl.config(text="[Auto] --", fg=WARN)
        else:
            t = self.target_window.get()
            if t:
                d = t[:30] + "..." if len(t) > 30 else t
                self.focus_lbl.config(text=d, fg=GREEN)
            else:
                self.focus_lbl.config(text=T("no_focus"), fg=GRAY)

    def _set_target(self, title):
        self.target_window.set(title)
        self.focus_mode.set("manual")
        self.update_focus_label()
        self.save_config()

    def _auto_focus(self):
        w = find_window_by_keyword(self.auto_keyword.get())
        if w:
            self.target_window.set(w.title)
            self.focus_mode.set("auto")
            self._parse_map(w.title)
            self.update_focus_label()
            self.save_config()
        else:
            self.status.set(T("auto_not_found"))

    def _start_editor(self):
        p = self.editor_path.get()
        if p and os.path.exists(p):
            subprocess.Popen([p], cwd=os.path.dirname(p))
            self.status.set("Editor started!")
        else:
            self.status.set("Set editor path in Settings!")

    def _open_converter(self):
        MapConverterWindow(self.root, self)

    def _help(self):
        hw = tk.Toplevel(self.root)
        hw.title(T("guide"))
        hw.attributes("-topmost", True)
        hw.configure(bg=BG)
        hw.geometry("420x480")
        t = tk.Text(hw, font=("Consolas", 9), bg=BG2, fg=FG, wrap=tk.WORD, padx=15, pady=15)
        t.insert("1.0", T("help_text"))
        t.config(state=tk.DISABLED)
        t.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # ---- CONFIG ----

    def load_config(self):
        try:
            if not os.path.exists(CONFIG_FILE):
                return
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                d = json.load(f)
            self.button_entries = d.get("buttons", [])
            self.delay_ms.set(d.get("delay_ms", 30))
            self.console_key.set(d.get("console_key", "c"))
            self.close_console.set(d.get("close_console", True))
            self.always_on_top.set(d.get("always_on_top", True))
            self.target_window.set(d.get("target_window", ""))
            self.lang.set(d.get("lang", "en"))
            self.focus_mode.set(d.get("focus_mode", "auto"))
            self.auto_keyword.set(d.get("auto_keyword", "TwoWorlds Editor"))
            self.console_keyword.set(d.get("console_keyword", "Console"))
            self.editor_path.set(d.get("editor_path", ""))
            self.last_map.set(d.get("last_map", ""))
            self.mc_sdk_path.set(d.get("mc_sdk_path", ""))
            self.mc_game_path.set(d.get("mc_game_path", ""))
            self.mc_saves_path.set(d.get("mc_saves_path", ""))
            self.mc_wd_file.set(d.get("mc_wd_file", ""))
            self.mc_repacker.set(d.get("mc_repacker", ""))
            # Migrate old
            if not self.button_entries and "files" in d:
                for fp in d["files"]:
                    fn = os.path.splitext(os.path.basename(fp))[0]
                    self.button_entries.append({"name": fn, "commands": [], "source": "file", "filepath": fp})
        except Exception:
            self.button_entries = []

    def save_config(self):
        try:
            d = {
                "buttons": self.button_entries,
                "delay_ms": self.delay_ms.get(),
                "console_key": self.console_key.get(),
                "close_console": self.close_console.get(),
                "always_on_top": self.always_on_top.get(),
                "target_window": self.target_window.get(),
                "lang": self.lang.get(),
                "focus_mode": self.focus_mode.get(),
                "auto_keyword": self.auto_keyword.get(),
                "console_keyword": self.console_keyword.get(),
                "editor_path": self.editor_path.get(),
                "last_map": self.last_map.get(),
                "mc_sdk_path": self.mc_sdk_path.get(),
                "mc_game_path": self.mc_game_path.get(),
                "mc_saves_path": self.mc_saves_path.get(),
                "mc_wd_file": self.mc_wd_file.get(),
                "mc_repacker": self.mc_repacker.get(),
            }
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(d, f, indent=2)
        except Exception:
            pass

    # ---- BUTTONS ----

    def add_file(self):
        fp = filedialog.askopenfilename(title=T("add_txt"),
                                         filetypes=[("Text", "*.txt"), ("All", "*.*")])
        if not fp:
            return
        for e in self.button_entries:
            if e.get("filepath") == fp:
                return
        fn = os.path.splitext(os.path.basename(fp))[0]
        entry = {"name": fn, "commands": [], "source": "file", "filepath": fp}
        self.button_entries.append(entry)
        self.save_config()
        self._create_btn(entry)

    def add_manual(self):
        d = tk.Toplevel(self.root)
        d.title(T("add_commands_as_button"))
        d.attributes("-topmost", True)
        d.configure(bg=BG)
        d.geometry("400x350")
        d.grab_set()
        tk.Label(d, text=T("enter_btn_name"), font=("Segoe UI", 10), bg=BG, fg=FG).pack(padx=10, pady=(10, 2), anchor="w")
        nv = tk.StringVar(value="Custom")
        tk.Entry(d, textvariable=nv, font=("Segoe UI", 10), bg=BG2, fg=FG,
                insertbackground=FG).pack(fill=tk.X, padx=10, pady=(0, 5))
        tk.Label(d, text="Commands (one per line):", font=("Segoe UI", 10), bg=BG, fg=FG).pack(padx=10, anchor="w")
        txt = tk.Text(d, font=("Consolas", 9), bg=BG2, fg=FG, insertbackground=FG, height=12)
        txt.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        def go():
            n = nv.get().strip()
            cmds = [l.strip() for l in txt.get("1.0", tk.END).splitlines() if l.strip()]
            if n and cmds:
                self.add_inline_button(n, cmds)
                d.destroy()
        tk.Button(d, text=T("add_as_button"), font=("Segoe UI", 10), bg=ACCENT, fg=FG,
                 bd=0, padx=15, pady=6, cursor="hand2", command=go).pack(pady=10)

    def add_inline_button(self, name, commands):
        entry = {"name": name, "commands": list(commands), "source": "inline"}
        self.button_entries.append(entry)
        self.save_config()
        self._create_btn(entry)

    def _get_commands(self, entry):
        if entry["source"] == "file":
            try:
                with open(entry.get("filepath", ""), "r", encoding="utf-8") as f:
                    return [l.strip() for l in f if l.strip()]
            except Exception:
                return []
        return entry.get("commands", [])

    def _create_btn(self, entry):
        cnt = len(self._get_commands(entry))
        row = tk.Frame(self.btn_frame, bg=BG)
        row.pack(fill=tk.X, pady=2)
        btn = tk.Button(row, text=f"\u25B6 {entry['name']}  ({cnt})",
                       font=("Segoe UI", 9), bg=BG2, fg=FG, bd=0, padx=10, pady=5,
                       anchor="w", activebackground=BG3, cursor="hand2",
                       command=lambda e=entry: self.execute(e))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

        def ctx(event, e=entry, r=row, b=btn):
            m = tk.Menu(self.root, tearoff=0, bg=BG2, fg=FG, activebackground=ACCENT, font=("Segoe UI", 9))
            m.add_command(label=T("expand"), command=lambda: ExpandWindow(self.root, self, e))
            m.add_separator()
            m.add_command(label=T("rename"), command=lambda: self._rename(e, b))
            m.add_command(label=T("remove"), command=lambda: self._remove(e, r))
            m.post(event.x_root, event.y_root)

        btn.bind("<Button-3>", ctx)
        self.button_widgets.append((row, entry, btn))

    def refresh_buttons(self):
        for row, entry, btn in self.button_widgets:
            cnt = len(self._get_commands(entry))
            btn.config(text=f"\u25B6 {entry['name']}  ({cnt})")

    def _rename(self, entry, btn):
        n = simpledialog.askstring(T("rename"), T("enter_name"),
                                    initialvalue=entry["name"], parent=self.root)
        if n:
            entry["name"] = n
            cnt = len(self._get_commands(entry))
            btn.config(text=f"\u25B6 {n}  ({cnt})")
            self.save_config()

    def _remove(self, entry, frame):
        frame.destroy()
        if entry in self.button_entries:
            self.button_entries.remove(entry)
        self.button_widgets = [(f, e, b) for f, e, b in self.button_widgets if e is not entry]
        self.save_config()

    # ---- EXECUTION ----

    def _find_editor(self):
        import pygetwindow as gw
        if self.focus_mode.get() == "auto":
            w = find_window_by_keyword(self.auto_keyword.get())
            if w:
                self.target_window.set(w.title)
                self._parse_map(w.title)
            return w
        t = self.target_window.get()
        if t:
            ws = gw.getWindowsWithTitle(t)
            return ws[0] if ws else None
        return None

    def _stop(self):
        self.stop_requested = True
        self.status.set("Stopping...")

    def _console_focused(self):
        try:
            import pygetwindow as gw
            a = gw.getActiveWindow()
            return a and a.title and self.console_keyword.get().lower() in a.title.lower()
        except Exception:
            return False

    def execute_single_command(self, cmd):
        threading.Thread(target=self._inject, args=([cmd],), daemon=True).start()

    def execute(self, entry):
        if self.running:
            self.status.set(T("running"))
            return
        cmds = self._get_commands(entry)
        if not cmds:
            self.status.set(T("file_empty"))
            return
        threading.Thread(target=self._inject, args=(cmds,), daemon=True).start()

    def _inject(self, commands):
        self.running = True
        self.stop_requested = False
        self.stop_btn.pack(side=tk.RIGHT, padx=(4, 0))
        delay = self.delay_ms.get() / 1000.0
        ck = self.console_key.get()
        total = len(commands)

        try:
            self.status.set(T("focusing"))
            time.sleep(0.15)

            ew = self._find_editor()
            if not ew:
                self.status.set(T("auto_not_found") if self.focus_mode.get() == "auto" else T("no_target"))
                return

            try:
                if ew.isMinimized:
                    ew.restore()
                ew.activate()
                time.sleep(0.25)
            except Exception as e:
                self.status.set(f"{T('focus_error')} {e}")
                return

            self.status.set(T("opening_console"))
            pyautogui.press(ck)
            time.sleep(0.4)

            cw = find_window_by_keyword(self.console_keyword.get())
            if cw:
                try:
                    cw.activate()
                    time.sleep(0.15)
                except Exception:
                    pass
            else:
                self.status.set("Console not found!")
                return

            for i, cmd in enumerate(commands):
                if self.stop_requested:
                    self.status.set(f"Stopped {i}/{total}")
                    break
                if not self._console_focused():
                    self.status.set(f"Focus lost! {i}/{total}")
                    break
                self.status.set(f"[{i+1}/{total}] {cmd[:28]}...")
                clipboard_paste(self.root, cmd)
                time.sleep(delay)
                pyautogui.press("enter")
                time.sleep(delay)
            else:
                if self.close_console.get():
                    time.sleep(0.1)
                    pyautogui.press("escape")
                self.status.set(f"{total} {T('executed')}")

        except pyautogui.FailSafeException:
            self.status.set(T("aborted"))
        except Exception as e:
            self.status.set(f"{T('error')} {e}")
        finally:
            self.running = False
            self.stop_requested = False
            self.stop_btn.pack_forget()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
