function [ w ] = ABCDw( ABCD )
%ANCDw This calculates the spot size in a resonator in the plane at which
%the ABCD matrix is defined

A = ABCD(1,1);
B = ABCD(1,2);
C = ABCD(2,1);
D = ABCD(2,2);

%The wavelength of the light. This may need to be entered with higher
%precision
Lambda = 780E-9;

m = (A+D)/2;
w = sqrt(abs(B)*Lambda/pi * sqrt(1/(1-m^2)));
X = sprintf('Beam radius is %f meters',w);
disp(X)
end