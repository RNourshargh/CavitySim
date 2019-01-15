function [] = InitialiseCavityPath()
%InitialiseCavityPath Adds all of the cavity functions to the search path.
%This should be updated if run on another system.
%The initial path can be restored by running RemoveCavityPath. Check this
%location has been removed from the final path
%*******This should be rewritten to import the path from a file
oldpath = path;
oldpath=path(oldpath,'D:\OneDrive\Documents\Subject Notes\PhD\Year2\Cavity\CavityMatlab\Functions');
path(oldpath,'D:\OneDrive\Documents\Subject Notes\PhD\Year2\Cavity\CavityMatlab')
end

