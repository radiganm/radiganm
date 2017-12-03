## pi.py
## Mac Radigan

import os
from collections import OrderedDict

INVARIANT_PUBLICATION = 'f379e9385edeef35627a231754162bbee863be27'

def get_content(repo):
  content = OrderedDict([])
  content['repo'] = repo
  filename = "../%s/README.md" % repo
  if os.path.isfile(filename):
    content['README'] = filename
  else:
    content['README'] = 'N/A'
  return content

def get_meta(repos):
  meta = []
  for repo in sorted(repos, key=lambda v: v.upper()):
    meta.append(get_content(repo))
  return meta

repos = sorted(os.listdir(path='..'), key=lambda v: v.upper())
metas = get_meta(repos)

apply_templates()

## *EOF*
