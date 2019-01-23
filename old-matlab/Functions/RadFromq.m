function [ w ] = RadFromq( q )
%RadFromq calculates the beam radius from the complex radius of curvature
%at the point where the radius of curvature is defined

[~,Lambda,~]=ConfigCavEnv();

w = sqrt(-Lambda/(pi* Imag(1/q)));
end

