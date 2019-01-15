function [ ROC ] = ABCDroc( ABCD )
%This funntion calculates the radius of curvature (in metres) of the fundamental
%gausian mode of a cavity in the loacation at which the
%ABCD matrix is evaluated. i.e. the intial plane.
A = ABCD(1,1);
B = ABCD(1,2);
C = ABCD(2,1);
D = ABCD(2,2);

ROC = 2*B/(D-A);

X = sprintf('The beam radius of curvature is %f metres',ROC);
disp(X)

end

