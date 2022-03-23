
function y_out = Flocking_Matlab()

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MArch 2019, Orit Peleg, orit.peleg@colorado.edu
% Code for HW3 CSCI 4314/5314 Dynamic Models in Biology
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

close all;
set(0,'Defaultlinelinewidth',5, 'DefaultlineMarkerSize',6,...
    'DefaultTextFontSize',5, 'DefaultAxesFontSize',18);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% initialize parameters
N = 200;        %No. of boids
frames = 100;   %No. of frames in movie
limit = 5;    %Axis limits
L=limit*2; 
P = 10;         %Spread of initial position (gaussian)
V = 10;         %Spread of initial velocity (gaussian)
delta = 1; %0.01;  %Time step
c1 = 0.00001;       %Attraction scaling factor
c2 = 0.01;         %Repulsion scaling factor
c3 = 1;          %Heading scaling factor
c4 = 0.00000001; %0.01;         %Randomness scaling factor
vlimit = 1;    %Maximum velocity
v_object = 1.2;
obstacle = [0 0];
x1=-1;
x2=1;
y1=-1;
y2=1;
%x = [x1, x2, x2, x1, x1];
%y = [y1, y1, y2, y2, y1];
x = 0;
y = 0;

%creating static position for obstacle
obs = [2;2];


%Initialize
p = P*randn(2,N);
v = V*randn(2,N);
figure(); 
%Main loop
for k=1:frames
    v1=zeros(2,N);
    v2=zeros(2,N);

    %velocity when object is added
    object_repulsion=zeros(2,N);
    %YOUR CODE HERE
    v3 = [sum( v ( 1 , : ) ) /N; sum( v ( 2 , : ) ) /N ]*c3;
    
    %Calculate average veolcity
    if(norm(v3) > vlimit), v3 = v3*vlimit/norm(v3); end %Limit max velocity
    for n=1:N
        for m=1:N
            if m ~= n
				%YOUR CODE HERE
				%Compute vector r from one agent to the next
                r = p ( : ,m) - p( : , n );
            

                %computing vector r_o from one agent to obstacle
                r_o = p( : ,m) - obs;
                
                
                
                if r(1)>L/2, r(1) = r(1)-L;
                elseif r(1)<-L/2, r(1) = r(1)+L;
                end
                
                if r(2)>L/2, r(2) = r(2)-L;
                elseif r(2)<-L/2, r(2) = r(2)+L;
                end

                if r_o(1)>L/2, r_o(1) = r_o(1)-L;
                elseif r_o(1)<-L/2, r_o(1) = r_o(1) +L;
                end

                if r_o(2)>L/2, r_o(2) = r_o(2)-L;
                elseif r_o(2)<-L/2, r_o(2) = r_o(2) +L;
                end

                


                
				%YOUR CODE HERE
                %Compute distance between agents rmag 
                rmag = sqrt( r(1)^2+ r(2)^2);
                r_object = sqrt( r_o(1)^2+ r_o(2)^2);
                %Compute Attraction v1
                v1( : , n ) = v1 ( : , n ) + c1*r ;
                %Compute repulsion (non-linear scaling) v2
                v2 ( : , n ) = v2 ( : , n ) - c2 *r / ( rmag ^2 ) ;
             
                %computing repuslion for obstacle
                object_repulsion(: ,n) = object_repulsion(: ,n) -c2*r_o /(r_object ^ 2);

            end
        end
        %YOUR CODE HERE
        %Compute random velocity component v4
        %Update velocity
        v4(:,n) = c4*randn(2,1);
        v( : , n ) = v1 ( : , n)+v2 ( : , n) + v3+v4( : , n );
    end
    %YOUR CODE HERE
    %Update position
    p( : , n) = p ( : , n ) + v( : , n )* delta ;
    % Periodic boundary 
    tmp_p = p;
    
    tmp_p(1,p(1,:)>L/2) = tmp_p(1,p(1,:)>L/2) - L;
    tmp_p(2,p(2,:)>L/2) = tmp_p(2,p(2,:)>L/2) - L;
    tmp_p(1,p(1,:)<-L/2)  = tmp_p(1,p(1,:)<-L/2) + L;
    tmp_p(2,p(2,:)<-L/2)  = tmp_p(2,p(2,:)<-L/2) + L;
   
    
    p = tmp_p;
    %Update plot:
    plot(p(1,:),p(2,:),'k+','Markersize',4); 
    quiver(p(1,:),p(2,:),v(1,:),v(2,:)); %For drawing velocity arrows
    axis([-limit-limit/2 limit+limit/2 -limit-limit/2 limit+limit/2]); axis square; 
    hold on
    %plot(x, y, 'b', 'LineWidth', 3);
    %plot(2,2, 'O')
    %hold on;
    %plot(2*obstacle(1), obstacle(1),'ro','MarkerSize' ,5);
    drawnow; 
    hold off;
    pause(0.1);
end
y_out=0; 


end




