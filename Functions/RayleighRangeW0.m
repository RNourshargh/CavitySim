function [ zr ] = RayleighRangeW0( w0, lambda )
%This calculates the Rayleigh range from a beam waist and wavelength.
%If no wavelength is given it is asumed to be 780nm
%All units are in metres
switch nargin
        case 2
            L = lambda;
        case 1
            L=780E-9;
        otherwise
            disp('Error incorrect number of variables')
end
zr = pi* w0^2/L; 

end

