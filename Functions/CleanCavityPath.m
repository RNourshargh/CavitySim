function [] = CleanCavityPath()
%CleanCavityPath removes the cavity path locations from the search path.
%CavityPath.txt should be updated on a new system
%These locations can be reinstalled by running InitialiseCavityPath()

%Make an array containing the cavity path locations
NewPathsArray = ReadCavPathFile();

%Find the size of this array = number of locations to remove
L = size(NewPathsArray,1);

%Remove these locations from the path
for i = 1:L
    rmpath(NewPathsArray(i))
   
end
end

