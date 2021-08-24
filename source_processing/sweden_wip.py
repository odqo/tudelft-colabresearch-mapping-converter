import re

from project import Project
from project_address import ProjectAddress


def process_se_wip(data, source_name):
  '''Process list of wip projects from Sweden
  '''
  print('Processing Sweden (wip projects)...')
  projects = []

  for ip in data:
    project = Project(ip[2], source_name)
    project.address = ProjectAddress('Sweden', 'SE')
    project.address.region = ip[1]
    project.development_stage = 'developing'

    projects.append(project)

  print(f'Processed: {len(projects)} projects\n')
  return projects
