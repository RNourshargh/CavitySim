function [M] = ConfigCavEnv()
%ConfigCav Imports the ConfigCavENv CSV and outputs an array containing
%these evironmental variables, and the individual variables.
M = csvread('ConfigCavEnv.csv',1,0);

%Lambda = M(1,1)
%Test = M(1,2)
end

