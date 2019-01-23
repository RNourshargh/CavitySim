function [StringArray] = ImportLineSepSTR( FileLocation )
%ImportLineSepSTR Imports a line seperated string to an array of strings
fid = fopen(FileLocation);
StringCellArray = textscan(fid, '%s','delimiter','\r');
StringArray = string(StringCellArray{1});
end