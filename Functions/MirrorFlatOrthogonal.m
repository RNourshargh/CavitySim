function [ABCD,OPL] = MirrorFlatOrthogonal()
%% MirrorFlatOrthogonal Generates ABCD matrix and OPL for a flat mirror
%The mirror must be orthogonal to the input beam dirrection.
%Inputs: None
%Outputs: ABCD-matrix, OPL - Optical Path Length

ABCD = [1 , 0; 0 , 1];
OPL = 0; %Planar mirrors contribute no additional optical path length
end