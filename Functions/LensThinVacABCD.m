function [ABCD,OPL] = LensThinVacABCD(LensFile)
%LensThinABCD Imports a lens file and outputs ABCD matrix with the
%thin lens approximation and additional optical path length OPL. It is only
%valid under the thin lens approximation in a vacuum
%Inputs: LensFile.csv
%Outputs: ABCD (matrix), OPL (Optical Path length added by the component)

%Imports the second row of the LensFile to an array M
LensProperties = csvread(LensFile,1,0);

%reads the focal length in metres from the LensProperties file
f = LensProperties(1)

%Calculate the ABCD matrix from the lens properties
ABCD = [1 , 0; -1/f , 1]

%OPL is 0 for a thin lens
OPL = 0
end

