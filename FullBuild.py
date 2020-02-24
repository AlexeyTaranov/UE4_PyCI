import subprocess
import ue4paths
import projectParser


def checkCode(code):
    if code != 0:
        print(code)
        exit()


def start_proc(args):
    proc = subprocess.Popen(args)
    code = proc.wait()
    checkCode(code)


project = projectParser.BuildProjectInfo()

uproject = '-project=' + projectParser.BuildProjectInfo().uproject()
build_args = [ue4paths.ubt(), uproject, '-projectfiles', '-game', '-rocket', 'progress']
start_proc(build_args)

compile_args = [ue4paths.MSVC, project.solution(), r'/t:build', '/p:Platform=Win64;verbosity=diagnostic']
start_proc(compile_args)

build = '-archivedirectory=' + project.buildPath()
build_args = [ue4paths.uat(), 'BuildCookRun', uproject, '-noP4', '-platform=Win64', '-clientconfig=Development',
              '-cook', '-allmaps', '-build', '-stage', '-pak', '-archive', build]
start_proc(build_args)
build_proc = subprocess.Popen(build_args)

cook_args = [ue4paths.uat(), 'BuildCookRun', uproject, '-noP4', '-platform=Win64', '-clientconfig=Development',
             '-cook', '-allmaps', '-NoCompile', '-stage', '-pak', '-archive', build]
start_proc(cook_args)
