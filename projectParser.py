import argparse
from os import path
from enum import Enum


class BuildProjectInfo:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-projectPath', type=str, dest='projectPath')
        parser.add_argument('-projectName', type=str, dest='projectName')
        parser.add_argument('-buildPath', type=str, dest='buildPath')
        parser.add_argument('-configuration', type=int, dest='configuration')
        parser.add_argument('-platform', type=str, dest='platform')
        self.args = parser.parse_args()
        self.checkAttr('projectPath')
        self.checkAttr('projectName')

    def checkAttr(self, atrname):
        if hasattr(self, atrname):
            print('Need attribute -' + atrname)
            exit(1)

    def solution(self):
        return path.join(self.args.projectPath, self.args.projectName) + '_' + self.platform().name + '.sln'

    def uproject(self):
        return path.join(self.args.projectPath, self.args.projectName) + '.uproject'

    def buildPath(self):
        if self.args.buildPath is None:
            return r'C:\Builds'
        return self.args.buildPath

    def platform(self):
        if self.args.platform is None:
            return Platform.Win64
        if self.args.platform == 'Android':
            return Platform.Android
        elif self.args.platform == 'Win64':
            return Platform.Win64

    def configuration(self):
        if self.args.configuration is None:
            return Configuration.Shipping
        return Configuration(self.args.configuration)


class Platform(Enum):
    Win64 = 0
    Android = 1


class Configuration(Enum):
    DebugGame = 0
    Development = 1
    Shipping = 2
