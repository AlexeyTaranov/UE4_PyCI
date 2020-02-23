import subprocess
import ue4paths
import projectBuildInfo

project = '-project=' + projectBuildInfo.BuildProjectInfo().uproject()
args = [ue4paths.ubt(), project, '-projectfiles', '-game', '-rocket', 'progress']
subprocess.run(args)
