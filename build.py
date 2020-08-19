# $fontforge -lang=py -script WWQ.py

import fontforge as ff
import shutil

font="FRBTaiwaneseKana"

f = ff.open(font+".sfd")
f.mergeFeature("features.fea")
f.selection.all()
f.unlinkReferences()
f.removeOverlap()
f.generate(font+".otf", flags=("opentype", "no-hints", "omit-instructions"))
f.close()
