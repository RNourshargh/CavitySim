function [ABCD,OPL] = PathFreeSpace(PathLength)
%% PathFreeSpace Generates the ABCD matrix and OPL for free space propagation
% Inputs: PathLength (in metres)
% Outputs: ABCD matrix, OPL - Optical Path Length
% Notes: The refractive index of the medium n0 is set im the ConfigCavEnv.csv
% file and by default is 1. The ray starts and ends in this medium.
% Refraction must be handled seperately

%% Import refractive index of free space of media from Config file
[~,~, n0] = ConfigCavEnv();
%% Compute Outputs
ABCD = [1, PathLength; 0, 1];
OPL = PathLength*n0;
end

