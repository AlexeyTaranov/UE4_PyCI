# UE4_PyCI
Python scripts for build in CI UE4 projects

It's simple python scripts for building UE4 projects with CI as Jenkins.


#### Requirements:
##### 1. Python 3.x
##### 2. Unreal Engine 4
##### 3. Visual Studio 
##### 4. CI (Jenkins for this Example) (additional)


#### Steps:
##### 1. Setup your CI with Unreal Engine Project.
##### 2. Set Paths in ue4paths.py
##### 3. Configure args for run script in CI


-projectPath=* Absolute Path to project*

-projectName= *Yeah, it's project name (projectName.uproject)*

-buildPath= *Absolute path to builds*

-configuration = *DebugGame , Development, Shipping*

-platform= *Win64, Android*

Example from Jenkins: call C:\Python\Python38\python.exe 
D:\UE4_PyCI\FullBuild.py -projectName="Interaction" -projectPath="%WORKSPACE%" 
-buildPath="%WORKSPACE%\Builds" -platform="Android" -configuration=Development

Build and Enjoy!
