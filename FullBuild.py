import subprocess
import ue4paths
import projectParser


def start_proc(args):
    proc = subprocess.Popen(args)
    code = proc.wait()
    if code != 0:
        print(code)
        exit(1)


project = projectParser.BuildProjectInfo()
platform_name = '-platform=' + project.platform()
configuration_name = '-configuration=' + project.configuration()

uproject = '-project=' + project.uproject()
cook_args = [ue4paths.ubt(), uproject, '-projectfiles', '-game', 'progress']
start_proc(cook_args)

platform_name_verb = '/p:Platform=' + project.platform()
configuration_name_verb = '/p:Configuration=' + project.configuration()
compile_args = [ue4paths.MSVC, project.solution(), r'/t:build', configuration_name_verb, platform_name_verb]
start_proc(compile_args)


targetplatform = '-targetplatform=' + project.platform()
cook_args = [ue4paths.uat(), 'BuildCookRun', uproject, '-noP4', '-cook', '-allmaps', '-build',
             '-stage', '-pak', '-archive', platform_name, configuration_name, targetplatform]
if project.buildPath() is not None:
    build = '-archivedirectory=' + project.buildPath()
    cook_args.append(build)

if project.platform() == 'Android':
    cook_args.append('-cookflavor=' + project.cookflavor())
start_proc(cook_args)
