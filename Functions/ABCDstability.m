function [ AD ] = ABCDstability( ABCD)
%This function calculates and returns the stability parameter (ABCD trace).
%The result is printed to the terminal in words.

AD = trace(ABCD);

if(AD<2) && (AD>-2)
    disp('Cavity is stable')
    fprintf('A+D = %f \n', AD);
    
elseif (AD>2) || (AD<-2) 
    disp('Cavity is Unstable')
    fprintf('A+D = %f \n', AD);
    
else 
    disp('error not a valid transfer matrix')

end

