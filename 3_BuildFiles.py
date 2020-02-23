import subprocess
import ue4paths
import projectBuildInfo

project = projectBuildInfo.BuildProjectInfo()
uproject = '-project=' + project.uproject()
build = r'-archivedirectory=' + project.buildPath()
args = [ue4paths.uat(), 'BuildCookRun', uproject, '-noP4', '-platform=Win64', '-clientconfig=Development',
        '-cook', '-allmaps', '-build', '-stage', '-pak', '-archive', build]
subprocess.run(args)
