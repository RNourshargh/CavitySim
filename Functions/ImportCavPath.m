function [NewPathsArray] = ImportCavPath()
%ImportCavPath imports the CavityPath.txt file to a string array output
%   Detailed explanation goes here
NewPathsArray = ImportLineSepSTR( 'CavityPath.txt');
end

