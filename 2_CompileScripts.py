import subprocess
import ue4paths
import projectBuildInfo

project = projectBuildInfo.BuildProjectInfo()
args = [ue4paths.MSVC, project.solution(), r'/t:build', '/p:Platform=Win64;verbosity=diagnostic']
subprocess.run(args)
