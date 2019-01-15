function [] = InitialiseCavityPath()
%InitialiseCavityPath Adds all of the cavity functions to the search path.
%CavityPath.txt should be updated on a new system
%These locations can be removed by running CleanCavityPath()

%Make an array containing the new locations
NewPathsArray = ReadCavPathFile();

%Find the size of this array = number of new locations to add
L = size(NewPathsArray,1);

%Add these locations to the path
for i = 1:L
    addpath(NewPathsArray(i),'-end')
    
end
end

