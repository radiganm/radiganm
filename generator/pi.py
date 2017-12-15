## pi.py
## Mac Radigan

import os
from collections import OrderedDict
import re

INVARIANT_PUBLICATION = 'f379e9385edeef35627a231754162bbee863be27'

def parse_org(filename):
  tags = OrderedDict([])
  with open(filename) as f: org = f.read()
  p = r"#\+([A-Za-z0-9\-]*):[ ]*([A-Za-z0-9.,:'/ \(\)ń\-\?\=]*)"
  ms = re.findall(p, org)
  if ms is not None: 
    for m in ms:
      tags[m[0]] = m[1]
  return tags

def get_content(repo):
  content = OrderedDict([])
  content['repo'] = repo
  ## GH Markdown File
  filename = "../%s/README.md" % repo
  if os.path.isfile(filename):
    content['README'] = filename
  else:
    content['README'] = None
  ## Org-Mode File
  filename = "../%s/README.org" % repo
  if os.path.isfile(filename):
    content['tags'] = parse_org(filename)
  else:
    content['tags'] = None
  ##
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
