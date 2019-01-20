function [ q2 ] = ABCDtransform( ABCD, q1 )
%% This applies the ABCD transform to the input complex beam radius and returns the output

A = ABCD(1,1);
B = ABCD(1,2);
C = ABCD(2,1);
D = ABCD(2,2);

q2 = (A*q1 + B)/(C*q1 +D);
end

