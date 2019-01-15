function [ zr ] = RayleighRangeW0(w0)
%This calculates the Rayleigh range from the beam waist using the
%ConfigCavEnv value for wavelength
%All units are in metres

[~,Lambda,~]=ConfigCavEnv();

zr = pi* w0^2/Lambda;
end

