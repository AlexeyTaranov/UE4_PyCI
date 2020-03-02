import argparse
from os import path
from enum import Enum


class BuildProjectInfo:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-projectPath', type=str, dest='projectPath')
        parser.add_argument('-projectName', type=str, dest='projectName')
        parser.add_argument('-buildPath', type=str, dest='buildPath')
        parser.add_argument('-configuration', type=str, dest='configuration')
        parser.add_argument('-platform', type=str, dest='platform')
        parser.add_argument('-cookflavor', type=str, dest='cookflavor')
        self.args = parser.parse_args()

    def checkAttr(self, atrname):
        if hasattr(self, atrname):
            print('Need attribute -' + atrname)
            exit(1)

    def projectPath(self):
        return self.args.projectPath

    def solution(self):
        return path.join(self.args.projectPath, self.args.projectName) + '.sln'

    def uproject(self):
        return path.join(self.args.projectPath, self.args.projectName) + '.uproject'

    def buildPath(self):
        return self.args.buildPath

    def platform(self):
        if self.args.platform is None:
            return 'Win64'
        platformList = ['Win64', 'Android']
        if self.args.platform in platformList:
            return self.args.platform
        else:
            return 'Win64'

    def configuration(self):
        if self.args.configuration is None:
            return 'Development'
        configurationList = ['DebugGame', 'Development', 'Shipping']
        if self.args.configuration in configurationList:
            return self.args.configuration
        else:
            return 'Development'

    def cookflavor(self):
        if self.args.cookflavor is None:
            return 'Multi'
        cookList = ['ATC', 'DXT', 'ETC1', 'ETC1a', 'ETC2', 'PVRTC', 'ASTC', 'Multi']
        if self.args.cookflavor in cookList:
            return self.args.cookflavor
        else:
            return 'Multi'
