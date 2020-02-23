import argparse
from os import path


class BuildProjectInfo:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-projectPath', type=str, dest='projectPath')
        parser.add_argument('-projectName', type=str, dest='name')
        parser.add_argument('-buildPath', type=str, dest='buildPath')
        parser.add_argument('-buildType', type=str, dest='type')
        parser.add_argument('-platform', type=str, dest='platform')
        self.args = parser.parse_args()

    def solution(self):
        return path.join(self.args.projectPath, self.args.name) + '.sln'

    def uproject(self):
        return path.join(self.args.projectPath, self.args.name) + '.uproject'

    def buildPath(self):
        return self.args.buildPath
