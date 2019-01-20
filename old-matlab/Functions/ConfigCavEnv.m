function [M,Lambda, n0] = ConfigCavEnv()
%ConfigCav Imports the ConfigCavEnv CSV and outputs an array containing
%these evironmental variables, and the individual variables.
M = csvread('ConfigCavEnv.csv',1,0);

Lambda = M(1,1);
n0 = M(1,2);
end

