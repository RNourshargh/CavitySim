function [ w ] = ABCDw( ABCD )
%ANCDw This calculates the spot size in a resonator in the plane at which
%the ABCD matrix is defined

%Recalling constant values, wavelength
[~,Lambda]=ConfigCavEnv();

A = ABCD(1,1);
B = ABCD(1,2);
C = ABCD(2,1);
D = ABCD(2,2);

m = (A+D)/2;
w = sqrt(abs(B)*Lambda/pi * sqrt(1/(1-m^2)));

fprintf('Beam radius is %f meters\n',w);

end